# 2022 NAICS Official Taxonomy Package — OPS-001

This directory contains the canonical, fully normalized 2022 North American Industry Classification System (NAICS) taxonomy extracted directly from the official U.S. Census Bureau structure file.

## Manifest of Files

| File | Format | Description |
| :--- | :--- | :--- |
| [`naics-2022.csv`](./naics-2022.csv) | CSV | Flat normalized 2–6 digit hierarchy with parent codes and sector mappings (2,125 rows) |
| [`naics-2022.json`](./naics-2022.json) | JSON | Machine-readable array of all 2,125 entities with full metadata |
| [`naics-2022.yaml`](./naics-2022.yaml) | YAML | High-density ontology registry for OPS-001 systems and Company Brain |
| [`NAICS-2022.md`](./NAICS-2022.md) | Markdown | Human-readable documentation, sector summaries, and 2022 change analysis |
| [`hierarchy.json`](./hierarchy.json) | JSON | Recursive parent/child tree and graph edges for Neo4j / UI visualization |
| [`sources.md`](./sources.md) | Markdown | Census provenance, publication citations, SHA-256 hash, and change keys |
| [`2022_NAICS_Structure.xlsx`](./2022_NAICS_Structure.xlsx) | Binary | Pristine original Excel workbook downloaded from Census.gov |

## Data Schema

```typescript
interface NAICSRecord {
  code: string;              // e.g. '11', '31-33', '111110'
  title: string;             // Clean English title
  title_raw: string;         // Official title with 'T' indicator
  level: 'Sector' | 'Subsector' | 'Industry Group' | 'NAICS Industry' | 'National Industry';
  level_digits: number;      // 2, 3, 4, 5, or 6
  change_indicator: '*' | '**' | '***' | '****' | null;
  change_description: string;
  trilateral: boolean;       // Agreement between US, Canada, Mexico
  parent_code: string | null;// Direct ancestor code
  sector_code: string;       // Top-level sector (e.g. '11', '31-33')
  sector_title: string;      // Top-level sector title
}
```
