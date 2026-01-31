# Solartech Operations Framework - Quick Start Guide

## Overview

The Solartech Operations Framework provides a complete business intelligence system for managing B2B distribution operations, including pipeline management, margin analysis, inventory tracking, and intercompany relationships.

## Files in This Directory

### 1. SOLARTECH_SYSTEM.md
**The Master Blueprint**
- Business model overview
- Key metrics and definitions
- Data integration architecture
- Dashboard specifications
- Integration workflow and success criteria

**Use this for**: Understanding the overall system, defining metrics, and planning implementation

---

### 2. DATA_REQUIREMENTS.md
**The Data Specification Document**
- Exact field mappings for all Zoho exports
- Step-by-step export instructions for each module
- File naming conventions
- Data quality checklist
- Automation recommendations

**Use this for**: Setting up data exports, troubleshooting data issues, automating the pipeline

---

### 3. solartech_dashboard.xlsx
**The Operational Workbook**

#### Sheet Organization:

**RAW DATA IMPORT SHEETS** (Starting with `_RAW_`)
- `_RAW_Deals` - Paste Zoho CRM Deals export
- `_RAW_Invoices` - Paste Zoho Invoices export
- `_RAW_Stock` - Paste Zoho Inventory Stock levels
- `_RAW_PO` - Paste Zoho Purchase Orders (from WCI)
- `_RAW_SO` - Paste Zoho Sales Orders
- `Settings` - Configuration and assumptions

**ANALYSIS DASHBOARDS**
1. **Pipeline Tracker** - Sales pipeline by stage
   - Deal counts and values by stage
   - Win/loss metrics
   - Revenue forecast (probability-weighted)
   - Summary KPIs (open pipeline, total pipeline, win rate)

2. **Margin Analysis** - Profitability metrics
   - Gross margin by product line (Solar, Boiler, Water)
   - Margin by top customers
   - COGS vs revenue trend
   - Section for intercompany margins

3. **Inventory Status** - Stock health monitoring
   - Qty on hand by product category
   - Inventory value and days outstanding
   - Reorder level tracking
   - Status indicators (OK / REORDER / SLOW)
   - Slow-moving products section

4. **Intercompany Tracking** - Upstream & downstream management
   - WCI purchases by month (PO count, spend, avg PO value)
   - Hippos sales by month (order count, revenue, avg order value)
   - Intercompany margin analysis (WCI cost → Solartech price → Hippos price)
   - Markup calculation by product

5. **Monthly KPIs** - Executive summary scorecard
   - 12 key metrics (Revenue, Profit, Margins, Pipeline, Inventory, Customer metrics)
   - Current month vs prior month vs YTD target
   - Easy input for manual data entry

---

## How to Use the Framework

### Step 1: Initial Setup (First Time)
1. Read `SOLARTECH_SYSTEM.md` to understand the business model
2. Review `DATA_REQUIREMENTS.md` for export specifications
3. Configure Zoho to export data (see automation section in DATA_REQUIREMENTS.md)
4. Save export templates to avoid re-entering specifications each month

### Step 2: Monthly Data Pipeline
1. **Export Data from Zoho** (weekly/monthly per schedule in DATA_REQUIREMENTS.md)
   - Deals (from CRM)
   - Invoices (from Inventory)
   - Stock levels (from Inventory)
   - Purchase Orders (from Inventory, filtered for WCI)
   - Sales Orders (from Inventory, including Hippos)

2. **Import into Excel** (takes ~10 minutes)
   - Open `solartech_dashboard.xlsx`
   - Go to `_RAW_Deals` sheet
   - Paste Deals CSV starting at cell A2 (not A1 - headers already there)
   - Repeat for Invoices, Stock, PO, SO sheets
   - All analysis sheets auto-populate

3. **Review Dashboards**
   - Pipeline Tracker: Check stage progression, forecast accuracy
   - Margin Analysis: Monitor profitability by product
   - Inventory Status: Identify slow-moving SKUs, reorder needs
   - Intercompany Tracking: Review WCI spend and Hippos revenue
   - Monthly KPIs: Input any manual metrics

### Step 3: Monthly Review Meeting
- Review all 5 dashboard tabs
- Compare month-over-month trends
- Identify issues: overstock, margin erosion, pipeline risk
- Update Settings sheet with monthly assumptions
- Archive previous month's workbook

---

## Color Coding Reference

### Formula Inputs (Planning/Scenarios)
- **Blue Font** = Input cells (values you can change)
  - Examples: Probability assumptions, manual KPI entries, product costs
  - These are the cells to update for scenarios

### Formula Calculations (Read-Only Results)
- **Black Font** = Calculated formulas (auto-calculate when inputs change)
  - Examples: Totals, averages, margins, forecasts
  - Don't edit these cells

### Configuration
- **Settings Sheet** - Update the Monthly COGS value to keep DIO calculations accurate

---

## Key Metrics Explained

