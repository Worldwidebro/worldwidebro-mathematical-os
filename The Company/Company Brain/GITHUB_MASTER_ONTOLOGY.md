---
type: infrastructure-control-ontology
canonical: true
authority: code-and-collaboration-plane
version: 1.0
updated_at: 2026-10-02T00:00:00Z
source_of_truth: true
---

# GITHUB_MASTER_ONTOLOGY v1.0 — Code & Collaboration Control Plane

**GitHub is not merely "where the code lives." It is simultaneously a repository system, collaboration platform, identity/access system, CI/CD automation, security layer, package registry, release system, and evidence source.**

This ontology models **[GITHUB]** as a first-class Company Brain control plane that provides implementation evidence and execution capability for the entire enterprise.

---

## Core Principle: Declared ≠ Observed ≠ Verified

```
[DECLARED_REPOSITORY_STATE]
        ≠
[OBSERVED_REPOSITORY_STATE]
        ≠
[VERIFIED_REPOSITORY_STATE]
```

Example:
- **Declared:** "This repo is deployed and live"
- **Observed:** GitHub workflow shows commit, build passed, deploy job ran
- **Verified:** HTTP 200 from production URL confirms actual running state

---

## [GITHUB_COMPLETE_ARCHITECTURE] — 18 Domains

```
[GITHUB]

├─ [IDENTITY]
│  ├── [GITHUB_ACCOUNT]
│  ├── [GITHUB_ORGANIZATION]
│  ├── [GITHUB_USER]
│  ├── [GITHUB_TEAM]
│  ├── [GITHUB_BOT]
│  ├── [GITHUB_APP]
│  └── [GITHUB_ACTION]
│
├─ [REPOSITORIES]
│  ├── [REPOSITORY]
│  ├── [PUBLIC_REPOSITORY]
│  ├── [PRIVATE_REPOSITORY]
│  ├── [FORK]
│  ├── [TEMPLATE_REPOSITORY]
│  ├── [ARCHIVED_REPOSITORY]
│  ├── [MONOREPO]
│  └── [MIRROR]
│
├─ [CODE]
│  ├── [SOURCE_CODE]
│  ├── [CONFIGURATION]
│  ├── [DOCUMENTATION]
│  ├── [SCHEMAS]
│  ├── [SCRIPTS]
│  ├── [INFRASTRUCTURE_CODE]
│  ├── [TESTS]
│  └── [GENERATED_CODE]
│
├─ [GIT]
│  ├── [COMMIT]
│  ├── [BRANCH]
│  ├── [TAG]
│  ├── [RELEASE]
│  ├── [MERGE]
│  ├── [REBASE]
│  ├── [DIFF]
│  ├── [HISTORY]
│  ├── [BLAME]
│  └── [WORKTREE]
│
├─ [PULL_REQUESTS]
│  ├── [PULL_REQUEST]
│  ├── [PR_REVIEW]
│  ├── [APPROVAL]
│  ├── [CHANGE_REQUEST]
│  ├── [MERGE]
│  └── [MERGE_CONFLICT]
│
├─ [ISSUES]
│  ├── [ISSUE]
│  ├── [BUG]
│  ├── [FEATURE_REQUEST]
│  ├── [TASK]
│  ├── [DISCUSSION]
│  ├── [ISSUE_LABEL]
│  ├── [MILESTONE]
│  └── [ISSUE_RELATIONSHIP]
│
├─ [PROJECTS]
│  ├── [GITHUB_PROJECT]
│  ├── [PROJECT_BOARD]
│  ├── [PROJECT_ITEM]
│  ├── [VIEW]
│  ├── [FIELD]
│  └── [PROJECT_AUTOMATION]
│
├─ [ACTIONS]
│  ├── [GITHUB_ACTIONS]
│  ├── [WORKFLOW]
│  ├── [WORKFLOW_RUN]
│  ├── [JOB]
│  ├── [STEP]
│  ├── [RUNNER]
│  ├── [SELF_HOSTED_RUNNER]
│  ├── [ARTIFACT]
│  ├── [CACHE]
│  └── [SCHEDULE]
│
├─ [CI_CD]
│  ├── [CONTINUOUS_INTEGRATION]
│  ├── [CONTINUOUS_DELIVERY]
│  ├── [CONTINUOUS_DEPLOYMENT]
│  ├── [BUILD]
│  ├── [TEST]
│  ├── [PACKAGE]
│  ├── [DEPLOY]
│  └── [ROLLBACK]
│
├─ [SECURITY]
│  ├── [CODE_SCANNING]
│  ├── [DEPENDABOT]
│  ├── [SECRET_SCANNING]
│  ├── [SECURITY_ADVISORY]
│  ├── [DEPENDENCY]
│  ├── [VULNERABILITY]
│  ├── [SECURITY_POLICY]
│  ├── [CODEOWNERS]
│  └── [BRANCH_PROTECTION]
│
├─ [ACCESS_CONTROL]
│  ├── [AUTHENTICATION]
│  ├── [AUTHORIZATION]
│  ├── [ROLE]
│  ├── [PERMISSION]
│  ├── [TEAM]
│  ├── [COLLABORATOR]
│  ├── [DEPLOY_KEY]
│  ├── [PERSONAL_ACCESS_TOKEN]
│  ├── [SSH_KEY]
│  ├── [GITHUB_APP]
│  └── [OIDC]
│
├─ [PACKAGES]
│  ├── [GITHUB_PACKAGES]
│  ├── [CONTAINER_IMAGE]
│  ├── [NPM_PACKAGE]
│  ├── [MAVEN_PACKAGE]
│  ├── [RUBYGEMS]
│  ├── [PYTHON_PACKAGE]
│  └── [PACKAGE_VERSION]
│
├─ [RELEASES]
│  ├── [RELEASE]
│  ├── [VERSION]
│  ├── [TAG]
│  ├── [RELEASE_NOTES]
│  ├── [BINARY]
│  └── [RELEASE_ARTIFACT]
│
├─ [COLLABORATION]
│  ├── [CODE_REVIEW]
│  ├── [DISCUSSION]
│  ├── [COMMENT]
│  ├── [MENTION]
│  ├── [NOTIFICATION]
│  └── [SUBSCRIPTION]
│
├─ [WEBHOOKS]
│  ├── [WEBHOOK]
│  ├── [EVENT]
│  ├── [PAYLOAD]
│  ├── [DELIVERY]
│  └── [EVENT_HANDLER]
│
├─ [INTEGRATIONS]
│  ├── [MCP]
│  ├── [GITHUB_API]
│  ├── [GITHUB_APP]
│  ├── [WEBHOOK]
│  ├── [OAUTH]
│  ├── [CLAUDE_CODE]
│  ├── [ANTIGRAVITY]]
│  ├── [CODEX]]
│  ├── [OMNIROUTE]]
│  └── [CI_CD_SYSTEM]
│
├─ [REPOSITORY_INTELLIGENCE]
│  ├── [REPOSITORY_DISCOVERY]
│  ├── [REPOSITORY_CLASSIFICATION]
│  ├── [REPOSITORY_INDEXING]
│  ├── [CAPABILITY_EXTRACTION]
│  ├── [DEPENDENCY_GRAPH]
│  ├── [CODE_GRAPH]
│  ├── [ENTITY_RESOLUTION]
│  ├── [VENTURE_MAPPING]
│  ├── [REPO_TO_REVENUE]
│  ├── [GAP_DETECTION]
│  └── [SYNERGY_DETECTION]
│
├─ [OBSERVABILITY]
│  ├── [WORKFLOW_LOG]
│  ├── [BUILD_LOG]
│  ├── [DEPLOYMENT_LOG]
│  ├── [AUDIT_LOG]
│  ├── [SECURITY_EVENT]
│  └── [TELEMETRY]
│
└─ [REALITY]
   ├── [REPOSITORY_EXISTS]
   ├── [CODE_EXISTS]
   ├── [BRANCH_EXISTS]
   ├── [COMMIT_EXISTS]
   ├── [WORKFLOW_EXISTS]
   ├── [BUILD_VERIFIED]
   ├── [TEST_VERIFIED]
   ├── [DEPLOYMENT_VERIFIED]
   ├── [DEPENDENCY_VERIFIED]
   └── [REPOSITORY_STATE]
```

