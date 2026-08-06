import { Router, Request, Response } from 'express';

export const dashboardRouter = Router();

// ==========================================
// IN-MEMORY DATA STORE (INITIAL STATE)
// ==========================================
const Store = {
  workspaces: [
    { id: 'iza-prod', name: 'IZA OS', env: 'prod', color: '#a78bfa', initials: 'IZ' },
    { id: 'iza-staging', name: 'IZA OS', env: 'staging', color: '#f59e0b', initials: 'IZ' },
    { id: 'hermes-lab', name: 'Hermes Lab', env: 'dev', color: '#22d3ee', initials: 'HL' },
  ],
  currentWorkspace: 'iza-prod',
  OPCOS: [
    { id: 'tech', name: 'Technology', color: '#22d3ee', icon: '⚙' },
    { id: 'fin',  name: 'Finance',    color: '#10b981', icon: '$' },
    { id: 'ops',  name: 'Operations', color: '#f59e0b', icon: '◈' },
    { id: 'mkt',  name: 'Marketing',  color: '#ec4899', icon: '◉' },
    { id: 'con',  name: 'Construction', color: '#a78bfa', icon: '▲' },
  ],
  TEAMS: [
    { id: 'eng', name: 'Engineering', opco: 'tech', mission: 'Build and maintain core product' },
    { id: 'infra', name: 'Infrastructure', opco: 'tech', mission: 'Scale systems and reliability' },
    { id: 'data', name: 'Data & AI', opco: 'tech', mission: 'Power intelligence layer' },
    { id: 'acct', name: 'Accounting', opco: 'fin', mission: 'Financial integrity' },
    { id: 'treasury', name: 'Treasury', opco: 'fin', mission: 'Capital allocation' },
    { id: 'logistics', name: 'Logistics', opco: 'ops', mission: 'Operational execution' },
    { id: 'brand', name: 'Brand', opco: 'mkt', mission: 'Narrative and positioning' },
    { id: 'estimator', name: 'Estimation', opco: 'con', mission: 'Project cost modeling' },
  ],
  STATUSES: [
    { key: 'active', label: 'ACTIVE', color: 'green', icon: '🟢' },
    { key: 'waiting', label: 'WAITING', color: 'amber', icon: '🟡' },
    { key: 'learning', label: 'LEARNING', color: 'blue', icon: '🔵' },
    { key: 'review', label: 'REVIEW', color: 'purple', icon: '🟣' },
    { key: 'failed', label: 'FAILED', color: 'red', icon: '🔴' },
    { key: 'offline', label: 'OFFLINE', color: 'gray', icon: '⚫' },
  ],
  AGENTS: [
    { id:'frontend', name:'Frontend Agent', role:'Software Engineer', team:'eng', opco:'tech', status:'active', mission:'Build user interfaces and design systems', reportsTo:'Engineering Director', capabilities:['React','Next.js','UI Design','Testing'], cpu:42, mem:128, confidence:94, task:'Dashboard UI', progress:72, docs:48, decisions:12, can:['Read designs','Write code'], cannot:['Deploy production'], createdAt:'2025-09-14', tokens:184200, cost:2.47 },
    { id:'backend', name:'Backend Agent', role:'Software Engineer', team:'eng', opco:'tech', status:'active', mission:'Design and implement APIs', reportsTo:'Engineering Director', capabilities:['Node.js','PostgreSQL','APIs','Auth'], cpu:58, mem:256, confidence:91, task:'API Development', progress:45, docs:72, decisions:18, can:['Read specs','Write code','Run tests'], cannot:['Modify schema'], createdAt:'2025-08-02', tokens:412800, cost:5.81 },
    { id:'qa', name:'QA Agent', role:'Quality Engineer', team:'eng', opco:'tech', status:'review', mission:'Validate quality and coverage', reportsTo:'Engineering Director', capabilities:['Testing','Playwright','Code Review'], cpu:18, mem:96, confidence:88, task:'Review PR #482', progress:90, docs:24, decisions:8, can:['Read code','Write tests'], cannot:['Merge code'], createdAt:'2025-10-11', tokens:98400, cost:1.32 },
    { id:'devops', name:'DevOps Agent', role:'Infrastructure Engineer', team:'infra', opco:'tech', status:'active', mission:'Maintain deployments and CI/CD', reportsTo:'Infra Lead', capabilities:['Kubernetes','Terraform','CI/CD'], cpu:31, mem:192, confidence:96, task:'Canary rollout v2.4.1', progress:60, docs:36, decisions:22, can:['Deploy staging','Scale pods'], cannot:['Modify prod secrets'], createdAt:'2025-07-20', tokens:267500, cost:3.62 },
    { id:'dataeng', name:'Data Engineer', role:'Data Engineer', team:'data', opco:'tech', status:'learning', mission:'Build data pipelines', reportsTo:'Data Lead', capabilities:['Python','Spark','ETL','SQL'], cpu:67, mem:512, confidence:82, task:'Training on Q2 corpus', progress:33, docs:128, decisions:6, can:['Read data','Write pipelines'], cannot:['Delete tables'], createdAt:'2025-11-03', tokens:892100, cost:11.24 },
    { id:'analyst', name:'Strategy Analyst', role:'Strategist', team:'treasury', opco:'fin', status:'active', mission:'Model strategic scenarios', reportsTo:'Finance Director', capabilities:['Modeling','Forecasting','Research'], cpu:24, mem:164, confidence:89, task:'Marketplace launch model', progress:55, docs:94, decisions:31, can:['Read reports','Draft analysis'], cannot:['Approve spend'], createdAt:'2025-06-15', tokens:524800, cost:7.12 },
    { id:'accountant', name:'Accountant Agent', role:'Accountant', team:'acct', opco:'fin', status:'active', mission:'Reconcile transactions', reportsTo:'Finance Director', capabilities:['GAAP','Reconciliation','Tax'], cpu:12, mem:84, confidence:97, task:'Monthly close', progress:80, docs:210, decisions:14, can:['Read ledger','Post entries'], cannot:['Approve write-offs'], createdAt:'2025-05-22', tokens:156300, cost:2.08 },
    { id:'logistics', name:'Logistics Agent', role:'Operations Manager', team:'logistics', opco:'ops', status:'waiting', mission:'Coordinate shipments', reportsTo:'Ops Director', capabilities:['Routing','Scheduling','Vendor Mgmt'], cpu:8, mem:72, confidence:76, task:'Awaiting vendor confirmation', progress:40, docs:56, decisions:9, can:['Read orders','Schedule'], cannot:['Cancel orders'], createdAt:'2025-09-30', tokens:78200, cost:1.04 },
    { id:'brand', name:'Brand Agent', role:'Creative Director', team:'brand', opco:'mkt', status:'active', mission:'Craft brand narrative', reportsTo:'Marketing Director', capabilities:['Copywriting','Design','Campaigns'], cpu:34, mem:148, confidence:87, task:'Q3 campaign brief', progress:65, docs:42, decisions:15, can:['Read briefs','Draft copy'], cannot:['Publish externally'], createdAt:'2025-10-18', tokens:234600, cost:3.18 },
    { id:'estimator', name:'Construction Estimator', role:'Cost Estimator', team:'estimator', opco:'con', status:'active', mission:'Model project costs', reportsTo:'Construction Director', capabilities:['Estimation','Materials','Labor'], cpu:45, mem:220, confidence:92, task:'High-rise bid #2041', progress:28, docs:156, decisions:19, can:['Read plans','Run estimates'], cannot:['Submit bids'], createdAt:'2025-08-29', tokens:398700, cost:5.32 },
    { id:'recruiter', name:'Talent Agent', role:'Recruiter', team:'logistics', opco:'ops', status:'review', mission:'Source and screen candidates', reportsTo:'Ops Director', capabilities:['Sourcing','Screening','Interviews'], cpu:22, mem:110, confidence:84, task:'Senior engineer pipeline', progress:50, docs:38, decisions:11, can:['Read profiles','Send invites'], cannot:['Make offers'], createdAt:'2025-11-12', tokens:142800, cost:1.92 },
    { id:'risk', name:'Risk Agent', role:'Risk Analyst', team:'treasury', opco:'fin', status:'active', mission:'Identify and mitigate risk', reportsTo:'Finance Director', capabilities:['Risk Modeling','Compliance','Audit'], cpu:19, mem:132, confidence:93, task:'Vendor risk assessment', progress:70, docs:88, decisions:27, can:['Read contracts','Flag issues'], cannot:['Block deals'], createdAt:'2025-07-08', tokens:312400, cost:4.21 },
    { id:'support', name:'Support Agent', role:'Customer Support', team:'logistics', opco:'ops', status:'failed', mission:'Resolve customer issues', reportsTo:'Ops Director', capabilities:['Tickets','FAQ','Escalation'], cpu:0, mem:0, confidence:42, task:'Error: context overflow', progress:12, docs:14, decisions:3, can:['Read tickets','Reply'], cannot:['Issue refunds'], createdAt:'2025-10-02', tokens:42100, cost:0.58 },
    { id:'research', name:'Research Agent', role:'Researcher', team:'data', opco:'tech', status:'active', mission:'Survey literature and benchmarks', reportsTo:'Data Lead', capabilities:['Papers','Summarization','Synthesis'], cpu:38, mem:196, confidence:90, task:'LLM benchmarking survey', progress:58, docs:204, decisions:8, can:['Read web','Write reports'], cannot:['Execute code'], createdAt:'2025-09-19', tokens:721400, cost:9.64 },
    { id:'security', name:'Security Agent', role:'Security Engineer', team:'infra', opco:'tech', status:'active', mission:'Monitor threats and vulnerabilities', reportsTo:'Infra Lead', capabilities:['Scanning','Incident Response','Audit'], cpu:27, mem:180, confidence:95, task:'Weekly vulnerability scan', progress:85, docs:62, decisions:16, can:['Read logs','Block IPs'], cannot:['Modify firewall rules'], createdAt:'2025-06-30', tokens:189200, cost:2.54 },
    { id:'sales', name:'Sales Agent', role:'Sales Engineer', team:'brand', opco:'mkt', status:'waiting', mission:'Qualify and convert leads', reportsTo:'Marketing Director', capabilities:['Outreach','Demos','Pricing'], cpu:5, mem:68, confidence:79, task:'Awaiting CRM sync', progress:20, docs:28, decisions:7, can:['Read leads','Send emails'], cannot:['Negotiate contracts'], createdAt:'2025-11-01', tokens:64300, cost:0.87 },
  ],
  DEPENDENCIES: {
    frontend: ['backend','qa'],
    backend: ['devops','security'],
    qa: ['frontend','backend'],
    devops: ['security'],
    dataeng: ['research'],
    analyst: ['risk','accountant'],
    accountant: ['risk'],
    logistics: ['estimator'],
    brand: ['analyst'],
    estimator: ['risk'],
    recruiter: ['analyst'],
    risk: ['security'],
    research: ['dataeng'],
    security: ['devops'],
    sales: ['brand','analyst'],
  } as Record<string, string[]>,
  TASKS: [
    { id:'T-1204', agent:'frontend', title:'Build Dashboard UI', status:'in_progress', priority:'high', created:'2h ago', progress:72 },
    { id:'T-1203', agent:'backend', title:'Implement /projects/status endpoint', status:'in_progress', priority:'high', created:'3h ago', progress:45 },
    { id:'T-1202', agent:'qa', title:'Review PR #482', status:'review', priority:'medium', created:'4h ago', progress:90 },
    { id:'T-1201', agent:'devops', title:'Canary rollout v2.4.1', status:'in_progress', priority:'high', created:'5h ago', progress:60 },
    { id:'T-1200', agent:'dataeng', title:'Train on Q2 corpus', status:'in_progress', priority:'medium', created:'6h ago', progress:33 },
    { id:'T-1199', agent:'analyst', title:'Marketplace launch model', status:'in_progress', priority:'high', created:'8h ago', progress:55 },
    { id:'T-1198', agent:'accountant', title:'Monthly close — July', status:'in_progress', priority:'high', created:'1d ago', progress:80 },
    { id:'T-1197', agent:'logistics', title:'Awaiting vendor confirmation', status:'blocked', priority:'medium', created:'1d ago', progress:40 },
    { id:'T-1196', agent:'brand', title:'Q3 campaign brief', status:'in_progress', priority:'medium', created:'1d ago', progress:65 },
    { id:'T-1195', agent:'estimator', title:'High-rise bid #2041', status:'in_progress', priority:'high', created:'2d ago', progress:28 },
    { id:'T-1194', agent:'recruiter', title:'Senior engineer pipeline', status:'review', priority:'medium', created:'2d ago', progress:50 },
    { id:'T-1193', agent:'risk', title:'Vendor risk assessment', status:'in_progress', priority:'high', created:'2d ago', progress:70 },
    { id:'T-1192', agent:'support', title:'Resolve ticket overflow', status:'failed', priority:'critical', created:'3h ago', progress:12 },
    { id:'T-1191', agent:'research', title:'LLM benchmarking survey', status:'in_progress', priority:'low', created:'3d ago', progress:58 },
    { id:'T-1190', agent:'security', title:'Weekly vulnerability scan', status:'in_progress', priority:'high', created:'4h ago', progress:85 },
    { id:'T-1189', agent:'sales', title:'Awaiting CRM sync', status:'blocked', priority:'medium', created:'1d ago', progress:20 },
  ],
  DECISIONS: [
    { id:'D-481', question:'Launch marketplace pilot?', framework:'RACI + Pre-mortem', agents:['analyst','risk','accountant','logistics'], recommendation:'Proceed with pilot in 3 regions', confidence:86, artifacts:5, status:'pending', created:'2h ago',
      trace:[
        { step:1, agent:'analyst', action:'Analyzed TAM/SAM/SOM across 12 markets', conclusion:'Top 3 regions show 3.2x ROI within 18 months', confidence:88 },
        { step:2, agent:'risk', action:'Modeled downside scenarios', conclusion:'Maximum exposure capped at $420K with staged rollout', confidence:91 },
        { step:3, agent:'accountant', action:'Reviewed cash flow impact', conclusion:'Funding available from Q3 reserve without debt', confidence:94 },
        { step:4, agent:'logistics', action:'Assessed operational readiness', conclusion:'Can support 3 regions with current team; 4th requires hiring', confidence:78 },
        { step:5, agent:'analyst', action:'Synthesized final recommendation', conclusion:'Proceed with pilot in NA, EU-West, APAC-SG', confidence:86 },
      ]},
    { id:'D-480', question:'Adopt new LLM provider?', framework:'Weighted scoring', agents:['dataeng','research','security'], recommendation:'Defer — run 30-day benchmark', confidence:78, artifacts:3, status:'approved', created:'1d ago',
      trace:[
        { step:1, agent:'research', action:'Surveyed 6 providers on benchmarks', conclusion:'Provider X leads on reasoning; Provider Y on speed', confidence:82 },
        { step:2, agent:'dataeng', action:'Estimated migration cost', conclusion:'~3 engineering weeks + data pipeline rework', confidence:75 },
        { step:3, agent:'security', action:'Reviewed data handling policies', conclusion:'Provider X has weaker EU data residency guarantees', confidence:88 },
      ]},
    { id:'D-479', question:'Increase Q3 marketing budget by 22%?', framework:'ROI analysis', agents:['analyst','brand','accountant'], recommendation:'Approve with milestone gates', confidence:91, artifacts:7, status:'approved', created:'2d ago', trace:[] as any[] },
    { id:'D-478', question:'Retire legacy auth service?', framework:'Risk matrix', agents:['security','devops','backend'], recommendation:'Migrate by end of Q3', confidence:94, artifacts:4, status:'approved', created:'3d ago', trace:[] as any[] },
    { id:'D-477', question:'Expand to APAC construction market?', framework:'Strategic fit', agents:['estimator','analyst','risk'], recommendation:'Research phase — 90 days', confidence:72, artifacts:6, status:'pending', created:'4d ago', trace:[] as any[] },
    { id:'D-476', question:'Hire 5 senior engineers?', framework:'Capacity model', agents:['recruiter','analyst','accountant'], recommendation:'Approve 3 hires in Q3', confidence:88, artifacts:4, status:'approved', created:'5d ago', trace:[] as any[] },
  ],
  APPROVALS: [
    { id:'A-201', agent:'Construction Estimator Agent v2', requestedBy:'Construction OPCO', purpose:'Automate project cost estimates with 90% accuracy and multi-material support', reviews:{strategy:'approved',finance:'pending',risk:'approved'} as Record<string, string>, created:'3h ago' },
    { id:'A-200', agent:'Compliance Monitor Agent', requestedBy:'Finance OPCO', purpose:'Real-time regulatory compliance scanning across all jurisdictions', reviews:{strategy:'approved',finance:'approved',risk:'pending'} as Record<string, string>, created:'1d ago' },
    { id:'A-199', agent:'Customer Success Agent', requestedBy:'Operations OPCO', purpose:'Proactive customer health monitoring and churn prediction', reviews:{strategy:'pending',finance:'approved',risk:'approved'} as Record<string, string>, created:'2d ago' },
  ],
  EVENTS: [
    { time:'now', type:'task.completed', agent:'Backend Agent', agentId:'backend', text:'Completed API endpoint /health', color:'green' },
    { time:'2m', type:'decision.created', agent:'Strategy Analyst', agentId:'analyst', text:'New decision: Marketplace pilot', color:'purple' },
    { time:'5m', type:'agent.started', agent:'DevOps Agent', agentId:'devops', text:'Started canary rollout v2.4.1', color:'cyan' },
    { time:'8m', type:'memory.updated', agent:'Research Agent', agentId:'research', text:'Indexed 42 new papers', color:'blue' },
    { time:'12m', type:'approval.requested', agent:'Construction Estimator', agentId:'estimator', text:'New agent awaiting approval', color:'amber' },
    { time:'18m', type:'agent.failed', agent:'Support Agent', agentId:'support', text:'Context overflow — needs intervention', color:'red' },
    { time:'24m', type:'task.created', agent:'Frontend Agent', agentId:'frontend', text:'New task: Dashboard UI', color:'cyan' },
    { time:'31m', type:'agent.started', agent:'QA Agent', agentId:'qa', text:'Reviewing PR #482', color:'cyan' },
  ],
  AUDIT_LOG: [
    { time:'14:32:08', actor:'Alex Kowalski', action:'Approved decision D-478', target:'Legacy auth retirement', type:'decision' },
    { time:'14:18:44', actor:'System', action:'Agent entered failed state', target:'support', type:'agent' },
    { time:'13:55:12', actor:'Hermes', action:'Created new decision', target:'D-481', type:'decision' },
    { time:'13:42:01', actor:'DevOps Agent', action:'Deployed canary v2.4.1', target:'prod-east', type:'deploy' },
    { time:'12:18:33', actor:'Alex Kowalski', action:'Updated permissions', target:'security', type:'agent' },
    { time:'11:04:19', actor:'System', action:'Auto-approved agent', target:'research', type:'agent' },
    { time:'10:22:47', actor:'Strategy Analyst', action:'Submitted recommendation', target:'D-479', type:'decision' },
    { time:'09:15:03', actor:'Alex Kowalski', action:'Created agent', target:'recruiter', type:'agent' },
  ],
  NOTIFICATIONS: [
    { id:1, title:'Support Agent failed', desc:'Context overflow — needs intervention', time:'18m ago', unread:true, type:'error', route:'/agents' },
    { id:2, title:'New approval request', desc:'Construction Estimator Agent v2', time:'3h ago', unread:true, type:'warning', route:'/approvals' },
    { id:3, title:'Decision pending', desc:'D-481: Marketplace pilot', time:'2h ago', unread:true, type:'info', route:'/decisions' },
    { id:4, title:'Deployment successful', desc:'Canary v2.4.1 — 60% traffic', time:'5h ago', unread:false, type:'success', route:'/tasks' },
    { id:5, title:'Memory threshold', desc:'Research Agent exceeded 200 docs', time:'8h ago', unread:false, type:'info', route:'/memory' },
  ],
  CHANNELS: [
    { id:'eng-sync', name:'engineering-sync', unread:12, active:true, members:['frontend','backend','qa','devops'] },
    { id:'cross-opco', name:'cross-opco', unread:4, active:false, members:['analyst','brand','logistics'] },
    { id:'incident', name:'incident-response', unread:1, active:false, urgent:true, members:['security','devops','support'] },
    { id:'strategy', name:'strategy-room', unread:0, active:false, members:['analyst','risk','accountant'] },
    { id:'deploy', name:'deployment-ops', unread:7, active:false, members:['devops','backend','security'] },
    { id:'research', name:'research-lab', unread:0, active:false, members:['research','dataeng'] },
  ],
  activeChannel:'eng-sync',
  MESSAGES: {
    'eng-sync':[
      { agent:'frontend', msg:'Need API endpoint: /projects/status', time:'14:23', type:'request' },
      { agent:'backend', msg:'Created endpoint. Artifact: api-update.md', time:'14:25', type:'response' },
      { agent:'qa', msg:'Writing integration tests for the new endpoint', time:'14:28', type:'update' },
      { agent:'devops', msg:'Will include in next canary rollout', time:'14:31', type:'update' },
      { agent:'frontend', msg:'Perfect. Integrating now. ETA 20 minutes.', time:'14:32', type:'response' },
    ],
    'cross-opco':[
      { agent:'analyst', msg:'Q3 forecast ready for cross-opco review', time:'11:14', type:'update' },
      { agent:'brand', msg:'Marketing alignment needed on messaging', time:'11:22', type:'request' },
      { agent:'logistics', msg:'Operations can support proposed timeline', time:'11:45', type:'response' },
    ],
    'incident':[
      { agent:'security', msg:'⚠ Anomalous traffic pattern detected on auth endpoint', time:'14:18', type:'alert' },
      { agent:'support', msg:'Customer tickets spiking — 47 new in 10 minutes', time:'14:19', type:'alert' },
      { agent:'devops', msg:'Initiating canary rollback to v2.4.0', time:'14:20', type:'action' },
    ],
    'strategy':[
      { agent:'analyst', msg:'Marketplace pilot model complete', time:'09:14', type:'update' },
      { agent:'risk', msg:'Reviewed — downside acceptable with staging', time:'09:42', type:'response' },
    ],
    'deploy':[
      { agent:'devops', msg:'Canary v2.4.1 at 60% traffic', time:'13:42', type:'update' },
      { agent:'backend', msg:'Error rates nominal at 0.02%', time:'13:48', type:'update' },
    ],
    'research':[
      { agent:'research', msg:'New paper: "Scaling laws for agents" — relevant to our work', time:'10:22', type:'update' },
      { agent:'dataeng', msg:'Added to corpus. Indexing now.', time:'10:34', type:'response' },
    ],
  } as Record<string, any[]>,
  MEMORY: [
    { type:'Document', title:'Q2 Strategic Review.pdf', agent:'Strategy Analyst', agentId:'analyst', time:'12m ago', size:'2.4 MB' },
    { type:'Code', title:'api-update.md', agent:'Backend Agent', agentId:'backend', time:'28m ago', size:'14 KB' },
    { type:'Report', title:'Vendor Risk Assessment', agent:'Risk Agent', agentId:'risk', time:'1h ago', size:'842 KB' },
    { type:'Decision', title:'D-481: Marketplace pilot', agent:'Multi-agent', agentId:'analyst', time:'2h ago', size:'5 artifacts' },
    { type:'Document', title:'High-rise bid #2041.xlsx', agent:'Construction Estimator', agentId:'estimator', time:'3h ago', size:'1.8 MB' },
    { type:'Code', title:'dashboard-v2.tsx', agent:'Frontend Agent', agentId:'frontend', time:'4h ago', size:'32 KB' },
    { type:'Report', title:'Monthly Financial Close', agent:'Accountant Agent', agentId:'accountant', time:'5h ago', size:'1.2 MB' },
    { type:'Document', title:'LLM Benchmark Survey', agent:'Research Agent', agentId:'research', time:'6h ago', size:'3.1 MB' },
    { type:'Code', title:'k8s-canary.yaml', agent:'DevOps Agent', agentId:'devops', time:'7h ago', size:'8 KB' },
    { type:'Decision', title:'D-480: LLM provider', agent:'Multi-agent', agentId:'dataeng', time:'1d ago', size:'3 artifacts' },
  ],
  WORKFLOWS: [
    { name:'Code Review Pipeline', steps:5, runs:142, success:94, status:'active', avgTime:'4.2m' },
    { name:'Deployment Canary', steps:8, runs:38, success:100, status:'active', avgTime:'18.4m' },
    { name:'Customer Issue Triage', steps:6, runs:89, success:87, status:'active', avgTime:'2.8m' },
    { name:'Monthly Financial Close', steps:12, runs:7, success:100, status:'active', avgTime:'3.2h' },
    { name:'Vendor Risk Assessment', steps:9, runs:24, success:92, status:'active', avgTime:'22m' },
    { name:'Campaign Brief Generation', steps:7, runs:18, success:89, status:'paused', avgTime:'6.1m' },
  ],
};

