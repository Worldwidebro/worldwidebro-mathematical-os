export const serviceName = 'notification-service';
export const version = '1.0.0';
export const status = 'active';

export interface HealthCheckResult {
  serviceName: string;
  version: string;
  status: 'healthy' | 'unhealthy';
  timestamp: string;
  uptime: number;
}

const startTime = Date.now();

export function getHealthStatus(): HealthCheckResult {
  return {
    serviceName,
    version,
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: Math.floor((Date.now() - startTime) / 1000)
  };
}

export function initializeService(): { serviceName: string; initialized: boolean; timestamp: string } {
  return {
    serviceName,
    initialized: true,
    timestamp: new Date().toISOString()
  };
}

export function sendNotification(recipientId: string, channel: 'email' | 'sms' | 'push', message: string) {
  return {
    notificationId: `notif-${Date.now()}`,
    recipientId,
    channel,
    message,
    status: 'delivered',
    sentAt: new Date().toISOString()
  };
}

export function getNotificationLogs(recipientId: string) {
  return [
    { id: 'notif-1', recipientId, channel: 'email', status: 'delivered', timestamp: new Date().toISOString() }
  ];
}
