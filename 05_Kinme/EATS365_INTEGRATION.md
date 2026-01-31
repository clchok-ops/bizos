# Eats365 Integration Guide (Kinme)

> Step-by-step to connect Eats365 POS to BizOS

---

## Overview

Eats365 is a restaurant POS system with Open APIs for third-party integration. They have:
- **Developer Portal**: https://developer.eats365pos.com/
- **API Documentation**: https://docs.eats365pos.net/api (requires partner access)
- **Merchant Portal**: Where you redeem production tokens

---

## Step 1: Request Developer Access

Eats365 requires approval before API access. You need to:

1. **Email Eats365** at their developer contact (check developer portal)
2. **Include in your email**:
   ```
   Subject: API Integration Request - Kinme Restaurant

   Hi Eats365 Team,

   I'm requesting API access for integration purposes.

   Restaurant: Kinme
   Contact: [Your Name]
   Email: [Your Email]
   Phone: [Your Phone]

   Intended Use:
   - Pull daily sales data for financial reporting
   - Menu item performance analysis
   - Automated food cost tracking

   APIs Needed:
   - Orders/Transactions API
   - Menu API
   - Reports API (if available)

   Please advise on the process to obtain API credentials.

   Thank you,
   [Your Name]
   ```

3. **Wait for response** — They'll review and provide:
   - Partner Key
   - Demo restaurant account (sandbox)
   - Access to API documentation

---

## Step 2: Sandbox Development

Once approved:

1. **Log into Developer Portal**: https://developer.eats365pos.com/
2. **Get sandbox credentials**
3. **Access API docs** at https://docs.eats365pos.net/api
4. **Test endpoints** against demo restaurant

### Expected Available APIs

Based on Eats365's documentation, expect these API categories:

| API | Purpose | Use For |
|-----|---------|---------|
| **Menu API** | Menu items, prices, photos | Menu engineering analysis |
| **Orders API** | Transaction data | Daily sales tracking |
| **Reports API** | Aggregated data | Revenue summaries |
| **Inventory API** | Stock levels | Food cost tracking |

### Authentication

Likely OAuth2 or API Key based. Documentation will specify:
- Authorization header format
- Token refresh process
- Rate limits

---

## Step 3: Certification

Eats365 requires certification before production access:

1. **Build your integration** using sandbox
2. **Submit for review**
3. **Pass certification tests**
4. **Receive production credentials**

---

## Step 4: Production Token

Once certified:

1. Log into **Merchant Portal** (Kinme's Eats365 admin)
2. Go to **Integration** in left panel
3. Select **Developer Portal Application**
4. Click **Connect New App**
5. Enter the **Production Token** provided by Eats365
6. Click **Next** to complete

---

## Step 5: API Integration

### Base URL
```
https://api.eats365pos.net/v1/  (or as specified in docs)
```

### Sample Requests (Pseudocode)

**Get Daily Orders**:
```bash
curl -X GET "https://api.eats365pos.net/v1/orders" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "date_from": "2025-01-30",
    "date_to": "2025-01-30"
  }'
```

**Get Menu Items**:
```bash
curl -X GET "https://api.eats365pos.net/v1/menu/items" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Get Daily Report**:
```bash
curl -X GET "https://api.eats365pos.net/v1/reports/daily" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"date": "2025-01-30"}'
```

---

## Alternative: Manual Export (While Waiting for API)

If API approval takes time, use manual export:

### Daily Sales Export

1. Log into Eats365 Back Office
2. Go to **Reports** → **Sales Report**
3. Select date range (previous day)
4. Click **Export** → **CSV**
5. Save to: `BizOS/_INBOX/kinme_sales_YYYY-MM-DD.csv`

### Menu Export

1. Go to **Menu** → **All Items**
2. Export full menu with prices
3. Save to: `BizOS/05_Kinme/menu_export.csv`

### What to Include in Exports

**Sales Export** should have:
- Date/Time
- Order ID
- Item names and quantities
- Item prices
- Total amount
- Payment method
- Table number (if applicable)

**Menu Export** should have:
- Item name
- Category
- Selling price
- Item ID/SKU

---

## n8n Configuration

### Credential Setup

Once you have API access:

1. **n8n** → **Credentials** → **Add Credential**
2. Select **HTTP Header Auth**
3. Configure:
   ```
   Name: Eats365
   Header Name: Authorization
   Header Value: Bearer YOUR_PRODUCTION_TOKEN
   ```

### n8n Workflow: Kinme Daily Sales

```
Trigger (6 AM)
    → HTTP Request (GET /orders?date=yesterday)
    → Function (calculate metrics)
    → IF (threshold check)
        → True: Append flag to CONTEXT.md + Send alert
        → False: Continue
    → Write File (daily log)
