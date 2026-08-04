'use client';

import { useCallback, useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { supabase } from '@/lib/supabase-client';
import { api } from '@/lib/api';
import type { User, UserRole } from '@realestate-os/shared-types';

interface AuthState {
  user: User | null;
  role: UserRole | null;
  isLoading: boolean;
  isAuthenticated: boolean;
  error: string | null;
}
const mapUser = (supabaseUser: any): User => ({
  id: supabaseUser.id,
  email: supabaseUser.email || '',
  fullName: supabaseUser.user_metadata?.full_name || '',
  role: supabaseUser.user_metadata?.role || 'landlord',
  createdAt: supabaseUser.created_at,
  updatedAt: supabaseUser.updated_at || supabaseUser.created_at,
});

export function useAuth() {
  const router = useRouter();
  const [state, setState] = useState<AuthState>({
    user: null,
    role: null,
    isLoading: true,
    isAuthenticated: false,
    error: null,
  });

  // Check auth on mount
  useEffect(() => {
    const checkAuth = async () => {
      try {
        const {
          data: { session },
        } = await supabase.auth.getSession();

        if (session?.access_token) {
          api.setAccessToken(session.access_token);
          api.setUserId(session.user.id);
          setState((prev) => ({
            ...prev,
            isAuthenticated: true,
            user: mapUser(session.user),
            role: session.user?.user_metadata?.role || null,
            isLoading: false,
          }));
        } else {
          setState((prev) => ({
            ...prev,
            isLoading: false,
          }));
        }
      } catch (err) {
        setState((prev) => ({
          ...prev,
          isLoading: false,
          error: err instanceof Error ? err.message : 'Failed to check auth',
        }));
      }
    };

    checkAuth();

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange(async (event, session) => {
      if (session?.access_token) {
        api.setAccessToken(session.access_token);
        api.setUserId(session.user.id);
        setState((prev) => ({
          ...prev,
          isAuthenticated: true,
          user: mapUser(session.user),
          role: session.user?.user_metadata?.role || null,
        }));
      } else {
        api.setAccessToken(null);
        setState((prev) => ({
          ...prev,
          user: null,
          role: null,
          isAuthenticated: false,
        }));
      }
    });

    return () => {
      subscription?.unsubscribe();
    };
  }, []);

  const login = useCallback(
    async (email: string, password: string) => {
      setState((prev) => ({ ...prev, isLoading: true, error: null }));
      try {
        const { data, error } = await supabase.auth.signInWithPassword({
          email,
          password,
        });

        if (error) throw error;

        setState((prev) => ({
          ...prev,
          isLoading: false,
          isAuthenticated: true,
          user: mapUser(data.user),
          role: data.user?.user_metadata?.role || null,
        }));
        return data.user?.user_metadata?.role || 'landlord';
      } catch (err) {
        const errorMessage = err instanceof Error ? err.message : 'Login failed';
        setState((prev) => ({
          ...prev,
          isLoading: false,
          error: errorMessage,
        }));
        return false;
      }
    },
    []
  );

  const register = useCallback(
    async (email: string, password: string, fullName: string, role: UserRole) => {
      setState((prev) => ({ ...prev, isLoading: true, error: null }));
      try {
        const { error: signUpError } = await supabase.auth.signUp({
          email,
          password,
          options: {
            data: {
              full_name: fullName,
              role,
            },
          },
        });

        if (signUpError) throw signUpError;

        setState((prev) => ({
          ...prev,
          isLoading: false,
        }));
        return true;
      } catch (err) {
        const errorMessage = err instanceof Error ? err.message : 'Registration failed';
        setState((prev) => ({
          ...prev,
          isLoading: false,
          error: errorMessage,
        }));
        return false;
      }
    },
    []
  );

  const logout = useCallback(async () => {
    setState((prev) => ({ ...prev, isLoading: true, error: null }));
    try {
      await supabase.auth.signOut();
      api.setAccessToken(null);
      api.setUserId(null);
      setState({
        user: null,
        role: null,
        isLoading: false,
        isAuthenticated: false,
        error: null,
      });
      router.push('/');
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Logout failed';
      setState((prev) => ({
        ...prev,
        isLoading: false,
        error: errorMessage,
      }));
    }
  }, [router]);

  return {
    ...state,
    login,
    register,
    logout,
  };
}
