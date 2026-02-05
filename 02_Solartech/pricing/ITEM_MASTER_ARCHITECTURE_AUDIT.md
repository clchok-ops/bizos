# Item Master Architecture Audit

**Date:** 2026-02-05
**Status:** 🔴 Action Required
**Scope:** Item Master, Composite Master, Pricing Master alignment

---

## Executive Summary

| Issue Category | Count | Severity |
|----------------|-------|----------|
| Brand name mismatches | 5 | 🟡 Medium |
| Missing brand mappings | 19 | 🟡 Medium |
| Category naming inconsistency | 14 | 🔴 High |
| Missing data (brands) | 142 | 🟡 Medium |
| Missing Item IDs | 96 | 🟡 Medium |
| Duplicate SKUs | 2 | 🔴 High |
| Orphan composite mappings | 101 | 🔴 High |
| List Price = 0 | 240 | 🟡 Medium |

---

## 1. Brand Discrepancies

### 1.1 Brands in Item Master NOT in Kwan's Active List

These brands exist in Item Master but are not in the actively traded brand list:

| Item Master Brand | Issue | Action |
|-------------------|-------|--------|
| `Apsystem` | Spelling differs from `APsystems` | Standardize to `APsystems` → Code: `APS` |
| `Commandor` | Spelling differs from `Commando` | Standardize to `Commando` → Code: `CMD` |
| `Themowatt` | Spelling differs from `Thermowatt` | Standardize to `Thermowatt` → Code: `THW` |
| `Sunglow` | Not in active list | Add to brand codes OR mark inactive |
| `Vartex` | Not in active list | Add to brand codes OR mark inactive |
| `S - Solar PV` | Invalid brand name | This is a category, not a brand — remove |

### 1.2 Kwan's Active Brands NOT in Item Master

These brands are actively traded but have no items in Item Master:

| Brand | Code | Expected Items |
|-------|------|----------------|
| Trina | TRI | PV Modules |
| Water-Care Industries | WCI | Water systems |
| Calgon | CAL | Filtration media |
| Kingfeels | KGF | PV Mounting |
| Esteel | EST | Storage tanks |
| Helukabel | HEL | DC Cable |
| BMG | BMG | Hot water tanks |
| TNB | TNB | Services |
| HeatFirst | HTF | Heat pumps |
| METHEWE | MTW | Smart meters |
| MSIG | MSG | Insurance |
| Labor | LAB | Services |
| Generic/Unbranded | OEM | Various |

---

## 2. Category Architecture Issues

### 2.1 Current State (Inconsistent)

**Item Master uses numbered prefixes:**
```
1. Inverters
2. Energy Storage
3. BOS & Protection
...
```

**Composite Master uses different naming:**
```
Solar PV
Solar Heater
Misc
```

**Kwan's system uses 3-letter codes:**
```
INV, ESS, BOS, MOD, HWS, WTS, WCN...
```

### 2.2 Recommended Category Mapping

| Item Master Category | → Code | Description |
|---------------------|--------|-------------|
| 1. Inverters | INV | Solar inverters & microinverters |
| 2. Energy Storage | ESS | Battery systems |
| 3. BOS & Protection | BOS | Cables, connectors, combiner boxes |
| 4. PV Modules | MOD | Solar panels |
| 5. Hot Water Systems | HWS | Solar & electric water heaters |
| 6. Water Treatment | WTS | Filtration & purification systems |
| 7. Water Consumables | WCN | Filters, cartridges, media |
| 9. Consumables | CNS | General consumables |
| 10. Tools & PPE | TOL | Installation tools, safety gear |
| 11. Mechanical Infra | MEC | Pumps, valves, piping |
| 13. Mounting & Structure | MNT | Rails, clamps, structures |
| 14. Services | SVC | Installation, maintenance, fees |
| Labour & Fees | SVC | (merge into Services) |
| Equipment Rental | SVC | (merge into Services) |

### 2.3 Zone vs Business Unit (Distinct Purposes)

**Zone** = Manages allowed categories (warehouse/inventory focus)

| Zone | Code | Allowed Categories |
|------|------|-------------------|
| Solar | S | INV, ESS, BOS, MOD |
| Water | W | HWS, WTS, WCN |
| General | G | MEC, ELE, FAS, CNS, TOL, MNT |
| Services | V | SVC |

