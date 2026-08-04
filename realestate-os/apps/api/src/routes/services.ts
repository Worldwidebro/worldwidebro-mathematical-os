import { Router, Request, Response } from 'express';

const router = Router();

export const SERVICES_CATALOG = [
  { id: 'identity-service', name: 'Identity Service', route: '/api/identity', category: 'auth', description: 'Auth, User RBAC & JWT issuance', status: 'HEALTHY', version: '1.0.0' },
  { id: 'organization-service', name: 'Organization Service', route: '/api/organization', category: 'core', description: 'Multi-tenant organization contexts', status: 'HEALTHY', version: '1.0.0' },
  { id: 'property-service', name: 'Property Service', route: '/api/properties', category: 'asset', description: 'Property & unit CRUD, asset tracking', status: 'HEALTHY', version: '1.0.0' },
  { id: 'listing-service', name: 'Listing Service', route: '/api/listings', category: 'asset', description: 'MLS integration & listing management', status: 'HEALTHY', version: '1.0.0' },
  { id: 'loans-service', name: 'Loan Service', route: '/api/loans', category: 'finance', description: 'Loan pipeline & servicing hub', status: 'HEALTHY', version: '1.0.0' },
  { id: 'crm-service', name: 'CRM Service', route: '/api/crm', category: 'crm', description: 'Investor & buyer CRM, lead pipeline', status: 'HEALTHY', version: '1.0.0' },
  { id: 'underwriting-service', name: 'Underwriting Service', route: '/api/underwriting', category: 'analytics', description: 'Deal financial modeling, cap rates, cash flow', status: 'HEALTHY', version: '1.0.0' },
  { id: 'valuation-service', name: 'Valuation Service', route: '/api/valuation', category: 'analytics', description: 'Automated Valuation Model (AVM) & comp analysis', status: 'HEALTHY', version: '1.0.0' },
  { id: 'mortgage-service', name: 'Mortgage Service', route: '/api/mortgage', category: 'finance', description: 'Loan application & origination engine', status: 'HEALTHY', version: '1.0.0' },
  { id: 'closing-service', name: 'Closing Service', route: '/api/closing', category: 'legal', description: 'Escrow, title search, and deal closing', status: 'HEALTHY', version: '1.0.0' },
  { id: 'lease-service', name: 'Lease Service', route: '/api/lease', category: 'legal', description: 'E-signature & lease contract generation', status: 'HEALTHY', version: '1.0.0' },
  { id: 'tenant-service', name: 'Tenant Service', route: '/api/tenant', category: 'tenant', description: 'Tenant portal, screening & communications', status: 'HEALTHY', version: '1.0.0' },
  { id: 'rent-collection-service', name: 'Rent Collection Service', route: '/api/rent-collection', category: 'finance', description: 'Stripe/ACH payment ledger & auto-reminders', status: 'HEALTHY', version: '1.0.0' },
  { id: 'maintenance-service', name: 'Maintenance Service', route: '/api/maintenance', category: 'operations', description: 'Work orders, contractor triage & dispatch', status: 'HEALTHY', version: '1.0.0' },
  { id: 'asset-management-service', name: 'Asset Management Service', route: '/api/asset-management', category: 'asset', description: 'NOI optimization, capex & portfolio analytics', status: 'HEALTHY', version: '1.0.0' },
  { id: 'syndication-service', name: 'Syndication Service', route: '/api/syndication', category: 'capital', description: 'Investor portal, equity raising & distributions', status: 'HEALTHY', version: '1.0.0' },
  { id: 'document-service', name: 'Document Service', route: '/api/document', category: 'storage', description: 'Document storage, OCR parsing & file vault', status: 'HEALTHY', version: '1.0.0' },
  { id: 'notification-service', name: 'Notification Service', route: '/api/notification', category: 'comm', description: 'SMS, email & push notification gateway', status: 'HEALTHY', version: '1.0.0' },
  { id: 'analytics-service', name: 'Analytics Service', route: '/api/analytics', category: 'analytics', description: 'Business intelligence & executive metrics', status: 'HEALTHY', version: '1.0.0' },
  { id: 'market-intelligence-service', name: 'Market Intelligence Service', route: '/api/market-intelligence', category: 'market', description: 'Rent estimates & market macro trends', status: 'HEALTHY', version: '1.0.0' },
  { id: 'inspection-service', name: 'Inspection Service', route: '/api/inspection', category: 'operations', description: 'Property condition reports & audit parsing', status: 'HEALTHY', version: '1.0.0' },
  { id: 'disposition-service', name: 'Disposition Service', route: '/api/disposition', category: 'asset', description: 'Asset liquidation & sales channel', status: 'HEALTHY', version: '1.0.0' },
  { id: 'tax-service', name: 'Property Tax Service', route: '/api/tax', category: 'finance', description: 'Property tax appeals & assessment deductions', status: 'HEALTHY', version: '1.0.0' },
  { id: 'insurance-service', name: 'Insurance Service', route: '/api/insurance', category: 'risk', description: 'Risk scoring, policy tracking & claims', status: 'HEALTHY', version: '1.0.0' },
  { id: 'utility-management-service', name: 'Utility Management Service', route: '/api/utility-management', category: 'operations', description: 'Metering & utility invoice parsing', status: 'HEALTHY', version: '1.0.0' },
  { id: 'vendor-service', name: 'Vendor Service', route: '/api/vendor', category: 'operations', description: 'Contractor network & compliance verification', status: 'HEALTHY', version: '1.0.0' },
  { id: 'marketing-automation-service', name: 'Marketing Automation Service', route: '/api/marketing-automation', category: 'marketing', description: 'Campaign management & property flyers', status: 'HEALTHY', version: '1.0.0' },
  { id: 'e-signature-service', name: 'E-Signature Service', route: '/api/e-signature', category: 'legal', description: 'Digital signature integration stub', status: 'HEALTHY', version: '1.0.0' },
  { id: 'audit-logging-service', name: 'Audit Logging Service', route: '/api/audit-logging', category: 'security', description: 'Activity audit trails & compliance log', status: 'HEALTHY', version: '1.0.0' },
  { id: 'spatial-service', name: 'Spatial Service', route: '/api/spatial', category: 'data', description: 'GIS, mapping & zoning data analysis', status: 'HEALTHY', version: '1.0.0' },
  { id: 'construction-service', name: 'Construction Service', route: '/api/construction', category: 'operations', description: 'Rehab project management & budgeting', status: 'HEALTHY', version: '1.0.0' },
  { id: 'portfolio-optimization-service', name: 'Portfolio Optimization Service', route: '/api/portfolio-optimization', category: 'finance', description: 'Yield maximization & balance sheet rebalancing', status: 'HEALTHY', version: '1.0.0' },
  { id: 'investor-relations-service', name: 'Investor Relations Service', route: '/api/investor-relations', category: 'capital', description: 'K-1 distribution & waterfall calculations', status: 'HEALTHY', version: '1.0.0' },
  { id: 'accounting-service', name: 'Accounting Service', route: '/api/accounting', category: 'finance', description: 'Double-entry general ledger', status: 'HEALTHY', version: '1.0.0' },
  { id: 'ai-gateway-service', name: 'AI Gateway Service', route: '/api/ai-gateway', category: 'ai', description: 'LLM execution proxy & agent state manager', status: 'HEALTHY', version: '1.0.0' },
];

