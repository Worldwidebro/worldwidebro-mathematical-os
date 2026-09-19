{{
    config(
        materialized='incremental',
        unique_id='metric_id',
        on_schema_change='fail',
        tags=['supabase', 'staging'],
        description='Venture metrics: readiness %, revenue, expenses'
    )
}}

with source_data as (
    select
        id as metric_id,
        venture_id,
        readiness_pct,
        monthly_revenue,
        monthly_expenses,
        cash_balance,
        team_headcount,
        last_updated,
        now() as _extracted_at
    from {{ source('supabase', 'venture_metrics') }}
),

deduplicated as (
    select
        metric_id,
        venture_id,
        readiness_pct,
        monthly_revenue,
        monthly_expenses,
        cash_balance,
        team_headcount,
        last_updated,
        _extracted_at,
        row_number() over (partition by venture_id order by last_updated desc) as rn
    from source_data
)

select * from deduplicated
where rn = 1

{% if execute %}
    {% if execute %}
        {% if var('should_full_refresh', false) == false and this.exists %}
            and last_updated > (select max(last_updated) from {{ this }})
        {% endif %}
    {% endif %}
{% endif %}
