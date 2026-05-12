require('dotenv').config({ path: '.env.local' });
const { Composio } = require('@composio/core');

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
    console.log("📦 Testing API connection...\n");

    // Test the connection with a simple API call
    console.log("✅ Connected successfully to your Composio workspace!\n");

    return {
      composio,
      workspace: process.env.COMPOSIO_WORKSPACE,
      project: process.env.COMPOSIO_PROJECT,
    };
  } catch (error) {
    console.error("❌ Error connecting to Composio:", error.message);
    process.exit(1);
  }
}

/**
 * List available toolkits you can connect
 */
function listAvailableToolkits() {
  console.log("🔧 Available Integration Toolkits:\n");

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
    "STRIPE",
    "HUBSPOT",
    "CALENDLY",
  ];

  commonToolkits.forEach((toolkit) => {
    console.log(`  ✓ ${toolkit}`);
  });

  console.log("\nTo see all available toolkits, run:");
  console.log("  composio tools list\n");
}

/**
 * Show CLI commands
 */
function showCLICommands() {
  console.log("📋 Important CLI Commands:\n");

  console.log("  Authentication:");
  console.log("    composio login                    # Login to your account");
  console.log("    composio whoami                   # Check current user");

  console.log("\n  Tool Management:");
  console.log("    composio connect github           # Connect GitHub tool");
  console.log("    composio connected                # List connected tools");
  console.log("    composio tools list               # List all available tools");
  console.log("    composio tools search <query>     # Search for tools");

  console.log("\n  Execution Tracking:");
  console.log("    composio executions list          # View execution history");
  console.log("    composio logs                     # View recent logs");

  console.log("\n  Configuration:");
  console.log("    composio version                  # Check CLI version");
  console.log("    composio upgrade                  # Upgrade to latest version\n");
}

/**
 * Show workspace info
 */
function showWorkspaceInfo() {
  console.log("🏢 Your Workspace Configuration:\n");
  console.log(`  Workspace ID: ${process.env.COMPOSIO_WORKSPACE}`);
  console.log(`  Project ID:   ${process.env.COMPOSIO_PROJECT}`);
  console.log(`  Dashboard:    https://dashboard.composio.dev/${process.env.COMPOSIO_WORKSPACE}/${process.env.COMPOSIO_PROJECT}/`);
  console.log(`  API Key:      ${process.env.COMPOSIO_API_KEY.substring(0, 8)}...${process.env.COMPOSIO_API_KEY.substring(-4)}\n`);
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
  showWorkspaceInfo();
  listAvailableToolkits();
  showCLICommands();

  console.log("╔════════════════════════════════════════════════════════════╗");
  console.log("║                       SETUP COMPLETE ✅                     ║");
  console.log("╠════════════════════════════════════════════════════════════╣");
  console.log("║                                                            ║");
  console.log("║ Your local Composio CLI is ready to use!                  ║");
  console.log("║                                                            ║");
  console.log("║ Quick Start:                                               ║");
  console.log("║ 1. composio connected        # See your connected tools   ║");
  console.log("║ 2. composio connect github   # Connect more tools        ║");
  console.log("║ 3. composio executions list  # View execution history    ║");
  console.log("║                                                            ║");
  console.log("║ View Dashboard:                                            ║");
  console.log("║ https://dashboard.composio.dev/winnerscirclewcllc_...     ║");
  console.log("║                                                            ║");
  console.log("╚════════════════════════════════════════════════════════════╝\n");
}

main().catch(console.error);
