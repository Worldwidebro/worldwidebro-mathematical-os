import { WebClient } from 'https://esm.sh/@slack/web-api@6.9.0';

const slack = new WebClient(Deno.env.get('SLACK_BOT_TOKEN'));
const CHANNEL_ID = Deno.env.get('SLACK_CHANNEL_ID');

interface RevenueAlert {
  mrr: number;
  target: number;
  growth_pct: number;
}

interface DealAlert {
  dealName: string;
  score: number;
  operator: string;
  dealValue?: number;
}

interface TaskAlert {
  taskName: string;
  status: string;
  completedBy?: string;
}

export async function notifyRevenueAlert(data: RevenueAlert): Promise<void> {
  const percentOfTarget = ((data.mrr / data.target) * 100).toFixed(1);
  const status =
    data.mrr >= data.target
      ? '✅ *On track!*'
      : data.mrr >= data.target * 0.8
        ? '⚠️ *Getting close*'
        : '🚨 *Below target*';

  await slack.chat.postMessage({
    channel: CHANNEL_ID!,
    blocks: [
      {
        type: 'header',
        text: {
          type: 'plain_text',
          text: '💰 Revenue Update',
        },
      },
      {
        type: 'section',
        fields: [
          {
            type: 'mrkdwn',
            text: `*Current MRR*\n$${data.mrr.toFixed(2)}`,
          },
          {
            type: 'mrkdwn',
            text: `*Target*\n$${data.target.toFixed(2)}`,
          },
          {
            type: 'mrkdwn',
            text: `*Progress*\n${percentOfTarget}%`,
          },
          {
            type: 'mrkdwn',
            text: `*Growth*\n${data.growth_pct > 0 ? '+' : ''}${data.growth_pct.toFixed(1)}%`,
          },
        ],
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: status,
        },
      },
    ],
  });

  console.log(`✅ Revenue alert sent`);
}

export async function notifyDealSourced(data: DealAlert): Promise<void> {
  const scoreEmoji = data.score >= 80 ? '🔥' : data.score >= 60 ? '✨' : '⭐';

  await slack.chat.postMessage({
    channel: CHANNEL_ID!,
    blocks: [
      {
        type: 'header',
        text: {
          type: 'plain_text',
          text: '🎯 New Deal Sourced',
        },
      },
      {
        type: 'section',
        fields: [
          {
            type: 'mrkdwn',
            text: `*Deal*\n${data.dealName}`,
          },
          {
            type: 'mrkdwn',
            text: `*Score*\n${scoreEmoji} ${data.score}/100`,
          },
          {
            type: 'mrkdwn',
            text: `*Operator*\n${data.operator}`,
          },
          {
            type: 'mrkdwn',
            text: data.dealValue
              ? `*Value*\n$${data.dealValue.toFixed(0)}`
              : `*Status*\nQualified`,
          },
        ],
      },
      {
        type: 'actions',
        elements: [
          {
            type: 'button',
            text: {
              type: 'plain_text',
              text: 'Review Deal',
            },
            value: data.dealName,
          },
          {
            type: 'button',
            text: {
              type: 'plain_text',
              text: 'Contact Operator',
            },
            value: data.operator,
          },
        ],
      },
    ],
  });

  console.log(`✅ Deal alert sent: ${data.dealName}`);
}

export async function notifyTaskComplete(data: TaskAlert): Promise<void> {
  await slack.chat.postMessage({
    channel: CHANNEL_ID!,
    blocks: [
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `✅ *Task Completed*\n\n*${data.taskName}*\nStatus: ${data.status}${data.completedBy ? `\nCompleted by: ${data.completedBy}` : ''}`,
        },
      },
    ],
  });

  console.log(`✅ Task completion notification sent`);
}

export async function notifySystemAlert(
  title: string,
  message: string,
  severity: 'info' | 'warning' | 'error'
): Promise<void> {
  const emojis: Record<string, string> = {
    info: 'ℹ️',
    warning: '⚠️',
    error: '🚨',
  };

  await slack.chat.postMessage({
    channel: CHANNEL_ID!,
    blocks: [
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `${emojis[severity]} *${title}*\n${message}`,
        },
      },
    ],
  });

  console.log(`✅ ${severity.toUpperCase()} alert sent`);
}

export async function handleSlackNotifications(
  request: Request
): Promise<Response> {
  try {
    const { type, data } = await request.json();

    switch (type) {
      case 'revenue_alert':
        await notifyRevenueAlert(data);
        break;
      case 'deal_sourced':
        await notifyDealSourced(data);
        break;
      case 'task_complete':
        await notifyTaskComplete(data);
        break;
      case 'system_alert':
        await notifySystemAlert(data.title, data.message, data.severity);
        break;
      default:
        throw new Error(`Unknown notification type: ${type}`);
    }

    return new Response(
      JSON.stringify({ success: true, notification_type: type }),
      {
        headers: { 'Content-Type': 'application/json' },
        status: 200,
      }
    );
  } catch (error) {
    console.error('Slack notification error:', error);
    return new Response(
      JSON.stringify({
        error: error instanceof Error ? error.message : 'Unknown error',
      }),
      { headers: { 'Content-Type': 'application/json' }, status: 500 }
    );
  }
}

Deno.serve(handleSlackNotifications);
