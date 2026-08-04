'use client';

import { useEffect, useState } from 'react';
import { useAuth } from '@/hooks/useAuth';
import { paymentsApi } from '@/lib/api';
import {
  CreditCard,
  DollarSign,
  AlertCircle,
  CheckCircle,
  ChevronRight,
  Loader2,
  RefreshCw,
} from 'lucide-react';

interface RentPayment {
  id: string;
  unit_id: string;
  month: string;
  amount: number;
  paid_date: string | null;
  status: 'pending' | 'paid' | 'late';
  stripe_payment_id: string | null;
}

export default function BillingPage() {
  const { logout, isLoading: authLoading } = useAuth();
  const [payments, setPayments] = useState<RentPayment[]>([]);
  const [loading, setLoading] = useState(true);
  const [syncStatus, setSyncStatus] = useState<any>(null);
  const [refundLoading, setRefundLoading] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const payRes = await paymentsApi.list();
      if (payRes.error) throw new Error(payRes.error);
      setPayments((payRes.data as RentPayment[]) || []);

      const reconRes = await fetch('/api/rent-payments/reconciliation');
      if (reconRes.ok) {
        setSyncStatus(await reconRes.json());
      }
    } catch (err: any) {
      setError(err.message || 'Failed to load billing data');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleRefund = async (paymentId: string, reason: string) => {
    setRefundLoading(paymentId);
    try {
      const res = await fetch('/api/rent-payments/refund', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ paymentId, reason }),
      });

      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.error);
      }

      const data = await res.json();
      alert(`Refund initiated: ${data.refundId}`);
      await fetchData();
    } catch (err: any) {
      alert(err.message || 'Failed to process refund');
    } finally {
      setRefundLoading(null);
    }
  };

  const handlePortalLink = async () => {
    try {
      const res = await fetch('/api/rent-payments/portal', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ customerId: 'cus_example' }),
      });

      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.error);
      }

      const data = await res.json();
      window.open(data.url, '_blank');
    } catch (err: any) {
      alert(err.message || 'Failed to open billing portal');
    }
  };

  const paidCount = payments.filter(p => p.status === 'paid').length;
  const pendingCount = payments.filter(p => p.status === 'pending').length;
  const lateCount = payments.filter(p => p.status === 'late').length;
  const totalCollected = payments
    .filter(p => p.status === 'paid')
    .reduce((sum, p) => sum + p.amount, 0);

  const last12Months = payments
    .sort((a, b) => new Date(b.month).getTime() - new Date(a.month).getTime())
    .slice(0, 12);

  if (authLoading || loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-900">
        <div className="text-center space-y-4">
          <Loader2 className="animate-spin h-10 w-10 text-blue-500 mx-auto" />
          <p className="text-gray-400 text-sm">Loading billing dashboard...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100 font-sans">
      <header className="border-b border-gray-800 bg-gray-900 px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <CreditCard className="h-6 w-6 text-blue-500" />
          <div>
            <h1 className="text-lg font-bold text-white">Billing & Payments</h1>
            <p className="text-xs text-gray-400">Manage subscriptions and payment history</p>
          </div>
        </div>
        <button
          onClick={logout}
          className="text-xs text-gray-400 hover:text-white font-semibold px-3 py-1.5 rounded-lg border border-gray-800 hover:bg-gray-800 transition-colors"
        >
          Sign Out
        </button>
      </header>

      <main className="max-w-6xl mx-auto p-6 space-y-8">
        {error && (
          <div className="bg-red-950/30 border border-red-800 rounded-lg p-4 flex items-start gap-3">
            <AlertCircle className="h-5 w-5 text-red-400 flex-shrink-0 mt-0.5" />
            <div className="text-sm text-red-200">{error}</div>
          </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="bg-gray-900 border border-gray-800 rounded-lg p-4">
            <div className="text-xs font-semibold text-gray-400 uppercase">Total Collected</div>
            <div className="text-2xl font-bold text-emerald-400 mt-2">
              ${totalCollected.toLocaleString()}
            </div>
            <div className="text-[10px] text-gray-500 mt-1">{paidCount} payments received</div>
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-lg p-4">
            <div className="text-xs font-semibold text-gray-400 uppercase">Pending</div>
            <div className="text-2xl font-bold text-amber-500 mt-2">
              ${payments
                .filter(p => p.status === 'pending')
                .reduce((sum, p) => sum + p.amount, 0)
                .toLocaleString()}
            </div>
            <div className="text-[10px] text-gray-500 mt-1">{pendingCount} awaiting payment</div>
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-lg p-4">
            <div className="text-xs font-semibold text-gray-400 uppercase">Overdue</div>
            <div className="text-2xl font-bold text-red-500 mt-2">
              ${payments
                .filter(p => p.status === 'late')
                .reduce((sum, p) => sum + p.amount, 0)
                .toLocaleString()}
            </div>
            <div className="text-[10px] text-gray-500 mt-1">{lateCount} past due</div>
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-lg p-4">
            <div className="text-xs font-semibold text-gray-400 uppercase">Sync Status</div>
            <div className="mt-2 space-y-1 text-[10px]">
              <div className="text-gray-300">
                {syncStatus?.webhookStats?.processed || 0} events processed
              </div>
              <div className="text-gray-500">
                Last: {syncStatus?.lastSync ? new Date(syncStatus.lastSync).toLocaleDateString() : 'Never'}
              </div>
            </div>
          </div>
        </div>

        <div className="bg-gray-900 border border-gray-800 rounded-lg p-6">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-lg font-bold">Payment Method</h2>
            <button
              onClick={handlePortalLink}
              className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold rounded-lg transition-colors"
            >
              Manage Subscription
              <ChevronRight className="h-4 w-4" />
            </button>
          </div>
          <div className="p-4 bg-gray-950 border border-gray-800 rounded-lg">
            <p className="text-sm text-gray-300">
              Click "Manage Subscription" to update payment methods and billing settings in Stripe Customer
              Portal.
            </p>
          </div>
        </div>

        <div className="bg-gray-900 border border-gray-800 rounded-lg overflow-hidden">
          <div className="px-6 py-4 border-b border-gray-800 flex items-center justify-between">
            <h2 className="text-lg font-bold">Transaction History (Last 12 Months)</h2>
            <button
              onClick={fetchData}
              className="p-2 rounded-lg hover:bg-gray-800 transition-colors"
              title="Refresh"
            >
              <RefreshCw className="h-4 w-4 text-gray-400" />
            </button>
          </div>

          {last12Months.length === 0 ? (
            <div className="p-12 text-center text-gray-400">
              <DollarSign className="h-12 w-12 text-gray-700 mx-auto mb-3" />
              <p className="text-xs">No transactions recorded yet.</p>
            </div>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs border-collapse">
                <thead>
                  <tr className="bg-gray-950 text-gray-400 uppercase tracking-wider font-semibold border-b border-gray-800">
                    <th className="px-6 py-3">Month</th>
                    <th className="px-6 py-3">Amount</th>
                    <th className="px-6 py-3">Paid Date</th>
                    <th className="px-6 py-3">Status</th>
                    <th className="px-6 py-3">Action</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-800">
                  {last12Months.map(payment => (
                    <tr key={payment.id} className="hover:bg-gray-800/40">
                      <td className="px-6 py-4 text-gray-300 font-medium">
                        {new Date(payment.month + '-01').toLocaleDateString(undefined, {
                          month: 'long',
                          year: 'numeric',
                        })}
                      </td>
                      <td className="px-6 py-4 text-gray-300">${payment.amount.toLocaleString()}</td>
                      <td className="px-6 py-4 text-gray-400">
                        {payment.paid_date ? new Date(payment.paid_date).toLocaleDateString() : '—'}
                      </td>
                      <td className="px-6 py-4">
                        <span
                          className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase inline-flex items-center gap-1 ${
                            payment.status === 'paid'
                              ? 'bg-emerald-950/40 text-emerald-400 border border-emerald-800'
                              : payment.status === 'late'
                              ? 'bg-red-950/40 text-red-400 border border-red-800'
                              : 'bg-amber-950/40 text-amber-500 border border-amber-800'
                          }`}
                        >
                          {payment.status === 'paid' && <CheckCircle className="h-3 w-3" />}
                          {payment.status === 'late' && <AlertCircle className="h-3 w-3" />}
                          {payment.status}
                        </span>
                      </td>
                      <td className="px-6 py-4">
                        {payment.status === 'paid' && (
                          <button
                            onClick={() => handleRefund(payment.id, 'Landlord initiated refund')}
                            disabled={refundLoading === payment.id}
                            className="text-xs text-gray-400 hover:text-red-400 transition-colors disabled:opacity-50"
                          >
                            {refundLoading === payment.id ? (
                              <Loader2 className="h-3 w-3 animate-spin inline" />
                            ) : (
                              'Refund'
                            )}
                          </button>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
