# Solartech Data Requirements - Zoho Exports

This document specifies exactly which data exports are needed from Zoho CRM and Zoho Inventory to populate the Solartech Operations dashboards.

---

## ZOHO CRM EXPORTS

### 1. Deals/Opportunities Report

**Export Format**: CSV or Excel
**Update Frequency**: Weekly
**Fields Required**:
```
ID | Deal_Name | Account_ID | Account_Name | Product_Category |
Deal_Amount | Currency | Stage | Probability |
Expected_Close_Date | Closed_Date | Created_Date | Last_Modified_Date |
Sales_Rep_ID | Sales_Rep_Name | Status |
Lost_Reason | Next_Step | Description
```

**Field Descriptions**:
- `ID`: Unique deal identifier (e.g., "DEAL-001234")
- `Deal_Name`: Deal/opportunity name (e.g., "ABC Manufacturing - Solar Install Q2")
- `Account_ID`: Link to customer account
- `Account_Name`: Customer company name
- `Product_Category`: Category of products (Solar/Boiler/Water/Mixed)
- `Deal_Amount`: Total deal value in base currency (numeric)
- `Stage`: Current pipeline stage (Prospect / Qualification / Proposal / Negotiation / Closed Won / Closed Lost)
- `Probability`: % likelihood of close (0-100)
- `Expected_Close_Date`: Forecasted close date (YYYY-MM-DD)
- `Closed_Date`: Actual close date if won (YYYY-MM-DD)
- `Created_Date`: When deal was created (YYYY-MM-DD)
- `Last_Modified_Date`: Last update date (YYYY-MM-DD)
- `Sales_Rep_ID`: Owner of the deal
- `Sales_Rep_Name`: Name of sales representative
- `Status`: Win/Loss status (Open / Won / Lost)
- `Lost_Reason`: Why deal was lost (if applicable)
- `Next_Step`: Next action needed
- `Description`: Deal notes/summary

**How to Export**:
1. Zoho CRM → Reports → Create New Report → Deals
2. Filter: All Deals (or Current Month for faster processing)
3. Select all fields listed above
4. Export as CSV/Excel
5. Save as: `Zoho_CRM_Deals_[YYYY-MM-DD].csv`

---

### 2. Accounts/Customers Master

**Export Format**: CSV or Excel
**Update Frequency**: Monthly (or when new accounts added)
**Fields Required**:
```
ID | Account_Name | Industry | Account_Type |
Account_Revenue | Location | Website |
Primary_Contact_Name | Email | Phone |
Parent_Company | Is_Intercompany | Account_Status |
Created_Date | Annual_Contract_Value | Segment
```

**Field Descriptions**:
- `ID`: Unique account identifier
- `Account_Name`: Official company name
- `Industry`: Industry classification (Manufacturing / Construction / Facilities / Retail / Other)
- `Account_Type`: Type of customer (B2B_Business / Hippos / WCI)
- `Account_Revenue`: Annual revenue of customer (numeric, if available)
- `Location`: Primary address/city
- `Website`: Company website URL
- `Primary_Contact_Name`: Main point of contact
- `Email`: Contact email
- `Phone`: Contact phone number
- `Parent_Company`: If subsidiary, name of parent
- `Is_Intercompany`: Flag (Yes/No) - True if WCI or Hippos
- `Account_Status`: Active / Inactive / Prospect
- `Created_Date`: When account was added to CRM
- `Annual_Contract_Value`: ACV if applicable
- `Segment`: Customer segment (Enterprise / Mid-Market / SMB)

**How to Export**:
1. Zoho CRM → Accounts (or Contacts if configured)
2. Select all fields listed above
3. Export as CSV/Excel
4. Save as: `Zoho_CRM_Accounts_[YYYY-MM-DD].csv`

**Special Instructions**:
- Ensure WCI account is flagged as `Is_Intercompany: Yes`
- Ensure Hippos account is flagged as `Is_Intercompany: Yes`
- Mark all B2B customers as `Account_Type: B2B_Business`

---

### 3. Products/Catalog

**Export Format**: CSV or Excel
**Update Frequency**: As needed (when new products added)
**Fields Required**:
```
ID | Product_Name | Product_Category |
SKU | Description | Unit |
Standard_Price | List_Price |
Quantity_in_Stock | Status
```

**Field Descriptions**:
- `ID`: Unique product ID
- `Product_Name`: Official product name
- `Product_Category`: Solar / Boiler / Water Treatment
- `SKU`: Stock keeping unit (internal code)
- `Description`: Product description/specs
- `Unit`: Unit of sale (Each / Pair / Set / Pallet / etc.)
- `Standard_Price`: Standard selling price to B2B customers
- `List_Price`: List price (if different from standard)
- `Quantity_in_Stock`: Current inventory quantity (pull from Zoho Inventory)
- `Status`: Active / Inactive / Discontinued

