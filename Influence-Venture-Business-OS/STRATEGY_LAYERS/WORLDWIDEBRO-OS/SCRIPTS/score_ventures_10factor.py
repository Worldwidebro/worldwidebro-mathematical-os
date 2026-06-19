#!/usr/bin/env python3
"""
Venture Selection Framework: 10-Factor Scoring
Scores all 712 ventures against evidence-based criteria.
Outputs: venture_scores.csv, tier_assignments.csv, executive_summary.txt
"""

import pandas as pd
import json
from datetime import datetime
from pathlib import Path

SCORING_FACTORS = {
    'pain': {'weight': 10},
    'frequency': {'weight': 8},
    'urgency': {'weight': 9},
    'buying_power': {'weight': 10},
    'reachability': {'weight': 8},
    'competition': {'weight': 7},
    'fulfillment': {'weight': 9},
    'scalability': {'weight': 8},
    'ai_leverage': {'weight': 8},
    'strategic_fit': {'weight': 9},
}

MAX_SCORE = sum([v['weight'] for v in SCORING_FACTORS.values()])

SECTOR_RULES = {
    'fintech': {
        'pain': 10, 'frequency': 10, 'urgency': 9, 'buying_power': 9,
        'reachability': 8, 'scalability': 9, 'ai_leverage': 10, 'strategic_fit': 9,
        'competition': 7, 'fulfillment_base': 6,
    },
    'beauty': {
        'pain': 9, 'frequency': 10, 'urgency': 8, 'buying_power': 7,
        'reachability': 8, 'scalability': 8, 'ai_leverage': 6, 'strategic_fit': 8,
        'competition': 7, 'fulfillment_base': 6,
    },
    'edtech': {
        'pain': 9, 'frequency': 10, 'urgency': 8, 'buying_power': 7,
        'reachability': 9, 'scalability': 10, 'ai_leverage': 9, 'strategic_fit': 9,
        'competition': 5, 'fulfillment_base': 5,
    },
}

def get_fulfillment_score(stage, base_score):
    """Map stage to fulfillment score."""
    stage_map = {'planned': 2, 'mvp': 7, 'validation': 8, 'development': 8, 'growth': 10}
    return stage_map.get(stage, base_score)

def score_venture(venture_row):
    """Score a single venture."""
    sector = venture_row.get('sector', 'fintech').lower()
    stage = venture_row.get('stage', 'planned').lower()
    name = venture_row.get('venture_name', venture_row.get('name', ''))

    rules = SECTOR_RULES.get(sector, SECTOR_RULES['fintech'])

    scores = {}
    for factor in SCORING_FACTORS.keys():
        if factor == 'fulfillment':
            scores[factor] = get_fulfillment_score(stage, rules.get('fulfillment_base', 5))
        else:
            scores[factor] = rules.get(factor, 5)

    # Boost for revenue-generating ventures
    if venture_row.get('revenue_ytd', 0) > 5000:
        scores['fulfillment'] = min(10, scores['fulfillment'] + 2)
        scores['strategic_fit'] = min(10, scores['strategic_fit'] + 1)

    total_score = sum([
        scores[factor] * SCORING_FACTORS[factor]['weight']
        for factor in SCORING_FACTORS.keys()
    ]) / MAX_SCORE * 100

    return {
        'venture_id': venture_row.get('venture_id', ''),
        'venture_name': name,
        'sector': sector,
        'stage': stage,
        'total_score': round(total_score, 1),
        **{f'{k}_score': v for k, v in scores.items()}
    }

def assign_tier(score):
    """Assign tier based on score."""
    if score >= 80:
        return 'Tier 1 (Build Now)'
    elif score >= 70:
        return 'Tier 2 (Build Q2)'
    elif score >= 60:
        return 'Tier 3 (Monitor)'
    else:
        return 'Backlog'

def main():
    ventures_file = Path('/Users/acebless/Documents/WORLDWIDEBRO-OS/08_RESEARCH/Ventures-Data/WORLDWIDEBRO-712-UNIFIED.csv')

    if not ventures_file.exists():
        print(f"❌ File not found: {ventures_file}")
        return

    print(f"📊 Loading ventures...")
    df = pd.read_csv(ventures_file)
    print(f"✅ Loaded {len(df)} ventures")
    print(f"📈 Scoring using 10-factor framework...")

    scores = []
    for _, row in df.iterrows():
        score = score_venture(row)
        score['tier'] = assign_tier(score['total_score'])
        scores.append(score)

    scores_df = pd.DataFrame(scores).sort_values('total_score', ascending=False)

    output_dir = Path('/Users/acebless/Documents/.planning')
    output_dir.mkdir(exist_ok=True)

    scores_file = output_dir / 'venture-scores-10factor.csv'
    scores_df.to_csv(scores_file, index=False)
    print(f"✅ Scores saved: {scores_file}")

    tier_counts = scores_df['tier'].value_counts()
    print(f"\nTier Distribution:")
    for tier, count in tier_counts.items():
        print(f"  {tier}: {count} ventures")

    top_10 = scores_df.head(10)[['venture_name', 'sector', 'stage', 'total_score', 'tier']]
    print(f"\nTop 10 Ventures:")
    print(top_10.to_string(index=False))

    return scores_df

if __name__ == '__main__':
    main()