// ==========================================
// API ENDPOINTS
// ==========================================

// GET /api/dashboard/store - Full Store retrieval
dashboardRouter.get('/store', (req: Request, res: Response) => {
  res.json(Store);
});

// GET /api/dashboard/stats - Aggregate KPIs
dashboardRouter.get('/stats', (req: Request, res: Response) => {
  const activeCount = Store.AGENTS.filter(a => a.status === 'active').length;
  const runningTasks = Store.TASKS.filter(t => t.status === 'in_progress').length;
  const pendingDecisions = Store.DECISIONS.filter(d => d.status === 'pending').length;
  const totalCost = Store.AGENTS.reduce((s, a) => s + a.cost, 0);

  res.json({
    activeCount,
    totalAgents: Store.AGENTS.length,
    runningTasks,
    pendingDecisions,
    totalCost,
  });
});

// GET /api/dashboard/agents - List all agents
dashboardRouter.get('/agents', (req: Request, res: Response) => {
  res.json(Store.AGENTS);
});

// POST /api/dashboard/agents - Create a new agent from wizard
dashboardRouter.post('/agents', (req: Request, res: Response) => {
  try {
    const { name, role, mission, opco, team, reportsTo, capabilities, can, cannot } = req.body;
    if (!name || !role || !mission || !opco || !team) {
      return res.status(400).json({ error: 'Missing required agent fields' });
    }

    const id = name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') + '-' + Date.now().toString(36).slice(-4);
    const newAgent = {
      id,
      name,
      role,
      mission,
      opco,
      team,
      reportsTo: reportsTo || 'OPCO Director',
      status: 'offline',
      capabilities: Array.isArray(capabilities) ? capabilities : [],
      can: Array.isArray(can) ? can : [],
      cannot: Array.isArray(cannot) ? cannot : [],
      cpu: 0,
      mem: 128,
      confidence: 85,
      task: 'Awaiting activation',
      progress: 0,
      docs: 0,
      decisions: 0,
      createdAt: new Date().toISOString().split('T')[0],
      tokens: 0,
      cost: 0,
    };

    Store.AGENTS.push(newAgent);

    // Audit and event log
    const nowStr = new Date().toTimeString().split(' ')[0];
    Store.AUDIT_LOG.unshift({
      time: nowStr,
      actor: 'Alex Kowalski',
      action: 'Created new agent',
      target: id,
      type: 'agent'
    });
    Store.EVENTS.unshift({
      time: 'now',
      type: 'agent.started',
      agent: name,
      agentId: id,
      text: `Created new agent: ${name}`,
      color: 'cyan'
    });

    res.status(201).json(newAgent);
  } catch (err: any) {
    res.status(500).json({ error: err.message });
  }
});

