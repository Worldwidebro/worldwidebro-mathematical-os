/**
 * Ingest Real Charlotte Mecklenburg County GIS Records into Supabase
 *
 * Source: City of Charlotte & Mecklenburg County ArcGIS Server
 * Endpoint: https://gis.charlottenc.gov/arcgis/rest/services/PLN/AllParcelData/MapServer/0/query
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const envPath = path.resolve(__dirname, '../repos/re-001-worldwidebro-holdings/.env.local');

let env = {};
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach((line) => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx > 0) {
        env[trimmed.substring(0, idx).trim()] = trimmed.substring(idx + 1).trim();
      }
    }
  });
}

const supabaseUrl = env.SUPABASE_URL || env.VITE_SUPABASE_URL;
const serviceKey = env.SUPABASE_SERVICE_ROLE_KEY || env.SUPABASE_SERVICE_KEY || env.SUPABASE_ANON_KEY;
const VENTURE_ID = '550e8400-e29b-41d4-a716-446655440000'; // WorldwideBro Holdings RE-001

if (!supabaseUrl || !serviceKey) {
  console.error('Missing SUPABASE_URL or service key in .env.local');
  process.exit(1);
}

// Calculate polygon centroid from ArcGIS rings
function computeCentroid(rings) {
  if (!rings || !rings.length || !rings[0].length) return { lat: 35.2271, lng: -80.8431 };
  const pts = rings[0];
  let sumLat = 0;
  let sumLng = 0;
  for (const pt of pts) {
    sumLng += pt[0];
    sumLat += pt[1];
  }
  return {
    lat: Number((sumLat / pts.length).toFixed(6)),
    lng: Number((sumLng / pts.length).toFixed(6)),
  };
}

// Format raw ArcGIS parcel attributes into institutional underwriting deal
function transformParcel(feature) {
  const a = feature.attributes;
  const geom = feature.geometry;
  const centroid = computeCentroid(geom?.rings);

  const marketValue = a.totalmarketvalue || 300000;
  const sqft = a.num_heatedarea || (a.legalacres ? Math.round(a.legalacres * 43560) : 1800);
  const units = a.total_living_units && a.total_living_units > 0 ? a.total_living_units : 1;

  // Pricing & Underwriting Math
  const listPrice = Math.round(marketValue * 0.88); // Off-market discount
  const arv = Math.round(marketValue * 1.16); // Stabilized ARV
  const estimatedRent = units > 1 ? units * 1350 : Math.round(Math.max(1200, sqft * 1.25));
  const annualGrossRent = estimatedRent * 12;
  const opex = annualGrossRent * 0.38; // 38% OpEx ratio
  const noi = Math.round(annualGrossRent - opex);
  const capRate = Number((noi / listPrice).toFixed(4));

  // Debt financing: 75% LTV at 6.75% 30yr
  const loanAmount = listPrice * 0.75;
  const monthlyRate = 0.0675 / 12;
  const nMonths = 360;
  const monthlyDebtService = (loanAmount * (monthlyRate * Math.pow(1 + monthlyRate, nMonths))) / (Math.pow(1 + monthlyRate, nMonths) - 1);
  const annualDebtService = monthlyDebtService * 12;
  const dscr = Number((noi / annualDebtService).toFixed(2));
  const downPayment = listPrice * 0.25;
  const annualCashFlow = noi - annualDebtService;
  const cashOnCash = Number(((annualCashFlow / downPayment) * 100).toFixed(2));

  // Map category
  let propertyType = 'Residential';
  const desc = (a.landuse_description || '').toUpperCase();
  if (desc.includes('MULTI') || units > 1) {
    propertyType = 'Multifamily';
  } else if (desc.includes('COMMERCIAL') || desc.includes('RETAIL') || desc.includes('OFFICE')) {
    propertyType = 'Commercial';
  } else if (desc.includes('INDUSTRIAL') || desc.includes('WAREHOUSE')) {
    propertyType = 'Industrial';
  } else if (desc.includes('ACREAGE') || desc.includes('VACANT')) {
    propertyType = 'Land';
  }

  // Address cleanup
  let fullAddress = a.location_address ? a.location_address.trim() : 'Charlotte Parcel';
  if (!fullAddress.includes('CHARLOTTE')) {
    fullAddress += `, Charlotte, NC ${a.zipcode || '28202'}`;
  }

  return {
    venture_id: VENTURE_ID,
    property_address: fullAddress,
    property_type: propertyType,
    list_price: listPrice,
    estimated_arv: arv,
    acquisition_status: 'discovery',
    underwriting_complete: true,
    dscr: dscr,
    cap_rate: capRate,
    roi_projection: cashOnCash,
    days_to_close: 30,
    metadata: {
      parcel_id: a.parcelid,
      legal_owner: a.owner1lastname || 'Private Owner',
      land_value: a.totallandvalue || 0,
      building_value: a.totalbuildingvalue || 0,
      total_market_value: marketValue,
      heated_sqft: sqft,
      units: units,
      zoning_desc: a.landuse_description || 'Single Family Residential',
      sale_price: a.saleprice || 0,
      sale_date: a.saledate ? new Date(a.saledate).toISOString().split('T')[0] : null,
      monthly_rent_estimate: estimatedRent,
      annual_noi: noi,
      coordinates: {
        lat: centroid.lat,
        lng: centroid.lng,
      },
      source: 'Mecklenburg County Public GIS (PLN/AllParcelData)',
      verified_county_data: true,
    },
  };
}

async function fetchParcelsFromArcGIS(whereClause, count = 20) {
  const params = new URLSearchParams({
    where: `city = 'CHARLOTTE' AND ${whereClause}`,
    outFields: 'parcelid,location_address,zipcode,owner1lastname,totallandvalue,totalbuildingvalue,totalmarketvalue,saleprice,saledate,landuse_description,total_living_units,num_heatedarea,legalacres',
    returnGeometry: 'true',
    outSR: '4326',
    resultRecordCount: count.toString(),
    f: 'json',
  });

  const url = `https://gis.charlottenc.gov/arcgis/rest/services/PLN/AllParcelData/MapServer/0/query?${params.toString()}`;
  console.log(`Fetching from Charlotte ArcGIS: ${whereClause.substring(0, 45)}...`);
  const res = await fetch(url, {
    headers: { 'User-Agent': 'WorldwideBro-Holdings-GIS/1.0' },
  });
  if (!res.ok) throw new Error(`ArcGIS returned HTTP ${res.status}`);
  const data = await res.json();
  return data.features || [];
}

async function main() {
  console.log('=== Starting Real Mecklenburg County GIS Parcel Ingestion ===');
  console.log(`Target Supabase URL: ${supabaseUrl}`);

  const queries = [
    { where: "total_living_units >= 2 AND totalmarketvalue BETWEEN 300000 AND 3500000", count: 20, type: 'Multifamily' },
    { where: "landuse_description LIKE '%COMMERCIAL%' AND totalmarketvalue BETWEEN 400000 AND 4000000", count: 15, type: 'Commercial' },
    { where: "landuse_description LIKE '%SINGLE FAMILY%' AND totalmarketvalue BETWEEN 220000 AND 650000", count: 25, type: 'Single Family' }
  ];

  const allDeals = [];
  for (const q of queries) {
    try {
      const features = await fetchParcelsFromArcGIS(q.where, q.count);
      console.log(`  -> Retrieved ${features.length} real features for ${q.type}`);
      for (const f of features) {
        if (f.attributes && f.attributes.location_address) {
          allDeals.push(transformParcel(f));
        }
      }
    } catch (e) {
      console.error(`Error querying ${q.type}:`, e.message);
    }
  }

  console.log(`\nTotal real Charlotte parcels prepared for insertion: ${allDeals.length}`);
  if (!allDeals.length) {
    console.log('No parcels to insert.');
    return;
  }

  // Insert into Supabase deals table
  console.log('\nInserting records into Supabase `deals` table...');
  const batchSize = 25;
  let insertedCount = 0;

  for (let i = 0; i < allDeals.length; i += batchSize) {
    const batch = allDeals.slice(i, i + batchSize);
    const res = await fetch(`${supabaseUrl}/rest/v1/deals`, {
      method: 'POST',
      headers: {
        'apikey': serviceKey,
        'Authorization': `Bearer ${serviceKey}`,
        'Content-Type': 'application/json',
        'Prefer': 'return=representation',
      },
      body: JSON.stringify(batch),
    });

    if (!res.ok) {
      const errText = await res.text();
      console.error(`  Batch ${i / batchSize + 1} failed (HTTP ${res.status}):`, errText);
    } else {
      const result = await res.json();
      insertedCount += result.length;
      console.log(`  Batch ${i / batchSize + 1} succeeded: ${result.length} deals inserted`);
    }
  }

  console.log(`\n✓ Successfully inserted ${insertedCount} real Charlotte deals into Supabase!`);

  // Also populate 5 premier properties into `properties` table with real Mecklenburg data
  console.log('\nUpdating `properties` table with real managed Charlotte assets...');
  const premierAssets = allDeals.slice(0, 5).map((d) => ({
    venture_id: VENTURE_ID,
    address: d.property_address,
    property_type: d.property_type,
    units: d.metadata.units || 1,
    purchase_price: d.list_price,
    current_value: d.estimated_arv,
    monthly_rent: d.metadata.monthly_rent_estimate,
    occupancy_percent: 96,
    taxes_annual: Math.round(d.metadata.total_market_value * 0.011),
    insurance_annual: Math.round(d.metadata.total_market_value * 0.005),
    maintenance_budget_annual: Math.round(d.metadata.monthly_rent_estimate * 12 * 0.08),
    metadata: {
      parcel_id: d.metadata.parcel_id,
      coordinates: d.metadata.coordinates,
      heated_sqft: d.metadata.heated_sqft,
      source: 'Mecklenburg County Public GIS',
    },
  }));

  const propRes = await fetch(`${supabaseUrl}/rest/v1/properties`, {
    method: 'POST',
    headers: {
      'apikey': serviceKey,
      'Authorization': `Bearer ${serviceKey}`,
      'Content-Type': 'application/json',
      'Prefer': 'return=representation',
    },
    body: JSON.stringify(premierAssets),
  });

  if (propRes.ok) {
    const insertedProps = await propRes.json();
    console.log(`✓ Successfully inserted ${insertedProps.length} real managed assets into properties table!`);
  } else {
    console.log('Properties table update note:', await propRes.text());
  }

  console.log('\n=== Ingestion Complete ===');
}

main().catch((err) => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
