const path = require('path');
module.paths.push(path.resolve(__dirname, '../../services/api/node_modules'));

const axios = require('axios');
const { spawn } = require('child_process');

const BASE_URL = 'http://localhost:4005/api';

async function runTests() {
  console.log('=== STARTING DISPATCHOS INTEGRATION TESTS ===');
  
  // 1. Verify Health
  try {
    const res = await axios.get(`${BASE_URL}/health`);
    console.log('✅ Health check pass:', res.data);
  } catch (err) {
    console.error('❌ Health check fail:', err.message);
    process.exit(1);
  }

  let activeLoadId = 'mock-load-uuid-10482';
  let activeTenderId = 'mock-tender-uuid-8821';

  // 2. Submit Order
  try {
    const res = await axios.post(`${BASE_URL}/orders`, {
      reference_number: `REF-${Date.now()}`,
      origin: { address: '100 Main St, Charlotte, NC', lat: 35.227085, lng: -80.843124 },
      destination: { address: '200 Peach St, Atlanta, GA', lat: 33.748995, lng: -84.387982 },
      weight_lbs: 42000.00
    });
    activeLoadId = res.data.load.id;
    console.log('✅ Order intake pass. Load created:', activeLoadId);
  } catch (err) {
    console.error('❌ Order intake fail:', err.message);
    process.exit(1);
  }

  // 3. Dispatch Tender
  try {
    const res = await axios.post(`${BASE_URL}/tenders`, {
      load_id: activeLoadId,
      carrier_id: 'carrier-uuid-9921',
      offer_price_usd: 1250.00
    });
    activeTenderId = res.data.tender.id;
    console.log('✅ Tender created pass. Tender ID:', activeTenderId);
  } catch (err) {
    console.error('❌ Tender creation fail:', err.message);
    process.exit(1);
  }

  // 4. Accept Tender
  try {
    const res = await axios.post(`${BASE_URL}/tenders/${activeTenderId}/accept`, {
      driver_id: 'driver-uuid-4412',
      vehicle_id: 'vehicle-uuid-5521'
    });
    console.log('✅ Tender accept pass. Status:', res.data.tender.status);
  } catch (err) {
    console.error('❌ Tender accept fail:', err.message);
    process.exit(1);
  }

  // 5. Update GPS Telemetry
  try {
    const res = await axios.post(`${BASE_URL}/tracking/gps`, {
      driver_id: 'driver-uuid-4412',
      vehicle_id: 'vehicle-uuid-5521',
      latitude: 34.052234,
      longitude: -81.034834,
      speed_mph: 62.5
    });
    console.log('✅ GPS telemetry ingestion pass:', res.data.telemetry);
  } catch (err) {
    console.error('❌ GPS telemetry fail:', err.message);
    process.exit(1);
  }

  // 6. Upload POD Document
  try {
    const res = await axios.post(`${BASE_URL}/documents/upload`, {
      load_id: activeLoadId,
      doc_type: 'POD',
      file_url: 'https://storage.dispatch.os/pod/10482_signed.pdf'
    });
    console.log('✅ POD document upload & OCR pass:', res.data.document.ocr_extracted_text);
  } catch (err) {
    console.error('❌ POD upload fail:', err.message);
    process.exit(1);
  }

  // 7. Calculate Settlement
  try {
    const res = await axios.post(`${BASE_URL}/settlement/${activeLoadId}`, {
      carrier_cost_usd: 850.00,
      driver_pay_usd: 300.00,
      fuel_usd: 120.00,
      tolls_usd: 15.00
    });
    console.log('✅ Settlement gross profit calculation pass:', res.data.settlement);
  } catch (err) {
    console.error('❌ Settlement calculation fail:', err.message);
    process.exit(1);
  }

  console.log('=== ALL DISPATCHOS TESTS PASSED SUCCESSFULLY ===');
  process.exit(0);
}

// Spin up API server in background
const serverPath = path.resolve(__dirname, '../../services/api/src/server.ts');
const tsNodePath = path.resolve(__dirname, '../../services/api/node_modules/.bin/ts-node');

console.log('Booting API server...');
const server = spawn(tsNodePath, [serverPath], {
  env: { ...process.env, PORT: '4005' },
  stdio: 'inherit'
});

// Wait 3 seconds for server to bind port, then execute tests
setTimeout(() => {
  runTests().then(() => {
    server.kill();
  }).catch((err) => {
    console.error(err);
    server.kill();
    process.exit(1);
  });
}, 3000);
