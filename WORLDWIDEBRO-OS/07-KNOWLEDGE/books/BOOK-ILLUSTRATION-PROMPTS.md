# Adventure Atlas — Ready-to-Use Illustration Prompts

**For:** ComfyUI + Stable Diffusion / SDXL / Flux  
**Format:** Use with `run_batch.py` or individual `run_workflow.py` commands  
**Style:** Warm watercolor, children's book illustration style  

---

## Master Style Definition

Use this as a prefix for every prompt:

```
Warm, inviting watercolor illustration, children's picture book style, 
soft colors, friendly characters, emotional storytelling, 
professional children's book quality, illustration by acclaimed children's book artist
```

---

## Page-by-Page Prompts (19 images needed)

### Page 2: Boy Reaching for Book
```
A curious 7-year-old boy reaching for a mysterious leather-bound book on a shelf, 
cozy morning light, dust particles, warm oranges and blues, books around, 
grandparent's study, magical atmosphere. Watercolor children's book illustration.
```

### Page 3: Opening the Blank Book
```
7-year-old boy opening a large, beautiful leather book with blank glowing pages, 
sitting at table, amazed expression, soft window light, cozy room, magical feeling, 
watercolor, children's book quality.
```

### Page 4: Grandma Explaining
```
Warm scene of grandmother and young boy sitting together, grandmother pointing at 
blank book, smiling kindly, cozy armchair, wooden furniture, family photos, warm 
lighting, watercolor, loving moment.
```

### Page 6: Kids Building Blocks
```
Two 7-year-old children (Max and Zoe) building tall colorful block tower, laughing, 
playful energy, bright colors, sunny playroom, scattered blocks, joyful, watercolor.
```

### Page 7: Max Drawing in Atlas
```
Close-up of boy at wooden desk, drawing and writing in notebook carefully, colored 
pencils nearby, warm lamplight, focused expression, creative moment, watercolor.
```

### Page 8: Caterpillar on Leaf
```
Close-up of bright green caterpillar with dots and tiny legs on green leaf, 
magnifying glass nearby, boy observing carefully, nature, garden setting, 
watercolor, curious observation.
```

### Page 10: Adventure Montage
```
Four small scenes: soccer player scoring goal, child on bike without training wheels, 
baking cookies in kitchen, catching glowing firefly at dusk. Combined on one page, 
warm colors, adventure montage, watercolor.
```

### Page 12: Exploring Together
```
Max and Zoe exploring nature: climbing oak tree, collecting rocks, catching tadpoles 
in creek, building fort with blankets. Multiple activities, outdoor adventure, 
friendship, cooperation, watercolor.
```

### Page 13: Atlas Full and Proud
```
Young boy proudly holding thick full notebook (Adventure Atlas) with many pages, 
smiling, grandmother looking on with pride, cozy home, warm lighting, wooden 
furniture, family love, achievement.
```

### Page 14: Grandma Reviews Atlas
```
Grandmother and Max sitting together, grandmother reading through full atlas, 
reviewing drawings, both smiling, emotional bonding moment, cozy, lamp lighting, 
warm colors, memory making.
```

### Page 18: New Beginning
```
7-year-old boy by window in morning sunlight, holding brand new blank notebook 
(Year Two atlas), pen in hand, excited ready expression, peaceful, cozy room, 
hopeful, new beginning, watercolor.
```

---

## Additional Supporting Scenes

Choose/generate any of these for secondary pages:

- School classroom, Zoe smiling
- Soccer field, ball in net
- Bike riding, no training wheels
- Cookie baking with parent
- Firefly glowing at night
- Creek with rocks
- Tree with climbing boy
- Bedroom with writing desk
- Park with playground
- Nature scene with leaves

---

## How to Generate with ComfyUI

### Step 1: Check ComfyUI Status
```bash
python3 ~/.hermes/hermes-agent/skills/creative/comfyui/scripts/health_check.py
```

Expected: `✓ comfy-cli installed` `✓ server running` `✓ checkpoint found`

### Step 2: Generate One Test Image
```bash
cd ~/.hermes/hermes-agent/skills/creative/comfyui

python3 scripts/run_workflow.py \
  --workflow workflows/sdxl_txt2img.json \
  --args '{
    "prompt": "Warm, inviting watercolor illustration, children'\''s picture book style, A curious 7-year-old boy reaching for a mysterious leather-bound book on a shelf, cozy morning light, dust particles, warm oranges and blues...",
    "negative_prompt": "blurry, low quality, text, watermark, distorted, ugly, bad anatomy",
    "steps": 25,
    "seed": 12345
  }' \
  --output-dir /Users/acebless/Documents/books/illustrations
```

**Check output:** `/Users/acebless/Documents/books/illustrations/` should have a PNG

### Step 3: Generate All 19 Images
```bash
# Option A: Batch generation (all at once)
python3 scripts/run_batch.py \
  --workflow workflows/sdxl_txt2img.json \
  --count 19 \
  --args '{"steps": 25}' \
  --output-dir /Users/acebless/Documents/books/illustrations

# Option B: Individual with different seeds (best quality control)
# Generate each prompt separately with --seed to control randomness
```

---

## Recommended Settings

**For SDXL (balanced):**
- Steps: 25 (quality vs speed)
- Guidance: 8 (follow prompt well)
- Sampler: DPM++ (fast, good quality)
- Seed: -1 (random each time)

**For Flux (if available, higher quality):**
- Steps: 20 (Flux is efficient)
- Guidance: 3.5 (Flux likes lower guidance)
- Better quality, takes longer

---

## Output Files

ComfyUI saves as:
- Format: PNG (lossless, print-ready)
- Filenames: `comfyui_00001_.png`, `comfyui_00002_.png`
- Resolution: 768x1024 (portrait book page)

---

## Time Estimate

- SDXL: 2-3 min per image = ~50 min total
- Flux: 4-5 min per image = ~90 min total
- With queue: probably 1.5-2.5 hours

---

## Cost

**ComfyUI local:** $0 (just your GPU)  
**Comfy Cloud:** $2-5 per image ($38-95 total)

---

## Quality Tips

1. **Consistency:** Same style prefix for all
2. **Be specific:** "Max" not "a boy"
3. **Emotions matter:** "joyful, wondering, amazed"
4. **Test first:** Generate 3 test images, adjust, then batch
5. **Negative prompt:** Always include what to avoid

---

## Next Step

Run this command right now to verify ComfyUI works:

```bash
python3 ~/.hermes/hermes-agent/skills/creative/comfyui/scripts/health_check.py
```

If that works → you can generate all 19 illustrations in 2 hours, free.

If that fails → we fall back to Midjourney ($100) or DIY.

---

**Your son gets a book with real AI-generated illustrations made by you. That's the story.**
