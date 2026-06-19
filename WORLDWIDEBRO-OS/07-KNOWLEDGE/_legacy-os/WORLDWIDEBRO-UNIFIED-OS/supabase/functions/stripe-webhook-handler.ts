import Stripe from 'https://esm.sh/stripe@13.0.0';
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2.38.4';

const stripe = new Stripe(Deno.env.get('STRIPE_SECRET_KEY')!);
const supabase = createClient(
  Deno.env.get('SUPABASE_URL')!,
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
);

export async function handleStripeWebhook(
  request: Request
): Promise<Response> {
  const signature = request.headers.get('stripe-signature');
  const body = await request.text();

  try {
    const event = stripe.webhooks.constructEvent(
      body,
      signature!,
      Deno.env.get('STRIPE_WEBHOOK_SECRET')!
    );

    console.log(`Processing Stripe event: ${event.type}`);

    switch (event.type) {
      case 'payment_intent.succeeded': {
        const paymentIntent = event.data.object as Stripe.PaymentIntent;

        const { error } = await supabase.from('spending_transaction').insert({
          id: paymentIntent.id,
          date: new Date(paymentIntent.created * 1000),
          amount: paymentIntent.amount / 100,
          currency: paymentIntent.currency,
          customer_id: paymentIntent.customer,
          status: 'completed',
          description: paymentIntent.description,
          stripe_metadata: paymentIntent.metadata,
          created_at: new Date(),
        });

        if (error) throw error;
        console.log(
          `✅ Payment recorded: ${paymentIntent.currency.toUpperCase()} ${paymentIntent.amount / 100}`
        );
        break;
      }

      case 'customer.subscription.created': {
        const subscription = event.data.object as Stripe.Subscription;
        const priceAmount =
          (subscription.items.data[0]?.price?.unit_amount || 0) / 100;

        const { error } = await supabase.from('spending_transaction').insert({
          id: subscription.id,
          date: new Date(subscription.created * 1000),
          amount: priceAmount,
          currency: subscription.currency,
          customer_id: subscription.customer as string,
          status: 'active',
          type: 'subscription',
          stripe_metadata: {
            billing_cycle_anchor: subscription.billing_cycle_anchor,
            interval: subscription.items.data[0]?.price?.recurring?.interval,
          },
          created_at: new Date(),
        });

        if (error) throw error;
        console.log(
          `✅ Subscription created: ${subscription.currency.toUpperCase()} ${priceAmount}/mo`
        );
        break;
      }

      case 'customer.subscription.deleted': {
        const subscription = event.data.object as Stripe.Subscription;

        const { error } = await supabase
          .from('spending_transaction')
          .update({ status: 'cancelled' })
          .eq('id', subscription.id);

        if (error) throw error;
        console.log(`✅ Subscription cancelled: ${subscription.id}`);
        break;
      }

      case 'invoice.paid': {
        const invoice = event.data.object as Stripe.Invoice;

        const { error } = await supabase.from('spending_transaction').insert({
          id: invoice.id,
          date: new Date(invoice.created * 1000),
          amount: invoice.total / 100,
          currency: invoice.currency,
          customer_id: invoice.customer as string,
          status: 'paid',
          type: 'invoice',
          description: `Invoice #${invoice.number}`,
          created_at: new Date(),
        });

        if (error) throw error;
        console.log(`✅ Invoice paid: ${invoice.currency.toUpperCase()} ${invoice.total / 100}`);
        break;
      }
    }

    return new Response(JSON.stringify({ received: true }), {
      headers: { 'Content-Type': 'application/json' },
      status: 200,
    });
  } catch (error) {
    console.error('Webhook error:', error);
    return new Response(
      JSON.stringify({
        error: error instanceof Error ? error.message : 'Unknown error',
      }),
      { headers: { 'Content-Type': 'application/json' }, status: 400 }
    );
  }
}

Deno.serve(handleStripeWebhook);
