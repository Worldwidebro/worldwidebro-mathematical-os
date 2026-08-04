'use client';

import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { useAuth } from '@/hooks/useAuth';
import { Button } from '@/components/ui/button';
import { Building2, LogOut, Menu } from 'lucide-react';
import { useState } from 'react';

export function Nav() {
  const { isAuthenticated, role, logout, isLoading } = useAuth();
  const router = useRouter();
  const [isOpen, setIsOpen] = useState(false);

  const handleLogout = async () => {
    await logout();
    router.push('/');
  };

  if (!isAuthenticated || isLoading) {
    return null;
  }

  return (
    <nav className="sticky top-0 z-40 border-b bg-white shadow-sm">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          <Link href="/" className="flex items-center gap-2">
            <Building2 className="h-8 w-8 text-blue-600" />
            <span className="text-xl font-bold text-gray-900">RE-OS</span>
          </Link>

          <div className="hidden items-center gap-4 md:flex">
            {role === 'landlord' && (
              <>
                <Link href="/landlord/dashboard" className="text-gray-700 hover:text-gray-900">
                  Dashboard
                </Link>
              </>
            )}
            {role === 'tenant' && (
              <>
                <Link href="/tenant/portal" className="text-gray-700 hover:text-gray-900">
                  Portal
                </Link>
                <Link href="/tenant/portal/maintenance" className="text-gray-700 hover:text-gray-900">
                  Maintenance
                </Link>
              </>
            )}
            <Button
              variant="ghost"
              size="sm"
              onClick={handleLogout}
              className="flex items-center gap-2"
            >
              <LogOut className="h-4 w-4" />
              Logout
            </Button>
          </div>

          <button
            className="md:hidden"
            onClick={() => setIsOpen(!isOpen)}
            aria-label="Toggle menu"
          >
            <Menu className="h-6 w-6" />
          </button>
        </div>

        {isOpen && (
          <div className="border-t py-4 md:hidden">
            {role === 'landlord' && (
              <>
                <Link
                  href="/landlord/dashboard"
                  className="block py-2 text-gray-700 hover:text-gray-900"
                >
                  Dashboard
                </Link>
              </>
            )}
            {role === 'tenant' && (
              <>
                <Link href="/tenant/portal" className="block py-2 text-gray-700 hover:text-gray-900">
                  Portal
                </Link>
                <Link
                  href="/tenant/portal/maintenance"
                  className="block py-2 text-gray-700 hover:text-gray-900"
                >
                  Maintenance
                </Link>
              </>
            )}
            <button
              onClick={handleLogout}
              className="mt-4 w-full rounded-md bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
            >
              Logout
            </button>
          </div>
        )}
      </div>
    </nav>
  );
}
