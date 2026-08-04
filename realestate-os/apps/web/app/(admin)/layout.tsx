'use client';

import { useAuth } from '@/hooks/useAuth';
import { redirect } from 'next/navigation';

export default function AdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const { user, isLoading } = useAuth();

  if (isLoading) return null;
  if (!user) redirect('/login');

  return <>{children}</>;
}
