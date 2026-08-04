import { describe, it, expect } from 'vitest';
import { SERVICES_CATALOG } from '../services.js';

describe('Central API Gateway & 35 Microservices Router Tests', () => {
  it('should contain all 35 microservices in catalog', () => {
    expect(SERVICES_CATALOG).toHaveLength(35);
    
    const requiredRoutes = [
      '/api/identity',
      '/api/organization',
      '/api/properties',
      '/api/listings',
      '/api/loans',
      '/api/crm',
      '/api/underwriting',
      '/api/valuation',
      '/api/mortgage',
      '/api/closing',
      '/api/lease',
      '/api/tenant',
      '/api/rent-collection',
      '/api/maintenance',
      '/api/asset-management',
      '/api/syndication',
      '/api/document',
      '/api/notification',
      '/api/analytics',
      '/api/market-intelligence',
      '/api/inspection',
      '/api/disposition',
      '/api/tax',
      '/api/insurance',
      '/api/utility-management',
      '/api/vendor',
      '/api/marketing-automation',
      '/api/e-signature',
      '/api/audit-logging',
      '/api/spatial',
      '/api/construction',
      '/api/portfolio-optimization',
      '/api/investor-relations',
      '/api/accounting',
      '/api/ai-gateway',
    ];

    requiredRoutes.forEach((route) => {
      const found = SERVICES_CATALOG.find((svc) => svc.route === route);
      expect(found).toBeDefined();
      expect(found?.status).toBe('HEALTHY');
      expect(found?.description).toBeTruthy();
    });
  });
});
