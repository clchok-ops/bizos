# HIPPOS Operations Framework - File Index

**Framework Status:** Ready for Production
**Version:** 1.0
**Created:** January 31, 2025
**Last Updated:** January 31, 2025

---

## File Manifest

### Core Documentation

#### 1. README.md
- **Size:** 9.6 KB
- **Type:** Quick Start Guide
- **Purpose:** Getting started guide with common scenarios, troubleshooting, and monthly workflow
- **Read Time:** 10 minutes
- **Who Should Read First:** Operations manager, finance lead, new users
- **Key Sections:**
  - Files overview and purpose
  - Getting started (5-step startup process)
  - Common data entry patterns
  - Monthly review checklist
  - Troubleshooting guide

#### 2. HIPPOS_SYSTEM.md
- **Size:** 7.3 KB
- **Type:** Strategic Framework Document
- **Purpose:** Comprehensive business model documentation, metrics definitions, and data requirements context
- **Read Time:** 15 minutes
- **Who Should Read:** Executive stakeholders, finance leadership, business analysts
- **Key Sections:**
  - Business overview and transition plan (boiler → solar)
  - Revenue streams and suppliers (WCI, Solartech)
  - Financial metrics framework (job margins, CAC, LTV, repeat rate)
  - KPI dashboard structure for B2C service business
  - Zoho data integration points
  - Pricing strategy considerations
  - Decision framework and assumptions

#### 3. DATA_REQUIREMENTS.md
- **Size:** 9.6 KB
- **Type:** Technical Specification
- **Purpose:** Exact Zoho exports needed to populate the framework
- **Read Time:** 15 minutes
- **Who Should Read:** Finance operations person, Zoho admin, data steward
- **Key Sections:**
  - Zoho CRM exports (Customers, Jobs/Opportunities, Leads)
  - Zoho Inventory exports (Products, Supplier costs)
  - Zoho Books exports (Invoices, Labor, Expenses)
  - Monthly data import workflow
  - Data quality checklist
  - File naming conventions
  - Troubleshooting common export issues

#### 4. INDEX.md (this file)
- **Type:** File Navigation Guide
- **Purpose:** Directory of all framework components with descriptions and usage patterns

---

### Operational Tools

#### 5. hippos_dashboard.xlsx
- **Size:** 18 KB
- **Type:** Excel Workbook (5 sheets)
- **Purpose:** Real-time operational tracking and KPI calculation
- **Format:** Pre-built formulas, ready for data entry
- **Last Verified:** All 139 formulas tested, 0 errors
- **Color Coding:**
  - 🔵 Blue font = User input cells
  - ⚫ Black font = Formulas (fixed calculations)
  - 🟢 Green font = Cross-sheet linked formulas

**Sheet 1: Job Costing**
- Track every service job: labor, materials, revenue, margins
- 10 pre-formatted rows for monthly job entry
- Auto-calculates: Labor cost, Gross margin $, Gross margin %
- Monthly summary with key metrics
- **Formulas:** 39
- **Input rows:** 6-15

**Sheet 2: Customer Tracker**
- Track customer lifetime value and repeat business patterns
- 20 pre-formatted rows for customer data
- Auto-identifies repeat customers
- Calculates days since last service
- Monthly metrics: repeat rate, avg LTV, repeat LTV vs. single-purchase LTV
- **Formulas:** 48
- **Input rows:** 6-25

**Sheet 3: Pricing Master**
- Master catalog of all services and products
- Pre-loaded with 10 example items (boiler, solar, service calls, etc.)
- Auto-calculates markup % from cost and price
- Pricing strategy assumptions section
- **Formulas:** 10
- **Pre-populated rows:** 6-15

**Sheet 4: Pipeline & Leads**
- Sales pipeline and opportunity tracking
- 15 pre-formatted rows for active deals
- Auto-calculates weighted pipeline value (value × probability)
- Pipeline summary metrics
- **Formulas:** 21
- **Input rows:** 6-20

**Sheet 5: Monthly KPIs**
- Master KPI dashboard pulling from all other sheets
- Organized into 5 metric categories
- Key assumptions input section
- Auto-calculated: Revenue, Profitability, Customer, Operational metrics
- Manual input: New customer count, satisfaction scores, completion rates
- **Formulas:** 21 (mostly cross-sheet references)
- **Assumption rows:** 5-8

---

## Usage Scenarios

### Scenario 1: First-Time Setup (Week 1)
**Goal:** Get the framework running with your first month of data

