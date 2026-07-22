'use client';
import { useState, useEffect } from 'react';
import { getAgents, getAgentTasks, getAgentDecisions, getSkillExecutions } from '@/lib/supabase';
import { createClient } from '@supabase/supabase-js';

type Tab = 'dashboard' | 'agents' | 'mcp' | 'skills';
const supabase = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL || '', process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '');

export default function Dashboard() {
  const [tab, setTab] = useState<Tab>('dashboard');
  const [agents, setAgents] = useState<any[]>([]);
  const [tasks, setTasks] = useState<any[]>([]);
  const [decisions, setDecisions] = useState<any[]>([]);
  const [skills, setSkills] = useState<any[]>([]);
  const [mcps, setMcps] = useState<any[]>([]);
  const [mrr, setMrr] = useState(0);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const [ag, tk, dc, sk] = await Promise.all([
        getAgents(),
        getAgentTasks(),
        getAgentDecisions(),
        getSkillExecutions(),
      ]);
      setAgents(ag);
      setTasks(tk);
      setDecisions(dc);
      setSkills(sk);

      const defaultMcps = [
        { name: 'slack', status: 'active', category: 'communication', capabilities: ['send_message'], used_by: ['CON-001'] },
        { name: 'supabase', status: 'active', category: 'database', capabilities: ['query', 'insert'], used_by: ['all'] },
        { name: 'neo4j', status: 'active', category: 'graph', capabilities: ['cypher_query'], used_by: ['all'] },
        { name: 'stripe', status: 'active', category: 'payment', capabilities: ['charge', 'refund'], used_by: ['FIN-001'] },
        { name: 'gmail', status: 'active', category: 'email', capabilities: ['send', 'read'], used_by: ['STA-001'] },
      ];
      setMcps(defaultMcps);

      try {
        const sevenDaysAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString();
        const { data } = await supabase.from('payments').select('amount').eq('status', 'succeeded').gte('created_at', sevenDaysAgo);
        setMrr(data?.reduce((sum, p: any) => sum + (p.amount || 0), 0) || 0);
      } catch (err) {
        console.error('MRR query error:', err);
      }

      setLoading(false);
    }
    load();
  }, []);

  if (loading) return <div className="min-h-screen bg-slate-900 text-white p-8">Loading...</div>;

  const activeAgents = agents.filter((a: any) => a.status === 'active').length;
  const runningTasks = tasks.filter((t: any) => t.status === 'in_progress').length;
  const pendingDecisions = decisions.filter((d: any) => d.status === 'pending').length;
  const activeMcps = mcps.filter((m: any) => m.status === 'active').length;

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 text-slate-50">
      <div className="border-b border-slate-800 bg-slate-900/50 backdrop-blur sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-8 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-cyan-400 to-blue-600 flex items-center justify-center font-bold text-black">Η</div>
            <div><h1 className="text-xl font-bold">Hermes Command Center</h1><p className="text-xs text-slate-400">VEX OPCO Engine · Real-time Operations</p></div>
          </div>
          <span className="inline-flex items-center gap-2 text-xs px-3 py-1 rounded-full bg-green-500/10 text-green-400 border border-green-500/20"><span className="w-2 h-2 rounded-full bg-green-400 animate-pulse"></span> LIVE</span>
        </div>
        <div className="border-t border-slate-800 flex gap-0 max-w-7xl mx-auto px-8">
          {(['dashboard', 'agents', 'mcp', 'skills'] as const).map(t => (
            <button key={t} onClick={() => setTab(t)} className={`px-4 py-3 text-sm font-medium border-b-2 transition ${tab === t ? 'border-cyan-400 text-cyan-400' : 'border-transparent text-slate-400 hover:text-slate-300'}`}>
              {t === 'dashboard' && '📊 Dashboard'}
              {t === 'agents' && '🤖 Agency Agents'}
              {t === 'mcp' && '🔌 MCP Registry'}
              {t === 'skills' && '⚙️ Skills Execution'}
            </button>
          ))}
        </div>
      </div>

      <div className="max-w-7xl mx-auto p-8">
        {tab === 'dashboard' && (
          <>
            <div className="grid grid-cols-5 gap-4 mb-8">
              <KPICard label="Active Agents" value={activeAgents} total={agents.length} color="green" />
              <KPICard label="Running Tasks" value={runningTasks} total={tasks.length} color="cyan" />
              <KPICard label="Pending Decisions" value={pendingDecisions} total={decisions.length} color="amber" />
              <KPICard label="Active MCPs" value={activeMcps} total={mcps.length} color="purple" />
              <div className="bg-gradient-to-br from-green-500/20 text-green-400 border border-green-500/30 rounded-lg p-5">
                <div className="text-xs font-medium text-slate-400 mb-2">💰 REVENUE THIS WEEK</div>
                <div style={{fontSize:'26px', fontWeight:'bold'}}>${mrr.toFixed(2)}</div>
                <div style={{fontSize:'12px', color:'var(--text-3)', marginTop:'8px'}}>Paid customers</div>
              </div>
            </div>

            <div className="grid grid-cols-3 gap-4">
              <div className="col-span-2 bg-slate-800/50 border border-slate-700 rounded-lg p-6">
                <h2 className="text-lg font-bold mb-4">Top Agents by Confidence</h2>
                <div className="space-y-3">
                  {agents.slice(0, 5).map((a: any, i: number) => (
                    <div key={i} className="flex items-center gap-3 p-3 rounded bg-slate-700/30">
                      <div className="w-8 h-8 rounded bg-cyan-500/20 flex items-center justify-center text-xs font-bold text-cyan-400">{(a.name || 'A').substring(0, 2).toUpperCase()}</div>
                      <div className="flex-1"><div className="text-sm font-medium">{a.name || 'Agent'}</div><div className="text-xs text-slate-400">{a.role || 'Unknown'}</div></div>
                      <div className="text-right"><div className="text-sm font-bold text-green-400">{Math.round((a.confidence || 0.5) * 100)}%</div></div>
                    </div>
                  ))}
                </div>
              </div>

              <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-6">
                <h2 className="text-lg font-bold mb-4">OPCO Health</h2>
                <div className="space-y-3">
                  {['Technology', 'Finance', 'Operations'].map(opco => (
                    <div key={opco}>
                      <div className="text-xs font-medium text-slate-400 mb-1">{opco}</div>
                      <div className="w-full h-2 bg-slate-600 rounded-full overflow-hidden">
                        <div className="h-full bg-gradient-to-r from-cyan-400 to-blue-400" style={{width: Math.random() * 100 + '%'}}></div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </>
        )}

        {tab === 'agents' && (
          <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-6">
            <h2 className="text-lg font-bold mb-4">Active Agents</h2>
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead className="border-b border-slate-700">
                  <tr>
                    <th className="text-left py-2 px-3 font-medium text-slate-400">Name</th>
                    <th className="text-left py-2 px-3 font-medium text-slate-400">Status</th>
                    <th className="text-left py-2 px-3 font-medium text-slate-400">Role</th>
                    <th className="text-right py-2 px-3 font-medium text-slate-400">Tasks</th>
                  </tr>
                </thead>
                <tbody>
                  {agents.map((a: any, i: number) => (
                    <tr key={i} className="border-b border-slate-700/50">
                      <td className="py-3 px-3">{a.name || 'Agent'}</td>
                      <td className="py-3 px-3"><span className={`inline-flex items-center gap-1 px-2 py-1 rounded text-xs font-bold ${a.status === 'active' ? 'bg-green-500/10 text-green-400' : 'bg-amber-500/10 text-amber-400'}`}><span className={`w-1.5 h-1.5 rounded-full ${a.status === 'active' ? 'bg-green-400' : 'bg-amber-400'}`}></span>{(a.status || 'idle').toUpperCase()}</span></td>
                      <td className="py-3 px-3 text-slate-400">{a.role || '—'}</td>
                      <td className="py-3 px-3 text-right font-mono">{a.task_count || 0}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {tab === 'mcp' && (
          <div className="grid grid-cols-2 gap-4">
            {mcps.map((mcp: any, i: number) => (
              <div key={i} className="bg-slate-800/50 border border-slate-700 rounded-lg p-4">
                <div className="flex items-start justify-between mb-3">
                  <div><h3 className="font-bold text-sm">{mcp.name}</h3><p className="text-xs text-slate-400 mt-1">{mcp.category}</p></div>
                  <span className={`text-xs px-2 py-1 rounded ${mcp.status === 'active' ? 'bg-green-500/20 text-green-400' : 'bg-slate-600 text-slate-400'}`}>{mcp.status === 'active' ? '●' : '○'} {mcp.status}</span>
                </div>
                <div className="text-xs text-slate-400"><p className="mb-2">Capabilities: {mcp.capabilities?.join(', ') || '—'}</p><p>Used by: {mcp.used_by?.join(', ') || 'Internal'}</p></div>
              </div>
            ))}
          </div>
        )}

        {tab === 'skills' && (
          <div className="space-y-4">
            {skills.slice(0, 10).map((skill: any, i: number) => (
              <div key={i} className="bg-slate-800/50 border border-slate-700 rounded-lg p-4">
                <div className="flex items-center justify-between mb-2"><h3 className="font-bold">{skill.name || skill.skill || 'Skill'}</h3><span className={`text-xs px-2 py-1 rounded font-mono ${skill.status === 'completed' ? 'bg-green-500/20 text-green-400' : skill.status === 'running' ? 'bg-cyan-500/20 text-cyan-400' : 'bg-slate-600 text-slate-400'}`}>{skill.status || 'pending'}</span></div>
                <div className="h-2 bg-slate-600 rounded-full overflow-hidden mb-2"><div className="h-full bg-gradient-to-r from-cyan-400 to-blue-400" style={{width: (skill.progress || 0) + '%'}}></div></div>
                <div className="text-xs text-slate-400">{skill.progress || 0}% · {skill.tokens_used || 0} tokens · ETA {skill.eta_seconds || 0}s</div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

function KPICard({ label, value, total, color }: any) {
  const colorMap: any = {
    green: 'from-green-500/20 text-green-400 border-green-500/30',
    cyan: 'from-cyan-500/20 text-cyan-400 border-cyan-500/30',
    amber: 'from-amber-500/20 text-amber-400 border-amber-500/30',
    purple: 'from-purple-500/20 text-purple-400 border-purple-500/30',
  };
  return (
    <div className={`bg-gradient-to-br ${colorMap[color]} border rounded-lg p-5`}>
      <div className="text-xs font-medium text-slate-400 mb-2">{label}</div>
      <div className={`text-3xl font-bold ${colorMap[color].split(' ')[1]}`}>{value}</div>
      <div className="text-xs text-slate-400 mt-2">of {total} total</div>
    </div>
  );
}
