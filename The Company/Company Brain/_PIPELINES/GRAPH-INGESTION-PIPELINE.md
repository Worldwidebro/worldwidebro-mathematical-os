# Graph Ingestion Pipeline

**Document ID:** INGESTION-PIPELINE-001  
**Updated:** 2026-09-17  
**Purpose:** Convert Markdown wiki + XML ontology → RDF triples → Neo4j  
**Authority:** CP-045 (Graph Logic)

---

## Overview

The Company Brain ingestion pipeline converts knowledge from multiple sources into a unified, queryable knowledge graph.

```
┌─────────────────────────────────────────────────────────────────┐
│                        DATA SOURCES                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  GitHub Repos     Markdown Wiki     XML Ontology   Databases   │
│  ClickUp Tasks    Agent Logs        APIs            Emails     │
│  Evaluation       Decision Records  Events         Metrics     │
│                                                                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│              ENTITY EXTRACTION & NORMALIZATION                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  - Parse frontmatter (id, type, wiki)                           │
│  - Extract typed wikilinks (relationship::[[target]])           │
│  - Normalize entity IDs and names                               │
│  - Resolve cross-references                                    │
│                                                                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│             RELATIONSHIP EXTRACTION & MAPPING                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  - Extract predicates from typed wikilinks                      │
│  - Map to ontology relationship types                           │
│  - Validate predicate semantics                                 │
│  - Apply domain/range constraints                               │
│                                                                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│           RDF TRIPLE GENERATION & VALIDATION                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  - Create RDF triples (subject, predicate, object)              │
│  - Attach provenance metadata                                   │
│  - Validate against ontology schema                             │
│  - Handle conflicts and duplicates                              │
│                                                                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                   NEO4J INGESTION                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  - Create nodes from entities                                   │
│  - Create edges from triples                                    │
│  - Index for performance                                        │
│  - Enable graph traversal                                       │
│                                                                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│               SEMANTIC INDEXING (QDRANT)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  - Embed entity descriptions                                    │
│  - Embed relationship context                                   │
│  - Enable semantic search for agents                            │
│                                                                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                   AGENT RETRIEVAL & ACTION                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  - Agents query graph for knowledge                             │
│  - Agents traverse relationships                                │
│  - Agents execute decisions based on logic                      │
│  - Agents produce new events/results                            │
│                                                                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                 GRAPH UPDATES & FEEDBACK                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  - New facts from agent execution                               │
│  - State changes                                                │
│  - Evaluation results                                           │
│  - Loop back to enrichment                                      │
│                                                                 │
└────────────────────┴────────────────────────────────────────────┘
```

---

## Stage 1: Entity Extraction

### Input: Markdown File

```markdown
---
id: logic-006
type: logic-layer
name: Revenue Logic
layer-number: 6
domain: domain-business
control-plane: cp-006
wiki: [[30-REVENUE/REVENUE-LOOPS.md]]
---

# Logic-006: Revenue Logic

**Core Question:** How do we turn activity into revenue?

belongs-to-domain::[[Business Domain]]
governed-by-control-plane::[[CP-006]]
governs::[[Agent: Revenue Loop Agent]]
```

### Extraction

```python
def extract_entity(markdown_file):
    # Parse frontmatter
    frontmatter = yaml.safe_load(markdown_file.split('---')[1])
    
    # Extract core attributes
    entity = {
        'id': frontmatter['id'],
        'type': frontmatter['type'],
        'name': frontmatter['name'],
        'wiki': frontmatter.get('wiki'),
        'created_at': now(),
        'provenance': {
            'source': markdown_file.path,
            'imported_by': 'markdown-ingester',
            'confidence': 0.95
        }
    }
    
    return entity

# Output
entity = {
    'id': 'logic-006',
    'type': 'logic-layer',
    'name': 'Revenue Logic',
    'wiki': '[[30-REVENUE/REVENUE-LOOPS.md]]',
    'provenance': {...}
}
```

