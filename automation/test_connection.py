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

        # Test connection
        print("\n2. Testing API connection...")
        result = client.get_users()
        users = result.get("users", [])
        print(f"   OK - Connected! Found {len(users)} users:")
        for user in users[:5]:  # Show first 5
            print(f"      - {user.get('full_name')} ({user.get('email')})")
        if len(users) > 5:
            print(f"      ... and {len(users) - 5} more")

        # Test deals access
        print("\n3. Testing Deals module...")
        deals_result = client.get_deals(per_page=5)
        deals = deals_result.get("data", [])
        print(f"   OK - Can read deals. Sample of {len(deals)}:")
        for deal in deals[:3]:
            print(f"      - {deal.get('Deal_Name')} (Stage: {deal.get('Stage')})")

        # Test COQL
        print("\n4. Testing COQL query...")
        coql_result = client.coql_query(
            "SELECT Deal_Name, Amount, Stage FROM Deals WHERE Amount > 50000 LIMIT 3"
        )
        coql_deals = coql_result.get("data", [])
        print(f"   OK - COQL working. Found {len(coql_deals)} large deals")

        print("\n" + "=" * 50)
        print("ALL TESTS PASSED!")
        print("Zoho API is ready for Kaizen Architecture")
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
