class ScoringEngine:
    def calculate_readiness(self, code_completeness, api_readiness, documentation_score, test_coverage):
        raw_score = (
            code_completeness * 0.4 +
            api_readiness * 0.3 +
            documentation_score * 0.2 +
            test_coverage * 0.1
        )
        score = round(raw_score)
        
        # Mapped from AGENTS.md rules
        if score >= 90:
            tier = 'AUTONOMOUS'
        elif score >= 80:
            tier = 'SUPERVISED'
        elif score >= 70:
            tier = 'MONITORED'
        else:
            tier = 'TRAINING'
            
        return {"score": score, "tier": tier}

    def generate_report(self, code_completeness, api_readiness, documentation_score, test_coverage):
        res = self.calculate_readiness(code_completeness, api_readiness, documentation_score, test_coverage)
        score = res["score"]
        tier = res["tier"]
        
        lines = [
            f"📊 Venture Readiness Audit: {score}% ({tier})",
            f"==========================================",
            f"- Code Completeness: {code_completeness}%",
            f"- API Gateway Wiring: {api_readiness}%",
            f"- Documentation Depth: {documentation_score}%",
            f"- Test Suite Coverage: {test_coverage}%",
            ""
        ]
        
        if tier == 'AUTONOMOUS':
            lines.append("✅ System is 100% autonomous. Ready for direct deployment without supervision.")
        elif tier == 'SUPERVISED':
            lines.append("⚠️ Requires team lead approval ($1K+) or manual oversight for transactions.")
        elif tier == 'MONITORED':
            lines.append("⚠️ Requires manager/director approval on all executions.")
        else:
            lines.append("❌ Undergoing training. Pull from production until score reaches 70%.")
            
        return "\n".join(lines)
