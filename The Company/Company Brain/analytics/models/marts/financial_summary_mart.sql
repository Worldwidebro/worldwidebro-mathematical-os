{{
    config(
        materialized='table',
        tags=['marts', 'financial'],
        description='Financial summary: revenue, expenses, margin by venture and month'
    )
}}

with metrics as (
    select
        venture_id,
        monthly_revenue,
        monthly_expenses,
        cash_balance,
        last_updated,
        date_trunc('month', last_updated)::date as metric_month
    from {{ ref('stg_supabase_metrics') }}
),

ventureInfo as (
    select
        venture_id,
        name as venture_name,
        sector
    from {{ ref('stg_supabase_ventures') }}
),

aggregated as (
    select
        v.venture_id,
        v.venture_name,
        v.sector,
        m.metric_month,
        sum(m.monthly_revenue) as total_revenue,
        sum(m.monthly_expenses) as total_expenses,
        sum(m.monthly_revenue) - sum(m.monthly_expenses) as net_income,
        case
            when sum(m.monthly_revenue) > 0
            then (sum(m.monthly_revenue) - sum(m.monthly_expenses)) / sum(m.monthly_revenue)
            else 0
        end as margin_pct,
        max(m.cash_balance) as ending_cash,
        count(distinct m.last_updated) as metric_count
    from metrics m
    left join ventureInfo v on m.venture_id = v.venture_id
    where m.last_updated >= date_trunc('month', current_date - interval 12 month)
    group by v.venture_id, v.venture_name, v.sector, m.metric_month
)

select * from aggregated
order by metric_month desc, total_revenue desc
