# BizOS Setup Playbook

> Step-by-step instructions to make everything operational

**Status**: Execute in order
**Estimated Time**: 2-4 hours total

---

## Table of Contents

1. [Pre-Flight Checklist](#1-pre-flight-checklist)
2. [EatPOS365 Setup (Kinme)](#2-eatpos365-setup-kinme)
3. [Zoho One Setup (Solartech/Hippos)](#3-zoho-one-setup-solartechhippos)
4. [Odoo Setup (WCI)](#4-odoo-setup-wci)
5. [IBKR Setup (Trading)](#5-ibkr-setup-trading)
6. [n8n Installation & Configuration](#6-n8n-installation--configuration)
7. [Building the Workflows](#7-building-the-workflows)
8. [Testing & Validation](#8-testing--validation)
9. [Go-Live Checklist](#9-go-live-checklist)

---

## 1. Pre-Flight Checklist

Before starting, confirm you have:

| Item | Status |
|------|--------|
| Admin access to EatPOS365 | ☐ |
| Admin access to Zoho One | ☐ |
| Admin access to Odoo | ☐ |
| IBKR account (paper trading ok) | ☐ |
| n8n account or self-hosted instance | ☐ |
| BizOS folder synced to iCloud | ☐ |

### Credentials Storage

**IMPORTANT**: Never store credentials in BizOS files. Use:
- n8n's built-in credential manager
- macOS Keychain
- 1Password/Bitwarden
- Environment variables

Create a secure note (outside BizOS) to track:
```
EatPOS365:
- API Key: [stored in n8n]
- Base URL: [stored in n8n]

Zoho:
- Client ID: [stored in n8n]
- Client Secret: [stored in n8n]
- Refresh Token: [stored in n8n]

Odoo:
- URL: [stored in n8n]
- Database: [stored in n8n]
- API Key: [stored in n8n]

IBKR:
- Account ID: [stored in n8n]
- API Key: [stored in n8n]
```

---

## 2. EatPOS365 Setup (Kinme)

### Step 2.1: Check API Availability

1. Log into EatPOS365 admin panel
2. Navigate to: **Settings** → **Integrations** or **API** or **Developer**
3. Look for:
   - REST API documentation
   - API key generation
   - Webhook configuration

**If API exists**, continue to Step 2.2.

**If NO API**, skip to [Step 2.5: Manual Export Fallback](#step-25-manual-export-fallback).

### Step 2.2: Generate API Credentials

1. In EatPOS365 admin:
   ```
   Settings → API/Integrations → Generate API Key
   ```

2. Note down:
   - **API Key**: `xxxxxxxxxxxxxxxxxxxxxxxx`
   - **API Secret** (if applicable): `xxxxxxxxxxxxxxxx`
   - **Base URL**: Usually `https://api.eatpos365.com/v1/` or similar

3. Store credentials securely (NOT in BizOS).

### Step 2.3: Test API Endpoints

Test using curl or Postman:

```bash
# Test authentication
curl -X GET "https://api.eatpos365.com/v1/me" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get transactions (adjust endpoint as per their docs)
curl -X GET "https://api.eatpos365.com/v1/transactions?date=2025-01-30" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get menu items
curl -X GET "https://api.eatpos365.com/v1/menu" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Step 2.4: Document Available Endpoints

Create a reference of what's available:

| Endpoint | Method | Purpose | Example Response |
|----------|--------|---------|------------------|
| `/transactions` | GET | Daily sales | `{transactions: [...]}` |
| `/transactions/{id}` | GET | Single transaction | `{id, items, total, ...}` |
| `/menu` | GET | Menu items | `{items: [...]}` |
| `/inventory` | GET | Stock levels | `{items: [...]}` |
| `/reports/daily` | GET | Daily summary | `{revenue, covers, ...}` |

**Note**: Actual endpoints depend on EatPOS365's API. Check their documentation.

### Step 2.5: Manual Export Fallback

If no API, set up manual export process:

1. **Daily Export** (do this each morning):
   ```
   EatPOS365 → Reports → Daily Sales → Export CSV
   ```

2. **Save to**: `BizOS/_INBOX/kinme_sales_YYYY-MM-DD.csv`

3. **Claude processes** the CSV when you start a session.

4. **Required fields in export**:
   - Date/Time
   - Transaction ID
   - Items sold (with quantities)
   - Item prices
   - Total amount
   - Payment method

### Step 2.6: EatPOS365 Credentials in n8n

Once you have API access:

1. Open n8n
2. Go to **Credentials** → **Add Credential**
3. Select **HTTP Header Auth** or **API Key**
4. Configure:
   ```
   Name: EatPOS365
   Header Name: Authorization
   Header Value: Bearer YOUR_API_KEY
   ```

---

## 3. Zoho One Setup (Solartech/Hippos)

### Step 3.1: Register API Client

1. Go to: https://api-console.zoho.com/
2. Click **Add Client**
3. Select **Self Client** (for server-to-server)
4. Fill in:
   - Client Name: `BizOS Integration`
   - Homepage URL: `https://yourdomain.com` (or placeholder)
   - Authorized Redirect URIs: `https://n8n.yourdomain.com/rest/oauth2-credential/callback`

5. Click **Create**

6. Note down:
   - **Client ID**: `1000.XXXXXXXXXXXXXXXXXX`
   - **Client Secret**: `xxxxxxxxxxxxxxxxxxxxxxxx`

### Step 3.2: Generate Refresh Token

**Option A: Using Self Client (Recommended)**

1. In API Console, click on your client
2. Go to **Generate Code** tab
3. Select scopes (check all that apply):
   ```
   ZohoCRM.modules.ALL
   ZohoCRM.settings.ALL
   ZohoInventory.fullaccess.all
   ZohoAnalytics.data.read
   ```

4. Select **Time Duration**: Choose longest available
5. Enter your **Zoho account email**
6. Click **Create**
7. Copy the **Authorization Code** (valid 1 minute!)

8. Immediately exchange for tokens:

```bash
curl -X POST "https://accounts.zoho.com/oauth/v2/token" \
  -d "grant_type=authorization_code" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "code=AUTHORIZATION_CODE_FROM_STEP_7"
```

9. Response contains:
   ```json
   {
     "access_token": "xxxx",
     "refresh_token": "xxxx",  // SAVE THIS - doesn't expire
     "expires_in": 3600
   }
   ```

### Step 3.3: Test Zoho CRM API

```bash
# Get all deals
curl -X GET "https://www.zohoapis.com/crm/v2/Deals" \
  -H "Authorization: Zoho-oauthtoken YOUR_ACCESS_TOKEN"

# Get all contacts
curl -X GET "https://www.zohoapis.com/crm/v2/Contacts" \
  -H "Authorization: Zoho-oauthtoken YOUR_ACCESS_TOKEN"

# Get inventory items
curl -X GET "https://inventory.zoho.com/api/v1/items" \
  -H "Authorization: Zoho-oauthtoken YOUR_ACCESS_TOKEN" \
  -H "organization_id: YOUR_ORG_ID"
```

### Step 3.4: Get Organization ID (for Inventory)

```bash
curl -X GET "https://inventory.zoho.com/api/v1/organizations" \
  -H "Authorization: Zoho-oauthtoken YOUR_ACCESS_TOKEN"
```

Note the `organization_id` from response.

### Step 3.5: Key Zoho Endpoints Reference

**CRM (Solartech/Hippos Sales)**:
| Endpoint | Purpose |
|----------|---------|
| `GET /crm/v2/Deals` | All deals in pipeline |
| `GET /crm/v2/Deals?criteria=(Stage:equals:Closed Won)` | Won deals |
| `GET /crm/v2/Contacts` | All contacts |
| `GET /crm/v2/Leads` | All leads |

**Inventory (Solartech/Hippos Stock)**:
| Endpoint | Purpose |
|----------|---------|
| `GET /inventory/v1/items` | All items |
| `GET /inventory/v1/items/{id}` | Single item |
| `GET /inventory/v1/inventoryadjustments` | Stock changes |
| `GET /inventory/v1/purchaseorders` | POs |

**Analytics**:
| Endpoint | Purpose |
|----------|---------|
| `POST /analytics/v1/{org_id}/{workspace}/data` | Custom queries |

### Step 3.6: Zoho Credentials in n8n

1. Go to **Credentials** → **Add Credential**
2. Select **Zoho CRM OAuth2 API** (built-in)
3. Configure:
   ```
   Client ID: [from Step 3.1]
   Client Secret: [from Step 3.1]
   ```
4. Click **Connect** and authorize

For Zoho Inventory, add separate credential:
1. **Credentials** → **Add Credential**
2. Select **HTTP Request** (with OAuth2)
3. Configure manually with refresh token flow

---

## 4. Odoo Setup (WCI)

### Step 4.1: Enable API Access

1. Log into Odoo as admin
2. Go to: **Settings** → **General Settings**
3. Enable **Developer Mode** (bottom of page)
4. Go to: **Settings** → **Users** → Select your user
5. Go to **Preferences** tab
6. Look for **API Key** section or **Password for API**

**Option A: API Key (Odoo 14+)**
- Generate API Key in user preferences
- Use this instead of password for API calls

**Option B: Password-based (older Odoo)**
- Use regular username/password
- Less secure but works

### Step 4.2: Get Connection Details

Note down:
- **URL**: `https://your-company.odoo.com` (or self-hosted URL)
- **Database**: Usually your company name
- **Username**: Your login email
- **API Key/Password**: From Step 4.1

### Step 4.3: Test Odoo XML-RPC

Odoo uses XML-RPC. Test with Python:

```python
import xmlrpc.client

url = "https://your-company.odoo.com"
db = "your-database"
username = "your-email@example.com"
password = "your-api-key"

# Authenticate
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
print(f"User ID: {uid}")

# Test query
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Get manufacturing orders
orders = models.execute_kw(db, uid, password,
    'mrp.production', 'search_read',
    [[['state', '=', 'confirmed']]],
    {'fields': ['name', 'product_id', 'product_qty', 'date_planned_start']}
)
print(orders)
```

### Step 4.4: Key Odoo Models Reference

**Manufacturing (MRP)**:
| Model | Purpose |
|-------|---------|
| `mrp.production` | Manufacturing orders |
| `mrp.bom` | Bills of materials |
| `mrp.workorder` | Work orders |

**Inventory**:
| Model | Purpose |
|-------|---------|
| `stock.quant` | Current stock levels |
| `stock.move` | Stock movements |
| `stock.picking` | Transfers |
| `product.product` | Products |

**Sales**:
| Model | Purpose |
|-------|---------|
| `sale.order` | Sales orders |
| `res.partner` | Customers/Vendors |

### Step 4.5: Useful Odoo Queries

```python
# Get all manufacturing orders
models.execute_kw(db, uid, password,
    'mrp.production', 'search_read',
    [[]],
    {'fields': ['name', 'product_id', 'product_qty', 'state', 'date_planned_start']}
)

# Get current stock levels
models.execute_kw(db, uid, password,
    'stock.quant', 'search_read',
    [[['location_id.usage', '=', 'internal']]],
    {'fields': ['product_id', 'quantity', 'location_id']}
)

# Get BOMs
models.execute_kw(db, uid, password,
    'mrp.bom', 'search_read',
    [[]],
    {'fields': ['product_tmpl_id', 'product_qty', 'bom_line_ids']}
)
```

### Step 4.6: Odoo Credentials in n8n

n8n doesn't have a native Odoo node, so use HTTP Request:

1. **Credentials** → **Add Credential**
2. Select **HTTP Request**
3. For XML-RPC, we'll build custom requests in workflows

Alternatively, install community Odoo node:
```bash
# In n8n
npm install n8n-nodes-odoo
```

---

## 5. IBKR Setup (Trading)

### Step 5.1: Choose API Method

| Method | Best For | Setup Complexity |
|--------|----------|------------------|
| **Client Portal API** | Simple queries, positions, P&L | Easy |
| **TWS API** | Full trading, real-time data | Medium |
| **Flex Web Service** | Reports, historical data | Easy |

**Recommendation**: Start with **Client Portal API** for monitoring.

### Step 5.2: Client Portal API Setup

1. Log into IBKR Account Management
2. Go to: **Settings** → **User Settings**
3. Find **API** section
4. Enable **Client Portal API**
5. Note your **Account ID**

### Step 5.3: Run the Gateway

Client Portal API requires a local gateway:

1. Download: https://www.interactivebrokers.com/en/trading/ib-api.php
2. Extract and run:
   ```bash
   # Navigate to extracted folder
   cd clientportal.gw

   # Start gateway
   ./bin/run.sh root/conf.yaml
   ```

3. Open browser: `https://localhost:5000`
4. Log in with IBKR credentials
5. Gateway is now running

### Step 5.4: Test Client Portal API

```bash
# Check authentication status
curl -k "https://localhost:5000/v1/api/iserver/auth/status"

# Get accounts
curl -k "https://localhost:5000/v1/api/portfolio/accounts"

# Get positions
curl -k "https://localhost:5000/v1/api/portfolio/{accountId}/positions/0"

# Get account summary
curl -k "https://localhost:5000/v1/api/portfolio/{accountId}/summary"
```

### Step 5.5: Key IBKR Endpoints

| Endpoint | Purpose |
|----------|---------|
| `GET /portfolio/accounts` | List accounts |
| `GET /portfolio/{acct}/positions/0` | Current positions |
| `GET /portfolio/{acct}/summary` | Account summary |
| `GET /portfolio/{acct}/ledger` | Cash balances |
| `GET /iserver/marketdata/history` | Historical prices |
| `POST /iserver/account/{acct}/orders` | Place order |

### Step 5.6: Flex Web Service (Alternative)

For automated reports without running gateway:

1. Log into Account Management
2. Go to: **Reports** → **Flex Queries**
3. Create new query:
   - Select data: Trades, Positions, Cash
   - Format: XML or CSV
   - Period: Daily

4. Note the **Query ID** and **Token**

5. Fetch report:
   ```bash
   # Request report
   curl "https://gdcdyn.interactivebrokers.com/Universal/servlet/FlexStatementService.SendRequest?t=YOUR_TOKEN&q=YOUR_QUERY_ID&v=3"

   # Returns reference code, then fetch:
   curl "https://gdcdyn.interactivebrokers.com/Universal/servlet/FlexStatementService.GetStatement?q=REFERENCE_CODE&t=YOUR_TOKEN&v=3"
   ```

### Step 5.7: IBKR Credentials in n8n

For Client Portal API (requires gateway running):
1. **Credentials** → **Add Credential**
2. Select **HTTP Request**
3. Configure:
   ```
   Name: IBKR Client Portal
   URL: https://localhost:5000
   ```
4. Add SSL handling for self-signed cert

For Flex Web Service:
1. Store token as environment variable or credential

---

## 6. n8n Installation & Configuration

### Step 6.1: Choose Deployment

| Option | Pros | Cons |
|--------|------|------|
| **n8n Cloud** | No maintenance, easy | Monthly cost, data on their servers |
| **Self-hosted (Docker)** | Full control, free | Maintenance, need server |
| **Self-hosted (npm)** | Lightweight | Less isolated |

**Recommendation**: Start with n8n Cloud for simplicity, migrate later if needed.

### Step 6.2: n8n Cloud Setup

1. Go to: https://n8n.io/
2. Sign up for account
3. Create new instance
4. Note your URL: `https://your-instance.app.n8n.cloud`

### Step 6.3: Self-Hosted (Docker)

```bash
# Create directory
mkdir n8n-docker && cd n8n-docker

# Create docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: "3.8"

services:
  n8n:
    image: n8nio/n8n
    restart: always
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=your-secure-password
      - N8N_HOST=your-domain.com
      - N8N_PORT=5678
      - N8N_PROTOCOL=https
      - WEBHOOK_URL=https://your-domain.com/
      - GENERIC_TIMEZONE=Asia/Singapore
    volumes:
      - n8n_data:/home/node/.n8n
      - /path/to/BizOS:/data/BizOS  # Mount BizOS folder

volumes:
  n8n_data:
EOF

# Start
docker-compose up -d
```

### Step 6.4: Connect n8n to BizOS Folder

**For n8n Cloud**:
You'll need to use cloud storage integration:

1. Move BizOS to Dropbox, Google Drive, or OneDrive
2. Use respective n8n nodes to read/write files

**For Self-hosted**:
Mount the folder in Docker (see docker-compose above), then use "Read/Write File" nodes with path `/data/BizOS/`.

**Alternative - iCloud via API**:
Complex setup, not recommended. Use Dropbox/OneDrive instead.

### Step 6.5: Install Community Nodes

In n8n:
1. Go to **Settings** → **Community Nodes**
2. Install:
   - `n8n-nodes-odoo` (if available)
   - Any other useful nodes

---

## 7. Building the Workflows

### Workflow 1: Kinme Daily Sales

**Trigger**: Schedule - Every day at 6:00 AM

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Schedule   │───►│  HTTP GET   │───►│  Function   │
│  Trigger    │    │  EatPOS365  │    │  Calculate  │
│  (6 AM)     │    │  /sales     │    │  Metrics    │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                   ┌─────────────────────────┤
                   │                         │
                   ▼                         ▼
            ┌─────────────┐           ┌─────────────┐
            │  IF: Check  │           │  Write File │
            │  Thresholds │           │  Daily Log  │
            └─────────────┘           └─────────────┘
                   │
          ┌────────┴────────┐
          ▼                 ▼
   ┌─────────────┐   ┌─────────────┐
   │  Threshold  │   │  No Issue   │
   │  Breached   │   │  (end)      │
   └─────────────┘   └─────────────┘
          │
          ▼
   ┌─────────────┐    ┌─────────────┐
   │  Append to  │───►│  Send       │
   │  CONTEXT.md │    │  Alert      │
   └─────────────┘    └─────────────┘
```

**n8n Node Configuration**:

**Node 1: Schedule Trigger**
```json
{
  "triggerTimes": {
    "item": [{ "hour": 6, "minute": 0 }]
  }
}
```

**Node 2: HTTP Request (EatPOS365)**
```json
{
  "method": "GET",
  "url": "https://api.eatpos365.com/v1/reports/daily",
  "authentication": "predefinedCredentialType",
  "nodeCredentialType": "httpHeaderAuth",
  "queryParameters": {
    "date": "={{ $now.minus({days: 1}).toFormat('yyyy-MM-dd') }}"
  }
}
```

**Node 3: Function (Calculate Metrics)**
```javascript
const data = $input.first().json;
const thresholds = {
  food_cost_max: 0.35,
  revenue_drop: 0.20
};

// Calculate metrics
const metrics = {
  date: $now.minus({days: 1}).toFormat('yyyy-MM-dd'),
  revenue: data.total_revenue,
  covers: data.total_covers,
  avg_spend: data.total_revenue / data.total_covers,
  food_cost_pct: data.food_cost / data.food_revenue,
  beverage_revenue: data.beverage_revenue,
  food_revenue: data.food_revenue
};

// Check thresholds
const flags = [];
if (metrics.food_cost_pct > thresholds.food_cost_max) {
  flags.push({
    type: 'COST',
    message: `Food cost hit ${(metrics.food_cost_pct * 100).toFixed(1)}% (threshold: ${thresholds.food_cost_max * 100}%)`
  });
}

return {
  json: {
    metrics,
    flags,
    hasFlags: flags.length > 0
  }
};
```

**Node 4: IF (Check for Flags)**
```json
{
  "conditions": {
    "boolean": [{
      "value1": "={{ $json.hasFlags }}",
      "value2": true,
      "operation": "equal"
    }]
  }
}
```

**Node 5: Write File (Daily Log)**
```json
{
  "fileName": "=/data/BizOS/05_Kinme/daily_logs/{{ $json.metrics.date }}.json",
  "fileContent": "={{ JSON.stringify($json.metrics, null, 2) }}"
}
```

**Node 6: Read File (CONTEXT.md)**
```json
{
  "filePath": "/data/BizOS/_CONTEXT.md"
}
```

**Node 7: Function (Append Flag)**
```javascript
const context = $input.first().json.data;
const flags = $('Function').first().json.flags;
const date = $now.toFormat('yyyy-MM-dd');

// Find flags table and append
let newContext = context;
flags.forEach(flag => {
  const newRow = `| ${date} | Kinme | ${flag.type} | ${flag.message} | Open |`;
  newContext = newContext.replace(
    '| — | — | — | No flags yet | — |',
    newRow
  );
});

return { json: { content: newContext } };
```

**Node 8: Write File (Update CONTEXT.md)**
```json
{
  "fileName": "/data/BizOS/_CONTEXT.md",
  "fileContent": "={{ $json.content }}"
}
```

**Node 9: Send Email (Alert)**
```json
{
  "fromEmail": "bizos@yourdomain.com",
  "toEmail": "chok@yourdomain.com",
  "subject": "[BizOS Alert] Kinme - Threshold Breached",
  "text": "={{ $('Function').first().json.flags.map(f => f.message).join('\\n') }}"
}
```

---

### Workflow 2: Weekly Context Rollup

**Trigger**: Schedule - Every Sunday at 9:00 PM

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Schedule   │───►│  Read       │───►│  Function   │
│  (Sun 9PM)  │    │ CONTEXT.md  │    │  Rollup     │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                                             ▼
                                      ┌─────────────┐
                                      │  Write      │
                                      │ CONTEXT.md  │
                                      └─────────────┘
                                             │
                                             ▼
                                      ┌─────────────┐
                                      │  Send       │
                                      │  Weekly     │
                                      │  Digest     │
                                      └─────────────┘
```

**Rollup Function**:
```javascript
const context = $input.first().json.data;
const now = $now.toFormat('yyyy-MM-dd');

// Update "Last Updated" timestamp
let updated = context.replace(
  /\*\*Last Updated\*\*: .*/,
  `**Last Updated**: ${now}`
);

// Update "Updated By"
updated = updated.replace(
  /\*\*Updated By\*\*: .*/,
  `**Updated By**: n8n (weekly rollup)`
);

// Clear resolved flags (keep only Open status)
// ... flag cleanup logic

return { json: { content: updated } };
```

---

### Workflow 3: Trading Daily Check

**Trigger**: Schedule - Every weekday at 4:00 PM (market close)

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Schedule   │───►│  HTTP GET   │───►│  Function   │
│  (4 PM M-F) │    │  IBKR       │    │  Calculate  │
└─────────────┘    │  Positions  │    │  Metrics    │
                   └─────────────┘    └─────────────┘
                                             │
                         ┌───────────────────┤
                         │                   │
                         ▼                   ▼
                  ┌─────────────┐     ┌─────────────┐
                  │  IF: Check  │     │  Append to  │
                  │  Drawdown   │     │  Journal    │
                  └─────────────┘     └─────────────┘
                         │
                ┌────────┴────────┐
                ▼                 ▼
         ┌─────────────┐   ┌─────────────┐
         │  Alert:     │   │  No Issue   │
         │  Drawdown   │   └─────────────┘
         │  Warning    │
         └─────────────┘
```

**IBKR Positions Request**:
```json
{
  "method": "GET",
  "url": "https://localhost:5000/v1/api/portfolio/{{ $credentials.accountId }}/positions/0",
  "options": {
    "allowSelfSignedCertificates": true
  }
}
```

**Metrics Calculation**:
```javascript
const positions = $input.first().json;
const thresholds = { max_drawdown: 0.05 };

let totalValue = 0;
let totalPnl = 0;

positions.forEach(p => {
  totalValue += p.mktValue;
  totalPnl += p.unrealizedPnl;
});

// You'd need to track high water mark separately
const highWaterMark = /* fetch from stored value */;
const drawdown = (highWaterMark - totalValue) / highWaterMark;

return {
  json: {
    date: $now.toFormat('yyyy-MM-dd'),
    totalValue,
    totalPnl,
    drawdown,
    exceedsThreshold: drawdown > thresholds.max_drawdown,
    positions: positions.map(p => ({
      symbol: p.contractDesc,
      qty: p.position,
      value: p.mktValue,
      pnl: p.unrealizedPnl
    }))
  }
};
```

---

### Workflow 4: Zoho Pipeline Check (Solartech/Hippos)

**Trigger**: Schedule - Every Monday at 8:00 AM

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Schedule   │───►│  Zoho CRM   │───►│  Function   │
│  (Mon 8AM)  │    │  Get Deals  │    │  Analyze    │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                                             ▼
                                      ┌─────────────┐
                                      │  Check      │
                                      │  Stalled    │
                                      │  Deals      │
                                      └─────────────┘
                                             │
                         ┌───────────────────┤
                         ▼                   ▼
                  ┌─────────────┐     ┌─────────────┐
                  │  Flag       │     │  Update     │
                  │  Issues     │     │  CONTEXT    │
                  └─────────────┘     └─────────────┘
```

**Zoho CRM Node**:
- Use built-in Zoho CRM node
- Operation: Get Many
- Resource: Deal
- Return All: true

**Stalled Deal Detection**:
```javascript
const deals = $input.all();
const now = new Date();
const stalledThreshold = 14; // days

const stalled = deals.filter(deal => {
  const lastActivity = new Date(deal.json.Modified_Time);
  const daysSinceActivity = (now - lastActivity) / (1000 * 60 * 60 * 24);
  return daysSinceActivity > stalledThreshold &&
         !['Closed Won', 'Closed Lost'].includes(deal.json.Stage);
});

return {
  json: {
    totalDeals: deals.length,
    stalledDeals: stalled.length,
    stalledList: stalled.map(d => ({
      name: d.json.Deal_Name,
      stage: d.json.Stage,
      value: d.json.Amount,
      lastActivity: d.json.Modified_Time
    }))
  }
};
```

---

### Workflow 5: WCI Production Check

**Trigger**: Schedule - Every Monday at 8:00 AM

This requires XML-RPC calls to Odoo. Use HTTP Request nodes:

**Authentication Node**:
```javascript
// First, authenticate to get uid
const xmlrpc = require('xmlrpc');
const client = xmlrpc.createSecureClient({
  host: 'your-company.odoo.com',
  port: 443,
  path: '/xmlrpc/2/common'
});

// This would need to be done via HTTP Request
// with properly formatted XML-RPC payload
```

**Alternative - Use Python Code Node**:
```python
import xmlrpc.client

url = "https://your-company.odoo.com"
db = "your-database"
username = "your-email"
password = "your-api-key"

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Get manufacturing orders
orders = models.execute_kw(db, uid, password,
    'mrp.production', 'search_read',
    [[['state', 'in', ['confirmed', 'progress']]]],
    {'fields': ['name', 'product_id', 'product_qty', 'date_planned_start']}
)

return orders
```

---

## 8. Testing & Validation

### Test Checklist

| System | Test | Expected Result | Status |
|--------|------|-----------------|--------|
| EatPOS365 | Pull yesterday's sales | JSON with transactions | ☐ |
| Zoho CRM | Pull all deals | Array of deal objects | ☐ |
| Zoho Inventory | Pull stock levels | Array of items | ☐ |
| Odoo | Pull MO list | Array of orders | ☐ |
| IBKR | Pull positions | Array of positions | ☐ |
| n8n → BizOS | Write test file | File appears in folder | ☐ |
| n8n → Email | Send test alert | Email received | ☐ |
| Kinme Workflow | Run manually | Daily log created | ☐ |
| Rollup Workflow | Run manually | CONTEXT.md updated | ☐ |

### Manual Test Each Workflow

1. In n8n, open workflow
2. Click **Execute Workflow** (manual run)
3. Check each node's output
4. Verify files created/updated
5. Verify alerts sent (if applicable)

### Validation Script

Create a test endpoint in n8n:

```javascript
// Webhook that tests all integrations
const results = {
  timestamp: new Date().toISOString(),
  tests: []
};

// Test EatPOS365
try {
  // ... API call
  results.tests.push({ system: 'EatPOS365', status: 'OK' });
} catch (e) {
  results.tests.push({ system: 'EatPOS365', status: 'FAIL', error: e.message });
}

// Test Zoho
// ... similar

// Test Odoo
// ... similar

// Test IBKR
// ... similar

return results;
```

---

## 9. Go-Live Checklist

### Before Activating Workflows

| Item | Status |
|------|--------|
| All API credentials tested and working | ☐ |
| All workflows tested manually | ☐ |
| Alert email/notification working | ☐ |
| BizOS folder accessible from n8n | ☐ |
| Thresholds reviewed and adjusted | ☐ |
| CONTEXT.md backed up | ☐ |

### Activation Order

1. **Week 1**: Activate Kinme Daily only
   - Monitor for issues
   - Verify daily logs created
   - Adjust thresholds if too sensitive

2. **Week 2**: Add Trading Daily (if IBKR ready)
   - Monitor drawdown calculations
   - Verify journal entries

3. **Week 3**: Add Zoho Pipeline Check
   - Verify deal data accuracy
   - Adjust stalled threshold if needed

4. **Week 4**: Add WCI Production Check
   - Verify Odoo data accuracy
   - Monitor for false alerts

5. **Week 5**: Activate Weekly Rollup
   - Full system operational
   - Review first automated rollup

### Post-Launch Monitoring

First 2 weeks, check daily:
- [ ] Workflows executed successfully
- [ ] No error notifications from n8n
- [ ] Files being created as expected
- [ ] CONTEXT.md being updated correctly
- [ ] Alerts appropriate (not too many/few)

### Troubleshooting Quick Reference

| Issue | Likely Cause | Fix |
|-------|--------------|-----|
| Workflow not running | Schedule misconfigured | Check timezone, cron expression |
| API error 401 | Token expired | Refresh OAuth token |
| API error 429 | Rate limited | Add delays between calls |
| File not created | Path wrong | Check mount/path configuration |
| Wrong data | API response changed | Update parsing logic |

---

## Quick Command Reference

### Test Commands

```bash
# Test EatPOS365
curl -X GET "https://api.eatpos365.com/v1/health" \
  -H "Authorization: Bearer $EATPOS_KEY"

# Test Zoho
curl -X GET "https://www.zohoapis.com/crm/v2/Deals" \
  -H "Authorization: Zoho-oauthtoken $ZOHO_TOKEN"

# Test Odoo (via Python)
python3 test_odoo.py

# Test IBKR (gateway must be running)
curl -k "https://localhost:5000/v1/api/iserver/auth/status"
```

### n8n CLI Commands

```bash
# Start n8n (npm install)
n8n start

# Start n8n (Docker)
docker-compose up -d

# View logs
docker-compose logs -f n8n

# Import workflow
n8n import:workflow --input=workflow.json

# Export workflow
n8n export:workflow --id=1 --output=workflow.json
```

---

## Support Resources

| System | Documentation |
|--------|---------------|
| EatPOS365 | Check their admin panel or contact support |
| Zoho API | https://www.zoho.com/crm/developer/docs/api/v2/ |
| Odoo API | https://www.odoo.com/documentation/16.0/developer/reference/external_api.html |
| IBKR API | https://interactivebrokers.github.io/cpwebapi/ |
| n8n | https://docs.n8n.io/ |

---

**End of Setup Playbook**
