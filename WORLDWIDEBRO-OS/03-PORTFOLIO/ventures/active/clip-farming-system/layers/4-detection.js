/**
 * Layer 4: Clip Detection Engine
 * Purpose: Identify 12 best viral moments in transcript using Claude
 */

const Anthropic = require("@anthropic-ai/sdk");
const client = new Anthropic();

async function detectClips(transcript, context) {
  const {
    venture_id = "unknown",
    venture_name = "Unknown",
    sector = "General",
    trending_topics = [],
    founder_name = "Founder",
  } = context;

  const systemPrompt = `You are an expert content strategist for viral clips.
Analyze the transcript and find the 12 most viral-worthy moments.

For each clip identify:
- Timestamp (start-end)
- Type: emotional_hook | framework | quote | contrarian | actionable
- Text: exact quote
- Scores (1-10): emotional_impact, relevance, shareability
- Best platforms: TikTok | Instagram | LinkedIn | Twitter | YouTube | Facebook
- Hook: short caption

SCORING:
- Emotional: 8-10 impact, medium relevance, high shareability
- Framework: low emotion, high relevance, high shareability
- Quote: medium emotion, high relevance, very high shareability
- Contrarian: medium emotion, high relevance, very high shareability
- Actionable: low emotion, high relevance, medium shareability

Return ONLY valid JSON array with this exact structure:
[
  {
    "clip_id": 1,
    "timestamp": "00:12:34-00:12:45",
    "duration": 11,
    "type": "emotional_hook",
    "text": "exact quote",
    "emotional_impact": 9,
    "relevance": 7,
    "shareability": 9,
    "final_score": 8.3,
    "best_platforms": ["TikTok", "Instagram"],
    "suggested_hook": "short headline"
  }
]

Return ONLY JSON array, no other text.`;

  const userPrompt = `Analyze this ${sector} interview with ${founder_name} from ${venture_name}.

Trending topics: ${trending_topics.join(", ") || "general startup topics"}

Transcript:
${transcript}

Find 12 most viral clips. Score each. Recommend platforms.
Return only JSON array, sorted by final_score (highest first).`;

  try {
    console.log(`🧠 Analyzing ${venture_name}...`);

    const response = await client.messages.create({
      model: "claude-3-5-sonnet-20241022",
      max_tokens: 4000,
      system: systemPrompt,
      messages: [
        {
          role: "user",
          content: userPrompt,
        },
      ],
    });

    const responseText = response.content[0].text;
    const clips = JSON.parse(responseText);

    if (!Array.isArray(clips)) {
      throw new Error("Expected array response");
    }

    clips.sort((a, b) => b.final_score - a.final_score);
    const topClips = clips.slice(0, 12);

    return {
      venture_id,
      venture_name,
      sector,
      clips_count: topClips.length,
      clips: topClips,
      timestamp: new Date().toISOString(),
    };
  } catch (error) {
    console.error("❌ Error:", error.message);
    throw error;
  }
}

module.exports = { detectClips };

// Test if run directly
if (require.main === module) {
  const transcript = `
00:00:00: Welcome. I'm John Smith, founder of PayrollMaster.
00:02:15: I started this because payroll was broken. I remember missing a payment to an employee.
That was the moment I realized this was a $100B problem waiting to be solved.
00:05:30: Here's what everyone gets wrong about payroll. They think it's just cutting checks.
Actually, compliance is 90%. Everyone does this backwards.
00:08:45: Our framework: Step 1, automate data. Step 2, handle compliance. Step 3, instant reporting.
00:12:34: One thing surprised me - founders don't know they're breaking tax law.
It's scary how many legal edge cases exist. We became the guardrails.
00:15:00: Advice: never underestimate compliance. It's boring but it'll kill you.
  `;

  const context = {
    venture_id: "hrms-001",
    venture_name: "PayrollMaster",
    sector: "HR/Payroll",
    founder_name: "John Smith",
    trending_topics: ["AI automation", "Compliance 2026"],
  };

  detectClips(transcript, context)
    .then((result) => {
      console.log("\n✅ Complete! Top 3 Clips:");
      result.clips.slice(0, 3).forEach((clip, idx) => {
        console.log(`\n${idx + 1}. [${clip.type}] Score: ${clip.final_score}`);
        console.log(`   Time: ${clip.timestamp}`);
        console.log(`   Text: "${clip.text}"`);
        console.log(`   Platforms: ${clip.best_platforms.join(", ")}`);
      });
    })
    .catch((err) => console.error("Error:", err));
}