### Sales & Pipeline
- **Pipeline Value** = Sum of all open deals (Prospect through Negotiation stages)
- **Win Rate** = Closed Won / (Closed Won + Closed Lost)
- **Forecast** = Pipeline Value × Average Probability % (shows expected revenue)

### Margins
- **Gross Margin %** = (Revenue - COGS) / Revenue
- **Intercompany Markup** = (Solartech Price - WCI Cost) / WCI Cost
- Higher margins by product help identify profit drivers

### Inventory
- **Days Inventory Outstanding (DIO)** = (Inventory Value / Monthly COGS) × 30
  - Lower is better (faster turnover)
  - Update `Settings!B2` with monthly COGS for accuracy
- **Reorder Alert** = When Qty on Hand < Reorder Level
- **Slow-Moving** = In stock > 90 days

### Intercompany
- **WCI Purchases** = Cost of goods (COGS driver)
- **Hippos Sales** = Revenue channel (% of total revenue)
- **Markup Chain** = Track profit at each stage (WCI → Solartech → Hippos)

---

## Troubleshooting

### Dashboard shows all zeros or errors

**Most Common Cause**: Raw data not imported correctly

**Fix**:
1. Check `_RAW_Deals` sheet - is there data in rows 3+?
2. Verify CSV was pasted starting at A2 (not A1)
3. Confirm headers in row 2 match expected columns
4. Check for missing columns (some fields may be blank)

### "Calculation errors" or "#REF!" formulas

**Cause**: Sheets or columns moved

**Fix**:
1. Don't rename or reorder the `_RAW_` sheets (formulas reference them by name)
2. Don't delete columns in raw sheets
3. Use Ctrl+Home to go to cell A1 before pasting new data
4. If broken, restore from backup and re-paste carefully

### Inventory or Margin analysis shows incorrect values

**Cause**: Product category names don't match

**Fix**:
1. In `_RAW_Invoices`, column B must have exact values: "Solar", "Boiler", "Water Treatment"
2. In `_RAW_Stock`, column C must match exactly
3. Check for extra spaces, different capitalization
4. Use Find & Replace (Ctrl+H) to standardize before pasting

### Won't import WCI Purchase Orders correctly

**Fix**:
1. In `DATA_REQUIREMENTS.md`, see section on Purchase Orders
2. Make sure you're exporting from Zoho Inventory → Purchase Orders
3. Filter for Vendor = "WCI" before exporting
4. Verify PO_DATE is in YYYY-MM-DD format

---

## Advanced Features

### Scenario Planning
1. Save a copy of the workbook: `solartech_dashboard_SCENARIO_NAME.xlsx`
2. Change blue font values to test different scenarios
3. Watch how margins, inventory, and forecasts change
4. Compare scenarios side-by-side

### Tracking Hippos Performance
1. In Sales Orders, ensure `Is_Intercompany` column correctly flags Hippos orders
2. Intercompany Tracking sheet shows Hippos buy vs sell volumes
3. Use this to monitor: Are they selling through inventory to consumers?
4. Calculate Hippos "Sell-Through Rate" = Hippos Sales / Hippos Purchases

### Margin Waterfall
Create a custom analysis:
1. WCI cost (from PO data)
2. Solartech markup (sell price to Hippos - WCI cost)
3. Hippos markup (retail price - Solartech price)
4. Track how margin is distributed across the chain

---

## Best Practices

1. **Backup Monthly** - Save each month's workbook with date: `solartech_dashboard_2025-01_JANUARY.xlsx`
2. **Keep Raw Data** - Never modify `_RAW_` sheets, they're your source of truth
3. **Update Settings** - Change `Settings!B2` monthly with actual COGS for accurate DIO
4. **Check Formulas** - Each quarter, verify formulas still reference correct cells
5. **Automate Exports** - Use Zoho Workflows or your IT team to auto-email exports
6. **Document Assumptions** - Add notes about unusual numbers or one-time items
7. **Share Monthly** - Schedule standing meeting to review all 5 dashboard tabs

---

## Support & Questions

- **Data questions**: See `DATA_REQUIREMENTS.md` section by section
- **Metric definitions**: See `SOLARTECH_SYSTEM.md` Key Business Metrics section
- **Formula issues**: Check cell formula (F2 shows formula bar) - look for cell references
- **Setup help**: Follow the "Initial Setup" section at top of README

---

## File Locations

All files stored in:
```
/sessions/focused-clever-maxwell/mnt/BizOS/02_Solartech/
```

- `SOLARTECH_SYSTEM.md` - Business framework & architecture
- `DATA_REQUIREMENTS.md` - Export specifications & procedures
- `solartech_dashboard.xlsx` - Operational workbook
- `README.md` - This file

---

## Version History

- **v1.0** - Initial framework created Jan 31, 2025
  - 5 analysis dashboards (Pipeline, Margin, Inventory, Intercompany, KPIs)
  - 6 raw data import sheets (Deals, Invoices, Stock, PO, SO, Settings)
  - All formulas validated and error-free
  - Ready for Zoho data import
