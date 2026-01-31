# Solartech Dashboard - Formula Reference Guide

This document explains the formulas used in the dashboard and how they work.

## Sheet Cross-References

All analysis dashboards pull data from raw import sheets:

```
Pipeline Tracker      → uses _RAW_Deals (Columns A-G)
Margin Analysis       → uses _RAW_Invoices (Columns A-E) + _RAW_Stock (Columns A-G)
Inventory Status      → uses _RAW_Stock (Columns A-G)
Intercompany Tracking → uses _RAW_PO (Columns A-D) + _RAW_SO (Columns A-D)
Monthly KPIs          → Manual input (blue font cells)
```

---

## Pipeline Tracker Formulas

### Basic Pipeline Analysis

For each sales stage (Prospect, Qualification, Proposal, Negotiation, Closed Won, Closed Lost):

**Column B: Deal Count**
```excel
=COUNTIF(_RAW_Deals!F:F,"[Stage Name]")
```
- Counts all deals where Stage (column F) equals the named stage
- Example: `=COUNTIF(_RAW_Deals!F:F,"Prospect")`

**Column C: Total Value**
```excel
=SUMIF(_RAW_Deals!F:F,"[Stage Name]",_RAW_Deals!E:E)
```
- Sums Deal Amount (column E) for all deals in that stage
- Example: `=SUMIF(_RAW_Deals!F:F,"Prospect",_RAW_Deals!E:E)`

