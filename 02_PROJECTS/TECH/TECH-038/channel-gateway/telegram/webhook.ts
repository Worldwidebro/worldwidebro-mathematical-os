import { routeMessage } from '../router';
import { IncomingMessage } from '../types';

export async function handleTelegramWebhook(body: any): Promise<any> {
  const message = body.message;
  if (!message?.text && !message?.voice) return { ok: true };

  const incoming: IncomingMessage = {
    channel: 'telegram',
    channel_id: String(message.from.id),
    venture_id: process.env.VENTURE_ID || 'LT-005',
    content: message.text || '[voice]',
    message_type: message.text ? 'text' : 'voice',
    timestamp: new Date(message.date * 1000).toISOString(),
  };

  const response = await routeMessage(incoming);
  return sendTelegramMessage(message.chat.id, response.text);
}

async function sendTelegramMessage(chat_id: string, text: string): Promise<any> {
  console.log(`[Telegram] → ${chat_id}: ${text}`);
  return { ok: true };
}