---

## [REPOSITORY_AS_ENTITY] — Graph Model

Every repository is a first-class entity in the Company Brain graph:

```
[REPOSITORY]
│
├── [IDENTITY]
│   ├── [REPOSITORY_ID]
│   ├── [NAME]
│   ├── [GITHUB_URL]
│   └── [SLUG]
│
├── [OWNERSHIP]
│   ├── [OWNER]
│   ├── [ORGANIZATION]
│   ├── [MAINTAINER]
│   └── [CONTRIBUTORS]
│
├── [TECHNICAL]
│   ├── [LANGUAGES]
│   ├── [FRAMEWORKS]
│   ├── [DEPENDENCIES]
│   ├── [CAPABILITIES]
│   └── [INFRASTRUCTURE]
│
├── [BUSINESS]
│   ├── [VENTURE]
│   ├── [SECTOR]
│   ├── [OPCO]
│   ├── [PRODUCT]
│   └── [REVENUE_MODEL]
│
├── [CODE]
│   ├── [SOURCE_CODE]
│   ├── [TESTS]
│   ├── [DOCUMENTATION]
│   └── [INFRASTRUCTURE_CODE]
│
├── [EXECUTION]
│   ├── [ISSUES]
│   ├── [PULL_REQUESTS]
│   ├── [WORKFLOWS]
│   ├── [RELEASES]
│   └── [DEPLOYMENTS]
│
└── [STATE]
    ├── [REPOSITORY_STATE]
    ├── [HEALTH]
    ├── [ACTIVITY]
    └── [LAST_VERIFIED]
```

