/**
 * Seed 50 US States Cadastral Registry into PostgreSQL / Supabase
 * RE-001 Worldwidebro Group — Task RE-021
 *
 * Source: _REGISTRIES/CANONICAL/50_STATE_REAL_ESTATE_DATA_REGISTRY.csv
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const csvPath = path.resolve(__dirname, '../_REGISTRIES/CANONICAL/50_STATE_REAL_ESTATE_DATA_REGISTRY.csv');
const sqlOutPath = path.resolve(__dirname, '../repos/re-001-worldwidebro-holdings/supabase/seed_50_states.sql');

if (!fs.existsSync(csvPath)) {
  console.error(`Registry CSV not found at: ${csvPath}`);
  process.exit(1);
}

// Simple RFC4180-compliant CSV line parser
function parseCSVLine(line) {
  const result = [];
  let start = 0;
  let inQuotes = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (c === '"') {
      inQuotes = !inQuotes;
    } else if (c === ',' && !inQuotes) {
      let field = line.substring(start, i).trim();
      if (field.startsWith('"') && field.endsWith('"')) {
        field = field.slice(1, -1).replace(/""/g, '"');
      }
      result.push(field);
      start = i + 1;
    }
  }
  let field = line.substring(start).trim();
  if (field.startsWith('"') && field.endsWith('"')) {
    field = field.slice(1, -1).replace(/""/g, '"');
  }
  result.push(field);
  return result;
}

const fileContent = fs.readFileSync(csvPath, 'utf8');
const lines = fileContent.split('\n').map((l) => l.trim()).filter(Boolean);
const headers = parseCSVLine(lines[0]);

const rows = [];
for (let i = 1; i < lines.length; i++) {
  const values = parseCSVLine(lines[i]);
  if (values.length >= 6) {
    const row = {};
    headers.forEach((h, idx) => {
      row[h] = values[idx] || '';
    });
    rows.push(row);
  }
}

console.log(`Parsed ${rows.length} jurisdictions from 50_STATE_REAL_ESTATE_DATA_REGISTRY.csv`);

// Generate idempotent SQL inserts
const sqlStatements = [
  '-- ============================================================================',
  '-- Seed Data: 50 US States + Federal Data Layer for RE-001 Real Estate Intelligence',
  '-- Target Table: `states`',
  '-- ============================================================================',
  '',
];

for (const r of rows) {
  const stateCode = r.state_code;
  const stateName = r.state_name.replace(/'/g, "''");
  const fipsCode = r.fips_code;
  const geoUnit = (r.primary_geo_unit || 'Counties').replace(/'/g, "''");
  const countyCount = parseInt(r.county_count, 10) || 0;
  const dominantAssessor = (r.dominant_assessor_system || '').replace(/'/g, "''");
  const dominantDeed = (r.dominant_deed_system || '').replace(/'/g, "''");
  const statewideGis = (r.statewide_gis_portal || '').replace(/'/g, "''");
  const metadata = JSON.stringify({
    core_records_ingested: r.core_records_ingested,
    update_frequency: r.update_frequency,
    ingestion_method: r.ingestion_method,
    auth_requirement: r.auth_requirement,
    licensing_terms: r.licensing_terms,
  }).replace(/'/g, "''");

  sqlStatements.push(`
INSERT INTO states (state_code, state_name, fips_code, primary_geo_unit, county_count, dominant_assessor_system, dominant_deed_system, statewide_gis_portal, metadata)
VALUES ('${stateCode}', '${stateName}', '${fipsCode}', '${geoUnit}', ${countyCount}, '${dominantAssessor}', '${dominantDeed}', '${statewideGis}', '${metadata}'::jsonb)
ON CONFLICT (state_code) DO UPDATE SET
  state_name = EXCLUDED.state_name,
  fips_code = EXCLUDED.fips_code,
  primary_geo_unit = EXCLUDED.primary_geo_unit,
  county_count = EXCLUDED.county_count,
  dominant_assessor_system = EXCLUDED.dominant_assessor_system,
  dominant_deed_system = EXCLUDED.dominant_deed_system,
  statewide_gis_portal = EXCLUDED.statewide_gis_portal,
  metadata = EXCLUDED.metadata,
  updated_at = NOW();
  `.trim());
}

fs.writeFileSync(sqlOutPath, sqlStatements.join('\n\n'), 'utf8');
console.log(`✓ Successfully generated idempotent SQL migration for ${rows.length} jurisdictions: ${sqlOutPath}`);
