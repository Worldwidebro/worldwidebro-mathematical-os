[[STARTHERE]] | [[REALITY]] | [[01-IDENTITY|Identity Career Graph]] | [[INDEX]]

# WHO I AM: Career Graph & Intelligent Resume

**Status:** Building (2026-09-11)  
**Purpose:** Queryable career identity that understands your highest capabilities  
**Format:** Neo4j schema + Obsidian notes + Portfolio links

---

## PART 1: COMPLETE YOUR BACKGROUND

Answer these to populate your career graph. Fill in only what's accurate; leave blank what you don't want to share.

### SECTION A: Core Identity

```yaml
whoiam:
  preferred_name: ""  # What do you go by?
  current_title: ""   # Your current role
  years_experience: ""  # Total years in tech/business
  
  location:
    primary: ""       # Where you are now
    open_to: []       # NYC, remote, specific regions?
    
  mission_statement: ""  # In one sentence: why do you do this?
  
  examples:
    title: "Infrastructure & AI Systems Architect"
    experience: "12+ years"
    location: "Remote, NYC timezone"
    mission: "Build distributed systems that enable AI at scale"
```

### SECTION B: Employment History

```yaml
employment:
  - company: ""
    title: ""
    years: "2024-present"  # or "2024-2026"
    key_achievements:
      - ""  # Quantified if possible
      - ""
    technologies_used: []
    team_size_led: 0
    revenue_impact: ""  # "$X revenue", "reduced costs by Y%"
    
  - company: ""
    title: ""
    years: ""
    key_achievements: []
    technologies_used: []
    team_size_led: 0
    revenue_impact: ""

# Example structure:
  - company: "Worldwidebro Holdings"
    title: "Infrastructure Architect"
    years: "2024-present"
    key_achievements:
      - "Built distributed AI infrastructure across 2 machines (Air + Studio)"
      - "Designed 22-stage cognitive pipeline for 789 ventures"
      - "Established Neo4j knowledge graph with 20K+ edges"
    technologies_used: ["Neo4j", "Qdrant", "Ollama", "Docker", "Tailscale"]
    team_size_led: 0  # Self-driven
    revenue_impact: ""  # TBD - building revenue loops
```

### SECTION C: Education & Credentials

```yaml
education:
  - degree: ""  # BS, MS, PhD
    field: ""   # Computer Science, Mathematics, etc.
    school: ""
    graduation_year: 0
    gpa: 0.0
    
certifications:
  - name: ""
    issuer: ""
    year: 0
    
technical_credentials:
  - area: ""
  - area: ""
```

### SECTION D: Skills Hierarchy (Rate 1-10)

```yaml
technical_skills:
  infrastructure:
    kubernetes: 0     # 1-10, be honest
    docker: 0
    cloud_platforms: 0  # AWS/GCP/Azure
    networking: 0
    databases: 0
    
  ai_ml:
    llms: 0           # Working with LLMs
    embeddings: 0     # Vector DBs, retrieval
    model_serving: 0  # Ollama, inference
    prompt_engineering: 0
    
  backend:
    python: 0
    go: 0
    rust: 0
    system_design: 0
    
  leadership:
    team_building: 0
    strategic_planning: 0
    execution: 0
    decision_making: 0

soft_skills:
  communication: 0
  learning_velocity: 0
  problem_solving: 0
  autonomy: 0
```

### SECTION E: Open Source & Portfolio

```yaml
portfolio:
  github_username: ""
  
  repositories:
    - name: ""
      url: ""
      description: ""
      stars: 0
      language: ""
      
  writing:
    - title: ""
      url: ""
      topic: ""
      
  speaking:
    - title: ""
      conference: ""
      year: 0
      url: ""
```

### SECTION F: What You're Looking For

```yaml
desired_roles:
  - "CTO"
  - "VP Engineering"
  - "Principal Engineer"
  
target_companies:
  - name: ""
    why: ""
    stage: "seed/growth/scale"
    sector: ""
    
target_compensation:
  salary_min: 0
  salary_max: 0
  equity_range: "0.5-2%"
  
constraints:
  - ""  # e.g., "must be remote", "no travel"
  
nice_to_haves:
  - ""  # e.g., "equity upside", "technical founding"
```