---

## Stage 2: Relationship Extraction

### Input: Typed Wikilinks from Markdown Body

```markdown
belongs-to-domain::[[Business Domain]]
governed-by-control-plane::[[CP-006]]
governs::[[Agent: Revenue Loop Agent]]
constrained-by-policy::[[Policy: GAAP Revenue Recognition]]
uses-knowledge::[[Knowledge: Customer Acquisition Costs]]
```

### Extraction

```python
def extract_relationships(markdown_file):
    relationships = []
    
    # Regex to find typed wikilinks
    pattern = r'(\w+-\w+)::(\[\[([^\]]+)\]\])'
    
    for match in re.finditer(pattern, markdown_file.content):
        predicate = match.group(1)  # 'belongs-to-domain'
        target_text = match.group(3)  # 'Business Domain'
        
        rel = {
            'subject': markdown_file.frontmatter['id'],
            'predicate': predicate,
            'object_text': target_text,  # Will be resolved later
            'source': markdown_file.path,
            'created_at': now()
        }
        
        relationships.append(rel)
    
    return relationships

# Output
relationships = [
    {
        'subject': 'logic-006',
        'predicate': 'belongs-to-domain',
        'object_text': 'Business Domain',
        'source': '...REVENUE-LOOPS.md',
        'created_at': '2026-09-17T19:30:00Z'
    },
    {
        'subject': 'logic-006',
        'predicate': 'governed-by-control-plane',
        'object_text': 'CP-006',
        'source': '...REVENUE-LOOPS.md',
        'created_at': '2026-09-17T19:30:00Z'
    },
    # ...more relationships
]
```

---

## Stage 3: Entity Resolution

### Problem: Target Entities May Not Have Been Processed Yet

```python
def resolve_entity_references(relationships, entity_registry):
    resolved = []
    
    for rel in relationships:
        # Look up target entity by name, id, or alias
        target = entity_registry.find(
            name=rel['object_text'],
            fuzzy=True
        )
        
        if target:
            rel['object'] = target['id']
            rel['resolved'] = True
        else:
            # Create placeholder for forward reference
            rel['object'] = generate_id(rel['object_text'])
            rel['resolved'] = False
            rel['unresolved_name'] = rel['object_text']
        
        resolved.append(rel)
    
    return resolved

# Output: Resolved references
relationships = [
    {
        'subject': 'logic-006',
        'predicate': 'belongs-to-domain',
        'object': 'domain-business',  # Resolved
        'resolved': True,
        'source': '...',
        'created_at': '2026-09-17T19:30:00Z'
    },
    # ...more
]
```

---

## Stage 4: Validate Against Ontology

### Schema Validation

```python
def validate_relationship(rel, ontology):
    # Look up predicate in ontology
    pred_schema = ontology.relationships.get(rel['predicate'])
    
    if not pred_schema:
        raise ValueError(f"Unknown predicate: {rel['predicate']}")
    
    # Get subject and object types
    subject = entities.get(rel['subject'])
    obj = entities.get(rel['object'])
    
    # Check domain constraint
    if subject['type'] not in pred_schema['domain']:
        raise ValueError(
            f"Invalid domain for {rel['predicate']}: "
            f"expected {pred_schema['domain']}, got {subject['type']}"
        )
    
    # Check range constraint
    if obj['type'] not in pred_schema['range']:
        raise ValueError(
            f"Invalid range for {rel['predicate']}: "
            f"expected {pred_schema['range']}, got {obj['type']}"
        )
    
    return True

# All relationships validated ✅
```

---

## Stage 5: Create RDF Triples

### RDF Triple Format

