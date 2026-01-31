# HIPPOS - Zoho Data Export Requirements

## Overview
This document specifies the exact data exports needed from Zoho One to populate the HIPPOS Operations Framework dashboards. Each export should be scheduled monthly or imported as-needed.

---

## 1. ZOHO CRM EXPORTS

### 1.1 Customers Export
**Report Name:** All Customers with Full History
**Schedule:** Monthly (by 1st business day of month)
**Format:** CSV or Excel

**Required Fields:**
- `customer_id` (unique identifier)
- `customer_name`
- `email`
- `phone`
- `address` (full address)
- `acquisition_date` (when customer first booked)
- `lifetime_revenue_total` (auto-calculated if available)
- `last_service_date`
- `service_type` (Boiler/Solar/Mixed)
- `repeat_customer_flag` (Y/N)
- `contact_method` (how acquired: direct, referral, online, etc.)
- `customer_status` (Active/Inactive/Lost)
- `repeat_count` (number of repeat jobs)

**Expected Rows:** All active + inactive customers with transaction history
**Notes:** Include customers from past 24 months at minimum

---

### 1.2 Opportunities/Jobs Export
**Report Name:** All Jobs and Service Calls (Past 12 Months)
**Schedule:** Monthly (by 2nd business day of month)
**Format:** CSV or Excel

