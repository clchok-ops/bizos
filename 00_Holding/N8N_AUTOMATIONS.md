# n8n Automation Architecture

> The brain that makes continuous improvement automatic

**Last Updated**: 2025-01-31
**Status**: Design phase

---

## Overview

n8n workflows handle three core functions:

1. **PULL** — Get data from source systems automatically
2. **MONITOR** — Watch for anomalies and threshold breaches
3. **UPDATE** — Keep CONTEXT.md current without manual intervention

```
┌─────────────────────────────────────────────────────────────────┐
│                         n8n WORKFLOWS                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│   │  Zoho   │    │  Odoo   │    │EatPOS365│    │  IBKR   │     │
│   │ (Solar/ │    │  (WCI)  │    │ (Kinme) │    │(Trading)│     │
│   │ Hippos) │    │         │    │         │    │         │     │
│   └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘     │
│        │              │              │              │           │
│        ▼              ▼              ▼              ▼           │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │              SCHEDULED DATA PULLS                        │  │
│   │   Daily: Sales, inventory levels, key metrics            │  │
│   │   Weekly: Full summaries, P&L snapshots                  │  │
│   └────────────────────────┬────────────────────────────────┘  │
│                            │                                    │
│                            ▼                                    │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │              THRESHOLD MONITORING                        │  │
│   │   Check against predefined thresholds                    │  │
│   │   Flag anomalies immediately                             │  │
│   └────────────────────────┬────────────────────────────────┘  │
│                            │                                    │
│              ┌─────────────┴─────────────┐                     │
│              ▼                           ▼                      │
│   ┌─────────────────────┐     ┌─────────────────────┐          │
│   │   ALERT (if issue)  │     │   UPDATE CONTEXT    │          │
│   │   Email/Slack/Push  │     │   Append to .md     │          │
│   └─────────────────────┘     └─────────────────────┘          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Workflow Catalog

### 1. KINME Daily Sales Summary

**Trigger**: Daily at 6:00 AM (after close)
**Source**: EatPOS365 API
**Actions**:
1. Pull previous day's transactions
2. Calculate: Revenue, covers, avg spend, food/bev split
3. Compare to trailing 7-day average
4. If anomaly detected → append to Flags in CONTEXT.md
5. Write daily summary to `05_Kinme/daily_logs/`

**Thresholds**:
- Revenue down >20% from 7-day avg → Flag
- Covers down >15% → Flag
- Average spend change >10% → Flag

```yaml
# n8n workflow structure (pseudocode)
nodes:
  - Schedule Trigger (6:00 AM daily)
  - EatPOS365 API: Get yesterday's transactions
  - Function: Calculate metrics
  - IF: Check thresholds
    - True: Append to CONTEXT.md Flags
  - Write File: Daily log
  - (Optional) Send Notification
```

---

### 2. KINME Weekly Food Cost Analysis

**Trigger**: Every Monday at 7:00 AM
**Source**: EatPOS365 + Inventory data (if available)
**Actions**:
1. Pull week's sales by item
2. Calculate theoretical food cost (if recipes mapped)
3. Compare to actual inventory movement
4. Identify variance
5. Update CONTEXT.md with summary

**Thresholds**:
- Food cost % > 35% → Flag
- Variance between theoretical vs actual > 5% → Flag
- Any item food cost > 40% → Flag specific item

---

### 3. SOLARTECH/HIPPOS Weekly Pipeline

**Trigger**: Every Monday at 8:00 AM
**Source**: Zoho CRM API
**Actions**:
1. Pull deals by stage
2. Calculate pipeline value, conversion rates
3. Identify stalled deals (no activity >14 days)
4. Compare to previous week
5. Update CONTEXT.md

**Thresholds**:
- Pipeline value drop >20% → Flag
- Stalled deals >5 → Flag
- Win rate drop >10% → Flag

---

### 4. WCI Production Summary

**Trigger**: Every Monday at 8:00 AM
**Source**: Odoo MRP API
**Actions**:
1. Pull production orders completed/pending
2. Calculate on-time delivery rate
3. Identify bottlenecks or delays
4. Check inventory levels vs reorder points
5. Update CONTEXT.md

**Thresholds**:
- On-time rate <90% → Flag
- Any material below reorder point → Flag
- Production backlog >X days → Flag

---

### 5. TRADING Daily Position Check

**Trigger**: Daily at market close (4:00 PM)
**Source**: IBKR API (when configured)
**Actions**:
1. Pull current positions
2. Calculate daily P&L, total exposure
3. Calculate drawdown from peak
4. Update CONTEXT.md

**Thresholds**:
- Drawdown >5% from peak → Flag
- Single position >20% of portfolio → Flag
- Daily loss >2% → Flag

---

### 6. CONTEXT.md Weekly Rollup

**Trigger**: Every Sunday at 9:00 PM
**Source**: All daily/weekly data
**Actions**:
1. Compile weekly summary for each entity
2. Clear resolved flags
3. Update "Next Session Focus" based on priorities
4. Archive old logs

**Output**:
- Fresh CONTEXT.md ready for Monday
- Weekly digest email (optional)

---

## Integration Requirements

### EatPOS365
- [ ] Confirm API availability
- [ ] Get API credentials
- [ ] Test endpoints: transactions, items, inventory
- [ ] Document rate limits

### Zoho
- [ ] Zoho CRM API setup
- [ ] Zoho Inventory API setup
- [ ] Zoho Analytics API setup
- [ ] OAuth configuration for n8n

### Odoo
- [ ] Odoo XML-RPC or REST API access
- [ ] Test endpoints: manufacturing, inventory, sales
- [ ] Document authentication method

### IBKR
- [ ] Client Portal API or TWS API
- [ ] Paper trading account for testing
- [ ] Document position/P&L endpoints

### File System (iCloud/OneDrive)
- [ ] n8n can write to BizOS folder
- [ ] Test CONTEXT.md append operation
- [ ] Set up file versioning/backup

---

## Threshold Configuration

Create a central config file for all thresholds:

```json
{
  "kinme": {
    "food_cost_max": 0.35,
    "revenue_drop_alert": 0.20,
    "covers_drop_alert": 0.15
  },
  "trading": {
    "max_drawdown": 0.05,
    "max_position_size": 0.20,
    "daily_loss_limit": 0.02
  },
  "solartech": {
    "pipeline_drop_alert": 0.20,
    "stalled_deal_days": 14
  },
  "wci": {
    "on_time_min": 0.90,
    "backlog_max_days": 7
  }
}
```

This lives in `00_Holding/thresholds.json` and n8n reads from it.

---

## Implementation Order

| Priority | Workflow | Reason |
|----------|----------|--------|
| 1 | Kinme Daily Sales | Immediate value, validates architecture |
| 2 | Context Weekly Rollup | Makes system self-maintaining |
| 3 | Trading Daily Check | Once IBKR connected |
| 4 | Solartech/Hippos Pipeline | Zoho integration |
| 5 | WCI Production | Odoo integration |

---

## Next Steps

1. **Verify API access** for EatPOS365
2. **Create test workflow** in n8n for Kinme daily
3. **Test file write** to BizOS folder from n8n
4. **Set up notification channel** (email or Slack)
5. **Build first production workflow**

---

*"The best system is one you don't have to remember to use."*
