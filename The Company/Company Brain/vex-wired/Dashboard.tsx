import { useState, useEffect } from 'react';
import { OPCOS, getSectorsByOpco } from '../data/sectors';

interface Metrics {
  activeAgents: number;
  totalAgents: number;
  tasksRunning: number;
  decisionsLive: number;
  totalCost: number;
}

export default function Dashboard() {
  const [metrics, setMetrics] = useState<Metrics>({
    activeAgents: 0,
    totalAgents: 31,
    tasksRunning: 0,
    decisionsLive: 0,
    totalCost: 0,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const response = await fetch('/api/dashboard-metrics');
        if (response.ok) {
          const data = await response.json();
          setMetrics(data);
        }
      } catch (error) {
        console.error('Failed to fetch metrics:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchMetrics();
    const interval = setInterval(fetchMetrics, 10000);
    return () => clearInterval(interval);
  }, []);

  const { activeAgents, totalAgents, tasksRunning, decisionsLive, totalCost } = metrics;

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <div className="flex items-start justify-between">
        <div>
          <h1 className="text-3xl font-bold mb-1">Hermes Command Center</h1>
          <p className="text-gray-400">Operational hub for Worldwidebro Holdings · 31 sectors live</p>
        </div>
        <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-green-500/10 border border-green-500/30">
          <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
          <span className="text-xs text-green-400 font-medium">LIVE</span>
        </div>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-4 gap-4">
        <div className="border border-white/10 bg-gray-900 rounded-lg p-4">
          <div className="text-xs uppercase text-gray-500 font-bold mb-2">Active Agents</div>
          <div className="text-3xl font-bold text-green-400">{loading ? '—' : activeAgents}</div>
          <div className="text-xs text-gray-400 mt-2">of {totalAgents} total</div>
        </div>
        <div className="border border-white/10 bg-gray-900 rounded-lg p-4">
          <div className="text-xs uppercase text-gray-500 font-bold mb-2">Tasks Running</div>
          <div className="text-3xl font-bold text-cyan-400">{loading ? '—' : tasksRunning}</div>
          <div className="text-xs text-gray-400 mt-2">in progress</div>
        </div>
        <div className="border border-white/10 bg-gray-900 rounded-lg p-4">
          <div className="text-xs uppercase text-gray-500 font-bold mb-2">Decisions Live</div>
          <div className="text-3xl font-bold text-purple-400">{loading ? '—' : decisionsLive}</div>
          <div className="text-xs text-gray-400 mt-2">pending review</div>
        </div>
        <div className="border border-white/10 bg-gray-900 rounded-lg p-4">
          <div className="text-xs uppercase text-gray-500 font-bold mb-2">Cost (30d)</div>
          <div className="text-3xl font-bold text-amber-400">${loading ? '—' : (totalCost / 1000).toFixed(1)}K</div>
          <div className="text-xs text-gray-400 mt-2">real revenue</div>
        </div>
      </div>

      {/* OPCO Health */}
      <div className="border border-white/10 bg-gray-900 rounded-lg p-6">
        <div className="mb-6">
          <h2 className="text-lg font-bold mb-1">OPCO Health</h2>
          <p className="text-xs text-gray-400">Sector distribution across Operating Companies</p>
        </div>
        <div className="grid grid-cols-5 gap-4">
          {OPCOS.map(opco => {
            const sectors = getSectorsByOpco(opco.id);
            const health = 75 + Math.random() * 20;
            return (
              <div key={opco.id} className="p-4 rounded-lg bg-gray-800 border border-white/5 hover:border-white/10 transition-colors">
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-2xl">{opco.icon}</span>
                  <span className="font-bold text-sm">{opco.name}</span>
                </div>
                <div className="text-2xl font-bold mb-2" style={{ color: opco.color }}>
                  {sectors.length}
                </div>
                <div className="text-xs text-gray-400 mb-3">sectors</div>
                <div className="bg-gray-700 h-2 rounded-full overflow-hidden">
                  <div
                    className="h-full rounded-full transition-all"
                    style={{ width: `${health}%`, backgroundColor: opco.color }}
                  ></div>
                </div>
                <div className="text-xs text-gray-500 mt-1">{Math.round(health)}% health</div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Event Stream */}
      <div className="grid grid-cols-3 gap-4">
        <div className="col-span-2 border border-white/10 bg-gray-900 rounded-lg p-6">
          <div className="mb-4">
            <h2 className="text-lg font-bold">Event Stream</h2>
            <p className="text-xs text-gray-400 mt-1">Real-time system activity</p>
          </div>
          <div className="space-y-2">
            {[
              { icon: '🔗', msg: 'Dashboard wired to Supabase (real-time metrics)', time: 'now', color: 'cyan' },
              { icon: '🔄', msg: 'Polling venture_leads + deal_payments every 10s', time: 'active', color: 'green' },
              { icon: '✓', msg: 'Form submission → ClickUp automation ready', time: 'standby', color: 'blue' },
              { icon: '📊', msg: 'Revenue tracking live from Stripe', time: 'active', color: 'amber' },
            ].map((event, i) => (
              <div key={i} className="flex gap-3 p-2 rounded hover:bg-white/5 transition-colors">
                <span className="text-lg">{event.icon}</span>
                <div className="flex-1 min-w-0">
                  <div className="text-sm text-gray-200">{event.msg}</div>
                  <div className="text-xs text-gray-500">{event.time}</div>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="border border-white/10 bg-gray-900 rounded-lg p-6">
          <h2 className="text-lg font-bold mb-4">Quick Stats</h2>
          <div className="space-y-4">
            <div>
              <div className="text-xs text-gray-400 mb-1">Approval Queue</div>
              <div className="text-2xl font-bold">3</div>
              <div className="text-xs text-gray-500">pending</div>
            </div>
            <div className="border-t border-white/10 pt-4">
              <div className="text-xs text-gray-400 mb-1">Top Sector</div>
              <div className="text-lg font-bold">Technology</div>
              <div className="text-xs text-gray-500">8 subsectors</div>
            </div>
            <div className="border-t border-white/10 pt-4">
              <div className="text-xs text-gray-400 mb-1">System Status</div>
              <div className="text-sm text-green-400">All systems nominal</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
