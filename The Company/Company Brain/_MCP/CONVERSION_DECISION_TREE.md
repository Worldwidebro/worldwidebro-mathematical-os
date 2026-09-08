---
id: CONVERSION-DECISION-TREE-001
title: File Conversion Decision Tree — Reference Guide
scope: Company Brain (all file conversion operations)
authority: CP-027 (Infrastructure Control Plane)
updated: 2026-09-06
status: ACTIVE
---

# CONVERSION DECISION TREE — Reference Guide

[[STARTHERE]] | [[FILE_CONVERSION_SERVICE|FILE_CONVERSION_SERVICE.md]] | [[_REGISTRIES/CANONICAL/FILE_FORMAT_REGISTRY.yaml|FILE_FORMAT_REGISTRY]]

**Purpose:** Complete reference for how the file conversion system makes decisions about engines, privacy, and fallbacks.

---

## 1. THE ALGORITHM (HIGH LEVEL)

```
INPUT (file + target format)
    ↓
┌─ STEP 1: VALIDATE
│  ├─ File exists?
│  ├─ Format recognized?
│  └─ Privacy tier valid?
│     └─ If any fail: RETURN ERROR
│
├─ STEP 2: LOAD REGISTRY
│  └─ Look up conversion path in FILE_FORMAT_REGISTRY.yaml
│     ├─ If found: STEP 3
│     └─ If NOT found: STEP 4 (FALLBACK)
│
├─ STEP 3: SELECT ENGINE
│  ├─ Get engine + command from registry
│  ├─ Check privacy tier enforcement
│  │  ├─ TIER_1_ALWAYS_LOCAL: Engine must be local (Pandoc, FFmpeg, etc.)
│  │  ├─ TIER_2_PREFER_LOCAL: Try local first, fallback to cloud
│  │  └─ TIER_3_CLOUD_OK: Either local or cloud acceptable
│  └─ If privacy check fails: PRIVACY_VIOLATION ERROR
│
├─ STEP 4: EXECUTE CONVERSION
│  ├─ Run shell command for selected engine
│  ├─ Monitor for errors & timeout
│  └─ Return to STEP 5 (QA)
│
├─ STEP 5: FALLBACK (if STEP 2 found nothing)
│  ├─ Is this a KNOWN LIMITATION?
│  │  ├─ If yes: Check [[KILL-LIST.md]] → Log & return ConversionNotPossible
│  │  └─ If no: Try CloudConvert/Zamzar API
│  └─ If privacy_tier == TIER_1_ALWAYS_LOCAL: PrivacyViolation error
│
└─ STEP 6: QUALITY ASSURANCE
   ├─ File size reasonable? (0.1x to 10x original)
   ├─ Content spot-check (first 100 lines if text)
   ├─ Metadata preserved?
   └─ Return ConversionResult with PASS/WARN/FAIL attestation
```

---

## 2. STEP-BY-STEP EXECUTION

### Step 1: VALIDATE INPUT

```python
# Pseudocode
def validate_input(input_path, target_format, privacy_tier):
    # 1. Does file exist?
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input not found: {input_path}")
    
    # 2. Can we detect format from filename?
    input_format = Path(input_path).suffix.lstrip('.')
    if not input_format:
        raise ConversionError(f"Cannot detect format: {input_path}")
    
    # 3. Is privacy_tier valid?
    valid_tiers = [
        "TIER_1_ALWAYS_LOCAL",
        "TIER_2_PREFER_LOCAL",
        "TIER_3_CLOUD_OK"
    ]
    if privacy_tier not in valid_tiers:
        raise ConversionError(f"Invalid privacy_tier: {privacy_tier}")
    
    return input_format
```

**Decision points:**
- ✅ File exists + format detected + tier valid → STEP 2
- ❌ Any check fails → RETURN ERROR

---

### Step 2: LOAD REGISTRY

Load `_REGISTRIES/CANONICAL/FILE_FORMAT_REGISTRY.yaml` and search for conversion path.

```python
def find_conversion_path(registry, from_format, to_format):
    """Search registry for conversion spec"""
    for class_name, class_spec in registry['CANONICAL_FORMATS'].items():
        conversions = class_spec.get('conversions', [])
        for conv in conversions:
            # Match input format
            if conv.get('from') in [f".{from_format}", from_format]:
                # Match output format (or default if omitted)
                if conv.get('to') in [f".{to_format}", to_format] or 'to' not in conv:
                    return conv
    return None
```

**Decision points:**
- ✅ Conversion found in registry → STEP 3
- ❌ Not found → STEP 5 (FALLBACK)

