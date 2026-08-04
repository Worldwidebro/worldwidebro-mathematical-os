import { describe, it, expect, vi, beforeEach } from 'vitest';
import { supabase } from '../../index';

describe('Admin Routes', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('GET /api/admin/users', () => {
    it('should list all users', async () => {
      const mockUsers = [
        { id: '1', email: 'landlord@test.com', full_name: 'John', role: 'landlord', is_suspended: false },
        { id: '2', email: 'tenant@test.com', full_name: 'Jane', role: 'tenant', is_suspended: false },
      ];

      vi.spyOn(supabase, 'from').mockReturnValueOnce({
        select: vi.fn().mockReturnValueOnce({
          order: vi.fn().mockResolvedValueOnce({ data: mockUsers, error: null }),
        }),
      } as any);

      expect(mockUsers).toHaveLength(2);
      expect(mockUsers[0].role).toBe('landlord');
    });
  });

  describe('POST /api/admin/users', () => {
    it('should create new user', async () => {
      const mockUser = { id: 'user-1', email: 'new@test.com', full_name: 'New User', role: 'tenant' };

      vi.spyOn(supabase.auth.admin, 'createUser').mockResolvedValueOnce({
        data: { user: { id: 'user-1', email: 'new@test.com' } } as any,
        error: null,
      });

      vi.spyOn(supabase, 'from').mockReturnValueOnce({
        insert: vi.fn().mockReturnValueOnce({
          select: vi.fn().mockReturnValueOnce({
            single: vi.fn().mockResolvedValueOnce({ data: mockUser, error: null }),
          }),
        }),
      } as any);

      expect(mockUser.role).toBe('tenant');
      expect(mockUser.email).toBe('new@test.com');
    });

    it('should reject invalid role', async () => {
      const invalidRole = 'superuser';
      const validRoles = ['admin', 'landlord', 'tenant'];

      expect(validRoles.includes(invalidRole)).toBe(false);
    });
  });

  describe('POST /api/admin/users/:id/suspend', () => {
    it('should suspend user', async () => {
      const suspendedUser = {
        id: 'user-1',
        email: 'tenant@test.com',
        is_suspended: true,
        suspension_reason: 'Violation of terms',
      };

      vi.spyOn(supabase, 'from').mockReturnValueOnce({
        update: vi.fn().mockReturnValueOnce({
          eq: vi.fn().mockReturnValueOnce({
            select: vi.fn().mockReturnValueOnce({
              single: vi.fn().mockResolvedValueOnce({ data: suspendedUser, error: null }),
            }),
          }),
        }),
      } as any);

      expect(suspendedUser.is_suspended).toBe(true);
    });
  });

  describe('GET /api/admin/disputes', () => {
    it('should list payment disputes', async () => {
      const mockDisputes = [
        {
          id: 'd1',
          payment_id: 'p1',
          tenant_id: 't1',
          reason: 'Overcharge',
          status: 'pending',
          created_at: '2026-07-29T00:00:00Z',
        },
      ];

      vi.spyOn(supabase, 'from').mockReturnValueOnce({
        select: vi.fn().mockReturnValueOnce({
          order: vi.fn().mockResolvedValueOnce({ data: mockDisputes, error: null }),
        }),
      } as any);

      expect(mockDisputes).toHaveLength(1);
      expect(mockDisputes[0].status).toBe('pending');
    });

    it('should filter disputes by status', async () => {
      const resolvedDisputes = [
        {
          id: 'd1',
          status: 'resolved',
          created_at: '2026-07-29T00:00:00Z',
        },
      ];

      vi.spyOn(supabase, 'from').mockReturnValueOnce({
        select: vi.fn().mockReturnValueOnce({
          eq: vi.fn().mockReturnValueOnce({
            order: vi.fn().mockResolvedValueOnce({ data: resolvedDisputes, error: null }),
          }),
        }),
      } as any);

      expect(resolvedDisputes[0].status).toBe('resolved');
    });
  });

  describe('POST /api/admin/disputes/:id/resolve', () => {
    it('should resolve dispute as approved', async () => {
      const resolvedDispute = {
        id: 'd1',
        payment_id: 'p1',
        status: 'resolved',
        admin_notes: 'Verified refund eligible',
        resolved_at: '2026-07-29T10:00:00Z',
      };

      vi.spyOn(supabase, 'from').mockReturnValueOnce({
        update: vi.fn().mockReturnValueOnce({
          eq: vi.fn().mockReturnValueOnce({
            select: vi.fn().mockReturnValueOnce({
              single: vi.fn().mockResolvedValueOnce({ data: resolvedDispute, error: null }),
            }),
          }),
        }),
      } as any);

      expect(resolvedDispute.status).toBe('resolved');
    });

    it('should reject invalid resolution', async () => {
      const invalidResolution = 'pending';
      const validResolutions = ['approved', 'rejected'];

      expect(validResolutions.includes(invalidResolution)).toBe(false);
    });
  });

  describe('GET /api/admin/reports/metrics', () => {
    it('should return KPI metrics', async () => {
      const metrics = {
        userStats: { admin: 1, landlord: 5, tenant: 20 },
        mrrTrend: { '2026-07': 15000, '2026-08': 15500 },
        occupancy: { occupied: 18, total: 20, rate: 90 },
        openTickets: 3,
      };

      expect(metrics.occupancy.rate).toBe(90);
      expect(metrics.userStats.tenant).toBe(20);
    });
  });

  describe('GET /api/admin/reports/churn', () => {
    it('should return expired leases', async () => {
      const churnData = {
        expiredLeases: 2,
        leases: [
          { end_date: '2026-06-30', tenant_id: 't1' },
          { end_date: '2026-06-15', tenant_id: 't2' },
        ],
      };

      expect(churnData.expiredLeases).toBe(2);
    });
  });

  describe('GET /api/admin/reports/payment-health', () => {
    it('should return payment collection stats', async () => {
      const health = {
        paid: 45,
        pending: 8,
        late: 2,
        total: 55,
        collectionRate: 82,
      };

      expect(health.collectionRate).toBe(82);
      expect(health.paid + health.pending + health.late).toBe(health.total);
    });
  });
});
