export interface IncomingMessage {
  channel: 'whatsapp' | 'telegram' | 'voice' | 'web';
  channel_id: string;
  venture_id: string;
  content: string;
  message_type: 'text' | 'media' | 'voice' | 'location';
  media_url?: string;
  timestamp: string;
}

export interface AgentResponse {
  text: string;
  actions?: Array<{ type: string; payload: any }>;
  context_update?: Record<string, any>;
}