// POST /api/dashboard/agents/:id/status - Toggle agent status
dashboardRouter.post('/agents/:id/status', (req: Request, res: Response) => {
  const { id } = req.params;
  const agent = Store.AGENTS.find(a => a.id === id);
  if (!agent) {
    return res.status(404).json({ error: 'Agent not found' });
  }

  agent.status = agent.status === 'active' ? 'offline' : 'active';
  
  const nowStr = new Date().toTimeString().split(' ')[0];
  Store.AUDIT_LOG.unshift({
    time: nowStr,
    actor: 'Alex Kowalski',
    action: `Toggled agent status to ${agent.status}`,
    target: id,
    type: 'agent'
  });

  res.json(agent);
});

// DELETE /api/dashboard/agents/:id - Retire agent
dashboardRouter.delete('/agents/:id', (req: Request, res: Response) => {
  const { id } = req.params;
  const idx = Store.AGENTS.findIndex(a => a.id === id);
  if (idx === -1) {
    return res.status(404).json({ error: 'Agent not found' });
  }

  const agent = Store.AGENTS[idx];
  Store.AGENTS.splice(idx, 1);

  const nowStr = new Date().toTimeString().split(' ')[0];
  Store.AUDIT_LOG.unshift({
    time: nowStr,
    actor: 'Alex Kowalski',
    action: 'Retired agent',
    target: id,
    type: 'agent'
  });

  res.json({ success: true, retired: agent.name });
});