```python
def create_triple(subject, predicate, obj, source):
    triple = {
        'subject': subject['id'],
        'subject_type': subject['type'],
        'predicate': predicate,
        'object': obj['id'],
        'object_type': obj['type'],
        'provenance': {
            'source': source,
            'created_at': now(),
            'confidence': 0.98,
            'verified': False
        }
    }
    
    return triple

# Example output
triple = {
    'subject': 'logic-006',
    'subject_type': 'logic-layer',
    'predicate': 'belongs-to-domain',
    'object': 'domain-business',
    'object_type': 'logic-domain',
    'provenance': {
        'source': '_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml',
        'created_at': '2026-09-17T19:30:00Z',
        'confidence': 0.98,
        'verified': False
    }
}
```

---

## Stage 6: Neo4j Ingestion

### Cypher Script Generation

```python
def generate_cypher(entities, triples):
    cypher = []
    
    # Create entity nodes
    for entity in entities:
        cypher.append(f"""
            MERGE (n:{entity['type'].upper()} {{id: '{entity['id']}'}})
            ON CREATE SET
                n.name = '{entity['name']}',
                n.wiki = '{entity.get('wiki', '')}',
                n.created_at = timestamp(),
                n.source = '{entity['provenance']['source']}',
                n.confidence = {entity['provenance']['confidence']}
        """)
    
    # Create relationships
    for triple in triples:
        cypher.append(f"""
            MATCH (s {{id: '{triple['subject']}'}})
            MATCH (o {{id: '{triple['object']}'}})
            CREATE (s)-[r:{triple['predicate'].upper()}]->(o)
            SET
                r.created_at = timestamp(),
                r.source = '{triple['provenance']['source']}',
                r.confidence = {triple['provenance']['confidence']},
                r.verified = {triple['provenance']['verified']}
        """)
    
    return '\n'.join(cypher)
```

### Neo4j Indexes

```cypher
-- Entity indexes
CREATE INDEX entity_id ON (n:Entity {id});
CREATE INDEX entity_type ON (n:Entity {type});
CREATE INDEX entity_name ON (n:Entity {name});

-- Relationship indexes
CREATE INDEX relationship_type ON ()-[r:RELATIONSHIP {predicate}]-();

-- Full-text search
CREATE FULLTEXT INDEX entities_search FOR (n:Entity) ON EACH [n.name, n.wiki];
```

---

## Stage 7: Semantic Indexing (Optional)

### Embedding & Qdrant Storage

```python
def embed_for_semantic_search(entities, client):
    for entity in entities:
        # Create searchable text
        text = f"{entity['name']} {entity['description']}"
        
        # Embed using nomic-embed-text or Claude embeddings
        embedding = client.embed(text, model='nomic-embed-text')
        
        # Store in Qdrant
        qdrant.upsert(
            collection='company-brain-entities',
            points=[
                {
                    'id': hash(entity['id']),
                    'vector': embedding,
                    'payload': {
                        'entity_id': entity['id'],
                        'entity_type': entity['type'],
                        'name': entity['name'],
                        'text': text
                    }
                }
            ]
        )
```

---

## Stage 8: Agent Retrieval

### Query Pattern 1: Direct Lookup

```cypher
-- Find all logics in Business domain
MATCH (logic:LogicLayer)-[:belongs-to-domain]->(domain)
WHERE domain.name = "Business Domain"
RETURN logic.name, logic.layer_number
```

### Query Pattern 2: Relationship Traversal

```cypher
-- What ventures does Logic-006 enable?
MATCH (logic:LogicLayer {id: 'logic-006'})-[:enables-venture]->(venture)
RETURN venture.name, venture.id
```

### Query Pattern 3: Dependency Chain

```cypher
-- What does Logic-006 depend on?
MATCH (logic:LogicLayer {id: 'logic-006'})-[:depends-on-logic*1..3]->(dep)
RETURN dep.name, dep.layer_number
ORDER BY dep.layer_number
```

### Query Pattern 4: Semantic Search (via Qdrant)

```python
# Agent asks: "What logics help us understand revenue?"
results = qdrant.search(
    collection='company-brain-entities',
    query_vector=embed("understand revenue"),
    limit=5
)

# Returns top 5 entities by semantic similarity
# Then agent can traverse from there in Neo4j
```

