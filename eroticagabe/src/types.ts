export type PortfolioData = {
  generatedAt: string;
  privacy: {
    publicFields: string[];
    excludedFields: string[];
  };
  founder: {
    name: string;
    handle: string;
    email: string;
    github: string;
    publicBio: string;
    proof: string[];
  };
  holdings: {
    owner: string;
    brand: string;
    contact: string;
    entityLayers: Array<{
      level: number;
      name: string;
      role: string;
      status: string;
    }>;
    capitalLayers: Array<{
      name: string;
      engine: string;
      targetMonthly: string;
      margin: string;
    }>;
  };
  metrics: {
    ventures: number;
    opcos: number;
    reposClassified: string;
    capitalLayers: number;
  };
  readinessSummary: {
    portfolioAverageReadiness: number;
    ventureCountVerified: number;
    ventureCountUnverified: number;
    methodology: string;
  };
  proof: Array<{
    label: string;
    stat: string;
    detail: string;
  }>;
  opcos: Array<{
    id: string;
    label: string;
    ventureCount: number;
  }>;
  ventures: Array<{
    id: string;
    name: string;
    sector: string;
    opco: string;
    stage: string;
    status: string;
    capabilities: string[];
    liveUrl?: string;
    readinessPct?: number;
    readinessTier?: string;
    auditedStage?: string;
    stageVerified: boolean;
  }>;
};