---

## [REPOSITORY_TO_REVENUE_GRAPH] — The Value Chain

```
[[REPOSITORY]]
      ↓
[[CAPABILITY]]
      ↓
[[VENTURE]]
      ↓
[[PRODUCT]]
      ↓
[[CUSTOMER]]
      ↓
[[TRANSACTION]]
      ↓
[[REVENUE]]
```

This connects code directly to business value.

---

## [PULL_REQUEST_EXECUTION_LOOP] — Complete Workflow

```
[REQUIREMENT]
      ↓
[ISSUE]
      ↓
[TASK]
      ↓
[BRANCH]
      ↓
[CODE_CHANGE]
      ↓
[COMMIT]
      ↓
[PULL_REQUEST]
      ↓
[CI_AUTOMATION]
      ├── [BUILD]
      ├── [TEST]
      └── [SECURITY_SCAN]
      ↓
[CODE_REVIEW]
      ├── [HUMAN_REVIEW]
      └── [APPROVAL]
      ↓
[MERGE]
      ↓
[DEPLOY]
      ↓
[VERIFICATION]
      ↓
[EVIDENCE]
      ↓
[REALITY]
```

---

## [GITHUB_ACTIONS_ONTOLOGY] — Automation & Evidence

```
[[GITHUB_ACTIONS]]
       ↓
[[WORKFLOW]]
       ├── [TRIGGER]
       │   ├── [PUSH]
       │   ├── [PULL_REQUEST]
       │   ├── [ISSUE]
       │   ├── [RELEASE]
       │   ├── [SCHEDULE]
       │   ├── [WEBHOOK]
       │   ├── [MANUAL_TRIGGER]
       │   └── [WORKFLOW_DISPATCH]
       ↓
[[JOB]]
       ↓
[[STEP]]
       ↓
[[RUNNER]]
       ↓
[[OUTPUT]]
       ↓
[[WORKFLOW_RUN]]
       ├── [QUEUED]
       ├── [IN_PROGRESS]
       ├── [SUCCESS]
       ├── [FAILURE]
       ├── [CANCELLED]
       └── [SKIPPED]
```

**Critical:** Workflow runs are EVIDENCE, not claims.

```
[[DEPLOYMENT_CLAIM]]
        ↓
[[GITHUB_WORKFLOW_RUN]]
        ↓
[[BUILD_LOGS]]
        ↓
[[TEST_RESULTS]]
        ↓
[[DEPLOYMENT_LOGS]]
        ↓
[[VERIFIED_DEPLOYMENT]]
```

---

## [REPOSITORY_STATE_MACHINE] — Canonical States

```
[REPOSITORY_STATE]

├── [UNKNOWN]           — Not yet discovered
├── [DISCOVERED]        — Found in GitHub
├── [INDEXED]           — Metadata extracted
├── [CLASSIFIED]        — Categorized
├── [MAPPED]            — Linked to ventures/capabilities
├── [ACTIVE]            — In development
├── [DEPLOYED]          — Live in production
├── [MAINTAINED]        — Regular updates
├── [STALE]             — No recent activity
├── [ABANDONED]         — Unmaintained
├── [ARCHIVED]          — Explicitly archived
├── [DEPRECATED]        — Marked for removal
└── [DELETED]           — Removed from GitHub
```

---