```

**HTTP Request Node Settings**:
```json
{
  "method": "GET",
  "url": "https://api.eats365pos.net/v1/orders",
  "authentication": "predefinedCredentialType",
  "nodeCredentialType": "httpHeaderAuth",
  "queryParameters": {
    "date_from": "={{ $now.minus({days: 1}).toFormat('yyyy-MM-dd') }}",
    "date_to": "={{ $now.minus({days: 1}).toFormat('yyyy-MM-dd') }}"
  }
}
```

---

## Data Mapping

Map Eats365 data to Kinme metrics:

| Eats365 Field | BizOS Metric | Calculation |
|---------------|--------------|-------------|
| `orders.total` | Daily Revenue | Sum of all order totals |
| `orders.count` | Covers | Count of orders (or guests if available) |
| `order.items` | Item Sales | Count by item |
| `item.category` | Category Split | Group by food/beverage |

### Metrics Calculation

```javascript
// In n8n Function node
const orders = $input.first().json.orders;

const metrics = {
  date: $now.minus({days: 1}).toFormat('yyyy-MM-dd'),
  revenue: orders.reduce((sum, o) => sum + o.total, 0),
  covers: orders.length,
  avg_spend: 0,
  food_revenue: 0,
  beverage_revenue: 0,
  item_sales: {}
};

metrics.avg_spend = metrics.revenue / metrics.covers;

// Categorize by food vs beverage
orders.forEach(order => {
  order.items.forEach(item => {
    if (item.category === 'Beverage' || item.category === 'Sake' || item.category === 'Drinks') {
      metrics.beverage_revenue += item.price * item.quantity;
    } else {
      metrics.food_revenue += item.price * item.quantity;
    }

    // Track item sales
    metrics.item_sales[item.name] = (metrics.item_sales[item.name] || 0) + item.quantity;
  });
});

return { json: metrics };
```

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| 401 Unauthorized | Token expired/invalid | Refresh token or re-authenticate |
| 403 Forbidden | Not certified for production | Complete certification process |
| 429 Rate Limited | Too many requests | Add delays, check rate limits |
| Empty response | Wrong date format | Check API date format requirements |

---

## Timeline

| Step | Estimated Time |
|------|----------------|
| Request developer access | 1-2 days response |
| Sandbox development | 1-2 days |
| Certification | 3-5 days |
| Production setup | 1 day |
| **Total** | **1-2 weeks** |

**While waiting**: Use manual CSV exports to start building Kinme CFO toolkit.

---

## Contacts

- **Eats365 Developer Portal**: https://developer.eats365pos.com/
- **Eats365 Support**: https://support.eats365pos.com/
- **Eats365 Integration Docs**: https://support.eats365pos.com/integrations

---

## Next Steps

1. [ ] Send API access request email to Eats365
2. [ ] While waiting: Export sales CSV manually for past 30 days
3. [ ] While waiting: Export menu with prices
4. [ ] Drop exports in `_INBOX/` for Claude to process
5. [ ] Once API approved: Set up n8n workflow

---

*"Don't wait for perfect automation. Start with manual, automate when ready."*
