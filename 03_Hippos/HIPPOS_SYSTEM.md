# HIPPOS Operations Framework

## Business Overview

**Company Name:** Hippos (formerly "Water Hippos")
**Business Model:** B2C Retail & Service
**Operating Region:** [To be specified]
**Current Status:** Active service provider with product/service transition underway

### Current Business Lines
- **Primary:** Boiler and water heating services (installation, maintenance, repair)
- **Emerging:** Solar energy systems and integrated energy management

### Strategic Transition Timeline
- **Current State (2025):** Boiler/water-focused revenue base, established customer relationships
- **2025 Target:** Solar product introduction, energy management offerings
- **Goal:** Become integrated energy solutions provider with recurring revenue from both legacy and new service lines

---

## Business Model Architecture

### Revenue Streams
1. **Service Calls & Installation**
   - One-time boiler installations
   - Emergency repair calls
   - Maintenance contracts (recurring)
   - Solar installations (new)

2. **Product Sales**
   - Boiler systems (WCI supplier)
   - Solar panels & inverters (Solartech distributor)
   - Accessories and components

3. **Recurring Revenue**
   - Maintenance contracts
   - Extended warranties
   - Monitoring/management subscriptions (future)

### Supplier Relationships
- **WCI:** Primary boiler/water equipment manufacturer
- **Solartech:** Solar equipment distributor
- **Other:** [To be added as needed]

---

## Key Financial Metrics Framework

### Job-Level Economics
- **Average Job Value:** $[VARIES BY TYPE]
  - Boiler Installation: $[X]
  - Service Call: $[X]
  - Solar Installation: $[X]

- **Job Margin Structure:**
  - Labor Cost per Job: [% of revenue or hourly rate calculation]
  - Material Cost per Job: [% of revenue or COGS]
  - Gross Margin Target: [70-85% typical for service businesses]
  - Net Margin Target: [15-25% after overhead]

### Customer Economics
- **Customer Acquisition Cost (CAC):** $[CALCULATE]
- **Lifetime Value (LTV):** $[CALCULATE]
- **LTV:CAC Ratio Target:** 3:1 minimum
- **Repeat Customer Rate:** [% of customers who return]
- **Average Customer Lifespan:** [Years]
- **Revenue per Customer (Annual):** $[CALCULATE]

### Operational Metrics
- **Job Completion Time:** [Hours average]
- **Jobs per Technician per Week:** [Target]
- **Average Wait Time to Service:** [Days]
- **First-Time Fix Rate:** [%]
- **Customer Satisfaction Score:** [1-5 or NPS]
- **Safety Incident Rate:** [Per X hours]

---

## KPI Dashboard Structure

### Critical KPIs for B2C Service Business

#### Revenue & Profitability (Monthly)
- Total Revenue by Service Type
- Gross Profit by Job Type
- Gross Margin %
- Labor Cost as % of Revenue
- Material Cost as % of Revenue
- Net Operating Margin %
- Revenue per Technician

#### Customer Metrics (Monthly & Rolling 12M)
- New Customers Acquired
- Repeat Customer Revenue (%)
- Customer Lifetime Value
- Customer Acquisition Cost (CAC)
- Churn Rate
- Net Revenue Retention (NRR)

#### Operational Metrics (Weekly & Monthly)
- Jobs Scheduled vs. Completed
- Average Job Revenue
- Average Job Margin
- Technician Utilization Rate (%)
- On-Time Completion Rate
- Customer Satisfaction Score
- Safety: Days Since Incident

#### Product Mix (Monthly)
- Revenue % by Product/Service Line
- Boiler Revenue Trend
- Solar Revenue Trend
- Service/Maintenance Revenue Trend
- Product Attach Rate (accessories per main job)

#### Pipeline & Growth (Weekly)
- Leads by Source
- Lead-to-Customer Conversion Rate
- Sales Cycle Length (days)
- Pipeline Value vs. Monthly Target

