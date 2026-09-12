# Strict Reality Connectivity Audit

**Last Run:** 2026-09-12T16:41:35.707754

**Rule:** NO HALLUCINATIONS. NO MOCKS. NO STATIC FILE CHECKS.
If a connection cannot be proven via a live API, active Database, or physical network socket, it **FAILS**.

## Audit Summary

- **Total Tests:** 500
- **Passing (Physical):** 40
- **Failing (Offline/Unwired):** 460

> **40/500 reality tests passing.**

## Test Matrix

| Test ID | Description | Status | Reality Evidence |
|---|---|---|---|
| CONN-001 | Company has a defined organizational root | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-002 | CEO connects to company | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-003 | Founder connects to company | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-004 | Departments connect to company | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-005 | Teams connect to departments | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-006 | Roles connect to teams | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-007 | People connect to roles | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-008 | Agents connect to roles | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-009 | Workflows connect to roles | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-010 | KPIs connect to roles | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-011 | Responsibilities connect to roles | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-012 | Authority connects to roles | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-013 | Inputs connect to roles | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-014 | Outputs connect to roles | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-015 | Decisions connect to roles | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-016 | Managers connect to roles | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-017 | Direct reports connect to managers | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-018 | Roles connect to departments | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-019 | Departments connect to strategic objectives | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-020 | Strategic objectives connect to company | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-021 | Company objectives connect to KPIs | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-022 | KPIs connect to measurable data | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-023 | Every role has an owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-024 | Every department has an owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-025 | Every organizational node has an upstream/downstream relationship | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-026 | Idea can identify its owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-027 | Idea connects to CEO | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-028 | Idea connects to Chief of Staff | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-029 | Idea connects to Product | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-030 | Idea connects to Strategy | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-031 | Idea connects to Research | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-032 | Idea connects to Marketing | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-033 | Idea connects to Finance | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-034 | Idea connects to Legal | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-035 | Idea connects to Security | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-036 | Idea connects to Design | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-037 | Idea connects to Architecture | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-038 | Idea connects to Engineering | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-039 | Idea connects to QA | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-040 | Idea connects to DevOps | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-041 | Idea connects to Sales | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-042 | Idea connects to Customer Success | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-043 | Idea connects to Support | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-044 | Idea connects to Analytics | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-045 | Idea identifies required departments | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-046 | Idea identifies unnecessary departments | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-047 | Idea identifies required roles | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-048 | Idea identifies required approvals | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-049 | Idea creates an execution path | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-050 | Idea produces a traceable lineage from origin to completion | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-051 | Idea assigns an Idea Owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-052 | Idea identifies Sponsor | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-053 | Idea identifies Product Owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-054 | Idea identifies Researcher | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-055 | Idea identifies Strategist | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-056 | Idea identifies Financial Reviewer | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-057 | Idea identifies Legal Reviewer | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-058 | Idea identifies Security Reviewer | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-059 | Idea identifies Designer | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-060 | Idea identifies Architect | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-061 | Idea identifies Engineering Owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-062 | Idea identifies QA Owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-063 | Idea identifies Release Owner | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-064 | Idea identifies Marketing Owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-065 | Idea identifies Sales Owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-066 | Idea identifies Customer Success Owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-067 | Idea identifies Support Owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-068 | Idea identifies Analytics Owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-069 | Each role has an actual person or agent | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-070 | Person has required permissions | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-071 | Person can see assigned work | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-072 | Person can receive handoff | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-073 | Person can produce required artifact | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-074 | Person can approve/reject when authorized | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-075 | Person can hand work to next role | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-076 | CEO connects to Executive department | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-077 | Chief of Staff connects to Executive Operations | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-078 | Product Manager connects to Product | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-079 | Researcher connects to Research | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-080 | Designer connects to Design | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-081 | Architect connects to Architecture | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-082 | Engineer connects to Engineering | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-083 | AI Engineer connects to AI | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-084 | Data Engineer connects to Data | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-085 | DevOps connects to Infrastructure | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-086 | QA connects to Quality | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-087 | Security Engineer connects to Security | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-088 | Marketer connects to Marketing | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-089 | Product Marketer connects to GTM | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-090 | SDR connects to Sales | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-091 | AE connects to Sales | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-092 | Partnership Manager connects to Partnerships | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-093 | RevOps connects to Revenue Operations | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-094 | CSM connects to Customer Success | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-095 | Support connects to Customer Support | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-096 | Accountant connects to Finance | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-097 | Counsel connects to Legal | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-098 | Recruiter connects to People | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-099 | Operations Manager connects to Operations | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-100 | Every person has an authoritative department assignment | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-101 | CEO → Chief of Staff | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-102 | Chief of Staff → Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-103 | Strategy → Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-104 | Research → Product | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-105 | Product → Design | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-106 | Product → Architecture | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-107 | Product → Finance | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-108 | Product → Legal | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-109 | Product → Security | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-110 | Design → UX Research | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-111 | Design → Engineering | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-112 | Architecture → Engineering | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-113 | Architecture → Data | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-114 | Architecture → Security | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-115 | Engineering → QA | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-116 | Engineering → DevOps | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-117 | QA → Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-118 | Security → Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-119 | Product → Marketing | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-120 | Product → Sales | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-121 | Marketing → Sales | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-122 | Sales → Customer Success | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-123 | Customer Success → Support | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-124 | Support → Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-125 | Analytics → Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-126 | Market signal reaches Research | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-127 | Research reaches Customer Research | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-128 | Customer Research reaches Product | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-129 | Competitor data reaches Strategy | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-130 | Market size reaches Strategy | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-131 | Pricing research reaches Finance | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-132 | Customer interviews reach Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-133 | Customer pain points reach Product | ❌ FAIL | [OFFLINE] LiteLLM: Offline across mesh (Port 4000) |
| CONN-134 | Search data reaches Marketing | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-135 | Sales objections reach Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-136 | Support tickets reach Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-137 | Usage data reaches Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-138 | Churn data reaches Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-139 | Feature requests reach Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-140 | Industry trends reach Strategy | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-141 | Regulatory changes reach Legal | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-142 | Security threats reach Security | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-143 | Technology changes reach Architecture | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-144 | Repository intelligence reaches Engineering | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-145 | Existing capabilities reach Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-146 | Existing agents reach Product | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-147 | Existing MCPs reach Architecture | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-148 | Existing workflows reach Operations | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-149 | Existing ventures reach Strategy | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-150 | Discovery evidence is traceable to its source | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-151 | Research creates opportunity | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-152 | Opportunity creates problem statement | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-153 | Problem statement identifies ICP | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-154 | ICP identifies user | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-155 | User identifies use case | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-156 | Use case identifies workflow | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-157 | Workflow identifies requirements | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-158 | Requirements identify features | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-159 | Features identify product scope | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-160 | Scope identifies MVP | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-161 | MVP identifies resources | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-162 | Resources identify cost | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-163 | Cost reaches Finance | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-164 | Research identifies competitors | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-165 | Competitors reach Product Marketing | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-166 | Research identifies differentiation | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-167 | Differentiation reaches Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-168 | Research identifies demand | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-169 | Demand reaches Growth | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-170 | Research identifies risks | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-171 | Risks reach Legal | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-172 | Risks reach Security | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-173 | Research identifies technical constraints | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-174 | Constraints reach Architecture | ❌ FAIL | [OFFLINE] LiteLLM: Offline across mesh (Port 4000) |
| CONN-175 | Research package can be approved/rejected | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-176 | Product creates PRD | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-177 | PRD connects to business objective | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-178 | PRD connects to customer problem | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-179 | PRD connects to user stories | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-180 | User stories connect to acceptance criteria | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-181 | Acceptance criteria connect to tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-182 | Requirements connect to design | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-183 | Requirements connect to architecture | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-184 | Requirements connect to data | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-185 | Requirements connect to security | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-186 | Requirements connect to compliance | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-187 | Requirements connect to analytics | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-188 | Requirements connect to KPIs | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-189 | Requirements connect to revenue model | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-190 | Requirements connect to pricing | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-191 | Requirements connect to onboarding | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-192 | Requirements connect to support | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-193 | Requirements connect to documentation | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-194 | Requirements connect to deployment | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-195 | Requirements connect to monitoring | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-196 | Requirements connect to rollback | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-197 | Requirements have owners | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-198 | Requirements have priority | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-199 | Requirements have status | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-200 | Every requirement can be traced to an original business/customer need | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-201 | Product brief reaches Designer | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-202 | Designer receives user stories | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-203 | Designer receives personas | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-204 | Designer receives workflows | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-205 | Designer creates user journey | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-206 | User journey connects to requirements | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-207 | User journey connects to screens | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-208 | Screens connect to components | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-209 | Components connect to design system | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-210 | Prototype connects to UX research | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-211 | UX feedback reaches Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-212 | UX feedback reaches Design | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-213 | Approved design connects to engineering | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-214 | Design tokens connect to implementation | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-215 | Figma components map to code components | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-216 | Design states map to application states | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-217 | Error states map to engineering requirements | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-218 | Empty states map to engineering requirements | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-219 | Loading states map to engineering requirements | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-220 | Accessibility requirements map to QA | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-221 | Responsive requirements map to QA | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-222 | Design version maps to product version | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-223 | Design changes trigger implementation review | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-224 | Design approval is recorded | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-225 | Final design has traceable provenance | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-226 | Product requirements reach Architect | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-227 | Architect creates system architecture | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-228 | Architecture identifies services | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-229 | Services identify repositories | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-230 | Repositories identify code owners | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-231 | Architecture identifies databases | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-232 | Databases identify schemas | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-233 | Architecture identifies APIs | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-234 | APIs identify consumers | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-235 | Architecture identifies integrations | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-236 | Integrations identify credentials/configuration | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-237 | Architecture identifies infrastructure | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-238 | Infrastructure identifies deployment targets | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-239 | Architecture identifies security controls | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-240 | Security controls reach Security | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-241 | Architecture identifies observability | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-242 | Observability reaches DevOps | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-243 | Architecture identifies data flows | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-244 | Data flows reach Data Engineering | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-245 | Architecture identifies AI components | ❌ FAIL | [OFFLINE] LiteLLM: Offline across mesh (Port 4000) |
| CONN-246 | AI components reach AI Engineering | ❌ FAIL | [OFFLINE] LiteLLM: Offline across mesh (Port 4000) |
| CONN-247 | Architecture identifies external dependencies | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-248 | Dependencies reach Procurement | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-249 | Architecture is version-controlled | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-250 | Architecture can be reconstructed from implementation | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-251 | Requirement maps to ticket | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-252 | Ticket maps to repository | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-253 | Repository maps to owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-254 | Owner maps to engineer | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-255 | Engineer maps to branch | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-256 | Branch maps to commit | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-257 | Commit maps to ticket | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-258 | Pull request maps to ticket | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-259 | Pull request maps to reviewer | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-260 | Reviewer maps to role | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-261 | Code review produces approval/rejection | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-262 | CI triggers from pull request | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-263 | Tests trigger from CI | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-264 | Security scanning triggers from CI | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-265 | Dependency scanning triggers from CI | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-266 | Build artifact maps to commit | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-267 | Build artifact maps to version | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-268 | Version maps to release | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-269 | Release maps to deployment | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-270 | Deployment maps to environment | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-271 | Environment maps to infrastructure | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-272 | Infrastructure maps to monitoring | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-273 | Monitoring maps to service | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-274 | Service maps back to repository | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-275 | Production code can be traced back to the original requirement | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-276 | Role can identify AI-capable tasks | ❌ FAIL | [OFFLINE] LiteLLM: Offline across mesh (Port 4000) |
| CONN-277 | Role can identify human-only tasks | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-278 | Role can identify hybrid tasks | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-279 | Role connects to AI agent | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-280 | Agent connects to role | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-281 | Agent connects to workflow | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-282 | Agent connects to tools | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-283 | Agent connects to MCP | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-284 | Agent connects to model | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-285 | Model connects to runtime | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-286 | Runtime connects to infrastructure | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-287 | Agent has defined inputs | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-288 | Agent has defined outputs | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-289 | Agent has permissions | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-290 | Agent has budget | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-291 | Agent has evaluation criteria | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-292 | Agent has escalation rules | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-293 | Agent can hand off to human | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-294 | Human can hand off to agent | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-295 | Agent can trigger workflow | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-296 | Workflow can trigger agent | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-297 | Agent execution is logged | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-298 | Agent result is validated | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-299 | Agent failure reaches owner | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-300 | Agent performance reaches analytics | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-301 | Role maps to required tools | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-302 | Tool maps to department | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-303 | Tool maps to workflow | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-304 | Tool maps to capability | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-305 | MCP maps to tool | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-306 | MCP maps to role | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-307 | MCP maps to agent | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-308 | Repository maps to capability | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-309 | Capability maps to venture | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-310 | Repository maps to workflow | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-311 | Workflow maps to tool | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-312 | Tool maps to credential requirement | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-313 | Credential maps to authorized owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-314 | Tool has health status | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-315 | MCP has health status | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-316 | API has health status | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-317 | Integration has health status | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-318 | Tool failure creates alert | ❌ FAIL | [OFFLINE] LiteLLM: Offline across mesh (Port 4000) |
| CONN-319 | Failed integration identifies affected workflows | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-320 | Affected workflows identify affected roles | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-321 | Roles identify affected ventures | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-322 | Existing tool is discovered before buying new tool | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-323 | Existing repository is discovered before rebuilding | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-324 | Existing workflow is discovered before creating duplicate | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-325 | Every capability has an authoritative implementation | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-326 | Every requirement has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-327 | Every feature has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-328 | Every API has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-329 | Every integration has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-330 | Every workflow has tests | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-331 | Every agent has tests | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-332 | Every role workflow has tests | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-333 | Every permission has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-334 | Authentication has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-335 | Authorization has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-336 | Data validation has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-337 | Error handling has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-338 | Performance has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-339 | Accessibility has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-340 | Security has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-341 | Privacy has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-342 | Compliance has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-343 | Deployment has tests | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-344 | Rollback has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-345 | Monitoring has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-346 | Alerts have tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-347 | Backups have tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-348 | Recovery has tests | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-349 | Production acceptance has tests | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-350 | Failed tests automatically identify the responsible owner | ❌ FAIL | [OFFLINE] LiteLLM: Offline across mesh (Port 4000) |
| CONN-351 | Product approval triggers release | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-352 | Release triggers deployment | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-353 | Deployment triggers monitoring | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-354 | Production availability triggers launch | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-355 | Launch triggers marketing | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-356 | Marketing creates campaign | ❌ FAIL | [OFFLINE] LiteLLM: Offline across mesh (Port 4000) |
| CONN-357 | Campaign creates landing page | ❌ FAIL | [OFFLINE] LiteLLM: Offline across mesh (Port 4000) |
| CONN-358 | Landing page creates lead | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-359 | Lead enters CRM | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-360 | CRM assigns owner | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-361 | Lead enters sales workflow | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-362 | SDR receives lead | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-363 | SDR qualifies lead | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-364 | Qualified lead reaches AE | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-365 | AE receives product positioning | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-366 | AE receives pricing | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-367 | AE receives proposal tools | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-368 | Proposal reaches prospect | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-369 | Prospect response reaches CRM | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-370 | Closed deal reaches Finance | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-371 | Payment reaches Finance | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-372 | Customer record reaches Customer Success | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-373 | Customer reaches onboarding | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-374 | Onboarding reaches product usage | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-375 | Revenue can be traced to the original product release | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-376 | Customer creates account | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-377 | Account creates customer record | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-378 | Customer record connects to product | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-379 | Product records usage | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-380 | Usage reaches analytics | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-381 | Analytics reaches Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-382 | Customer feedback reaches Product | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-383 | Support ticket reaches Support | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-384 | Support ticket connects to customer | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-385 | Support ticket connects to product | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-386 | Support ticket connects to feature | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-387 | Support ticket connects to bug | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-388 | Bug connects to engineering | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-389 | Feature request connects to roadmap | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-390 | Churn connects to customer success | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-391 | Churn connects to Product | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-392 | Renewal connects to Revenue | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-393 | Expansion connects to Sales | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-394 | Usage connects to customer health | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-395 | Customer health connects to CSM | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-396 | Customer success outcome connects to product value | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-397 | Product value connects to retention | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-398 | Retention connects to revenue | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-399 | Customer insight creates product improvement | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-400 | Customer lifecycle is fully traceable | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-401 | Product connects to pricing | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-402 | Pricing connects to billing | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-403 | Billing connects to payment | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-404 | Payment connects to accounting | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-405 | Accounting connects to revenue | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-406 | Revenue connects to product | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-407 | Revenue connects to customer | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-408 | Revenue connects to salesperson | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-409 | Revenue connects to marketing campaign | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-410 | Revenue connects to acquisition source | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-411 | Revenue connects to venture | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-412 | Revenue connects to product | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-413 | Cost connects to product | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-414 | Infrastructure cost connects to product | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-415 | AI/model cost connects to product | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-416 | Employee cost connects to department | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-417 | Vendor cost connects to workflow | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-418 | Gross margin connects to product | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-419 | CAC connects to marketing | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-420 | LTV connects to customer success | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-421 | ROI connects to product | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-422 | Cash flow connects to CFO | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-423 | Financial performance connects to CEO | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-424 | Capital allocation connects to portfolio | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-425 | Product economics can be reconstructed end-to-end | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-426 | Role has documented workflows | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-427 | Workflow has trigger | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-428 | Workflow has inputs | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-429 | Workflow has tasks | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-430 | Tasks have owners | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-431 | Tasks have tools | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-432 | Tasks have agents | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-433 | Tasks have outputs | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-434 | Outputs have validators | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-435 | Workflow has decision gates | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-436 | Workflow has exception paths | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-437 | Workflow has escalation paths | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-438 | Workflow has SLA | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-439 | Workflow has KPI | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-440 | Workflow has audit log | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-441 | Workflow has retry logic | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-442 | Workflow has failure handling | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-443 | Workflow has human override | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-444 | Workflow has completion criteria | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-445 | Workflow connects to department | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-446 | Workflow connects to role | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-447 | Workflow connects to venture | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-448 | Workflow connects to revenue | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-449 | Workflow connects to customer outcome | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-450 | Workflow can be executed from start to finish | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-451 | Company connects to ventures | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-452 | Venture connects to products | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-453 | Product connects to features | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-454 | Feature connects to requirements | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-455 | Requirement connects to roles | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-456 | Role connects to people | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-457 | People connect to departments | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-458 | Department connects to workflows | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-459 | Workflow connects to tools | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-460 | Tools connect to MCPs | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-461 | MCPs connect to agents | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-462 | Agents connect to models | ❌ FAIL | [OFFLINE] OmniRoute: Offline across mesh (Port 20128) |
| CONN-463 | Models connect to infrastructure | ❌ FAIL | [OFFLINE] LiteLLM: Offline across mesh (Port 4000) |
| CONN-464 | Infrastructure connects to repositories | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-465 | Repositories connect to capabilities | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-466 | Capabilities connect to ventures | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-467 | Customers connect to products | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-468 | Customers connect to revenue | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-469 | Revenue connects to ventures | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-470 | Ventures connect to strategy | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-471 | Strategy connects to objectives | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-472 | Objectives connect to KPIs | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-473 | KPIs connect to data | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-474 | Data connects back to decisions | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-475 | No critical node exists as an orphan | ❌ FAIL | [OFFLINE] Neo4j: Offline across mesh (Port 7474) |
| CONN-476 | Idea → CEO → Product → Research | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-477 | Research → Strategy → Business Case | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-478 | Business Case → Finance → Approval | ✅ PASS | [PHYSICAL] HTTP 200 OK from VEX Command Center |
| CONN-479 | Approval → Product → Requirements | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-480 | Requirements → Design → Prototype | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-481 | Prototype → UX Research → Approval | ❌ FAIL | [OFFLINE] Qdrant: Offline across mesh (Port 6333) |
| CONN-482 | Approved Design → Architecture | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-483 | Architecture → Engineering | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-484 | Engineering → Repository | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-485 | Repository → CI/CD | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-486 | CI/CD → QA | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-487 | QA → Security | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-488 | Security → Product Approval | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-489 | Product Approval → DevOps | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-490 | DevOps → Production | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-491 | Production → Marketing | ✅ PASS | [PHYSICAL] HTTP 200 OK from 6/6 Production Ventures |
| CONN-492 | Marketing → Lead | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-493 | Lead → Sales | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-494 | Sales → Customer | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-495 | Customer → Customer Success | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-496 | Customer Success → Usage | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-497 | Usage → Analytics | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-498 | Analytics → Product Improvement | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-499 | Product Improvement → New Requirements | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
| CONN-500 | New Requirements → Entire conveyor belt repeats | ❌ FAIL | [UNWIRED] No physical integration test wired yet |
