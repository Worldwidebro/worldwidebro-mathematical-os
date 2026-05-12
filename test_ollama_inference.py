#!/usr/bin/env python3
"""
Diagnostic: Test Ollama inference for a single repo
Helps identify why populate_repos_metadata.py returned no inferred data
"""

import os
import json
import re
import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://100.87.214.70:11434")

def test_ollama_connection():
    """Test basic connection to Ollama"""
    logger.info("=" * 80)
    logger.info("OLLAMA DIAGNOSTIC TEST")
    logger.info("=" * 80)
    logger.info(f"Testing Ollama at: {OLLAMA_URL}")

    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json()
            logger.info(f"✓ Ollama is running. Available models: {len(models.get('models', []))}")
            for model in models.get('models', [])[:3]:
                logger.info(f"  - {model.get('name')}")
            return True
        else:
            logger.error(f"✗ Ollama returned status {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        logger.error(f"✗ Ollama timeout at {OLLAMA_URL}")
        return False
    except requests.exceptions.ConnectionError as e:
        logger.error(f"✗ Cannot connect to Ollama: {e}")
        return False
    except Exception as e:
        logger.error(f"✗ Unexpected error: {e}")
        return False

def test_ollama_inference():
    """Test inference on a sample repo"""
    logger.info("\nTesting Ollama inference...")

    repo_name = "stripe"
    description = "Payment processing platform"

    prompt = f"""Analyze this software repository and provide structured metadata:

Repository: {repo_name}
Description: {description}

Provide JSON with these fields:
{{
  "purpose": "one-line purpose (what does this solve?)",
  "capabilities": ["array", "of", "technical capabilities"],
  "integration_effort": "low|medium|high|very_high",
  "estimated_integration_days": <int days to integrate>,
  "cost_estimate": "free|$1K-5K|$5K-20K|$20K+",
  "startup_complexity": "simple|moderate|complex|very_complex",
  "business_use_cases": ["array", "of", "business problems it solves"],
  "stack": ["technology", "stack", "languages"],
  "maturity": "experimental|beta|production|mature"
}}

Return ONLY valid JSON, no markdown code blocks."""

    try:
        logger.info(f"Sending inference request to Ollama...")
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": "qwen2.5:32b",
                "prompt": prompt,
                "stream": False,
                "temperature": 0.3
            },
            timeout=60  # 60 second timeout for Ollama
        )

        logger.info(f"Response status: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            response_text = result.get("response", "").strip()
            logger.info(f"Raw response length: {len(response_text)} chars")
            logger.info(f"First 200 chars: {response_text[:200]}")

            # Try to extract JSON
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                try:
                    metadata = json.loads(json_match.group())
                    logger.info(f"✓ JSON extracted successfully!")
                    logger.info(f"  Purpose: {metadata.get('purpose')}")
                    logger.info(f"  Capabilities: {metadata.get('capabilities')}")
                    logger.info(f"  Integration effort: {metadata.get('integration_effort')}")
                    return True
                except json.JSONDecodeError as e:
                    logger.error(f"✗ JSON parsing failed: {e}")
                    return False
            else:
                logger.error(f"✗ No JSON found in response")
                return False
        else:
            logger.error(f"✗ Ollama returned {response.status_code}: {response.text[:200]}")
            return False

    except requests.exceptions.Timeout:
        logger.error(f"✗ Ollama inference timeout (60s)")
        return False
    except Exception as e:
        logger.error(f"✗ Inference error: {e}")
        return False

if __name__ == "__main__":
    if test_ollama_connection():
        test_ollama_inference()
    else:
        logger.error("\nCannot proceed - Ollama is not accessible")