## [REPOSITORY_HEALTH] — Facts Over Scores

Instead of a single "health score," track observable facts:

```
[REPOSITORY_HEALTH]

├── [LAST_COMMIT]
│   └── timestamp
├── [OPEN_ISSUES]
│   └── count
├── [OPEN_PRS]
│   └── count
├── [FAILED_BUILDS]
│   └── count
├── [PASSING_TESTS]
│   └── percentage
├── [DEPENDENCY_STATUS]
│   ├── outdated
│   └── vulnerable
├── [SECURITY_ALERTS]
│   └── count
├── [DOCUMENTATION_STATUS]
│   └── [COMPLETE | PARTIAL | MISSING]
├── [DEPLOYMENT_STATUS]
│   └── [DEPLOYED | UNDEPLOYED]
├── [MAINTAINER_STATUS]
│   └── [ACTIVE | INACTIVE]
├── [ACTIVITY]
│   └── [HIGH | NORMAL | LOW | NONE]
└── [LAST_VERIFIED]
    └── timestamp
```

System determines state from evidence:

```
EVIDENCE
    ↓
ACTIVE = (LAST_COMMIT < 30 days) AND (OPEN_PRS > 0) AND (PASSING_TESTS > 80%)
STALE = (LAST_COMMIT > 90 days) AND (OPEN_ISSUES > 5)
BROKEN = (FAILED_BUILDS > 0) AND (PASSING_TESTS < 50%)
DEPLOYED = (DEPLOYMENT_STATUS = DEPLOYED) AND (HTTP_HEALTH_CHECK = 200)
```

---

## [GITHUB_SECURITY_ONTOLOGY] — Integration with Secrets & Auth

```
[[GITHUB_SECURITY]]
│
├── [[SECRET_SCANNING]]
│   └── [[CREDENTIAL_EXPOSURE_DETECTION]]
├── [[CODE_SCANNING]]
│   └── [[VULNERABILITY_DETECTION]]
├── [[DEPENDABOT]]
│   └── [[DEPENDENCY_UPDATES]]
├── [[DEPENDENCY_REVIEW]]
│   └── [[SUPPLY_CHAIN_SECURITY]]
├── [[SECURITY_ADVISORY]]
│   └── [[CVE_MANAGEMENT]]
├── [[CODEOWNERS]]
│   └── [[CODE_OWNERSHIP]]
├── [[BRANCH_PROTECTION]]
│   └── [[MERGE_ENFORCEMENT]]
├── [[RULESETS]]
│   └── [[GOVERNANCE_ENFORCEMENT]]
└── [[SECURITY_POLICY]]
    └── [[VULNERABILITY_DISCLOSURE]]
```

Connects to [[SECRETS_AND_AUTH]]:

```
[[GITHUB]]
   ↓
[[GITHUB_CREDENTIAL]]
   ↓
[[AUTHENTICATION]]
   ↓
[[GITHUB_TOKEN]]
   ↓
[[PERMISSION]]
   ↓
[[REPOSITORY_ACCESS]]
```

---

## [AGENT_ACCESS_TO_GITHUB] — Capability Model

Agents can consume GitHub as a capability substrate:

```
[[AGENT]]
 ├── [[READ_REPOSITORY]]
 ├── [[SEARCH_CODE]]
 ├── [[CREATE_BRANCH]]
 ├── [[EDIT_CODE]]
 ├── [[COMMIT]]
 ├── [[CREATE_PULL_REQUEST]]
 ├── [[REQUEST_REVIEW]]
 ├── [[READ_TEST_RESULTS]]
 ├── [[TRIGGER_WORKFLOW]]
 ├── [[READ_DEPLOYMENT_LOGS]]
 ├── [[CREATE_ISSUE]]
 ├── [[CREATE_DISCUSSION]]
 └── [[READ_EVIDENCE]]
```

Complete workflow:

```
[[CLAUDE_CODE]]
       ↓
[[GITHUB_API]]
       ↓
[[TASK]]
       ↓
[[CREATE_BRANCH]]
       ↓
[[EDIT_CODE]]
       ↓
[[COMMIT]]
       ↓
[[CREATE_PR]]
       ↓
[[GITHUB_ACTIONS]]
       ↓
[[TEST]]
       ↓
[[MERGE]]
       ↓
[[DEPLOY]]
       ↓
[[VERIFY]]
```

---

## [REPOSITORY_INTELLIGENCE_LOOP] — Discovery to Decision

