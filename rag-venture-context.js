// RAG Integration: Fetch Venture Context for Agent Prompts
// Loads venture data from Supabase before each call

const { createClient } = require('@supabase/supabase-js');

const supabaseUrl = process.env.SUPABASE_URL;
const supabaseKey = process.env.SUPABASE_KEY;
const supabase = createClient(supabaseUrl, supabaseKey);

const SECTOR_VENTURES = {
  'e-commerce': ['ECOM-001', 'ECOM-020', 'ECOM-050', 'ECOM-075'],
  'technology': ['TECH-001', 'TECH-030', 'TECH-050', 'SOFT-001'],
  'beauty-wellness': ['BW-001', 'BW-015', 'BW-025', 'BW-035']
};

async function getVentureContext(agentType, prospectIndustry = null) {
  try {
    const ventureIds = SECTOR_VENTURES[agentType] || [];

    if (ventureIds.length === 0) {
      return generateFallbackContext(agentType);
    }

    // Query primary venture for sector
    const primaryVentureId = ventureIds[0];

    const { data: venture, error } = await supabase
      .from('ventures')
      .select(`
        venture_code,
        name,
        description,
        pain_point,
        solution_summary,
        target_customer,
        pricing_monthly_min,
        pricing_monthly_max,
        implementation_timeline_days,
        key_benefits,
        recent_wins,
        competitor_comparison
      `)
      .eq('venture_code', primaryVentureId)
      .single();

    if (error || !venture) {
      console.warn(`Venture ${primaryVentureId} not found, using fallback`);
      return generateFallbackContext(agentType);
    }

    return buildContextPrompt(venture, agentType);

  } catch (err) {
    console.error('RAG context fetch error:', err);
    return generateFallbackContext(agentType);
  }
}

function buildContextPrompt(venture, agentType) {
  const templates = {
    'e-commerce': `You are calling about our inventory platform.

Product: ${venture.name}
Key Benefit: ${venture.key_benefits?.[0] || 'Multi-channel inventory sync'}
Pain Point They Have: ${venture.pain_point}
Our Solution: ${venture.solution_summary}

Pricing: $${venture.pricing_monthly_min}-$${venture.pricing_monthly_max}/month
Timeline: ${venture.implementation_timeline_days} days to live

Recent wins: ${venture.recent_wins?.join(', ') || 'Helping sellers reduce oversells'}

Remember: They're losing money to overselling right now. Quantify it.`,

    'technology': `You are calling about our CI/CD automation platform.

Product: ${venture.name}
Key Benefit: ${venture.key_benefits?.[0] || 'Cut deployment time by 90%'}
Pain Point: ${venture.pain_point}
Our Solution: ${venture.solution_summary}

Pricing: $${venture.pricing_monthly_min}-$${venture.pricing_monthly_max}/month
Timeline: 48 hours to first automated deploy

Recent wins: ${venture.recent_wins?.join(', ') || 'Helping teams ship 3x faster'}

Remember: Every minute of deploy time is engineering time lost. Frame as velocity gain.`,

    'beauty-wellness': `You are calling about our beauty booking platform.

Product: ${venture.name}
Key Benefit: ${venture.key_benefits?.[0] || '40% reduction in no-shows'}
Pain Point: ${venture.pain_point}
Our Solution: ${venture.solution_summary}

Pricing: $${venture.pricing_monthly_min}-$${venture.pricing_monthly_max}/month + processing
Timeline: 1 week to live

Recent wins: ${venture.recent_wins?.join(', ') || 'Helping salons eliminate revenue loss'}

Remember: 15% of their revenue is walking out the door due to no-shows.`
  };

  return templates[agentType] || templates['e-commerce'];
}

function generateFallbackContext(agentType) {
  const fallbacks = {
    'e-commerce': `You are Echo, our E-Commerce inventory specialist.

Our Solution: Multi-channel inventory platform that syncs Shopify, Amazon, eBay in real-time.
Key Benefit: 95% reduction in oversell incidents
Pricing: $2.5K-$5K/month
Pain Point: Multi-channel overselling costing them thousands/month
Implementation: 2-3 weeks

Always quantify their loss. Ask: "How many channels are you selling on?" and "How much are oversells costing you monthly?"`,

    'technology': `You are Swift, our Tech infrastructure specialist.

Our Solution: CI/CD automation that cuts deploys from 30 min to 3 min.
Key Benefit: 10x faster deployments = 3x faster shipping
Pricing: $3K-$8K/month
Pain Point: Deploy bottlenecks blocking feature velocity
Implementation: 48 hours to first automated deploy

Frame as: "More time shipping features, less time waiting for builds."`,

    'beauty-wellness': `You are Bella, our Beauty booking specialist.

Our Solution: Booking platform with SMS reminders that reduces no-shows.
Key Benefit: 40% no-show reduction + automated rescheduling
Pricing: $200-$500/month + 2% payment processing
Pain Point: 15% revenue loss to no-shows + 2 hours/day manual booking
Implementation: 1 week to live

Open with: "How much revenue are you leaving on the table from no-shows?"`
  };

  return fallbacks[agentType] || fallbacks['e-commerce'];
}

module.exports = { getVentureContext };
