import express from 'express';
import { supabase } from '../index';
import { Resend } from 'resend';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const router = express.Router();
const resend = new Resend(process.env.RESEND_API_KEY);

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const TEMPLATES_DIR = path.join(__dirname, '../templates');

// Load and interpolate template
function loadTemplate(templateName: string, variables: Record<string, string>): string {
  const templatePath = path.join(TEMPLATES_DIR, `${templateName}.html`);
  let html = fs.readFileSync(templatePath, 'utf-8');

  Object.entries(variables).forEach(([key, value]) => {
    html = html.replace(new RegExp(`{{${key}}}`, 'g'), value || '');
  });

  return html;
}

// Log email delivery
async function logEmailDelivery(
  template: string,
  recipient: string,
  subject: string,
  status: 'sent' | 'failed',
  error?: string
) {
  await supabase.from('email_deliveries').insert({
    template,
    recipient,
    subject,
    status,
    last_error: error,
    retry_count: 0,
  });
}

// POST /api/email/send-rent-reminder - Send rent reminder 3 days before due date
router.post('/send-rent-reminder', async (req, res) => {
  const { unitId, tenantEmail, tenantName, amount, dueDate, paymentLink } = req.body;

  try {
    const html = loadTemplate('rent-reminder', {
      amount: `$${parseFloat(amount).toFixed(2)}`,
      due_date: new Date(dueDate).toLocaleDateString(),
      payment_link: paymentLink,
    });

    const response = await resend.emails.send({
      from: process.env.RESEND_FROM_EMAIL || 'noreply@realestate-os.com',
      to: tenantEmail,
      subject: `Rent Payment Due - ${new Date(dueDate).toLocaleDateString()}`,
      html,
    });

    if (response.error) throw response.error;

    await logEmailDelivery('rent-reminder', tenantEmail, 'Rent Reminder', 'sent');
    res.json({ success: true, messageId: response.data?.id });
  } catch (err) {
    await logEmailDelivery('rent-reminder', tenantEmail, 'Rent Reminder', 'failed', String(err));
    res.status(500).json({ error: String(err) });
  }
});

// POST /api/email/send-maintenance-update - Send when maintenance status changes
router.post('/send-maintenance-update', async (req, res) => {
  const { ticketId, tenantEmail, status, notes } = req.body;

  try {
    const html = loadTemplate('maintenance-update', {
      ticket_id: ticketId,
      status: status.charAt(0).toUpperCase() + status.slice(1),
      notes: notes || 'No additional notes.',
    });

    const response = await resend.emails.send({
      from: process.env.RESEND_FROM_EMAIL || 'noreply@realestate-os.com',
      to: tenantEmail,
      subject: `Maintenance Request Update - #${ticketId}`,
      html,
    });

    if (response.error) throw response.error;

    await logEmailDelivery('maintenance-update', tenantEmail, 'Maintenance Update', 'sent');
    res.json({ success: true, messageId: response.data?.id });
  } catch (err) {
    await logEmailDelivery('maintenance-update', tenantEmail, 'Maintenance Update', 'failed', String(err));
    res.status(500).json({ error: String(err) });
  }
});

// POST /api/email/send-payment-receipt - Send immediately after payment confirmed
router.post('/send-payment-receipt', async (req, res) => {
  const { tenantEmail, amount, date, propertyName } = req.body;

  try {
    const html = loadTemplate('payment-receipt', {
      amount: `$${parseFloat(amount).toFixed(2)}`,
      date: new Date(date).toLocaleDateString(),
      property_name: propertyName,
    });

    const response = await resend.emails.send({
      from: process.env.RESEND_FROM_EMAIL || 'noreply@realestate-os.com',
      to: tenantEmail,
      subject: 'Payment Received - Receipt',
      html,
    });

    if (response.error) throw response.error;

    await logEmailDelivery('payment-receipt', tenantEmail, 'Payment Receipt', 'sent');
    res.json({ success: true, messageId: response.data?.id });
  } catch (err) {
    await logEmailDelivery('payment-receipt', tenantEmail, 'Payment Receipt', 'failed', String(err));
    res.status(500).json({ error: String(err) });
  }
});

// POST /api/email/send-escalation - Send to landlord if ticket open > 7 days
router.post('/send-escalation', async (req, res) => {
  const { landlordEmail, daysOpen, ticketDescription, portalLink } = req.body;

  try {
    const html = loadTemplate('maintenance-escalation', {
      days_open: String(daysOpen),
      ticket_description: ticketDescription,
      portal_link: portalLink,
    });

    const response = await resend.emails.send({
      from: process.env.RESEND_FROM_EMAIL || 'noreply@realestate-os.com',
      to: landlordEmail,
      subject: `ALERT: Maintenance Request Open for ${daysOpen} Days`,
      html,
    });

    if (response.error) throw response.error;

    await logEmailDelivery('maintenance-escalation', landlordEmail, 'Maintenance Escalation', 'sent');
    res.json({ success: true, messageId: response.data?.id });
  } catch (err) {
    await logEmailDelivery('maintenance-escalation', landlordEmail, 'Maintenance Escalation', 'failed', String(err));
    res.status(500).json({ error: String(err) });
  }
});

// POST /api/email/send-lease-welcome - Send on lease creation
router.post('/send-lease-welcome', async (req, res) => {
  const { tenantEmail, tenantName, property, leaseStart, leaseEnd, monthlyRent, leaseTerms, portalLink } = req.body;

  try {
    const html = loadTemplate('new-lease-welcome', {
      tenant_name: tenantName,
      property,
      lease_start: new Date(leaseStart).toLocaleDateString(),
      lease_end: new Date(leaseEnd).toLocaleDateString(),
      monthly_rent: `$${parseFloat(monthlyRent).toFixed(2)}`,
      lease_terms: leaseTerms || 'See portal for full terms',
      portal_link: portalLink,
    });

    const response = await resend.emails.send({
      from: process.env.RESEND_FROM_EMAIL || 'noreply@realestate-os.com',
      to: tenantEmail,
      subject: 'Welcome to Your New Lease',
      html,
    });

    if (response.error) throw response.error;

    await logEmailDelivery('new-lease-welcome', tenantEmail, 'New Lease Welcome', 'sent');
    res.json({ success: true, messageId: response.data?.id });
  } catch (err) {
    await logEmailDelivery('new-lease-welcome', tenantEmail, 'New Lease Welcome', 'failed', String(err));
    res.status(500).json({ error: String(err) });
  }
});

// GET /api/email/deliveries - Show delivery logs + retry status
router.get('/deliveries', async (req, res) => {
  const { status, limit = 50, offset = 0 } = req.query;

  try {
    let query = supabase.from('email_deliveries').select('*', { count: 'exact' });

    if (status) {
      query = query.eq('status', status);
    }

    const { data, count, error } = await query
      .order('created_at', { ascending: false })
      .range(Number(offset), Number(offset) + Number(limit) - 1);

    if (error) throw error;

    res.json({
      data,
      total: count,
      limit: Number(limit),
      offset: Number(offset),
    });
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

export default router;
