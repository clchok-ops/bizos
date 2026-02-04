#!/usr/bin/env python3
"""
Debug script to identify Zoho API issues.
"""

import os
import requests
from dotenv import load_dotenv

# Load credentials
load_dotenv()

CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")

print("=" * 60)
print("Zoho API Debug")
print("=" * 60)

# Step 1: Refresh token
print("\n1. Refreshing token...")
token_url = "https://accounts.zoho.com/oauth/v2/token"

response = requests.post(token_url, data={
    "grant_type": "refresh_token",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "refresh_token": REFRESH_TOKEN,
})

print(f"   Status: {response.status_code}")
token_data = response.json()
print(f"   Response: {token_data}")

if "access_token" not in token_data:
    print("\n   FAILED at token refresh!")
    exit(1)

access_token = token_data["access_token"]
api_domain = token_data.get("api_domain", "https://www.zohoapis.com")
print(f"   API Domain: {api_domain}")

# Step 2: Try different API versions and endpoints
print("\n2. Testing API endpoints...")

headers = {
    "Authorization": f"Zoho-oauthtoken {access_token}",
}

endpoints = [
    (f"{api_domain}/crm/v2/users", "v2 Users"),
    (f"{api_domain}/crm/v2/Deals", "v2 Deals"),
    (f"{api_domain}/crm/v3/users", "v3 Users"),
    (f"{api_domain}/crm/v3/Deals", "v3 Deals"),
    (f"{api_domain}/crm/v6/users", "v6 Users"),
    (f"{api_domain}/crm/v6/Deals", "v6 Deals"),
]

for url, label in endpoints:
    try:
        r = requests.get(url, headers=headers, params={"per_page": 1})
        print(f"   {label}: {r.status_code}")
        if r.status_code == 200:
            print(f"      SUCCESS! Use this version.")
            data = r.json()
            if "users" in data:
                print(f"      Found {len(data['users'])} users")
            elif "data" in data:
                print(f"      Found {len(data['data'])} records")
        elif r.status_code == 401:
            error = r.json() if r.text else {}
            print(f"      Error: {error.get('message', 'Unauthorized')}")
        else:
            print(f"      Response: {r.text[:100]}")
    except Exception as e:
        print(f"   {label}: ERROR - {e}")

print("\n" + "=" * 60)