**Business Unit** = Drives pricing tiers/margins

| Business Unit | Pricing Tier | Dealer? |
|---------------|--------------|---------|
| Solar: Residential (B2C) | 62.5% margin | Yes (56%) |
| Solar: Commercial (C&I) | 62.5% margin | No |
| Solar: Infrastructure | 62.5% margin | No |
| Water: Residential (B2C) | TBD | TBD |
| Water: Commercial (C&I) | TBD | TBD |
| Water: Infrastructure | TBD | TBD |
| Water: Recurring Care (Opex) | TBD | TBD |
| Services: Labour & Fees | 90% margin | No |
| Services: Equipment Rental | TBD | No |

---

## 3. Sub-Category Alignment

### 3.1 Item Master Sub-Categories (25 unique)

These need standardization and code assignment:

**Inverters (INV):**
- String Inverter
- Micro Inverter
- Monitoring & Comms

**Energy Storage (ESS):**
- Home Battery
- Commercial BESS

**BOS (BOS):**
- DC Components

**Hot Water (HWS):**
- Heaters (Solar/Elec)
- Heating Spares
- Solar Collectors
- Heater Mounting
- SS/Copper System

**Water Treatment (WTS):**
- Filtration Systems
- Softening Systems
- Treatment Spares
- System Connections

**Water Consumables (WCN):**
- Cartridges
- Filtration Media
- Industrial Chemicals
- Valves

**Mounting (MNT):**
- Solar Mounting
- PPR System

**Other:**
- Labor & Fees
- Pumps & Boosters
- Adhesives & Tapes
- PV Panels

### 3.2 Composite Master Sub-Categories (5 unique)

| Sub-Category | Alignment |
|--------------|-----------|
| INSTALLATION KIT | → MNT subcategory |
| PV INSTALLATION KIT | → MNT subcategory |
| COMBINER BOX PREFAB | → BOS subcategory |
| BATTERY KIT PREFAB | → ESS subcategory |
| Stump | → MNT subcategory |

---

## 4. SKU Format Issues

### 4.1 Current Patterns

| Pattern | Count | Examples |
|---------|-------|----------|
| Numeric only | 67 | 11215, 12754, 4050A |
| With dash | 220 | 100-1000, AV-421-63 |
| COMP- prefix | 39 | COMP-D-000121 |
| T- prefix | 47 | T-0345, T-0247 |
| Alphanumeric | 20 | S11450B, H12246 |
| Other | 2 | M4.8x16, SC M4x38MM |

### 4.2 Duplicate SKUs Found

| SKU | Occurrences | Action |
|-----|-------------|--------|
| 12799 | 2 | Review & deduplicate |
| FPV-63 | 2 | Review & deduplicate |

---

## 5. Data Quality Issues

### 5.1 Missing Data Summary

| Field | Missing | Total | % |
|-------|---------|-------|---|
| Item ID | 96 | 404 | 24% |
| SKU | 9 | 404 | 2% |
| Brand | 142 | 404 | 35% |
| Sub-Category | 19 | 404 | 5% |
| Cost Price | 96 | 404 | 24% |
| List Price = 0 | 240 | 404 | 59% |

### 5.2 Orphan Composite Mappings

**101 SKUs** referenced in Composite Master don't exist in Item Master:

```
KS-HK-S08-02, KL-02, SLR-EC-35-D, SLR-MC-35-D, EK-D,
KS-HK-S09-02, KS-HK-L21-WSD-M10300, SMFG-000390, SMFG-000380,
PART-000048, PART-000041, SMFG-000073, SMFG-000069...
```

These components are used in composite items but have no item record.

---

## 6. Proposed New Fields (Non-Breaking)

To clean up architecture without breaking existing data:

### 6.1 Item Master New Fields

| Field Name | Type | Purpose | Example | Required |
|------------|------|---------|---------|----------|
| `Category_Code` | Text(3) | Standardized category | INV, HWS, WTS | Yes |
| `SubCategory_Code` | Text(10) | Standardized subcategory | STR-INV, MCR-INV | Yes |
| `Brand_Code` | Text(3) | From Kwan's list | HOY, GRO, KIN | Yes (OEM if unbranded) |
| `Zone` | Text(1) | Category management | S/W/G/V | Auto (from Category) |
| `Vendor_SKU` | Text | Supplier's original code | HMS-2000-4T | Optional |
| `Item_Type` | Text | Item classification | ITEM / COMP_OPS / COMP_SALES | Yes |
| `Status_Clean` | Text | Clean status | Active/Inactive/Duplicate | Yes |

