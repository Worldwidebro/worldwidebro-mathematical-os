// Auth & User Types
export type UserRole = 'landlord' | 'tenant' | 'admin' | 'broker' | 'investor' | 'vendor' | 'agent' | 'org_admin' | 'org_member';

export interface User {
  id: string;
  email: string;
  fullName: string;
  role: UserRole;
  phone?: string;
  avatarUrl?: string;
  organizationId?: string;
  createdAt: string;
  updatedAt: string;
}

export interface Profile {
  id: string;
  userId: string;
  bio?: string;
  companyName?: string;
  jobTitle?: string;
  phoneNumber?: string;
  address?: string;
  city?: string;
  state?: string;
  zip?: string;
  preferences?: Record<string, unknown>;
  metadata?: Record<string, unknown>;
  createdAt: string;
  updatedAt: string;
}

export interface AuthToken {
  accessToken: string;
  refreshToken: string;
  user: Omit<User, 'createdAt' | 'updatedAt'>;
}

export interface AuthError {
  error: string;
  code?: string;
}

// Organizational Context Types
export interface Organization {
  id: string;
  name: string;
  slug: string;
  taxId?: string;
  domain?: string;
  logoUrl?: string;
  settings?: Record<string, unknown>;
  createdAt: string;
  updatedAt: string;
}

export interface OrgMember {
  id: string;
  organizationId: string;
  userId: string;
  role: 'owner' | 'admin' | 'member' | 'viewer';
  permissions?: string[];
  createdAt: string;
  updatedAt: string;
}

export interface OrgContext {
  organization: Organization;
  currentMember: OrgMember;
  activeRole: string;
  permissions: string[];
}

// Property, Unit & Listing Types
export interface Property {
  id: string;
  landlordId: string;
  organizationId?: string;
  name?: string;
  address: string;
  city: string;
  state: string;
  zip: string;
  totalUnits: number;
  propertyType?: 'residential' | 'commercial' | 'mixed_use' | 'industrial';
  squareFeet?: number;
  yearBuilt?: number;
  createdAt: string;
  updatedAt: string;
}

export interface Unit {
  id: string;
  propertyId: string;
  unitNumber: string;
  tenantId?: string;
  monthlyRent: number;
  deposit?: number;
  bedrooms?: number;
  bathrooms?: number;
  squareFeet?: number;
  status?: 'vacant' | 'occupied' | 'maintenance' | 'reserved';
  leaseStartDate: string;
  leaseEndDate: string;
  createdAt: string;
  updatedAt: string;
}

export type ListingStatus = 'draft' | 'active' | 'pending' | 'leased' | 'sold' | 'archived';

export interface Listing {
  id: string;
  propertyId: string;
  unitId?: string;
  title: string;
  description: string;
  price: number;
  status: ListingStatus;
  bedrooms?: number;
  bathrooms?: number;
  squareFeet?: number;
  images: string[];
  amenities?: string[];
  availableDate: string;
  createdAt: string;
  updatedAt: string;
}

export interface Tenant {
  id: string;
  email: string;
  fullName: string;
  phone?: string;
  unitId: string;
  createdAt: string;
  updatedAt: string;
}

// Mortgage & Loan Types
export type UnderwritingStatus = 'draft' | 'submitted' | 'under_review' | 'approved' | 'conditional_approval' | 'rejected' | 'withdrawn';

export interface Borrower {
  id: string;
  userId?: string;
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  ssnMasked?: string;
  creditScore?: number;
  annualIncome?: number;
  employer?: string;
  createdAt: string;
  updatedAt: string;
}

export interface LoanApplication {
  id: string;
  borrowerId: string;
  propertyId?: string;
  requestedAmount: number;
  loanTermMonths: number;
  interestRate?: number;
  loanType: 'conventional' | 'fha' | 'va' | 'jumbo' | 'commercial';
  status: UnderwritingStatus;
  documents?: string[];
  submittedAt?: string;
  decisionDate?: string;
  createdAt: string;
  updatedAt: string;
}