/**
 * GET /api/services or GET /
 * Central Service Catalog index returning all 35 mock microservices.
 */
const getServicesCatalog = (req: Request, res: Response) => {
  res.json({
    success: true,
    totalServicesCount: SERVICES_CATALOG.length,
    services: SERVICES_CATALOG,
    timestamp: new Date().toISOString(),
  });
};

router.get('/', getServicesCatalog);
router.get('/services', getServicesCatalog);

// 1. Identity Service
router.all('/identity*', (req: Request, res: Response) => {
  res.json({
    service: 'identity-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      activeSessions: 14,
      rbacRoles: ['admin', 'landlord', 'tenant', 'underwriter', 'investor'],
      jwtIssuer: 'realestate-os-auth',
      identityStatus: 'HEALTHY',
    },
  });
});

// 2. Organization Service
router.all('/organization*', (req: Request, res: Response) => {
  res.json({
    service: 'organization-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      organizationId: 'ORG-CHL-001',
      name: 'Worldwidebro Real Estate Holdings',
      tier: 'Enterprise',
      subTenants: 12,
      complianceStatus: 'VERIFIED',
    },
  });
});

// 3. Properties Service
router.all('/properties*', (req: Request, res: Response) => {
  res.json({
    service: 'property-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      totalProperties: 12,
      totalUnits: 148,
      occupiedUnits: 142,
      occupancyRate: '95.9%',
      featuredProperty: {
        id: 'PROP-101',
        name: 'Tryon Urban Towers',
        address: '412 N Tryon St, Charlotte, NC',
        unitsCount: 48,
      },
    },
  });
});

