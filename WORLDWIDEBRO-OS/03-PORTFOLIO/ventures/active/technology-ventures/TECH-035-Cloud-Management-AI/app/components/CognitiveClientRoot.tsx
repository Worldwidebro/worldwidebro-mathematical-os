'use client';

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useRef,
  useState,
} from 'react';
import { usePathname } from 'next/navigation';
import type { DecisionRulesFile, ExperimentsFile, MergedDecision } from '../../lib/cognitive/types';
import { evaluateRules } from '../../lib/cognitive/engine';
import {
  bumpAfterNavigation,
  bumpFormError,
  loadOrCreateSession,
  saveSession,
  toSignals,
  type PersistedSession,
} from '../../lib/cognitive/session';
import { emitSignal, stableVariant } from '../../lib/cognitive/telemetry';

type CognitiveContextValue = {
  session: PersistedSession;
  decision: MergedDecision;
  signals: ReturnType<typeof toSignals>;
  recordFormError: () => void;
  refreshSession: () => void;
};

const CognitiveContext = createContext<CognitiveContextValue | null>(null);

export function useCognitiveUX(): CognitiveContextValue | null {
  return useContext(CognitiveContext);
}

type Props = {
  ventureId: string;
  ventureName: string;
  repositoryUrl: string;
  experiments: ExperimentsFile;
  decisionRules: DecisionRulesFile;
  children: React.ReactNode;
};

export default function CognitiveClientRoot({
  ventureId,
  ventureName,
  repositoryUrl,
  experiments,
  decisionRules,
  children,
}: Props) {
  const pathname = usePathname() || '/';
  const ingestUrl =
    typeof process !== 'undefined' ? process.env.NEXT_PUBLIC_COGNITIVE_INGEST_URL || '' : '';
  const experimentsLogged = useRef(false);

  const [session, setSession] = useState<PersistedSession>(() => loadOrCreateSession(ventureId));

  const refreshSession = useCallback(() => {
    setSession(loadOrCreateSession(ventureId));
  }, [ventureId]);

  useEffect(() => {
    const onFormErr = () => {
      setSession((prev) => {
        const bumped = bumpFormError(prev);
        saveSession(ventureId, bumped);
        emitSignal(
          {
            venture_id: ventureId,
            session_id: bumped.session_id,
            event_type: 'form_error',
            page: pathname,
            metadata: { form_error_count: bumped.form_error_count },
          },
          ingestUrl || null
        );
        return bumped;
      });
    };
    window.addEventListener('cognitive-form-error', onFormErr);
    return () => window.removeEventListener('cognitive-form-error', onFormErr);
  }, [ventureId, pathname, ingestUrl]);

  useEffect(() => {
    setSession((prev) => {
      const bumped = bumpAfterNavigation(prev, pathname);
      saveSession(ventureId, bumped);
      emitSignal(
        {
          venture_id: ventureId,
          session_id: bumped.session_id,
          event_type: 'page_view',
          page: pathname,
          metadata: { venture_name: ventureName, repository_url: repositoryUrl },
        },
        ingestUrl || null
      );
      return bumped;
    });
  }, [pathname, ventureId, ventureName, repositoryUrl, ingestUrl]);

  useEffect(() => {
    if (!session.session_id) return;
    if (typeof window !== 'undefined') {
      const k = `cognitive_exp:${ventureId}:${session.session_id}`;
      if (window.sessionStorage.getItem(k)) {
        experimentsLogged.current = true;
        return;
      }
      window.sessionStorage.setItem(k, '1');
    }
    if (experimentsLogged.current) return;
    experimentsLogged.current = true;
    const tests = experiments?.tests || [];
    const sid = session.session_id;
    for (const t of tests) {
      const variant = stableVariant(sid, t.id);
      emitSignal(
        {
          venture_id: ventureId,
          session_id: sid,
          event_type: 'experiment_exposure',
          page: pathname,
          component_id: t.id,
          metadata: {
            hypothesis: t.hypothesis,
            variant_id: variant,
            metric: t.metric,
            rice: t.rice,
          },
        },
        ingestUrl || null
      );
    }
  }, [experiments, ventureId, session.session_id, pathname, ingestUrl]);

  const signals = useMemo(() => toSignals(session), [session]);
  const decision = useMemo(
    () => evaluateRules(signals, decisionRules),
    [signals, decisionRules]
  );

  const recordFormError = useCallback(() => {
    window.dispatchEvent(new Event('cognitive-form-error'));
  }, []);

  const ctx: CognitiveContextValue = useMemo(
    () => ({ session, decision, signals, recordFormError, refreshSession }),
    [session, decision, signals, recordFormError, refreshSession]
  );

  return (
    <CognitiveContext.Provider value={ctx}>
      <div
        className={`cognitive-root cognitive-disclosure-${decision.disclosure_level}`}
        data-guidance={decision.guidance_level}
        data-prioritize-nba={decision.prioritize_next_best_action ? 'true' : 'false'}
      >
        <div className="cognitive-strip" aria-live="polite">
          <span className="cognitive-strip__label">Cognitive UX</span>
          <span>guidance {decision.guidance_level}</span>
          <span>disclosure {decision.disclosure_level}</span>
          <span>{decision.rule_ids.length ? `${decision.rule_ids.length} rules` : 'baseline'}</span>
        </div>
        <AdaptiveChrome
          ventureId={ventureId}
          decision={decision}
          sessionId={session.session_id}
          ingestUrl={ingestUrl}
          pathname={pathname}
        />
        {children}
      </div>
    </CognitiveContext.Provider>
  );
}