// AI Agent Types
export type AgentCategory =
  | 'acquisition'
  | 'underwriting'
  | 'valuation'
  | 'crm'
  | 'marketing'
  | 'tenant'
  | 'leasing'
  | 'finance'
  | 'operations'
  | 'legal'
  | 'asset_management'
  | 'investor_relations'
  | 'inspection'
  | 'market'
  | 'tax'
  | 'insurance'
  | 'utility'
  | 'disposition';

export type AgentStatus = 'idle' | 'running' | 'active' | 'completed' | 'failed' | 'paused';

export interface AgentMetadata {
  agentId?: string;
  name: string;
  displayName?: string;
  version: string;
  description: string;
  category?: AgentCategory | string;
  capabilities?: string[];
  status: AgentStatus;
  author?: string;
  lastActiveAt?: string;
}

export interface AgentInvocationRequest {
  requestId: string;
  agentId: string;
  prompt: string;
  context?: Record<string, unknown>;
  parameters?: Record<string, unknown>;
  requestedBy: string;
  timestamp: string;
}

export interface AgentInvocationResponse {
  requestId: string;
  agentId: string;
  status: 'success' | 'failure';
  output: string;
  data?: Record<string, unknown>;
  tokensUsed?: number;
  executionTimeMs: number;
  timestamp: string;
}

export interface AgentExecutionLog {
  id?: string;
  agentId?: string;
  requestId?: string;
  timestamp: string;
  level: 'info' | 'warn' | 'error' | 'debug';
  message: string;
  details?: Record<string, unknown>;
  metadata?: Record<string, any>;
  step?: string;
  toolInvocation?: any;
  durationMs?: number;
}

export interface AgentExecutionResult {
  success: boolean;
  agentName: string;
  timestamp: string;
  executionTimeMs: number;
  logs: AgentExecutionLog[];
  output: Record<string, any>;
  error?: string;
}


// Payment Types
export interface RentPayment {
  id: string;
  unitId: string;
  tenantId: string;
  amount: number;
  dueDate: string;
  paidDate?: string;
  status: 'pending' | 'paid' | 'late' | 'failed';
  stripePaymentId?: string;
  createdAt: string;
  updatedAt: string;
}

// Maintenance Types
export interface MaintenanceRequest {
  id: string;
  propertyId: string;
  unitId: string;
  tenantId: string;
  description: string;
  priority: 'low' | 'medium' | 'high';
  status: 'open' | 'in_progress' | 'completed' | 'cancelled';
  photoUrl?: string;
  createdAt: string;
  updatedAt: string;
}

// Onboarding Types
export interface LandlordOnboardingData {
  step1: {
    fullName: string;
    phone: string;
    company?: string;
  };
  step2: {
    properties: Array<{
      address: string;
      city: string;
      state: string;
      zip: string;
      units: number;
    }>;
  };
  step3: {
    tenants: Array<{
      email: string;
      unitNumber?: string;
    }>;
  };
}

export interface TenantOnboardingData {
  email: string;
  password: string;
  fullName?: string;
  phone?: string;
  paymentMethodId?: string;
  leaseAccepted: boolean;
}

// API Response Types
export interface ApiResponse<T> {
  data?: T;
  error?: string;
  code?: string;
}

export interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  perPage: number;
}

// Dashboard Types
export interface DashboardStats {
  totalProperties: number;
  totalUnits: number;
  activeLeases: number;
  collectionRate: number;
  monthlyRecurringRevenue: number;
  pendingPayments: number;
}

export interface PropertySummary extends Property {
  units: number;
  occupiedUnits: number;
  nextRentDate?: string;
  monthlyRevenue: number;
}

// Admin Types
export interface AdminStats {
  activeUsers: number;
  collectionRate: number;
  monthlyRecurringRevenue: number;
  pendingMaintenance: number;
  failedPayments: number;
}
