import axios, { AxiosError, AxiosInstance } from 'axios';
import type { ApiResponse } from '@realestate-os/shared-types';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3001';

class ApiClient {
  private client: AxiosInstance;
  private accessToken: string | null = null;

  private userId: string | null = null;

  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    this.client.interceptors.request.use((config) => {
      if (this.accessToken) {
        config.headers.Authorization = `Bearer ${this.accessToken}`;
      }
      if (this.userId) {
        config.headers['x-user-id'] = this.userId;
      }
      return config;
    });

    this.client.interceptors.response.use(
      (response) => response,
      (error) => {
        if (error.response?.status === 401) {
          this.accessToken = null;
          if (typeof window !== 'undefined') {
            window.location.href = '/login';
          }
        }
        return Promise.reject(error);
      }
    );
  }

  setAccessToken(token: string | null) {
    this.accessToken = token;
  }

  setUserId(id: string | null) {
    this.userId = id;
  }

  async get<T>(endpoint: string): Promise<ApiResponse<T>> {
    try {
      const { data } = await this.client.get<T>(endpoint);
      return { data };
    } catch (error) {
      return this.handleError(error);
    }
  }

  async post<T, D = unknown>(endpoint: string, payload: D): Promise<ApiResponse<T>> {
    try {
      const { data } = await this.client.post<T>(endpoint, payload);
      return { data };
    } catch (error) {
      return this.handleError(error);
    }
  }

  async put<T, D = unknown>(endpoint: string, payload: D): Promise<ApiResponse<T>> {
    try {
      const { data } = await this.client.put<T>(endpoint, payload);
      return { data };
    } catch (error) {
      return this.handleError(error);
    }
  }

  async delete<T>(endpoint: string): Promise<ApiResponse<T>> {
    try {
      const { data } = await this.client.delete<T>(endpoint);
      return { data };
    } catch (error) {
      return this.handleError(error);
    }
  }

  private handleError(error: unknown): ApiResponse<never> {
    if (axios.isAxiosError(error)) {
      const axiosError = error as AxiosError<{ error: string }>;
      return {
        error: axiosError.response?.data?.error || axiosError.message || 'An error occurred',
        code: axiosError.response?.status.toString(),
      };
    }
    return { error: 'An unknown error occurred' };
  }
}

export const api = new ApiClient();

// Auth endpoints
export const authApi = {
  register: (email: string, password: string, fullName: string, role: 'landlord' | 'tenant') =>
    api.post<{ userId: string }>('/auth/register', { email, password, fullName, role }),

  login: (email: string, password: string) =>
    api.post<{ accessToken: string; refreshToken: string; user: unknown }>('/auth/login', {
      email,
      password,
    }),
};

// Properties endpoints
export const propertiesApi = {
  list: () => api.get('/properties'),
  get: (id: string) => api.get(`/properties/${id}`),
  create: (data: unknown) => api.post('/properties', data),
  update: (id: string, data: unknown) => api.put(`/properties/${id}`, data),
  delete: (id: string) => api.delete(`/properties/${id}`),
};

// Payments endpoints
export const paymentsApi = {
  list: (params?: { propertyId?: string }) =>
    api.get(`/rent-payments${params?.propertyId ? `?propertyId=${params.propertyId}` : ''}`),
  get: (id: string) => api.get(`/rent-payments/${id}`),
  create: (data: unknown) => api.post('/rent-payments', data),
  refund: (paymentId: string, reason: string) =>
    api.post('/rent-payments/refund', { paymentId, reason }),
  portal: (customerId: string) =>
    api.post('/rent-payments/portal', { customerId }),
  reconciliation: () => api.get('/rent-payments/reconciliation'),
};

// Maintenance endpoints
export const maintenanceApi = {
  list: (params?: { propertyId?: string }) => 
    api.get(`/maintenance${params?.propertyId ? `?propertyId=${params.propertyId}` : ''}`),
  get: (id: string) => api.get(`/maintenance/${id}`),
  create: (data: unknown) => api.post('/maintenance', data),
  update: (id: string, data: unknown) => api.put(`/maintenance/${id}`, data),
};
