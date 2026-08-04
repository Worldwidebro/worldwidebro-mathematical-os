'use client';

import { useEffect, useState } from 'react';
import { useAuth } from '@/hooks/useAuth';
import { Loader2, AlertCircle, LogOut, TrendingUp, TrendingDown, Users, Building, CreditCard } from 'lucide-react';
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

interface ChurnData {
  expiredLeases: number;
  leases: Array<{ end_date: string; tenant_id: string }>;
}

export default function ReportsPage() {
  const { logout, isLoading: authLoading } = useAuth();
  const [metrics, setMetrics] = useState<Metrics | null>(null);
  const [health, setHealth] = useState<PaymentHealth | null>(null);
  const [churn, setChurn] = useState<ChurnData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const [metricsRes, healthRes, churnRes] = await Promise.all([
        fetch('/api/admin/reports/metrics'),
        fetch('/api/admin/reports/payment-health'),
        fetch('/api/admin/reports/churn'),
      ]);

      if (!metricsRes.ok || !healthRes.ok || !churnRes.ok) {
        throw new Error('Failed to load reports');
      }

      const [metricsData, healthData, churnData] = await Promise.all([
        metricsRes.json(),
        healthRes.json(),
        churnRes.json(),
      ]);

      setMetrics(metricsData);
      setHealth(healthData);
      setChurn(churnData);
    } catch (err: any) {
      setError(err.message || 'Error loading reports');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  if (authLoading || loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-950">
        <div className="text-center space-y-4">
          <Loader2 className="animate-spin h-10 w-10 text-blue-500 mx-auto" />
          <p className="text-gray-400 text-sm">Loading analytics...</p>
        </div>
      </div>
    );
  }

  const userTotal = metrics
    ? metrics.userStats.admin + metrics.userStats.landlord + metrics.userStats.tenant
    : 0;

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      {/* Header */}
      <header className="border-b border-gray-800 bg-gray-900 px-6 py-4 flex items-center justify-between">
        <Link href="/admin" className="flex items-center gap-3">
          <div className="h-9 w-9 rounded-lg bg-red-600 flex items-center justify-center font-bold text-white">
            🔐
          </div>
          <div>
            <h1 className="text-lg font-bold text-white tracking-tight">Analytics</h1>
            <p className="text-xs text-gray-400">Platform metrics & reporting</p>
          </div>
        </Link>
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

        {/* User Metrics */}
        <div className="space-y-4">
          <h2 className="text-sm font-bold text-white">User Base</h2>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
              <div className="flex items-center gap-2 mb-2">
                <Users className="h-4 w-4 text-blue-500" />
                <span className="text-xs font-semibold text-gray-400">Total Users</span>
              </div>
              <div className="text-2xl font-bold text-white">{userTotal}</div>
            </div>

            <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
              <div className="flex items-center gap-2 mb-2">
                <Users className="h-4 w-4 text-red-500" />
                <span className="text-xs font-semibold text-gray-400">Admins</span>
              </div>
              <div className="text-2xl font-bold text-white">{metrics?.userStats.admin || 0}</div>
            </div>

            <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
              <div className="flex items-center gap-2 mb-2">
                <Building className="h-4 w-4 text-blue-500" />
                <span className="text-xs font-semibold text-gray-400">Landlords</span>
              </div>
              <div className="text-2xl font-bold text-white">{metrics?.userStats.landlord || 0}</div>
            </div>

            <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
              <div className="flex items-center gap-2 mb-2">
                <Users className="h-4 w-4 text-green-500" />
                <span className="text-xs font-semibold text-gray-400">Tenants</span>
              </div>
              <div className="text-2xl font-bold text-white">{metrics?.userStats.tenant || 0}</div>
            </div>
          </div>
        </div>

        {/* Occupancy & Tickets */}
        <div className="space-y-4">
          <h2 className="text-sm font-bold text-white">Property Management</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
              <div className="text-xs font-semibold text-gray-400 mb-2">Occupancy Rate</div>
              <div className="text-3xl font-bold text-emerald-400">{metrics?.occupancy.rate || 0}%</div>
              <div className="text-xs text-gray-500 mt-2">
                {metrics?.occupancy.occupied} of {metrics?.occupancy.total} units occupied
              </div>
            </div>

            <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
              <div className="text-xs font-semibold text-gray-400 mb-2">Open Tickets</div>
              <div className="text-3xl font-bold text-amber-400">{metrics?.openTickets || 0}</div>
              <div className="text-xs text-gray-500 mt-2">Maintenance requests pending</div>
            </div>

            <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
              <div className="text-xs font-semibold text-gray-400 mb-2">Churn Risk</div>
              <div className="text-3xl font-bold text-red-400">{churn?.expiredLeases || 0}</div>
              <div className="text-xs text-gray-500 mt-2">Expired leases requiring renewal</div>
            </div>
          </div>
        </div>

        {/* Payment Health */}
        <div className="space-y-4">
          <h2 className="text-sm font-bold text-white">Payment Collection</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
              <div className="flex items-center gap-2 mb-4">
                <CreditCard className="h-5 w-5 text-emerald-500" />
                <h3 className="font-semibold text-white">Collection Rate</h3>
              </div>
              <div className="text-4xl font-bold text-emerald-400 mb-2">{health?.collectionRate || 0}%</div>
              <div className="space-y-2 text-xs">
                <div className="flex justify-between">
                  <span className="text-gray-400">Paid:</span>
                  <span className="text-emerald-400 font-semibold">{health?.paid || 0}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-400">Pending:</span>
                  <span className="text-amber-400 font-semibold">{health?.pending || 0}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-400">Late:</span>
                  <span className="text-red-400 font-semibold">{health?.late || 0}</span>
                </div>
              </div>
            </div>

            <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
              <div className="flex items-center gap-2 mb-4">
                <TrendingUp className="h-5 w-5 text-blue-500" />
                <h3 className="font-semibold text-white">Payment Status Breakdown</h3>
              </div>
              <div className="space-y-3">
                <div>
                  <div className="flex justify-between text-xs mb-1">
                    <span className="text-gray-400">Paid</span>
                    <span className="text-emerald-400">
                      {((health?.paid || 0) / (health?.total || 1) * 100).toFixed(0)}%
                    </span>
                  </div>
                  <div className="h-1.5 bg-gray-800 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-emerald-500"
                      style={{ width: `${((health?.paid || 0) / (health?.total || 1) * 100)}%` }}
                    ></div>
                  </div>
                </div>
                <div>
                  <div className="flex justify-between text-xs mb-1">
                    <span className="text-gray-400">Pending</span>
                    <span className="text-amber-400">
                      {((health?.pending || 0) / (health?.total || 1) * 100).toFixed(0)}%
                    </span>
                  </div>
                  <div className="h-1.5 bg-gray-800 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-amber-500"
                      style={{ width: `${((health?.pending || 0) / (health?.total || 1) * 100)}%` }}
                    ></div>
                  </div>
                </div>
                <div>
                  <div className="flex justify-between text-xs mb-1">
                    <span className="text-gray-400">Late</span>
                    <span className="text-red-400">
                      {((health?.late || 0) / (health?.total || 1) * 100).toFixed(0)}%
                    </span>
                  </div>
                  <div className="h-1.5 bg-gray-800 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-red-500"
                      style={{ width: `${((health?.late || 0) / (health?.total || 1) * 100)}%` }}
                    ></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* MRR Trend */}
        {metrics?.mrrTrend && Object.keys(metrics.mrrTrend).length > 0 && (
          <div className="space-y-4">
            <h2 className="text-sm font-bold text-white">Monthly Recurring Revenue</h2>
            <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
              <div className="space-y-4">
                {Object.entries(metrics.mrrTrend)
                  .slice(-6)
                  .map(([month, amount], idx, arr) => {
                    const prev = idx > 0 ? arr[idx - 1][1] : amount;
                    const change = Number(amount) - Number(prev);
                    const pct = prev !== 0 ? ((change / Number(prev)) * 100).toFixed(1) : 0;

                    return (
                      <div key={month}>
                        <div className="flex items-center justify-between mb-2">
                          <span className="text-xs font-semibold text-gray-400">{month}</span>
                          <div className="flex items-center gap-2">
                            <span className="text-sm font-bold text-emerald-400">
                              ${(Number(amount) / 1000).toFixed(1)}K
                            </span>
                            {change > 0 ? (
                              <span className="flex items-center gap-0.5 text-xs text-emerald-400">
                                <TrendingUp className="h-3 w-3" />
                                +{pct}%
                              </span>
                            ) : change < 0 ? (
                              <span className="flex items-center gap-0.5 text-xs text-red-400">
                                <TrendingDown className="h-3 w-3" />
                                {pct}%
                              </span>
                            ) : (
                              <span className="text-xs text-gray-400">—</span>
                            )}
                          </div>
                        </div>
                        <div className="h-2 bg-gray-800 rounded-full overflow-hidden">
                          <div
                            className="h-full bg-emerald-500"
                            style={{ width: `${Math.min((Number(amount) / 20000) * 100, 100)}%` }}
                          ></div>
                        </div>
                      </div>
                    );
                  })}
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
