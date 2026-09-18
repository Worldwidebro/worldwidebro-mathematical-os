/**
 * Jest Setup File for Services Tests
 * Initializes test environment and mocks
 */

// Mock environment variables
process.env.SUPABASE_URL = 'https://aipehhzlsmfxxzwceppd.supabase.co';
process.env.SUPABASE_ANON_KEY = 'test_anon_key_mock_12345';

// Suppress console output during tests (comment out to debug)
// const originalLog = console.log;
// const originalWarn = console.warn;
// const originalError = console.error;

// beforeAll(() => {
//   console.log = jest.fn();
//   console.warn = jest.fn();
//   console.error = jest.fn();
// });

// afterAll(() => {
//   console.log = originalLog;
//   console.warn = originalWarn;
//   console.error = originalError;
// });

// Global test utilities
global.testUtils = {
  sleep: (ms: number) => new Promise(resolve => setTimeout(resolve, ms)),
  randomId: () => Math.random().toString(36).substring(2, 11),
  randomVenture: () => `TEST-${Math.random().toString(36).substring(2, 8).toUpperCase()}`,
};

declare global {
  var testUtils: {
    sleep: (ms: number) => Promise<void>;
    randomId: () => string;
    randomVenture: () => string;
  };
}

export {};
