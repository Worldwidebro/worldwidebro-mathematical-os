#!/usr/bin/env python3
"""
Revenue Attribution Pipeline
Tracks venture revenue back to agents, bases, and OpCos for attribution and performance metrics
"""

import uuid
from datetime import datetime
from typing import Dict, Optional

class RevenueAttributionPipeline:
    """End-to-end revenue attribution from transaction to dashboard"""

    def __init__(self, venture_mapping: Dict, agent_routing: Dict, cbp_registry: Dict):
        """Initialize with mapping data"""
        self.ventures = venture_mapping
        self.agents = agent_routing
        self.bases = cbp_registry
        self.transactions = []

    def capture_transaction(
        self,
        venture_id: str,
        amount_usd: float,
        agent_id: Optional[str] = None,
        transaction_type: str = "primary"
    ) -> Dict:
        """Step 1: Capture transaction from venture system"""

        transaction = {
            "transaction_id": str(uuid.uuid4()),
            "venture_id": venture_id,
            "amount_usd": amount_usd,
            "agent_id": agent_id,
            "timestamp": datetime.utcnow().isoformat(),
            "transaction_type": transaction_type,
            "status": "captured"
        }
        return transaction

    def attribute_to_base(self, transaction: Dict) -> Dict:
        """Step 3: Lookup venture → base mapping"""

        venture_id = transaction["venture_id"]
        if venture_id not in self.ventures:
            transaction["error"] = f"Venture {venture_id} not found in mapping"
            return transaction

        venture = self.ventures[venture_id]
        transaction["base_id"] = venture.get("base_id")
        transaction["domain"] = venture.get("domain")
        transaction["status"] = "attributed_to_base"

        return transaction

    def attribute_to_opco(self, transaction: Dict) -> Dict:
        """Step 5: Lookup base → domain → OpCo"""

        base_id = transaction.get("base_id")
        if not base_id:
            transaction["error"] = "No base_id for OpCo attribution"
            return transaction

        if base_id not in self.bases:
            transaction["error"] = f"Base {base_id} not in registry"
            return transaction

        base = self.bases[base_id]
        # OpCo would come from org structure (simplified here)
        opco_mapping = {
            "29-OPERATIONS": "OPCO-001",  # Operations OpCo
            "58-LOGISTICS": "OPCO-005",   # Logistics OpCo
            "54-FINANCIAL": "OPCO-010",   # Financial OpCo
        }

        domain = base.get("domain")
        transaction["opco_id"] = opco_mapping.get(domain, "OPCO-000")
        transaction["status"] = "attributed_to_opco"

        return transaction

    def attribute_to_agent(self, transaction: Dict) -> Dict:
        """Step 2: Assign to agent (explicit or backfill from base)"""

        agent_id = transaction.get("agent_id")
        if agent_id:
            transaction["agent_attribution"] = "explicit"
            return transaction

        # Backfill: base → primary agent
        base_id = transaction.get("base_id")
        if not base_id:
            transaction["agent_id"] = None
            transaction["agent_attribution"] = "unattributed"
            return transaction

        if base_id not in self.agents:
            transaction["agent_id"] = None
            transaction["agent_attribution"] = "base_not_found"
            return transaction

        agent = self.agents[base_id]
        transaction["agent_id"] = agent.get("primary_agent")
        transaction["agent_attribution"] = "backfilled"
        transaction["status"] = "attributed_to_agent"

        return transaction

    def execute_pipeline(self, transaction: Dict) -> Dict:
        """Execute full attribution pipeline"""

        # Step 1: Capture (already done)
        # Step 2: Attribute to agent
        transaction = self.attribute_to_agent(transaction)
        # Step 3: Attribute to base
        transaction = self.attribute_to_base(transaction)
        # Step 5: Attribute to OpCo
        transaction = self.attribute_to_opco(transaction)

        # Mark as complete
        if "error" not in transaction:
            transaction["status"] = "recorded"

        self.transactions.append(transaction)
        return transaction

    def aggregate_by_venture(self) -> Dict:
        """Aggregate: transactions by venture"""

        aggregated = {}
        for txn in self.transactions:
            if txn.get("status") == "recorded":
                venture = txn["venture_id"]
                if venture not in aggregated:
                    aggregated[venture] = {
                        "venture_id": venture,
                        "total_revenue": 0,
                        "transaction_count": 0,
                        "agents": set(),
                        "status": "verified"
                    }
                aggregated[venture]["total_revenue"] += txn["amount_usd"]
                aggregated[venture]["transaction_count"] += 1
                if txn.get("agent_id"):
                    aggregated[venture]["agents"].add(txn["agent_id"])

        # Convert sets to lists for JSON serialization
        for v in aggregated.values():
            v["agents"] = list(v["agents"])

        return aggregated

    def aggregate_by_base(self) -> Dict:
        """Aggregate: transactions by base"""

        aggregated = {}
        for txn in self.transactions:
            if txn.get("status") == "recorded":
                base = txn.get("base_id")
                if base not in aggregated:
                    aggregated[base] = {
                        "base_id": base,
                        "total_revenue": 0,
                        "transaction_count": 0,
                        "ventures": set(),
                        "status": "verified"
                    }
                aggregated[base]["total_revenue"] += txn["amount_usd"]
                aggregated[base]["transaction_count"] += 1
                aggregated[base]["ventures"].add(txn["venture_id"])

        for b in aggregated.values():
            b["ventures"] = list(b["ventures"])

        return aggregated

    def generate_dashboard_report(self) -> Dict:
        """Generate real-time revenue dashboard report"""

        by_venture = self.aggregate_by_venture()
        by_base = self.aggregate_by_base()

        total_revenue = sum(txn["amount_usd"] for txn in self.transactions if txn.get("status") == "recorded")
        total_transactions = len([t for t in self.transactions if t.get("status") == "recorded"])
        failed_transactions = len([t for t in self.transactions if "error" in t])

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "summary": {
                "total_revenue": total_revenue,
                "total_transactions": total_transactions,
                "failed_transactions": failed_transactions,
                "success_rate": (total_transactions / (total_transactions + failed_transactions) * 100) if (total_transactions + failed_transactions) > 0 else 0
            },
            "by_venture": by_venture,
            "by_base": by_base,
            "status": "live"
        }