**Required Fields:**
- `job_id` (unique identifier)
- `customer_id` (links to customer export)
- `job_date` (service date or installation date)
- `job_type` (Boiler Installation/Boiler Repair/Boiler Maintenance/Solar Installation/Solar Monitoring/Other)
- `job_description` (brief description of work)
- `job_status` (Scheduled/In Progress/Completed/Cancelled)
- `quoted_value` ($ amount quoted)
- `actual_revenue` ($ amount charged)
- `estimated_labor_hours`
- `actual_labor_hours`
- `assigned_technician` (name or ID)
- `completion_date` (if completed)
- `parts_materials_used` (description or category)
- `customer_satisfaction_rating` (1-5 or NPS if available)
- `repeat_job_flag` (Y/N - is this a repeat customer's job?)

**Expected Rows:** All jobs from past 12 months
**Notes:** Include cancelled/incomplete jobs for accuracy. Include proposed/quoted jobs not yet started.

---

### 1.3 Leads Export
**Report Name:** All Current and Recent Leads (Past 6 Months)
**Schedule:** Bi-weekly
**Format:** CSV or Excel

**Required Fields:**
- `lead_id` (unique identifier)
- `lead_name` (prospect company/person)
- `lead_source` (Google Search/Referral/Social Media/Direct Call/Website/Other)
- `lead_date` (when lead captured)
- `status` (New/Qualified/Proposal Sent/Negotiation/Won/Lost)
- `estimated_value` ($)
- `service_interest` (Boiler/Solar/Both)
- `sales_owner` (assigned to)
- `days_in_pipeline` (current stage duration)
- `notes` (reason won or lost)

**Expected Rows:** Typically 20-100 depending on pipeline activity
**Notes:** Leads that converted to customers should be marked "Won"

---

## 2. ZOHO INVENTORY EXPORTS

### 2.1 Products/Services Catalog
**Report Name:** Complete Product & Service Catalog
**Schedule:** Monthly (when pricing changes)
**Format:** CSV or Excel

**Required Fields:**
- `product_id` (unique identifier)
- `product_name`
- `product_type` (Boiler System/Solar Panel/Inverter/Accessories/Service/Maintenance Plan)
- `supplier` (WCI/Solartech/Internal/Other)
- `cost_price` (what you pay the supplier - COGS)
- `selling_price` (list price to customer)
- `product_category` (Boiler/Solar/Water/Energy Management)
- `unit_of_measure` (Each/Hour/Month)
- `current_stock` (if applicable)
- `reorder_level`

**Expected Rows:** 15-50 depending on catalog size
**Notes:** Include discontinued products marked as inactive (for historical costing accuracy)

---

### 2.2 Purchase Orders / Supplier Costs
**Report Name:** Recent Purchase Orders from Suppliers
**Schedule:** Monthly
**Format:** CSV or Excel

**Required Fields:**
- `po_id` (purchase order number)
- `supplier_name` (WCI/Solartech/Other)
- `product_id` (what was purchased)
- `quantity`
- `unit_cost` (price paid to supplier)
- `total_cost`
- `po_date` (order date)
- `receipt_date` (when received)
- `invoice_reference`

**Expected Rows:** Last 30-50 purchase orders
**Notes:** This validates your COGS numbers and supplier pricing trends

---

## 3. ZOHO BOOKS/FINANCE EXPORTS

### 3.1 Invoices with Line Items
**Report Name:** All Customer Invoices (Past 12 Months)
**Schedule:** Monthly
**Format:** CSV or Excel (one row per line item)

**Required Fields:**
- `invoice_number` (unique identifier)
- `invoice_date`
- `customer_id` (links to CRM)
- `job_id` (links to opportunity, if available)
- `line_item_description` (Labor/Boiler Unit/Solar Panel/Accessories/etc.)
- `line_item_quantity`
- `line_item_rate` (price charged for this line)
- `line_item_total` (quantity × rate)
- `invoice_total`
- `payment_status` (Paid/Unpaid/Partial)
- `payment_date` (if paid)
- `days_to_payment` (if paid)

**Expected Rows:** 100-500+ depending on transaction volume
**Notes:** One row per line item so you can match to job costs. Include credit memos as negative entries.

---

### 3.2 Expense Report - Labor Costs
**Report Name:** Technician/Labor Costs by Job or Person
**Schedule:** Monthly
**Format:** CSV or Excel

**Required Fields:**
- `expense_date`
- `technician_name` (or ID)
- `job_id` (what job did they work on)
- `hours_worked`
- `hourly_rate`
- `labor_cost_total`
- `expense_category` (wages/benefits/etc.)

**Expected Rows:** 50-200 depending on team size and job frequency
**Notes:** If you track via timesheets in Zoho, export those. If via payroll, estimate allocation by job.

---

### 3.3 Accounts Payable - Supplier Payments
**Report Name:** All Supplier Payments (Past 12 Months)
**Schedule:** Monthly
**Format:** CSV or Excel

**Required Fields:**
- `payment_date`
- `supplier_name` (WCI/Solartech/Other)
- `po_number` (or reference)
- `payment_amount`
- `payment_method` (Check/ACH/Card/Other)
- `invoice_reference` (from supplier)

**Expected Rows:** 30-100 depending on purchase frequency
**Notes:** Reconcile against POs and invoices for accuracy

---

### 3.4 Overhead & Operating Expenses
**Report Name:** Operating Expenses Summary (Monthly Breakdown)
**Schedule:** Monthly
**Format:** CSV or Excel

**Required Fields:**
- `month`
- `expense_category` (Rent/Utilities/Insurance/Vehicle/Software/Marketing/Other)
- `amount`
- `fixed_or_variable` (Fixed/Variable)

**Expected Rows:** 8-15 categories
**Notes:** These are allocated to customer/job as burden rates

---

## 4. ZOHO ANALYTICS (If Available)

### 4.1 Pre-built Reports
**Available Reports to Extract:**
- Customer Lifetime Value Report (if exists)
- Revenue by Product Report
- Repeat Customer Analysis
- Technician Performance Report

**If not available in Analytics:** Recreate these from raw CRM/Books data using the dashboard templates provided.

---

## Data Import Workflow

### Monthly Process (Recommended Schedule)
**Day 1-2 of Month:**
- Export from Zoho CRM: Customers, Jobs/Opportunities
- Export from Zoho Books: Invoices, Labor Costs, Expenses

**Day 3-4:**
- Export from Zoho Inventory: Products, Recent POs
- Export from Zoho CRM: Recent Leads

**Day 5:**
- Import all files into `hippos_dashboard.xlsx`
- Check for data quality (missing fields, duplicate IDs)
- Reconcile job revenue vs. invoice amounts

**Day 6-7:**
- Run dashboard calculations
- Review KPIs vs. prior month
- Prepare for management review

---

## Data Quality Checklist

Before importing into the dashboard, verify:

- [ ] All `customer_id` values are unique
- [ ] All `job_id` values are unique and match between CRM and Books exports
- [ ] `job_date` is not blank for completed jobs
- [ ] `actual_revenue` (or invoice totals) are greater than zero for completed jobs
- [ ] `labor_hours` and `labor_cost` are reasonably correlated
- [ ] COGS values match supplier invoices
- [ ] No duplicate job entries (same job appearing twice)
- [ ] All currency values are in the same currency (assume USD)
- [ ] Date fields are in consistent format (YYYY-MM-DD preferred)

---

## Troubleshooting Common Export Issues

### Issue: "Customer ID not found in Books"
**Cause:** Customer in CRM doesn't have corresponding invoice
**Solution:** Verify invoices are tied to correct CRM customer. May indicate new customer not yet invoiced.

### Issue: "Job revenue doesn't match invoice amount"
**Cause:** Job marked complete but invoice in draft/not finalized
**Solution:** Filter to "Paid" or "Sent" invoices only, or follow up on draft invoices.

### Issue: "Labor hours exceed job completion date"
**Cause:** Technician timesheet not aligned with job date
**Solution:** Ask team to log hours on actual job date or create mapping file.

### Issue: "Material costs missing for some jobs"
**Cause:** Boiler/products not tracked in Inventory for all jobs
**Solution:** Create standardized service bundles in Inventory and link each job to a service package.

---

## File Naming Convention

Save all exports with this naming convention for easy tracking:

```
HIPPOS_[EXPORT_TYPE]_[MONTH]_[YEAR].csv
```

Examples:
- `HIPPOS_CRM_CUSTOMERS_01_2025.csv`
- `HIPPOS_CRM_JOBS_01_2025.csv`
- `HIPPOS_BOOKS_INVOICES_01_2025.csv`
- `HIPPOS_INVENTORY_PRODUCTS_01_2025.csv`

---

## Automation Opportunity

**Future Enhancement:** If Zoho supports API access, automate weekly/daily pulls instead of monthly exports. This would enable real-time dashboard updates and faster decision-making.

**Contact Zoho Support** to confirm available APIs and integration options.

---

## Support & Questions

If data fields are unavailable in your Zoho instance:
1. Check custom fields (may contain needed data)
2. Verify Zoho modules are all active (CRM, Inventory, Books)
3. Review Zoho user permissions (ensure export user has read access)
4. Reach out to Zoho support for field mapping guidance

