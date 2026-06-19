/**
 * Layer 2: Research (with Tavily MCP integration)
 */

import { researchWithTavily } from "../mcp-integrations.js";

export async function researchTrends(context) {
  const { sector = "General" } = context;

  console.log(`\n🔍 Layer 2: Research`);
  console.log(`   Sector: ${sector}`);

  if (context.trending_topics) {
    return {
      venture_id: context.venture_id,
      trending_topics: context.trending_topics,
      status: "ready",
    };
  }

  // MCP integration point
  await researchWithTavily(sector);

  return {
    venture_id: context.venture_id,
    trending_topics: [`AI in ${sector}`, "2026 trends", "Emerging challenges"],
    status: "ready",
  };
}
