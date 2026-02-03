# Solartech Pricing System Validation Report
**Date:** 2026-02-03
**Validated by:** Claude (CTO Review Bot)

---

## Executive Summary

| Metric | Status |
|--------|--------|
| Files Validated | 3 |
| Total Issues Found | 6 critical, 4 warnings |
| Data Coverage | 352 of 2,751 SKUs have pricing (13%) |
| Composite Coverage | 31/31 composites have pricing (100%) |

**Overall Assessment:** ⚠️ **Needs Attention** - Significant gaps in pricing coverage and data quality issues need resolution before Zoho sync.

---

## 1. SKU Naming Convention Analysis

### Item SKU Prefixes (from Item Master)
| Prefix | Count | Example | Likely Category |
|--------|-------|---------|-----------------|
| T | 452 | T-524, T-0068 | Generic/Legacy items |
| COMP | 409 | COMP-008152 | Composite items |
| D | 170 | DTSD1352, DS3-H | Direct/Distribution |
| SKU | 85 | SKU-3Pin-01 | Standard items |
| PART | 74 | PART-000083 | Spare parts |
| IKPVKL | 60 | IKPVKL-xxx | PV Install Kit Klip-Lok |
| PVMSB | 59 | PVMSB-xxx | PV Mounting Structure |
| S | 58 | S11450B | Standalone items |
| SMFG | 48 | SMFG-xxx | Solartech Manufacturing |
| SLR | 33 | SLR-xxx | Solar products |

### Naming Convention Rules (Observed)
1. **Format:** `[PREFIX]-[NUMBER]` or `[PREFIX][NUMBER]`
2. **Case:** 96% uppercase
3. **Separator:** 83% use hyphens
4. **Numbers:** 98% contain numbers

### ✅ Recommended SKU Convention
```
[CATEGORY]-[SUBCATEGORY]-[SEQUENCE]
Example: SLR-INV-00123 (Solar Inverter #123)
```

---

## 2. Composite Naming Convention

### Current Pattern
Most composites follow: `[D-]PV Install Kit [Mounting Type] [Orientation] [Number]/R`

### Examples
- `D-PV Install Kit Klip-Lok 406 Portrait 1/R`
- `PV INSTALL KIT STANDING SEAM PORTRAIT 10/R`
- `D-APSYSTEMS 3P 2Acc Kit`

### ⚠️ Issues Found
- **Inconsistent casing:** Some ALL CAPS, some Title Case
- **Inconsistent D- prefix:** 12/31 have D- prefix, 19 don't
- **Abbreviations vary:** 1/R vs no suffix

### ✅ Recommended Composite Convention
```
D-[PRODUCT]-[MOUNTING]-[CONFIG]
Example: D-PVKIT-KLIPLOK406-P1R
```

---

## 3. Category Structure

### Business Units (9 total)
| Business Unit | Margin | Items |
|---------------|--------|-------|
| Solar: Residential (B2C) | 62.5% | Primary |
| Solar: Commercial (C&I) | 62.5% | |
| Solar: Infrastructure | 75.0% | |
| Water: Residential (B2C) | 62.5% | |
| Water: Commercial (C&I) | 62.5% | |
| Water: Recurring Care (Opex) | 70.0% | |
| Water: Infrastructure | 75.0% | |
| Services: Labour & Fees | 90.0% | |
| Services: Equipment Rental | 51.0% | |

### Product Categories (14 total)
1. Inverters
2. Energy Storage
3. BOS & Protection
4. PV Modules
5. Hot Water Systems
6. Water Treatment
7. Water Consumables
9. Consumables
10. Tools & PPE
11. Mechanical Infra
13. Mounting & Structure
14. Services
- Equipment Rental
- Labour & Fees

### ⚠️ Category Issues
- **Numbering gap:** Categories skip 8, 12
- **Inconsistent naming:** "Labour & Fees" vs "Labor & Fees" in sub-categories

---

## 4. Data Quality Issues

### 🔴 Critical Issues

| Issue | Count | Impact |
|-------|-------|--------|
| **Items with ZERO cost price** | 144 | Cannot calculate margins |
| **Items with MISSING cost price** | 96 | Cannot calculate margins |
| **Items with ZERO list price** | 240 | Invalid pricing in Zoho |
| **Items missing Zoho ID** | 96 | Cannot sync to Zoho |

### 🟡 Warnings