// 4. Listings Service
router.all('/listings*', (req: Request, res: Response) => {
  res.json({
    service: 'listing-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      activeListingsCount: 6,
      syndicatedChannels: ['Zillow', 'Realtor.com', 'Redfin', 'Trulia'],
      recentListing: {
        id: 'LIST-882',
        title: 'Luxury South End Townhome',
        price: 645000,
        status: 'ACTIVE_MLS',
      },
    },
  });
});

// 5. Loans Service
router.all('/loans*', (req: Request, res: Response) => {
  res.json({
    service: 'loans-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      activeLoansCount: 8,
      totalPrincipalBalance: 18450000,
      weightedAvgInterestRate: '6.45%',
      servicingStatus: 'CURRENT',
    },
  });
});

// 6. CRM Service
router.all('/crm*', (req: Request, res: Response) => {
  res.json({
    service: 'crm-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      totalLeadsCount: 412,
      accreditedInvestors: 84,
      activePipelineValue: 42000000,
      topLead: { name: 'Arthur Pendelton', leadScore: 94, status: 'Qualified LP' },
    },
  });
});

// 7. Underwriting Service
router.all('/underwriting*', (req: Request, res: Response) => {
  res.json({
    service: 'underwriting-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      underwritingEngine: 'RealEstateOS Pro-Forma V2',
      defaultTargetCapRate: 7.5,
      defaultTargetDSCR: 1.25,
      activeDealsInUnderwriting: 5,
    },
  });
});

// 8. Valuation Service
router.all('/valuation*', (req: Request, res: Response) => {
  res.json({
    service: 'valuation-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      avmModel: 'Spatial-Hedonic Neural Engine',
      avgConfidenceInterval: '94.2%',
      recentAppraisalsCount: 28,
    },
  });
});

// 9. Mortgage Service
router.all('/mortgage*', (req: Request, res: Response) => {
  res.json({
    service: 'mortgage-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      originationPipelineCount: 14,
      totalRequestedVolume: 8200000,
      approvedPreApprovals: 9,
    },
  });
});

// 10. Closing Service
router.all('/closing*', (req: Request, res: Response) => {
  res.json({
    service: 'closing-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      activeEscrowsCount: 3,
      titlePartners: ['First American Title', 'Fidelity National Title'],
      upcomingClosing: { dealId: 'DEAL-902', targetClosingDate: '2026-08-12', escrowBalance: 450000 },
    },
  });
});

// 11. Lease Service
router.all('/lease*', (req: Request, res: Response) => {
  res.json({
    service: 'lease-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      activeLeasesCount: 142,
      expiringIn30Days: 4,
      templateJurisdictions: ['NC', 'SC', 'GA', 'FL', 'VA'],
    },
  });
});

// 12. Tenant Service
router.all('/tenant*', (req: Request, res: Response) => {
  res.json({
    service: 'tenant-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      activeTenantsCount: 156,
      portalActivePct: '94.2%',
      tenantSatisfactionScore: '4.8/5.0',
    },
  });
});

