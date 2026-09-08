#!/usr/bin/env python3
"""
File Conversion Service — FastMCP Tool

Converts files between formats using local-first engines (Pandoc, FFmpeg, ImageMagick, etc.)
with automatic decision tree and privacy tier enforcement.

Authority: CP-027 (Infrastructure Control Plane)
Updated: 2026-09-06
"""

import os
import json
import subprocess
import logging
from pathlib import Path
from typing import Optional, Dict, List, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import yaml
import psycopg2
from fastmcp import Server

# Logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Paths
REGISTRY_PATH = Path("/Users/acebless/Documents/The Company/Company Brain/_REGISTRIES/CANONICAL/FILE_FORMAT_REGISTRY.yaml")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "changeme")
DB_NAME = os.getenv("POSTGRES_DB", "company_brain")
DB_PORT = int(os.getenv("POSTGRES_PORT", "5432"))

# Initialize MCP
mcp = Server("file-conversion-service")

# ============================================================================
# Data Structures
# ============================================================================

@dataclass
class ConversionResult:
    """Result of a file conversion operation"""
    success: bool
    input_path: str
    output_path: str
    input_format: str
    target_format: str
    engine_used: str
    command_executed: str
    conversion_time_seconds: float
    output_file_size_bytes: int
    quality_attestation: str  # PASS, WARN, FAIL
    error_message: Optional[str] = None
    decision_tree_log: List[str] = None

    def to_dict(self) -> Dict:
        return asdict(self)


# ============================================================================
# Conversion Errors
# ============================================================================

class ConversionError(Exception):
    """Base conversion error"""
    pass

class ConversionNotPossible(ConversionError):
    """No known conversion path"""
    pass

class PrivacyViolation(ConversionError):
    """File requires cloud upload but privacy tier forbids it"""
    pass

class FileNotFoundError(ConversionError):
    """Input file doesn't exist"""
    pass

class ConversionFailed(ConversionError):
    """Engine crashed or produced invalid output"""
    pass

class TimeoutError(ConversionError):
    """Conversion exceeded timeout"""
    pass


# ============================================================================
# Registry Management
# ============================================================================

def load_registry() -> Dict[str, Any]:
    """Load FILE_FORMAT_REGISTRY.yaml"""
    if not REGISTRY_PATH.exists():
        raise FileNotFoundError(f"Registry not found: {REGISTRY_PATH}")

    with open(REGISTRY_PATH, 'r') as f:
        data = yaml.safe_load(f)

    logger.info(f"✅ Registry loaded: {len(data.get('CANONICAL_FORMATS', {}))} format classes")
    return data


def find_conversion_path(registry: Dict, from_format: str, to_format: str) -> Optional[Dict]:
    """
    Find conversion path in registry.
    Returns conversion spec or None if not found.
    """
    canonical = registry.get("CANONICAL_FORMATS", {})

    # Search through each format class
    for class_name, class_spec in canonical.items():
        conversions = class_spec.get("conversions", [])
        for conv in conversions:
            if conv.get("from") == f".{from_format}" or conv.get("from") == from_format:
                if conv.get("to") == f".{to_format}" or conv.get("to") == to_format or "to" not in conv:
                    return conv

    return None


# ============================================================================
# Decision Tree
# ============================================================================