**Example registry lookup:**

Input: `document.docx` → `md`

```yaml
CANONICAL_FORMATS:
  DOCUMENT:
    canonical: .md
    conversions:
      - from: .docx
        to: .md
        engine: pandoc
        command: "pandoc {input} -t markdown -o {output}"
        cost: free
        privacy: local
```

✅ Found → engine = `pandoc`, proceed to STEP 3.

---

### Step 3: SELECT ENGINE

```python
def select_engine(registry, input_format, target_format, privacy_tier, quality_required):
    """Select engine based on registry + privacy tier"""
    
    # Get conversion path from registry
    conv = find_conversion_path(registry, input_format, target_format)
    if not conv:
        return None  # STEP 5: FALLBACK
    
    engine = conv.get('engine')
    privacy = conv.get('privacy', 'unknown')
    
    # Check privacy tier constraints
    if privacy_tier == "TIER_1_ALWAYS_LOCAL":
        local_engines = [
            "pandoc", "ffmpeg", "imagemagick", "duckdb",
            "libreoffice", "tesseract", "ocrmypdf"
        ]
        if engine not in local_engines:
            raise PrivacyViolation(
                f"Engine {engine} requires cloud upload, "
                f"but TIER_1_ALWAYS_LOCAL forbids it."
            )
    
    # If TIER_2 or TIER_3, any engine is acceptable
    
    return engine, conv.get('command')
```

**Privacy Tier Decision Matrix:**

| Privacy Tier | Allowed Engines | Action if Cloud Needed |
|--------------|-----------------|------------------------|
| TIER_1_ALWAYS_LOCAL | Local only (Pandoc, FFmpeg, ImageMagick, etc.) | **ERROR: PrivacyViolation** |
| TIER_2_PREFER_LOCAL | All (local preferred) | Use cloud with warning |
| TIER_3_CLOUD_OK | All (any order) | Use cloud without warning |

**Decision points:**
- ✅ Engine is local and privacy tier allows it → STEP 4 (EXECUTE)
- ✅ Engine is cloud and tier allows it → STEP 4 (EXECUTE)
- ❌ Engine is cloud but tier forbids → PRIVACY_VIOLATION ERROR

---

### Step 4: EXECUTE CONVERSION

```python
def execute_conversion(engine, command, input_path, output_path, timeout_seconds=300):
    """Run the shell command"""
    
    # Substitute paths into command
    cmd = command.format(input=input_path, output=output_path)
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout_seconds
        )
        
        if result.returncode != 0:
            raise ConversionFailed(
                f"Engine {engine} failed with code {result.returncode}: {result.stderr}"
            )
        
        return result.stdout, result.stderr
    
    except subprocess.TimeoutExpired:
        raise TimeoutError(f"Conversion exceeded {timeout_seconds}s")
```

**Example execution:**

```bash
# Engine: pandoc
# Command template: pandoc {input} -t markdown -o {output}
# Actual command executed:
pandoc /Users/acebless/Documents/document.docx -t markdown -o /Users/acebless/Documents/document.md

# Result:
# ✅ returncode = 0 → Success
# ❌ returncode ≠ 0 → ConversionFailed
# ⏱️  timeout exceeded → TimeoutError
```

**Decision points:**
- ✅ returncode = 0 → STEP 6 (QA)
- ❌ returncode ≠ 0 → CONVERSION_FAILED ERROR
- ⏱️  timeout → TIMEOUT_ERROR

---

### Step 5: FALLBACK (No registry entry found)

Triggered when STEP 2 finds no conversion path.

```python
def fallback_conversion(from_format, to_format, privacy_tier):
    """Attempt conversion without registry entry"""
    
    # Is this a KNOWN LIMITATION?
    kill_list = load_kill_list()  # _INFRASTRUCTURE/KILL-LIST.md
    if (from_format, to_format) in kill_list['known_impossible_conversions']:
        raise ConversionNotPossible(
            f"Conversion {from_format} → {to_format} is impossible. "
            "See [[KILL-LIST|KILL-LIST.md]] for details."
        )
    
    # Try cloud fallback
    if privacy_tier == "TIER_1_ALWAYS_LOCAL":
        raise PrivacyViolation(
            f"No local engine for {from_format} → {to_format}, "
            "and TIER_1_ALWAYS_LOCAL forbids cloud. "
            "Either: (1) add to FILE_FORMAT_REGISTRY.yaml, "
            "(2) use TIER_2 or TIER_3, or (3) find alternative approach."
        )
    
    # TIER_2 or TIER_3: try cloud
    logger.warning(f"Using CloudConvert fallback for {from_format} → {to_format}")
    return "cloudconvert"
```

