export const serviceName = 'document-service';
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

export function uploadDocument(filename: string, category: string) {
  return {
    documentId: `doc-${Date.now()}`,
    filename,
    category,
    url: `https://storage.realestate-os.local/docs/${filename}`,
    uploadedAt: new Date().toISOString()
  };
}

export function getDocumentMetadata(documentId: string) {
  return {
    documentId,
    filename: 'lease_agreement.pdf',
    sizeBytes: 1048576,
    mimeType: 'application/pdf',
    createdAt: new Date().toISOString()
  };
}
