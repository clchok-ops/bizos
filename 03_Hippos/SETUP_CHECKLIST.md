# HIPPOS Framework - Implementation Checklist

## Pre-Launch (Before Day 1)

### Documentation Review
- [ ] Read INDEX.md (5 minutes) - understand what exists
- [ ] Read README.md (10 minutes) - understand how to get started
- [ ] Skim HIPPOS_SYSTEM.md (5 minutes) - understand business context
- [ ] Skim DATA_REQUIREMENTS.md (5 minutes) - understand data sources

### Initial Setup
- [ ] Create shared folder for HIPPOS framework files
- [ ] Set up Zoho user account with export permissions
- [ ] Identify Zoho admin contact for API questions
- [ ] Ensure Excel is available and file opens without errors
- [ ] Test Excel file opens on your computer (should open in <2 seconds)

---

## Week 1 - Initial Data Collection

### Day 1: Zoho Exports
**Time:** 1-2 hours

- [ ] **CRM Exports** (Follow DATA_REQUIREMENTS.md section 1)
  - [ ] Export: All Customers with Full History
  - [ ] Export: All Jobs/Opportunities (Past 12 Months)
  - [ ] Export: All Leads (Past 6 Months)
  - [ ] Verify: Column headers match required fields
  - [ ] Save: Using naming convention HIPPOS_CRM_*.csv

- [ ] **Inventory Exports** (Follow DATA_REQUIREMENTS.md section 2)
  - [ ] Export: Complete Product & Service Catalog
  - [ ] Export: Recent Purchase Orders from Suppliers
  - [ ] Verify: COGS values are accurate
  - [ ] Save: Using naming convention HIPPOS_INVENTORY_*.csv

- [ ] **Books/Finance Exports** (Follow DATA_REQUIREMENTS.md section 3)
  - [ ] Export: All Customer Invoices (Past 12 Months)
  - [ ] Export: Technician/Labor Costs by Job
  - [ ] Export: All Supplier Payments (Past 12 Months)
  - [ ] Export: Operating Expenses Summary (Monthly Breakdown)
  - [ ] Verify: All amounts match Zoho totals
  - [ ] Save: Using naming convention HIPPOS_BOOKS_*.csv

### Day 2-3: Data Reconciliation
**Time:** 1-2 hours

- [ ] **Data Quality Check** (Follow DATA_REQUIREMENTS.md section "Data Quality Checklist")
  - [ ] Verify all Customer IDs are unique
  - [ ] Verify all Job IDs are unique
  - [ ] Verify Job Dates are populated for completed jobs
  - [ ] Verify Revenue > $0 for completed jobs
  - [ ] Verify Labor Hours and Labor Cost are correlated
  - [ ] Check for duplicate job entries
  - [ ] Verify all currency is consistent (USD)

- [ ] **Data Reconciliation**
  - [ ] Compare total invoices from Books export to CRM jobs total revenue
  - [ ] Check for missing jobs (in CRM but not invoiced)
  - [ ] Check for orphaned invoices (no matching job)
  - [ ] Verify supplier POs match COGS values
  - [ ] Resolve any discrepancies with Zoho admin

- [ ] **Data Organization**
  - [ ] Create folder: Data_Exports_2025_January
  - [ ] Copy all verified CSV files into folder
  - [ ] Create README with export dates and reconciliation notes
  - [ ] Store backup copy in secure location

---

## Week 2 - Framework Population

### Day 4-5: Job Costing Entry
**Time:** 1-2 hours

- [ ] Open hippos_dashboard.xlsx
- [ ] Go to "Job Costing" sheet

**For each job in your data:**
- [ ] Enter Job ID (A column)
- [ ] Enter Customer Name (B column)
- [ ] Enter Service Type (C column) - Boiler Installation, Service Call, Solar Installation, etc.
- [ ] Enter Job Date (D column) - format YYYY-MM-DD
- [ ] Enter Labor Hours (E column) - decimal format (e.g., 2.5)
- [ ] Enter Labor Rate (F column) - your hourly rate or average
- [ ] Enter Material Cost (H column) - COGS from your invoices
- [ ] Enter Job Revenue (I column) - what customer was charged
- [ ] **VERIFY:** Columns G, J, K auto-populate with formulas

**Validation:**
- [ ] All rows 6-15 have at least Job ID and Revenue
- [ ] No cells show #VALUE! or #DIV/0! errors
- [ ] Margin % looks reasonable (typically 30-60% for service businesses)
- [ ] Revenue and cost numbers match your invoices

### Day 6-7: Customer Tracker Entry
**Time:** 1-2 hours

- [ ] Open hippos_dashboard.xlsx
- [ ] Go to "Customer Tracker" sheet

**For each customer in your data:**
- [ ] Enter Customer ID (A column)
- [ ] Enter Customer Name (B column)
- [ ] Enter Acquisition Date (C column) - when customer first booked with you
- [ ] Enter Total Jobs (D column) - count of all jobs this customer had
- [ ] Enter Total Revenue (E column) - sum of all job revenues (Lifetime Value)
- [ ] Enter Last Service Date (F column) - most recent job date
- [ ] **VERIFY:** Column G auto-fills "Yes" or "No" for repeat customer
- [ ] **VERIFY:** Column H auto-calculates days since last service

