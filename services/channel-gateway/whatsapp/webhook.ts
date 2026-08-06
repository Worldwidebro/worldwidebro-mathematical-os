import { routeMessage } from '../router';
import { IncomingMessage } from '../types';

export async function handleWhatsAppWebhook(body: any): Promise<any> {
  const entry = body.entry?.[0];
  const changes = entry?.changes?.[0];
  const message = changes?.value?.messages?.[0];

  if (!message) return { status: 'ok' };

  const incoming: IncomingMessage = {
    channel: 'whatsapp',
    channel_id: message.from,
    venture_id: process.env.VENTURE_ID || 'LT-005',
    content: message.text?.body || '',
    message_type: message.type === 'text' ? 'text' : 'media',
    media_url: message.image?.link || message.document?.link,
    timestamp: new Date(parseInt(message.timestamp) * 1000).toISOString(),
  };

  const response = await routeMessage(incoming);
  return sendWhatsAppMessage(message.from, response.text);
}

async function sendWhatsAppMessage(phone: string, text: string): Promise<any> {
  console.log(`[WhatsApp] → ${phone}: ${text}`);
  return { status: 'queued' };
}

export async function verifyWebhookToken(token: string): Promise<boolean> {
  return token === process.env.WHATSAPP_WEBHOOK_TOKEN;
}
