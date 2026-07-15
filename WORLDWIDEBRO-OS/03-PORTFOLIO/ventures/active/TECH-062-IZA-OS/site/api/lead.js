const VENTURE_ID = 'TECH-062-IZA-OS';

function splitName(name) {
  const parts = (name || '').trim().split(/\s+/).filter(Boolean);
  if (parts.length === 0) return { first_name: null, last_name: null };
  const [first, ...rest] = parts;
  return { first_name: first, last_name: rest.join(' ') || null };
}

// Best-effort notifications. Failures here never block the lead from being saved —
// they're logged and swallowed so a notification outage can't lose a customer lead.
async function notifySlack(lead) {
  const webhookUrl = process.env.SLACK_WEBHOOK_URL;
  if (!webhookUrl) return;
  const lines = [
    `*New IZA OS lead* (${lead.source})`,
    `*${lead.first_name || ''} ${lead.last_name || ''}*`.trim() + (lead.company_name ? ` — ${lead.company_name}` : ''),
    lead.email,
    lead.industry ? `Industry: ${lead.industry}` : null,
    lead.stage && lead.stage !== 'new' ? `Recommended plan: ${lead.stage} (score ${lead.lead_score})` : null,
    lead.fit_notes ? `Message: ${lead.fit_notes}` : null,
  ].filter(Boolean);
  try {
    await fetch(webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: lines.join('\n') }),
    });
  } catch (err) {
    console.error('Slack notify failed', err);
  }
}

async function notifyEmail(lead) {
  const apiKey = process.env.RESEND_API_KEY;
  const toAddress = process.env.LEAD_NOTIFY_EMAIL;
  if (!apiKey || !toAddress) return;
  const html = `
    <p><strong>New IZA OS lead</strong> (${lead.source})</p>
    <p>${lead.first_name || ''} ${lead.last_name || ''} — ${lead.company_name || 'No company given'}</p>
    <p>Email: ${lead.email}${lead.phone ? ' · Phone: ' + lead.phone : ''}</p>
    ${lead.industry ? `<p>Industry: ${lead.industry}</p>` : ''}
    ${lead.stage && lead.stage !== 'new' ? `<p>Recommended plan: ${lead.stage} (score ${lead.lead_score})</p>` : ''}
    ${lead.fit_notes ? `<p>Message: ${lead.fit_notes}</p>` : ''}
  `;
  try {
    await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: process.env.LEAD_NOTIFY_FROM || 'IZA OS Leads <leads@resend.dev>',
        to: [toAddress],
        subject: `New lead: ${lead.company_name || lead.email}`,
        html,
      }),
    });
  } catch (err) {
    console.error('Resend notify failed', err);
  }
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }

  const body = req.body || {};
  const { source, name, company, email, phone, industry, message, quizAnswers, recommendation } = body;

  if (!email || typeof email !== 'string' || !email.includes('@')) {
    res.status(400).json({ error: 'A valid email is required.' });
    return;
  }

  const supabaseUrl = process.env.SUPABASE_URL;
  const supabaseKey = process.env.SUPABASE_SERVICE_KEY;
  if (!supabaseUrl || !supabaseKey) {
    console.error('Missing SUPABASE_URL or SUPABASE_SERVICE_KEY env vars');
    res.status(500).json({ error: 'Server misconfigured. Please email us directly.' });
    return;
  }

  const { first_name, last_name } = splitName(name);

  const payload = {
    venture_id: VENTURE_ID,
    email,
    first_name,
    last_name,
    company_name: company || null,
    industry: industry || null,
    phone: phone || null,
    source: source || 'website',
    source_url: req.headers.referer || req.headers.referrer || null,
    stage: (recommendation && recommendation.plan) || 'new',
    status: 'new',
    lead_score: recommendation && typeof recommendation.score === 'number' ? recommendation.score : null,
    fit_notes: message || null,
    enrichment_data: { quizAnswers: quizAnswers || null, message: message || null },
  };

  try {
    const resp = await fetch(`${supabaseUrl}/rest/v1/venture_leads`, {
      method: 'POST',
      headers: {
        apikey: supabaseKey,
        Authorization: `Bearer ${supabaseKey}`,
        'Content-Type': 'application/json',
        Prefer: 'return=minimal',
      },
      body: JSON.stringify(payload),
    });

    if (!resp.ok) {
      const errText = await resp.text();
      console.error('Supabase insert failed', resp.status, errText);
      res.status(502).json({ error: 'Failed to save your request. Please try again.' });
      return;
    }

    // Fire-and-forget: don't let a slow/broken notification channel delay the response.
    Promise.allSettled([notifySlack(payload), notifyEmail(payload)]).catch(() => {});

    res.status(200).json({ ok: true });
  } catch (err) {
    console.error('lead.js error', err);
    res.status(500).json({ error: 'Server error. Please try again.' });
  }
};
