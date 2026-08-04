import axios from 'axios';
import { supabase } from '../index';

const API_BASE = process.env.API_BASE || 'http://localhost:3001';

/**
 * Email Triggers Service
 * Pseudocode for cron-driven email automation
 * Wire into: node-cron, AWS EventBridge, or Vercel Cron Functions
 */

// ponytail: simple query + API calls, scales at 1000+/day (event-driven upgrade path)
export const emailTriggers = {
  /**
   * CRON: Daily 2pm - rent reminder 3 days before due
   */
  rentReminderCron: async () => {
    console.log('[EMAIL] Starting rent reminder cron...');
    try {
      const threeDaysFromNow = new Date();
      threeDaysFromNow.setDate(threeDaysFromNow.getDate() + 3);
      const dueDateStr = threeDaysFromNow.toISOString().split('T')[0];

      const { data: duePayments, error: payError } = await supabase
        .from('rent_payments')
        .select('id, amount, month, units!inner(id, rent_amount, tenant_id, property_id), units!inner(tenant_id(email, full_name))')
        .eq('status', 'pending')
        .eq('month', dueDateStr);

      if (payError) throw payError;

      for (const payment of duePayments || []) {
        const unit = payment.units as any;
        const tenant = unit.tenant_id as any;
        await axios.post(`${API_BASE}/api/email/send-rent-reminder`, {
          unitId: unit.id,
          tenantEmail: tenant.email,
          tenantName: tenant.full_name,
          amount: payment.amount,
          dueDate: payment.month,
          paymentLink: `${process.env.FRONTEND_URL}/tenant/portal?rent_payment=${payment.id}`,
        });
      }
      console.log(`[EMAIL] Sent ${duePayments?.length || 0} rent reminders`);
    } catch (err) {
      console.error('[EMAIL] Rent reminder cron failed:', err);
    }
  },

  /**
   * CRON: Daily 8am - escalate tickets open > 7 days
   */
  maintenanceEscalationCron: async () => {
    console.log('[EMAIL] Starting maintenance escalation cron...');
    try {
      const sevenDaysAgo = new Date();
      sevenDaysAgo.setDate(sevenDaysAgo.getDate() - 7);

      const { data: openTickets, error: ticketError } = await supabase
        .from('maintenance_requests')
        .select('id, description, created_at, property_id, properties!inner(created_by)')
        .neq('status', 'completed')
        .lt('created_at', sevenDaysAgo.toISOString());

      if (ticketError) throw ticketError;

      for (const ticket of openTickets || []) {
        const property = ticket.properties as any;
        const landlord = property.created_by as any;
        const { data: user } = await supabase
          .from('users')
          .select('email')
          .eq('id', landlord.id)
          .single();

        if (!user) continue;

        const daysOpen = Math.floor((Date.now() - new Date(ticket.created_at).getTime()) / (1000 * 60 * 60 * 24));
        await axios.post(`${API_BASE}/api/email/send-escalation`, {
          landlordEmail: user.email,
          daysOpen,
          ticketDescription: ticket.description,
          portalLink: `${process.env.FRONTEND_URL}/landlord/maintenance/${ticket.id}`,
        });
      }
      console.log(`[EMAIL] Sent ${openTickets?.length || 0} escalation alerts`);
    } catch (err) {
      console.error('[EMAIL] Maintenance escalation cron failed:', err);
    }
  },

  /**
   * TRIGGERED: maintenance status update
   */
  onMaintenanceStatusChange: async (ticketId: string, newStatus: string, notes?: string) => {
    console.log('[EMAIL] Maintenance status changed:', ticketId);
    try {
      const { data: ticket } = await supabase
        .from('maintenance_requests')
        .select('id, tenant_id, users!inner(email)')
        .eq('id', ticketId)
        .single();

      if (!ticket) return;
      const tenant = ticket.users as any;
      await axios.post(`${API_BASE}/api/email/send-maintenance-update`, {
        ticketId: ticket.id,
        tenantEmail: tenant.email,
        status: newStatus,
        notes: notes || '',
      });
    } catch (err) {
      console.error('[EMAIL] Maintenance status email failed:', err);
    }
  },

  /**
   * TRIGGERED: payment confirmed
   */
  onPaymentConfirmed: async (paymentId: string) => {
    console.log('[EMAIL] Payment confirmed:', paymentId);
    try {
      const { data: payment } = await supabase
        .from('rent_payments')
        .select('id, amount, paid_date, units!inner(id, tenant_id(email), property_id(address))')
        .eq('id', paymentId)
        .single();

      if (!payment) return;
      const unit = payment.units as any;
      const tenant = unit.tenant_id as any;
      const property = unit.property_id as any;
      await axios.post(`${API_BASE}/api/email/send-payment-receipt`, {
        tenantEmail: tenant.email,
        amount: payment.amount,
        date: payment.paid_date || new Date(),
        propertyName: property.address,
      });
    } catch (err) {
      console.error('[EMAIL] Payment receipt email failed:', err);
    }
  },

  /**
   * TRIGGERED: lease created
   */
  onLeaseCreated: async (leaseId: string) => {
    console.log('[EMAIL] New lease created:', leaseId);
    try {
      const { data: lease } = await supabase
        .from('leases')
        .select('id, start_date, end_date, terms, tenant_id(email, full_name), unit_id(id, rent_amount, property_id(address, city, state))')
        .eq('id', leaseId)
        .single();

      if (!lease) return;
      const tenant = lease.tenant_id as any;
      const unit = lease.unit_id as any;
      const property = unit.property_id as any;

      const leaseTermsHtml = lease.terms
        ? typeof lease.terms === 'string'
          ? lease.terms
          : `<ul>${(lease.terms as any[]).map((t) => `<li>${t}</li>`).join('')}</ul>`
        : '<p>See portal for full lease terms</p>';

      await axios.post(`${API_BASE}/api/email/send-lease-welcome`, {
        tenantEmail: tenant.email,
        tenantName: tenant.full_name,
        property: `${property.address}, ${property.city}, ${property.state}`,
        leaseStart: lease.start_date,
        leaseEnd: lease.end_date,
        monthlyRent: unit.rent_amount,
        leaseTerms: leaseTermsHtml,
        portalLink: `${process.env.FRONTEND_URL}/tenant/portal`,
      });
    } catch (err) {
      console.error('[EMAIL] New lease welcome email failed:', err);
    }
  },
};
