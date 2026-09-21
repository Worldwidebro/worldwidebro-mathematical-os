{{
    config(
        materialized='table',
        tags=['marts', 'capabilities'],
        description='Capability coverage analysis by venture, sector, and readiness stage'
    )
}}

with ventures as (
    select * from {{ ref('stg_supabase_ventures') }}
),

capabilities as (
    select * from {{ ref('stg_supabase_capabilities') }}
),

metrics as (
    select * from {{ ref('stg_supabase_metrics') }}
),

venture_capabilities as (
    select
        v.venture_id,
        v.name as venture_name,
        v.sector,
        v.status as venture_status,
        c.capability_id,
        c.name as capability_name,
        c.category as capability_category,
        coalesce(m.readiness_pct, 0.0) as readiness_pct
    from ventures v
    cross join capabilities c
    left join metrics m on v.venture_id = m.venture_id
)

select
    sector,
    capability_category,
    capability_name,
    count(distinct venture_id) as total_ventures_evaluated,
    count(distinct case when readiness_pct >= 0.7 then venture_id end) as ventures_covered_count,
    round(
        cast(count(distinct case when readiness_pct >= 0.7 then venture_id end) as numeric) / 
        nullif(count(distinct venture_id), 0) * 100, 
        2
    ) as coverage_pct,
    count(distinct case when readiness_pct < 0.7 then venture_id end) as gap_count,
    current_timestamp as calculated_at
from venture_capabilities
group by sector, capability_category, capability_name
order by sector, coverage_pct asc