**How to Export**:
1. Zoho CRM → Products (or Zoho Inventory → Products)
2. Select fields listed above
3. Export as CSV/Excel
4. Save as: `Zoho_CRM_Products_[YYYY-MM-DD].csv`

---

### 4. Sales Team / Users (Optional but Recommended)

**Export Format**: CSV or Excel
**Update Frequency**: Monthly
**Fields Required**:
```
ID | First_Name | Last_Name | Email |
Sales_Region | Manager | Status | Role
```

**Field Descriptions**:
- `ID`: User ID in Zoho
- `First_Name`: Sales rep first name
- `Last_Name`: Sales rep last name
- `Email`: Work email
- `Sales_Region`: Geographic region assigned
- `Manager`: Manager's name
- `Status`: Active / Inactive
- `Role`: Sales Rep / Sales Manager / Director / etc.

**How to Export**:
1. Zoho CRM → Settings → Users & Control → Users
2. Select fields listed above
3. Export as CSV/Excel
4. Save as: `Zoho_CRM_Users_[YYYY-MM-DD].csv`

---

## ZOHO INVENTORY EXPORTS

### 5. Stock/Inventory Levels

**Export Format**: CSV or Excel
**Update Frequency**: Weekly (or daily for high-velocity items)
**Fields Required**:
```
ID | Product_ID | Product_Name | Product_Category |
SKU | Unit_Cost | Quantity_on_Hand | Quantity_Reserved |
Quantity_Available | Reorder_Level | Reorder_Qty |
Warehouse_Location | Last_Stock_Update_Date |
Cost_of_Goods | Inventory_Value
```

**Field Descriptions**:
- `ID`: Unique inventory line item ID
- `Product_ID`: Link to product master
- `Product_Name`: Product name
- `Product_Category`: Solar / Boiler / Water
- `SKU`: Stock keeping unit
- `Unit_Cost`: Cost per unit from WCI or supplier (numeric)
- `Quantity_on_Hand`: Total units in warehouse
- `Quantity_Reserved`: Units already allocated to orders
- `Quantity_Available`: Open to sell (On Hand - Reserved)
- `Reorder_Level`: Minimum quantity before reorder
- `Reorder_Qty`: Quantity to order when hitting reorder level
- `Warehouse_Location`: Location in warehouse (if tracked)
- `Last_Stock_Update_Date`: Last count date
- `Cost_of_Goods`: Unit cost (same as Unit_Cost, for reference)
- `Inventory_Value`: Qty_on_Hand × Unit_Cost

**How to Export**:
1. Zoho Inventory → Products → Stock Levels
2. Select all locations/warehouses
3. Include all fields listed above
4. Export as CSV/Excel
5. Save as: `Zoho_Inventory_Stock_[YYYY-MM-DD].csv`

**Special Instructions**:
- Ensure `Unit_Cost` reflects actual cost from WCI (not selling price)
- Separate line items by warehouse if multiple locations
- Include both active and inactive/discontinued items (mark status separately)

---

### 6. Purchase Orders (from WCI)

**Export Format**: CSV or Excel
**Update Frequency**: Weekly
**Fields Required**:
```
ID | PO_Number | Vendor_ID | Vendor_Name |
PO_Date | Expected_Delivery_Date | Actual_Delivery_Date |
Product_ID | Product_Name | Product_Category |
Quantity_Ordered | Unit_Cost | Line_Total |
PO_Total | Status | Notes
```

**Field Descriptions**:
- `ID`: Unique purchase order ID
- `PO_Number`: PO reference number
- `Vendor_ID`: Link to WCI account
- `Vendor_Name`: Should be "WCI" or manufacturer name
- `PO_Date`: Date PO was created (YYYY-MM-DD)
- `Expected_Delivery_Date`: Forecasted arrival date
- `Actual_Delivery_Date`: When goods arrived (if received)
- `Product_ID`: Product being ordered
- `Product_Name`: Product name
- `Product_Category`: Solar / Boiler / Water
- `Quantity_Ordered`: Number of units on this line
- `Unit_Cost`: Cost per unit from WCI
- `Line_Total`: Qty × Unit Cost
- `PO_Total`: Sum of all line items on this PO
- `Status`: Draft / Sent / Received / Partially Received / Cancelled
- `Notes`: Any special notes (e.g., partial shipment, delay reason)

