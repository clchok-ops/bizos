# WCI Odoo Data Export Requirements

## Overview
This document specifies the exact data exports needed from Odoo to populate the WCI dashboard. All exports should be in CSV format unless otherwise noted.

---

## 1. MRP Module Exports

### 1.1 Production Orders (mo_export.csv)

**Report**: Manufacturing > Manufacturing Orders

**Required Columns**:
| Field | Odoo Location | Notes |
|-------|---------------|-------|
| MO Number | Name | Unique production order ID |
| Product | Product.Name | SKU/Product name |
| Quantity Ordered | Product Qty | Units to manufacture |
| Status | State | Draft, Confirmed, In Progress, Done |
| Date Ordered | Create Date | When MO was created |
| Planned Start Date | Planned Date Start | Scheduled production start |
| Planned End Date | Scheduled Date Finish | Scheduled completion date |
| Actual Start Date | Date Started | Actual production start (if available) |
| Actual End Date | Date Finished | Actual completion date (if Done) |
| Quantity Produced | Qty Produced | Actual units completed |
| Scrap Qty | Scrap | Units scrapped during production |
| Location | Location (Stock Location) | Manufacturing location code |

**Filter Criteria**:
- Status IN (Confirmed, In Progress, Done)
- Date Ordered >= [Month Start Date]
- Include last 90 days of history for backlog trending

**Export Frequency**: Daily

**File Format**: CSV, sorted by Planned End Date (earliest first)

---

### 1.2 Work Orders (wo_export.csv)

**Report**: Manufacturing > Work Orders

**Required Columns**:
| Field | Odoo Location | Notes |
|-------|---------------|-------|
| Work Order ID | Name | Unique identifier |
| MO Reference | Production Order (MO Number) | Link to parent MO |
| Operation | Operation.Name | Step in manufacturing process |
| Sequence | Sequence | Order of operations |
| Workstation | Workstation.Name | Equipment/resource used |
| Planned Hours | Duration Expected | Standard/planned labor hours |
| Actual Hours | Duration (Actual) | Actual labor hours used |
| Status | State | Pending, In Progress, Done |
| Date Started | Date Started | Actual start time |
| Date Finished | Date Finished | Actual finish time |
| Scrap Qty | Scrap | Units scrapped at this operation |
| Rework Qty | Rework Qty (custom field) | Units requiring rework |

**Filter Criteria**:
- Status IN (In Progress, Done)
- Date Finished >= [Month Start Date]

**Export Frequency**: Daily

**Notes**:
- If "Rework Qty" custom field doesn't exist, request IT to create it (Scrap vs Rework tracking)
- Use Duration Actual or calculate from Date Started/Finished if field unavailable

---

### 1.3 Bill of Materials (bom_export.csv)

**Report**: Manufacturing > Bill of Materials

**Required Columns**:
| Field | Odoo Location | Notes |
|-------|---------------|-------|
| BOM ID | Name | Unique BOM identifier |
| Product | Product Name | What is this BOM for? |
| Product SKU | Product Code | SKU for matching |
| Quantity | Product Qty | Qty of finished product |
| Component SKU | Bom Line > Product Code | Raw material code |
| Component Name | Bom Line > Product Name | Raw material description |
| Qty Per Unit | Bom Line > Product Qty | Quantity per finished unit |
| Unit of Measure | Bom Line > Product UOM | UOM (ea, kg, m, etc) |
| Standard Cost | Bom Line > Product > Standard Price | Unit cost of component |
| Type | Bom Line > Type | Normal, Phantom, Byproduct |
| Status | Active | True/False |

**Filter Criteria**:
- Status = Active
- Include all standard and custom BOMs

**Export Frequency**: Monthly (or when BOM changes)

**Notes**:
- Standard Cost should be the current material cost from the price list
- If "Standard Price" field unavailable, use last PO price or cost accounting valuation

---

### 1.4 Routings (routing_export.csv)

**Report**: Manufacturing > Routings

**Required Columns**:
| Field | Odoo Location | Notes |
|-------|---------------|-------|
| Routing ID | Name | Unique routing identifier |
| Product | Product Name | What product uses this routing? |
| Operation Sequence | Operation Line > Sequence | Order of operations |
| Operation Name | Operation Line > Operation Name | Name of operation (e.g., "Welding") |
| Workstation | Operation Line > Workstation Name | Equipment used |
| Duration Minutes | Operation Line > Time Cycle | Standard time per unit (minutes) |
| Setup Minutes | Operation Line > Time Setup (custom) | Setup time (if available) |
| Cost Category | Operation Line > Cost Category Name | Labor cost pool |
| Status | Active | True/False |

