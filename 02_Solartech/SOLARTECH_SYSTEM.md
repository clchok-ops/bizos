# Solartech Operations Framework

## Business Overview

**Company**: Solartech
**Model**: B2B Distribution
**Products**: Solar systems, boiler systems, water treatment products
**Primary Role**: Distributor/Wholesaler to businesses

### Organizational Structure
- **Parent Company**: Solartech (Operations HQ)
- **Manufacturing Partner**: WCI (supplier, manufacturer)
- **Retail Partner**: Hippos (B2C distribution, customer of Solartech)
- **Zoom Integration**: Zoho One ecosystem (CRM, Inventory, Analytics)

### Business Model
1. **Upstream**: Purchase products from WCI (manufacturing partner)
2. **Core Operations**: Warehouse inventory management, quality control, order fulfillment
3. **Downstream Distribution**: B2B sales to businesses + Hippos (B2C arm)
4. **Intercompany Relations**: Track both WCI purchases (cost of goods) and Hippos sales (revenue channel)

---

## Key Business Metrics

### Sales & Pipeline Metrics
- **Pipeline Value**: Total value of all open deals by stage
- **Win Rate**: Percentage of deals closed won vs. total closed (won + lost)
- **Sales Cycle Time**: Average days from opportunity creation to close date
- **Deal Size**: Average value per deal, by product line and customer segment
- **Monthly Recurring Revenue (MRR)**: Predictable revenue from contracts/frameworks
- **Revenue by Product Line**: Solar, Boiler, Water treatment breakdown

### Margin & Profitability
- **Gross Margin %**: (Revenue - COGS) / Revenue, by product line and customer
- **Net Margin %**: Profit after all operational expenses
- **Margin by Customer**: Highest/lowest margin customers
- **Intercompany Margin**: Markup on products from WCI to Hippos
- **COGS Tracking**: Product cost from WCI vs. selling price

### Inventory Metrics
- **Inventory Turnover Ratio**: COGS / Average Inventory Value
- **Days Inventory Outstanding (DIO)**: Days inventory sits before sale
- **Stock-Out Events**: Number of times unable to fulfill order
- **Inventory by Product Line**: Quantities and values in warehouse
- **Slow-Moving SKUs**: Products sitting longer than 90 days
- **Inventory Accuracy**: Physical counts vs. system records

### Intercompany Transactions
- **WCI Purchase Orders**: Monthly spend with manufacturing partner
- **Hippos Sales**: Monthly revenue to retail arm
- **Hippos Sell-Through Rate**: What Hippos actually sells to consumers
- **Intercompany Margins**: Markup between WCI cost and Hippos sale price
- **Inventory Held for Hippos**: Stock levels at Solartech allocated to Hippos

### Operational Metrics
- **Order Fulfillment Rate**: % of orders shipped on time, complete
- **Lead Time**: Days from order receipt to shipment
- **Customer Retention Rate**: % of previous year customers active this year
- **Account Growth**: Revenue growth per customer year-over-year

---

## Zoho Data Integration

### Source Systems
- **Zoho CRM**: Sales pipeline, customer data, deal tracking
- **Zoho Inventory**: Product master, stock levels, purchase/sales orders
- **Zoho Analytics**: Business intelligence, reporting (optional destination)

### Required Exports from Zoho CRM
1. **Deals/Opportunities Table**
   - Deal ID, Deal Name, Customer ID, Customer Name, Product Category
   - Deal Amount, Stage, Expected Close Date, Actual Close Date
   - Created Date, Last Modified Date, Owner (sales rep)
   - Status (Open, Won, Lost)

2. **Customers/Accounts Table**
   - Account ID, Account Name, Account Type (Business, Hippos, WCI)
   - Industry, Location, Revenue, Customer Segment
   - Contact Person, Email, Phone
   - Is Intercompany (Yes/No), Parent Company ID

3. **Products Table**
   - Product ID, Product Name, Product Category (Solar/Boiler/Water)
   - SKU, Standard Price, Cost Price (from WCI)

4. **Activities/Interactions** (optional for engagement tracking)
   - Call logs, email history, meeting notes

### Required Exports from Zoho Inventory
1. **Stock/Inventory Table**
   - Product ID, Product Name, Product Category
   - Unit Cost (from WCI), Quantity in Stock, Quantity Reserved
   - Warehouse Location, Last Updated Date
   - Reorder Level, Reorder Quantity

2. **Purchase Orders** (from WCI)
   - PO ID, PO Date, Vendor (WCI), Delivery Date
   - Product ID, Quantity, Unit Cost, Total Cost
   - Status (Draft, Sent, Received, Cancelled)

3. **Sales Orders** (to customers and Hippos)
   - Order ID, Order Date, Customer/Account ID, Customer Name
   - Product ID, Product Name, Quantity, Unit Price, Total Amount
   - Status (Pending, Shipped, Delivered), Shipment Date
   - Is Intercompany (flag for Hippos orders)

4. **Invoice Data**
   - Invoice ID, Date, Customer, Amount, Payment Status
   - Line items (Product, Qty, Unit Price, Extended Price)

### Data Export Frequency
- **Daily**: Current inventory levels, open orders
- **Weekly**: Pipeline snapshots, sales activity
- **Monthly**: Complete financial data, margin analysis, full intercompany reconciliation

---

## Dashboard Specifications

### Dashboard 1: Sales Pipeline (Real-Time)
**Purpose**: Monitor deal flow and revenue forecast

**Components**:
- **Pipeline Value by Stage**: Chart showing total $ in each stage (Prospect, Qualification, Proposal, Negotiation, Closed Won)
- **Deal Count by Stage**: Number of deals in each stage
- **Win/Loss Metrics**: Win rate %, average deal size, sales cycle time
- **Top Customers**: Revenue by top 10 accounts
- **Sales Rep Performance**: Revenue, deal count, win rate per sales team member
- **Forecast Accuracy**: Projected close date vs. actual (for historical periods)

