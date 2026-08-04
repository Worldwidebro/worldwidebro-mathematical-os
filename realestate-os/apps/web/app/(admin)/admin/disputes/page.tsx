'use client';

import { useEffect, useState } from 'react';
import { useAuth } from '@/hooks/useAuth';
import { Loader2, AlertCircle, LogOut, CheckCircle, Clock } from 'lucide-react';
import Link from 'next/link';

interface Dispute {
  id: string;
  payment_id: string;
  tenant_id: string;
  reason: string;
  status: 'pending' | 'under_review' | 'resolved' | 'rejected';
  admin_notes: string | null;
  resolved_by: string | null;
  resolved_at: string | null;
  created_at: string;
  updated_at: string;
}

export default function DisputesPage() {
  const { logout, isLoading: authLoading } = useAuth();
  const [disputes, setDisputes] = useState<Dispute[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedDispute, setSelectedDispute] = useState<Dispute | null>(null);
  const [notes, setNotes] = useState('');
  const [resolving, setResolving] = useState(false);

  const fetchDisputes = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch('/api/admin/disputes');
      if (!res.ok) throw new Error('Failed to load disputes');
      const data = await res.json();
      setDisputes(data || []);
    } catch (err: any) {
      setError(err.message || 'Error loading disputes');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchDisputes();
  }, []);

  const handleResolveDispute = async (resolution: 'approved' | 'rejected') => {
    if (!selectedDispute || !notes.trim()) {
      alert('Please add notes');
      return;
    }

    setResolving(true);
    try {
      const res = await fetch(`/api/admin/disputes/${selectedDispute.id}/resolve`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          adminNotes: notes,
          resolution,
        }),
      });

      if (!res.ok) throw new Error('Failed to resolve dispute');

      // Update local state
      setDisputes(prev =>
        prev.map(d =>
          d.id === selectedDispute.id
            ? {
                ...d,
                status: resolution === 'approved' ? 'resolved' : 'rejected',
                admin_notes: notes,
                resolved_at: new Date().toISOString(),
              }
            : d
        )
      );

      setSelectedDispute(null);
      setNotes('');
    } catch (err: any) {
      alert(err.message || 'Error resolving dispute');
    } finally {
      setResolving(false);
    }
  };

  if (authLoading || loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-950">
        <div className="text-center space-y-4">
          <Loader2 className="animate-spin h-10 w-10 text-blue-500 mx-auto" />
          <p className="text-gray-400 text-sm">Loading...</p>
        </div>
      </div>
    );
  }

  const pendingCount = disputes.filter(d => d.status === 'pending' || d.status === 'under_review').length;

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      {/* Header */}
      <header className="border-b border-gray-800 bg-gray-900 px-6 py-4 flex items-center justify-between">
        <Link href="/admin" className="flex items-center gap-3">
          <div className="h-9 w-9 rounded-lg bg-red-600 flex items-center justify-center font-bold text-white">
            🔐
          </div>
          <div>
            <h1 className="text-lg font-bold text-white tracking-tight">Payment Disputes</h1>
            <p className="text-xs text-gray-400">Review & resolve payment disputes</p>
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

      <main className="max-w-6xl mx-auto p-6 space-y-6">
        {/* Error Banner */}
        {error && (
          <div className="bg-red-950/40 border border-red-800 rounded-lg p-4 flex items-start gap-3">
            <AlertCircle className="h-5 w-5 text-red-400 flex-shrink-0 mt-0.5" />
            <p className="text-sm text-red-300">{error}</p>
          </div>
        )}

        {/* Summary */}
        <div className="bg-gray-900 border border-gray-800 rounded-xl p-5">
          <div className="flex items-center gap-3">
            <Clock className="h-5 w-5 text-amber-500" />
            <div>
              <div className="text-sm font-bold text-white">Pending Review: {pendingCount}</div>
              <div className="text-xs text-gray-400">Disputes awaiting resolution</div>
            </div>
          </div>
        </div>

        {/* Disputes Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {disputes.length === 0 ? (
            <div className="col-span-2 bg-gray-900 border border-gray-800 rounded-xl p-12 text-center">
              <CheckCircle className="h-12 w-12 text-gray-600 mx-auto mb-3" />
              <p className="text-sm text-gray-400">No disputes</p>
            </div>
          ) : (
            disputes.map(dispute => (
              <div
                key={dispute.id}
                className={`bg-gray-900 border rounded-xl p-5 cursor-pointer transition-all ${
                  selectedDispute?.id === dispute.id
                    ? 'border-blue-500 ring-2 ring-blue-500/20'
                    : 'border-gray-800 hover:border-gray-700'
                }`}
                onClick={() => setSelectedDispute(dispute)}
              >
                <div className="flex items-start justify-between mb-3">
                  <div>
                    <div className="text-xs font-semibold text-gray-400 mb-1">
                      Payment #{dispute.payment_id.slice(0, 8)}
                    </div>
                    <div className="text-sm font-bold text-white">{dispute.reason}</div>
                  </div>
                  <span
                    className={`text-[10px] px-2 py-0.5 rounded border font-medium ${
                      dispute.status === 'pending'
                        ? 'bg-amber-950/40 text-amber-400 border-amber-800'
                        : dispute.status === 'under_review'
                          ? 'bg-blue-950/40 text-blue-400 border-blue-800'
                          : dispute.status === 'resolved'
                            ? 'bg-emerald-950/40 text-emerald-400 border-emerald-800'
                            : 'bg-gray-800 text-gray-400 border-gray-700'
                    }`}
                  >
                    {dispute.status}
                  </span>
                </div>

                <div className="space-y-2 text-xs text-gray-400">
                  <div>
                    Tenant ID: <span className="text-gray-300">{dispute.tenant_id.slice(0, 8)}</span>
                  </div>
                  <div>
                    Submitted:{' '}
                    <span className="text-gray-300">
                      {new Date(dispute.created_at).toLocaleDateString()}
                    </span>
                  </div>
                  {dispute.admin_notes && (
                    <div className="pt-2 border-t border-gray-800">
                      <div className="text-gray-400">Admin notes:</div>
                      <div className="text-gray-300 italic mt-1">{dispute.admin_notes}</div>
                    </div>
                  )}
                </div>
              </div>
            ))
          )}
        </div>

        {/* Resolution Panel */}
        {selectedDispute && selectedDispute.status !== 'resolved' && selectedDispute.status !== 'rejected' && (
          <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
            <h3 className="text-sm font-bold text-white mb-4">Resolve Dispute</h3>
            <div className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-gray-400 mb-2">Admin Notes</label>
                <textarea
                  value={notes}
                  onChange={e => setNotes(e.target.value)}
                  className="w-full bg-gray-950 border border-gray-800 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500 resize-none h-24"
                  placeholder="Provide resolution details..."
                />
              </div>
              <div className="flex gap-3">
                <button
                  onClick={() => handleResolveDispute('approved')}
                  disabled={resolving}
                  className="flex-1 px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-semibold transition-colors disabled:opacity-50 flex items-center justify-center gap-2"
                >
                  {resolving && <Loader2 className="animate-spin h-3.5 w-3.5" />}
                  Approve
                </button>
                <button
                  onClick={() => handleResolveDispute('rejected')}
                  disabled={resolving}
                  className="flex-1 px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg text-xs font-semibold transition-colors disabled:opacity-50 flex items-center justify-center gap-2"
                >
                  {resolving && <Loader2 className="animate-spin h-3.5 w-3.5" />}
                  Reject
                </button>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