**Filter Criteria**:
- Status = Active
- Include all routings for manufactured products

**Export Frequency**: Monthly (or when routing changes)

---

### 1.5 Work Centers / Workstations (workstation_export.csv)

**Report**: Manufacturing > Work Centers

**Required Columns**:
| Field | Odoo Location | Notes |
|-------|---------------|-------|
| Workstation Code | Name | Unique workstation ID |
| Workstation Name | Description (or Name) | Human-readable name |
| Capacity (units/hour) | Capacity per Cycle | Maximum output rate |
| Machine Cost/Hour | Costs Lines > Cost (Hourly) | Machine operating cost |
| Labor Cost/Hour | Cost Category > Cost per Hour | Direct labor rate |
| Available Hours/Day | Availability (custom or manual) | Hours available for production |
| Status | Active | True/False |

**Filter Criteria**:
- Status = Active
- Include all manufacturing workstations

**Export Frequency**: Monthly

---

## 2. Inventory Module Exports

### 2.1 Current Stock Levels (inventory_status.csv)

**Report**: Inventory > Stock Levels (Valuation)

**Required Columns**:
| Field | Odoo Location | Notes |
|-------|---------------|-------|
| Product Code | Product Code | SKU |
| Product Name | Product Name | Description |
| Category | Product Category | Raw Material, WIP, Finished Goods, Scrap |
| Location | Location Name | Warehouse location |
| On-Hand Qty | Quantity On Hand | Current stock quantity |
| Reserved Qty | Reserved | Qty allocated to orders |
| Available Qty | Free | On-hand minus reserved |
| Unit Cost | Unit Cost (Valuation) | Current per-unit cost |
| Total Value | On-Hand Qty × Unit Cost | Total inventory value |
| UOM | Unit of Measure | ea, kg, m, etc |
| Last Stock Move Date | Latest Stock Move Date | Last in/out transaction |

**Locations to Include**:
- Stock / Raw Materials (supplier purchases)
- Stock / Work in Progress (production jobs)
- Stock / Finished Goods (ready to ship)
- Stock / Scrap (defective/unusable)

**Export Frequency**: Weekly (or at month-end)

**Notes**:
- Valuation method should match GL: FIFO, LIFO, or Average Cost
- Include only locations managed by WCI (exclude supplier/customer locations)

---

### 2.2 Stock Movements (stock_moves.csv)

**Report**: Inventory > Stock Moves

**Required Columns**:
| Field | Odoo Location | Notes |
|-------|---------------|-------|
| Stock Move ID | Name | Unique identifier |
| Date | Date | Transaction date |
| Product Code | Product Code | What moved? |
| From Location | Source Location | Where it came from |
| To Location | Destination Location | Where it went |
| Quantity | Quantity | Units moved |
| Unit Cost | Unit Cost | Cost per unit at time of move |
| Move Type | Move Type | Receipt, Issue, Internal Transfer, Return |
| Reference | Reference | PO#, MO#, SO# |
| Status | State | Draft, Confirmed, Done |

**Filter Criteria**:
- Status = Done
- Date >= [Month Start Date]
- Include all movement types

**Export Frequency**: Weekly

**Notes**:
- Use for detailed reconciliation and audit trail
- Stock adjustments should be flagged (Move Type = Adjustment)

---

### 2.3 Scrap Records (scrap_export.csv)

**Report**: Inventory > Stock Moves (filtered) OR Manufacturing > Scrap Orders (if separate module)

**Required Columns**:
| Field | Odoo Location | Notes |
|-------|---------------|-------|
| Scrap ID | Name or Reference | Unique scrap record ID |
| Date | Date | When scrap occurred |
| MO Reference | Manufacturing Order (if linked) | Which production job? |
| Work Order Reference | Work Order (if available) | Which operation? |
| Product Code | Product Code | What was scrapped? |
| Quantity Scrapped | Quantity | How many units? |
| Scrap Reason | Reason (custom field) | Why? (Material defect, Setup error, Operator error, etc) |
| Scrap Cost | Unit Cost × Qty | Total loss value |
| Location | From Location | Where it came from |
| Salvage Value | Salvage Value (if any) | Recovered value (if sold) |
| Status | Status | Open, Resolved, Credited |

**Filter Criteria**:
- Status IN (Open, Resolved, Credited)
- Date >= [Month Start Date]

