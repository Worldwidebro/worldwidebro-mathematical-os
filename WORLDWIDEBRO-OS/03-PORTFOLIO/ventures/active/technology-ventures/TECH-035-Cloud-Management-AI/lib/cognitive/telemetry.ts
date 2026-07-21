import type { SignalEventPayload } from './types';

const QUEUE_KEY = 'cognitive_signal_queue_v1';

function enqueue(payload: SignalEventPayload): void {
  if (typeof window === 'undefined') return;
  try {
    const raw = window.localStorage.getItem(QUEUE_KEY);
    const q: SignalEventPayload[] = raw ? JSON.parse(raw) : [];
    q.push(payload);
    while (q.length > 150) q.shift();
    window.localStorage.setItem(QUEUE_KEY, JSON.stringify(q));
  } catch {
    /* ignore */
  }
}

export function emitSignal(
  partial: Omit<SignalEventPayload, 'timestamp' | 'venture_id' | 'session_id'> & {
    venture_id: string;
    session_id: string;
  },
  ingestUrl?: string | null
): SignalEventPayload {
  const payload: SignalEventPayload = {
    ...partial,
    timestamp: new Date().toISOString(),
  };
  enqueue(payload);
  if (ingestUrl && typeof navigator !== 'undefined') {
    try {
      const body = JSON.stringify(payload);
      if (navigator.sendBeacon) {
        navigator.sendBeacon(ingestUrl, new Blob([body], { type: 'application/json' }));
      } else {
        void fetch(ingestUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body,
          keepalive: true,
        });
      }
    } catch {
      /* ignore */
    }
  }
  if (typeof process !== 'undefined' && process.env?.NODE_ENV === 'development') {
    // eslint-disable-next-line no-console
    console.debug('[cognitive]', payload.event_type, payload);
  }
  return payload;
}

export function stableVariant(sessionId: string, experimentId: string): 'A' | 'B' {
  const s = `${sessionId}:${experimentId}`;
  let h = 0;
  for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) >>> 0;
  return h % 2 === 0 ? 'A' : 'B';
}