// 13. Rent Collection Service
router.all('/rent-collection*', (req: Request, res: Response) => {
  res.json({
    service: 'rent-collection-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      mrrCollected: 284500,
      collectionEfficiencyPct: '98.2%',
      autoPayEnrollmentPct: '88.5%',
    },
  });
});

// 14. Maintenance Service
router.all('/maintenance*', (req: Request, res: Response) => {
  res.json({
    service: 'maintenance-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      openTicketsCount: 3,
      avgResolutionTimeHours: 14.2,
      emergencyRoutingStatus: 'ONLINE',
    },
  });
});

// 15. Asset Management Service
router.all('/asset-management*', (req: Request, res: Response) => {
  res.json({
    service: 'asset-management-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      portfolioAUM: 45000000,
      annualNOI: 3250000,
      portfolioYieldPct: 7.22,
    },
  });
});

// 16. Syndication Service
router.all('/syndication*', (req: Request, res: Response) => {
  res.json({
    service: 'syndication-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      activeFundsCount: 2,
      totalEquityRaised: 14500000,
      activeLpCount: 64,
    },
  });
});

// 17. Document Service
router.all('/document*', (req: Request, res: Response) => {
  res.json({
    service: 'document-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      vaultStorageProvider: 'S3-Compatible Secure Vault',
      totalDocumentsStored: 3420,
      ocrEngineStatus: 'HEALTHY',
    },
  });
});

// 18. Notification Service
router.all('/notification*', (req: Request, res: Response) => {
  res.json({
    service: 'notification-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      channels: ['Email (Resend)', 'SMS (Twilio)', 'Push (WebPush)'],
      delivered24hCount: 1240,
      deliverySuccessRatePct: '99.8%',
    },
  });
});

// 19. Analytics Service
router.all('/analytics*', (req: Request, res: Response) => {
  res.json({
    service: 'analytics-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      biEngine: 'RealEstateOS Executive Dashboard',
      activeDataStreams: 18,
      lastPipelineRun: new Date().toISOString(),
    },
  });
});

// 20. Market Intelligence Service
router.all('/market-intelligence*', (req: Request, res: Response) => {
  res.json({
    service: 'market-intelligence-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      coverageMarkets: ['Charlotte-Concord-Gastonia MSA', 'Raleigh-Durham MSA', 'Atlanta MSA'],
      trackedZipCodes: 45,
      macroScoreCharlotte: 88,
    },
  });
});

// 21. Inspection Service
router.all('/inspection*', (req: Request, res: Response) => {
  res.json({
    service: 'inspection-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      inspectionsCompletedThisMonth: 12,
      avgDefectResolutionDays: 4.5,
      ocrParserAccuracyPct: '96.8%',
    },
  });
});

// 22. Disposition Service
router.all('/disposition*', (req: Request, res: Response) => {
  res.json({
    service: 'disposition-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      activeDispositionPipelineCount: 2,
      totalTargetProceeds: 6800000,
      buyerMatchCount: 18,
    },
  });
});

// 23. Tax Service
router.all('/tax*', (req: Request, res: Response) => {
  res.json({
    service: 'tax-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      propertiesUnderTaxReview: 12,
      appealsFiledThisYear: 4,
      totalSavedTaxDollars: 38400,
    },
  });
});

// 24. Insurance Service
router.all('/insurance*', (req: Request, res: Response) => {
  res.json({
    service: 'insurance-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      activePoliciesCount: 12,
      totalInsuredValue: 48000000,
      claimsInPast12Mo: 0,
      riskGrade: 'A+',
    },
  });
});

// 25. Utility Management Service
router.all('/utility-management*', (req: Request, res: Response) => {
  res.json({
    service: 'utility-management-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      monitoredMetersCount: 148,
      monthlyUtilityBudget: 18500,
      anomalyDetectionEngine: 'ACTIVE',
    },
  });
});