**How to Export**:
1. Zoho Inventory → Purchase Orders
2. Filter: Vendor = WCI (or all suppliers)
3. Filter: Status includes Open, Received, Partially Received
4. Select fields listed above
5. Export as CSV/Excel
6. Save as: `Zoho_Inventory_PO_[YYYY-MM-DD].csv`

---

### 7. Sales Orders (to All Customers including Hippos)

**Export Format**: CSV or Excel
**Update Frequency**: Weekly
**Fields Required**:
```
ID | Order_Number | Order_Date | Customer_ID | Customer_Name |
Order_Total | Status |
Product_ID | Product_Name | Product_Category |
Quantity_Ordered | Quantity_Shipped |
Unit_Price | Line_Total |
Expected_Ship_Date | Actual_Ship_Date | Is_Intercompany |
Shipping_Address | Notes
```

**Field Descriptions**:
- `ID`: Unique sales order ID
- `Order_Number`: SO reference number
- `Order_Date`: Date order was placed (YYYY-MM-DD)
- `Customer_ID`: Link to customer account
- `Customer_Name`: Customer company name
- `Order_Total`: Total order value
- `Status`: Pending / Processing / Shipped / Delivered / Cancelled / On Hold
- `Product_ID`: Product being ordered
- `Product_Name`: Product name
- `Product_Category`: Solar / Boiler / Water
- `Quantity_Ordered`: Units ordered on this line
- `Quantity_Shipped`: Units actually shipped
- `Unit_Price`: Selling price per unit to this customer
- `Line_Total`: Qty × Unit Price
- `Expected_Ship_Date`: Forecasted shipment date
- `Actual_Ship_Date`: When shipped (if applicable)
- `Is_Intercompany`: Flag (Yes/No) - True if to Hippos
- `Shipping_Address`: Delivery address
- `Notes`: Special instructions, backorder notes, etc.

**How to Export**:
1. Zoho Inventory → Sales Orders
2. Filter: Date Range = Last 12 months (or configurable)
3. Include all customers (B2B + Hippos)
4. Select fields listed above
5. Export as CSV/Excel
6. Save as: `Zoho_Inventory_SO_[YYYY-MM-DD].csv`

**Special Instructions**:
- Flag all orders to Hippos with `Is_Intercompany: Yes`
- Include backorders and cancelled orders (mark in Status)
- Line-by-line detail (not summarized by order)

---

### 8. Invoices & Line Items

**Export Format**: CSV or Excel
**Update Frequency**: Weekly (or daily for recent invoices)
**Fields Required**:
```
Invoice_ID | Invoice_Number | Invoice_Date | Customer_ID | Customer_Name |
Invoice_Amount | Tax_Amount | Invoice_Total |
Payment_Status | Payment_Date |
Product_ID | Product_Name | Product_Category |
Quantity | Unit_Price | Line_Total |
Is_Intercompany | Notes
```

**Field Descriptions**:
- `Invoice_ID`: Unique invoice identifier
- `Invoice_Number`: Invoice reference number
- `Invoice_Date`: Date invoice was issued (YYYY-MM-DD)
- `Customer_ID`: Link to customer
- `Customer_Name`: Customer company name
- `Invoice_Amount`: Subtotal (before tax)
- `Tax_Amount`: Tax charged
- `Invoice_Total`: Total amount due
- `Payment_Status`: Unpaid / Partially Paid / Paid / Overdue
- `Payment_Date`: When payment received (if applicable)
- `Product_ID`: Product on this invoice line
- `Product_Name`: Product name
- `Product_Category`: Solar / Boiler / Water
- `Quantity`: Units invoiced
- `Unit_Price`: Price per unit
- `Line_Total`: Qty × Unit Price
- `Is_Intercompany`: Flag (Yes/No) - True if to Hippos
- `Notes`: Invoice notes/memo

**How to Export**:
1. Zoho Inventory → Invoices (or Zoho Books if using accounting module)
2. Filter: Date Range = Last 12-24 months
3. Include line-item detail (not summary)
4. Select fields listed above
5. Export as CSV/Excel
6. Save as: `Zoho_Inventory_Invoices_[YYYY-MM-DD].csv`

**Special Instructions**:
- One row per line item (not one row per invoice)
- Include both paid and unpaid invoices
- Include both invoices and credit memos (flag memos separately)

---

## ZOHO CRM - OPTIONAL ADVANCED EXPORTS

### 9. Activities (Calls, Emails, Meetings) - OPTIONAL

**Use Case**: Track sales engagement and forecast confidence
**Update Frequency**: Weekly
**Fields Required**:
```
ID | Deal_ID | Deal_Name | Activity_Type |
Activity_Date | Subject | Notes |
Sales_Rep_ID | Sales_Rep_Name | Outcome
```

