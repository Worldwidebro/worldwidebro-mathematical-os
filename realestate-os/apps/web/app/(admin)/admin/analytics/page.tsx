'use client';

import { useEffect, useState } from 'react';
import { Loader2, LogOut, Download } from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import { RevenueChart } from '@/components/analytics/RevenueChart';
import { OccupancyHeatmap } from '@/components/analytics/OccupancyHeatmap';
import { MaintenancePipeline } from '@/components/analytics/MaintenancePipeline';

interface KPIs {
  mrr: number;
  occupancyPct: number;
  avgResponseTimeHours: number;
  openTickets: number;
}

interface RevenueData {
  month: string;
  revenue: number;
}

interface OccupancyUnit {
  propertyId: string;
  propertyAddress: string;
  propertyCity: string;
  unitId: string;
  unitNumber: string;
  occupied: boolean;
}

interface MaintenanceStatus {
  status: string;
  count: number;
}

export default function AnalyticsDashboard() {
  const { logout, isLoading: authLoading } = useAuth();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [exporting, setExporting] = useState(false);

  // Data state
  const [kpis, setKpis] = useState<KPIs | null>(null);
  const [revenueData, setRevenueData] = useState<RevenueData[]>([]);
  const [occupancyData, setOccupancyData] = useState<OccupancyUnit[]>([]);
  const [maintenanceData, setMaintenanceData] = useState<MaintenanceStatus[]>([]);
  const [period, setPeriod] = useState<'30d' | '90d' | '12mo'>('12mo');

  const fetchAnalytics = async () => {
    setLoading(true);
    setError(null);
    try {
      // Fetch KPIs
      const kpiRes = await fetch('/api/analytics/kpis', {
        headers: { 'x-user-id': 'temp-user' }
      });
      if (!kpiRes.ok) throw new Error('Failed to fetch KPIs');
      const kpiData = await kpiRes.json();
      setKpis(kpiData);

      // Fetch revenue
      const revRes = await fetch(`/api/analytics/revenue?period=${period}`, {
        headers: { 'x-user-id': 'temp-user' }
      });
      if (!revRes.ok) throw new Error('Failed to fetch revenue');
      const revData = await revRes.json();
      setRevenueData(revData);

      // Fetch occupancy
      const occRes = await fetch('/api/analytics/occupancy', {
        headers: { 'x-user-id': 'temp-user' }
      });
      if (!occRes.ok) throw new Error('Failed to fetch occupancy');
      const occData = await occRes.json();
      setOccupancyData(occData);

      // Fetch maintenance
      const maintRes = await fetch('/api/analytics/maintenance', {
        headers: { 'x-user-id': 'temp-user' }
      });
      if (!maintRes.ok) throw new Error('Failed to fetch maintenance');
      const maintData = await maintRes.json();
      setMaintenanceData(maintData);
    } catch (err: any) {
      setError(err.message || 'Failed to load analytics');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAnalytics();
  }, [period]);

  const handleExport = async () => {
    setExporting(true);
    try {
      const res = await fetch('/api/analytics/export?format=csv', {
        method: 'POST',
        headers: { 'x-user-id': 'temp-user' }
      });
      if (!res.ok) throw new Error('Export failed');

      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `analytics-${new Date().toISOString().split('T')[0]}.csv`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (err: any) {
      alert('Export failed: ' + err.message);
    } finally {
      setExporting(false);
    }
  };

  if (authLoading || loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-950">
        <div className="text-center space-y-4">
          <Loader2 className="animate-spin h-10 w-10 text-blue-500 mx-auto" />
          <p className="text-gray-400 text-sm">Loading analytics dashboard...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      {/* Top Navigation */}
      <header className="border-b border-gray-800 bg-gray-900 px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="h-9 w-9 rounded-lg bg-blue-600 flex items-center justify-center font-bold text-white">
            📊
          </div>
          <div>
            <h1 className="text-lg font-bold text-white tracking-tight">Analytics Dashboard</h1>
            <p className="text-xs text-gray-400">Property management insights</p>
          </div>
        </div>
        <button
          onClick={logout}
          className="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-gray-800 hover:bg-gray-800 transition-colors text-xs text-gray-400 hover:text-white"
        >
          <LogOut className="h-4 w-4" />
          Sign Out
        </button>
      </header>

      <main className="max-w-7xl mx-auto p-6 space-y-8">
        {/* Error Alert */}
        {error && (
          <div className="bg-red-950 border border-red-800 text-red-400 px-4 py-3 rounded-lg text-sm">
            {error}
          </div>
        )}

        {/* Controls */}
        <div className="flex items-center justify-between flex-wrap gap-4">
          <div className="flex gap-2">
            {(['30d', '90d', '12mo'] as const).map((p) => (
              <button
                key={p}
                onClick={() => setPeriod(p)}
                className={`px-3 py-1.5 text-xs font-semibold rounded-lg transition-colors ${
                  period === p
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-800 text-gray-400 hover:text-white'
                }`}
              >
                {p === '30d' ? 'Last 30 Days' : p === '90d' ? 'Last 90 Days' : 'Last 12 Months'}
              </button>
            ))}
          </div>

          <button
            onClick={handleExport}
            disabled={exporting}
            className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-700 text-white text-xs font-semibold rounded-lg transition-colors"
          >
            {exporting ? (
              <Loader2 className="h-4 w-4 animate-spin" />
            ) : (
              <Download className="h-4 w-4" />
            )}
            Export CSV
          </button>
        </div>

        {/* KPI Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="bg-gray-900 border border-gray-800 rounded-xl p-5 relative overflow-hidden">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Monthly Recurring Revenue</div>
            <div className="text-3xl font-bold mt-2 text-emerald-400">
              ${kpis?.mrr.toLocaleString() || 0}
            </div>
            <div className="text-[10px] text-gray-500 mt-1">Last 30 days collected</div>
            <div className="absolute right-4 bottom-4 h-12 w-12 text-gray-800 opacity-20 text-2xl">💰</div>
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-xl p-5 relative overflow-hidden">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Occupancy Rate</div>
            <div className="text-3xl font-bold mt-2 text-blue-400">{kpis?.occupancyPct || 0}%</div>
            <div className="text-[10px] text-gray-500 mt-1">Units occupied</div>
            <div className="absolute right-4 bottom-4 h-12 w-12 text-gray-800 opacity-20 text-2xl">🏠</div>
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-xl p-5 relative overflow-hidden">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Avg Response Time</div>
            <div className="text-3xl font-bold mt-2 text-purple-400">{kpis?.avgResponseTimeHours || 0}h</div>
            <div className="text-[10px] text-gray-500 mt-1">Maintenance completion</div>
            <div className="absolute right-4 bottom-4 h-12 w-12 text-gray-800 opacity-20 text-2xl">⚙️</div>
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-xl p-5 relative overflow-hidden">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Open Tickets</div>
            <div className="text-3xl font-bold mt-2 text-amber-400">{kpis?.openTickets || 0}</div>
            <div className="text-[10px] text-gray-500 mt-1">Requires attention</div>
            <div className="absolute right-4 bottom-4 h-12 w-12 text-gray-800 opacity-20 text-2xl">🔔</div>
          </div>
        </div>

        {/* Charts Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Revenue Chart - spans 2 cols */}
          <div className="lg:col-span-2">
            <RevenueChart data={revenueData} />
          </div>

          {/* Maintenance Pipeline */}
          <MaintenancePipeline data={maintenanceData} />
        </div>

        {/* Occupancy Heatmap - full width */}
        <OccupancyHeatmap data={occupancyData} />
      </main>
    </div>
  );
}