// GET /api/dashboard/tasks - List all tasks
dashboardRouter.get('/tasks', (req: Request, res: Response) => {
  res.json(Store.TASKS);
});

// GET /api/dashboard/decisions - List decisions
dashboardRouter.get('/decisions', (req: Request, res: Response) => {
  res.json(Store.DECISIONS);
});

// GET /api/dashboard/approvals - List approvals
dashboardRouter.get('/approvals', (req: Request, res: Response) => {
  res.json(Store.APPROVALS);
});

// POST /api/dashboard/approvals/:id/act - Approve/Reject approvals
dashboardRouter.post('/approvals/:id/act', (req: Request, res: Response) => {
  const { id } = req.params;
  const { action } = req.body; // 'approve' | 'reject' | 'changes'
  
  const appr = Store.APPROVALS.find(a => a.id === id);
  if (!appr) {
    return res.status(404).json({ error: 'Approval request not found' });
  }

  const nowStr = new Date().toTimeString().split(' ')[0];

  if (action === 'approve') {
    Object.keys(appr.reviews).forEach(k => appr.reviews[k] = 'approved');
    Store.AUDIT_LOG.unshift({
      time: nowStr,
      actor: 'Alex Kowalski',
      action: 'Approved agent request',
      target: id,
      type: 'approval'
    });
  } else if (action === 'reject') {
    Object.keys(appr.reviews).forEach(k => appr.reviews[k] = 'rejected');
    Store.AUDIT_LOG.unshift({
      time: nowStr,
      actor: 'Alex Kowalski',
      action: 'Rejected agent request',
      target: id,
      type: 'approval'
    });
  } else if (action === 'changes') {
    const pending = Object.keys(appr.reviews).find(k => appr.reviews[k] === 'pending');
    if (pending) appr.reviews[pending] = 'rejected';
  }

  res.json(appr);
});

