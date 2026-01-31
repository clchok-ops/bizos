# WCI (Water-Care Industries) Framework

## Business Overview

**Company**: Water-Care Industries (WCI)
**Industry**: Boiler Manufacturing (B2B/B2B2C)
**Operations**: Manufacturing, MRP, Inventory Management, Sales/CRM
**ERP System**: Odoo (MRP, Inventory, Sales modules)

### Distribution Channels

1. **Solartech** (B2B Distributor)
   - Wholesale channel
   - Volume discounts apply
   - Transfer pricing model: Cost + margin allocation
   - Lead times: Standard 5-10 business days

2. **Hippos** (B2C Retail)
   - End consumer retail channel
   - Direct-to-consumer pricing
   - Higher margin structure
   - Lead times: Standard 3-5 business days

### Product Categories

- **Standard Boilers**: High volume, established BOMs
- **Custom Boilers**: Lower volume, engineered-to-order
- **Spare Parts/Accessories**: Service and maintenance products

---

## Key Performance Indicators (KPIs)

### Production Performance

| KPI | Target | Formula | Frequency |
|-----|--------|---------|-----------|
| **On-Time Delivery Rate** | 95% | (Orders delivered on scheduled date / Total orders) × 100 | Weekly |
| **Scrap Rate** | 2.5% | (Total scrap cost / Total production cost) × 100 | Daily |
| **Production Backlog** | < 5 days | Sum of unfulfilled production orders in days of output | Weekly |
| **Unit Production Cost** | TBD by SKU | Total production cost / Units produced | Monthly |
| **Capacity Utilization** | 85% | (Actual machine hours / Available machine hours) × 100 | Weekly |
| **First-Pass Yield** | 95% | (Units passing QA first inspection / Total units inspected) × 100 | Daily |

### Inventory Metrics

| KPI | Target | Formula | Frequency |
|-----|--------|---------|-----------|
| **Raw Material Inventory Turnover** | 8× annually | Cost of goods sold / Average raw material inventory | Monthly |
| **WIP Inventory** | 3-5 days | Sum of WIP value at cost | Weekly |
| **Finished Goods Turn** | 6× annually | Cost of goods sold / Average FG inventory | Monthly |
| **Inventory Accuracy** | 99% | (Counted units matching system / Total counted units) × 100 | Monthly |

### Order & Sales Metrics

| KPI | Target | Formula | Frequency |
|-----|--------|---------|-----------|
| **Order Fulfillment Cycle** | 10 days average | Days from order receipt to shipment | Per order |
| **Lead Time Variance** | ±2 days | Actual cycle time - Planned cycle time | Weekly |
| **Solartech On-Time Rate** | 96% | Deliveries to Solartech within agreed lead time | Weekly |
| **Hippos On-Time Rate** | 94% | Deliveries to Hippos within agreed lead time | Weekly |

---

## Odoo Data Requirements

### MRP Module
- **Production Orders**: Status, dates, planned vs actual quantities
- **Work Orders**: Resource assignments, cycle times, scrap records
- **BOMs**: Product structures, component quantities, operation sequences
- **Routings**: Machine assignments, labor hours, operation durations
- **Quality Checks**: Inspection results, rework occurrences

### Inventory Module
- **Stock Levels**: Current quantities by location (Raw Materials, WIP, Finished Goods)
- **Stock Moves**: All transactions (purchases, production issues, shipments)
- **Valuation**: Cost accounting (Standard, FIFO, or Average cost)
- **Warehouse Locations**: Raw materials, WIP, FG, rejected stock
- **Cycle Counts**: Physical inventory adjustments

### Sales/CRM Module
- **Sales Orders**: Customer, date, delivery date, line items, quantities
- **Delivery Dates**: Promised vs actual
- **Customer Pricing**: Solartech wholesale rates vs Hippos retail rates
- **Invoice Data**: Revenue recognition by customer/product
- **Order Notes**: Delivery preferences, special handling

---

## Manufacturing KPIs & Formulas

### Cost Analysis
```
Total Production Cost =
  (Raw Material Cost) +
  (Direct Labor Cost) +
  (Manufacturing Overhead) +
  (Scrap/Rework Cost)

Unit Production Cost = Total Production Cost / Units Produced

COGS (per unit) = Material Cost + Labor Cost + Allocated Overhead
```

