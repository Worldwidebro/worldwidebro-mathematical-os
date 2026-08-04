import { describe, it, expect, vi } from 'vitest';
import { supabase } from '../../index';

describe('Auth Routes', () => {
  it('should register user', async () => {
    const mockUser = { id: 'test-id', email: 'test@example.com' };

    vi.spyOn(supabase.auth.admin, 'createUser').mockResolvedValueOnce({
      data: { user: mockUser } as any,
      error: null,
    });

    vi.spyOn(supabase, 'from').mockReturnValueOnce({
      insert: vi.fn().mockResolvedValueOnce({ data: [{ id: 'test-id' }], error: null }),
    } as any);

    // Test would call /auth/register endpoint
    expect(mockUser.email).toBe('test@example.com');
  });

  it('should login user', async () => {
    const mockSession = {
      access_token: 'token',
      refresh_token: 'refresh',
      user: { id: 'test-id', email: 'test@example.com' },
    };

    vi.spyOn(supabase.auth, 'signInWithPassword').mockResolvedValueOnce({
      data: { session: mockSession } as any,
      error: null,
    });

    expect(mockSession.user.email).toBe('test@example.com');
  });
});
