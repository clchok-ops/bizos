# BizOS Automation Scripts

Zoho API integration for Kaizen Architecture monitoring.

## Setup

```bash
# Install dependencies
pip install requests python-dotenv

# Test connection
python test_connection.py
```

## Files

| File | Purpose |
|------|---------|
| `zoho_client.py` | Core API client with retry logic |
| `test_connection.py` | Quick connection test |
| `.env` | Credentials (gitignored) |

## Usage

```python
from zoho_client import ZohoClient

client = ZohoClient()

# Get deals
deals = client.get_deals(criteria="Stage:equals:Qualification")

# COQL query
result = client.coql_query("""
    SELECT Deal_Name, Amount, Stage, Owner
    FROM Deals
    WHERE Amount > 50000
    ORDER BY Amount DESC
    LIMIT 10
""")

# Create alert task
client.create_task(
    subject="[KAIZEN] High-risk deal needs attention",
    priority="High",
    due_date="2026-02-05",
    related_to={"module": "Deals", "id": "123456"}
)
```

## Credentials

Stored in `.env` (never committed):
- `ZOHO_CLIENT_ID`
- `ZOHO_CLIENT_SECRET`
- `ZOHO_REFRESH_TOKEN`

Refresh token is permanent unless revoked in Zoho console.
