# HIPPOS Operations Framework - Quick Start Guide

## Files Overview

### 1. HIPPOS_SYSTEM.md
**Purpose:** Strategic context and metrics framework for the Hippos B2C service business.

**Key Sections:**
- Business overview (current boiler/water focus, transition to solar)
- Revenue streams and supplier relationships (WCI, Solartech)
- Key financial metrics framework (job margins, CAC, LTV, repeat rate)
- Zoho data integration points
- Pricing structure considerations
- Data-driven decision framework

**Use When:** Onboarding new team members, quarterly strategy reviews, understanding business model

---

### 2. hippos_dashboard.xlsx
**Purpose:** Operational tracking and real-time KPI calculation.

**Sheets Included:**

#### Job Costing
- Track every job: labor, materials, revenue, margin
- 10 rows pre-formatted for job entry (blue cells = inputs)
- Auto-calculates gross margin % per job
- Monthly summary includes revenue per job, margin metrics
- **How to use:** Enter each job's hours, labor rate, materials cost, and revenue; formulas calculate margins

#### Customer Tracker
- Track customer lifetime value and repeat business
- 20 rows for customer data (blue cells = inputs)
- Auto-identifies repeat customers
- Calculates days since last service
- Monthly metrics: repeat rate, avg LTV, repeat vs. single-purchase LTV
- **How to use:** One row per customer; enter job count and total lifetime revenue; LTV calculates automatically

#### Pricing Master
- Catalog of all services and products
- Pre-loaded with 10 example items: boiler, solar, service calls, maintenance contracts
- Shows COGS vs. selling price and markup %
- Pricing strategy assumptions section (labor rate, margin targets)
- **How to use:** Update with your actual products/services; adjust prices as needed; formulas show markup %

#### Pipeline & Leads
- Track sales opportunities and deal progression
- 15 rows for active deals (blue cells = inputs)
- Auto-calculates weighted pipeline value (value × probability)
- Pipeline summary: total value, average deal size, time in pipeline
- **How to use:** Enter leads with estimated value and win probability; formulas weight pipeline by probability

#### Monthly KPIs
- Master dashboard pulling data from all other sheets
- Key assumptions section: CAC, labor cost, overhead, margin targets
- Organized sections: Revenue, Profitability, Customer, Operational metrics
- **Green formulas** = automatically pull from Job Costing or Customer Tracker sheets
- **Blue cells** = manual inputs (new customer count, satisfaction scores, etc.)
- **How to use:** Input monthly overhead and key metrics; review calculated KPIs; green cells auto-populate from other sheets

**Formula Color Code:**
- **Blue text** = Inputs (user enters data here)
- **Black text** = Hardcoded calculations
- **Green text** = Linked formulas (pull from other sheets)

---

### 3. DATA_REQUIREMENTS.md
**Purpose:** Exact specifications for Zoho exports needed to populate the dashboard.

**Key Sections:**

**Zoho CRM Exports:**
- Customers (with acquisition date, LTV)
- Jobs/Opportunities (job type, labor hours, costs, revenue, technician)
- Leads (source, value, stage, sales cycle)

**Zoho Inventory Exports:**
- Products/Services Catalog (COGS, pricing, supplier)
- Purchase Orders (supplier costs and trends)

**Zoho Books Exports:**
- Invoices with line items (revenue breakdown by service/product)
- Labor costs (technician hours and rates)
- Accounts payable (supplier payments)
- Operating expenses (monthly overhead)

**Monthly Workflow:**
- Days 1-2: Export from CRM and Books
- Days 3-4: Export from Inventory
- Day 5: Import and reconcile in dashboard
- Days 6-7: Review KPIs, prepare reports

---

## Getting Started (First Month)

### Step 1: Prepare Your Data
1. Review DATA_REQUIREMENTS.md
2. Export required data from Zoho One
3. Use the file naming convention: `HIPPOS_[TYPE]_[MONTH]_[YEAR].csv`

### Step 2: Populate Job Costing Sheet
1. Open hippos_dashboard.xlsx
2. Go to "Job Costing" sheet
3. Enter each job from past month:
   - Job ID, Customer, Service Type, Date
   - Labor hours and hourly rate (blue cells)
   - Material costs (blue cell)
   - Job revenue (blue cell)
4. Formulas auto-calculate labor cost and margins

### Step 3: Populate Customer Tracker Sheet
1. Go to "Customer Tracker" sheet
2. Enter each customer:
   - Customer ID, name, acquisition date (blue cells)
   - Number of jobs (blue cell)
   - Total revenue (LTV) to date (blue cell)
   - Last service date (blue cell)
3. Formulas auto-identify repeat customers and calculate retention metrics

### Step 4: Update Pricing Master
1. Review pre-loaded pricing
2. Add/edit products and services specific to your business
3. Verify COGS (cost) and selling prices are accurate
4. Adjust "Pricing Strategy & Assumptions" section with your labor rate and margin targets

### Step 5: Review Monthly KPIs
1. Go to "Monthly KPIs" sheet
2. Input key assumptions:
   - Customer Acquisition Cost
   - Average labor rate
   - Target gross margin
   - Total monthly overhead
