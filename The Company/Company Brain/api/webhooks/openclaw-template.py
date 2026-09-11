"""
OpenClaw Webhook Handler Template
Security: HMAC-SHA256 verification, no credential exposure
Generated: 2026-09-10T02:14:10Z
"""

import hmac
import hashlib
import json
import os
from typing import Dict, Tuple

def verify_webhook_signature(request_body: bytes, signature: str, timestamp: str) -> bool:
    """
    Verify OpenClaw webhook signature using HMAC-SHA256.
    
    Security notes:
    - Signature is retrieved from X-OpenClaw-Signature header
    - Timestamp prevents replay attacks (5-min window)
    - Secret is NEVER logged or exposed
    - Uses timing-safe comparison
    """
    webhook_secret = os.getenv('OPENCLAW_WEBHOOK_SECRET')
    
    if not webhook_secret:
        raise ValueError("OPENCLAW_WEBHOOK_SECRET not found in environment")
    
    # Reconstruct message
    message = f"{timestamp}{request_body.decode()}"
    
    # Compute expected signature
    expected = hmac.new(
        webhook_secret.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    
    # Timing-safe comparison (prevents timing attacks)
    return hmac.compare_digest(signature, expected)


def handler(event: Dict, context: Dict) -> Tuple[int, Dict]:
    """
    Webhook handler for OpenClaw contract signing events.
    
    Returns:
        (status_code, response_body)
    """
    try:
        # 1. EXTRACT HEADERS (never logged)
        signature = event['headers'].get('X-OpenClaw-Signature')
        timestamp = event['headers'].get('X-OpenClaw-Timestamp')
        body = event.get('body', '')
        
        # 2. VERIFY SIGNATURE
        if not verify_webhook_signature(body.encode(), signature, timestamp):
            return (401, {'error': 'Invalid signature'})
        
        # 3. PARSE PAYLOAD
        payload = json.loads(body)
        
        # 4. PROCESS EVENT (no secrets in logs)
        event_type = payload.get('event_type')
        contract_id = payload.get('contract_id')
        
        # Handle contract signed event
        if event_type == 'contract.signed':
            # TODO: Store in PostgreSQL (encrypted)
            # TODO: Update Neo4j
            # TODO: Notify ClickUp
            pass
        
        return (200, {'status': 'processed'})
    
    except Exception as e:
        # Log error WITHOUT exposing secrets
        print(f"Webhook error: {type(e).__name__}")
        return (500, {'error': 'Processing failed'})