**Validation:**
- [ ] All rows 6-25 have at least Customer ID and one job record
- [ ] No cells show #VALUE! or #DIV/0! errors
- [ ] Repeat customer rate (B31) is > 0%
- [ ] Average LTV (B33) seems reasonable for your business

---

## Week 3 - Calibration & Review

### Day 8-10: Pricing & Assumptions
**Time:** 1-2 hours

- [ ] Open hippos_dashboard.xlsx
- [ ] Go to "Pricing Master" sheet

**Review Pre-loaded Products:**
- [ ] Verify all 10 products are relevant to your business
- [ ] Update COGS (column D) with actual supplier costs
- [ ] Update Selling Prices (column E) with your current prices
- [ ] **VERIFY:** Markup % (column F) auto-calculates and shows reasonable margins
- [ ] Add/remove products as needed for your business

**Update Pricing Strategy Assumptions (B20-B23):**
- [ ] Enter your standard labor rate (hourly) - B20
- [ ] Enter your service call markup target % - B21
- [ ] Enter your product markup target % - B22
- [ ] Enter your minimum gross margin target % - B23

**Validation:**
- [ ] All COGS values are positive (or zero for service-only items)
- [ ] All selling prices > COGS for products
- [ ] Markup percentages are reasonable (30-50% for products typical)

### Day 11-13: KPI Configuration
**Time:** 1 hour

- [ ] Open hippos_dashboard.xlsx
- [ ] Go to "Monthly KPIs" sheet

**Enter Key Assumptions (B5-B8):**
- [ ] Customer Acquisition Cost - B5 (your average marketing spend per customer)
- [ ] Average Labor Cost per Hour - B6 (verify this matches Pricing Master B20)
- [ ] Target Gross Margin % - B7 (your target, typically 60-75%)
- [ ] Total Monthly Overhead - B8 (rent, utilities, insurance, vehicles, etc. combined)

**Review Calculated Metrics:**
- [ ] Revenue Metrics section (rows 12-17): Should show totals from Job Costing
- [ ] Profitability Metrics section (rows 21-29): Should show healthy margins
- [ ] Customer Metrics section (rows 33-40): LTV:CAC ratio should be ≥ 3:1
- [ ] Operational Metrics section (rows 44-49): Jobs completed should match Job Costing

**Troubleshooting:**
- [ ] If cells show "-" or blank, you may need more data rows
- [ ] If ratio seems off, verify inputs in blue cells are correct
- [ ] If revenue is 0, ensure Job Costing sheet has data and is saved

### Day 14: Full Verification
**Time:** 1 hour

- [ ] **Cross-Check Data:**
  - [ ] Job Costing total revenue (B20) matches Books export total
  - [ ] Customer Tracker customer count (B29) matches CRM export
  - [ ] Pricing Master products match your current inventory
  - [ ] Monthly overhead (B8) matches your finance records

- [ ] **Verify Formulas:**
  - [ ] Save and close Excel file
  - [ ] Reopen file - all green formulas should show values, not errors
  - [ ] Spot-check 3 calculations manually (e.g., margin = revenue - labor - material)
  - [ ] Check that changing a blue cell updates related green cells

- [ ] **Create Backup:**
  - [ ] Save file as: hippos_dashboard_2025_01_FINAL.xlsx
  - [ ] Copy to backup location
  - [ ] Store original template as: hippos_dashboard_TEMPLATE.xlsx (for next month)

---

## Week 4 - Leadership Review

### Day 15-17: Analysis & Insights
**Time:** 2 hours

- [ ] **Review Top-Line Metrics:**
  - [ ] Total Revenue (Monthly KPIs B12)
  - [ ] Gross Profit (Monthly KPIs B21)
  - [ ] Gross Margin % (Monthly KPIs B22)
  - [ ] Net Profit (Monthly KPIs B28)
  - [ ] Net Margin % (Monthly KPIs B29)

- [ ] **Customer Insights:**
  - [ ] Repeat Customer Rate (Monthly KPIs B35) - is it above 40%?
  - [ ] Average Customer LTV (Monthly KPIs B37) - is it 3x+ your CAC?
  - [ ] LTV:CAC Ratio (Monthly KPIs B39) - is it 3:1 or better?

- [ ] **Operational Insights:**
  - [ ] Jobs Completed (Monthly KPIs B44)
  - [ ] Average Revenue per Job (Monthly KPIs B16)
  - [ ] Average Gross Margin per Job (Monthly KPIs B46)
  - [ ] Labor Cost % of Revenue (Monthly KPIs B24) - should be 25-35%

- [ ] **Pipeline Health:**
  - [ ] Total Weighted Pipeline (Pipeline sheet B26) - vs. monthly target
  - [ ] Average Deal Size (Pipeline sheet B27)
  - [ ] Average Days in Pipeline (Pipeline sheet B29) - how long are deals taking?

