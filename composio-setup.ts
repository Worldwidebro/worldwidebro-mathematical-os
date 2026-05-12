import { Composio } from "@composio/core";

/**
 * Composio Setup - Initialize and test your workspace connection
 */

async function setupComposio() {
  console.log("\n🚀 Initializing Composio SDK...\n");

  // Initialize with your API key
  const composio = new Composio({
    apiKey: process.env.COMPOSIO_API_KEY || "ak_nCUr47rLtuThE2_5XTqr",
  });

  console.log("✅ Composio initialized");
  console.log(`📍 Workspace: ${process.env.COMPOSIO_WORKSPACE}`);
  console.log(`📁 Project: ${process.env.COMPOSIO_PROJECT}\n`);

  try {
    // Get all available tools
    console.log("📦 Fetching available tools...\n");

    // Get specific toolkit (example: GitHub)
    const tools = await composio.tools.get("default-user", {
      toolkits: ["GITHUB"],
    });

    console.log(`Found ${tools.length} GitHub tools:`);
    tools.slice(0, 5).forEach((tool) => {
      console.log(`  • ${tool.name}`);
    });

    if (tools.length > 5) {
      console.log(`  ... and ${tools.length - 5} more`);
    }

    console.log("\n✅ Connection successful!\n");

    // Return connection info
    return {
      composio,
      workspace: process.env.COMPOSIO_WORKSPACE,
      project: process.env.COMPOSIO_PROJECT,
      toolsAvailable: tools.length,
    };
  } catch (error) {
    console.error("❌ Error connecting to Composio:", error);
    process.exit(1);
  }
}

/**
 * List available toolkits you can connect
 */
async function listAvailableToolkits(composio: Composio) {
  console.log("\n🔧 Available Integration Toolkits:\n");

  const commonToolkits = [
    "GITHUB",
    "SLACK",
    "GMAIL",
    "JIRA",
    "LINEAR",
    "TRELLO",
    "NOTION",
    "CONFLUENCE",
    "MICROSOFT_TEAMS",
    "ASANA",
    "SALESFORCE",
    "ZAPIER",
    "MAKE",
  ];

  commonToolkits.forEach((toolkit) => {
    console.log(`  ✓ ${toolkit}`);
  });

  console.log("\nTo see all available toolkits, run:");
  console.log("  composio tools list\n");
}

/**
 * Example: Execute a tool
 */
async function executeToolExample(composio: Composio) {
  console.log("📋 Example: Executing a Tool\n");

  console.log("To execute a GitHub action, you would do:");
  console.log(`
  const result = await composio.tools.execute('GITHUB_CREATE_REPO', {
    userId: 'your-user-id',
    arguments: {
      repo_name: 'my-new-repo',
      description: 'Created by Composio',
      private: false
    }
  });
  `);
}

/**
 * Main setup flow
 */
async function main() {
  console.log("╔════════════════════════════════════════════════════════════╗");
  console.log("║                     COMPOSIO LOCAL SETUP                   ║");
  console.log("║                   WinnersCircle Workspace                  ║");
  console.log("╚════════════════════════════════════════════════════════════╝");

  const setup = await setupComposio();
  await listAvailableToolkits(setup.composio);
  executeToolExample(setup.composio);

  console.log("╔════════════════════════════════════════════════════════════╗");
  console.log("║                       NEXT STEPS                           ║");
  console.log("╠════════════════════════════════════════════════════════════╣");
  console.log("║                                                            ║");
  console.log("║ 1. View your dashboard:                                    ║");
  console.log("║    https://dashboard.composio.dev/winnerscirclewcllc...    ║");
  console.log("║                                                            ║");
  console.log("║ 2. Connect tools from CLI:                                 ║");
  console.log("║    composio connect github                                 ║");
  console.log("║    composio connect slack                                  ║");
  console.log("║                                                            ║");
  console.log("║ 3. List connected tools:                                   ║");
  console.log("║    composio connected                                      ║");
  console.log("║                                                            ║");
  console.log("║ 4. Create an agent that uses these tools                   ║");
  console.log("║                                                            ║");
  console.log("║ 5. Track execution in your dashboard                       ║");
  console.log("║                                                            ║");
  console.log("╚════════════════════════════════════════════════════════════╝\n");
}

main().catch(console.error);
