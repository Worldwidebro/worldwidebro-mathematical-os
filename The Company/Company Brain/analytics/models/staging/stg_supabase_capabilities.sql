{{
    config(
        materialized='incremental',
        unique_id='capability_id',
        on_schema_change='fail',
        tags=['supabase', 'staging'],
        description='Capabilities mapped to ventures'
    )
}}

with source_data as (
    select
        id as capability_id,
        name,
        description,
        category,
        status,
        created_at,
        updated_at,
        now() as _extracted_at,
        row_number() over (partition by id order by updated_at desc) as rn
    from {{ source('supabase', 'capabilities') }}
),

deduped as (
    select
        capability_id,
        name,
        description,
        category,
        status,
        created_at,
        updated_at,
        _extracted_at
    from source_data
    where rn = 1
)

select * from deduped

{% if execute %}
    {% if execute %}
        {% if var('should_full_refresh', false) == false and this.exists %}
            and updated_at > (select max(updated_at) from {{ this }})
        {% endif %}
    {% endif %}
{% endif %}
