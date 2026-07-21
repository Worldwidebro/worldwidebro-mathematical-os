export type GuidanceLevel = 'minimal' | 'standard' | 'high';
export type DisclosureLevel = 'compressed' | 'default' | 'expanded';

export interface SessionSignals {
  confidence_score: number;
  risk_score: number;
  returning_user: boolean;
  form_error_count: number;
  page_views: number;
}

export interface RuleWhen {
  risk_score_gte?: number;
  confidence_score_lte?: number;
  confidence_score_gte?: number;
  risk_score_lte?: number;
  returning_user?: boolean;
  form_error_count_gte?: number;
}

export interface RuleThen {
  inject_confirmation_step?: boolean;
  show_risk_copy?: boolean;
  guidance_level?: GuidanceLevel;
  disclosure_level?: DisclosureLevel;
  show_contextual_help?: boolean;
  prioritize_next_best_action?: boolean;
  prefill_known_fields?: boolean;
  prioritize_resume_flow?: boolean;
  switch_to_guided_form_mode?: boolean;
  offer_human_support?: boolean;
}

export interface DecisionRulesFile {
  version: string;
  description?: string;
  rules: Array<{ id: string; when: RuleWhen; then: RuleThen }>;
}

export interface MergedDecision {
  rule_ids: string[];
  inject_confirmation_step: boolean;
  show_risk_copy: boolean;
  guidance_level: GuidanceLevel;
  disclosure_level: DisclosureLevel;
  show_contextual_help: boolean;
  prioritize_next_best_action: boolean;
  prefill_known_fields: boolean;
  prioritize_resume_flow: boolean;
  switch_to_guided_form_mode: boolean;
  offer_human_support: boolean;
}

export interface SignalEventPayload {
  event_id?: string;
  venture_id: string;
  session_id: string;
  event_type: string;
  page?: string;
  component_id?: string;
  metadata?: Record<string, unknown>;
  timestamp: string;
}

export interface ExperimentTest {
  id: string;
  hypothesis: string;
  metric?: string;
  rice?: { reach: number; impact: number; confidence: number; effort: number };
}

export interface ExperimentsFile {
  venture_id?: string;
  tests: ExperimentTest[];
}