**Actions:**
1. Read: README.md (Quick Start section)
2. Export: Follow DATA_REQUIREMENTS.md to export from Zoho
3. Populate: Enter job data into Job Costing sheet (rows 6-15)
4. Populate: Enter customer data into Customer Tracker sheet (rows 6-25)
5. Review: Check Monthly KPIs dashboard for calculated metrics
6. Save: Archive with date: `hippos_dashboard_2025_01.xlsx`

**Time Required:** 2-3 hours

---

### Scenario 2: Monthly Operations Review (Every Month)
**Goal:** Update metrics and track performance

**Actions:**
1. Export: Zoho CRM, Books, Inventory per DATA_REQUIREMENTS.md
2. Reconcile: Verify data against Job Costing expectations
3. Input: Enter month's jobs in Job Costing (rows 6-15)
4. Input: Enter customer updates in Customer Tracker (rows 6-25)
5. Review: Check Monthly KPIs against prior month
6. Analyze: Identify variance and investigate root causes
7. Archive: Save with month/year in filename

**Time Required:** 2-4 hours
**Frequency:** Monthly (recommended first week of month)

---

### Scenario 3: Pricing Review (Quarterly)
**Goal:** Evaluate pricing and margin strategy

**Actions:**
1. Open: Pricing Master sheet
2. Review: COGS for each product (verify against recent POs)
3. Review: Selling prices against market
4. Review: Pricing Strategy assumptions (labor rate, markup targets)
5. Update: Adjust prices or costs as needed
6. Analyze: Check impact on Job Costing margins in latest month
7. Document: Notes on changes made and rationale

**Resources:**
- Pricing Master sheet (full product catalog)
- Supplier data from DATA_REQUIREMENTS (WCI, Solartech)
- Recent job margins from Job Costing sheet

**Time Required:** 1-2 hours

---

### Scenario 4: Customer Lifetime Value Analysis
**Goal:** Understand which customers are most valuable

**Actions:**
1. Open: Customer Tracker sheet
2. Sort: By Total Revenue (column E) descending
3. Identify: Top 20% of customers by revenue
4. Analyze: Repeat rate of top customers vs. average
5. Strategy: Plan retention/expansion efforts for high-value customers
6. Compare: Repeat customer LTV (B35) vs. single-purchase LTV (B36)

**Metrics to Calculate:**
- Which 20% of customers generate 80% of revenue?
- Are high-value customers mostly repeat or one-time?
- Which service types correlate with repeat business?

**Resources:**
- Customer Tracker sheet
- HIPPOS_SYSTEM.md (LTV definitions)

**Time Required:** 30 minutes

---

### Scenario 5: Sales Pipeline Forecast
**Goal:** Predict next month's revenue from current pipeline

**Actions:**
1. Open: Pipeline & Leads sheet
2. Review: All leads with probability > 0%
3. Calculate: Sum of weighted values (column H) = realistic forecast
4. Compare: Weighted pipeline value (B26) vs. monthly revenue target
5. Action: If shortfall, identify gap and leads needed

**Key Metrics:**
- Total Weighted Pipeline (B26): Expected revenue from current deals
- Average Deal Value (B27): Size to target
- Average Probability (B28): Quality indicator
- Average Days in Pipeline (B29): Velocity indicator

**Resources:**
- Pipeline & Leads sheet
- HIPPOS_SYSTEM.md (sales cycle length context)

**Time Required:** 15 minutes

---

### Scenario 6: Labor Cost Analysis
**Goal:** Ensure technician efficiency and profitability

**Actions:**
1. Open: Job Costing sheet
2. Review: Labor hours and labor cost per job
3. Calculate: Average labor cost (B27 in summary)
4. Compare: Against standard labor rate
5. Investigate: Jobs with high labor hours relative to revenue
6. Identify: Training needs or pricing adjustments

**Key Metrics:**
- Total Labor Cost (B21): Monthly labor burden
- Labor Cost % of Revenue (B24): Should be 25-35% for healthy business
- Avg Labor Cost per Job (B27): Efficiency indicator
- Avg Revenue per Job (B26): Pricing validation

**Resources:**
- Job Costing sheet
- HIPPOS_SYSTEM.md (job margins section)

**Time Required:** 30 minutes

---

## Data Flow Diagram