**Decision points:**
- ✅ Known impossible → Log to [[KILL-LIST|KILL-LIST.md]]
- ✅ TIER_2/TIER_3 → Try CloudConvert/Zamzar API
- ❌ TIER_1_ALWAYS_LOCAL → PrivacyViolation ERROR

---

### Step 6: QUALITY ASSURANCE

```python
def quality_assurance(input_path, output_path):
    """Validate conversion output"""
    
    checks = []
    
    # Check 1: Output exists and is readable
    if not os.path.exists(output_path):
        return "FAIL"
    
    # Check 2: File size is reasonable
    input_size = os.path.getsize(input_path)
    output_size = os.path.getsize(output_path)
    
    if output_size == 0:
        return "FAIL"
    
    ratio = output_size / input_size if input_size > 0 else 1
    
    # Warn if suspiciously compressed or expanded
    if ratio < 0.1 or ratio > 10.0:
        checks.append("WARN")
    else:
        checks.append("PASS")
    
    # Check 3: Spot-check content (if text)
    # (Not implemented in pseudocode, but would validate first 100 lines)
    
    # Summary
    if "FAIL" in checks:
        return "FAIL"
    elif "WARN" in checks:
        return "WARN"
    else:
        return "PASS"
```

**Attestation levels:**
- ✅ **PASS** — All checks passed, output is valid
- ⚠️ **WARN** — Conversion succeeded but output size suspicious (e.g., 20x compression)
- ❌ **FAIL** — Output file missing, empty, or corrupted

---

## 3. DECISION TREE FLOWCHART

```
                            START
                              ↓
                    ┌─────────────────┐
                    │  STEP 1:        │
                    │  VALIDATE       │
                    │  INPUT          │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  File exists?   │
                    │  Format detect? │
                    │  Tier valid?    │
                    └────┬────────┬───┘
                         │        │
                    NO ◄─┘        └─► YES
                     │                 │
                ┌─────▼─────┐     ┌────▼──────────┐
                │   ERROR:  │     │  STEP 2:      │
                │ FileNotFound │ │ LOAD REGISTRY │
                └───────────┘     └────┬──────────┘
                                       │
                                ┌──────▼──────┐
                                │ Find conv   │
                                │ path?       │
                                └──┬───────┬──┘
                                   │       │
                            FOUND ◄┘       └─► NOT FOUND
                              │                 │
                        ┌─────▼─────────┐   ┌──▼──────────┐
                        │  STEP 3:      │   │ STEP 5:     │
                        │  SELECT       │   │ FALLBACK    │
                        │  ENGINE       │   └──┬───────┬──┘
                        └──┬────────┬───┘      │       │
                           │        │     POSSIBLE  IMPOSSIBLE
                        ✅ │        │ ❌  │       │
                           │    PRIVACY   │       │
                           │    VIOLATION │       │
                    ┌──────▼──────┐  │   │   ┌───▼──────┐
                    │  STEP 4:    │  │   │   │  ERROR:  │
                    │  EXECUTE    │  │   │   │  Not     │
                    │  CONVERSION │  │   │   │  Possible│
                    └──┬───────┬──┘  │   │   └──────────┘
                       │       │     │   │
                    OK │ ERROR │     │   └──────┐
                       │       │     │          │
        ┌──────┐   ┌───▼─┐ ┌──▼───┐│          │
        │STEP6:│   │✅   │ │ ❌   ││          │
        │ QA   │   │PASS │ │FAIL  ││          │
        └──┬───┘   └─────┘ └──────┘└──────────┘
           │
    ┌──────▼──────────┐
    │ RETURN RESULT   │
    │ (PASS/WARN/FAIL)│
    └─────────────────┘
```

---

## 4. DECISION MATRIX BY FORMAT CLASS

### DOCUMENTS (.md, .docx, .pdf, .html)

```
FROM → TO       Engine      Local?  Cost    Privacy    Command
------          -------     ------  -----   --------   -------
.docx → .md     pandoc      ✅      FREE    Local      pandoc input.docx -t markdown -o output.md
.md → .pdf      pandoc      ✅      FREE    Local      pandoc input.md -o output.pdf
.md → .docx     pandoc      ✅      FREE    Local      pandoc input.md -t docx -o output.docx
.html → .md     pandoc      ✅      FREE    Local      pandoc input.html -t markdown -o output.md
.html → .pdf    wkhtmltopdf ✅      FREE    Local      wkhtmltopdf input.html output.pdf
.pdf → .txt     pdftotext   ✅      FREE    Local      pdftotext input.pdf output.txt
```