**Item_Type Values:**
- `ITEM` — Standard inventory item (404 in Item Master)
- `COMP_OPS` — Ops composite (internal assembly, 31 in Ops Composite Master)
- `COMP_SALES` — Sales composite (pricing bundle, 31 in Sales Composite)

**Vendor_SKU Logic:**
- Optional field for traceability (reorders, warranty)
- Many KINETICO numeric codes (11215) ARE vendor codes — document them
- COMP- prefix items = WCI vendor codes

### 6.2 Composite Master New Fields

| Field Name | Type | Purpose |
|------------|------|---------|
| `Category_Code` | Text(3) | Align to Item Master |
| `SubCategory_Code` | Text(10) | Align to Item Master |
| `Item_Type` | Text | COMP_OPS or COMP_SALES |
| `Validation_Status` | Text | All components exist? |

### 6.3 Sales Composite Cleanup

| SKU | Status | Action |
|-----|--------|--------|
| D-Stump | ✅ TRUE DUPLICATE | Delete (duplicate of T-514) |
| Testing Code 1 | ❌ TEST DATA | Delete |
| 11 D- prefix items | ⚠️ FLAGGED | Human review needed |

---

## 7. Action Items

### Immediate (Data Quality)

- [ ] Fix duplicate SKUs: 12799, FPV-63
- [ ] Standardize brand spellings: Apsystem → APsystems, Commandor → Commando, Themowatt → Thermowatt
- [ ] Remove invalid brand: "S - Solar PV"
- [ ] Review 101 orphan composite mappings

### Short-term (Architecture)

- [ ] Add new fields to Item Master (Category_Code, Brand_Code, etc.)
- [ ] Populate Category_Code mapping
- [ ] Populate Brand_Code from Kwan's list
- [ ] Decide on Sunglow and Vartex (add to codes or mark inactive)

### Medium-term (Alignment)

- [ ] Align Composite Master categories to Item Master codes
- [ ] Create validation rules for new items
- [ ] Build SKU_Display generation formula

---

## 8. Architecture Rules (Going Forward)

### Rule A1: Category & Brand Codes Required
All new items MUST have:
- `Category_Code` from approved list (14 codes)
- `Brand_Code` from Kwan's approved list (33 codes, or OEM if unbranded)

### Rule A2: Item_Type Required
All items MUST have Item_Type:
- `ITEM` — Standard inventory items
- `COMP_OPS` — Ops composites (internal assembly)
- `COMP_SALES` — Sales composites (pricing bundles)

### Rule A3: No Duplicate SKUs
SKU must be unique. Use `D-` prefix ONLY to mark items for deactivation (not for variants).

### Rule A4: Composite Validation
All `Mapped Item SKU` in Composite Master must exist in Item Master before activation.

### Rule A5: Zone Derived from Category
Zone auto-calculated:
- INV/ESS/BOS/MOD → S (Solar)
- HWS/WTS/WCN → W (Water)
- MEC/ELE/FAS/CNS/TOL/MNT → G (General)
- SVC → V (Services)

### Rule A6: Business Unit Determines Pricing
BU drives margin tiers — see Section 2.3 for pricing matrix.

### Rule A7: Vendor_SKU Optional
Vendor codes stored separately from internal SKU for traceability (reorders, warranty claims).

### Rule A8: Brand Name Standardization
Use canonical spelling from BRAND_CODE_MASTER.md:
- APsystems (not Apsystem)
- Commando (not Commandor)
- Thermowatt (not Themowatt)

---

## 9. Reference Documents

| Document | Purpose |
|----------|---------|
| BRAND_CODE_MASTER.md | Authoritative brand & category codes |
| ITEM_MASTER_CLEANUP_WORKBOOK.xlsx | Actionable discrepancy lists |
| PRICING_RULES_CONFIRM.xlsx (Kwan tab) | Human-approved active brands |

---

*Generated by CTO Review Bot — 2026-02-05*
