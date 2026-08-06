/**
 * Trigger.dev webhook handler for Apple Notes ingestion.
 * Receives notes from Zapier/Trigger.dev and routes to apple_notes_agent.py
 */

import { z } from "zod";

// Schema for incoming Apple Note webhook
const AppleNoteWebhookSchema = z.object({
  note_content: z.string().min(10),
  note_id: z.string().optional(),
  source: z.enum(["apple_notes", "zapier", "manual"]).default("apple_notes"),
  timestamp: z.string().optional(),
});

type AppleNoteWebhook = z.infer<typeof AppleNoteWebhookSchema>;

// Configuration
const AGENT_API_URL = process.env.AGENT_API_URL || "http://localhost:8000";
const AGENT_API_KEY = process.env.AGENT_API_KEY || "";

interface AgentResponse {
  success: boolean;
  note_id: string;
  venture_id?: string;
  note_type?: string;
  entities?: string[];
  actions?: string[];
  errors?: string[];
}

/**
 * Send note to Python agent for processing
 */
async function sendToAgent(note: AppleNoteWebhook): Promise<AgentResponse> {
  try {
    const response = await fetch(`${AGENT_API_URL}/process-note`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...(AGENT_API_KEY && { Authorization: `Bearer ${AGENT_API_KEY}` }),
      },
      body: JSON.stringify({
        content: note.note_content,
        note_id: note.note_id,
        source: note.source,
      }),
    });

    if (!response.ok) {
      throw new Error(`Agent returned ${response.status}: ${response.statusText}`);
    }

    const result = await response.json();
    return {
      success: true,
      note_id: result.note_id,
      venture_id: result.venture_id,
      note_type: result.note_type,
      entities: result.entities,
      actions: result.actions,
    };
  } catch (error) {
    console.error("Agent processing failed:", error);
    return {
      success: false,
      note_id: note.note_id || "unknown",
      errors: [String(error)],
    };
  }
}

/**
 * Handle incoming webhook from Trigger.dev
 * Returns 202 Accepted immediately; processing happens async
 */
export async function handleAppleNoteWebhook(
  payload: unknown
): Promise<{ statusCode: number; body: Record<string, unknown> }> {
  try {
    // Validate payload
    const note = AppleNoteWebhookSchema.parse(payload);
    console.log(`Received note: ${note.note_id || "new"}`);

    // Process note asynchronously (fire and forget)
    sendToAgent(note)
      .then((result) => {
        console.log(
          `Note ${result.note_id} processed: ${result.success ? "✓" : "✗"}`
        );
        if (result.errors) {
          console.error(`  Errors: ${result.errors.join(", ")}`);
        } else if (result.success) {
          console.log(
            `  Venture: ${result.venture_id}, Type: ${result.note_type}`
          );
          console.log(`  Entities: ${result.entities?.length || 0}`);
          console.log(`  Actions: ${result.actions?.length || 0}`);
        }
      })
      .catch((err) => console.error(`Async processing error: ${err}`));

    // Return 202 Accepted immediately
    return {
      statusCode: 202,
      body: {
        status: "accepted",
        note_id: note.note_id,
        message: "Note queued for processing",
      },
    };
  } catch (error) {
    console.error("Webhook parsing failed:", error);
    return {
      statusCode: 400,
      body: {
        error: "Invalid payload",
        details: error instanceof Error ? error.message : String(error),
      },
    };
  }
}

/**
 * Next.js API route handler
 * Usage: pages/api/webhooks/apple-notes.ts
 */
export async function appleNotesApiRoute(req: any, res: any) {
  if (req.method !== "POST") {
    res.status(405).json({ error: "Method not allowed" });
    return;
  }

  const { statusCode, body } = await handleAppleNoteWebhook(req.body);
  res.status(statusCode).json(body);
}

/**
 * Express middleware
 * Usage: app.post("/webhook/apple-notes", expressMiddleware)
 */
export function createExpressMiddleware() {
  return async (req: any, res: any) => {
    if (req.method !== "POST") {
      res.status(405).json({ error: "Method not allowed" });
      return;
    }

    const { statusCode, body } = await handleAppleNoteWebhook(req.body);
    res.status(statusCode).json(body);
  };
}
