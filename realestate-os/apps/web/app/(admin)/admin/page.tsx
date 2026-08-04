'use client';

import { useEffect, useState } from 'react';
import { useAuth } from '@/hooks/useAuth';
import { Users, AlertCircle, BarChart3, LogOut, Loader2, TrendingUp } from 'lucide-react';
import Link from 'next/link';

interface Metrics {
  userStats: { admin: number; landlord: number; tenant: number };
  mrrTrend: Record<string, number>;
  occupancy: { occupied: number; total: number; rate: number };
  openTickets: number;
}

interface PaymentHealth {
  paid: number;
  pending: number;
  late: number;
  total: number;
  collectionRate: number;
}

export default function AdminDashboard() {
  const { logout, isLoading: authLoading } = useAuth();
  const [metrics, setMetrics] = useState<Metrics | null>(null);
  const [health, setHealth] = useState<PaymentHealth | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchMetrics = async () => {
    setLoading(true);
    setError(null);
    try {
      const metricsRes = await fetch('/api/admin/reports/metrics');
      const healthRes = await fetch('/api/admin/reports/payment-health');

      if (!metricsRes.ok || !healthRes.ok) throw new Error('Failed to load metrics');

      const metricsData = await metricsRes.json();
      const healthData = await healthRes.json();

      setMetrics(metricsData);
      setHealth(healthData);
    } catch (err: any) {
      setError(err.message || 'Error loading dashboard');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchMetrics();
  }, []);

  if (authLoading || loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-950">
        <div className="text-center space-y-4">
          <Loader2 className="animate-spin h-10 w-10 text-blue-500 mx-auto" />
          <p className="text-gray-400 text-sm">Loading Admin Portal...</p>
        </div>
      </div>
    );
  }

  const currentMRR = metrics
    ? Math.max(...Object.values(metrics.mrrTrend || {}).map(v => Number(v) || 0)) || 0
    : 0;
  const totalUsers = metrics
    ? metrics.userStats.admin + metrics.userStats.landlord + metrics.userStats.tenant
    : 0;

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      {/* Header */}
      <header className="border-b border-gray-800 bg-gray-900 px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="h-9 w-9 rounded-lg bg-red-600 flex items-center justify-center font-bold text-white text-lg">
            🔐
          </div>
          <div>
            <h1 className="text-lg font-bold text-white tracking-tight">Admin Portal</h1>
            <p className="text-xs text-gray-400">RE-OS System Management</p>
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

      <main className="max-w-6xl mx-auto p-6 space-y-8">
        {/* Error Banner */}
        {error && (
          <div className="bg-red-950/40 border border-red-800 rounded-lg p-4 flex items-start gap-3">
            <AlertCircle className="h-5 w-5 text-red-400 flex-shrink-0 mt-0.5" />
            <p className="text-sm text-red-300">{error}</p>
          </div>
        )}

        {/* KPI Grid */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Total Users</div>
            <div className="text-2xl font-bold mt-2">{totalUsers}</div>
            <div className="text-[10px] text-gray-500 mt-1">
              {metrics?.userStats.admin} admin, {metrics?.userStats.landlord} landlord,{' '}
              {metrics?.userStats.tenant} tenant
            </div>
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Monthly Rent (MRR)</div>
            <div className="text-2xl font-bold mt-2 text-emerald-400">${(currentMRR / 1000).toFixed(1)}K</div>
            <div className="text-[10px] text-gray-500 mt-1">Current month total</div>
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Occupancy Rate</div>
            <div className="text-2xl font-bold mt-2 text-blue-400">{metrics?.occupancy.rate || 0}%</div>
            <div className="text-[10px] text-gray-500 mt-1">
              {metrics?.occupancy.occupied} of {metrics?.occupancy.total} units
            </div>
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Collection Rate</div>
            <div className="text-2xl font-bold mt-2 text-amber-400">{health?.collectionRate || 0}%</div>
            <div className="text-[10px] text-gray-500 mt-1">
              {health?.paid} paid, {health?.late} late
            </div>
          </div>
        </div>

        {/* Quick Actions */}
        <div className="space-y-4">
          <h2 className="text-sm font-bold text-white">Admin Functions</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <Link href="/admin/users">
              <div className="bg-gray-900 border border-gray-800 hover:border-gray-700 rounded-xl p-6 cursor-pointer transition-all">
                <div className="flex items-center gap-3 mb-3">
                  <Users className="h-5 w-5 text-blue-500" />
                  <h3 className="font-semibold text-white">User Management</h3>
                </div>
                <p className="text-xs text-gray-400">Create, suspend, manage user accounts</p>
              </div>
            </Link>

            <Link href="/admin/disputes">
              <div className="bg-gray-900 border border-gray-800 hover:border-gray-700 rounded-xl p-6 cursor-pointer transition-all">
                <div className="flex items-center gap-3 mb-3">
                  <AlertCircle className="h-5 w-5 text-amber-500" />
                  <h3 className="font-semibold text-white">Payment Disputes</h3>
                </div>
                <p className="text-xs text-gray-400">Review and resolve payment disputes</p>
              </div>
            </Link>

            <Link href="/admin/reports">
              <div className="bg-gray-900 border border-gray-800 hover:border-gray-700 rounded-xl p-6 cursor-pointer transition-all">
                <div className="flex items-center gap-3 mb-3">
                  <BarChart3 className="h-5 w-5 text-green-500" />
                  <h3 className="font-semibold text-white">Analytics</h3>
                </div>
                <p className="text-xs text-gray-400">View detailed platform metrics</p>
              </div>
            </Link>
          </div>
        </div>

        {/* MRR Trend */}
        {metrics?.mrrTrend && (
          <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
            <div className="flex items-center gap-2 mb-4">
              <TrendingUp className="h-5 w-5 text-emerald-500" />
              <h3 className="font-bold text-white">Revenue Trend (Last 6 Months)</h3>
            </div>
            <div className="grid grid-cols-3 md:grid-cols-6 gap-2">
              {Object.entries(metrics.mrrTrend)
                .slice(-6)
                .map(([month, amount]) => (
                  <div key={month} className="bg-gray-950 rounded-lg p-3 text-center">
                    <div className="text-[10px] text-gray-400 mb-1">{month}</div>
                    <div className="text-sm font-bold text-emerald-400">${(Number(amount) / 1000).toFixed(1)}K</div>
                  </div>
                ))}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
