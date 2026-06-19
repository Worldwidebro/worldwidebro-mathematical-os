/**
 * Test Layer 4: Clip Detection
 */

import { detectClips } from "./layers/4-detection.js";

const TRANSCRIPT = `
00:00:00: Welcome to the podcast. I'm John Smith, founder of PayrollMaster.
00:01:30: We handle payroll, taxes, compliance for startups in one platform.
00:03:15: I started this because I was frustrated. Payroll took 6 hours every month.
I missed a payment once. That moment I realized payroll was completely broken.
00:06:45: Here's what people get wrong: they think it's just cutting checks.
But compliance and taxes are 90% of the work. Everyone does this backwards.
00:09:20: Our framework: Step 1, automate data collection. Step 2, handle compliance.
Step 3, instant reporting. That's how you fix payroll.
00:12:34: One thing surprised me - founders don't know they're breaking tax law.
I had a customer ask "wait, we have to report that to the IRS?"
It's scary how many edge cases exist. We became the guardrails.
00:15:00: My biggest mistake was underestimating the compliance problem.
I thought tech was hard. Actually, staying compliant in 50 states is hard.
00:17:45: Advice: never underestimate the boring stuff.
Payroll is boring but it'll kill your company if you get it wrong.
00:20:00: The future is AI-driven compliance.
Instead of hiring a payroll person, you get an AI that knows every rule.
`;

const CONTEXT = {
  venture_id: "hrms-001",
  venture_name: "PayrollMaster",
  sector: "HR/Payroll SaaS",
  founder_name: "John Smith",
  trending_topics: ["AI automation", "Compliance 2026", "Founder mistakes"],
};

async function runTest() {
  console.log("\n🎬 LAYER 4: CLIP DETECTION TEST");
  console.log("═".repeat(50));
  console.log(`Venture: ${CONTEXT.venture_name}`);
  console.log(`Founder: ${CONTEXT.founder_name}`);
  console.log(`Sector: ${CONTEXT.sector}\n`);

  try {
    console.log("⏳ Analyzing with Claude...\n");
    const result = await detectClips(TRANSCRIPT, CONTEXT);

    console.log("✅ COMPLETE\n");
    console.log(`Found: ${result.clips_count} viral clips`);

    console.log("\nTOP 5 CLIPS:");
    console.log("═".repeat(50));

    result.clips.slice(0, 5).forEach((clip, idx) => {
      console.log(
        `\n${idx + 1}. [${clip.type}] Score: ${clip.final_score.toFixed(1)}/10`
      );
      console.log(`   Time: ${clip.timestamp}`);
      console.log(`   Platforms: ${clip.best_platforms.join(", ")}`);
      console.log(`   Hook: "${clip.suggested_hook}"`);
    });

    console.log("\n" + "═".repeat(50));
    console.log("ALL 12 CLIPS:");
    result.clips.forEach((clip, idx) => {
      console.log(
        `${(idx + 1).toString().padStart(2)}. ${clip.type.padEnd(12)} ${clip.final_score.toFixed(1)}/10`
      );
    });

    console.log("\n✅ Layer 4 Test Successful!");
    return result;
  } catch (error) {
    console.error("❌ Error:", error.message);
    process.exit(1);
  }
}

runTest();
