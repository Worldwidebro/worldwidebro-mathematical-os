# AI Estimating Service

**Port:** 8006  
**Purpose:** Auto-estimate job costs in 3 seconds  
**Input:** Trade type, location, hours, materials  
**Output:** Labor cost, material cost, total, platform profit

## Endpoint

```bash
POST /mcp/tools/estimate_job

{
  "trade": "drywall",
  "location": "charlotte",
  "hours": 40,
  "materials": {"drywall_sheets": 50, "tape": 10}
}
```

## Response

```json
{
  "labor_cost": 3230,
  "material_cost": 1890,
  "total_estimate": 5120,
  "platform_profit": 614,
  "confidence": 0.82
}
```

This integrates into the CON OS deal intake pipeline to auto-populate estimates.
