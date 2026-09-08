---
id: FILE-CONVERSION-SERVICE-001
title: File Conversion Service — MCP Capability
scope: Company Brain (all agents, all systems)
authority: CP-027 (Infrastructure Control Plane)
updated: 2026-09-06
status: ACTIVE
---

# FILE CONVERSION SERVICE — MCP-Enabled Capability

[[STARTHERE]] | [[_REGISTRIES/CANONICAL/FILE_FORMAT_REGISTRY.yaml|FILE_FORMAT_REGISTRY]] | [[CLAUDE.md|Infrastructure Status]]

**Purpose:** Convert files between formats using local-first engines (FFmpeg, Pandoc, ImageMagick, etc.) with automatic decision tree and privacy tier enforcement.

**Authority:** CP-027 (Infrastructure Control Plane)

---

## 1. SERVICE ARCHITECTURE

```
┌─────────────────────────────────────────────────────────┐
│         Claude Code / Antigravity IDE                   │
│    (Agent requests file conversion)                     │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ↓
┌─────────────────────────────────────────────────────────┐
│         OmniRoute FastMCP Adapter                       │
│  (/Users/acebless/.omniroute/bin/antigravity-mcp.mjs)  │
│   (110 tools exposed; file_convert is one of them)     │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ↓
┌─────────────────────────────────────────────────────────┐
│    File Conversion Service (FastMCP Tool)              │
│  (_MCP/file_conversion_service.py)                      │
│                                                         │
│  1. Parse input format & target format                 │
│  2. Look up [[FILE_FORMAT_REGISTRY.yaml]]              │
│  3. Run conversion decision tree                       │
│  4. Select best engine (local free → cloud)           │
│  5. Execute conversion                                 │
│  6. Verify output & return                            │
└──────────────────┬──────────────────────────────────────┘
                   │
        ┌──────────┼──────────┬────────────────┐
        ↓          ↓          ↓                ↓
    PANDOC    IMAGEMAGICK  FFMPEG    DUCKDB/LIBREOFFICE
   (docs)     (images)     (video)   (data)
   (local)    (local)      (local)   (local)
```

---

## 2. MCP TOOL SPECIFICATION

### Tool Name
```
file_convert
```

### Function
```python
@mcp.tool()
def file_convert(
    input_path: str,
    target_format: str,
    privacy_tier: str = "TIER_2_PREFER_LOCAL",
    quality_required: str = "medium",
    output_path: Optional[str] = None,
    timeout_seconds: int = 300,
    verbose: bool = False
) -> ConversionResult:
    """
    Convert a file from one format to another using optimal engine.
    
    Args:
        input_path: Full path to input file (e.g., /path/to/document.docx)
        target_format: Target format without dot (e.g., "md", "pdf", "mp4")
        privacy_tier: One of TIER_1_ALWAYS_LOCAL, TIER_2_PREFER_LOCAL, TIER_3_CLOUD_OK
        quality_required: One of "low", "medium", "high" (affects engine selection)
        output_path: Full path to output file. If None, auto-generated in same dir.
        timeout_seconds: Max execution time (default 300s)
        verbose: Return detailed logs of decision tree execution
    
    Returns:
        ConversionResult:
            - success: bool
            - input_path: str
            - output_path: str
            - input_format: str
            - target_format: str
            - engine_used: str
            - command_executed: str
            - conversion_time_seconds: float
            - output_file_size_bytes: int
            - quality_attestation: str (PASS/WARN/FAIL)
            - error_message: Optional[str]
            - decision_tree_log: List[str] (if verbose=True)
    
    Raises:
        ConversionNotPossible: No known conversion path (check registry)
        PrivacyViolation: File would require cloud upload but tier forbids it
        FileNotFound: Input file doesn't exist
        ConversionFailed: Engine crashed or produced invalid output
        TimeoutError: Conversion exceeded timeout_seconds
    """
```

---

## 3. DECISION TREE ALGORITHM

Executed automatically by the service:

```python
DECISION_TREE = """
┌─ STEP 1: VALIDATE INPUT
│  ├─ File exists?
│  ├─ Format recognized?
│  ├─ Privacy tier valid?
│  └─ Target format valid?
│
├─ STEP 2: LOAD REGISTRY
│  └─ Fetch conversion path from FILE_FORMAT_REGISTRY.yaml
│     ├─ If found: STEP 3
│     └─ If NOT found: STEP 5 (FALLBACK)
│
├─ STEP 3: SELECT ENGINE
│  ├─ Priority 1: Local FREE engines (Pandoc, ImageMagick, FFmpeg, DuckDB, LibreOffice)
│  │  └─ If privacy_tier == TIER_1_ALWAYS_LOCAL, MUST use local
│  ├─ Priority 2: Local PAID engines (rarely)
│  ├─ Priority 3: Cloud engines (CloudConvert, Zamzar)
│  │  └─ Only if privacy_tier allows cloud
│  └─ Priority 4: Manual intervention (last resort)
│
├─ STEP 4: EXECUTE CONVERSION
│  ├─ Assemble command from registry
│  ├─ Run with timeout_seconds limit
│  ├─ Monitor for errors
│  └─ Return to STEP 6 (QA)
│
├─ STEP 5: FALLBACK (if no path found)
│  ├─ Is this a known limitation?
│  │  ├─ If yes: Log in [[KILL-LIST.md]] & return error
│  │  └─ If no: Try CloudConvert/Zamzar
│  └─ If privacy_tier forbids cloud: Return PrivacyViolation error
│
└─ STEP 6: QUALITY ASSURANCE
   ├─ File size reasonable? (0.1x to 10x original)
   ├─ Content spot-check (first 100 lines/1MB for spot-check)
   ├─ Metadata preserved where applicable
   ├─ No corruption/encoding errors
   └─ Return ConversionResult with attestation
"""
```

---

## 4. EXAMPLE USAGE

### From Claude Code Agent

```python
# Agent invokes MCP tool
result = await mcp.call_tool(
    "file_convert",
    input_path="/Users/acebless/Documents/contract.pdf",
    target_format="md",
    privacy_tier="TIER_1_ALWAYS_LOCAL",  # Never cloud upload
    quality_required="high",
    verbose=True
)

if result.success:
    print(f"✅ Converted to {result.output_path}")
    print(f"   Engine: {result.engine_used}")
    print(f"   Time: {result.conversion_time_seconds}s")
    print(f"   Quality: {result.quality_attestation}")
else:
    print(f"❌ Conversion failed: {result.error_message}")
```

### From Shell

```bash
# Via MCP CLI (if exposed)
omniroute mcp call file_convert \
  --input_path="/Users/acebless/Documents/slide.pptx" \
  --target_format="pdf" \
  --privacy_tier="TIER_2_PREFER_LOCAL" \
  --quality_required="high"

# Returns JSON:
{
  "success": true,
  "input_path": "/Users/acebless/Documents/slide.pptx",
  "output_path": "/Users/acebless/Documents/slide.pdf",
  "engine_used": "libreoffice",
  "conversion_time_seconds": 2.34,
  "quality_attestation": "PASS"
}
```

---

## 5. ENGINE COMMANDS REFERENCE

Built into the service (auto-selected by decision tree):

