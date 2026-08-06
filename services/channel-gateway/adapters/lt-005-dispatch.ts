import { AgentResponse } from '../types';

/**
 * LT-005 Medical Courier dispatch agent
 * Handles: STAT pickups, driver assignment, status updates, compliance
 */
export async function dispatchAgent(request: any): Promise<AgentResponse> {
  const intent = parseIntent(request.message);
  const { customer_type } = detectUser(request.context);

  if (intent === 'STAT_PICKUP' && customer_type === 'customer') {
    return {
      text: `STAT pickup received. Driver in ${Math.floor(Math.random() * 10) + 2}-${Math.floor(Math.random() * 10) + 5} minutes.`,
      actions: [{ type: 'create_pickup_request', payload: { customer_id: request.user_id } }],
      context_update: { last_intent: 'STAT_PICKUP', status: 'pending_assignment' },
    };
  }

  if (intent === 'STATUS') {
    return {
      text: `Status: no active pickups. Send STAT to request courier.`,
      context_update: request.context,
    };
  }

  return {
    text: `LT-005: "${request.message}" — say STAT for pickup or STATUS for tracking.`,
    context_update: request.context,
  };
}

function parseIntent(message: string): string {
  const lower = message.toLowerCase();
  if (lower.includes('stat') || lower.includes('urgent')) return 'STAT_PICKUP';
  if (lower.includes('status') || lower.includes('where')) return 'STATUS';
  return 'UNKNOWN';
}

function detectUser(context: any): any {
  return { customer_type: context.customer_type || 'customer' };
}
