import type { NextApiRequest, NextApiResponse } from 'next';
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = process.env.SUPABASE_URL || 'https://rhlkjelglvurowdalrgh.supabase.co';
const supabaseKey = process.env.SUPABASE_ANON_KEY || '';

const supabase = createClient(supabaseUrl, supabaseKey);

interface Venture {
  id: string;
  name: string;
  sector: string;
  stage: string;
  status: string;
  mrr: string;
}

const OPCO_MAPPING: Record<string, string> = {
  'OPCO-Technology': 'TECH',
  'OPCO-Finance': 'FIN',
  'OPCO-Operations': 'OPS',
  'OPCO-Construction': 'CON',
  'OPCO-RealEstate': 'RE',
  'OPCO-Logistics': 'LT',
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Venture[] | { error: string }>
) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const opcoId = req.query.opco as string || 'OPCO-Technology';
    const opcoPrefix = OPCO_MAPPING[opcoId] || 'TECH';

    // Query Supabase for ventures matching the OPCO
    const { data: ventures, error } = await supabase
      .from('ventures')
      .select('id, name, sector, stage, status')
      .ilike('id', `${opcoPrefix}-%`);

    if (error) throw error;

    // Transform and add mock MRR (would come from deal_payments in real implementation)
    const transformedVentures: Venture[] = (ventures || []).map((v: any) => ({
      id: v.id,
      name: v.name,
      sector: v.sector,
      stage: v.stage,
      status: v.status,
      mrr: v.stage === 'Revenue' ? '$5K-$25K' : '$0',
    }));

    res.setHeader('Cache-Control', 'public, max-age=60, s-maxage=60');
    res.status(200).json(transformedVentures);
  } catch (error) {
    console.error('Ventures API error:', error);
    res.status(500).json({
      error: error instanceof Error ? error.message : 'Failed to fetch ventures',
    });
  }
}