---

## PART 2: Your Skills Mapped to Neo4j

Once you complete Part 1, this schema will be built:

```cypher
# YOU
CREATE (you:Person {
  name: "Your Name",
  title: "Current Role",
  bio: "Your mission statement",
  years_experience: 12,
  preferred_role: ["CTO", "VP Eng", "Principal Engineer"],
  open_to_equity: true
})

# SKILLS with proof
CREATE (skill1:Skill {
  name: "AI Systems Architecture",
  level: 9,  # 1-10
  verified_by: ["Company Brain", "Ollama integration", "Neo4j design"],
  proof: ["Built 22-stage AI pipeline", "Integrated 3 LLM systems"]
})

CREATE (skill2:Skill {
  name: "Distributed Infrastructure",
  level: 9,
  verified_by: ["Air-Studio setup", "Tailscale network", "T7 Shield"]
})

# LINK YOU TO SKILLS
CREATE (you)-[:HAS_SKILL {
  level: 9,
  years: 8,
  most_recent_use: "2026-09-11",
  proof: "Built Company Brain infrastructure"
}]->(skill1)

# ACHIEVEMENTS with impact
CREATE (achievement1:Achievement {
  title: "Built distributed AI infrastructure",
  impact: "Enables 789 ventures to access local inference",
  metric: "20K+ Neo4j edges, 17K vectors, 3 inference systems",
  date: "2026-09-11"
})

CREATE (you)-[:ACHIEVED]->(achievement1)

# TARGET COMPANIES
CREATE (company1:Company {
  name: "Anthropic",
  sector: "AI Safety",
  stage: "scale",
  why_interested: "Building safe AI infrastructure at scale",
  match_score: null  # Calculated when you apply
})

CREATE (you)-[:INTERESTED_IN]->(company1)

# TARGET ROLES
CREATE (role1:Role {
  title: "Principal Infrastructure Engineer",
  company: "Anthropic",
  required_skills: ["distributed systems", "AI inference", "infrastructure"],
  compensation: 350000,
  equity: 0.1
})

CREATE (role1)-[:REQUIRES]->(skill1)
CREATE (role1)-[:REQUIRES]->(skill2)
```

---

## PART 3: Your Queryable Resume

Once the graph is built, you can ask these questions:

```cypher
# QUESTION 1: What am I actually good at?
MATCH (you:Person)-[r:HAS_SKILL]->(skill:Skill)
WHERE r.level >= 8
RETURN skill.name, r.level, skill.verified_by
ORDER BY r.level DESC

# QUESTION 2: Which roles should I prioritize?
MATCH (you:Person)-[:HAS_SKILL]->(skill)
WITH skill
MATCH (role:Role)-[:REQUIRES]->(skill)
RETURN role.company, role.title, COUNT(skill) as matched_skills
ORDER BY matched_skills DESC

# QUESTION 3: What's my unique combination of skills?
MATCH (you:Person)-[:HAS_SKILL]->(skill)
RETURN COLLECT(skill.name) as my_skills
# Shows: intersection of what makes YOU unique (not just "I know Python")

# QUESTION 4: What should I emphasize for [Company]?
MATCH (company:Company {name: "Anthropic"})-[:HIRING_FOR]->(role)
-[:REQUIRES]->(required_skill)
WITH COLLECT(required_skill) as needed
MATCH (you:Person)-[:HAS_SKILL]->(your_skill)
WHERE your_skill IN needed
RETURN your_skill.name, your_skill.level, 
       "MATCH" as status

# QUESTION 5: What's missing from my profile?
MATCH (role:Role {company: "Anthropic"})-[:REQUIRES]->(needed:Skill)
WITH COLLECT(needed) as needed_skills
MATCH (you:Person)-[:HAS_SKILL]->(have:Skill)
WITH needed_skills, COLLECT(have) as my_skills
UNWIND needed_skills as need
WHERE need NOT IN my_skills
RETURN need.name as gap

# QUESTION 6: Generate tailored cover letter keywords
MATCH (you:Person {company: "Anthropic"})-[:HAS_SKILL]->(matching_skill)
MATCH (matching_skill)-[:RELATED_TO]->(industry_keyword)
RETURN COLLECT(matching_skill.name) + COLLECT(industry_keyword.name) 
       as talking_points
```