```
ZOHO ONE
├── CRM (Customers, Jobs, Leads)
├── Inventory (Products, Pricing, Suppliers)
└── Books (Invoices, Expenses, Labor)
    ↓
    (Export per DATA_REQUIREMENTS.md)
    ↓
hippos_dashboard.xlsx
├── Job Costing (↑ from Books + CRM)
├── Customer Tracker (↑ from CRM)
├── Pricing Master (↑ from Inventory, manual inputs)
├── Pipeline & Leads (↑ from CRM)
└── Monthly KPIs (↓ pulls from all above)
    ↓
Business Insights & Decisions
```

---

## Key Metrics Quick Reference

### Revenue Metrics
- **Total Revenue:** Sum of all job revenues
- **Average Revenue per Job:** Total Revenue ÷ Jobs Completed
- **Revenue per Technician:** Total Revenue ÷ Number of Technicians

### Profitability Metrics
- **Gross Profit:** Revenue - (Labor Cost + Material Cost)
- **Gross Margin %:** Gross Profit ÷ Revenue
- **Labor Cost %:** Labor Cost ÷ Revenue (target: 25-35%)
- **Material Cost %:** Material Cost ÷ Revenue (target: 20-40%)
- **Net Profit:** Gross Profit - Overhead
- **Net Margin %:** Net Profit ÷ Revenue (target: 15-25%)

### Customer Metrics
- **Customer Acquisition Cost (CAC):** Total marketing spend ÷ New customers
- **Lifetime Value (LTV):** Total revenue from customer over lifetime
- **LTV:CAC Ratio:** LTV ÷ CAC (target: 3:1 minimum)
- **Repeat Rate:** Repeat customers ÷ Total customers (target: 40%+)
- **Payback Period:** CAC ÷ (LTV ÷ 12 months)

### Operational Metrics
- **Jobs Completed:** Count of finished jobs
- **Total Labor Hours:** Sum of all technician hours
- **Gross Margin per Job:** Average job profit
- **Labor Cost per Job:** Average job labor cost
- **Days Since Last Service:** Indicator of customer churn risk

---

## Customization Guide

### Adding a New Sheet
1. Right-click tab in Excel
2. Choose "Insert Sheet"
3. Follow same color coding and formula patterns
4. Link new metrics to Monthly KPIs dashboard

### Updating Product Catalog
1. Open Pricing Master sheet
2. Add/edit rows as needed
3. Formulas auto-calculate markup %
4. No need to update other sheets

### Adding New KPIs
1. Open Monthly KPIs sheet
2. Add new metric labels in column A
3. For auto-calculated metrics, use formulas referencing source sheets
4. For manual metrics, use blue input cells

### Integrating with Zoho API (Future)
1. Contact Zoho support for API access
2. Use their REST API or Zapier integration
3. Replace manual exports with automated weekly pulls
4. Dashboard will update in real-time

---

## Version Control & Archiving

### Recommended Naming Convention
```
hippos_dashboard_YYYY_MM.xlsx
Examples:
- hippos_dashboard_2025_01.xlsx
- hippos_dashboard_2025_02.xlsx
```

### Archiving Strategy
- Save final version of each month before starting new month
- Store in shared drive with access controls
- Keep rolling 12-month archive for trend analysis
- Backup monthly to external storage

### Change Log
**v1.0 (Jan 31, 2025)**
- Initial framework created
- 5 sheets, 139 formulas
- All formulas tested, 0 errors
- Ready for first data entry

---

## Support & Troubleshooting

**Quick Link Guide:**
- Getting started → README.md (Getting Started section)
- Data export questions → DATA_REQUIREMENTS.md
- Business context → HIPPOS_SYSTEM.md
- Specific metrics → HIPPOS_SYSTEM.md (KPI Dashboard Structure)
- Formula errors → README.md (Troubleshooting section)
- Excel structure → This file (File Manifest)

**Common Issues:**
- See README.md section "Troubleshooting"
- See DATA_REQUIREMENTS.md section "Troubleshooting Common Export Issues"

---

## Success Metrics

**How to know this framework is working:**

✓ Monthly reporting takes <4 hours (down from manual process)
✓ You can answer "What was our profit last month?" in 5 minutes
✓ You can identify your top 10 customers and their LTV in <10 minutes
✓ You can forecast next month's revenue from the pipeline
✓ You understand your labor efficiency and can benchmark against goals
✓ You can track month-to-month KPI trends
✓ Your team uses the data to make decisions, not just for reporting

---

**Ready to begin? Start with README.md → Getting Started section**
