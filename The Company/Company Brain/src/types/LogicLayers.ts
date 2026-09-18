/**
 * Logic Layers Registry Types
 * 
 * Defines TypeScript interfaces for the LOGIC_LAYERS_REGISTRY.yaml
 * Used by task classification system to map tasks → logic layers → capabilities
 */

export type LogicLayerCategory = 
  | 'outreach'
  | 'sales'
  | 'support'
  | 'product'
  | 'operations';

export interface LogicLayer {
  /** Unique identifier (e.g., LOGIC-001) */
  id: string;
  /** Human-readable name (e.g., "Cold Outreach") */
  name: string;
  /** Detailed description of what this layer does */
  description: string;
  /** Category grouping (outreach, sales, support, product, operations) */
  category: LogicLayerCategory;
  /** List of capabilities required for this layer */
  capabilities: string[];
  /** Example tasks that use this layer */
  example_tasks?: string[];
}

export interface LogicLayersRegistry {
  logic_layers: Record<string, LogicLayer>;
}

/**
 * Get all capabilities required for a logic layer
 * @param layerId - The logic layer ID (e.g., "LOGIC-001")
 * @param registry - The loaded registry
 * @returns Array of capability names
 */
export function getCapabilitiesForLayer(
  layerId: string,
  registry: LogicLayersRegistry
): string[] {
  const layer = registry.logic_layers[layerId];
  if (!layer) {
    throw new Error(`Logic layer not found: ${layerId}`);
  }
  return layer.capabilities;
}

/**
 * Get all logic layers in a category
 * @param category - The category to filter by
 * @param registry - The loaded registry
 * @returns Array of logic layers in that category
 */
export function getLayersByCategory(
  category: LogicLayerCategory,
  registry: LogicLayersRegistry
): LogicLayer[] {
  return Object.values(registry.logic_layers).filter(
    layer => layer.category === category
  );
}

/**
 * Find logic layers that contain a specific capability
 * @param capability - The capability name to search for
 * @param registry - The loaded registry
 * @returns Array of logic layers that have this capability
 */
export function findLayersWithCapability(
  capability: string,
  registry: LogicLayersRegistry
): LogicLayer[] {
  return Object.values(registry.logic_layers).filter(
    layer => layer.capabilities.includes(capability)
  );
}

/**
 * Get all unique capabilities across a set of logic layers
 * @param layerIds - Array of logic layer IDs
 * @param registry - The loaded registry
 * @returns Set of all capabilities needed
 */
export function getUniqueCapabilitiesForLayers(
  layerIds: string[],
  registry: LogicLayersRegistry
): Set<string> {
  const capabilities = new Set<string>();
  
  for (const layerId of layerIds) {
    const caps = getCapabilitiesForLayer(layerId, registry);
    caps.forEach(cap => capabilities.add(cap));
  }
  
  return capabilities;
}

/**
 * Check if a logic layer exists
 * @param layerId - The logic layer ID to check
 * @param registry - The loaded registry
 * @returns true if the layer exists
 */
export function layerExists(
  layerId: string,
  registry: LogicLayersRegistry
): boolean {
  return layerId in registry.logic_layers;
}

/**
 * Get all logic layer IDs
 * @param registry - The loaded registry
 * @returns Array of all layer IDs
 */
export function getAllLayerIds(registry: LogicLayersRegistry): string[] {
  return Object.keys(registry.logic_layers);
}

/**
 * Map a task description to relevant logic layers
 * This is a basic implementation that checks example_tasks
 * For production, use a more sophisticated classification method
 * @param taskDescription - The task description to classify
 * @param registry - The loaded registry
 * @returns Array of matching logic layer IDs
 */
export function classifyTaskToLayers(
  taskDescription: string,
  registry: LogicLayersRegistry
): string[] {
  const lowerDescription = taskDescription.toLowerCase();
  const matches: string[] = [];
  
  Object.entries(registry.logic_layers).forEach(([layerId, layer]) => {
    // Check if task description matches any example tasks (case-insensitive)
    const hasMatch = layer.example_tasks?.some(example =>
      lowerDescription.includes(example.toLowerCase()) ||
      example.toLowerCase().includes(lowerDescription)
    ) ?? false;
    
    // Also check if description keywords match
    const descriptionMatch = 
      lowerDescription.includes(layer.category) ||
      lowerDescription.includes(layer.name.toLowerCase());
    
    if (hasMatch || descriptionMatch) {
      matches.push(layerId);
    }
  });
  
  return matches;
}

/**
 * Create a summary of a logic layer for display
 * @param layerId - The logic layer ID
 * @param registry - The loaded registry
 * @returns Formatted string summary
 */
export function getLayerSummary(
  layerId: string,
  registry: LogicLayersRegistry
): string {
  const layer = registry.logic_layers[layerId];
  if (!layer) {
    return `Unknown layer: ${layerId}`;
  }
  
  return `
Layer: ${layer.name} (${layer.id})
Category: ${layer.category}
Description: ${layer.description}
Capabilities: ${layer.capabilities.join(', ')}
Example Tasks: ${layer.example_tasks?.join('; ') || 'None'}
  `.trim();
}
