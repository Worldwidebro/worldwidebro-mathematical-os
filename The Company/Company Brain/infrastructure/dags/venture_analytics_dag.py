from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.models import Variable
from airflow.utils.task_group import TaskGroup

default_args = {
    'owner': 'data-engineering',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email': ['data-alerts@worldwidebro.com'],
}

dag = DAG(
    'venture_analytics_pipeline',
    default_args=default_args,
    description='Daily venture analytics: Fivetran → dbt → Great Expectations',
    schedule_interval='0 1 * * *',  # Run at 1 AM UTC daily
    catchup=False,
    tags=['analytics', 'ventures', 'daily'],
)

# Task 1: Trigger Fivetran sync
trigger_fivetran = SimpleHttpOperator(
    task_id='trigger_fivetran_sync',
    http_conn_id='fivetran_api',
    endpoint='/v1/teams/{{ var.value.fivetran_team_id }}/connectors',
    method='PATCH',
    data={
        'pause': False,
    },
    dag=dag,
)

# Task 2: Wait for Fivetran to complete
wait_for_fivetran = BashOperator(
    task_id='wait_for_fivetran',
    bash_command="""
        python << EOF
        import requests
        import time

        api_url = '{{ var.value.fivetran_api_url }}'
        api_token = '{{ var.value.fivetran_api_token }}'

        connector_id = '{{ var.value.fivetran_connector_id }}'
        max_wait = 3600  # 1 hour max
        poll_interval = 60  # Check every 60 seconds

        start_time = time.time()
        while time.time() - start_time < max_wait:
            response = requests.get(
                f'{api_url}/v1/connectors/{connector_id}',
                headers={'Authorization': f'Bearer {api_token}'}
            )
            status = response.json()['data']['sync_state']['lifecycle_state']

            if status == 'IDLE':
                print("Fivetran sync complete")
                exit(0)

            time.sleep(poll_interval)

        raise Exception("Fivetran sync timeout")
        EOF
    """,
    dag=dag,
)

# Task 3-5: dbt execution (with task group for organization)
with TaskGroup('dbt_execution') as dbt_group:
    dbt_seed = BashOperator(
        task_id='dbt_seed',
        bash_command='cd /opt/analytics && dbt seed --profiles-dir . --target dev',
    )

    dbt_staging = BashOperator(
        task_id='dbt_staging_models',
        bash_command='cd /opt/analytics && dbt run --profiles-dir . --target dev --select staging',
    )

    dbt_marts = BashOperator(
        task_id='dbt_marts',
        bash_command='cd /opt/analytics && dbt run --profiles-dir . --target dev --select marts',
    )

    dbt_test = BashOperator(
        task_id='dbt_tests',
        bash_command='cd /opt/analytics && dbt test --profiles-dir . --target dev',
    )

    dbt_seed >> dbt_staging >> dbt_marts >> dbt_test

# Task 6: Great Expectations validation
validate_data_quality = BashOperator(
    task_id='validate_data_quality',
    bash_command="""
        cd /opt/analytics && python << EOF
        from great_expectations.data_context import DataContext

        context = DataContext('/opt/analytics/great_expectations')
        checkpoint = context.get_checkpoint('ventures_daily_validation')

        result = checkpoint.run()
        if not result.success:
            raise Exception("Data quality validation failed")

        print("Data quality checks passed")
        EOF
    """,
    dag=dag,
)

# Task 7: Update documentation (dbt docs)
update_docs = BashOperator(
    task_id='update_dbt_docs',
    bash_command='cd /opt/analytics && dbt docs generate --profiles-dir . --target dev',
    dag=dag,
)

# Define task dependencies
trigger_fivetran >> wait_for_fivetran >> dbt_group >> validate_data_quality >> update_docs

# SLA: All tasks must complete within 4 hours
dag.default_view = 'graph'
dag.sla_miss_callback = None  # Add Slack notification if needed
