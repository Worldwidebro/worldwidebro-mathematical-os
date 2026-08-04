// vex-api/src/matching/engine.ts
// Track C: Partner Matching Engine + Capability Graph
// Connects Neo4j capability graph to Supabase opportunities

import { Driver } from 'neo4j-driver';

export interface PartnerMatch {
  partner_id: string;
  name: string;
  tier: string;
  capabilities: string[];
  matching_capabilities: number;
  score: number;
  region: string;
  reason: string;
}

export interface Opportunity {
  id: string;
  industry: string;
  value: number;
  products_needed: string[];
  region: string;
}

export class MatchingEngine {
  constructor(private driver: Driver) {}

  /**
   * Find best partners for an opportunity
   */
  async findBestPartners(opportunity: Opportunity, limit = 5): Promise<PartnerMatch[]> {
    const session = this.driver.session();

    try {
      const query = `
        MATCH (o:Opportunity {id: $opportunity_id})-[:REQUIRES_CAPABILITY]->(cap:Capability)
        MATCH (p:Partner)-[:HAS_CAPABILITY]->(cap)
        WHERE p.status = 'active' AND p.tier IN ['partner', 'strategic']
          AND (p)-[:OPERATES_IN]->(r:Region {name: $region})
        WITH p, r, count(cap) as matching_caps
        ORDER BY matching_caps DESC, p.score DESC
        LIMIT $limit
        RETURN p.id as partner_id, p.name, p.tier, p.capabilities, p.score, r.name as region, matching_caps
      `;

      const result = await session.run(query, {
        opportunity_id: opportunity.id,
        region: opportunity.region,
        limit: limit,
      });

      return result.records.map((record) => {
        const matching = record.get('matching_caps');
        return {
          partner_id: record.get('partner_id'),
          name: record.get('name'),
          tier: record.get('tier'),
          capabilities: record.get('p.capabilities'),
          matching_capabilities: matching,
          score: record.get('p.score'),
          region: record.get('region'),
          reason: `Matches ${matching} capabilities needed for ${opportunity.industry}`,
        };
      });
    } finally {
      await session.close();
    }
  }

  /**
   * Find partners by capability + region
   */
  async findPartnersByCapability(capability: string, region: string): Promise<PartnerMatch[]> {
    const session = this.driver.session();

    try {
      const query = `
        MATCH (p:Partner)-[:HAS_CAPABILITY]->(c:Capability {name: $capability})
        WHERE p.status = 'active'
          AND (p)-[:OPERATES_IN]->(r:Region {name: $region})
        RETURN p.id as partner_id, p.name, p.tier, p.capabilities, p.score, r.name as region
        ORDER BY p.score DESC
      `;

      const result = await session.run(query, { capability, region });

      return result.records.map((record) => ({
        partner_id: record.get('partner_id'),
        name: record.get('name'),
        tier: record.get('tier'),
        capabilities: record.get('p.capabilities'),
        matching_capabilities: 1,
        score: record.get('p.score'),
        region: record.get('region'),
        reason: `Specializes in ${capability}`,
      }));
    } finally {
      await session.close();
    }
  }

  /**
   * Sync partner from Supabase to Neo4j graph
   */
  async syncPartnerToGraph(partner: {
    id: string;
    name: string;
    capabilities: string[];
    tier: string;
    score: number;
    coverage_area: string;
  }): Promise<boolean> {
    const session = this.driver.session();

    try {
      const query = `
        MERGE (p:Partner {id: $id})
        SET p.name = $name, p.tier = $tier, p.score = $score, p.capabilities = $capabilities
        WITH p
        MATCH (r:Region {name: $region})
        MERGE (p)-[:OPERATES_IN]->(r)
        RETURN p.id
      `;

      await session.run(query, {
        id: partner.id,
        name: partner.name,
        tier: partner.tier,
        score: partner.score,
        capabilities: partner.capabilities,
        region: partner.coverage_area,
      });

      return true;
    } finally {
      await session.close();
    }
  }

  /**
   * Create opportunity node in Neo4j
   */
  async createOpportunityNode(opportunity: {
    id: string;
    industry: string;
    value: number;
    products_needed: string[];
    region: string;
  }): Promise<boolean> {
    const session = this.driver.session();

    try {
      const query = `
        CREATE (o:Opportunity {
          id: $id,
          industry: $industry,
          value: $value,
          products_needed: $products_needed,
          created_at: timestamp()
        })
        WITH o
        MATCH (r:Region {name: $region})
        CREATE (o)-[:IN_REGION]->(r)
        WITH o
        UNWIND $products_needed as product
        MATCH (c:Capability {name: product})
        CREATE (o)-[:REQUIRES_CAPABILITY]->(c)
        RETURN o.id
      `;

      await session.run(query, {
        id: opportunity.id,
        industry: opportunity.industry,
        value: opportunity.value,
        products_needed: opportunity.products_needed,
        region: opportunity.region,
      });

      return true;
    } finally {
      await session.close();
    }
  }
}

/**
 * Seed Neo4j with capabilities and regions
 */
export async function seedCapabilityGraph(driver: Driver): Promise<void> {
  const session = driver.session();

  try {
    // Create capabilities
    await session.run(`
      UNWIND $caps as cap
      MERGE (c:Capability {name: cap.name})
      SET c.category = cap.category
    `, {
      caps: [
        { name: 'dispatch', category: 'operations' },
        { name: 'staffing', category: 'workforce' },
        { name: 'construction', category: 'operations' },
        { name: 'ai', category: 'platform' },
        { name: 'healthcare', category: 'compliance' },
        { name: 'compliance', category: 'compliance' },
      ]
    });

    // Create regions
    await session.run(`
      UNWIND $regions as r
      MERGE (reg:Region {name: r.name})
      SET reg.state = r.state
    `, {
      regions: [
        { name: 'Arizona', state: 'AZ' },
        { name: 'North Carolina', state: 'NC' },
        { name: 'Texas', state: 'TX' },
      ]
    });

    console.log('✅ Capability graph seeded');
  } finally {
    await session.close();
  }
}
