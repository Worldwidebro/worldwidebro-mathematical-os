/**
 * Example usage of LogicLayers registry and helper functions
 */

import yaml from 'js-yaml';
import fs from 'fs';
import {
  LogicLayersRegistry,
  getCapabilitiesForLayer,
  getLayersByCategory,
  findLayersWithCapability,
  getUniqueCapabilitiesForLayers,
  classifyTaskToLayers,
  getLayerSummary,
} from '../types/LogicLayers';

// Load the registry
const registryYaml = fs.readFileSync('../data/LOGIC_LAYERS_REGISTRY.yaml', 'utf-8');
const registry = yaml.load(registryYaml) as LogicLayersRegistry;

// Example 1: Get capabilities for a specific layer
console.log('=== Example 1: Get Capabilities ===');
const coldOutreachCaps = getCapabilitiesForLayer('LOGIC-001', registry);
console.log('Cold Outreach (LOGIC-001) requires:', coldOutreachCaps);

// Example 2: Find all layers in a category
console.log('\n=== Example 2: Layers by Category ===');
const salesLayers = getLayersByCategory('sales', registry);
console.log(`Sales layers (${salesLayers.length}):`);
salesLayers.forEach(layer => console.log(`  - ${layer.id}: ${layer.name}`));

// Example 3: Find layers with a specific capability
console.log('\n=== Example 3: Find Layers with Capability ===');
const emailWritingLayers = findLayersWithCapability('write-emails', registry);
console.log('Layers that require email writing:');
emailWritingLayers.forEach(layer => console.log(`  - ${layer.id}: ${layer.name}`));

// Example 4: Get unique capabilities for a multi-layer task
console.log('\n=== Example 4: Combined Capabilities ===');
const layerIds = ['LOGIC-001', 'LOGIC-002', 'LOGIC-003'];
const combinedCaps = getUniqueCapabilitiesForLayers(layerIds, registry);
console.log(`Capabilities needed for ${layerIds.join(', ')}:`);
console.log(Array.from(combinedCaps).sort().join(', '));

// Example 5: Classify a task to layers
console.log('\n=== Example 5: Task Classification ===');
const taskDescription = "Create a cold email sequence to reach startup founders";
const matchedLayers = classifyTaskToLayers(taskDescription, registry);
console.log(`Task: "${taskDescription}"`);
console.log(`Matched layers: ${matchedLayers.join(', ')}`);

// Example 6: Get layer summary for display
console.log('\n=== Example 6: Layer Summary ===');
console.log(getLayerSummary('LOGIC-004', registry));

// Example 7: Integration with task classification
console.log('\n=== Example 7: Task Classification Pipeline ===');
const task = {
  id: 'TASK-123',
  description: 'Send personalized discovery emails to qualified leads',
  priority: 'high'
};

const taskLayers = classifyTaskToLayers(task.description, registry);
const taskCapabilities = getUniqueCapabilitiesForLayers(taskLayers, registry);

console.log(`Task: ${task.description}`);
console.log(`Classified layers: ${taskLayers.join(', ')}`);
console.log(`Required capabilities: ${Array.from(taskCapabilities).join(', ')}`);