**Export Frequency**: Daily (for KPI tracking)

**Notes**:
- If "Reason" custom field doesn't exist, request IT to create it
- Essential for root cause analysis on Scrap Rate KPI

---

## 3. Sales/CRM Module Exports

### 3.1 Sales Orders (so_export.csv)

**Report**: Sales > Orders

**Required Columns**:
| Field | Odoo Location | Notes |
|-------|---------------|-------|
| Order Number | Name | Sales order ID (SO###) |
| Customer | Partner Name | Solartech or Hippos |
| Order Date | Date Order | When customer placed order |
| Promised Delivery Date | Commitment Date | Customer's requested delivery |
| Line Item | Line Number | Multiple lines per SO |
| Product Code | Product Code | SKU ordered |
| Quantity Ordered | Product Qty | Units ordered |
| Unit Price | Unit Price | Price per unit (before discounts) |
| Discount % | Discount % | Any line-level discount |
| Line Total | Subtotal (Qty × Price × (1-Discount%)) | Revenue for this line |
| Status | State | Draft, Confirmed, Delivered, Canceled |

**Filter Criteria**:
- Status IN (Confirmed, Delivered)
- Date Order >= [Last 90 days]
- Customer IN (Solartech, Hippos)

**Export Frequency**: Daily

**Notes**:
- Essential for On-Time Delivery KPI calculation
- Use for Transfer Pricing validation (compare SO price to transfer price)

---

### 3.2 Delivery Records (delivery_export.csv)

**Report**: Inventory > Deliveries (Stock Pickings - Outgoing)

**Required Columns**:
| Field | Odoo Location | Notes |
|-------|---------------|-------|
| Delivery ID | Name | Shipment/Picking ID |
| Order Number | Sale Order Reference | Which SO is this fulfilling? |
| Customer | Partner Name | Solartech or Hippos |
| Planned Date | Scheduled Date | When was it supposed to ship? |
| Actual Date | Date Done | When did it actually ship? |
| Product Code | Product Code | What was shipped? |
| Quantity Shipped | Done Qty | Units actually shipped |
| Status | State | Confirmed, In Transit, Done |
| Delay Days | Actual Date - Planned Date | Days late (if positive) |

**Filter Criteria**:
- Status = Done
- Date Done >= [Month Start Date]

**Export Frequency**: Daily (as shipments complete)

**Notes**:
- Match with SO export for On-Time Delivery Rate calculation
- Allows variance analysis: promised vs actual

---

### 3.3 Invoice Data (invoice_export.csv)

**Report**: Accounting > Invoices (Customer Invoices only)

**Required Columns**:
| Field | Odoo Location | Notes |
|-------|---------------|-------|
| Invoice Number | Name | Invoice ID |
| Customer | Partner Name | Solartech or Hippos |
| Invoice Date | Invoice Date | Date issued |
| Order Reference | Sale Order Reference | Which SO? |
| Product Code | Invoice Line > Product Code | SKU |
| Quantity Invoiced | Invoice Line > Qty | Units billed |
| Unit Price | Invoice Line > Unit Price | Price per unit |
| Line Total | Invoice Line > Subtotal | Revenue recognized |
| Total Invoice Amount | Amount Total (Sum) | Total invoice value |
| Status | State | Draft, Posted, Paid, Cancelled |

**Filter Criteria**:
- Status = Posted
- Invoice Date >= [Month Start Date]

**Export Frequency**: Weekly or at month-end

**Notes**:
- Used for revenue reconciliation
- Validates Transfer Pricing (internal vs external revenue)

---

## 4. Accounting / General Ledger Exports

### 4.1 Manufacturing Costs (gl_export.csv)

**Report**: Accounting > General Ledger OR Manufacturing > Cost Analysis

**Required Columns**:
| Field | Odoo Location | Notes |
|-------|---------------|-------|
| GL Account | Account Code | 5200-Direct Materials, 5210-Direct Labor, 5220-Overhead |
| Account Name | Account Name | Cost pool name |
| Amount | Debit or Credit | Cost incurred |
| Date | Date Posted | When recorded |
| MO Reference | Reference / Analytic Tag | Which MO (if available)? |
| Cost Category | Cost Category (Analytic) | Material, Labor, Overhead, Scrap |
| Product (if available) | Analytic Tag / Product | Which product? |

**Accounts to Include**:
- 5200 Direct Materials
- 5210 Direct Labor (by workstation/cost center)
- 5220 Manufacturing Overhead (allocation)
- 5230 Scrap/Rework
- 5400 COGS (periodic validation)

**Filter Criteria**:
- Date Posted >= [Month Start Date]
- Account Code 52xx range

**Export Frequency**: Monthly (GL cycle)

**Notes**:
- If MRP module lacks cost tracking, GL is the authoritative source
- Overhead allocation method must be consistent and documented

---

## 5. Custom Fields Required (IT Checklist)

If not present in your Odoo instance, request these custom fields:

| Module | Model | Field Name | Type | Purpose |
|--------|-------|------------|------|---------|
| Manufacturing | Work Order | Rework Qty | Integer | Track rework units separately from scrap |
| Manufacturing | Scrap Order | Scrap Reason | Selection | Root cause (Material defect, Setup error, Operator error, Equipment failure, etc) |
| Manufacturing | Production Order | Backlog Days | Computed | Days from creation to scheduled end |
| Inventory | Stock Move | Scrap Reason | Selection | Why was this scrapped? (link to MO scrap records) |
| Sales | Sale Order | Customer Channel | Selection | Solartech (Wholesale) or Hippos (Retail) |
| Manufacturing | Routing Line | Time Setup | Float | Setup time separate from cycle time |

---

## Export Template Structure

### File Naming Convention
```
mo_export_2024-01-31.csv
wo_export_2024-01-31.csv
bom_export_2024-01.csv  (monthly, no date)
routing_export_2024-01.csv  (monthly, no date)
workstation_export_2024-01.csv  (monthly, no date)
inventory_status_2024-01-31.csv
stock_moves_2024-01-31.csv
scrap_export_2024-01-31.csv
so_export_2024-01-31.csv
delivery_export_2024-01-31.csv
invoice_export_2024-01-31.csv
gl_export_2024-01.csv  (monthly, no date)
```

### Folder Structure
```
/sessions/focused-clever-maxwell/mnt/BizOS/04_WCI/
├── data_exports/
│   ├── daily/
│   │   ├── mo_export_YYYY-MM-DD.csv
│   │   ├── wo_export_YYYY-MM-DD.csv
│   │   ├── scrap_export_YYYY-MM-DD.csv
│   │   ├── so_export_YYYY-MM-DD.csv
│   │   └── delivery_export_YYYY-MM-DD.csv
│   ├── weekly/
│   │   ├── inventory_status_YYYY-MM-DD.csv
│   │   ├── stock_moves_YYYY-MM-DD.csv
│   │   └── invoice_export_YYYY-MM-DD.csv
│   └── monthly/
│       ├── bom_export_YYYY-MM.csv
│       ├── routing_export_YYYY-MM.csv
│       ├── workstation_export_YYYY-MM.csv
│       └── gl_export_YYYY-MM.csv
└── wci_dashboard.xlsx  (consumes the above exports)
```

---

## Data Quality Checks

Before importing into dashboard, verify:

1. **No Missing Required Columns**: All columns listed above present in export
2. **Date Format Consistency**: All dates in YYYY-MM-DD format
3. **Numeric Values**: No text in quantity/cost columns (except headers)
4. **No Duplicate Records**: Primary key fields unique
5. **Status Values Match Odoo**: Only expected values present (e.g., "Done", not "Completed")
6. **Foreign Key References Valid**: Product codes, customer names match master data

---

## Implementation Steps

1. **Prepare Odoo**: Ensure all custom fields created (see section 5)
2. **Test Exports**: Export a small date range (1 week) first
3. **Validate Format**: Check all columns present, data types correct
4. **Load into Dashboard**: Import CSVs into wci_dashboard.xlsx using Data > Get External Data (or copy-paste with proper formatting)
5. **Verify Formulas**: Ensure all dashboard formulas calculate correctly post-import
6. **Automate (Optional)**: Set up scheduled Odoo reports or use third-party sync tool (e.g., Zapier, Integromat) for recurring exports

---

## Support & Troubleshooting

**Question**: What if my Odoo version doesn't have a field?
**Answer**: Contact your Odoo admin or implementation partner. Most fields are in standard v13+. Older versions may need customization.

**Question**: Can I automate these exports?
**Answer**: Yes. Set up scheduled Odoo report exports (Automation > Actions > Email Reporting) or use a third-party integration tool.

**Question**: How do I handle multi-currency or multi-language?
**Answer**: Convert all costs to base currency; use product internal codes (SKU) rather than translated names.

**Question**: What's the file size limit for imports?
**Answer**: Excel limits: ~1M rows per sheet. For large exports, split by month or use database import instead.
