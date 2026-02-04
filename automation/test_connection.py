#!/usr/bin/env python3
"""
Quick test script for Zoho API connection.
Usage: python3 test_connection.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from zoho_client import ZohoClient

def main():
    print("=" * 50)
    print("Zoho API Connection Test")
    print("=" * 50)

    try:
        print("\n1. Loading credentials...")
        client = ZohoClient()
        print("   OK - Credentials loaded")

        print("\n2. Testing Deals module...")
        deals_result = client.get_deals(per_page=5)
        deals = deals_result.get("data", [])
        print(f"   OK - Can read deals! Found {len(deals)} sample deals:")
        for deal in deals[:3]:
            name = deal.get('Deal_Name', 'Unknown')
            stage = deal.get('Stage', 'Unknown')
            amount = deal.get('Amount') or 0
            print(f"      - {name} | {stage} | RM {amount:,.0f}")

        print("\n3. Testing pagination (page 2)...")
        page2 = client.get_deals(page=2, per_page=5)
        deals2 = page2.get("data", [])
        print(f"   OK - Pagination works. Page 2 has {len(deals2)} deals")

        print("\n4. Counting total deals...")
        total = 0
        page = 1
        while True:
            result = client.get_deals(page=page, per_page=200)
            data = result.get("data", [])
            if not data:
                break
            total += len(data)
            page += 1
            if page > 50:  # Safety limit
                break
        print(f"   OK - Total deals accessible: {total}")

        print("\n" + "=" * 50)
        print("ALL TESTS PASSED!")
        print("Zoho API ready for Kaizen Architecture")
        print("=" * 50)
        print("\nNote: COQL queries need ZohoCRM.coql.READ scope.")
        print("We'll use pagination + Python filtering instead.")
        return True

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