3. Review all calculated KPIs - they will auto-populate from Job Costing and Customer Tracker
4. For operational metrics not auto-calculated, enter manually:
   - New customers acquired
   - Customer satisfaction score
   - On-time completion rate

---

## Key Metrics to Track Monthly

### Revenue & Profitability
- Total revenue
- Gross profit and margin %
- Labor cost as % of revenue
- Material cost as % of revenue
- Net profit (after overhead)

### Customer Health
- Repeat customer rate (target: 40%+)
- Average customer LTV
- LTV:CAC ratio (target: 3:1 minimum)
- Payback period (how long to recover CAC)

### Operations
- Jobs completed per month
- Average revenue per job
- Gross margin per job
- Labor utilization (hours worked / available hours)

### Sales Pipeline
- Total weighted pipeline value
- Average deal size
- Time to close (days in pipeline)

---

## Common Data Entry Patterns

### Job Costing
**Scenario 1: Boiler Installation with parts and labor**
- Service Type: "Boiler Installation"
- Labor Hours: 4.0
- Labor Rate: $95/hr
- Material Cost: $1,200 (boiler unit cost)
- Job Revenue: $3,500 (what customer was charged)
- Result: Gross Margin = $3,500 - (4 × $95) - $1,200 = $1,920 (54.9%)

**Scenario 2: Service call with diagnostic fee**
- Service Type: "Service Call - Repair"
- Labor Hours: 1.5
- Labor Rate: $95/hr
- Material Cost: $150 (replacement parts)
- Job Revenue: $400 (charged flat rate)
- Result: Gross Margin = $400 - (1.5 × $95) - $150 = $117.50 (29.4%)

### Customer Tracker
**Scenario 1: One-time customer**
- Total Jobs: 1
- Total Revenue: $3,500
- Last Service Date: 2025-01-15
- Result: Repeat Customer? = No

**Scenario 2: Loyal maintenance customer**
- Total Jobs: 8 (maintenance contract + emergency calls)
- Total Revenue: $4,200
- Last Service Date: 2025-01-20
- Result: Repeat Customer? = Yes

---

## Troubleshooting

### "Formula shows #DIV/0! or #VALUE!"
- Ensure all blue input cells have values before formulas calculate
- Check that numeric fields (revenue, hours) aren't text
- Verify no commas in numeric entries

### "Green cells aren't updating from Job Costing"
- Verify sheet names match exactly: "Job Costing", "Customer Tracker"
- Ensure you've entered data in rows 6-15 (not other rows)
- Save and close/reopen file to refresh cross-sheet references

### "My numbers don't match Zoho"
- Check DATA_REQUIREMENTS.md to verify you exported correct fields
- Verify dates are within the current month
- Check for draft invoices (should exclude) vs. completed jobs (include)
- Reconcile manually against your Zoho reports

---

## Monthly Review Checklist

**Week 1 (Data Import):**
- [ ] Exported all required data from Zoho
- [ ] Imported jobs into Job Costing sheet
- [ ] Imported customers into Customer Tracker sheet
- [ ] Verified all blue cells are populated

**Week 2 (KPI Review):**
- [ ] Checked all formulas calculate without errors
- [ ] Reviewed Monthly KPIs dashboard
- [ ] Identified top 3 KPIs vs. target
- [ ] Noted any significant variances (±10%)

**Week 3 (Analysis):**
- [ ] Analyzed which jobs were most/least profitable
- [ ] Reviewed repeat customer rate vs. target
- [ ] Checked customer acquisition cost trend
- [ ] Evaluated pricing accuracy

**Week 4 (Action):**
- [ ] Documented insights and findings
- [ ] Identified one improvement opportunity
- [ ] Prepared summary for leadership review
- [ ] Archived current month's data (save copy with date)

---

## Integration with Zoho

### Recommended Monthly Process
1. **First Tuesday:** Request/download CRM and Books exports from Zoho
2. **Wednesday:** Clean and reconcile data per DATA_REQUIREMENTS.md
3. **Thursday:** Paste data into dashboard sheets
4. **Friday:** Review KPIs and prepare summary
5. **Following Monday:** Present to leadership

### Future Automation
- **Zoho API:** If Zoho supports API, automate weekly pulls for real-time dashboards
- **Zapier/Integration:** Consider automation for invoice-to-job linking
- **Custom Zoho Reports:** Build pre-filtered reports in Zoho that match export requirements

---

## Contact & Questions

**If you need to adjust this framework:**
- HIPPOS_SYSTEM.md: Update business context, metrics definitions
- hippos_dashboard.xlsx: Modify formulas, add sheets for new business lines
- DATA_REQUIREMENTS.md: Add fields based on your specific Zoho customizations

**Key Resources:**
- Zoho CRM help: https://www.zoho.com/crm/
- Zoho Books help: https://www.zoho.com/books/
- Zoho Inventory help: https://www.zoho.com/inventory/

---

**Framework Created:** January 2025
**Next Review Date:** [Set to end of first month using this framework]
**Owner:** [Operations/Finance Lead]