# ==================================================
# EXAMPLE USAGE (Testing)
# ==================================================

def test_pipeline():
    """Test revenue attribution pipeline"""

    # Mock data
    ventures = {
        "OPS-001": {"base_id": "B291", "domain": "29-OPERATIONS"},
        "LT-005": {"base_id": "B581", "domain": "58-LOGISTICS"},
        "CALLCENTER": {"base_id": "B291", "domain": "29-OPERATIONS"},
    }

    agents = {
        "B291": {"primary_agent": "Operations Manager Agent"},
        "B581": {"primary_agent": "Logistics Operations Agent"},
    }

    bases = {
        "B291": {"domain": "29-OPERATIONS"},
        "B581": {"domain": "58-LOGISTICS"},
    }

    pipeline = RevenueAttributionPipeline(ventures, agents, bases)

    # Simulate transactions
    print("🔄 Simulating revenue transactions...\n")

    # Transaction 1: OPS-001 with explicit agent
    txn1 = pipeline.capture_transaction(
        venture_id="OPS-001",
        amount_usd=2500,
        agent_id="agent-staffing-001"
    )
    result1 = pipeline.execute_pipeline(txn1)
    print(f"✅ Transaction 1: {result1['venture_id']} ${result1['amount_usd']}")
    print(f"   → Base: {result1.get('base_id')}, Agent: {result1.get('agent_id')}")

    # Transaction 2: LT-005 without explicit agent (will backfill)
    txn2 = pipeline.capture_transaction(
        venture_id="LT-005",
        amount_usd=1800
    )
    result2 = pipeline.execute_pipeline(txn2)
    print(f"\n✅ Transaction 2: {result2['venture_id']} ${result2['amount_usd']}")
    print(f"   → Base: {result2.get('base_id')}, Agent (backfilled): {result2.get('agent_id')}")

    # Transaction 3: CALLCENTER
    txn3 = pipeline.capture_transaction(
        venture_id="CALLCENTER",
        amount_usd=3200
    )
    result3 = pipeline.execute_pipeline(txn3)
    print(f"\n✅ Transaction 3: {result3['venture_id']} ${result3['amount_usd']}")
    print(f"   → Base: {result3.get('base_id')}, Agent (backfilled): {result3.get('agent_id')}")

    # Generate dashboard report
    print("\n" + "=" * 50)
    dashboard = pipeline.generate_dashboard_report()

    print(f"\n📊 REVENUE DASHBOARD REPORT")
    print(f"   Total Revenue: ${dashboard['summary']['total_revenue']:.2f}")
    print(f"   Transactions: {dashboard['summary']['total_transactions']}")
    print(f"   Success Rate: {dashboard['summary']['success_rate']:.1f}%")

    print(f"\n💰 By Venture:")
    for venture_id, data in dashboard['by_venture'].items():
        print(f"   {venture_id}: ${data['total_revenue']:.2f} ({data['transaction_count']} txns)")

    print(f"\n🏢 By Base:")
    for base_id, data in dashboard['by_base'].items():
        print(f"   {base_id}: ${data['total_revenue']:.2f} ({data['transaction_count']} txns, {len(data['ventures'])} ventures)")

    print("\n✅ Pipeline test complete")

if __name__ == '__main__':
    test_pipeline()