function AdaptiveChrome({
  ventureId,
  decision,
  sessionId,
  ingestUrl,
  pathname,
}: {
  ventureId: string;
  decision: MergedDecision;
  sessionId: string;
  ingestUrl: string;
  pathname: string;
}) {
  const [helpOpen, setHelpOpen] = useState(false);

  const onCtaClick = (componentId: string) => {
    emitSignal(
      {
        venture_id: ventureId,
        session_id: sessionId,
        event_type: 'cta_click',
        page: pathname,
        component_id: componentId,
      },
      ingestUrl || null
    );
  };

  if (
    !decision.show_risk_copy &&
    !decision.show_contextual_help &&
    !decision.inject_confirmation_step &&
    !decision.offer_human_support
  ) {
    return null;
  }

  return (
    <div className="cognitive-chrome" role="region" aria-label="Adaptive guidance">
      {decision.show_risk_copy || decision.inject_confirmation_step ? (
        <div className="cognitive-banner cognitive-banner--risk">
          <strong>Before you continue:</strong>{' '}
          {decision.show_risk_copy
            ? 'High-impact actions deserve a second look. Confirm details and expected outcomes.'
            : 'Please confirm you understand this step before proceeding.'}
          {decision.inject_confirmation_step ? (
            <label className="cognitive-check">
              <input
                type="checkbox"
                onChange={(e) => {
                  if (e.target.checked) {
                    emitSignal(
                      {
                        venture_id: ventureId,
                        session_id: sessionId,
                        event_type: 'confirmation_ack',
                        page: pathname,
                        metadata: { ack: true },
                      },
                      ingestUrl || null
                    );
                  }
                }}
              />
              I understand this step
            </label>
          ) : null}
        </div>
      ) : null}

      {decision.show_contextual_help || decision.offer_human_support ? (
        <div className="cognitive-help">
          <button
            type="button"
            className="cognitive-help-toggle"
            onClick={() => {
              setHelpOpen((v) => !v);
              onCtaClick('contextual_help_toggle');
            }}
          >
            {decision.offer_human_support ? 'Get human support' : 'Contextual help'}
          </button>
          {helpOpen ? (
            <div className="cognitive-help-panel">
              <p>
                {decision.switch_to_guided_form_mode
                  ? 'Guided mode: answer one field at a time. We will surface the next best action.'
                  : 'Tips adapt to your session. Prefer a human? Use Contact and note your goal.'}
              </p>
              {decision.offer_human_support ? (
                <a href="/contact" className="cognitive-help-link" onClick={() => onCtaClick('help_contact')}>
                  Open contact
                </a>
              ) : null}
            </div>
          ) : null}
        </div>
      ) : null}
    </div>
  );
}
