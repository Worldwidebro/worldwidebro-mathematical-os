import type { SessionSignals } from './types';

const STORAGE_PREFIX = 'cognitive_session_v1:';

export interface PersistedSession {
  session_id: string;
  venture_id: string;
  first_seen_iso: string;
  last_seen_iso: string;
  visit_count: number;
  page_views: number;
  confidence_score: number;
  risk_score: number;
  form_error_count: number;
  last_path: string;
}

function storageKey(ventureId: string): string {
  return `${STORAGE_PREFIX}${ventureId}`;
}

function safeParse(raw: string | null): PersistedSession | null {
  if (!raw) return null;
  try {
    return JSON.parse(raw) as PersistedSession;
  } catch {
    return null;
  }
}

function newSession(ventureId: string): PersistedSession {
  const now = new Date().toISOString();
  return {
    session_id:
      typeof crypto !== 'undefined' && 'randomUUID' in crypto
        ? crypto.randomUUID()
        : `sess_${Math.random().toString(36).slice(2)}`,
    venture_id: ventureId,
    first_seen_iso: now,
    last_seen_iso: now,
    visit_count: 1,
    page_views: 0,
    confidence_score: 0.5,
    risk_score: 0.22,
    form_error_count: 0,
    last_path: '',
  };
}

/** Sessions older than this gap count as a new visit for returning_user heuristics. */
const VISIT_GAP_MS = 1000 * 60 * 45;

export function loadOrCreateSession(ventureId: string): PersistedSession {
  if (typeof window === 'undefined') return newSession(ventureId);
  const prev = safeParse(window.localStorage.getItem(storageKey(ventureId)));
  const now = Date.now();
  if (!prev) {
    const s = newSession(ventureId);
    window.localStorage.setItem(storageKey(ventureId), JSON.stringify(s));
    return s;
  }
  const last = Date.parse(prev.last_seen_iso || prev.first_seen_iso);
  const isNewVisit = Number.isFinite(last) && now - last > VISIT_GAP_MS;
  const next: PersistedSession = {
    ...prev,
    visit_count: isNewVisit ? prev.visit_count + 1 : prev.visit_count,
    last_seen_iso: new Date().toISOString(),
  };
  window.localStorage.setItem(storageKey(ventureId), JSON.stringify(next));
  return next;
}

export function saveSession(ventureId: string, patch: Partial<PersistedSession>): PersistedSession {
  if (typeof window === 'undefined') return newSession(ventureId);
  const cur = safeParse(window.localStorage.getItem(storageKey(ventureId))) || newSession(ventureId);
  const next = { ...cur, ...patch, last_seen_iso: new Date().toISOString() };
  window.localStorage.setItem(storageKey(ventureId), JSON.stringify(next));
  return next;
}

export function toSignals(session: PersistedSession): SessionSignals {
  const returning_user = session.visit_count > 1;
  return {
    confidence_score: clamp(session.confidence_score, 0, 1),
    risk_score: clamp(session.risk_score, 0, 1),
    returning_user,
    form_error_count: session.form_error_count,
    page_views: session.page_views,
  };
}

export function clamp(n: number, min: number, max: number): number {
  return Math.min(max, Math.max(min, n));
}

/** Heuristic updates after navigation */
export function bumpAfterNavigation(
  session: PersistedSession,
  path: string
): PersistedSession {
  let confidence = session.confidence_score + 0.035;
  let risk = session.risk_score;
  const highIntent = /\/(contact|get-involved)(\/|$)/.test(path);
  if (highIntent) risk += 0.07;
  if (path !== session.last_path) confidence += 0.02;
  return {
    ...session,
    page_views: session.page_views + 1,
    last_path: path,
    confidence_score: clamp(confidence, 0.08, 0.96),
    risk_score: clamp(risk, 0.05, 0.96),
  };
}

export function bumpFormError(session: PersistedSession): PersistedSession {
  return {
    ...session,
    form_error_count: session.form_error_count + 1,
    confidence_score: clamp(session.confidence_score - 0.12, 0.05, 1),
    risk_score: clamp(session.risk_score + 0.05, 0, 1),
  };
}