### Quality Metrics
```
Scrap Rate (%) = (Total Scrap $ / Total Production $) × 100
  - Target: 2.5% or less
  - Tracked by: Work order, operation, material

Rework Cost = Labor + Material consumed in rework
  - Should be separate from scrap rate
  - Tracked by: Root cause analysis

First-Pass Yield (%) = (Good units / Total units produced) × 100
  - Excludes reworked units
  - Target: 95%+
```

### Schedule Adherence
```
On-Time Delivery Rate (%) =
  (Orders shipped by promised date / Total orders) × 100

Late Orders = Orders shipped after promised date
  - By # of days late
  - By customer (Solartech vs Hippos)

Production Backlog (days) =
  Sum of all open production orders / Average daily output

Lead Time Performance =
  (Actual lead time - Planned lead time) / Planned lead time × 100
  - Positive = delayed
  - Negative = early (less critical)
```

---

## Transfer Pricing Considerations

### Solartech (B2B Wholesale)

**Pricing Model**: Cost + Agreed Margin
- Used to allocate manufacturing costs fairly
- Ensures WCI recognizes fair value of goods manufactured
- Basis for inter-company transfer pricing compliance

```
Solartech Transfer Price =
  (Standard Manufacturing Cost per unit) × (1 + Margin %)

Standard Manufacturing Cost per unit =
  Material Cost + Direct Labor + Allocated Overhead

Typical Margin: 15-25% (depends on market, volume)
```

**Key Inputs**:
- Bill of Materials with current material costs
- Direct labor hours and rates
- Manufacturing overhead allocation rate
- Volume discounts applied to material purchases

### Hippos (B2C Retail)

**Pricing Model**: Cost + Markup (Higher than wholesale)
- Higher pricing reflects retail channel economics
- Accounts for: packaging, handling, retail margin expectation
- Base unit cost = Solartech transfer price or direct cost calc

```
Hippos Sales Price =
  (Standard Manufacturing Cost per unit) × (1 + Retail Markup %)

Typical Retail Markup: 50-100% (varies by product)
```

**Adjustments**:
- Promotional discounts
- Volume tiering for bulk orders
- Channel-specific packaging/prep costs

### Internal Governance

1. **Cost Basis Review**: Quarterly review of standard costs
2. **Variance Tracking**: Actual vs standard cost performance
3. **Margin Monitoring**: Ensure profitability at both channels
4. **Compliance**: Documentation for transfer pricing regulations
5. **Volume Planning**: Forecast demand to optimize manufacturing runs

---

## Data Flow Architecture

```
Odoo System
├── MRP Module
│   ├── Production Orders (Manufacturing)
│   ├── Work Orders (Operations & Labor)
│   ├── BOMs (Product structure)
│   └── Routings (Processes)
├── Inventory Module
│   ├── Raw Materials (Receipts)
│   ├── WIP (In-progress jobs)
│   ├── Finished Goods (Ready to ship)
│   └── Stock Moves (All transactions)
└── Sales/CRM Module
    ├── Sales Orders (Solartech & Hippos)
    ├── Delivery Records
    └── Invoice/Revenue

↓ Exports (Weekly/Monthly) ↓

Dashboard System (wci_dashboard.xlsx)
├── Production Tracker
├── BOM Costing
├── Inventory Status
├── Transfer Pricing
└── Monthly KPIs
```

---

## Dashboard Update Frequency

| Sheet | Frequency | Data Source | Responsibility |
|-------|-----------|-------------|-----------------|
| Production Tracker | Daily | MRP + Inventory | Production Manager |
| BOM Costing | Monthly | MRP + Inventory + GL | Accounting |
| Inventory Status | Weekly | Inventory + Stock Moves | Inventory Manager |
| Transfer Pricing | Monthly | BOM Costing + Sales | Finance Director |
| Monthly KPIs | Monthly | All above + Sales | Operations Manager |

---

## Success Criteria

- Dashboard updates within 2 business days of month-end close
- All formulas auto-calculate from raw Odoo exports
- Scrap rate tracked and trended
- On-time delivery to both customers > 94%
- Production backlog never exceeds 5 days
- Inventory accuracy > 99%
- Standard costs maintained within ±5% of actual
