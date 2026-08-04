'use client';

import { useEffect, useState } from 'react';
import { useAuth } from '@/hooks/useAuth';
import { supabase } from '@/lib/supabase-client';
import { maintenanceApi } from '@/lib/api';
import axios from 'axios';
import { 
  Home, 
  Calendar, 
  CreditCard, 
  Wrench, 
  AlertCircle, 
  CheckCircle2, 
  Loader2, 
  ArrowRight, 
  LogOut,
  User,
  Clock
} from 'lucide-react';

interface Property {
  id: string;
  address: string;
  city: string;
  state: string;
  zip_code: string;
}

interface Unit {
  id: string;
  property_id: string;
  unit_number: string;
  rent_amount: number;
  properties?: Property;
}

interface Lease {
  id: string;
  unit_id: string;
  start_date: string;
  end_date: string;
  terms: any;
}

interface RentPayment {
  id: string;
  month: string;
  amount: number;
  paid_date: string | null;
  status: 'pending' | 'paid' | 'late';
}

interface MaintenanceRequest {
  id: string;
  description: string;
  status: 'open' | 'assigned' | 'in_progress' | 'completed';
  created_at: string;
}

export default function TenantPortal() {
  const { user, logout, isLoading: authLoading } = useAuth();
  
  // Data state
  const [unit, setUnit] = useState<Unit | null>(null);
  const [lease, setLease] = useState<Lease | null>(null);
  const [payments, setPayments] = useState<RentPayment[]>([]);
  const [maintenance, setMaintenance] = useState<MaintenanceRequest[]>([]);
  
  // UI states
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'lease' | 'payments' | 'maintenance'>('lease');
  const [payLoading, setPayLoading] = useState(false);
  
  // Maintenance Form state
  const [description, setDescription] = useState('');
  const [maintLoading, setMaintLoading] = useState(false);

  const fetchTenantData = async () => {
    if (!user) return;
    setLoading(true);
    try {
      // 1. Fetch unit
      const { data: unitData, error: unitErr } = await supabase
        .from('units')
        .select('*, properties:property_id(*)')
        .eq('tenant_id', user.id)
        .maybeSingle();

      if (unitErr) throw unitErr;
      
      if (unitData) {
        setUnit(unitData as any);

        // 2. Fetch lease
        const { data: leaseData, error: leaseErr } = await supabase
          .from('leases')
          .select('*')
          .eq('tenant_id', user.id)
          .maybeSingle();

        if (leaseErr) throw leaseErr;
        setLease(leaseData);

        // 3. Fetch payments
        const { data: payData, error: payErr } = await supabase
          .from('rent_payments')
          .select('*')
          .eq('unit_id', unitData.id)
          .order('month', { ascending: false });

        if (payErr) throw payErr;
        setPayments(payData || []);

        // 4. Fetch maintenance requests
        const { data: maintData, error: maintErr } = await supabase
          .from('maintenance_requests')
          .select('*')
          .eq('tenant_id', user.id)
          .order('created_at', { ascending: false });

        if (maintErr) throw maintErr;
        setMaintenance(maintData || []);
      }
    } catch (err) {
      console.error('Error loading tenant data:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (!authLoading && user) {
      fetchTenantData();
    }
  }, [user, authLoading]);

  const handlePayRent = async (payment: RentPayment) => {
    if (!unit) return;
    setPayLoading(true);
    try {
      const token = (await supabase.auth.getSession()).data.session?.access_token;
      
      const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3001';
      const res = await axios.post(`${API_URL}/api/rent-payments/create-payment-link`, {
        unitId: unit.id,
        month: payment.month,
        amount: payment.amount
      }, {
        headers: {
          'x-user-id': user?.id,
          'Authorization': `Bearer ${token}`
        }
      });

      if (res.data?.url) {
        window.location.href = res.data.url;
      } else {
        throw new Error('Failed to generate payment redirect');
      }
    } catch (err: any) {
      console.error(err);
      alert(err.response?.data?.error || err.message || 'Payment server offline');
    } finally {
      setPayLoading(false);
    }
  };

  const handleCreateMaintenance = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!description.trim() || !unit) return;
    setMaintLoading(true);
    try {
      const res = await maintenanceApi.create({
        propertyId: unit.property_id,
        description,
        photoUrl: ''
      });

      if (res.error) throw new Error(res.error);
      setDescription('');
      
      // Reload requests
      const { data: maintData } = await supabase
        .from('maintenance_requests')
        .select('*')
        .eq('tenant_id', user!.id)
        .order('created_at', { ascending: false });
      setMaintenance(maintData || []);
      
      alert('Maintenance request submitted successfully!');
    } catch (err: any) {
      alert(err.message || 'Failed to submit request');
    } finally {
      setMaintLoading(false);
    }
  };

  if (authLoading || loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-900">
        <div className="text-center space-y-4">
          <Loader2 className="animate-spin h-10 w-10 text-emerald-500 mx-auto" />
          <p className="text-gray-400 text-sm">Authenticating Tenant Profile...</p>
        </div>
      </div>
    );
  }

  // Find active due rent payment
  const pendingPayment = payments.find(p => p.status === 'pending');

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100 font-sans">
      {/* Navigation Header */}
      <header className="border-b border-gray-800 bg-gray-900 px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="h-9 w-9 rounded-lg bg-emerald-600 flex items-center justify-center font-bold text-white text-lg">
            👤
          </div>
          <div>
            <h1 className="text-lg font-bold text-white tracking-tight">Worldwidebro Real Estate</h1>
            <p className="text-xs text-gray-400">Tenant OS Portal</p>
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

      {!unit ? (
        <main className="max-w-xl mx-auto p-12 text-center mt-12 bg-gray-900 border border-gray-800 rounded-xl space-y-4">
          <Home className="h-12 w-12 text-gray-600 mx-auto" />
          <h2 className="text-lg font-bold text-white">No Lease Active</h2>
          <p className="text-sm text-gray-400">Your account is not currently linked to any active rental unit lease. Please contact your property manager to finish onboarding.</p>
        </main>
      ) : (
        <main className="max-w-4xl mx-auto p-6 space-y-8">
          {/* Welcome Dashboard Header */}
          <div className="flex flex-wrap items-center justify-between gap-4 bg-gray-900 border border-gray-800 rounded-xl p-6">
            <div className="space-y-1">
              <h2 className="text-xl font-bold text-white flex items-center gap-2">
                Welcome back, {user?.fullName || 'Resident'}!
              </h2>
              <p className="text-xs text-gray-400">
                Unit {unit.unit_number} · {unit.properties?.address}, {unit.properties?.city}
              </p>
            </div>
            {pendingPayment ? (
              <div className="flex items-center gap-4 bg-amber-950/20 border border-amber-800/60 rounded-lg p-3">
                <AlertCircle className="h-5 w-5 text-amber-500 flex-shrink-0" />
                <div className="text-xs">
                  <div className="font-semibold text-white">Rent payment pending</div>
                  <div className="text-gray-400">${Number(pendingPayment.amount).toLocaleString()} due for {new Date(pendingPayment.month + '-02').toLocaleDateString(undefined, {month: 'long'})}</div>
                </div>
                <button 
                  onClick={() => handlePayRent(pendingPayment)}
                  disabled={payLoading}
                  className="px-3 py-1.5 bg-amber-600 hover:bg-amber-700 disabled:bg-gray-700 text-white font-bold text-xs rounded transition-colors flex items-center gap-1"
                >
                  {payLoading && <Loader2 className="animate-spin h-3.5 w-3.5" />}
                  Pay Rent
                </button>
              </div>
            ) : (
              <div className="flex items-center gap-3 bg-emerald-950/20 border border-emerald-800/60 rounded-lg p-3">
                <CheckCircle2 className="h-5 w-5 text-emerald-500" />
                <div className="text-xs text-emerald-400 font-semibold">Rent fully paid for this month!</div>
              </div>
            )}
          </div>

          {/* Tabs Navigation */}
          <div className="flex gap-6 border-b border-gray-800">
            <button 
              onClick={() => setActiveTab('lease')}
              className={`py-3 text-sm font-medium border-b-2 transition-all ${
                activeTab === 'lease' ? 'border-emerald-500 text-white' : 'border-transparent text-gray-400 hover:text-white'
              }`}
            >
              My Lease
            </button>
            <button 
              onClick={() => setActiveTab('payments')}
              className={`py-3 text-sm font-medium border-b-2 transition-all ${
                activeTab === 'payments' ? 'border-emerald-500 text-white' : 'border-transparent text-gray-400 hover:text-white'
              }`}
            >
              Payment History
            </button>
            <button 
              onClick={() => setActiveTab('maintenance')}
              className={`py-3 text-sm font-medium border-b-2 transition-all ${
                activeTab === 'maintenance' ? 'border-emerald-500 text-white' : 'border-transparent text-gray-400 hover:text-white'
              }`}
            >
              Maintenance Requests
            </button>
          </div>

          {/* Tab Views */}
          {activeTab === 'lease' && (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="md:col-span-2 bg-gray-900 border border-gray-800 rounded-xl p-6 space-y-6">
                <h3 className="text-base font-bold text-white flex items-center gap-2">
                  <Calendar className="h-5 w-5 text-emerald-500" /> Agreement Summary
                </h3>
                {lease ? (
                  <div className="grid grid-cols-2 gap-6 text-sm">
                    <div className="space-y-1">
                      <div className="text-xs text-gray-400 uppercase">Lease Term</div>
                      <div className="text-white font-medium">
                        {new Date(lease.start_date).toLocaleDateString()} – {new Date(lease.end_date).toLocaleDateString()}
                      </div>
                    </div>
                    <div className="space-y-1">
                      <div className="text-xs text-gray-400 uppercase">Monthly Rental Amount</div>
                      <div className="text-white font-medium">${Number(unit.rent_amount).toLocaleString()} / month</div>
                    </div>
                    <div className="space-y-1">
                      <div className="text-xs text-gray-400 uppercase">Registered Resident</div>
                      <div className="text-white font-medium flex items-center gap-1">
                        <User className="h-4 w-4 text-gray-500" /> {user?.fullName || 'Resident'}
                      </div>
                    </div>
                  </div>
                ) : (
                  <p className="text-xs text-gray-400">Lease agreement details currently processing...</p>
                )}
              </div>

              <div className="bg-gray-900 border border-gray-800 rounded-xl p-6 flex flex-col justify-between">
                <div>
                  <h4 className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Utility Rules & Terms</h4>
                  <p className="text-xs text-gray-400 mt-3 leading-relaxed">
                    Rent is collected on the 1st of every month. Late penalties ($50 + $10/day) apply from the 5th onwards.
                  </p>
                </div>
                <button 
                  onClick={() => setActiveTab('payments')}
                  className="mt-6 w-full py-2 bg-gray-800 hover:bg-gray-700 text-white rounded-lg text-xs font-semibold flex items-center justify-center gap-1.5 transition-all"
                >
                  View Rent Statement
                  <ArrowRight className="h-4 w-4" />
                </button>
              </div>
            </div>
          )}

          {activeTab === 'payments' && (
            <div className="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden">
              <div className="px-6 py-4 border-b border-gray-800">
                <h3 className="font-bold text-white text-sm">Rent Payment Log</h3>
              </div>
              {payments.length === 0 ? (
                <div className="p-12 text-center text-gray-400">
                  <CreditCard className="h-12 w-12 text-gray-700 mx-auto mb-3" />
                  <p className="text-xs">No payment cycles recorded.</p>
                </div>
              ) : (
                <div className="overflow-x-auto">
                  <table className="w-full text-left text-xs border-collapse">
                    <thead>
                      <tr className="bg-gray-950 text-gray-400 uppercase tracking-wider font-semibold border-b border-gray-800">
                        <th className="px-6 py-3">Rental Period</th>
                        <th className="px-6 py-3">Amount Due</th>
                        <th className="px-6 py-3">Payment Date</th>
                        <th className="px-6 py-3">Payment Status</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-800">
                      {payments.map(pay => (
                        <tr key={pay.id} className="hover:bg-gray-800/40">
                          <td className="px-6 py-4 text-gray-300 font-medium">
                            {new Date(pay.month + '-02').toLocaleDateString(undefined, {month: 'long', year: 'numeric'})}
                          </td>
                          <td className="px-6 py-4 text-gray-300">${Number(pay.amount).toLocaleString()}</td>
                          <td className="px-6 py-4 text-gray-400">
                            {pay.paid_date ? new Date(pay.paid_date).toLocaleDateString() : '—'}
                          </td>
                          <td className="px-6 py-4">
                            <span className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase ${
                              pay.status === 'paid' 
                                ? 'bg-emerald-950/40 text-emerald-400 border border-emerald-800' 
                                : 'bg-amber-950/40 text-amber-500 border border-amber-800'
                            }`}>
                              {pay.status}
                            </span>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          )}

          {activeTab === 'maintenance' && (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {/* Request form */}
              <div className="bg-gray-900 border border-gray-800 rounded-xl p-6 h-fit">
                <h3 className="text-sm font-bold text-white mb-4 flex items-center gap-1.5">
                  <Wrench className="h-4.5 w-4.5 text-emerald-500" /> New Maintenance Request
                </h3>
                <form onSubmit={handleCreateMaintenance} className="space-y-4">
                  <div>
                    <label className="block text-xs font-semibold text-gray-400 mb-1">Issue Description</label>
                    <textarea 
                      value={description}
                      onChange={e => setDescription(e.target.value)}
                      rows={4}
                      className="w-full bg-gray-950 border border-gray-800 rounded-lg p-2.5 text-xs text-white focus:outline-none focus:border-emerald-500 resize-none"
                      placeholder="Explain the problem (e.g. Kitchen sink faucet leak)..."
                      required
                    />
                  </div>
                  <button 
                    type="submit"
                    disabled={maintLoading}
                    className="w-full py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-semibold flex items-center justify-center gap-1.5 transition-colors"
                  >
                    {maintLoading && <Loader2 className="animate-spin h-3.5 w-3.5" />}
                    File Ticket
                  </button>
                </form>
              </div>

              {/* Requests history */}
              <div className="md:col-span-2 bg-gray-900 border border-gray-800 rounded-xl p-6">
                <h3 className="text-sm font-bold text-white mb-4">Request Log</h3>
                {maintenance.length === 0 ? (
                  <div className="text-center py-12 text-gray-400">
                    <Clock className="h-10 w-10 text-gray-700 mx-auto mb-2" />
                    <p className="text-xs">No maintenance requests filed yet.</p>
                  </div>
                ) : (
                  <div className="space-y-4">
                    {maintenance.map(req => (
                      <div key={req.id} className="bg-gray-950 border border-gray-800/80 rounded-lg p-4 space-y-2">
                        <div className="flex items-center justify-between">
                          <span className={`text-[10px] px-2 py-0.5 rounded font-bold uppercase ${
                            req.status === 'completed' 
                              ? 'bg-emerald-950/40 text-emerald-400 border border-emerald-800' 
                              : req.status === 'in_progress' 
                              ? 'bg-blue-950/40 text-blue-400 border border-blue-800'
                              : 'bg-amber-950/40 text-amber-500 border border-amber-800'
                          }`}>
                            {req.status.replace('_', ' ')}
                          </span>
                          <span className="text-[10px] text-gray-500">{new Date(req.created_at).toLocaleDateString()}</span>
                        </div>
                        <p className="text-xs text-gray-300 leading-relaxed">{req.description}</p>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>
          )}
        </main>
      )}
    </div>
  );
}