// 26. Vendor Service
router.all('/vendor*', (req: Request, res: Response) => {
  res.json({
    service: 'vendor-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      registeredVendorsCount: 42,
      verifiedInsurancePct: '100%',
      topTrades: ['Plumbing', 'HVAC', 'Electrical', 'Roofing', 'General Contractor'],
    },
  });
});

// 27. Marketing Automation Service
router.all('/marketing-automation*', (req: Request, res: Response) => {
  res.json({
    service: 'marketing-automation-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      activeCampaignsCount: 4,
      emailsSentThisMonth: 14500,
      conversionRatePct: '4.2%',
    },
  });
});

// 28. E-Signature Service
router.all('/e-signature*', (req: Request, res: Response) => {
  res.json({
    service: 'e-signature-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      signatureEngine: 'RealEstateOS Native E-Sign / DocuSign Bridge',
      documentsPendingSignature: 2,
      completedSignaturesThisMonth: 34,
    },
  });
});

// 29. Audit Logging Service
router.all('/audit-logging*', (req: Request, res: Response) => {
  res.json({
    service: 'audit-logging-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      auditLogStore: 'Immutable Append-Only DB Log',
      loggedEvents24hCount: 4820,
      complianceStandard: 'SOC2-Compliant Audit Trail',
    },
  });
});

// 30. Spatial Service
router.all('/spatial*', (req: Request, res: Response) => {
  res.json({
    service: 'spatial-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      gisEngine: 'PostGIS Spatial Query Engine',
      trackedParcelsCount: 14200,
      zoningOverlayData: 'LOADED',
    },
  });
});

// 31. Construction Service
router.all('/construction*', (req: Request, res: Response) => {
  res.json({
    service: 'construction-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      activeRehabProjectsCount: 2,
      totalConstructionBudget: 420000,
      completionPctAverage: '64.5%',
    },
  });
});

// 32. Portfolio Optimization Service
router.all('/portfolio-optimization*', (req: Request, res: Response) => {
  res.json({
    service: 'portfolio-optimization-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      optimizerStatus: 'ACTIVE',
      sharpeRatio: 1.84,
      targetPortfolioIRR: '19.2%',
    },
  });
});

// 33. Investor Relations Service
router.all('/investor-relations*', (req: Request, res: Response) => {
  res.json({
    service: 'investor-relations-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      activeInvestorsCount: 64,
      totalDistributionsYTD: 850000,
      nextDistributionDate: '2026-10-01',
    },
  });
});

// 34. Accounting Service
router.all('/accounting*', (req: Request, res: Response) => {
  res.json({
    service: 'accounting-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      ledgerSystem: 'Double-Entry General Ledger',
      reconciledAccountsCount: 14,
      trialBalanceStatus: 'BALANCED',
    },
  });
});

// 35. AI Gateway Service
router.all('/ai-gateway*', (req: Request, res: Response) => {
  res.json({
    service: 'ai-gateway-service',
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      gatewayStatus: 'ONLINE',
      activeAgentsCount: 20,
      llmProxyProvider: 'RealEstateOS Anthropic / Gemini Hybrid Proxy',
      tokensProcessed24h: 184000,
    },
  });
});

// Generic parameterized route handler for GET /:serviceName/* and POST /:serviceName/*
router.all('/:serviceName*', (req: Request, res: Response) => {
  const { serviceName } = req.params;
  const foundInCatalog = SERVICES_CATALOG.find(
    (s) => s.id === serviceName || s.id === `${serviceName}-service` || s.route === `/api/${serviceName}`
  );
  res.json({
    service: foundInCatalog ? foundInCatalog.id : `${serviceName}-service`,
    status: 'active',
    endpoint: req.originalUrl,
    data: {
      serviceName,
      status: foundInCatalog ? foundInCatalog.status : 'HEALTHY',
      version: foundInCatalog ? foundInCatalog.version : '1.0.0',
      timestamp: new Date().toISOString(),
    },
  });
});

export default router;