---

## Zoho Data Integration Requirements

### Data Extraction Points

#### From Zoho CRM
- Customer records (contact info, address, job history)
- Leads and lead source tracking
- Opportunity pipeline (jobs scheduled)
- Job completion dates and details
- Customer interaction history
- Customer satisfaction surveys/ratings

#### From Zoho Inventory
- Product/service catalog with pricing
- COGS for boilers and solar equipment
- Supplier relationships (WCI, Solartech)
- Stock levels and turnover
- Pricing tier definitions

#### From Zoho Books/Finance
- Invoice data (revenue, dates, payment status)
- Labor costs by job (technician time)
- Material costs by job (from supplier purchases)
- Overhead costs (rent, insurance, utilities, vehicles, etc.)
- Accounts payable and supplier payments

#### From Zoho Analytics (if available)
- Pre-built reports on customer behavior
- Supplier performance metrics
- Cash flow projections

### Key Data Fields Needed
- **Jobs/Opportunities:** Job ID, Customer ID, Job Type, Service Date, Labor Hours, Materials Cost, Job Revenue, Status
- **Customers:** Customer ID, Acquisition Date, Repeat Status, Total Revenue (LTV), Last Service Date
- **Products:** Product ID, Product Type, Cost, Selling Price, Supplier
- **Technicians:** Technician ID, Hours Worked, Jobs Completed, Utilization Rate

---

## Pricing Structure Considerations

### Service-Based Pricing
- **Hourly Rate Structure:** Boiler calls typically $[X/hour] + parts
- **Package Pricing:** Maintenance plans at $[X/month]
- **Diagnostic Fees:** $[X] per call (often waived with job booking)

### Product-Based Pricing
- **Boiler Systems:** Cost-plus markup (30-50% typical)
- **Solar Systems:** Competitive vs. Solartech wholesale pricing
- **Accessories:** Higher margin products for cross-sell

### Tiered Offerings
- **Basic:** Service calls, repairs (boiler-focused)
- **Standard:** Installation + basic maintenance (boiler or solar)
- **Premium:** Complete energy management solution (future state)

### Pricing Review Cycle
- Quarterly review of competitive landscape
- Annual adjustment for cost inflation
- Product-specific pricing based on supplier cost changes

---

## Data-Driven Decision Framework

### Questions This Framework Answers
1. Which customers are most profitable? (Focus for retention)
2. What's our real cost per job by type? (Pricing validation)
3. How many repeat customers do we have? (Retention KPI)
4. Is solar cannibalization or incremental? (Product strategy)
5. What's optimal technician dispatch? (Operations efficiency)
6. Where do profitable customers come from? (Marketing ROI)
7. How much overhead per customer? (Unit economics)

### Monthly Review Cycle
1. **Week 1:** Data imports and reconciliation
2. **Week 2:** KPI calculation and variance analysis
3. **Week 3:** Deep dives into underperforming areas
4. **Week 4:** Leadership review and action items

---

## Assumptions & Notes

### Current Assumptions (To Validate)
- Boiler service is mature, high-margin line of business
- Solar transition will initially have lower margins (market entry)
- Repeat customer rate is key competitive advantage
- Technician labor is largest variable cost
- Seasonal variation exists (heating demand winter-focused)

### Data Maturity Level
- **Current:** Manual tracking, likely incomplete historical data
- **Target:** Full data flow from Zoho within 90 days
- **Long-term:** Real-time dashboards with daily updates

### System Architecture
- Monthly Excel-based reporting (operational dashboard)
- Weekly KPI snapshots (management review)
- Quarterly strategic reviews with 12-month trend analysis
- Annual pricing and margin benchmarking

---

## Document Map
- **HIPPOS_SYSTEM.md** (this file): Strategic context and metrics framework
- **hippos_dashboard.xlsx**: Operational tracking and calculations
- **DATA_REQUIREMENTS.md**: Exact Zoho exports needed
