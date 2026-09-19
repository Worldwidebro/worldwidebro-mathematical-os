{{
    config(
        materialized='table',
        tags=['marts', 'ventures'],
        description='Dimensional model: venture readiness by stage, sector, status'
    )
}}

with ventures as (
    select * from {{ ref('stg_supabase_ventures') }}
),

metrics as (
    select * from {{ ref('stg_supabase_metrics') }}
),

joined as (
    select
        v.venture_id,
        v.name as venture_name,
        v.sector,
        v.status as venture_status,
        m.readiness_pct,
        m.monthly_revenue,
        m.monthly_expenses,
        m.cash_balance,
        m.team_headcount,
        case
            when m.readiness_pct >= 0.8 then 'Launch Ready'
            when m.readiness_pct >= 0.6 then 'Scaling'
            when m.readiness_pct >= 0.4 then 'Validation'
            else 'Ideation'
        end as readiness_stage,
        m.last_updated as last_metric_updated,
        v.created_at as venture_created_at
    from ventures v
    left join metrics m on v.venture_id = m.venture_id
)

select * from joined
order by readiness_pct desc
