# Solartech Report Configuration Guide

> **Purpose**: Configure automated reports from Zoho CRM and Zoho Inventory to feed the 360° analysis loop
> **Last Updated**: 2026-02-02
> **Status**: ✅ FULLY OPERATIONAL (verified Feb 2, 2026)

---

## Current State

### Zoho CRM Scheduled Reports (org798433294) - ✅ VERIFIED 2026-02-02
| Report Name | Frequency | Format | Time | Next Run | Status |
|-------------|-----------|--------|------|----------|--------|
| Confirm PV Sales | Daily | CSV | 9PM | Feb 2 | ✅ |
| Non-confirm PV Sales | Daily | CSV | 9PM | Feb 2 | ✅ |
| Paid Invoices (Weekly Report) | Daily | CSV | 9PM | Feb 2 | ✅ |
| Ongoing Deals Report_Filtered for Actions | Daily | CSV | 9PM | Feb 2 | ✅ |

**Note**: There are also 3 WEEKLY versions of these reports (still running) - can be disabled once daily flow is confirmed working.

### Zoho Inventory Scheduled Reports (org833030419)
| Report Name | Current Frequency | Recommended | Format | Recipient |
|-------------|-------------------|-------------|--------|-----------|
| Stock Summary (Weekly) | Weekly | **Daily** | CSV | automation@solartech.com.my |
| Stock Summary Report Everything | Weekly | **Daily** | CSV | automation@solartech.com.my |
| Sales Summary | Weekly | **Daily** | CSV | automation@solartech.com.my |

---

## Missing Reports to Add

### Zoho CRM - New Reports Needed
1. **Win/Loss Analysis Report** (Daily)
   - Module: Deals
   - Filters: Stage = Closed Won OR Closed-Lost
   - Fields: Deal Name, Account, Amount, Stage, Owner, Close Date, Sales Cycle Duration
   - Purpose: Track daily conversions and losses

2. **Aging Deals Report** (Daily)
   - Module: Deals
   - Filters: Stage NOT IN (Closed Won, Closed-Lost) AND Created > 90 days ago
   - Fields: Deal Name, Account, Amount, Stage, Owner, Created Time, Days Open
   - Purpose: Flag stale deals for risk model

3. **Quote Conversion Report** (Weekly)
   - Module: Quotes
   - Fields: Quote Subject, Deal Name, Stage, Amount, Created Time, Modified Time
   - Purpose: Track quote-to-deal conversion rates

### Zoho Inventory - New Reports Needed
1. **Purchase Order Summary** (Daily)
   - Fields: PO Number, Vendor, Status, Total, Order Date
   - Purpose: Track procurement activity

2. **Shipment Status Report** (Daily)
   - Fields: Shipment ID, Sales Order, Status, Ship Date
   - Purpose: Track fulfillment performance

---

## Manual Configuration Steps

### Step 1: Update CRM Report Frequencies

For each of the 3 weekly CRM reports:
1. Go to **Zoho CRM** > **Reports** > **Scheduled Reports**
2. Click on the report name (e.g., "Paid Invoices (Weekly Report)")
3. Click **Edit**
4. Change **Repeat Type** from "Weekly" to "Daily"
5. Change **Export file as** from "XLS" to "CSV"
6. Verify **Recipient** is `automation@solartech.com.my`
7. Click **Save**

Direct links:
- https://crm.zoho.com/crm/org798433294/tab/Reports/schedules

### Step 2: Update Inventory Report Frequencies

For each of the 3 weekly Inventory reports:
1. Go to **Zoho Inventory** > **Settings** > **Scheduled Reports**
2. Click on the report name
3. Change **Repeat Type** to "Daily"
4. Ensure **Format** is "CSV"
5. Verify **Recipient** is `automation@solartech.com.my`
6. Click **Save**

Direct link:
- https://inventory.zoho.com/app/833030419#/settings/scheduledreports

### Step 3: Create Missing Reports

#### Win/Loss Analysis Report (CRM)
1. Go to **Reports** > **Deal Reports**
2. Click **Create Report**
3. Select **Tabular Report**
4. Module: **Deals**
5. Add columns: Deal Name, Account Name, Amount, Stage, Deal Owner, Closing Date
6. Add filter: Stage is "Closed Won" OR Stage is "Closed-Lost"
7. Save as "Win-Loss Analysis"
8. Schedule: Daily to automation@solartech.com.my

#### Aging Deals Report (CRM)
1. Create new Tabular Report on Deals
2. Add columns: Deal Name, Account Name, Amount, Stage, Deal Owner, Created Time
3. Add formula column: Days Open = TODAY() - Created Time
4. Add filter: Stage NOT IN (Closed Won, Closed-Lost)
5. Add filter: Created Time < 90 days ago
6. Save as "Aging Deals"
7. Schedule: Daily

---

## Data Flow Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Zoho CRM      │    │  Zoho Inventory │    │    Eats365      │
│                 │    │                 │    │    (Kinme)      │
└────────┬────────┘    └────────┬────────┘    └────────┬────────┘
         │                      │                      │
         │ Daily CSV            │ Daily CSV            │ Manual Export
         │ Reports              │ Reports              │ (API pending)
         │                      │                      │
         └──────────┬───────────┴──────────────────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │ automation@solartech │
         │     .com.my          │
         └──────────┬───────────┘
                    │
                    │ Auto-forward to
                    │ iCloud BizOS folder
                    │
                    ▼
         ┌──────────────────────┐
         │  BizOS/_INBOX/       │
         │  (Landing Zone)      │
         └──────────┬───────────┘
                    │
                    │ Claude processes
                    │ at session start
                    │
                    ▼
         ┌──────────────────────┐
         │  360° Analysis       │
         │  - Risk Scoring      │
         │  - Anomaly Detection │
         │  - KPI Tracking      │
         └──────────┬───────────┘
                    │
                    │ Updates
                    │
                    ▼
         ┌──────────────────────┐
         │  _CONTEXT.md         │
         │  (Persistent Memory) │
         └──────────────────────┘
```

---

## Verification Checklist

### Zoho CRM Reports
- [x] Reports configured as Daily (not Weekly)
- [x] Export format set to CSV (not XLS)
- [x] Scheduled for 9PM daily
- [x] Emails arriving at automation@solartech.com.my

### Email-to-_INBOX Pipeline (✅ WORKING)
- [x] automation@solartech.com.my receiving emails from Zoho
- [x] Inbox rules forwarding attachments to iCloud
- [x] Files landing in BizOS/_INBOX/zoho/ folder

**Issue resolved (Feb 2, 2026)**: Mail.app rule wasn't applying automatically to existing emails. Fixed by manually applying rules. Future emails should process automatically.

**Root cause**: AppleScript mail rule was created after some emails arrived; existing emails weren't retroactively processed.

---

## Notes

- XLS format causes parsing issues; always use CSV
- Daily at 11:30 PM captures full day's data
- Zoho CRM new UI may require multiple attempts for form submission
- automation@solartech.com.my should have inbox rules to forward attachments to iCloud

*End of Configuration Guide*