class DecisionTree:
    """Conversion decision tree"""

    def __init__(self, registry: Dict, verbose: bool = False):
        self.registry = registry
        self.verbose = verbose
        self.log = []

    def _log(self, msg: str):
        """Log decision step"""
        self.log.append(msg)
        if self.verbose:
            logger.debug(f"[DT] {msg}")

    def select_engine(
        self,
        input_format: str,
        target_format: str,
        privacy_tier: str,
        quality_required: str
    ) -> str:
        """
        Run decision tree to select best engine.
        Returns engine name (pandoc, ffmpeg, imagemagick, etc.)
        """
        self._log(f"STEP 1: Validate inputs")
        self._log(f"  Input: .{input_format}, Target: .{target_format}, Privacy: {privacy_tier}")

        # Find conversion path
        self._log(f"STEP 2: Load registry and find conversion path")
        conv_path = find_conversion_path(self.registry, input_format, target_format)

        if not conv_path:
            self._log(f"  ❌ No conversion path found")
            if privacy_tier == "TIER_1_ALWAYS_LOCAL":
                raise ConversionNotPossible(
                    f"No conversion path from .{input_format} to .{target_format}. "
                    "Cannot use cloud (TIER_1_ALWAYS_LOCAL). Add to FILE_FORMAT_REGISTRY.yaml"
                )
            else:
                self._log(f"  ℹ️  Fallback: Try CloudConvert/Zamzar")
                return "cloudconvert"  # fallback

        self._log(f"  ✅ Path found: {conv_path.get('engine')}")

        # Select engine by priority
        self._log(f"STEP 3: Select engine by priority")
        engine = conv_path.get("engine", "unknown")
        cost = conv_path.get("cost", "unknown")

        # Privacy tier enforcement
        if privacy_tier == "TIER_1_ALWAYS_LOCAL":
            local_engines = ["pandoc", "ffmpeg", "imagemagick", "duckdb", "libreoffice", "tesseract", "ocrmypdf"]
            if engine not in local_engines:
                self._log(f"  ❌ Engine {engine} is not local (privacy violation)")
                raise PrivacyViolation(
                    f"Conversion requires cloud engine {engine}, but TIER_1_ALWAYS_LOCAL forbids it."
                )

        self._log(f"  ✅ Engine selected: {engine} (cost: {cost})")
        return engine

    def get_decision_log(self) -> List[str]:
        return self.log


# ============================================================================
# Engine Executors
# ============================================================================

class EngineExecutor:
    """Execute conversion commands for various engines"""

    @staticmethod
    def execute_command(command: str, timeout: int = 300) -> (int, str, str):
        """Execute shell command and return (returncode, stdout, stderr)"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            raise TimeoutError(f"Command exceeded {timeout}s timeout: {command}")

    @staticmethod
    def pandoc(input_path: str, output_path: str, from_fmt: str, to_fmt: str) -> str:
        """Pandoc conversion"""
        cmd = f"pandoc '{input_path}' -t {to_fmt} -o '{output_path}'"
        return cmd

    @staticmethod
    def ffmpeg(input_path: str, output_path: str, from_fmt: str, to_fmt: str) -> str:
        """FFmpeg conversion"""
        # Default to h264/aac for video
        if to_fmt == "mp4":
            cmd = f"ffmpeg -i '{input_path}' -c:v h264 -c:a aac '{output_path}' -y"
        elif to_fmt == "gif":
            cmd = f"ffmpeg -i '{input_path}' -vf 'scale=480:-1' -r 10 '{output_path}' -y"
        else:
            cmd = f"ffmpeg -i '{input_path}' '{output_path}' -y"
        return cmd

    @staticmethod
    def imagemagick(input_path: str, output_path: str, from_fmt: str, to_fmt: str) -> str:
        """ImageMagick conversion"""
        if from_fmt == "svg":
            cmd = f"convert -background white '{input_path}' '{output_path}'"
        else:
            cmd = f"convert '{input_path}' '{output_path}'"
        return cmd

    @staticmethod
    def libreoffice(input_path: str, output_path: str, from_fmt: str, to_fmt: str) -> str:
        """LibreOffice conversion"""
        output_dir = str(Path(output_path).parent)
        cmd = f"libreoffice --headless --convert-to {to_fmt} --outdir '{output_dir}' '{input_path}'"
        return cmd

    @staticmethod
    def duckdb(input_path: str, output_path: str, from_fmt: str, to_fmt: str) -> str:
        """DuckDB conversion for data formats"""
        if from_fmt == "csv" and to_fmt == "json":
            cmd = f"""duckdb <<EOF
