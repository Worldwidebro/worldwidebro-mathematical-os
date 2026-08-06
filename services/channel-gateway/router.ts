import { IncomingMessage, AgentResponse } from './types';

// ponytail: in-memory state for dev/test; swap Supabase tables when infrastructure ready
const identities = new Map<string, any>();
const sessions = new Map<string, any>();

export async function routeMessage(incoming: IncomingMessage): Promise<AgentResponse> {
  const identity = await resolveIdentity(
    incoming.channel,
    incoming.channel_id,
    incoming.venture_id
  );

  const session = await getOrCreateSession(
    identity.user_id,
    incoming.channel,
    incoming.venture_id
  );

  console.log(`[${incoming.channel}] ${identity.user_id}: ${incoming.content}`);

  const response = await dispatchToAgent({
    session_id: session.session_id,
    user_id: identity.user_id,
    venture_id: incoming.venture_id,
    message: incoming.content,
    context: session.context,
    metadata: { channel: incoming.channel, timestamp: incoming.timestamp },
  });

  session.context = response.context_update || session.context;
  session.last_message_at = new Date().toISOString();

  return response;
}

async function resolveIdentity(channel: string, channel_id: string, venture_id: string): Promise<any> {
  const key = `${venture_id}:${channel}:${channel_id}`;
  if (identities.has(key)) return identities.get(key);

  const identity = { user_id: `${channel}_${channel_id}`, venture_id, customer_type: 'customer' };
  if (channel === 'whatsapp' || channel === 'voice') identity.phone = channel_id;
  if (channel === 'telegram') identity.telegram_id = channel_id;

  identities.set(key, identity);
  return identity;
}

async function getOrCreateSession(user_id: string, channel: string, venture_id: string): Promise<any> {
  const key = `${venture_id}:${user_id}:${channel}`;
  if (sessions.has(key)) return sessions.get(key);

  const session = {
    session_id: `${user_id}_${channel}_${Date.now()}`,
    user_id,
    channel,
    context: {},
    last_message_at: new Date().toISOString(),
  };

  sessions.set(key, session);
  return session;
}

async function dispatchToAgent(request: any): Promise<AgentResponse> {
  const agents = { 'LT-005': 'dispatch', 'CON-001': 'construction', 'OPS-001': 'staffing' };
  const agent = agents[request.venture_id] || 'fallback';

  // TODO: wire to actual LangGraph/MCP agent
  return {
    text: `[${agent}] Processing: "${request.message}"`,
    context_update: request.context,
  };
}