---

### 10. Pipeline History / Snapshots - OPTIONAL

**Use Case**: Track deal velocity and stage progression
**Update Frequency**: Monthly
**Fields Required**:
```
Deal_ID | Deal_Name | Stage_Date | Previous_Stage |
New_Stage | Amount_Change | Days_in_Previous_Stage |
Status_Update_Date
```

---

## EXPORT SCHEDULE & AUTOMATION

### Recommended Export Schedule

| Export | Frequency | When | Owner |
|--------|-----------|------|-------|
| Deals/Opportunities | Weekly | Every Wednesday | CRM Admin |
| Accounts/Customers | Monthly | 1st of month | CRM Admin |
| Products | As needed | When catalog changes | Inventory Manager |
| Stock/Inventory | Weekly | Every Wednesday | Inventory Manager |
| Purchase Orders (WCI) | Weekly | Every Wednesday | Procurement |
| Sales Orders | Weekly | Every Wednesday | Operations |
| Invoices | Weekly | Every Friday | Finance |
| Sales Team | Monthly | 1st of month | HR/Admin |

### Automation Recommendations

**Option 1: Manual Export (Simple)**
- Create recurring calendar reminders
- Export manually from Zoho each week
- Save to shared folder with standardized naming
- Import into Excel dashboard

**Option 2: Zoho Workflows (Intermediate)**
- Use Zoho CRM Workflows to trigger periodic exports
- Auto-email CSV to team email
- Save to shared Zoho workspace

**Option 3: Zoho API Integration (Advanced)**
- Use Zoho API to auto-sync data
- Direct connection from Zoho to Excel (via Power Query or similar)
- Real-time or scheduled sync (daily/weekly)

---

## FILE NAMING CONVENTION

All exports should follow this naming pattern:

```
[System]_[Report]_[YYYY-MM-DD].csv

Examples:
- Zoho_CRM_Deals_2025-01-31.csv
- Zoho_Inventory_Stock_2025-01-31.csv
- Zoho_Inventory_PO_2025-01-31.csv
- Zoho_Inventory_SO_2025-01-31.csv
- Zoho_Inventory_Invoices_2025-01-31.csv
- Zoho_CRM_Accounts_2025-01-31.csv
```

---

## IMPORT INTO EXCEL DASHBOARD

The `solartech_dashboard.xlsx` file has dedicated import sheets labeled:

- **[Raw] Deals** - Paste Deals CSV here
- **[Raw] Accounts** - Paste Accounts CSV here
- **[Raw] Products** - Paste Products CSV here
- **[Raw] Stock** - Paste Stock/Inventory CSV here
- **[Raw] PO** - Paste Purchase Orders CSV here
- **[Raw] SO** - Paste Sales Orders CSV here
- **[Raw] Invoices** - Paste Invoices CSV here

Instructions for importing:
1. Open exported CSV in Excel or text editor
2. Copy all data (Ctrl+A, Ctrl+C)
3. Go to corresponding [Raw] sheet in dashboard
4. Paste starting at cell A1 (Ctrl+V)
5. All dashboards will auto-populate from the raw data

---

## DATA QUALITY CHECKLIST

Before importing, verify:

- [ ] All date fields are in YYYY-MM-DD format
- [ ] All numeric fields have no currency symbols or thousand separators
- [ ] No blank rows in the middle of data
- [ ] Customer IDs match between CRM and Inventory (if applicable)
- [ ] Product IDs are consistent across all exports
- [ ] WCI is flagged as "Is_Intercompany: Yes"
- [ ] Hippos is flagged as "Is_Intercompany: Yes"
- [ ] No duplicate records
- [ ] All required fields are present (no missing columns)

---

## Troubleshooting

**Q: Where do I find the Deals report in Zoho CRM?**
A: CRM → Reports → Create New Report → Select Module "Deals" → Choose "Standard" report type

**Q: How do I filter for only open deals?**
A: When creating the report, add filter: Status = Open (or Stage ≠ Closed Won / Closed Lost)

**Q: Can I automate these exports?**
A: Yes, see "Automation Recommendations" section above. Zoho Workflows or API recommended.

**Q: What if a field doesn't exist in our Zoho setup?**
A: It's OK to omit optional fields. Required fields are noted with asterisks (*) in the specs.

**Q: How far back should I export historical data?**
A: For first setup: 24 months of sales orders and invoices. For ongoing: Previous month + current month only.

---

## Contact & Support

For questions about these data requirements:
- Reach out to the BizOS Operations team
- Reference this document
- Provide sample CSV to troubleshoot issues