COPY (SELECT * FROM read_csv('{input_path}'))
TO '{output_path}' (FORMAT JSON);
EOF"""
        elif from_fmt == "csv" and to_fmt == "parquet":
            cmd = f"""duckdb <<EOF
COPY (SELECT * FROM read_csv('{input_path}'))
TO '{output_path}' (FORMAT PARQUET);
EOF"""
        else:
            cmd = f"duckdb 'SELECT * FROM read_{from_fmt}(\"{input_path}\");'"
        return cmd

    @staticmethod
    def tesseract(input_path: str, output_path: str, from_fmt: str, to_fmt: str) -> str:
        """Tesseract OCR (image -> text)"""
        # Output path should be without extension for tesseract
        output_no_ext = str(Path(output_path).with_suffix(''))
        cmd = f"tesseract '{input_path}' '{output_no_ext}'"
        return cmd

    @staticmethod
    def ocrmypdf(input_path: str, output_path: str, from_fmt: str, to_fmt: str) -> str:
        """OCRmyPDF (scanned PDF -> searchable PDF)"""
        cmd = f"ocrmypdf '{input_path}' '{output_path}'"
        return cmd


# ============================================================================
# Quality Assurance
# ============================================================================

class QualityAssurance:
    """Post-conversion quality checks"""

    @staticmethod
    def check_file_size(input_path: str, output_path: str) -> (bool, str):
        """
        Check if output file size is reasonable.
        Returns (is_valid, message)
        """
        try:
            input_size = os.path.getsize(input_path)
            output_size = os.path.getsize(output_path)

            if output_size == 0:
                return False, "Output file is empty (0 bytes)"

            ratio = output_size / input_size if input_size > 0 else 1

            # Allow 0.1x to 10x size ratio
            if 0.1 <= ratio <= 10.0:
                return True, f"File size OK (ratio: {ratio:.2f}x)"
            elif ratio < 0.1:
                return False, f"Output suspiciously small (ratio: {ratio:.2f}x)"
            else:
                return False, f"Output suspiciously large (ratio: {ratio:.2f}x)"
        except Exception as e:
            return False, f"Size check failed: {str(e)}"

    @staticmethod
    def check_output_exists(output_path: str) -> (bool, str):
        """Check if output file exists and is readable"""
        if not os.path.exists(output_path):
            return False, "Output file does not exist"
        if not os.path.isfile(output_path):
            return False, "Output path is not a file"
        return True, "Output file exists"

    @staticmethod
    def run_checks(input_path: str, output_path: str) -> str:
        """
        Run all QA checks.
        Returns attestation: PASS, WARN, or FAIL
        """
        checks = []

        # Check 1: Output exists
        exists, msg = QualityAssurance.check_output_exists(output_path)
        checks.append((exists, msg))
        if not exists:
            return "FAIL"

        # Check 2: File size
        size_ok, msg = QualityAssurance.check_file_size(input_path, output_path)
        checks.append((size_ok, msg))

        # Summary
        failures = sum(1 for ok, _ in checks if not ok)
        if failures == 0:
            return "PASS"
        elif failures == 1:
            return "WARN"
        else:
            return "FAIL"


# ============================================================================
# MCP Tool
# ============================================================================

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
    """
    Convert a file from one format to another using optimal engine.

    Args:
        input_path: Full path to input file (e.g., /path/to/document.docx)
        target_format: Target format without dot (e.g., "md", "pdf", "mp4")
        privacy_tier: One of TIER_1_ALWAYS_LOCAL, TIER_2_PREFER_LOCAL, TIER_3_CLOUD_OK
        quality_required: One of "low", "medium", "high"
        output_path: Full path to output file. If None, auto-generated.
        timeout_seconds: Max execution time (default 300s)
        verbose: Return detailed logs

    Returns:
        Dict with conversion result
    """
    start_time = datetime.now()
    dt_log = []

    try:
        # Validate input
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")

        # Detect input format
        input_format = Path(input_path).suffix.lstrip('.')
        if not input_format:
            raise ConversionError(f"Cannot detect format from filename: {input_path}")

        # Auto-generate output path if needed
        if not output_path:
            output_path = str(Path(input_path).with_suffix(f".{target_format}"))

        # Load registry
        registry = load_registry()

        # Run decision tree
        dt = DecisionTree(registry, verbose=verbose)
        engine = dt.select_engine(input_format, target_format, privacy_tier, quality_required)
        dt_log = dt.get_decision_log()

        # Build command
        executor = EngineExecutor()
        method = getattr(executor, engine, None)
        if not method:
            raise ConversionError(f"Unknown engine: {engine}")

        command = method(input_path, output_path, input_format, target_format)

        logger.info(f"🔄 Executing: {command}")

        # Execute conversion
        returncode, stdout, stderr = executor.execute_command(command, timeout_seconds)

        if returncode != 0:
            raise ConversionFailed(f"Engine {engine} failed with code {returncode}: {stderr}")

        # Quality assurance
        qa = QualityAssurance()
        quality_attestation = qa.run_checks(input_path, output_path)

        # Calculate time
        conversion_time = (datetime.now() - start_time).total_seconds()
        output_size = os.path.getsize(output_path)

        # Log to database
        try:
            _log_conversion(
                input_path, output_path, input_format, target_format,
                engine, privacy_tier, "success", conversion_time, None
            )
        except Exception as db_err:
            logger.warning(f"Failed to log conversion: {db_err}")

        result = ConversionResult(
            success=True,
            input_path=input_path,
            output_path=output_path,
            input_format=input_format,
            target_format=target_format,
            engine_used=engine,
            command_executed=command,
            conversion_time_seconds=conversion_time,
            output_file_size_bytes=output_size,
            quality_attestation=quality_attestation,
            error_message=None,
            decision_tree_log=dt_log
        )

        logger.info(f"✅ Conversion successful: {output_path} ({quality_attestation})")
        return result.to_dict()

    except Exception as e:
        conversion_time = (datetime.now() - start_time).total_seconds()
        error_msg = str(e)

        # Log failure to database
        try:
            _log_conversion(
                input_path, output_path or "",
                Path(input_path).suffix.lstrip('.'),
                target_format,
                "unknown", privacy_tier, "failed", conversion_time, error_msg
            )
        except Exception as db_err:
            logger.warning(f"Failed to log error: {db_err}")

        result = ConversionResult(
            success=False,
            input_path=input_path,
            output_path=output_path or "",
            input_format=Path(input_path).suffix.lstrip('.'),
            target_format=target_format,
            engine_used="none",
            command_executed="",
            conversion_time_seconds=conversion_time,
            output_file_size_bytes=0,
            quality_attestation="FAIL",
            error_message=error_msg,
            decision_tree_log=dt_log
        )

        logger.error(f"❌ Conversion failed: {error_msg}")
        return result.to_dict()


# ============================================================================
# Database Logging
# ============================================================================

def _log_conversion(
    input_path: str,
    output_path: str,
    input_format: str,
    target_format: str,
    engine_used: str,
    privacy_tier: str,
    status: str,
    conversion_time: float,
    error_message: Optional[str]
):
    """Log conversion to audit table"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO conversion_audit
            (input_path, input_format, target_format, engine_used, privacy_tier, status, conversion_time_seconds, error_message)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            input_path, input_format, target_format, engine_used,
            privacy_tier, status, conversion_time, error_message
        ))

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        logger.warning(f"Database logging failed (non-critical): {e}")


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    logger.info("🚀 File Conversion Service started")
    logger.info(f"Registry path: {REGISTRY_PATH}")
    logger.info(f"Database: {DB_HOST}:{DB_PORT}/{DB_NAME}")

    # Run MCP server
    import asyncio
    asyncio.run(mcp.run(transport="stdio"))
