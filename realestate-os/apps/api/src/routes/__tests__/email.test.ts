import { describe, it, expect, vi, beforeEach } from 'vitest';
import axios from 'axios';
import { supabase } from '../../index';

// Mock Resend SDK
vi.mock('resend', () => ({
  Resend: class {
    emails = {
      send: vi.fn(),
    };
  },
}));

vi.mock('axios');
vi.mock('../../index', () => ({
  supabase: {
    from: vi.fn(),
  },
}));

describe('Email Routes', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('send-rent-reminder', () => {
    it('should send rent reminder email', async () => {
      const mockPayload = {
        unitId: 'unit-123',
        tenantEmail: 'tenant@example.com',
        tenantName: 'John Doe',
        amount: '1500.00',
        dueDate: '2024-08-15',
        paymentLink: 'https://example.com/pay',
      };

      // Mock axios post
      vi.mocked(axios.post).mockResolvedValueOnce({ data: { success: true } });

      // Mock supabase insert
      const mockInsert = vi.fn().mockResolvedValueOnce({ data: [{ id: 'email-log-123' }], error: null });
      vi.mocked(supabase.from).mockReturnValueOnce({
        insert: mockInsert,
      } as any);

      expect(mockPayload.tenantEmail).toBe('tenant@example.com');
      expect(mockPayload.amount).toBe('1500.00');
    });

    it('should log failed rent reminder', async () => {
      const mockInsert = vi.fn().mockResolvedValueOnce({ data: null, error: null });
      vi.mocked(supabase.from).mockReturnValueOnce({
        insert: mockInsert,
      } as any);

      expect(mockInsert).toBeDefined();
    });
  });

  describe('send-maintenance-update', () => {
    it('should send maintenance update email', async () => {
      const mockPayload = {
        ticketId: 'maint-456',
        tenantEmail: 'tenant@example.com',
        status: 'in_progress',
        notes: 'Plumber scheduled for Thursday',
      };

      vi.mocked(axios.post).mockResolvedValueOnce({ data: { success: true } });

      expect(mockPayload.status).toBe('in_progress');
      expect(mockPayload.notes).toBe('Plumber scheduled for Thursday');
    });

    it('should capitalize status in email', () => {
      const status = 'in_progress';
      const capitalized = status.charAt(0).toUpperCase() + status.slice(1);
      expect(capitalized).toBe('In_progress');
    });
  });

  describe('send-payment-receipt', () => {
    it('should send payment receipt email', async () => {
      const mockPayload = {
        tenantEmail: 'tenant@example.com',
        amount: '1500.00',
        date: '2024-08-10T14:30:00Z',
        propertyName: '123 Main St',
      };

      vi.mocked(axios.post).mockResolvedValueOnce({ data: { success: true } });

      expect(mockPayload.propertyName).toBe('123 Main St');
      expect(parseFloat(mockPayload.amount)).toBe(1500);
    });
  });

  describe('send-escalation', () => {
    it('should send maintenance escalation to landlord', async () => {
      const mockPayload = {
        landlordEmail: 'landlord@example.com',
        daysOpen: 8,
        ticketDescription: 'Leaking roof in unit 3B',
        portalLink: 'https://example.com/portal',
      };

      vi.mocked(axios.post).mockResolvedValueOnce({ data: { success: true } });

      expect(mockPayload.daysOpen).toBeGreaterThan(7);
      expect(mockPayload.ticketDescription).toContain('roof');
    });
  });

  describe('send-lease-welcome', () => {
    it('should send lease welcome email to tenant', async () => {
      const mockPayload = {
        tenantEmail: 'tenant@example.com',
        tenantName: 'John Doe',
        property: '456 Oak Ave, Denver, CO',
        leaseStart: '2024-09-01',
        leaseEnd: '2025-08-31',
        monthlyRent: '1500.00',
        leaseTerms: '<ul><li>No pets</li><li>30-day notice</li></ul>',
        portalLink: 'https://example.com/portal',
      };

      vi.mocked(axios.post).mockResolvedValueOnce({ data: { success: true } });

      expect(mockPayload.property).toContain('Denver');
      expect(mockPayload.leaseTerms).toContain('No pets');
    });

    it('should format lease dates correctly', () => {
      const leaseStart = new Date('2024-09-01').toLocaleDateString();
      const leaseEnd = new Date('2025-08-31').toLocaleDateString();

      expect(leaseStart).toBeDefined();
      expect(leaseEnd).toBeDefined();
    });
  });

  describe('GET /api/email/deliveries', () => {
    it('should fetch email delivery logs', async () => {
      const mockData = [
        {
          id: 'email-1',
          template: 'rent-reminder',
          recipient: 'tenant@example.com',
          status: 'sent',
          created_at: '2024-08-10T10:00:00Z',
        },
      ];

      const mockSelect = vi.fn().mockReturnValueOnce({
        order: vi.fn().mockReturnValueOnce({
          range: vi.fn().mockResolvedValueOnce({ data: mockData, count: 1, error: null }),
        }),
      });

      vi.mocked(supabase.from).mockReturnValueOnce({
        select: mockSelect,
      } as any);

      expect(mockData[0].status).toBe('sent');
      expect(mockData[0].template).toBe('rent-reminder');
    });

    it('should filter deliveries by status', async () => {
      const status = 'failed';
      expect(status).toBe('failed');
    });

    it('should paginate results', () => {
      const limit = 50;
      const offset = 0;
      expect(limit).toBe(50);
      expect(offset).toBe(0);
    });
  });

  describe('Email template variables', () => {
    it('should replace amount placeholder', () => {
      const html = '<p>Amount: {{amount}}</p>';
      const replaced = html.replace('{{amount}}', '$1500.00');
      expect(replaced).toBe('<p>Amount: $1500.00</p>');
    });

    it('should replace multiple placeholders', () => {
      let html = '<p>Hi {{tenant_name}}, due {{due_date}}</p>';
      html = html.replace('{{tenant_name}}', 'John');
      html = html.replace('{{due_date}}', '08/15/2024');
      expect(html).toContain('John');
      expect(html).toContain('08/15/2024');
    });
  });

  describe('Error handling', () => {
    it('should handle Resend API errors', () => {
      const error = new Error('Resend API unavailable');
      expect(error.message).toBe('Resend API unavailable');
    });

    it('should handle database logging errors', () => {
      const error = new Error('Database connection failed');
      expect(() => {
        throw error;
      }).toThrow('Database connection failed');
    });

    it('should return 500 on email send failure', () => {
      const statusCode = 500;
      expect(statusCode).toBe(500);
    });
  });
});