```python
ENGINES = {
    "pandoc": {
        "formats": ["md", "docx", "html", "latex", "epub", "rst"],
        "command": "pandoc {input} {options} -o {output}",
        "cost": "free",
        "privacy": "local",
        "conversions": {
            "docx_to_md": "pandoc {input} -t markdown -o {output}",
            "md_to_pdf": "pandoc {input} -o {output}",
            "md_to_docx": "pandoc {input} -t docx -o {output}",
            "html_to_md": "pandoc {input} -t markdown -o {output}",
        }
    },
    
    "ffmpeg": {
        "formats": ["mp4", "mov", "mkv", "webm", "mp3", "wav", "aac", "flac"],
        "command": "ffmpeg -i {input} {options} {output}",
        "cost": "free",
        "privacy": "local",
        "conversions": {
            "mov_to_mp4": "ffmpeg -i {input} -c:v h264 -c:a aac {output}",
            "mp4_to_gif": "ffmpeg -i {input} -vf 'scale=480:-1' -r 10 {output}",
            "mp3_to_wav": "ffmpeg -i {input} -c:a pcm_s16le {output}",
        }
    },
    
    "imagemagick": {
        "formats": ["png", "jpg", "webp", "gif", "tiff", "bmp", "svg"],
        "command": "convert {input} {options} {output}",
        "cost": "free",
        "privacy": "local",
        "conversions": {
            "jpg_to_png": "convert {input} {output}",
            "png_to_webp": "convert {input} -quality 80 {output}",
            "svg_to_png": "convert -background white {input} {output}",
        }
    },
    
    "duckdb": {
        "formats": ["csv", "json", "jsonl", "parquet", "xlsx"],
        "command": "duckdb",
        "cost": "free",
        "privacy": "local",
        "conversions": {
            "csv_to_json": "duckdb 'COPY (SELECT * FROM read_csv(\"{input}\")) TO \"{output}\" (FORMAT JSON);'",
            "csv_to_parquet": "duckdb 'COPY (SELECT * FROM read_csv(\"{input}\")) TO \"{output}\" (FORMAT PARQUET);'",
            "xlsx_to_csv": "duckdb 'COPY (SELECT * FROM read_excel(\"{input}\")) TO \"{output}\" (FORMAT CSV);'",
        }
    },
    
    "libreoffice": {
        "formats": ["xlsx", "docx", "pptx", "pdf", "odt"],
        "command": "libreoffice --headless --convert-to {format} {input}",
        "cost": "free",
        "privacy": "local",
        "conversions": {
            "docx_to_pdf": "libreoffice --headless --convert-to pdf {input}",
            "xlsx_to_csv": "libreoffice --headless --convert-to csv {input}",
            "pptx_to_pdf": "libreoffice --headless --convert-to pdf {input}",
        }
    },
    
    "tesseract": {
        "formats": ["txt"],  # OCR text extraction
        "command": "tesseract {input} {output}",
        "cost": "free",
        "privacy": "local",
        "conversions": {
            "png_to_txt": "tesseract {input} {output}",
            "jpg_to_txt": "tesseract {input} {output}",
        }
    },
    
    "ocrmypdf": {
        "formats": ["pdf"],  # Searchable PDF
        "command": "ocrmypdf {input} {output}",
        "cost": "free",
        "privacy": "local",
        "conversions": {
            "scanned_pdf_to_searchable_pdf": "ocrmypdf {input} {output}",
        }
    },
    
    "cloudconvert": {
        "formats": ["*"],  # 200+ formats
        "cost": "pay-per-use ($0.25-1.00/file)",
        "privacy": "cloud",
        "api": "https://api.cloudconvert.com/v2/convert",
        "conversions": "See CloudConvert docs"
    },
    
    "zamzar": {
        "formats": ["*"],  # 1,100+ formats
        "cost": "pay-per-use ($0.29-1.00/file)",
        "privacy": "cloud",
        "api": "https://www.zamzar.com/api/v1/convert",
        "conversions": "See Zamzar docs"
    }
}
```

---

## 6. PRIVACY TIER ENFORCEMENT

```python
PRIVACY_ENFORCEMENT = {
    "TIER_1_ALWAYS_LOCAL": {
        "allowed_engines": ["pandoc", "ffmpeg", "imagemagick", "duckdb", "libreoffice", "tesseract", "ocrmypdf"],
        "forbidden_engines": ["cloudconvert", "zamzar"],
        "error_if_no_local": "PrivacyViolation",
        "use_case": "Contracts, credentials, financial data, source code, PII"
    },
    
    "TIER_2_PREFER_LOCAL": {
        "allowed_engines": ["all"],
        "priority": ["local_free", "local_paid", "cloud"],
        "error_if_no_local": "Falls back to cloud with warning",
        "use_case": "Internal docs, research, business documents"
    },
    
    "TIER_3_CLOUD_OK": {
        "allowed_engines": ["all"],
        "priority": ["local_free", "cloud"],
        "error_if_no_local": "Uses cloud",
        "use_case": "Public content, published materials, non-sensitive images"
    }
}
```

---

## 7. ERROR HANDLING

Service returns structured errors:

```python
class ConversionError(Exception):
    """Base conversion error"""
    pass

class ConversionNotPossible(ConversionError):
    """No known conversion path exists for this format pair"""
    
class PrivacyViolation(ConversionError):
    """File type requires cloud upload but privacy tier forbids it"""
    
class FileNotFound(ConversionError):
    """Input file doesn't exist"""
    
class ConversionFailed(ConversionError):
    """Engine crashed or produced invalid output"""
    
class TimeoutError(ConversionError):
    """Conversion exceeded timeout_seconds"""
```

