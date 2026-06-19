import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { createClient } from "@supabase/supabase-js";
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

// Load .env
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const envPath = path.join(__dirname, "..", ".env");
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, "utf-8");
  envContent.split("\n").forEach(line => {
    const [key, value] = line.split("=");
    if (key && value) process.env[key.trim()] = value.trim();
  });
}

const supabase = createClient(
  process.env.SUPABASE_URL || "https://cyhzilqldouzgynacqpe.supabase.co",
  process.env.SUPABASE_KEY
);

const server = new Server({
  name: "portfolio-mcp",
  version: "1.0.0",
});

server.setRequestHandler("tools/list", async () => ({
  tools: [
    {
      name: "list_ventures_by_sector",
      description: "Get all ventures in a specific sector with metrics",
      inputSchema: {
        type: "object",
        properties: {
          sector: { type: "string", description: "Sector name (e.g., Healthcare, AI, SaaS)" },
          limit: { type: "number", description: "Max results (default 50)" }
        },
        required: ["sector"]
      }
    },
    {
      name: "list_ventures_by_stage",
      description: "Get ventures filtered by stage (MVP, Growth, Scale, etc)",
      inputSchema: {
        type: "object",
        properties: {
          stage: { type: "string" },
          limit: { type: "number" }
        },
        required: ["stage"]
      }
    },
    {
      name: "search_ventures",
      description: "Search ventures by name or keywords",
      inputSchema: {
        type: "object",
        properties: {
          query: { type: "string" },
          limit: { type: "number" }
        },
        required: ["query"]
      }
    },
    {
      name: "get_venture_metrics",
      description: "Get detailed metrics for a specific venture",
      inputSchema: {
        type: "object",
        properties: {
          venture_id: { type: "string" }
        },
        required: ["venture_id"]
      }
    },
    {
      name: "find_ventures_at_risk",
      description: "Find ventures with runway < 6 months or negative growth",
      inputSchema: {
        type: "object",
        properties: {
          runway_threshold_months: { type: "number", description: "Default 6" },
          limit: { type: "number" }
        }
      }
    },
    {
      name: "portfolio_summary",
      description: "Get overall portfolio health summary",
      inputSchema: {
        type: "object",
        properties: {
          by_sector: { type: "boolean", description: "Break down by sector" }
        }
      }
    }
  ]
}));

server.setRequestHandler("tools/call", async (request) => {
  const { name, arguments: args } = request.params;

  try {
    if (name === "list_ventures_by_sector") {
      const { sector, limit = 50 } = args;
      const { data, error } = await supabase
        .from("ventures")
        .select("id, name, stage, status, sector")
        .eq("sector", sector)
        .limit(limit);

      if (error) throw error;
      return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
    }

    if (name === "list_ventures_by_stage") {
      const { stage, limit = 50 } = args;
      const { data, error } = await supabase
        .from("ventures")
        .select("id, name, sector, stage, status")
        .eq("stage", stage)
        .limit(limit);

      if (error) throw error;
      return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
    }

    if (name === "search_ventures") {
      const { query, limit = 50 } = args;
      const { data, error } = await supabase
        .from("ventures")
        .select("id, name, sector, stage, status")
        .ilike("name", `%${query}%`)
        .limit(limit);

      if (error) throw error;
      return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
    }

    if (name === "get_venture_metrics") {
      const { venture_id } = args;
      const { data, error } = await supabase
        .from("ventures")
        .select("*")
        .eq("id", venture_id)
        .single();

      if (error) throw error;
      return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
    }

    if (name === "find_ventures_at_risk") {
      const { runway_threshold_months = 6, limit = 50 } = args;
      const { data, error } = await supabase
        .from("ventures")
        .select("id, name, sector, stage, status")
        .lt("runway_months", runway_threshold_months)
        .limit(limit);

      if (error) throw error;
      return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
    }

    if (name === "portfolio_summary") {
      const { by_sector = false } = args;
      const { data, error } = await supabase
        .from("ventures")
        .select("sector, stage, status, COUNT(*) as count", { count: "exact" });

      if (error) throw error;
      return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
    }

    return {
      content: [{ type: "text", text: `Unknown tool: ${name}` }],
      isError: true
    };
  } catch (error) {
    return {
      content: [{ type: "text", text: `Error: ${error.message}` }],
      isError: true
    };
  }
});

const transport = new StdioServerTransport();
await server.connect(transport);