**Column D: Avg Deal Size**
```excel
=IFERROR(C[Row]/B[Row],0)
```
- Divides Total Value by Deal Count
- IFERROR returns 0 if no deals exist (prevents #DIV/0! error)
- Example: `=IFERROR(C5/B5,0)`

**Column E: Min Deal**
```excel
=IFERROR(MINIFS(_RAW_Deals!E:E,_RAW_Deals!F:F,"[Stage Name]"),"-")
```
- Finds minimum deal amount in that stage
- Returns "-" if no data exists
- Example: `=IFERROR(MINIFS(_RAW_Deals!E:E,_RAW_Deals!F:F,"Prospect"),"-")`

**Column F: Max Deal**
```excel
=IFERROR(MAXIFS(_RAW_Deals!E:E,_RAW_Deals!F:F,"[Stage Name]"),"-")
```
- Finds maximum deal amount in that stage
- Returns "-" if no data exists

**Column G: Probability Avg**
```excel
=IFERROR(AVERAGEIF(_RAW_Deals!F:F,"[Stage Name]",_RAW_Deals!G:G),0)
```
- Calculates average probability for all deals in that stage
- Probability comes from column G in raw data
- Returns 0 if no deals

**Column H: Forecast**
```excel
=IFERROR(C[Row]*(G[Row]/100),0)
```
- Multiplies Total Value by Probability percentage to get weighted forecast
- Example: $1M pipeline × 50% probability = $500K forecast
- Divides by 100 because probability is stored as 0-100 (not 0-1)

### Summary Metrics

**Open Pipeline** (sum of Prospect through Negotiation stages)
```excel
=SUM(C5:C8)
```

**Total Pipeline** (all deals open + closed)
```excel
=SUM(C5:C11)
```

**Win Rate %**
```excel
=IFERROR(C10/(C10+C11),0)
```
- C10 = Closed Won deals
- C11 = Closed Lost deals
- Calculates: Won / (Won + Lost)
- Returns 0 if no closed deals (prevents #DIV/0!)

---

## Margin Analysis Formulas

### Margin by Product Line

For each product category (Solar, Boiler, Water Treatment):

**Column B: Total Revenue**
```excel
=SUMIF(_RAW_Invoices!B:B,"[Category]",_RAW_Invoices!E:E)
```
- Sums Line Total (column E) for all invoices in that product category
- Example: `=SUMIF(_RAW_Invoices!B:B,"Solar",_RAW_Invoices!E:E)`

**Column C: Total COGS**
```excel
=SUMIF(_RAW_Stock!C:C,"[Category]",_RAW_Stock!F:F)
```
- Sums Inventory Value (column F) from stock sheet for that category
- Note: This assumes Inventory Value = Unit Cost × Qty on Hand

**Column D: Gross Profit**
```excel
=B[Row]-C[Row]
```
- Simple subtraction: Revenue - COGS
- Example: `=B5-C5`

**Column E: Gross Margin %**
```excel
=IFERROR(D[Row]/B[Row],0)
```
- (Gross Profit / Revenue) × 100%
- Formatted as percentage (0.0"%")
- Returns 0 if no revenue (prevents #DIV/0!)

### Totals Row

Uses SUM and same formulas as above to aggregate across all product categories.

---

## Inventory Status Formulas

### Inventory by Product Line

For each product category (Solar, Boiler, Water Treatment):

**Column B: Qty on Hand**
```excel
=SUMIF(_RAW_Stock!C:C,"[Category]",_RAW_Stock!D:D)
```
- Sums Qty on Hand (column D) for that category
- Example: `=SUMIF(_RAW_Stock!C:C,"Solar",_RAW_Stock!D:D)`

**Column C: Inventory Value**
```excel
=SUMIF(_RAW_Stock!C:C,"[Category]",_RAW_Stock!F:F)
```
- Sums Inventory Value (column F) for that category
- Uses: Unit Cost × Qty on Hand (pre-calculated in raw data)

**Column D: Reorder Level**
```excel
=SUMIF(_RAW_Stock!C:C,"[Category]",_RAW_Stock!G:G)
```
- Sums all reorder levels for that category
- Used to trigger alerts when Qty on Hand falls below this

**Column E: Days Inventory Outstanding (DIO)**
```excel
=IFERROR((C[Row]/Settings!$B$2)/30,0)
```
- Calculates: (Inventory Value / Monthly COGS) × 30 days
- Uses Monthly COGS from Settings sheet cell B2
- Lower is better (faster turnover)
- Example: `=IFERROR((C5/Settings!$B$2)/30,0)`
- Note: Divide by 30 to get days (COGS is monthly)

**Column F: Status Alert**
```excel
=IF(B[Row]<D[Row],"REORDER",IF(E[Row]>90,"SLOW","OK"))
```
- Three-level logic:
  - If Qty < Reorder Level → "REORDER" (urgent)
  - Else if Days > 90 → "SLOW" (slow-moving)
  - Else → "OK" (healthy)
- Example: `=IF(B5<D5,"REORDER",IF(E5>90,"SLOW","OK"))`

---

## Intercompany Tracking Formulas

### Intercompany Margin Analysis

For each product in the markup chain:

**Column B: WCI Cost** (input - blue font)
```
User enters the cost price from WCI
Example: $1,500
```

**Column C: Solartech Price** (input - blue font)
```
User enters Solartech's selling price to Hippos
Example: $1,800
```

**Column D: Hippos Price** (input - blue font)
```
User enters Hippos's retail price to consumers
Example: $2,400
```

**Column E: Total Markup %**
```excel
=IFERROR((D[Row]-C[Row])/C[Row],0)
```
- Calculates Hippos's markup as percentage
- (Hippos Price - Solartech Price) / Solartech Price
- Shows how much Hippos marks up from Solartech
- Returns 0 if no Solartech price

**Markup Chain Breakdown Example:**
```
WCI Cost:          $1,500        (Manufacturer's cost)
↓ Solartech +20%
Solartech Price:   $1,800        (+$300 markup)
↓ Hippos +33%
Hippos Price:      $2,400        (+$600 markup)
↓
Consumer:          $2,400        (Final retail)

Solartech Margin:  $300 / $1,500 = 20.0%
Hippos Markup:     (2400-1800)/1800 = 33.3%
```

---

## Monthly KPIs Sheet

### KPI Input Format

All KPI metrics use blue font for inputs. They're divided into three types:

**Financial Metrics:**
```excel
Number Format: $#,##0;($#,##0);-
Examples: Revenue ($), Profit ($), Inventory Value ($)
```

**Percentage Metrics:**
```excel
Number Format: 0.0"%"
Examples: Margin %, Win Rate %, Fulfillment Rate %
```

**Count Metrics:**
```excel
Number Format: #,##0
Examples: Deals Closed, Customer Count
```

### Formula Pattern (if using auto-calculation)

To sum pipeline value from Pipeline Tracker:
```excel
='Pipeline Tracker'!C13
```

To sum from invoices (if not using Pipeline Tracker):
```excel
=SUMIF(_RAW_Invoices!B:B,"*",_RAW_Invoices!E:E)
```

---

## Common Formula Patterns Used

### 1. SUMIF (Single Condition)
```excel
=SUMIF(range_to_check, criteria, sum_range)
```
**Use when**: You want to sum values that match one condition
**Example**: `=SUMIF(_RAW_Stock!C:C,"Solar",_RAW_Stock!F:F)` (sum inventory value where category = Solar)

### 2. COUNTIF (Count with Condition)
```excel
=COUNTIF(range_to_check, criteria)
```
**Use when**: You want to count items matching a condition
**Example**: `=COUNTIF(_RAW_Deals!F:F,"Prospect")` (count deals in Prospect stage)

### 3. AVERAGEIF (Average with Condition)
```excel
=AVERAGEIF(range_to_check, criteria, average_range)
```
**Use when**: You want average of values matching a condition
**Example**: `=AVERAGEIF(_RAW_Deals!F:F,"Prospect",_RAW_Deals!G:G)` (avg probability of Prospect deals)

### 4. MINIFS / MAXIFS (Min/Max with Condition)
```excel
=MINIFS(min_range, criteria_range, criteria)
=MAXIFS(max_range, criteria_range, criteria)
```
**Use when**: You want minimum/maximum of values matching criteria
**Example**: `=MAXIFS(_RAW_Deals!E:E,_RAW_Deals!F:F,"Prospect")` (largest deal in Prospect stage)

### 5. IFERROR (Error Handling)
```excel
=IFERROR(formula, fallback_value)
```
**Use when**: You want to prevent errors (#DIV/0!, #VALUE!, etc.)
**Example**: `=IFERROR(C5/B5,0)` (divide, but return 0 if denominator is 0)

### 6. IF (Conditional Logic)
```excel
=IF(condition, value_if_true, value_if_false)
=IF(condition1, value1, IF(condition2, value2, value3))  [nested]
```
**Example**: `=IF(B5<D5,"REORDER",IF(E5>90,"SLOW","OK"))`

---

## Data Flow Diagram

```
                         ZOHO SYSTEMS
                    ┌──────┬──────────┐
                    │ Zoho  │  Zoho   │
                    │ CRM   │ Inventory│
                    └──────┴──────────┘
                         │      │
        CSV/Excel Exports │      │ CSV/Excel Exports
                         ▼      ▼
        ┌──────────────────────────────────┐
        │    solartech_dashboard.xlsx      │
        ├──────────────────────────────────┤
        │   RAW DATA IMPORT SHEETS:        │
        │  • _RAW_Deals (CRM)              │
        │  • _RAW_Invoices (Inventory)     │
        │  • _RAW_Stock (Inventory)        │
        │  • _RAW_PO (Inventory - WCI)     │
        │  • _RAW_SO (Inventory)           │
        │  • Settings                      │
        └──────────────────────────────────┘
                         │
        ┌────────────────┼────────────────────┐
        │                │                    │
        ▼                ▼                    ▼
    ┌─────────┐  ┌──────────────┐  ┌──────────────────┐
    │Pipeline │  │  Margin      │  │  Inventory       │
    │Tracker  │  │  Analysis    │  │  Status          │
    └─────────┘  └──────────────┘  └──────────────────┘
        │                │                    │
        └────────────────┼────────────────────┘
                         │
        ┌────────────────┼────────────────────┐
        │                │                    │
        ▼                ▼                    ▼
   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
   │Intercompany  │  │  Monthly     │  │  Executive   │
   │Tracking      │  │  KPIs        │  │  Reviews     │
   └──────────────┘  └──────────────┘  └──────────────┘
```

---

## Troubleshooting Formula Errors

### #DIV/0! Error (Division by Zero)
**Cause**: Denominator is 0
**Solution**: Use IFERROR() wrapper
```excel
# Wrong:
=C5/B5

# Right:
=IFERROR(C5/B5,0)
```

### #REF! Error (Invalid Cell Reference)
**Cause**: Cell reference is broken (sheet deleted, column moved)
**Solution**:
- Check that _RAW_ sheet names haven't changed
- Verify columns haven't been deleted or reordered
- Use Ctrl+` to show all formulas and inspect carefully

### #VALUE! Error (Wrong Data Type)
**Cause**: Formula expects number but got text
**Solution**:
- Ensure raw data columns are all numbers (not text)
- Check for $ signs or text mixed in numbers
- Use VALUE() function to convert text to numbers if needed

### #NAME? Error (Unrecognized Function)
**Cause**: Typo in function name or unsupported function
**Solution**:
- Verify spelling of function (SUMIF, COUNTIF, etc.)
- Ensure function is supported in your Excel version
- Check for missing parentheses

---

## Extending the Framework

### Adding a New Product Category

1. Go to relevant analysis sheet (e.g., Margin Analysis)
2. Add new row after existing categories
3. Copy formulas from row above, change "Solar" to "NewCategory"
4. Update TOTAL formulas to include new category (e.g., SUM(B5:B8) instead of SUM(B5:B7))

### Adding New Deals/Customers

1. Just paste new export data into _RAW_Deals sheet
2. All Pipeline Tracker metrics auto-update
3. New customers appear in totals

### Adding New Intercompany Products

1. Go to Intercompany Tracking sheet
2. Add new row in "Markup Analysis" section
3. Enter product name and three prices (WCI cost, Solartech price, Hippos price)
4. Formula for markup % auto-calculates

### Changing Reporting Periods

1. Go to Settings sheet
2. Update "Fiscal Year Start Month" in cell B4 (1=Jan, 6=June, etc.)
3. Dates in raw data will recalculate based on fiscal calendar

---

## Best Practices for Formulas

1. **Always use cell references, not hardcoded values**
   - Use: `=SUM(B2:B10)`
   - Not: `=100 + 50 + 25`

2. **Use IFERROR for division and risky operations**
   - Prevents #DIV/0! and other errors from breaking dashboards

3. **Reference other sheets explicitly**
   - Use: `=SUM(_RAW_Deals!C:C)`
   - Not: `=SUM(_RAW_Deals.C:C)` (different syntax)

4. **Keep logic in Settings sheet for easy updates**
   - Monthly COGS, currency, fiscal year settings
   - Avoids hunting through 10 formulas to change one assumption

5. **Name important ranges for clarity**
   - In Excel: Formulas → Define Name
   - Use: `=SUM(monthly_revenue)` instead of `=SUM(B2:B13)`

6. **Document complex formulas with comments**
   - Right-click cell → Insert Comment
   - Explain purpose and data assumptions