```
[[GITHUB]]
      ↓
[[REPOSITORY_DISCOVERY]]
      ↓
[[REPOSITORY_REGISTRY]]
      ↓
[[REPOSITORY_CLASSIFICATION]]
      ├── Language
      ├── Framework
      ├── Purpose (library, tool, service, app, etc.)
      └── Status (active, stale, archived, etc.)
      ↓
[[CAPABILITY_EXTRACTION]]
      ├── Technical capabilities
      ├── Integration points
      ├── Dependencies
      └── Infrastructure requirements
      ↓
[[ENTITY_RESOLUTION]]
      ├── Author/owner identification
      ├── Team assignment
      ├── Cross-reference with other systems
      └── Duplicate detection
      ↓
[[BUSINESS_MAPPING]]
      ├── Venture mapping
      ├── Sector assignment
      ├── Product assignment
      ├── Revenue model
      └── OPCO assignment
      ↓
[[DEPENDENCY_ANALYSIS]]
      ├── Internal dependencies
      ├── External dependencies
      ├── Supply chain risk
      └── Update requirements
      ↓
[[GAP_DETECTION]]
      ├── Missing functionality
      ├── Unaddressed capabilities
      ├── Overlapping features
      └── Redundancy detection
      ↓
[[SYNERGY_ANALYSIS]]
      ├── Integration opportunities
      ├── Reuse potential
      ├── Composition opportunities
      └── Cross-venture value
      ↓
[[REPO_TO_REVENUE]]
      └── Connect repository to revenue impact
      ↓
[[DECISION]]
      ├── Build/buy/integrate/skip decision
      ├── Resource allocation
      └── Priority ranking
```

---

## [GITHUB_EVIDENCE_TYPES] — What Counts as Proof

```
[[GITHUB_EVIDENCE]]

├── [[COMMIT]]
│   └── Code change with timestamp and author
├── [[PULL_REQUEST]]
│   └── Change review and approval record
├── [[WORKFLOW_RUN]]
│   └── Automated test/build execution log
├── [[TEST_RESULT]]
│   └── Test pass/fail evidence
├── [[SECURITY_SCAN]]
│   └── Vulnerability detection results
├── [[BUILD_LOG]]
│   └── Build success/failure evidence
├── [[DEPLOYMENT_LOG]]
│   └── Deployment execution evidence
├── [[RELEASE]]
│   └── Version release evidence
├── [[CODE_OWNERSHIP]]
│   └── CODEOWNERS file evidence
└── [[BRANCH_PROTECTION]]
    └── Governance enforcement evidence
```

---

## [REALITY_VERIFICATION_LOOP] — No Fake Completion

```
CLAIM
    ↓ (Agent says: "Deployed")
GITHUB_EVIDENCE
    ↓ (Check: Is there a workflow run?)
OBSERVATION
    ↓ (Check: Did it succeed?)
VERIFICATION
    ↓ (Check: HTTP 200 from production URL)
REALITY
    ↓
KNOWLEDGE_GRAPH
    ↓
NEXT_DECISION
```

Example failure:

```
CLAIM: "Feature X is live"
GITHUB_CHECK: Workflow shows "failed"
OBSERVATION: Build failed in CI
REALITY: Feature NOT deployed
ACTION: Alert and investigate
```

---

## [GITHUB_REALITY] — Source of Truth

```
[GITHUB_REALITY]

├── [REPOSITORY_EXISTS]
│   ├── Name, URL, visibility verified
│   └── Last checked: <timestamp>
├── [CODE_EXISTS]
│   ├── Latest commit hash verified
│   └── Last checked: <timestamp>
├── [BRANCH_EXISTS]
│   ├── Branch name, head commit verified
│   └── Last checked: <timestamp>
├── [WORKFLOW_EXISTS]
│   ├── Workflow file path verified
│   └── Last checked: <timestamp>
├── [WORKFLOW_RUN_VERIFIED]
│   ├── Most recent run checked
│   ├── Status verified (success/failure)
│   └── Last checked: <timestamp>
├── [BUILD_VERIFIED]
│   ├── Artifacts present
│   ├── Build logs available
│   └── Last checked: <timestamp>
├── [TESTS_VERIFIED]
│   ├── Test count
│   ├── Pass rate
│   └── Last checked: <timestamp>
├── [DEPLOYMENT_VERIFIED]
│   ├── Deployment environment
│   ├── Version deployed
│   └── Last checked: <timestamp>
└── [SECURITY_VERIFIED]
    ├── Secret scan status
    ├── Vulnerabilities count
    └── Last checked: <timestamp>
```

