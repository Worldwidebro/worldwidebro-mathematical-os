'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import type { UserRole } from '@realestate-os/shared-types';
import { 
  Building2, 
  Shield, 
  Users, 
  DollarSign, 
  Hammer, 
  Briefcase, 
  Wrench, 
  Bot, 
  Network, 
  Code, 
  Layers, 
  FileText, 
  ArrowRight, 
  CheckCircle2, 
  ChevronRight, 
  Activity, 
  Terminal,
  Database,
  Search,
  Cpu,
  Copy,
  Check
} from 'lucide-react';
import { uiPrompts, UIPrompt } from '@/lib/ui-prompts';

export default function PlatformPortal() {
  const router = useRouter();
  const [selectedRole, setSelectedRole] = useState<UserRole | null>(null);
  const [selectedSector, setSelectedSector] = useState<string>('property-management');
  const [activeTab, setActiveTab] = useState<'sectors' | 'modules' | 'agents' | 'repo' | 'prompts'>('sectors');
  const [promptSearch, setPromptSearch] = useState('');
  const [selectedPromptCategory, setSelectedPromptCategory] = useState<string>('all');
  const [copiedId, setCopiedId] = useState<number | null>(null);

  const handleCopyPrompt = (text: string, id: number) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const promptCategories = [
    'all',
    'Brand & Visual Language',
    'Landing Pages',
    'Authentication',
    'Executive Dashboard',
    'CRM',
    'Property Management',
    'Brokerage',
    'Investing',
    'Construction',
    'Lending',
    'AI',
    'Documents',
    'Analytics',
    'Mobile',
    'Collaboration',
    'Settings & Administration'
  ];

  const filteredPrompts = uiPrompts.filter(p => {
    const matchesCategory = selectedPromptCategory === 'all' || p.category === selectedPromptCategory;
    const matchesSearch = p.text.toLowerCase().includes(promptSearch.toLowerCase()) || 
                          p.category.toLowerCase().includes(promptSearch.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  const handleContinue = () => {
    if (selectedRole) {
      router.push(`/register?role=${selectedRole}&sector=${selectedSector}`);
    }
  };

  const sectors = [
    {
      id: 'brokerage',
      title: 'Brokerage',
      icon: Briefcase,
      color: 'from-blue-600 to-cyan-500',
      description: 'Residential, Commercial, Luxury Brokerage, Listings & Buyer Representation.',
      bullets: ['MLS Sync & Auto Listings', 'Buyer/Seller CRM Pipelines', 'Showing Request Orchestration']
    },
    {
      id: 'property-management',
      title: 'Property Management',
      icon: Building2,
      color: 'from-emerald-600 to-teal-500',
      description: 'Residential, Multifamily, Commercial, HOA & Corporate Housing Operations.',
      bullets: ['Automated Rent Collection', 'Tenant Screening & Portals', 'Maintenance Ticket Triage']
    },
    {
      id: 'investing',
      title: 'Investing & Syndication',
      icon: DollarSign,
      color: 'from-amber-600 to-yellow-500',
      description: 'Buy & Hold, BRRRR, House Flipping, Private Equity & REIT Operations.',
      bullets: ['Underwriting & Cash Flow Modeling', 'Cap Rate & IRR Calculators', 'Waterfalls & Exit Analysis']
    },
    {
      id: 'development',
      title: 'Development & Build',
      icon: Hammer,
      color: 'from-purple-600 to-pink-500',
      description: 'Land acquisition, Build-to-Rent, Mixed-Use & Residential Development.',
      bullets: ['Permit & RFI Logging', 'Subcontractor Tendering', 'Budget & Change Order Audits']
    },
    {
      id: 'lending',
      title: 'Lending & Debt',
      icon: Shield,
      color: 'from-rose-600 to-orange-500',
      description: 'Hard Money, Construction Loans, Private Credit & Mortgage Brokerage.',
      bullets: ['Loan Underwriting Engine', 'Draw Requests & Funding Logs', 'Risk Assessment Analytics']
    },
    {
      id: 'marketplace',
      title: 'Marketplace',
      icon: Network,
      color: 'from-indigo-600 to-purple-500',
      description: 'Connecting buyers, sellers, vendors, wholesale deals & contractors.',
      bullets: ['Vendor Matching Algorithm', 'Wholesale Deal Pipelines', 'Contractor Bid Matrices']
    }
  ];

  const modules = [
    { title: 'Identity', desc: 'SSO, multi-tenant RBAC policies, and granular permissions.', status: 'Active' },
    { title: 'CRM', desc: 'Unified communication timelines, notes, pipeline tracking, SMS & calling.', status: 'Active' },
    { title: 'Property Manager', desc: 'Lease contracts, move logs, maintenance ticketing, Stripe billing.', status: 'Active' },
    { title: 'Listings', desc: 'Photos, virtual tours, open house scheduling, MLS sync gateways.', status: 'Active' },
    { title: 'Investments', desc: 'NOI, Cap Rates, cash flow models, debt waterfalls, exit analysis.', status: 'Beta' },
    { title: 'Construction', desc: 'Daily logs, RFIs, subcontractor schedules, materials auditing.', status: 'Beta' },
    { title: 'Finance', desc: 'General ledger, payroll, invoice processing, bank reconciliations.', status: 'Beta' },
    { title: 'Lending', desc: 'Applications, collateral tracking, underwriting logs, draw pipelines.', status: 'Beta' }
  ];

  const aiAgents = [
    { name: 'Acquisition Agent', role: 'Analyzes listings, calculates cash-on-cash return, files offer sheets.' },
    { name: 'Underwriting Agent', role: 'Extracts rent rolls, builds debt waterfall models, calculates IRR.' },
    { name: 'Maintenance Dispatcher', role: 'Triages tenant maintenance reports, matches local vendors, approves tickets.' },
    { name: 'Lease Renewal Agent', role: 'Monitors lease end-dates, drafts agreements, triggers renewals via e-sign.' },
    { name: 'MLS Sync Agent', role: 'Synchronizes external MLS property feeds with internal listing indices.' },
    { name: 'Invoice processing Agent', role: 'Ingests subcontractor invoices via OCR, reconciles against budgets.' }
  ];

  const repoFiles = [
    'identity/', 'auth/', 'api-gateway/', 'crm/', 'property-service/', 'listings/',
    'mls-sync/', 'acquisitions/', 'underwriting/', 'investments/', 'finance/',
    'accounting/', 'lending/', 'property-management/', 'leasing/', 'maintenance/',
    'vendors/', 'construction/', 'development/', 'documents/', 'workflows/',
    'ai-agents/', 'knowledge-graph/', 'rag/', 'analytics/', 'web/', 'mobile/',
    'customer-portal/', 'owner-portal/', 'tenant-portal/', 'investor-portal/',
    'vendor-portal/', 'integrations/', 'observability/', 'devops/'
  ];

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100 font-sans flex flex-col justify-between overflow-x-hidden selection:bg-emerald-500 selection:text-black">
      {/* Background Glow Effect */}
      <div className="absolute top-0 left-1/4 w-[500px] h-[500px] bg-emerald-500/10 rounded-full blur-[120px] pointer-events-none" />
      <div className="absolute top-1/3 right-1/4 w-[600px] h-[600px] bg-blue-500/5 rounded-full blur-[150px] pointer-events-none" />

      {/* Top Navbar */}
      <header className="relative max-w-7xl mx-auto w-full px-6 py-6 flex items-center justify-between border-b border-gray-900 bg-gray-950/80 backdrop-blur-md z-30">
        <div className="flex items-center gap-3">
          <div className="h-10 w-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-cyan-500 flex items-center justify-center font-black text-white text-xl tracking-tighter shadow-lg shadow-emerald-950/40">
            RE
          </div>
          <div>
            <h1 className="text-base font-bold text-white tracking-tight flex items-center gap-1.5">
              RealEstateOS <span className="text-[10px] bg-emerald-950 border border-emerald-800 text-emerald-400 px-1.5 py-0.5 rounded font-medium">v1.0</span>
            </h1>
            <p className="text-[10px] text-gray-400">AI Boss Holdings Delegation Platform</p>
          </div>
        </div>

        <div className="flex items-center gap-4 text-xs">
          <Link href="/login" className="px-4 py-2 border border-gray-800 hover:bg-gray-900 rounded-lg text-gray-300 font-medium transition-colors">
            Sign In
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <main className="relative max-w-7xl mx-auto w-full px-6 py-12 md:py-20 z-20 grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        {/* Left Hand: Platform Value Prop */}
        <div className="lg:col-span-7 space-y-8">
          <div className="space-y-4">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-950/40 border border-emerald-900/60 text-emerald-400 text-xs font-semibold">
              <Bot className="h-3.5 w-3.5" /> Launching Real Estate Companies with AI Agents
            </div>
            <h2 className="text-4xl md:text-5xl font-black text-white tracking-tight leading-tight">
              One Operating System for the Entire <span className="bg-gradient-to-r from-emerald-400 to-cyan-400 bg-clip-text text-transparent">Property Lifecycle</span>.
            </h2>
            <p className="text-sm md:text-base text-gray-400 leading-relaxed max-w-2xl">
              An AI-native operating system designed to run brokerages, investment funds, development pipelines, lending desks, and property managers from a shared modular architecture.
            </p>
          </div>

          {/* PRD Tabs */}
          <div className="border border-gray-900 rounded-xl bg-gray-900/40 overflow-hidden backdrop-blur-sm">
            {/* Tabs Header */}
            <div className="flex bg-gray-950 border-b border-gray-900 text-xs">
              <button 
                onClick={() => setActiveTab('sectors')}
                className={`flex-1 py-3 font-semibold transition-all border-b-2 ${
                  activeTab === 'sectors' ? 'border-emerald-500 text-white bg-gray-900/20' : 'border-transparent text-gray-400 hover:text-white'
                }`}
              >
                Business Models
              </button>
              <button 
                onClick={() => setActiveTab('modules')}
                className={`flex-1 py-3 font-semibold transition-all border-b-2 ${
                  activeTab === 'modules' ? 'border-emerald-500 text-white bg-gray-900/20' : 'border-transparent text-gray-400 hover:text-white'
                }`}
              >
                Core Modules
              </button>
              <button 
                onClick={() => setActiveTab('agents')}
                className={`flex-1 py-3 font-semibold transition-all border-b-2 ${
                  activeTab === 'agents' ? 'border-emerald-500 text-white bg-gray-900/20' : 'border-transparent text-gray-400 hover:text-white'
                }`}
              >
                AI Agent Network
              </button>
              <button 
                onClick={() => setActiveTab('repo')}
                className={`flex-1 py-3 font-semibold transition-all border-b-2 ${
                  activeTab === 'repo' ? 'border-emerald-500 text-white bg-gray-900/20' : 'border-transparent text-gray-400 hover:text-white'
                }`}
              >
                Repository Spec
              </button>
              <button 
                onClick={() => setActiveTab('prompts')}
                className={`flex-1 py-3 font-semibold transition-all border-b-2 ${
                  activeTab === 'prompts' ? 'border-emerald-500 text-white bg-gray-900/20' : 'border-transparent text-gray-400 hover:text-white'
                }`}
              >
                UI Prompt DB
              </button>
            </div>

            {/* Tabs Body */}
            <div className="p-6">
              {activeTab === 'sectors' && (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {sectors.map(sec => (
                    <div key={sec.id} className="p-4 bg-gray-950/60 border border-gray-800/80 rounded-lg hover:border-gray-700 transition-all flex flex-col justify-between space-y-3">
                      <div>
                        <div className="flex items-center gap-2 mb-1.5">
                          <div className={`p-1.5 rounded bg-gradient-to-tr ${sec.color} text-white`}>
                            <sec.icon className="h-4 w-4" />
                          </div>
                          <h4 className="font-bold text-sm text-white">{sec.title}</h4>
                        </div>
                        <p className="text-xs text-gray-400 leading-relaxed">{sec.description}</p>
                      </div>
                      <ul className="space-y-1 text-[10px] text-gray-500 border-t border-gray-900 pt-2.5">
                        {sec.bullets.map((b, idx) => (
                          <li key={idx} className="flex items-center gap-1.5">
                            <span className="h-1 w-1 bg-emerald-500 rounded-full" />
                            {b}
                          </li>
                        ))}
                      </ul>
                    </div>
                  ))}
                </div>
              )}

              {activeTab === 'modules' && (
                <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                  {modules.map(mod => (
                    <div key={mod.title} className="p-3 bg-gray-950/60 border border-gray-800/80 rounded-lg space-y-1.5">
                      <div className="flex items-center justify-between">
                        <h4 className="font-bold text-xs text-white">{mod.title}</h4>
                        <span className={`text-[9px] px-1 rounded font-bold uppercase tracking-wider ${
                          mod.status === 'Active' ? 'bg-emerald-950/60 border border-emerald-900 text-emerald-400' : 'bg-amber-950/60 border border-amber-900 text-amber-500'
                        }`}>
                          {mod.status}
                        </span>
                      </div>
                      <p className="text-[10px] text-gray-400 leading-relaxed">{mod.desc}</p>
                    </div>
                  ))}
                </div>
              )}

              {activeTab === 'agents' && (
                <div className="space-y-3">
                  <div className="flex items-center justify-between border-b border-gray-900 pb-2 text-[10px] text-gray-400">
                    <span>AGENT NAME</span>
                    <span>PRIMARY DELEGATION ROLE</span>
                  </div>
                  {aiAgents.map(agent => (
                    <div key={agent.name} className="flex flex-wrap items-center justify-between gap-2 py-1 border-b border-gray-900/60">
                      <div className="flex items-center gap-2">
                        <Cpu className="h-3.5 w-3.5 text-emerald-400" />
                        <span className="font-bold text-xs text-white">{agent.name}</span>
                      </div>
                      <span className="text-[11px] text-gray-400">{agent.role}</span>
                    </div>
                  ))}
                </div>
              )}

              {activeTab === 'repo' && (
                <div className="bg-gray-950/90 rounded-lg p-4 font-mono text-[10px] text-emerald-400 border border-gray-850 max-h-[300px] overflow-y-auto">
                  <div className="flex items-center gap-2 text-gray-400 border-b border-gray-900 pb-2 mb-2">
                    <Terminal className="h-4 w-4" />
                    <span>realestate-os/ folder layout (PRD Section 11)</span>
                  </div>
                  <div className="grid grid-cols-2 md:grid-cols-3 gap-2">
                    {repoFiles.map(file => (
                      <div key={file} className="flex items-center gap-1.5 hover:text-white transition-colors cursor-default">
                        <Code className="h-3 w-3 text-cyan-400" />
                        <span>{file}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {activeTab === 'prompts' && (
                <div className="space-y-4">
                  {/* Category filters */}
                  <div className="flex flex-wrap gap-1 mb-2 max-h-[80px] overflow-y-auto border-b border-gray-900 pb-2">
                    {promptCategories.map(cat => (
                      <button
                        key={cat}
                        onClick={() => setSelectedPromptCategory(cat)}
                        className={`px-2 py-0.5 rounded text-[9px] font-medium transition-all ${
                          selectedPromptCategory === cat 
                            ? 'bg-emerald-600 text-white font-bold' 
                            : 'bg-gray-950 border border-gray-800 text-gray-400 hover:text-white hover:border-gray-700'
                        }`}
                      >
                        {cat}
                      </button>
                    ))}
                  </div>

                  {/* Search bar */}
                  <div className="relative">
                    <Search className="absolute left-3 top-2.5 h-3.5 w-3.5 text-gray-500" />
                    <input
                      type="text"
                      placeholder="Search 100 design prompts..."
                      value={promptSearch}
                      onChange={e => setPromptSearch(e.target.value)}
                      className="w-full bg-gray-950 border border-gray-800 rounded-lg pl-9 pr-4 py-2 text-xs text-white focus:outline-none focus:border-emerald-500"
                    />
                  </div>

                  {/* Prompts list */}
                  <div className="space-y-2.5 max-h-[220px] overflow-y-auto pr-1">
                    {filteredPrompts.map(p => (
                      <div key={p.id} className="p-3 bg-gray-950/60 border border-gray-800/80 rounded-lg flex items-start justify-between gap-3 hover:border-gray-750 transition-all">
                        <div className="space-y-1">
                          <span className="inline-block text-[8px] px-1 py-0.2 rounded font-bold uppercase bg-gray-900 border border-gray-800 text-cyan-400">
                            {p.category}
                          </span>
                          <p className="text-[11px] text-gray-300 leading-relaxed">{p.text}</p>
                        </div>
                        <button
                          onClick={() => handleCopyPrompt(p.text, p.id)}
                          className="flex-shrink-0 p-1 rounded bg-gray-900 hover:bg-gray-850 border border-gray-800 hover:border-gray-700 transition-all text-gray-400 hover:text-white"
                          title="Copy prompt"
                        >
                          {copiedId === p.id ? (
                            <Check className="h-3 w-3 text-emerald-500" />
                          ) : (
                            <Copy className="h-3 w-3" />
                          )}
                        </button>
                      </div>
                    ))}
                    {filteredPrompts.length === 0 && (
                      <div className="text-center py-8 text-gray-500 text-xs">
                        No prompts matched your search.
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Right Hand: Interactive Portal Action Box */}
        <div className="lg:col-span-5 bg-gray-900/60 border border-gray-800/80 rounded-2xl p-6 md:p-8 backdrop-blur-md shadow-2xl relative">
          <div className="absolute top-0 right-0 h-12 w-12 bg-emerald-500/10 rounded-full blur-xl pointer-events-none" />
          
          <div className="space-y-2 mb-6">
            <h3 className="text-xl font-bold text-white tracking-tight">Access Terminal</h3>
            <p className="text-xs text-gray-400">Configure your workspace context to enter the operations suite.</p>
          </div>

          <div className="space-y-6">
            {/* Step 1: Select Business Sector */}
            <div className="space-y-2">
              <label className="block text-[11px] font-bold text-gray-400 uppercase tracking-wider">1. Select Business Sector</label>
              <select 
                value={selectedSector}
                onChange={e => setSelectedSector(e.target.value)}
                className="w-full bg-gray-950 border border-gray-800 hover:border-gray-700 rounded-xl px-4 py-3 text-xs text-white focus:outline-none focus:border-emerald-500 transition-colors"
              >
                <option value="property-management">Property Management (PM-OS)</option>
                <option value="brokerage">Brokerage & MLS Operations</option>
                <option value="investing">Investing & Private Equity</option>
                <option value="development">Development & Construction</option>
                <option value="lending">Lending & Draw Pipelines</option>
              </select>
            </div>

            {/* Step 2: Choose Role */}
            <div className="space-y-3">
              <label className="block text-[11px] font-bold text-gray-400 uppercase tracking-wider">2. Choose Role context</label>
              
              <div className="grid grid-cols-1 gap-3">
                <button
                  type="button"
                  onClick={() => setSelectedRole('landlord')}
                  className={`p-4 rounded-xl border transition-all text-left flex items-start gap-3.5 ${
                    selectedRole === 'landlord'
                      ? 'border-emerald-500 bg-emerald-950/20'
                      : 'border-gray-800 bg-gray-950/30 hover:border-gray-700'
                  }`}
                >
                  <div className={`p-2 rounded-lg ${selectedRole === 'landlord' ? 'bg-emerald-600 text-white' : 'bg-gray-800 text-gray-400'}`}>
                    <Building2 className="h-5 w-5" />
                  </div>
                  <div>
                    <h4 className="font-bold text-xs text-white">🏢 Landlord / General Operator</h4>
                    <p className="text-[10px] text-gray-400 mt-1 leading-relaxed">Administer assets, manage templates, run underwriting pipelines.</p>
                  </div>
                </button>

                <button
                  type="button"
                  onClick={() => setSelectedRole('tenant')}
                  className={`p-4 rounded-xl border transition-all text-left flex items-start gap-3.5 ${
                    selectedRole === 'tenant'
                      ? 'border-emerald-500 bg-emerald-950/20'
                      : 'border-gray-800 bg-gray-950/30 hover:border-gray-700'
                  }`}
                >
                  <div className={`p-2 rounded-lg ${selectedRole === 'tenant' ? 'bg-emerald-600 text-white' : 'bg-gray-800 text-gray-400'}`}>
                    <Users className="h-5 w-5" />
                  </div>
                  <div>
                    <h4 className="font-bold text-xs text-white">👤 Tenant / Client Resident</h4>
                    <p className="text-[10px] text-gray-400 mt-1 leading-relaxed">Pay statements, submit maintenance tickets, request loan draws.</p>
                  </div>
                </button>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="space-y-4 pt-2">
              <button
                onClick={handleContinue}
                disabled={!selectedRole}
                className="w-full py-3 bg-gradient-to-r from-emerald-600 to-cyan-500 disabled:from-gray-800 disabled:to-gray-850 hover:from-emerald-700 hover:to-cyan-600 disabled:cursor-not-allowed text-white font-bold text-xs rounded-xl flex items-center justify-center gap-1.5 transition-all shadow-lg shadow-emerald-900/10"
              >
                Enter Portal Onboarding
                <ArrowRight className="h-4 w-4" />
              </button>

              <div className="flex items-center justify-center gap-1 text-[11px] text-gray-400">
                <span>Already have a workspace account?</span>
                <Link href="/login" className="text-emerald-400 hover:text-emerald-300 font-bold transition-colors">
                  Login Here
                </Link>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* Footer / Stats Section */}
      <footer className="relative max-w-7xl mx-auto w-full px-6 py-8 border-t border-gray-900 bg-gray-950 text-gray-500 text-[10px] z-20 flex flex-col md:flex-row items-center justify-between gap-4">
        <div>
          <p>© {new Date().getFullYear()} AI Boss Holdings. RealEstateOS is powered by Worldwidebro OS delegation.</p>
        </div>
        <div className="flex items-center gap-6">
          <span>Charlotte, NC Operations</span>
          <span>99.9% Uptime SLA</span>
          <span>Neo4j Sector Map Alignment</span>
        </div>
      </footer>
    </div>
  );
}