**Privacy Tier Implications:**
- TIER_1: ✅ All local, safe to convert any document
- TIER_2: ✅ Same (all local)
- TIER_3: ✅ Same

---

### IMAGES (.png, .jpg, .webp, .svg)

```
FROM → TO           Engine          Local?  Cost    Command
------              ------          ------  -----   -------
.jpg → .png         imagemagick     ✅      FREE    convert input.jpg output.png
.png → .webp        imagemagick     ✅      FREE    convert input.png -quality 80 output.webp
.svg → .png         imagemagick     ✅      FREE    convert -background white input.svg output.png
.gif → .png         imagemagick     ✅      FREE    convert input.gif output.png
.bmp → .png         imagemagick     ✅      FREE    convert input.bmp output.png
```

**Privacy Tier Implications:**
- TIER_1: ✅ Assume all images local (rarely sensitive)
- TIER_2/3: ✅ Same

---

### VIDEO/AUDIO (.mp4, .mov, .mp3, .wav, .webm)

```
FROM → TO       Engine      Local?  Cost    Command
------          -------     ------  -----   -------
.mov → .mp4     ffmpeg      ✅      FREE    ffmpeg -i input.mov -c:v h264 -c:a aac output.mp4
.mkv → .mp4     ffmpeg      ✅      FREE    ffmpeg -i input.mkv -c:v h264 -c:a aac output.mp4
.mp4 → .gif     ffmpeg      ✅      FREE    ffmpeg -i input.mp4 -vf 'scale=480:-1' -r 10 output.gif
.mp3 → .wav     ffmpeg      ✅      FREE    ffmpeg -i input.mp3 -c:a pcm_s16le output.wav
.m4a → .mp3     ffmpeg      ✅      FREE    ffmpeg -i input.m4a -c:a libmp3lame output.mp3
```

**Privacy Tier Implications:**
- TIER_1: ⚠️ Video/audio may contain sensitive information (screencasts, recordings)
- TIER_2: ✅ Prefer local FFmpeg
- TIER_3: ✅ Local acceptable

---

### DATA (.csv, .json, .xlsx, .parquet)

```
FROM → TO           Engine      Local?  Cost    Command
------              ------      ------  -----   -------
.csv → .json        duckdb      ✅      FREE    duckdb "COPY (SELECT * FROM read_csv(...)) TO output.json"
.csv → .parquet     duckdb      ✅      FREE    duckdb "COPY (SELECT * FROM read_csv(...)) TO output.parquet"
.xlsx → .csv        libreoffice ✅      FREE    libreoffice --headless --convert-to csv input.xlsx
.xlsx → .json       duckdb      ✅      FREE    duckdb "COPY (SELECT * FROM read_excel(...)) TO output.json"
.json → .csv        duckdb      ✅      FREE    duckdb "COPY (SELECT * FROM read_json(...)) TO output.csv"
```

**Privacy Tier Implications:**
- TIER_1: ❌ DATA almost always needs TIER_1 (may contain PII, customer records, financial data)
- TIER_2: ⚠️ OK if internal/anonymized
- TIER_3: Only for public datasets

---

### OCR/SCANNED (.pdf scanned → .pdf searchable → .md)

```
FROM → TO                   Engine      Local?  Cost    Command
------                      -------     ------  -----   -------
.pdf (scanned) → .pdf (searchable)   ocrmypdf   ✅      FREE    ocrmypdf input.pdf output.pdf
.pdf (searchable) → .txt   pdftotext   ✅      FREE    pdftotext input.pdf output.txt
.png/.jpg → .txt           tesseract   ✅      FREE    tesseract input.png output
```

**Privacy Tier Implications:**
- TIER_1: ⚠️ Scanned contracts/documents need TIER_1 (very sensitive)
- TIER_2/3: OK for published materials

---

## 5. ERROR HANDLING BY TYPE

### ConversionNotPossible

```
Reason: No conversion path found in registry + not a known limitation
Action: Check [[KILL-LIST|KILL-LIST.md]] or add to FILE_FORMAT_REGISTRY.yaml
User Message: "No conversion from .custom → .weird found. Request to add to registry."
```

### PrivacyViolation

```
Reason: Conversion requires cloud engine but privacy_tier forbids it
Action: Suggest higher privacy tier OR add local engine to registry
User Message: "Cannot convert .sensitive → .target (requires CloudConvert, but TIER_1_ALWAYS_LOCAL). 
              Approve TIER_2 or add local engine to FILE_FORMAT_REGISTRY.yaml"
```