---

## [GITHUB_CLAUDE_INTEGRATION] — Unified System

```
[[CLAUDE_CODE]]
      │
      ├── [[MCP]]
      │    └── [[GITHUB_API]]
      │
      └── [[OMNIROUTE]]
           └── [[MODEL_SELECTION]]
                ↓
           [[REASONING]]
                ↓
           [[CODE_GENERATION]]
                ↓
           [[GITHUB]]
                ├── Create branch
                ├── Edit files
                ├── Commit
                ├── Push
                ├── Create PR
                └── Read verification
                ↓
           [[GITHUB_ACTIONS]]
                ├── Test
                ├── Build
                ├── Deploy
                └── Verify
                ↓
           [[EVIDENCE]]
                ↓
           [[KNOWLEDGE_GRAPH]]
                ↓
           [[NEXT_TASK]]
```

---

## [COMPANY_BRAIN_GITHUB_INTEGRATION] — Master Connection

```
                         [[WHOAMI]]
                             │
                             ↓
                       [[COMPANY_BRAIN]]
                             │
                ┌────────────┴────────────┐
                ↓                         ↓
          [[KNOWLEDGE]]               [[INTENT]]
          (Obsidian)              (Objectives)
                │                         │
        [[WIKI_LINKS]]             [[REQUIREMENTS]]
                │                         │
                └──────────┬──────────────┘
                           ↓
                      [[GITHUB]]
                           │
              ┌────────────┼────────────┐
              ↓            ↓            ↓
        [[REPOSITORY]] [[ISSUE]]  [[PULL_REQUEST]]
              │            │            │
              ↓            ↓            ↓
         [[CODE]]       [[TASK]]    [[REVIEW]]
              │                         │
              └────────────┬────────────┘
                           ↓
                    [[GITHUB_ACTIONS]]
                           ↓
              ┌────────────┼────────────┐
              ↓            ↓            ↓
          [[BUILD]]     [[TEST]]   [[SECURITY]]
              │            │            │
              └────────────┼────────────┘
                           ↓
                     [[DEPLOYMENT]]
                           ↓
                  [[VERIFICATION]]
                           ↓
                       [[EVIDENCE]]
                           ↓
                      [[REALITY]]
                           │
                           ↓
                  [[KNOWLEDGE_GRAPH]]
                           │
                           ↓
                    [[CLAUDE_CODE]]
                           │
                           ↓
                      [[OMNIROUTE]]
                           │
                           ↓
                       [[MODEL]]
                           │
                           ↓
                      [[AGENT]]
                           │
                           ↓
                    [[AGENT_TASK]]
                           │
                           ↓
                       [[ACTION]]
                           │
                           ↓
                       [[OUTCOME]]
                           │
                           └──────→ [[GITHUB]]
                                     ↺
```

---

## [CRITICAL_ARCHITECTURAL_SEPARATION]

```
[[OBSIDIAN]]
    = HUMAN KNOWLEDGE / CONTEXT / INTENT

[[GITHUB]]
    = CODE / VERSION / COLLABORATION / AUTOMATION / EVIDENCE

[[NEO4J]]
    = RELATIONSHIP GRAPH

[[QDRANT]]
    = SEMANTIC RETRIEVAL

[[OMNIROUTE]]
    = MODEL / PROVIDER ROUTING

[[CLAUDE]]
    = INTELLIGENCE / REASONING / EXECUTION INTERFACE

[[COMPANY_BRAIN]]
    = ORCHESTRATION / DECISION / KNOWLEDGE / EXECUTION

[[REALITY]]
    = VERIFIED STATE (GitHub workflows, HTTP checks, tests)
```

Each layer has explicit boundaries and responsibility.

---

**Related:** [[WHOAMI.md]] · [[WHERE_WE_ARE.md]] · [[DATA_FLOW.md]] · [[INFRASTRUCTURE.md]] · [[CROSS_LINK_MASTER_ONTOLOGY.md]] · [[OMNIROUTE_MASTER_ONTOLOGY.md]] · [[SECRETS_AND_AUTH_MASTER_ONTOLOGY.md]]

**Code & collaboration control plane v1.0: GitHub as first-class Company Brain entity with repository intelligence, execution evidence, and complete agent integration.**

