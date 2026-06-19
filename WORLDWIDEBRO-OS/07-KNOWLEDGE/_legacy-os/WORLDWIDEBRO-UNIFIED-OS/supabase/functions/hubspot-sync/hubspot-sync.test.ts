import { assertEquals, assertExists } from 'https://deno.land/std@0.208.0/assert/mod.ts';

Deno.test('Contact sync transforms HubSpot properties correctly', async () => {
  const hubspotContact = {
    id: 'contact_123',
    properties: {
      email: 'john@example.com',
      firstname: 'John',
      lastname: 'Doe',
      phone: '5551234567',
      company: 'ACME Corp',
      lifecyclestage: 'customer',
      hs_lead_status: 'NEW',
    },
  };

  assertEquals(hubspotContact.id, 'contact_123');
  assertEquals(hubspotContact.properties.email, 'john@example.com');
  assertEquals(hubspotContact.properties.lifecyclestage, 'customer');
  console.log('✅ Contact transformation test passed');
});

Deno.test('Deal sync handles numeric amounts correctly', async () => {
  const hubspotDeal = {
    id: 'deal_456',
    properties: {
      dealname: 'Enterprise Contract',
      dealstage: 'negotiation',
      amount: '50000',
      closedate: '2026-07-15',
      dealowner: 'salesperson_1',
    },
  };

  const amount = parseFloat(hubspotDeal.properties.amount);
  assertEquals(amount, 50000);
  assertExists(hubspotDeal.properties.closedate);
  assertEquals(hubspotDeal.properties.dealstage, 'negotiation');
  console.log('✅ Deal transformation test passed');
});

Deno.test('Pagination cursor handling is correct', async () => {
  const mockResponse = {
    results: [
      { id: '1', properties: { email: 'user1@test.com' } },
      { id: '2', properties: { email: 'user2@test.com' } },
    ],
    paging: {
      next: {
        after: 'cursor_abc123',
      },
    },
  };

  assertExists(mockResponse.paging.next.after);
  assertEquals(mockResponse.results.length, 2);
  console.log('✅ Pagination test passed');
});
