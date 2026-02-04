#!/usr/bin/env python3
"""
Quick test script for Zoho API connection.
Run this to verify credentials are working.

Usage:
    python test_connection.py
"""

import sys
from pathlib import Path

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from zoho_client import ZohoClient

def main():
    print("=" * 50)
    print("Zoho API Connection Test")
    print("=" * 50)

    try:
        # Initialize client
        print("\n1. Loading credentials...")
        client = ZohoClient()
        print("   OK - Credentials loaded")

        # Test deals access
        print("\n2. Testing Deals module...")
        deals_result = client.get_deals(per_page=5)
        deals = deals_result.get("data", [])
        print(f"   OK - Can read deals! Found {len(deals)} sample deals:")
        for deal in deals[:3]:
            name = deal.get('Deal_Name', 'Unknown')
            stage = deal.get('Stage', 'Unknown')
            amount = deal.get('Amount', 0)
            print(f"      - {name} | {stage} | RM {amount:,.0f}")

        # Test search
        print("\n3. Testing search (large deals >50K)...")
        search_result = client.search_deals(
            criteria="(Amount:greater_than:50000)",
        )
        large_deals = search_result.get("data", [])
        print(f"   OK - Search working. Found {len(large_deals)} large deals")

        # Test COQL
        print("\n4. Testing COQL query...")
        coql_result = client.coql_query(
            "SELECT Deal_Name, Amount, Stage FROM Deals LIMIT 3"
        )
        coql_deals = coql_result.get("data", [])
        print(f"   OK - COQL working. Returned {len(coql_deals)} records")

        print("\n" + "=" * 50)
        print("ALL TESTS PASSED!")
        print("Zoho API ready for Kaizen Architecture")
        print("=" * 50)
        return True

    except Exception as e:
        print(f"\nERROR: {e}")
        print("\nTroubleshooting:")
        print("  1. Check .env file has correct credentials")
        print("  2. Ensure refresh token hasn't been revoked")
        print("  3. Verify API scopes in Zoho console")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
