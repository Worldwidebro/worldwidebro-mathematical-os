---
name: skill-relationships
description: VEX skill graph — competencies, training, certification, proficiency
metadata:
  type: reference
  version: 1.0
  status: active
  last_updated: 2026-08-07
---

# Skills & Competency Graph

## SKILL

```yaml
SKILL
  ├── REQUIRED_FOR → CAPABILITY
  ├── REQUIRED_FOR → ROLE
  ├── TAUGHT_IN → COURSE
  ├── PRACTICED_IN → VENTURE
  ├── MEASURED_BY → COMPETENCY_SCORE
  ├── DEPENDS_ON → SKILL (prerequisites)
  ├── CERTIFIES → CERTIFICATION
  └── LEVEL → (beginner|intermediate|advanced|expert)
```

Properties: `id`, `name`, `category`, `description`, `proficiency_required`, `last_updated`, `difficulty_level`

## COMPETENCY_SCORE

```yaml
COMPETENCY_SCORE
  ├── MEASURES → SKILL
  ├── ACHIEVED_BY → PERSON
  ├── CERTIFIED_BY → CERTIFICATION|EXECUTIVE
  ├── SCORE → (0-100)
  ├── VERIFIED_AT → DATE
  ├── EXPIRES_AT → DATE (NULL = permanent)
  └── EVIDENCE → LINK[]
```

Properties: `id`, `person_id`, `skill_id`, `score`, `verified_date`, `expiration_date`, `verified_by`

## COURSE

```yaml
COURSE
  ├── TEACHES → SKILL[]
  ├── REQUIRED_FOR → CERTIFICATION
  ├── DURATION → HOURS
  ├── DIFFICULTY → LEVEL
  ├── COMPLETION_RATE → PERCENT
  ├── INSTRUCTOR → PERSON|SYSTEM
  └── PLATFORM → LEARNING_SYSTEM
```

Properties: `id`, `name`, `description`, `platform`, `duration_hours`, `instructor`, `completion_required_percent`

## CERTIFICATION

```yaml
CERTIFICATION
  ├── REQUIRES_SKILL → SKILL[]
  ├── REQUIRES_COURSE → COURSE
  ├── REQUIRED_FOR → ROLE|CAPABILITY
  ├── AWARDED_BY → EXECUTIVE|SYSTEM
  ├── VALIDITY_PERIOD → MONTHS
  ├── RENEWAL_REQUIRED → BOOLEAN
  └── EXAM_REQUIRED → BOOLEAN
```

Properties: `id`, `name`, `issuing_body`, `validity_months`, `renewal_required`, `exam_required`

## PERSON_SKILL

```yaml
PERSON_SKILL
  ├── PERSON → PERSON
  ├── SKILL → SKILL
  ├── PROFICIENCY_LEVEL → (1-5)
  ├── YEARS_OF_EXPERIENCE → NUMBER
  ├── LAST_PRACTICED → DATE
  ├── LAST_VERIFIED → DATE
  ├── CERTIFICATION → CERTIFICATION
  └── VERIFIED_BY → EXECUTIVE|SYSTEM
```

Properties: `person_id`, `skill_id`, `proficiency_level`, `years_experience`, `last_practiced_date`, `verified_date`

## Skill Dependency Tree

```
CAPABILITY (Payment Processing)
  ├── REQUIRES_SKILL: Stripe API Integration (expert)
  ├── REQUIRES_SKILL: Error Handling (advanced)
  ├── REQUIRES_SKILL: Security Best Practices (advanced)
  └── REQUIRES_SKILL: Testing & QA (intermediate)

                 ↓
            
SKILL (Stripe API Integration)
  ├── DEPENDS_ON: REST API Design (prerequisite)
  ├── DEPENDS_ON: Authentication/OAuth (prerequisite)
  ├── TAUGHT_IN: Stripe Developer Course
  ├── PRACTICED_IN: CON-001, FIN-037
  └── MEASURED_BY: COMPETENCY_SCORE

                 ↓
            
COURSE (Stripe Developer Course)
  ├── DURATION: 8 hours
  ├── TEACHES: Stripe API Integration
  ├── TEACHES: Webhook Handling
  ├── TEACHES: Idempotency
  └── COMPLETION_REQUIRED: 100%

                 ↓
            
CERTIFICATION (Stripe Developer Certified)
  ├── REQUIRES_SKILL: Stripe API Integration
  ├── REQUIRES_COURSE: Stripe Developer Course
  ├── REQUIRED_FOR: Role (Payment Systems Engineer)
  └── VALIDITY_PERIOD: 12 months
```

## Proficiency Levels

| Level | Score | What You Can Do |
|-------|-------|-----------------|
| 1 | 0-20 | Aware of concept, cannot apply |
| 2 | 21-40 | Can apply with guidance |
| 3 | 41-60 | Can apply independently |
| 4 | 61-80 | Can teach others |
| 5 | 81-100 | Expert, can architect solutions |

## Skill Categories

```
Technical Skills
├── Backend Development
├── Frontend Development
├── DevOps & Infrastructure
├── Data Engineering
├── AI/ML Engineering
└── Security

Business Skills
├── Product Management
├── Sales & Marketing
├── Finance & Accounting
├── Operations
└── Strategy

Soft Skills
├── Leadership
├── Communication
├── Problem Solving
├── Collaboration
└── Adaptability
```

## Temporal Properties

Every skill assignment includes:
- `acquired_date` (when person first achieved this skill)
- `verified_date` (when last verified/tested)
- `proficiency_level` (0-5)
- `expiration_date` (NULL = no expiration; some certs expire)