| Issue | Count | Impact |
|-------|-------|--------|
| Items missing SKU | 9 | Cannot match to Zoho |
| Duplicate SKUs | 2 | Data integrity risk |
| SKUs in Price Master not in Zoho | 41 | Orphaned records |

---

## 5. Cross-File Consistency

### SKU Coverage Gap
```
Item Master (Zoho):     2,751 SKUs
Price Master:             393 SKUs
├─ In Both:               352 SKUs ✅
├─ No Pricing (Gap):    2,399 SKUs ⚠️
└─ Orphaned:               41 SKUs ❓
```

**87% of SKUs have NO PRICING defined!**

### Orphaned SKUs (in Price Master but not Item Master)
These may be:
- Discontinued items not removed from Price Master
- New items not yet in Zoho
- Labor/service codes

```
APCUT-01, HSC-#1(M), HYS-3.0LV-EUG1, HYS-3.6LV-EUG1,
HYS-4.6LV-EUG1, LAB-ELEC-MSB-UPG, LAB-GEN-MOB-OUT,
LAB-GEN-VO-MAN, LAB-SOL-BATT-RET, LAB-SOL-EV-CHARG...
```

---

## 6. Margins Table Validation

### Current Structure ✅
| Field | Purpose |
|-------|---------|
| TEAM | Business Unit identifier |
| Ratio | Weight (sums to 90%) |
| Margin | Cost markup % |
| List | List price discount from MSRP |
| Discount (Green/Amber/Red) | Approval tiers |
| Dealer | Dealer discount |
| GP columns | Calculated gross profit |

### ⚠️ Issues
- Row 8 has no TEAM but has Margin (0.70) - orphaned row?
- Row 10-11 have incomplete data (CONTRACT, Equipment Rental)

---

## 7. Recommended Actions

### Immediate (Before Zoho Sync)

1. **Fix Zero/Missing Prices**
   - Review 144 items with zero cost
   - Fill 96 items with missing cost
   - Recalculate 240 items with zero list price

2. **Resolve Orphaned SKUs**
   - Verify 41 SKUs not in Zoho - add or remove
   - Update 96 items missing Zoho ID

3. **Fix Duplicate SKUs**
   - Identify and merge 2 duplicate SKU records

### Short-term (Standardization)

4. **Standardize Naming Conventions**
   - Document SKU prefix meanings
   - Apply consistent casing (recommend: UPPERCASE)
   - Standardize composite naming format

5. **Fill Pricing Gap**
   - Prioritize pricing for 2,399 unpiced SKUs
   - Or mark as "Not for Sale" in Zoho

### Long-term (Automation)

6. **Automate Sync**
   - Build Zoho → Excel export routine
   - Build Excel → Zoho import routine
   - Schedule weekly reconciliation

---

## File Structure Reference

### Solartech Price Master.xlsx
```
├── Item SKUs (404 rows)
│   └── Columns: Item ID, Name, Business Unit, Category,
│                Sub-Category, SKU, Brand, Cost Price,
│                Stock Moving Status, List Price
├── Composite SKUs (31 rows)
│   └── Columns: Item ID, Item SKU, Name, Status, List Price
└── Margins (12 rows)
    └── Columns: TEAM, Ratio, Margin, List, Discounts, GP
```

### SKU Composite Master.xlsx
```
├── PASTE_ZOHO_HERE (31 rows) ← Zoho export paste area
│   └── Columns: Item ID, SKU, Name, Usage unit,
│                Selling Price, Status, New Selling Price
└── The Composite Master (2,878 rows) ← BOM details
    └── Columns: Item ID, SKU, Name, Category, Sub Category,
                 Status, Mapped Item SKU/Name/Qty/Price
```

### SKU Item Master.xlsm
```
├── PASTE_ZOHO_HERE (2,800 rows) ← Zoho export paste area
│   └── Columns: item_id, name, sku, status, rate, item_type,
│                product_type, purchase_rate, unit, etc.
└── The SKU Master (10,000+ rows) ← Working data
    └── Columns: item_id, name, Business Unit, Category,
                 Sub-Category, sku, purchase_rate, etc.
```

---

## Next Steps

1. ☐ Review this report with Ops team
2. ☐ Decide on SKU naming convention standard
3. ☐ Fix critical data quality issues
4. ☐ Perform test sync with subset of data
5. ☐ Full Zoho sync after validation

---
*Report generated by CTO Review Bot*