**Frequency**: Updated daily from CRM

### Dashboard 2: Margin & Profitability (Monthly)
**Purpose**: Track margin performance by product line and customer

**Components**:
- **Gross Margin % by Product Line**: Solar, Boiler, Water treatment breakdown
- **Margin by Top Customers**: Highest and lowest margin customers
- **COGS vs. Revenue Trend**: 12-month trend chart
- **Intercompany Margin Analysis**:
  - WCI purchase price → Solartech sale price → Hippos sale price
  - Markup % at each stage
- **Margin Variance**: Actual vs. target margin by product
- **Product Mix**: % of revenue by product category

**Frequency**: Updated monthly (post-close)

### Dashboard 3: Inventory Health (Weekly)
**Purpose**: Monitor stock levels, turnover, and potential issues

**Components**:
- **Inventory Turnover Ratio**: Days inventory outstanding (DIO)
- **Stock Level Summary**:
  - Total inventory value by product line
  - Quantity on hand by product
  - Value at risk (inventory > 90 days)
- **Slow-Moving Products**: Products below reorder level or > 90 days old
- **WCI Purchase Status**: Open POs, on-order quantities, delivery dates
- **Hippos Allocation**: How much inventory is committed to/held for Hippos
- **Stock-Out Risk**: Products near minimum stock level

**Frequency**: Updated weekly (synced from Zoho Inventory)

### Dashboard 4: Intercompany Tracking (Monthly)
**Purpose**: Monitor relationships with WCI (upstream) and Hippos (downstream)

**Components**:
- **WCI Purchases**: Monthly spend, YTD total, top products by volume
- **Hippos Sales**: Monthly revenue, YTD total, top products sold
- **Hippos Sell-Through**: What Hippos sold to consumers vs. what they bought from Solartech
- **Inventory Allocation**: What's held for Hippos vs. other customers
- **Intercompany Margins**: Markup between WCI cost and Hippos price
- **Payment Status**: Payables to WCI, receivables from Hippos

**Frequency**: Updated monthly

### Dashboard 5: Operations Summary (Executive)
**Purpose**: High-level business health scorecard

**Components**:
- **Revenue YTD**: Actual vs. plan (budget)
- **Gross Profit YTD**: $ and %
- **Key Metrics Scorecard**:
  - Order fulfillment rate (%)
  - Customer retention rate (%)
  - Inventory turnover (days)
  - Days sales outstanding (DSO)
- **Alerts**: Stock-outs, overdue orders, large deals at risk
- **Trend Indicators**: Red/yellow/green status for key metrics

**Frequency**: Updated daily

---

## Data Model & Relationships

### Core Entities
```
Customers (Accounts)
├── B2B Businesses (primary customers)
├── Hippos (intercompany, B2C retail arm)
└── WCI (intercompany, supplier/manufacturer)

Products
├── Solar Systems
├── Boiler Systems
└── Water Treatment

Deals/Opportunities
├── Customer ID → Customers
├── Product Category → Products
└── Sales Rep ID → Users

Inventory/Stock
├── Product ID → Products
├── Warehouse Location
└── Reserved Qty → (to Hippos or specific customer)

Purchase Orders (from WCI)
├── Vendor ID → WCI account
└── Product ID → Products

Sales Orders
├── Customer ID → Customers
├── Product ID → Products
└── Intercompany Flag (True if to Hippos)

Invoices
├── Customer ID → Customers
├── Sales Order ID → Sales Orders
└── Line Items (Product, Qty, Price)
```

---

## Integration Workflow

### Monthly Operations Cycle

1. **1st of Month**:
   - Export prior month data from Zoho CRM (deals, customers)
   - Export invoice data from Zoho Inventory/Accounting
   - Calculate month-end financials

2. **Week 1**:
   - Update Dashboard 2 (Margin & Profitability)
   - Update Dashboard 4 (Intercompany Tracking)
   - Generate management reports

3. **Week 2**:
   - Review pipeline with sales team
   - Adjust forecasts based on recent activity

4. **Weekly (Every Wed)**:
   - Update Dashboard 1 (Pipeline) from CRM
   - Update Dashboard 3 (Inventory) from Zoho Inventory
   - Monitor for stock-outs or overstock situations

5. **Daily**:
   - Dashboard 5 (Operations Summary) auto-refreshes
   - Alerts trigger for exceptions (overdue orders, low stock)

---

## Success Criteria

- **Pipeline Visibility**: Can forecast revenue by stage with 85%+ accuracy
- **Margin Management**: Identify and address margin erosion within 5 days
- **Inventory Efficiency**: Maintain inventory turnover within target range (specify based on products)
- **Intercompany Clarity**: Full visibility into WCI costs and Hippos performance
- **Order Fulfillment**: 95%+ on-time, complete order fulfillment rate
- **Customer Growth**: Track top 20 customers for growth and retention

---

## File Locations & References

- **Dashboard Workbook**: `/sessions/focused-clever-maxwell/mnt/BizOS/02_Solartech/solartech_dashboard.xlsx`
- **Data Requirements**: `/sessions/focused-clever-maxwell/mnt/BizOS/02_Solartech/DATA_REQUIREMENTS.md`
- **Zoho CRM Export**: [To be imported from Zoho interface]
- **Zoho Inventory Export**: [To be imported from Zoho interface]

---

## Next Steps

1. Define KPI targets and thresholds (what's "good" performance?)
2. Set up automated Zoho exports (daily/weekly/monthly)
3. Configure data import process into Excel dashboards
4. Establish monthly review cadence with stakeholders
5. Train team on dashboard interpretation and action items