### Day 18: Presentation Preparation
**Time:** 1 hour

- [ ] **Create Summary Report:**
  - [ ] One-page summary with key metrics
  - [ ] Simple charts: Revenue trend, margin %, customer acquisition
  - [ ] Highlights: Top performing products/services, best customers
  - [ ] Issues: Any metrics significantly below target?
  - [ ] Recommendations: 2-3 actions to improve next month

- [ ] **Prepare for Leadership Meeting:**
  - [ ] Print or prepare digital version of dashboard
  - [ ] Prepare to answer: "What drove profitability up/down?"
  - [ ] Prepare to answer: "Which are our most valuable customers?"
  - [ ] Prepare to answer: "What should we focus on next month?"

### Day 19-20: Leadership Review & Planning
**Time:** 1 hour

- [ ] **Conduct Leadership Review:**
  - [ ] Present monthly KPIs and key insights
  - [ ] Discuss variances vs. expectations
  - [ ] Review customer acquisition and retention
  - [ ] Discuss pricing strategy and margins
  - [ ] Plan action items for next month

- [ ] **Document Decisions:**
  - [ ] Note any pricing changes decided
  - [ ] Note any operational changes to implement
  - [ ] Note any new business targets
  - [ ] Store meeting notes with monthly data

---

## Month 2+ - Monthly Rhythm

### First Week: Data Collection (1 hour)
- [ ] Export from Zoho (CRM, Inventory, Books)
- [ ] Save with month/year naming convention
- [ ] Run data quality checks

### Second Week: Framework Population (2 hours)
- [ ] Make copy of previous month's file
- [ ] Clear data cells, keep formulas
- [ ] Enter new month's Job Costing data
- [ ] Enter new month's Customer Tracker data
- [ ] Verify all calculations update

### Third Week: Analysis (1 hour)
- [ ] Review Monthly KPIs dashboard
- [ ] Compare to prior month and annual targets
- [ ] Identify variances and root causes
- [ ] Prepare summary report

### Fourth Week: Leadership Review (1 hour)
- [ ] Present metrics to leadership
- [ ] Discuss variances and actions
- [ ] Plan month ahead
- [ ] Archive data file with final naming

---

## Success Criteria (How to know you're done)

### Framework is Ready When:
- [ ] All 5 Excel sheets have data populated
- [ ] Monthly KPIs dashboard shows calculated values (not errors)
- [ ] You can answer these questions in <5 minutes each:
  - [ ] "What was our total revenue last month?" (Monthly KPIs B12)
  - [ ] "What was our gross margin %?" (Monthly KPIs B22)
  - [ ] "How many jobs did we complete?" (Monthly KPIs B44)
  - [ ] "What's our repeat customer rate?" (Monthly KPIs B35)
  - [ ] "What's our average job value?" (Monthly KPIs B16)

### Framework is Working When:
- [ ] Monthly reporting takes <4 hours (down from previous manual process)
- [ ] Leadership is using data to make decisions
- [ ] You're catching trends month-to-month (revenue up/down, margins shifting, etc.)
- [ ] You can explain profitability by understanding labor, materials, and pricing
- [ ] You can identify which customers are most valuable and focus retention efforts

---

## Common Questions During Setup

**Q: "The Job Costing sheet only has 10 rows. What if I have more jobs?"**
A: Copy rows 6-15 and paste new rows below (16, 17, 18, etc.). Update the summary formulas in B19-B27 to include new rows (e.g., change =SUM(I6:I15) to =SUM(I6:I25)).

**Q: "Can I delete the example products in Pricing Master?"**
A: Yes, delete rows as needed. Just make sure you have all your actual products listed.

**Q: "Do I need to import invoices into the dashboard?"**
A: No, just verify that your Job Costing revenue total matches your invoice total. You don't need to manually import invoice details.

**Q: "What if my labor cost and material cost don't match exactly?"**
A: The dashboard estimates margins. Minor discrepancies are okay, but investigate major ones (>10%) - may indicate invoicing issues or untracked costs.

**Q: "How do I handle partial payments or cancelled jobs?"**
A: For cancelled jobs, exclude them from Job Costing and Customer Tracker. For partial payments, enter the invoiced amount (what customer was charged), not the received amount. Track payment separately in Zoho.

**Q: "Can I link this to Zoho directly?"**
A: Not yet, but you can ask Zoho about API access for automation in the future. For now, monthly CSV exports work fine.

---

## Need Help?

**Setup Questions:** See README.md → "Getting Started" section
**Data Export Questions:** See DATA_REQUIREMENTS.md
**Business Context Questions:** See HIPPOS_SYSTEM.md
**Troubleshooting:** See README.md → "Troubleshooting" section
**File Navigation:** See INDEX.md

---

**Estimated Total Setup Time: 10-15 hours (spread across 4 weeks)**
**Expected Ongoing Time: 2-4 hours per month**

**You're ready to begin! Start with the "Pre-Launch" section above.**