### FileNotFound

```
Reason: Input file doesn't exist or path is inaccessible
Action: Check file path and permissions
User Message: "Input file not found: /path/to/missing.docx"
```

### ConversionFailed

```
Reason: Engine crashed or produced invalid output (returncode ≠ 0)
Action: Check engine installation, logs, and command
User Message: "Engine pandoc failed with code 1: pandoc: unknown output format \"invalid\""
```

### TimeoutError

```
Reason: Conversion exceeded timeout_seconds (default 300s)
Action: Increase timeout or try quality_required='low'
User Message: "Conversion exceeded 300s timeout. Try quality_required='low' or larger timeout_seconds."
```

---

## 6. PRIVACY TIER GUIDANCE

**TIER_1_ALWAYS_LOCAL:**
- Contracts
- Financial records (invoices, bank statements, tax returns)
- Customer data (PII, health records, addresses)
- Source code
- Credentials (API keys, passwords)
- Proprietary information
- Screencasts/recordings of sensitive content

**TIER_2_PREFER_LOCAL:**
- Internal business documents
- Draft reports and emails
- Research notes
- Design files
- Marketing materials (not published)

**TIER_3_CLOUD_OK:**
- Published content (websites, blogs)
- Public images (stock photos, published graphics)
- Marketing materials (published)
- Generic media (stock video, generic audio)

---

## 7. TESTING THE DECISION TREE

### Test Case 1: Document Conversion (TIER_1)

```
Input:     /Users/acebless/contract.docx
Target:    md
Tier:      TIER_1_ALWAYS_LOCAL
Verbose:   True

Decision Tree Log:
  1. ✅ Validate: File exists, format .docx detected, tier valid
  2. ✅ Registry: Found conversion DOCUMENT class, .docx → .md
  3. ✅ Select Engine: pandoc (local, free, TIER_1 approved)
  4. ✅ Execute: pandoc contract.docx -t markdown -o contract.md
  5. ✅ Output: contract.md (45 KB, reasonable)
  6. ✅ QA: PASS

Result: success=True, engine=pandoc, quality_attestation=PASS
```

### Test Case 2: Data Conversion (TIER_2, Cloud Fallback)

```
Input:     /Users/acebless/inventory.xlsx
Target:    parquet
Tier:      TIER_2_PREFER_LOCAL
Verbose:   True

Decision Tree Log:
  1. ✅ Validate: File exists, format .xlsx detected, tier valid
  2. ✅ Registry: Found conversion DATA class, .xlsx → .parquet
  3. ✅ Select Engine: duckdb (local, free, TIER_2 approved)
  4. ✅ Execute: duckdb "COPY (SELECT * FROM read_excel(...)) TO output.parquet"
  5. ✅ Output: inventory.parquet (12 MB)
  6. ✅ QA: PASS

Result: success=True, engine=duckdb, quality_attestation=PASS
```

### Test Case 3: Impossible Conversion (TIER_1)

```
Input:     /Users/acebless/proprietary.xyz
Target:    json
Tier:      TIER_1_ALWAYS_LOCAL
Verbose:   True

Decision Tree Log:
  1. ✅ Validate: File exists, format .xyz detected, tier valid
  2. ❌ Registry: No conversion found for .xyz → .json
  3. FALLBACK: Check known_impossible_conversions — [(.xyz, .json) not found]
  4. FALLBACK: Try cloud? — TIER_1_ALWAYS_LOCAL forbids cloud
  5. ❌ PrivacyViolation

Result: success=False, error=PrivacyViolation
         Message: "No local engine for .xyz → .json, and TIER_1_ALWAYS_LOCAL forbids cloud."
```

---

## 8. INTEGRATION WITH OMNIROUTE

When an agent calls the MCP tool:

```
Agent → OmniRoute FastMCP → file_conversion_service.py → DECISION TREE → Engine
  │                                                            │
  └─ Result logged to conversion_audit table in PostgreSQL ───┘
```

Monitor conversions:

```sql
SELECT engine_used, COUNT(*) as count, AVG(conversion_time_seconds) as avg_time
FROM conversion_audit
WHERE timestamp > NOW() - INTERVAL '24 hours'
GROUP BY engine_used
ORDER BY count DESC;

-- Example output:
-- engine_used  | count | avg_time
-- pandoc       |   45  |  0.34
-- ffmpeg       |   12  |  2.45
-- imagemagick  |   89  |  0.21
-- duckdb       |   23  |  1.12
```

---

**Status:** ✅ COMPLETE | **Authority:** CP-027 | **Last Updated:** 2026-09-06