---

## PART 4: Your Portfolio (Linked to Skills)

```yaml
portfolio_items:
  - title: "Company Brain Infrastructure"
    url: "https://github.com/worldwidebro/company-brain"
    demonstrates:
      - skill: "Distributed Systems Architecture"
        evidence: "Air + Studio + T7 Shield coordination"
      - skill: "AI Systems Integration"
        evidence: "Neo4j + Qdrant + Ollama + OmniRoute"
      - skill: "Knowledge Graph Design"
        evidence: "20,363 edges, 22-stage pipeline"
    metrics: "789 ventures, 35 sectors, 50 domains"
    
  - title: "Storage & Connectivity System"
    url: "github.com/.../storage-relationships-map"
    demonstrates:
      - skill: "Infrastructure Engineering"
      - skill: "System Design"
      - skill: "Cross-Machine Orchestration"
    metrics: "1.8TB distributed storage, <50ms latency"
    
  - title: "Knowledge Graph Harness"
    url: "github.com/.../knowledge-graph-harness"
    demonstrates:
      - skill: "AI Architecture"
      - skill: "Self-Organizing Systems"
      - skill: "Executive Function"
    metrics: "Feedback loop enables self-improvement"
```

---

## PART 5: The Resume Generator

Once you complete Part 1-4, this tool generates:

```bash
# GENERATE RESUME FOR: Anthropic Principal Engineer role
python generate_resume.py \
  --target_company "Anthropic" \
  --target_role "Principal Infrastructure Engineer" \
  --output_format "cover_letter"

# Output: 
# - Personalized cover letter (emphasizing distributed AI systems)
# - Relevant achievements (showing proof of scale)
# - Technical keywords (matched to job description)
# - Portfolio links (showing real work)
```

---

## NEXT STEPS (DO THIS NOW)

1. **Fill in SECTION A-F above** (30 minutes)
   - Be specific and honest
   - Quantify everything you can
   - Include proof (links, dates, names)

2. **I'll build your Neo4j graph** (30 minutes)
   - Create all nodes
   - Link skills to achievements
   - Connect to target companies/roles

3. **We'll query it** (15 minutes)
   - "What am I actually good at?"
   - "Which companies should I target?"
   - "What should I emphasize?"

4. **Generate your resume** (10 minutes)
   - Personalized for each application
   - Optimized cover letters
   - Talking points matched to the role

5. **Start applying** (This week)
   - Neo4j ranks opportunities by fit
   - Ollama generates tailored letters
   - We track outcomes and learn

---

## THE OUTCOME

Instead of: Generic resume, same cover letter for everyone  
You get: **Intelligent career system that knows exactly why you're a fit**

Query: "Apply to Anthropic"
System returns:
- Why you match (distributed systems + AI infrastructure)
- What to emphasize (your unique infrastructure vision)
- Portfolio proof (Company Brain, 789 ventures)
- Conversation starters (specific challenges you've solved)

---

## Fill in below and we'll start building:

```yaml
# YOUR INFORMATION (Replace with your actual details)

identity:
  name: ""
  current_title: ""
  experience_years: ""
  location: ""
  
employment_history:
  current:
    company: ""
    title: ""
    start_year: 0
    
  previous:
    - company: ""
      title: ""
      years: "YYYY-YYYY"
    - company: ""
      title: ""
      years: "YYYY-YYYY"
      
top_5_skills:
  - name: ""
    level: 1-10
    proof: ""
  - name: ""
    level: 1-10
    proof: ""
    
target_roles:
  - company: ""
    role: ""
    compensation: ""
    
target_compensation:
  min: ""
  max: ""
  equity: ""
```

---

**Ready to build your career intelligence system?**

Share your information above and I'll:
1. Create your Neo4j career graph
2. Build Obsidian notes linking to it
3. Set up resume generation
4. Start optimizing your applications