// GET /api/dashboard/events - List events
dashboardRouter.get('/events', (req: Request, res: Response) => {
  res.json(Store.EVENTS);
});

// GET /api/dashboard/memory - Search/List memory
dashboardRouter.get('/memory', (req: Request, res: Response) => {
  res.json(Store.MEMORY);
});

// GET /api/dashboard/workflows - List workflows
dashboardRouter.get('/workflows', (req: Request, res: Response) => {
  res.json(Store.WORKFLOWS);
});

// GET /api/dashboard/audit - List audit trail
dashboardRouter.get('/audit', (req: Request, res: Response) => {
  res.json(Store.AUDIT_LOG);
});

// POST /api/dashboard/comms/messages - Post message to channel
dashboardRouter.post('/comms/messages', (req: Request, res: Response) => {
  const { channelId, message, type } = req.body;
  if (!channelId || !message) {
    return res.status(400).json({ error: 'Missing channelId or message text' });
  }

  if (!Store.MESSAGES[channelId]) {
    Store.MESSAGES[channelId] = [];
  }

  const newMsg = {
    agent: 'frontend',
    msg: message,
    time: new Date().toTimeString().slice(0,5),
    type: type || 'update'
  };

  Store.MESSAGES[channelId].push(newMsg);
  res.status(201).json(newMsg);
});
