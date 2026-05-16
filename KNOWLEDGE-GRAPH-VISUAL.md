---
title: Knowledge Graph Visualization
description: Interactive node-edge visualization of all entities and relationships
tags: graph, visualization, dataviewjs, interactive
created: 2026-05-15
---

# Knowledge Graph Visualization

**Live graph from**: `.planning/graph-data.json`

---

## Interactive Graph View

```dataviewjs
const data = await dv.io.load(".planning/graph-data.json");

if (!data || !data.entities || data.entities.length === 0) {
  dv.paragraph("⏳ No graph data found. Run: python3 obsidian_graph_sync.py");
} else {
  const entities = data.entities || [];
  const relationships = data.relationships || [];
  
  // Build node map
  const nodeMap = {};
  entities.forEach(e => {
    nodeMap[e.id] = {
      id: e.id,
      label: e.name,
      type: e.entity_type,
      venture: e.venture_id || "—"
    };
  });
  
  // Build adjacency for visualization
  const connections = {};
  entities.forEach(e => {
    connections[e.id] = {
      outgoing: [],
      incoming: []
    };
  });
  
  relationships.forEach(r => {
    if (connections[r.source_id]) {
      connections[r.source_id].outgoing.push({
        target: r.target_id,
        type: r.relation_type
      });
    }
    if (connections[r.target_id]) {
      connections[r.target_id].incoming.push({
        source: r.source_id,
        type: r.relation_type
      });
    }
  });
  
  // Generate HTML for graph visualization
  let html = `
    <div style="font-family: monospace; background: #f5f5f5; padding: 15px; border-radius: 8px;">
      <div style="margin-bottom: 20px;">
        <strong>📊 Knowledge Graph: ${entities.length} Nodes, ${relationships.length} Edges</strong>
      </div>
      
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
  `;
  
  // Left: Node list by type
  const typeGroups = {};
  entities.forEach(e => {
    if (!typeGroups[e.entity_type]) typeGroups[e.entity_type] = [];
    typeGroups[e.entity_type].push(e);
  });
  
  html += `<div><strong>Nodes by Type:</strong><br/>`;
  for (const [type, nodes] of Object.entries(typeGroups)) {
    html += `<div style="margin: 10px 0;">
      <span style="color: #0066cc; font-weight: bold;">${type}</span> (${nodes.length})
      <ul style="margin: 5px 0 0 20px; padding: 0;">
  `;
    nodes.forEach(n => {
      const connCount = (connections[n.id].outgoing.length + connections[n.id].incoming.length);
      html += `<li style="color: #333; margin: 3px 0;">
        <strong>${n.name}</strong> 
        <span style="color: #666;">← ${connCount} connections</span>
      </li>`;
    });
    html += `</ul></div>`;
  }
  html += `</div>`;
  
  // Right: Relationship matrix
  html += `<div><strong>Relationships:</strong><br/>`;
  const relTypes = {};
  relationships.forEach(r => {
    if (!relTypes[r.relation_type]) relTypes[r.relation_type] = [];
    relTypes[r.relation_type].push(r);
  });
  
  for (const [relType, rels] of Object.entries(relTypes)) {
    html += `<div style="margin: 10px 0;">
      <span style="color: #cc6600; font-weight: bold;">${relType}</span> (${rels.length})
      <ul style="margin: 5px 0 0 20px; padding: 0;">
    `;
    rels.forEach(r => {
      const source = nodeMap[r.source_id]?.label || r.source_id;
      const target = nodeMap[r.target_id]?.label || r.target_id;
      html += `<li style="color: #333; margin: 2px 0; font-size: 12px;">
        ${source} → ${target}
      </li>`;
    });
    html += `</ul></div>`;
  }
  html += `</div>`;
  
  html += `</div></div>`;
  
  dv.paragraph(html);
  
  // Connection details
  dv.paragraph("---");
  dv.paragraph("**🔗 Connection Details**");
  
  const connDetails = [];
  for (const [entityId, conn] of Object.entries(connections)) {
    const node = nodeMap[entityId];
    if (conn.outgoing.length > 0 || conn.incoming.length > 0) {
      connDetails.push({
        entity: node.label,
        type: node.type,
        outgoing: conn.outgoing.length,
        incoming: conn.incoming.length,
        total: conn.outgoing.length + conn.incoming.length
      });
    }
  }
  
  connDetails.sort((a, b) => b.total - a.total);
  
  dv.table(
    ["Entity", "Type", "Outgoing", "Incoming", "Total"],
    connDetails.map(c => [c.entity, c.type, c.outgoing, c.incoming, c.total])
  );
}
```

