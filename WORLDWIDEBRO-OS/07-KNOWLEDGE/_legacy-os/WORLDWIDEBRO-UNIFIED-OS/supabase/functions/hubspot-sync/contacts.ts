import { createClient } from 'https://esm.sh/@supabase/supabase-js@2.38.4';

const supabase = createClient(
  Deno.env.get('SUPABASE_URL')!,
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
);

const HUBSPOT_API_KEY = Deno.env.get('HUBSPOT_API_KEY');
const HUBSPOT_BASE_URL = 'https://api.hubapi.com';

interface HubSpotContact {
  id: string;
  properties: {
    email?: string;
    firstname?: string;
    lastname?: string;
    phone?: string;
    company?: string;
    lifecyclestage?: string;
    hs_lead_status?: string;
    [key: string]: any;
  };
}

interface ContactRecord {
  hubspot_id: string;
  email: string | null;
  firstname: string | null;
  lastname: string | null;
  phone: string | null;
  company: string | null;
  lifecyclestage: string | null;
  hs_lead_status: string | null;
  synced_at: string;
}

export async function syncHubSpotContacts(): Promise<Response> {
  try {
    let allContacts: HubSpotContact[] = [];
    let after: string | undefined;

    while (true) {
      const url = new URL(`${HUBSPOT_BASE_URL}/crm/v3/objects/contacts`);
      url.searchParams.append('limit', '100');
      url.searchParams.append(
        'properties',
        'email,firstname,lastname,phone,company,lifecyclestage,hs_lead_status'
      );

      if (after) {
        url.searchParams.append('after', after);
      }

      const response = await fetch(url.toString(), {
        headers: {
          Authorization: `Bearer ${HUBSPOT_API_KEY}`,
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HubSpot API error: ${response.statusText}`);
      }

      const data = await response.json();
      allContacts = allContacts.concat(data.results || []);

      if (!data.paging?.next?.after) {
        break;
      }
      after = data.paging.next.after;
    }

    const contacts: ContactRecord[] = allContacts.map((contact: HubSpotContact) => ({
      hubspot_id: contact.id,
      email: contact.properties.email || null,
      firstname: contact.properties.firstname || null,
      lastname: contact.properties.lastname || null,
      phone: contact.properties.phone || null,
      company: contact.properties.company || null,
      lifecyclestage: contact.properties.lifecyclestage || null,
      hs_lead_status: contact.properties.hs_lead_status || null,
      synced_at: new Date().toISOString(),
    }));

    const { error: upsertError } = await supabase
      .from('hubspot_contacts')
      .upsert(contacts, { onConflict: 'hubspot_id' });

    if (upsertError) throw upsertError;

    console.log(`✅ Synced ${contacts.length} contacts from HubSpot`);

    return new Response(
      JSON.stringify({
        success: true,
        synced_count: contacts.length,
        timestamp: new Date().toISOString(),
      }),
      {
        headers: { 'Content-Type': 'application/json' },
        status: 200,
      }
    );
  } catch (error) {
    console.error('HubSpot contact sync error:', error);
    return new Response(
      JSON.stringify({
        error: error instanceof Error ? error.message : 'Unknown error',
      }),
      { headers: { 'Content-Type': 'application/json' }, status: 500 }
    );
  }
}

Deno.serve(syncHubSpotContacts);
