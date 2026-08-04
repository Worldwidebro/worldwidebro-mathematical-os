import { AgentMetadata, AgentExecutionResult } from '@realestate-os/shared-types';
export declare const AI_AGENTS_LIST: AgentMetadata[];
export declare function getAllAgents(): AgentMetadata[];
export declare function getAgentByName(name: string): AgentMetadata | undefined;
export declare function invokeAgent(agentName: string, payload?: any): Promise<AgentExecutionResult>;
