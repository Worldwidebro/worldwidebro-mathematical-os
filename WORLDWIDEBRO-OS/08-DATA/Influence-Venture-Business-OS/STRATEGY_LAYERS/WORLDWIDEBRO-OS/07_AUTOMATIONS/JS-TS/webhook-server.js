// Webhook Server: VAPI Call Outcome Handler
// Starts Express server to receive call completion events from VAPI
// Logs to Supabase + Creates ClickUp tasks + Schedules demos

require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const { handleCallComplete } = require('./webhook-call-complete');

const app = express();
app.use(bodyParser.json());

// Middleware: Log all incoming requests
app.use((req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
  if (req.method === 'POST') {
    console.log('Body:', JSON.stringify(req.body).substring(0, 500));
  }
  next();
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    environment: {
      supabase: !!process.env.SUPABASE_URL,
      clickup: !!process.env.CLICKUP_TOKEN
    }
  });
});

// VAPI Webhook: Call Complete
app.post('/webhook/call-complete', handleCallComplete);

// VAPI Webhook: Transcript Ready
app.post('/webhook/transcript', (req, res) => {
  console.log('Transcript received:', req.body);
  // Store full transcript if needed
  res.status(200).json({ success: true });
});

// Error handler
app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(500).json({
    success: false,
    error: err.message
  });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`
╔════════════════════════════════════════╗
║   VAPI Call Webhook Server Started     ║
╠════════════════════════════════════════╣
║ Port: ${PORT}
║ Health: http://localhost:${PORT}/health
║ Webhook: http://localhost:${PORT}/webhook/call-complete
║ Status: Listening for VAPI events
╚════════════════════════════════════════╝
  `);
});

// Graceful shutdown
process.on('SIGINT', () => {
  console.log('\nShutting down gracefully...');
  process.exit(0);
});
