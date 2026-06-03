// Webhook Handler: Call Completion
// Receives call outcomes from VAPI and logs to ClickUp + Supabase

const { createClient } = require('@supabase/supabase-js');
const axios = require('axios');

const supabaseUrl = process.env.SUPABASE_URL;
const supabaseKey = process.env.SUPABASE_KEY;
const clickupToken = process.env.CLICKUP_TOKEN;

const supabase = createClient(supabaseUrl, supabaseKey);

const AGENT_PHONE_MAP = {
  '+1-XXX-ECOM-001': 'e-commerce',
  '+1-XXX-TECH-001': 'technology',
  '+1-XXX-BW-001': 'beauty-wellness'
};

async function handleCallComplete(req, res) {
  const {
    phoneNumber,
    prospectNumber,
    transcription,
    duration,
    outcome,
    transcript_url
  } = req.body;

  try {
    const agentType = AGENT_PHONE_MAP[phoneNumber] || 'unknown';

    // 1. Log call to Supabase
    const { data: callData, error: callError } = await supabase
      .from('ai_calls')
      .insert({
        prospect_phone: prospectNumber,
        agent_phone: phoneNumber,
        agent_type: agentType,
        transcript: transcription,
        transcript_url: transcript_url,
        call_duration: duration,
        outcome: outcome,
        warmth_score: extractWarmthScore(transcription),
        created_at: new Date()
      });

    if (callError) throw new Error(`Supabase insert failed: ${callError.message}`);

    // 2. Create/Update ClickUp task if interesting
    if (['interested', 'demo_booked', 'callback'].includes(outcome)) {
      const clickupListId = getClickUpListId(agentType);

      const taskPayload = {
        name: `[${outcome.toUpperCase()}] ${prospectNumber} - ${agentType}`,
        status: outcome === 'demo_booked' ? 'In Progress' : 'To Do',
        description: `Call transcript: ${transcript_url || 'See Supabase'}\n\nDuration: ${duration}s\nOutcome: ${outcome}`,
        custom_fields: [
          { id: 'warmth_score', value: extractWarmthScore(transcription) },
          { id: 'outcome_type', value: outcome },
          { id: 'call_duration', value: duration },
          { id: 'agent_type', value: agentType },
          { id: 'contact_phone', value: prospectNumber }
        ]
      };

      const { data: task } = await axios.post(
        `https://api.clickup.com/api/v2/list/${clickupListId}/task`,
        taskPayload,
        {
          headers: {
            Authorization: clickupToken,
            'Content-Type': 'application/json'
          }
        }
      );

      // 3. If demo booked, create calendar event
      if (outcome === 'demo_booked') {
        const demoDate = extractDemoDate(transcription);
        if (demoDate) {
          await createCalendarEvent({
            title: `[DEMO] ${prospectNumber} (${agentType})`,
            description: `AI Call Demo\nAgent: ${agentType}\nTranscript: ${transcript_url}`,
            startTime: new Date(demoDate),
            duration: 30,
            contactPhone: prospectNumber
          });
        }
      }

      res.status(200).json({
        success: true,
        message: 'Call logged and ClickUp task created',
        task_id: task.id
      });
    } else {
      // Log but don't create task for negative outcomes
      res.status(200).json({
        success: true,
        message: 'Call logged (not interested)',
        outcome: outcome
      });
    }

  } catch (error) {
    console.error('Webhook error:', error);
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
}

function extractWarmthScore(transcript) {
  // Simple scoring: presence of key positive phrases
  const positivePatterns = [
    'interested',
    'definitely',
    'absolutely',
    'love to see',
    'perfect',
    'exactly what',
    'demo sounds good',
    'when can we',
    'looking for something'
  ];

  const matches = positivePatterns.filter(pattern =>
    transcript?.toLowerCase().includes(pattern)
  ).length;

  // Base: 1 point per positive pattern, cap at 10
  return Math.min(3 + matches, 10);
}

function extractDemoDate(transcript) {
  // Extract demo date from transcript
  // Patterns: "Tuesday at 2pm", "Wednesday morning", "next Thursday"
  const datePatterns = [
    /(?:this\s+)?(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\s+(?:at\s+)?(\d{1,2}(?::?\d{2})?\s*(?:am|pm)?)/gi,
    /(?:next\s+)?(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\s+(?:at\s+)?(\d{1,2}(?::?\d{2})?\s*(?:am|pm)?)/gi
  ];

  for (const pattern of datePatterns) {
    const match = pattern.exec(transcript);
    if (match) {
      // Return ISO string (in production, calculate actual date)
      // For MVP, return next occurrence of matched day
      return new Date(); // Placeholder
    }
  }

  return null;
}

function getClickUpListId(agentType) {
  const listMap = {
    'e-commerce': process.env.CLICKUP_LIST_ECOM,
    'technology': process.env.CLICKUP_LIST_TECH,
    'beauty-wellness': process.env.CLICKUP_LIST_BEAUTY
  };
  return listMap[agentType];
}

async function createCalendarEvent(event) {
  // Integration with Google Calendar API
  // Requires: google.auth.OAuth2, googleapis library
  // For MVP: Log intent to create
  console.log('Calendar event to create:', event);
  // TODO: Wire to Google Calendar API
}

module.exports = { handleCallComplete };
