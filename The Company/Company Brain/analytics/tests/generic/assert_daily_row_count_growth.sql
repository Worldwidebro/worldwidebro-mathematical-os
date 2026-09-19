{% test assert_daily_row_count_growth(model, threshold_count=10) %}

{#
  Fails if the daily incremental row count is below a threshold.
  Used to detect pipeline failures or missing data.
#}

with current_day as (
    select count(*) as row_count
    from {{ model }}
    where date(_extracted_at) = current_date
),

yesterday as (
    select count(*) as row_count
    from {{ model }}
    where date(_extracted_at) = current_date - interval 1 day
)

select current_day.row_count
from current_day, yesterday
where current_day.row_count < {{ threshold_count }}
  and current_day.row_count < yesterday.row_count * 0.5  {# Alert if <50% of yesterday #}

{% endtest %}