---

## Entity Connectivity Heatmap

```dataviewjs
const data = await dv.io.load(".planning/graph-data.json");

if (data && data.entities && data.relationships) {
  const entities = data.entities;
  const relationships = data.relationships;
  
  // Count connections per entity
  const connCount = {};
  entities.forEach(e => {
    connCount[e.id] = {
      name: e.name,
      type: e.entity_type,
      count: 0
    };
  });
  
  relationships.forEach(r => {
    if (connCount[r.source_id]) connCount[r.source_id].count++;
    if (connCount[r.target_id]) connCount[r.target_id].count++;
  });
  
  // Generate heatmap
  const sorted = Object.values(connCount)
    .sort((a, b) => b.count - a.count)
    .slice(0, 10);
  
  dv.paragraph("**🔥 Most Connected Entities**");
  
  sorted.forEach(item => {
    const width = (item.count / (sorted[0]?.count || 1)) * 100;
    dv.paragraph(`
      <div style="margin: 8px 0;">
        <div style="font-weight: bold; margin-bottom: 4px;">${item.name} (${item.type})</div>
        <div style="background: #e0e0e0; border-radius: 4px; height: 20px; position: relative;">
          <div style="background: linear-gradient(90deg, #0066cc, #00ccff); border-radius: 4px; width: ${width}%; height: 100%; display: flex; align-items: center; justify-content: flex-end; padding-right: 8px;">
            <span style="color: white; font-size: 12px; font-weight: bold;">${item.count}</span>
          </div>
        </div>
      </div>
    `);
  });
}
```

---

## Graph Statistics

```dataviewjs
const data = await dv.io.load(".planning/graph-data.json");

if (data && data.entities && data.relationships) {
  const entities = data.entities;
  const rels = data.relationships;
  
  // Calculate metrics
  const typeCount = {};
  entities.forEach(e => {
    typeCount[e.entity_type] = (typeCount[e.entity_type] || 0) + 1;
  });
  
  const relTypeCount = {};
  rels.forEach(r => {
    relTypeCount[r.relation_type] = (relTypeCount[r.relation_type] || 0) + 1;
  });
  
  // Average degree
  const degrees = {};
  entities.forEach(e => degrees[e.id] = 0);
  rels.forEach(r => {
    degrees[r.source_id]++;
    degrees[r.target_id]++;
  });
  
  const avgDegree = (Object.values(degrees).reduce((a, b) => a + b, 0) / entities.length).toFixed(2);
  const maxDegree = Math.max(...Object.values(degrees));
  
  dv.paragraph(`
**📈 Graph Metrics**

- **Total Nodes**: ${entities.length}
- **Total Edges**: ${rels.length}
- **Graph Density**: ${(rels.length / (entities.length * (entities.length - 1) / 2) * 100).toFixed(2)}%
- **Average Degree**: ${avgDegree}
- **Max Degree**: ${maxDegree}
- **Number of Entity Types**: ${Object.keys(typeCount).length}
- **Number of Relationship Types**: ${Object.keys(relTypeCount).length}
  `);
}
```

---

## How to Read This

1. **Nodes by Type** — Shows all entities grouped by category (Venture, Decision, Metric, Risk)
2. **Relationships** — Shows all connections between entities
3. **Connection Details** — Ranked table showing most-connected entities
4. **Heatmap** — Visual bar chart of connectivity
5. **Statistics** — Graph density, degree distribution, type counts

**What these mean:**
- High connectivity = central entities (ventures connected to many decisions/metrics)
- Low connectivity = leaf nodes (risks connected to one venture)
- Density = how tightly interconnected (values 0-100%)

---

**Last synced**: Run `python3 obsidian_graph_sync.py` to update data
