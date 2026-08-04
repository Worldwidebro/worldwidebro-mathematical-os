'use client';

import { useEffect, useState } from 'react';
import { useAuth } from '@/hooks/useAuth';
import { propertiesApi } from '@/lib/api';
import { maintenanceApi } from '@/lib/api';
import { paymentsApi } from '@/lib/api';
import { 
  Building, 
  Users, 
  DollarSign, 
  Wrench, 
  Plus, 
  Loader2, 
  CreditCard, 
  LogOut, 
  CheckCircle, 
  AlertCircle,
  TrendingUp,
  MapPin
} from 'lucide-react';

interface Property {
  id: string;
  address: string;
  city: string;
  state: string;
  zip_code: string;
  units_count: number;
  units?: Unit[];
}

interface Unit {
  id: string;
  unit_number: string;
  rent_amount: number;
  tenant_id: string | null;
}

interface MaintenanceRequest {
  id: string;
  property_id: string;
  tenant_id: string;
  description: string;
  status: 'open' | 'assigned' | 'in_progress' | 'completed';
  created_at: string;
}

interface RentPayment {
  id: string;
  unit_id: string;
  month: string;
  amount: number;
  paid_date: string | null;
  status: 'pending' | 'paid' | 'late';
}

export default function LandlordDashboard() {
  const { logout, isLoading: authLoading } = useAuth();
  
  // Data state
  const [properties, setProperties] = useState<Property[]>([]);
  const [maintenance, setMaintenance] = useState<MaintenanceRequest[]>([]);
  const [payments, setPayments] = useState<RentPayment[]>([]);
  
  // Loading & UI states
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'properties' | 'maintenance' | 'payments'>('properties');
  const [showAddProp, setShowAddProp] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Form state
  const [address, setAddress] = useState('');
  const [city, setCity] = useState('');
  const [stateForm, setStateForm] = useState('');
  const [zipCode, setZipCode] = useState('');
  const [unitsCount, setUnitsCount] = useState(1);
  const [rentPerUnit, setRentPerUnit] = useState(1000);
  const [formLoading, setFormLoading] = useState(false);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const propRes = await propertiesApi.list();
      if (propRes.error) throw new Error(propRes.error);
      const props = (propRes.data || []) as Property[];
      setProperties(props);

      // Fetch maintenance for each property
      let allMaintenance: MaintenanceRequest[] = [];
      let allPayments: RentPayment[] = [];

      for (const prop of props) {
        const maintRes = await maintenanceApi.list({ propertyId: prop.id });
        if (!maintRes.error && maintRes.data) {
          allMaintenance = [...allMaintenance, ...(maintRes.data as MaintenanceRequest[])];
        }

        const payRes = await paymentsApi.list({ propertyId: prop.id });
        if (!payRes.error && payRes.data) {
          allPayments = [...allPayments, ...(payRes.data as RentPayment[])];
        }
      }

      setMaintenance(allMaintenance);
      setPayments(allPayments);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Failed to load dashboard data');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleAddProperty = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!address || !city || !stateForm || !zipCode) {
      alert('Please fill in all fields');
      return;
    }

    setFormLoading(true);
    try {
      const res = await propertiesApi.create({
        address,
        city,
        state: stateForm,
        zipCode,
        unitsCount,
        rentAmount: rentPerUnit // Pass rent target per unit to auto-initialize units
      });

      if (res.error) throw new Error(res.error);

      // Reset form
      setAddress('');
      setCity('');
      setStateForm('');
      setZipCode('');
      setUnitsCount(1);
      setRentPerUnit(1000);
      setShowAddProp(false);
      
      // Reload dashboard
      await fetchData();
    } catch (err: any) {
      alert(err.message || 'Failed to add property');
    } finally {
      setFormLoading(false);
    }
  };

  const handleUpdateMaintenanceStatus = async (id: string, newStatus: 'in_progress' | 'completed') => {
    try {
      const res = await maintenanceApi.update(id, { status: newStatus });
      if (res.error) throw new Error(res.error);
      
      // Update local state
      setMaintenance(prev => 
        prev.map(item => item.id === id ? { ...item, status: newStatus } : item)
      );
    } catch (err: any) {
      alert(err.message || 'Failed to update maintenance request');
    }
  };

  // KPIs Calculations
  const totalUnits = properties.reduce((acc, p) => acc + (p.units_count || 0), 0);
  const occupiedUnits = properties.reduce((acc, p) => {
    const occupied = p.units?.filter(u => u.tenant_id !== null).length || 0;
    return acc + occupied;
  }, 0);
  const occupancyRate = totalUnits > 0 ? Math.round((occupiedUnits / totalUnits) * 100) : 0;
  const openTickets = maintenance.filter(m => m.status !== 'completed').length;
  const totalRevenue = payments
    .filter(p => p.status === 'paid')
    .reduce((acc, p) => acc + Number(p.amount), 0);

  if (authLoading || loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-900">
        <div className="text-center space-y-4">
          <Loader2 className="animate-spin h-10 w-10 text-blue-500 mx-auto" />
          <p className="text-gray-400 text-sm">Synchronizing Landlord OS Portal...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100 font-sans">
      {/* Top Navigation */}
      <header className="border-b border-gray-800 bg-gray-900 px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="h-9 w-9 rounded-lg bg-blue-600 flex items-center justify-center font-bold text-white text-lg">
            🏢
          </div>
          <div>
            <h1 className="text-lg font-bold text-white tracking-tight">Worldwidebro Real Estate</h1>
            <p className="text-xs text-gray-400">Landlord OS Dashboard</p>
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
        {/* KPI Grid */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="bg-gray-900 border border-gray-800 rounded-xl p-5 relative overflow-hidden">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Properties Managed</div>
            <div className="text-2xl font-bold mt-2 flex items-baseline gap-2">
              {properties.length}
              <span className="text-xs text-gray-500 font-medium">({totalUnits} Units)</span>
            </div>
            <Building className="absolute right-4 bottom-4 h-12 w-12 text-gray-800 opacity-20" />
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-xl p-5 relative overflow-hidden">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Occupancy Rate</div>
            <div className="text-2xl font-bold mt-2">{occupancyRate}%</div>
            <div className="text-[10px] text-gray-500 mt-1">{occupiedUnits} of {totalUnits} units active</div>
            <Users className="absolute right-4 bottom-4 h-12 w-12 text-gray-800 opacity-20" />
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-xl p-5 relative overflow-hidden">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider">YTD Rent Collection</div>
            <div className="text-2xl font-bold mt-2 text-emerald-400">${totalRevenue.toLocaleString()}</div>
            <div className="text-[10px] text-gray-500 mt-1">Stripe Checkout verified payouts</div>
            <DollarSign className="absolute right-4 bottom-4 h-12 w-12 text-gray-800 opacity-20" />
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-xl p-5 relative overflow-hidden">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Active Tickets</div>
            <div className="text-2xl font-bold mt-2 text-amber-500">{openTickets}</div>
            <div className="text-[10px] text-gray-500 mt-1">Requires triage / contractor assignment</div>
            <Wrench className="absolute right-4 bottom-4 h-12 w-12 text-gray-800 opacity-20" />
          </div>
        </div>

        {/* Tab Controls & Actions */}
        <div className="flex flex-wrap items-center justify-between border-b border-gray-800 pb-px gap-4">
          <div className="flex gap-4">
            <button 
              onClick={() => setActiveTab('properties')}
              className={`py-3 text-sm font-medium border-b-2 transition-all ${
                activeTab === 'properties' ? 'border-blue-500 text-white' : 'border-transparent text-gray-400 hover:text-white'
              }`}
            >
              Properties & Units
            </button>
            <button 
              onClick={() => setActiveTab('maintenance')}
              className={`py-3 text-sm font-medium border-b-2 transition-all ${
                activeTab === 'maintenance' ? 'border-blue-500 text-white' : 'border-transparent text-gray-400 hover:text-white'
              }`}
            >
              Maintenance Feed
            </button>
            <button 
              onClick={() => setActiveTab('payments')}
              className={`py-3 text-sm font-medium border-b-2 transition-all ${
                activeTab === 'payments' ? 'border-blue-500 text-white' : 'border-transparent text-gray-400 hover:text-white'
              }`}
            >
              Transactions
            </button>
          </div>

          <button 
            onClick={() => setShowAddProp(true)}
            className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold text-xs rounded-lg transition-colors"
          >
            <Plus className="h-4 w-4" />
            Add Property
          </button>
        </div>

        {/* Add Property Form Overlay */}
        {showAddProp && (
          <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50 backdrop-blur-sm">
            <div className="bg-gray-900 border border-gray-800 rounded-xl w-full max-w-md p-6 relative">
              <h3 className="text-lg font-bold text-white mb-4">Register New Property</h3>
              <form onSubmit={handleAddProperty} className="space-y-4">
                <div>
                  <label className="block text-xs font-semibold text-gray-400 mb-1">Street Address</label>
                  <input 
                    type="text" 
                    value={address} 
                    onChange={e => setAddress(e.target.value)} 
                    className="w-full bg-gray-950 border border-gray-800 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500" 
                    placeholder="123 Charlotte Dr"
                    required
                  />
                </div>
                <div className="grid grid-cols-3 gap-2">
                  <div className="col-span-2">
                    <label className="block text-xs font-semibold text-gray-400 mb-1">City</label>
                    <input 
                      type="text" 
                      value={city} 
                      onChange={e => setCity(e.target.value)} 
                      className="w-full bg-gray-950 border border-gray-800 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500" 
                      placeholder="Charlotte"
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-gray-400 mb-1">State</label>
                    <input 
                      type="text" 
                      value={stateForm} 
                      onChange={e => setStateForm(e.target.value)} 
                      className="w-full bg-gray-950 border border-gray-800 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500" 
                      placeholder="NC"
                      required
                    />
                  </div>
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-400 mb-1">ZIP Code</label>
                  <input 
                    type="text" 
                    value={zipCode} 
                    onChange={e => setZipCode(e.target.value)} 
                    className="w-full bg-gray-950 border border-gray-800 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500" 
                    placeholder="28202"
                    required
                  />
                </div>
                <div className="grid grid-cols-2 gap-3">
                  <div>
                    <label className="block text-xs font-semibold text-gray-400 mb-1">Number of Units</label>
                    <input 
                      type="number" 
                      min="1"
                      value={unitsCount} 
                      onChange={e => setUnitsCount(Number(e.target.value))} 
                      className="w-full bg-gray-950 border border-gray-800 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500"
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-gray-400 mb-1">Rent per Unit ($)</label>
                    <input 
                      type="number" 
                      min="1"
                      value={rentPerUnit} 
                      onChange={e => setRentPerUnit(Number(e.target.value))} 
                      className="w-full bg-gray-950 border border-gray-800 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500"
                    />
                  </div>
                </div>
                <div className="flex gap-2 justify-end mt-6">
                  <button 
                    type="button" 
                    onClick={() => setShowAddProp(false)} 
                    className="px-4 py-2 border border-gray-800 rounded-lg text-xs font-semibold hover:bg-gray-800 transition-colors"
                  >
                    Cancel
                  </button>
                  <button 
                    type="submit" 
                    disabled={formLoading}
                    className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-colors"
                  >
                    {formLoading && <Loader2 className="animate-spin h-3.5 w-3.5" />}
                    Confirm Registry
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}

        {/* Tab Sections */}
        {activeTab === 'properties' && (
          <div className="space-y-4">
            {properties.length === 0 ? (
              <div className="bg-gray-900 border border-gray-800 rounded-xl p-12 text-center">
                <Building className="h-12 w-12 text-gray-600 mx-auto mb-3" />
                <h4 className="text-base font-bold text-white">No properties registered</h4>
                <p className="text-xs text-gray-400 mt-1 max-w-sm mx-auto">Add your first property asset to configure lease agreements and collect rent.</p>
              </div>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {properties.map(prop => (
                  <div key={prop.id} className="bg-gray-900 border border-gray-800 rounded-xl p-5 hover:border-gray-700 transition-all flex flex-col justify-between">
                    <div>
                      <div className="flex items-start justify-between">
                        <div className="flex items-center gap-2.5">
                          <div className="h-8 w-8 rounded bg-gray-800 flex items-center justify-center text-sm">🏢</div>
                          <div>
                            <h4 className="font-bold text-white text-sm">{prop.address}</h4>
                            <p className="text-[10px] text-gray-400 flex items-center gap-1 mt-0.5">
                              <MapPin className="h-3 w-3" /> {prop.city}, {prop.state} {prop.zip_code}
                            </p>
                          </div>
                        </div>
                        <span className="text-[10px] bg-blue-900/50 text-blue-400 px-2 py-0.5 rounded border border-blue-800 font-semibold uppercase">
                          {prop.units_count} Units
                        </span>
                      </div>

                      {/* Units display list */}
                      <div className="mt-4 pt-4 border-t border-gray-800 space-y-2">
                        <div className="text-[10px] text-gray-400 uppercase font-semibold">Units Status</div>
                        {prop.units && prop.units.map(unit => (
                          <div key={unit.id} className="flex items-center justify-between text-xs py-1.5 border-b border-gray-800/40 last:border-0">
                            <span className="font-medium text-gray-300">Unit {unit.unit_number}</span>
                            <div className="flex items-center gap-3">
                              <span className="text-gray-400">${Number(unit.rent_amount).toLocaleString()}/mo</span>
                              {unit.tenant_id ? (
                                <span className="bg-emerald-950/50 text-emerald-400 text-[10px] px-2 py-0.5 rounded border border-emerald-800 font-medium">
                                  Occupied
                                </span>
                              ) : (
                                <span className="bg-gray-800 text-gray-400 text-[10px] px-2 py-0.5 rounded border border-gray-700 font-medium">
                                  Vacant
                                </span>
                              )}
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {activeTab === 'maintenance' && (
          <div className="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden">
            <div className="px-6 py-4 border-b border-gray-800">
              <h3 className="font-bold text-white text-sm">Maintenance Triage Queue</h3>
            </div>
            {maintenance.length === 0 ? (
              <div className="p-12 text-center text-gray-400">
                <Wrench className="h-12 w-12 text-gray-700 mx-auto mb-3" />
                <p className="text-xs">No active maintenance requests submitted.</p>
              </div>
            ) : (
              <div className="divide-y divide-gray-800">
                {maintenance.map(req => (
                  <div key={req.id} className="p-6 flex flex-wrap items-start justify-between gap-4">
                    <div className="space-y-1 max-w-xl">
                      <div className="flex items-center gap-2">
                        <span className={`text-[10px] px-2 py-0.5 rounded font-bold uppercase ${
                          req.status === 'completed' 
                            ? 'bg-emerald-950/40 text-emerald-400 border border-emerald-800' 
                            : req.status === 'in_progress' 
                            ? 'bg-blue-950/40 text-blue-400 border border-blue-800'
                            : 'bg-amber-950/40 text-amber-500 border border-amber-800'
                        }`}>
                          {req.status.replace('_', ' ')}
                        </span>
                        <span className="text-[10px] text-gray-500">Submitted: {new Date(req.created_at).toLocaleDateString()}</span>
                      </div>
                      <p className="text-sm text-gray-200 mt-1">{req.description}</p>
                    </div>

                    <div className="flex gap-2">
                      {req.status === 'open' && (
                        <button 
                          onClick={() => handleUpdateMaintenanceStatus(req.id, 'in_progress')}
                          className="px-3 py-1.5 bg-blue-600 hover:bg-blue-700 text-white rounded text-xs font-semibold transition-colors"
                        >
                          Start Work
                        </button>
                      )}
                      {req.status === 'in_progress' && (
                        <button 
                          onClick={() => handleUpdateMaintenanceStatus(req.id, 'completed')}
                          className="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded text-xs font-semibold transition-colors"
                        >
                          Mark Resolved
                        </button>
                      )}
                      {req.status === 'completed' && (
                        <span className="text-xs text-gray-500 flex items-center gap-1.5">
                          <CheckCircle className="h-4 w-4 text-emerald-500" /> Done
                        </span>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {activeTab === 'payments' && (
          <div className="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden">
            <div className="px-6 py-4 border-b border-gray-800">
              <h3 className="font-bold text-white text-sm">Rent Transactions</h3>
            </div>
            {payments.length === 0 ? (
              <div className="p-12 text-center text-gray-400">
                <CreditCard className="h-12 w-12 text-gray-700 mx-auto mb-3" />
                <p className="text-xs">No transactions recorded.</p>
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
      </main>
    </div>
  );
}
