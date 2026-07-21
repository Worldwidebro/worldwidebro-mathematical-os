import type {
  DecisionRulesFile,
  DisclosureLevel,
  GuidanceLevel,
  MergedDecision,
  RuleThen,
  RuleWhen,
  SessionSignals,
} from './types';

function matchesWhen(when: RuleWhen, s: SessionSignals): boolean {
  if (when.risk_score_gte !== undefined && s.risk_score < when.risk_score_gte) return false;
  if (when.risk_score_lte !== undefined && s.risk_score > when.risk_score_lte) return false;
  if (when.confidence_score_lte !== undefined && s.confidence_score > when.confidence_score_lte)
    return false;
  if (when.confidence_score_gte !== undefined && s.confidence_score < when.confidence_score_gte)
    return false;
  if (when.returning_user !== undefined && s.returning_user !== when.returning_user) return false;
  if (when.form_error_count_gte !== undefined && s.form_error_count < when.form_error_count_gte)
    return false;
  return true;
}

const guidanceRank: Record<GuidanceLevel, number> = {
  minimal: 0,
  standard: 1,
  high: 2,
};

function applyFlags(then: RuleThen, merged: MergedDecision): void {
  if (then.inject_confirmation_step) merged.inject_confirmation_step = true;
  if (then.show_risk_copy) merged.show_risk_copy = true;
  if (then.show_contextual_help) merged.show_contextual_help = true;
  if (then.prioritize_next_best_action) merged.prioritize_next_best_action = true;
  if (then.prefill_known_fields) merged.prefill_known_fields = true;
  if (then.prioritize_resume_flow) merged.prioritize_resume_flow = true;
  if (then.switch_to_guided_form_mode) merged.switch_to_guided_form_mode = true;
  if (then.offer_human_support) merged.offer_human_support = true;
}

export function emptyDecision(): MergedDecision {
  return {
    rule_ids: [],
    inject_confirmation_step: false,
    show_risk_copy: false,
    guidance_level: 'standard',
    disclosure_level: 'default',
    show_contextual_help: false,
    prioritize_next_best_action: false,
    prefill_known_fields: false,
    prioritize_resume_flow: false,
    switch_to_guided_form_mode: false,
    offer_human_support: false,
  };
}

export function evaluateRules(signals: SessionSignals, file: DecisionRulesFile): MergedDecision {
  const merged = emptyDecision();
  let bestGuidance: GuidanceLevel = merged.guidance_level;
  let bestGuidanceRank = guidanceRank[bestGuidance];
  let lastDisclosure: DisclosureLevel | undefined;

  for (const rule of file.rules || []) {
    if (!matchesWhen(rule.when, signals)) continue;
    merged.rule_ids.push(rule.id);
    applyFlags(rule.then, merged);
    if (rule.then.guidance_level) {
      const r = guidanceRank[rule.then.guidance_level];
      if (r > bestGuidanceRank) {
        bestGuidanceRank = r;
        bestGuidance = rule.then.guidance_level;
      }
    }
    if (rule.then.disclosure_level) lastDisclosure = rule.then.disclosure_level;
  }

  if (merged.rule_ids.length) merged.guidance_level = bestGuidance;
  if (lastDisclosure) merged.disclosure_level = lastDisclosure;
  return merged;
}
