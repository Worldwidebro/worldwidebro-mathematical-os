export type Feature = 'dispatch' | 'staffing' | 'construction' | 'ai';

export interface License {
  sku: string;
  expires_at: string;
}

export function canAccess(licenses: License[], feature: Feature): boolean {
  const skuMap: Record<Feature, string[]> = {
    dispatch: ['dispatch', 'core'],
    staffing: ['staffing', 'core'],
    construction: ['construction', 'core'],
    ai: ['ai', 'core'],
  };

  const requiredSkus = skuMap[feature];
  const today = new Date().toISOString().split('T')[0];

  return requiredSkus.some(sku =>
    licenses.some(l => l.sku === sku && l.expires_at > today)
  );
}

export function getAccessibleFeatures(licenses: License[]): Feature[] {
  const allFeatures: Feature[] = ['dispatch', 'staffing', 'construction', 'ai'];
  return allFeatures.filter(f => canAccess(licenses, f));
}

export function daysUntilExpiration(license: License): number {
  const expDate = new Date(license.expires_at);
  const today = new Date();
  return Math.ceil((expDate.getTime() - today.getTime()) / (1000 * 60 * 60 * 24));
}