Example handling:

```python
try:
    result = await mcp.call_tool("file_convert", ...)
except PrivacyViolation:
    print("❌ Cannot convert: file too sensitive. Use TIER_2 or TIER_3 to enable cloud engines.")
except ConversionNotPossible:
    print("❌ No known conversion path. Add to FILE_FORMAT_REGISTRY.yaml or use web service.")
except TimeoutError:
    print("❌ Conversion took too long. Try quality_required='low' or split input.")
```

---

## 8. COST TRACKING & LOGGING

Service logs every conversion to local audit table:

```sql
-- Table: conversion_audit
CREATE TABLE conversion_audit (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMP DEFAULT NOW(),
    input_path TEXT NOT NULL,
    input_format TEXT NOT NULL,
    target_format TEXT NOT NULL,
    engine_used TEXT NOT NULL,
    privacy_tier TEXT,
    cost_cents INTEGER,  -- 0 for local, 25-100 for cloud
    success BOOLEAN,
    conversion_time_seconds FLOAT,
    error_message TEXT,
    agent_id TEXT,  -- Which agent requested conversion
    venture_id TEXT  -- Which venture/context
);

-- Example query: Cost per venture
SELECT venture_id, 
       SUM(cost_cents) / 100.0 as cost_usd,
       COUNT(*) as conversions
FROM conversion_audit
WHERE timestamp > NOW() - INTERVAL '30 days'
GROUP BY venture_id
ORDER BY cost_usd DESC;
```

---

## 9. MONITORING & OBSERVABILITY

Service emits metrics to OpenObserve:

```python
METRICS = {
    "file_conversion.requests_total": "Total conversion requests",
    "file_conversion.success_rate": "% successful conversions",
    "file_conversion.conversion_time_seconds": "Conversion duration histogram",
    "file_conversion.engine_usage": "Count by engine (pandoc, ffmpeg, etc.)",
    "file_conversion.privacy_tier_usage": "Count by privacy tier",
    "file_conversion.cost_usd_total": "Total cloud API spend",
    "file_conversion.error_rate": "% conversions that failed",
}

# Example OpenObserve query:
# SELECT timestamp, engine_used, conversion_time_seconds, success
# FROM file_conversion_logs
# WHERE timestamp > NOW() - INTERVAL '24 hours'
# ORDER BY conversion_time_seconds DESC LIMIT 50
```

---

## 10. INSTALLATION & SETUP

### 1. Install engines locally

```bash
brew install pandoc ffmpeg imagemagick duckdb libreoffice tesseract
pip install ocrmypdf fastmcp
```

### 2. Register service in FastMCP

File: `/Users/acebless/.venv/company-brain/lib/python3.12/site-packages/fastmcp_server.py`

```python
@mcp.tool()
def file_convert(
    input_path: str,
    target_format: str,
    privacy_tier: str = "TIER_2_PREFER_LOCAL",
    quality_required: str = "medium",
    output_path: Optional[str] = None,
    timeout_seconds: int = 300,
    verbose: bool = False
) -> Dict:
    """Convert files between formats using local-first engines."""
    # Implementation from _MCP/file_conversion_service.py
    pass
```

### 3. Restart Claude Code MCP

```bash
# Claude Code will auto-reload the MCP server
# Verify: curl http://localhost:20128/api/health
```

### 4. Test via Agent

```python
# In Claude Code:
result = await mcp.call_tool("file_convert", 
    input_path="/tmp/test.docx",
    target_format="md"
)
```

---

## 11. FUTURE ENHANCEMENTS

- [ ] Batch conversion support (`input_paths: List[str]`)
- [ ] Progress streaming for large files
- [ ] Parallel conversion (multiple files simultaneously)
- [ ] Format auto-detection (guess target format from intent)
- [ ] Web UI dashboard (conversion history, cost tracking)
- [ ] Scheduled conversions (convert on a cron schedule)
- [ ] Integration with Qdrant (index converted documents)
- [ ] Integration with Neo4j (track conversion lineage)

---

**Status:** ✅ READY FOR IMPLEMENTATION | **Authority:** CP-027 | **Last Updated:** 2026-09-06
