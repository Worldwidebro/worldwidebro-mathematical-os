export interface UIPrompt {
  id: number;
  category: string;
  text: string;
}

export const uiPrompts: UIPrompt[] = [
  // 1. Brand & Visual Language
  { id: 1, category: 'Brand & Visual Language', text: 'Design a premium AI-powered RealEstateOS landing page using modern enterprise SaaS aesthetics, generous whitespace, glassmorphism accents, rounded cards, and a blue, emerald, charcoal, and white palette.' },
  { id: 2, category: 'Brand & Visual Language', text: 'Create a complete design system with typography, spacing, color tokens, iconography, elevation, and component guidelines.' },
  { id: 3, category: 'Brand & Visual Language', text: 'Design a futuristic dashboard inspired by Bloomberg Terminal meets Linear meets Notion.' },
  { id: 4, category: 'Brand & Visual Language', text: 'Create an AI-native interface where intelligence feels embedded into every screen.' },
  { id: 5, category: 'Brand & Visual Language', text: 'Design a responsive layout that scales seamlessly from desktop to tablet and mobile.' },

  // 2. Landing Pages
  { id: 6, category: 'Landing Pages', text: 'Hero section showcasing the complete real estate lifecycle.' },
  { id: 7, category: 'Landing Pages', text: 'Enterprise landing page for institutional investors.' },
  { id: 8, category: 'Landing Pages', text: 'Property management marketing page.' },
  { id: 9, category: 'Landing Pages', text: 'Brokerage marketing page.' },
  { id: 10, category: 'Landing Pages', text: 'Real estate developer marketing page.' },
  { id: 11, category: 'Landing Pages', text: 'Lending platform landing page.' },
  { id: 12, category: 'Landing Pages', text: 'AI automation showcase page.' },
  { id: 13, category: 'Landing Pages', text: 'Marketplace landing page.' },
  { id: 14, category: 'Landing Pages', text: 'Customer success stories page.' },
  { id: 15, category: 'Landing Pages', text: 'Pricing page with SaaS tiers and enterprise plans.' },

  // 3. Authentication
  { id: 16, category: 'Authentication', text: 'Modern login page with SSO options.' },
  { id: 17, category: 'Authentication', text: 'Multi-step organization onboarding.' },
  { id: 18, category: 'Authentication', text: 'Team invitation flow.' },
  { id: 19, category: 'Authentication', text: 'Workspace creation wizard.' },
  { id: 20, category: 'Authentication', text: 'Role selection experience.' },

  // 4. Executive Dashboard
  { id: 21, category: 'Executive Dashboard', text: 'Executive command center with KPIs, revenue, occupancy, and AI insights.' },
  { id: 22, category: 'Executive Dashboard', text: 'CEO dashboard highlighting portfolio health.' },
  { id: 23, category: 'Executive Dashboard', text: 'CFO financial analytics workspace.' },
  { id: 24, category: 'Executive Dashboard', text: 'COO operations overview.' },
  { id: 25, category: 'Executive Dashboard', text: 'Interactive executive map of all managed properties.' },

  // 5. CRM
  { id: 26, category: 'CRM', text: 'Lead pipeline with Kanban stages.' },
  { id: 27, category: 'CRM', text: 'Contact profile with timeline and communication history.' },
  { id: 28, category: 'CRM', text: 'Company account overview.' },
  { id: 29, category: 'CRM', text: 'AI-assisted lead qualification interface.' },
  { id: 30, category: 'CRM', text: 'Deal tracking workspace.' },

  // 6. Property Management
  { id: 31, category: 'Property Management', text: 'Portfolio overview with occupancy heatmaps.' },
  { id: 32, category: 'Property Management', text: 'Property detail page.' },
  { id: 33, category: 'Property Management', text: 'Building and unit hierarchy.' },
  { id: 34, category: 'Property Management', text: 'Lease management dashboard.' },
  { id: 35, category: 'Property Management', text: 'Maintenance request center.' },
  { id: 36, category: 'Property Management', text: 'Work order tracking.' },
  { id: 37, category: 'Property Management', text: 'Tenant portal dashboard.' },
  { id: 38, category: 'Property Management', text: 'Owner portal dashboard.' },
  { id: 39, category: 'Property Management', text: 'Rent collection analytics.' },
  { id: 40, category: 'Property Management', text: 'Vendor assignment workspace.' },

  // 7. Brokerage
  { id: 41, category: 'Brokerage', text: 'MLS search experience.' },
  { id: 42, category: 'Brokerage', text: 'Interactive listing management page.' },
  { id: 43, category: 'Brokerage', text: 'Buyer dashboard.' },
  { id: 44, category: 'Brokerage', text: 'Seller dashboard.' },
  { id: 45, category: 'Brokerage', text: 'Showing scheduler with calendar.' },
  { id: 46, category: 'Brokerage', text: 'Offer management interface.' },
  { id: 47, category: 'Brokerage', text: 'Transaction coordinator workspace.' },
  { id: 48, category: 'Brokerage', text: 'Closing workflow timeline.' },

  // 8. Investing
  { id: 49, category: 'Investing', text: 'Acquisition pipeline.' },
  { id: 50, category: 'Investing', text: 'Property underwriting interface.' },
  { id: 51, category: 'Investing', text: 'Investment committee dashboard.' },
  { id: 52, category: 'Investing', text: 'Portfolio analytics.' },
  { id: 53, category: 'Investing', text: 'Capital stack visualization.' },
  { id: 54, category: 'Investing', text: 'Waterfall distribution interface.' },
  { id: 55, category: 'Investing', text: 'Cash flow forecasting dashboard.' },
  { id: 56, category: 'Investing', text: 'Investor reporting portal.' },

  // 9. Construction
  { id: 57, category: 'Construction', text: 'Construction project dashboard.' },
  { id: 58, category: 'Construction', text: 'Gantt schedule interface.' },
  { id: 59, category: 'Construction', text: 'Budget tracking workspace.' },
  { id: 60, category: 'Construction', text: 'Daily field reports.' },
  { id: 61, category: 'Construction', text: 'RFI management.' },
  { id: 62, category: 'Construction', text: 'Change order workflow.' },
  { id: 63, category: 'Construction', text: 'Permit tracking dashboard.' },
  { id: 64, category: 'Construction', text: 'Punch list interface.' },

  // 10. Lending
  { id: 65, category: 'Lending', text: 'Loan origination workflow.' },
  { id: 66, category: 'Lending', text: 'Borrower profile.' },
  { id: 67, category: 'Lending', text: 'Underwriting workspace.' },
  { id: 68, category: 'Lending', text: 'Construction draw management.' },
  { id: 69, category: 'Lending', text: 'Risk scoring dashboard.' },
  { id: 70, category: 'Lending', text: 'Portfolio lending analytics.' },

  // 11. AI
  { id: 71, category: 'AI', text: 'AI copilot chat integrated into every page.' },
  { id: 72, category: 'AI', text: 'Natural language property search.' },
  { id: 73, category: 'AI', text: 'AI-generated investment recommendations.' },
  { id: 74, category: 'AI', text: 'AI workflow automation builder.' },
  { id: 75, category: 'AI', text: 'AI document summarization.' },
  { id: 76, category: 'AI', text: 'Predictive maintenance dashboard.' },
  { id: 77, category: 'AI', text: 'AI valuation engine visualization.' },
  { id: 78, category: 'AI', text: 'Autonomous task execution timeline.' },

  // 12. Documents
  { id: 79, category: 'Documents', text: 'Digital document vault.' },
  { id: 80, category: 'Documents', text: 'Contract review interface.' },
  { id: 81, category: 'Documents', text: 'OCR extraction results.' },
  { id: 82, category: 'Documents', text: 'E-signature workflow.' },
  { id: 83, category: 'Documents', text: 'Version history comparison.' },

  // 13. Analytics
  { id: 84, category: 'Analytics', text: 'Business intelligence dashboard.' },
  { id: 85, category: 'Analytics', text: 'Geographic portfolio heatmap.' },
  { id: 86, category: 'Analytics', text: 'Occupancy analytics.' },
  { id: 87, category: 'Analytics', text: 'Revenue forecasting.' },
  { id: 88, category: 'Analytics', text: 'Executive KPI scorecards.' },

  // 14. Mobile
  { id: 89, category: 'Mobile', text: 'Mobile property management app.' },
  { id: 90, category: 'Mobile', text: 'Mobile maintenance technician app.' },
  { id: 91, category: 'Mobile', text: 'Mobile brokerage CRM.' },
  { id: 92, category: 'Mobile', text: 'Mobile investor dashboard.' },

  // 15. Collaboration
  { id: 93, category: 'Collaboration', text: 'Activity feed with comments.' },
  { id: 94, category: 'Collaboration', text: 'Team workspace with assignments.' },
  { id: 95, category: 'Collaboration', text: 'Notification center.' },
  { id: 96, category: 'Collaboration', text: 'Calendar and scheduling hub.' },

  // 16. Settings & Administration
  { id: 97, category: 'Settings & Administration', text: 'Organization settings with multi-tenant controls.' },
  { id: 98, category: 'Settings & Administration', text: 'Permissions and RBAC management.' },
  { id: 99, category: 'Settings & Administration', text: 'Integration marketplace.' },
  { id: 100, category: 'Settings & Administration', text: 'System administration dashboard with monitoring, audit logs, API usage, and AI health.' }
];
