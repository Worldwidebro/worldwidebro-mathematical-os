'use client';

import { useEffect, useState } from 'react';
import { useAuth } from '@/hooks/useAuth';
import { Plus, Loader2, Shield, Home, Users, AlertCircle, LogOut, Trash2, CheckCircle } from 'lucide-react';
import Link from 'next/link';

interface User {
  id: string;
  email: string;
  full_name: string;
  role: 'admin' | 'landlord' | 'tenant';
  phone: string | null;
  is_suspended: boolean;
  suspension_reason: string | null;
  created_at: string;
}

export default function UserManagementPage() {
  const { logout, isLoading: authLoading } = useAuth();
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [formLoading, setFormLoading] = useState(false);

  // Form state
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [role, setRole] = useState<'admin' | 'landlord' | 'tenant'>('tenant');

  const fetchUsers = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch('/api/admin/users');
      if (!res.ok) throw new Error('Failed to load users');
      const data = await res.json();
      setUsers(data || []);
    } catch (err: any) {
      setError(err.message || 'Error loading users');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleCreateUser = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || !password || !fullName) {
      alert('All fields required');
      return;
    }

    setFormLoading(true);
    try {
      const res = await fetch('/api/admin/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          password,
          fullName,
          role,
        }),
      });

      if (!res.ok) throw new Error('Failed to create user');

      // Reset form
      setEmail('');
      setPassword('');
      setFullName('');
      setRole('tenant');
      setShowCreateForm(false);

      // Refresh list
      await fetchUsers();
    } catch (err: any) {
      alert(err.message || 'Error creating user');
    } finally {
      setFormLoading(false);
    }
  };

  const handleSuspendUser = async (userId: string, reason: string) => {
    try {
      const res = await fetch(`/api/admin/users/${userId}/suspend`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ reason }),
      });

      if (!res.ok) throw new Error('Failed to suspend user');

      // Update local state
      setUsers(prev =>
        prev.map(u =>
          u.id === userId
            ? { ...u, is_suspended: true, suspension_reason: reason }
            : u
        )
      );
    } catch (err: any) {
      alert(err.message || 'Error suspending user');
    }
  };

  const handleUnsuspendUser = async (userId: string) => {
    try {
      const res = await fetch(`/api/admin/users/${userId}/unsuspend`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!res.ok) throw new Error('Failed to unsuspend user');

      // Update local state
      setUsers(prev =>
        prev.map(u =>
          u.id === userId
            ? { ...u, is_suspended: false, suspension_reason: null }
            : u
        )
      );
    } catch (err: any) {
      alert(err.message || 'Error unsuspending user');
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

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      {/* Header */}
      <header className="border-b border-gray-800 bg-gray-900 px-6 py-4 flex items-center justify-between">
        <Link href="/admin" className="flex items-center gap-3">
          <div className="h-9 w-9 rounded-lg bg-red-600 flex items-center justify-center font-bold text-white">
            🔐
          </div>
          <div>
            <h1 className="text-lg font-bold text-white tracking-tight">User Management</h1>
            <p className="text-xs text-gray-400">Create, suspend, manage users</p>
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

        {/* Create User Section */}
        <div className="flex justify-between items-center">
          <h2 className="text-sm font-bold text-white">All Users ({users.length})</h2>
          <button
            onClick={() => setShowCreateForm(!showCreateForm)}
            className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold text-xs rounded-lg transition-colors"
          >
            <Plus className="h-4 w-4" />
            Create User
          </button>
        </div>

        {/* Create User Form */}
        {showCreateForm && (
          <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
            <h3 className="text-sm font-bold text-white mb-4">New User</h3>
            <form onSubmit={handleCreateUser} className="space-y-4">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-semibold text-gray-400 mb-1">Full Name</label>
                  <input
                    type="text"
                    value={fullName}
                    onChange={e => setFullName(e.target.value)}
                    className="w-full bg-gray-950 border border-gray-800 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500"
                    placeholder="John Doe"
                    required
                  />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-400 mb-1">Email</label>
                  <input
                    type="email"
                    value={email}
                    onChange={e => setEmail(e.target.value)}
                    className="w-full bg-gray-950 border border-gray-800 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500"
                    placeholder="user@example.com"
                    required
                  />
                </div>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-semibold text-gray-400 mb-1">Password</label>
                  <input
                    type="password"
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                    className="w-full bg-gray-950 border border-gray-800 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500"
                    placeholder="••••••••"
                    required
                  />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-400 mb-1">Role</label>
                  <select
                    value={role}
                    onChange={e => setRole(e.target.value as 'admin' | 'landlord' | 'tenant')}
                    className="w-full bg-gray-950 border border-gray-800 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500"
                  >
                    <option value="tenant">Tenant</option>
                    <option value="landlord">Landlord</option>
                    <option value="admin">Admin</option>
                  </select>
                </div>
              </div>
              <div className="flex gap-2 justify-end pt-2">
                <button
                  type="button"
                  onClick={() => setShowCreateForm(false)}
                  className="px-4 py-2 border border-gray-800 rounded-lg text-xs font-semibold hover:bg-gray-800 transition-colors"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={formLoading}
                  className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-colors disabled:opacity-50"
                >
                  {formLoading && <Loader2 className="animate-spin h-3.5 w-3.5" />}
                  Create
                </button>
              </div>
            </form>
          </div>
        )}

        {/* Users Table */}
        <div className="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden">
          {users.length === 0 ? (
            <div className="p-12 text-center">
              <Users className="h-12 w-12 text-gray-600 mx-auto mb-3" />
              <p className="text-sm text-gray-400">No users yet</p>
            </div>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs border-collapse">
                <thead>
                  <tr className="bg-gray-950 text-gray-400 uppercase tracking-wider font-semibold border-b border-gray-800">
                    <th className="px-6 py-3">Name</th>
                    <th className="px-6 py-3">Email</th>
                    <th className="px-6 py-3">Role</th>
                    <th className="px-6 py-3">Status</th>
                    <th className="px-6 py-3">Created</th>
                    <th className="px-6 py-3">Actions</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-800">
                  {users.map(user => (
                    <tr key={user.id} className="hover:bg-gray-800/40">
                      <td className="px-6 py-4 text-gray-300 font-medium">{user.full_name}</td>
                      <td className="px-6 py-4 text-gray-400">{user.email}</td>
                      <td className="px-6 py-4">
                        <div className="flex items-center gap-1">
                          {user.role === 'admin' && <Shield className="h-3 w-3 text-red-500" />}
                          {user.role === 'landlord' && <Home className="h-3 w-3 text-blue-500" />}
                          {user.role === 'tenant' && <Users className="h-3 w-3 text-green-500" />}
                          <span>{user.role}</span>
                        </div>
                      </td>
                      <td className="px-6 py-4">
                        {user.is_suspended ? (
                          <span className="bg-red-950/40 text-red-400 text-[10px] px-2 py-0.5 rounded border border-red-800 font-medium">
                            Suspended
                          </span>
                        ) : (
                          <span className="bg-emerald-950/40 text-emerald-400 text-[10px] px-2 py-0.5 rounded border border-emerald-800 font-medium flex items-center gap-1 w-fit">
                            <CheckCircle className="h-3 w-3" /> Active
                          </span>
                        )}
                      </td>
                      <td className="px-6 py-4 text-gray-400">
                        {new Date(user.created_at).toLocaleDateString()}
                      </td>
                      <td className="px-6 py-4">
                        <div className="flex gap-2">
                          {user.is_suspended ? (
                            <button
                              onClick={() => handleUnsuspendUser(user.id)}
                              className="px-2 py-1 bg-emerald-600 hover:bg-emerald-700 text-white rounded text-xs font-semibold transition-colors"
                            >
                              Reactivate
                            </button>
                          ) : (
                            <button
                              onClick={() => {
                                const reason = prompt('Suspension reason:');
                                if (reason) handleSuspendUser(user.id, reason);
                              }}
                              className="px-2 py-1 bg-red-600 hover:bg-red-700 text-white rounded text-xs font-semibold transition-colors flex items-center gap-1"
                            >
                              <Trash2 className="h-3 w-3" />
                              Suspend
                            </button>
                          )}
                        </div>
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