---

## Stage 9: Graph Updates from Agent Actions

### Event: Agent Makes Decision

```python
def record_decision(agent_id, logic_id, decision, outcome):
    # Create new triple
    triple = {
        'subject': agent_id,
        'predicate': 'made-decision-via-logic',
        'object': logic_id,
        'provenance': {
            'source': 'agent-execution-log',
            'created_at': now(),
            'confidence': 0.99,
            'verified': True,  # Agent actions are verified by nature
            'decision': decision,
            'outcome': outcome
        }
    }
    
    # Ingest into graph
    ingest_triple(triple)
    
    # Create result node
    result = {
        'type': 'result',
        'decision_id': decision,
        'outcome': outcome
    }
    
    # Connect result to decision
    connect(triple, result)
```

---

## Stage 10: Learning Loop

### Evaluation Updates Graph

```python
def record_evaluation(logic_id, evaluation_result):
    # Create evaluation node
    eval_node = {
        'type': 'evaluation',
        'id': evaluation_result['id'],
        'logic_id': logic_id,
        'score': evaluation_result['score'],
        'feedback': evaluation_result['feedback']
    }
    
    # Link to logic
    triple = {
        'subject': logic_id,
        'predicate': 'evaluated-by',
        'object': eval_node['id'],
        'provenance': {
            'source': 'evaluation-system',
            'confidence': evaluation_result['confidence'],
            'verified': True
        }
    }
    
    # If score < threshold, create flag
    if eval_node['score'] < 0.80:
        flag = {
            'type': 'alert',
            'severity': 'high',
            'message': f"Logic {logic_id} evaluation below threshold"
        }
        
        connect_alert(eval_node, flag)
        escalate_to_control_plane(logic_id)
```

---

## Running the Pipeline

### Manual Trigger

```bash
# Process all markdown files in wiki
python ingestion_pipeline.py \
  --source markdown \
  --wiki-path ./Company\ Brain/ \
  --ontology ./_ONTOLOGY/COMPANY-BRAIN-ONTOLOGY.xml \
  --neo4j-uri bolt://localhost:7687 \
  --neo4j-user neo4j \
  --neo4j-password changeme \
  --qdrant-url http://localhost:6333

# Output: 72 entities, ~200 relationships imported
```

### Scheduled Ingestion

```yaml
# Schedule via Cron (runs every 6 hours)
schedule:
  - cron: "0 */6 * * *"
    task: ingestion-pipeline
    params:
      incremental: true  # Only process changed files
      verify: true       # Validate all triples
      embed: true        # Update semantic index
```

### Event-Driven Ingestion

```python
# Trigger on file change (via Git hook or file watcher)
def on_file_changed(file_path):
    if file_path.endswith('.md'):
        ingestion_pipeline.process_file(file_path)
        print(f"Ingested {file_path}")
```

---

## Monitoring & Health

### Ingestion Metrics

```python
metrics = {
    'entities_processed': 789,
    'relationships_created': 2341,
    'triples_validated': 2341,
    'resolution_failures': 0,
    'schema_violations': 0,
    'ingestion_time_seconds': 14.2,
    'neo4j_write_time_seconds': 8.1,
    'qdrant_embed_time_seconds': 6.1
}
```

### Validation Queries

```cypher
-- Check for orphaned nodes
MATCH (n) WHERE NOT ()--(n) RETURN n
LIMIT 10;

-- Check for invalid relationships
MATCH ()-[r]->() WHERE r.verified = false RETURN r LIMIT 10;

-- Graph statistics
MATCH (n) RETURN count(n) as total_nodes;
MATCH ()-[r]->() RETURN count(r) as total_edges;
```

---

## References

- Ontology: [[_ONTOLOGY/COMPANY-BRAIN-ONTOLOGY.xml]]
- Wiki Guide: [[_DOCS/TYPED-WIKILINKS-GUIDE.md]]
- Logic Layers: [[_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml]]

