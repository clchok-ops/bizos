# Architecture Review — Pre-Implementation Check

**Date:** 2026-02-05
**Updated:** 2026-02-05
**Purpose:** Validate architecture before Zoho implementation
**Status:** ✅ Phase 1 & 2 Complete

---

## 1. Architecture Summary

### 1.1 New Fields (Add to Zoho as Custom Fields)

| Field | Zoho Name | Type | Values | Required |
|-------|-----------|------|--------|----------|
| Category_Code | CF.Category_Code | Text(3) | INV, ESS, BOS, MOD, HWS, WTS, WCN, MEC, ELE, FAS, CNS, TOL, MNT, SVC | Yes |
| Brand_Code | CF.Brand_Code | Text(3) | 33 codes from Kwan's list | Yes (OEM if blank) |
| Zone | CF.Zone | Text(1) | S, W, G, V | Auto-derived |
| Vendor_SKU | CF.Vendor_SKU | Text(50) | Supplier's original code | Optional |
| Item_Type | CF.Item_Type | Dropdown | ITEM, COMP_OPS, COMP_SALES | Yes |
| Status_Clean | CF.Status_Clean | Dropdown | Active, Inactive, Duplicate | Yes |

### 1.2 Existing Fields (Keep As-Is)

| Field | Purpose | Notes |
|-------|---------|-------|
| Item ID | Zoho system ID | Don't touch |
| SKU | Internal code | Keep existing values |
| Name | Item name | Keep |
| Brand | Brand name (text) | Keep — Brand_Code is lookup |
| Category | Full category name | Keep — Category_Code is lookup |
| Sub-Category | Full subcategory | Keep |
| Business Unit | Pricing tier driver | Keep |
| Cost Price | Purchase cost | Keep |
| List Price | Base selling price | Keep |

---

## 2. Conflict Analysis & Decisions

### ✅ CONFIRMED APPROACH: Parallel Fields

| Decision | Outcome |
|----------|---------|
| Category handling | **Parallel fields** — Add `Category_Code` alongside existing `Product Category` |
| Zone storage | **Store in Zoho** (not calculated on export) |
| CONTRACT in Margins | **Keep** — Used for outsourced services margins |
| D- prefix items | **Duplicates** — Mark for deactivation |

### ✅ NO BREAKING CHANGES

| Check | Result |
|-------|--------|
| Business Unit alignment | ✅ 9/9 BUs match between Item Master and Margins |
| Category naming | ✅ ADD Category_Code as NEW field, keep Product Category |
| Brand naming | ✅ ADD Brand_Code as NEW field, keep Brand |
| SKU format | ✅ Keep existing SKUs, add Vendor_SKU as optional |
| Active records | ✅ Existing data untouched, new fields populate over time |
| User workflow | ✅ Users continue with Product Category, Category_Code for system use |

---

## 3. Zoho Implementation Plan

### Phase 1: Create Custom Fields in Zoho (Admin)

**In Zoho Inventory → Settings → Items → Custom Fields:**

```
1. CF.Category_Code
   - Type: Single Line Text
   - Max Length: 3
   - Required: Yes

2. CF.Brand_Code
   - Type: Single Line Text
   - Max Length: 3
   - Required: Yes (default: OEM)

3. CF.Zone
   - Type: Dropdown
   - Values: S, W, G, V
   - Required: Yes

4. CF.Vendor_SKU
   - Type: Single Line Text
   - Max Length: 50
   - Required: No

5. CF.Item_Type
   - Type: Dropdown
   - Values: ITEM, COMP_OPS, COMP_SALES
   - Required: Yes (default: ITEM)

6. CF.Status_Clean
   - Type: Dropdown
   - Values: Active, Inactive, Duplicate
   - Required: Yes (default: Active)
```

### Phase 2: Prepare Data Mapping File

Create Excel with mappings for bulk import:

| SKU | Category_Code | Brand_Code | Zone | Item_Type |
|-----|---------------|------------|------|-----------|
| 11215 | WTS | KIN | W | ITEM |
| HMS-2000 | INV | HOY | S | ITEM |
| ... | ... | ... | ... | ... |

### Phase 3: Bulk Update via Zoho Import

1. Export current items from Zoho
2. Add new columns with mapped values
3. Import back to Zoho (update mode)

### Phase 4: Validation

- [ ] All items have Category_Code
- [ ] All items have Brand_Code (or OEM)
- [ ] Zone derived correctly
- [ ] No orphan composites

---

## 4. Data Flow After Implementation

```
NEW ITEM ENTRY:
┌─────────────────────────────────────────────────────────────────┐
│ User enters: SKU, Name, Brand, Category, Business Unit          │
│ System auto-fills: Brand_Code (lookup), Category_Code (lookup)  │
│ System calculates: Zone (from Category_Code)                    │
│ User selects: Item_Type (ITEM/COMP_OPS/COMP_SALES)             │
└─────────────────────────────────────────────────────────────────┘

PRICING CALCULATION:
┌─────────────────────────────────────────────────────────────────┐
│ Input: Item + Business Unit                                     │
│ Lookup: Margin % from Margins table (by BU)                     │
│ Calculate: List Price, Discount Tiers                           │
└─────────────────────────────────────────────────────────────────┘

REPORTING:
┌─────────────────────────────────────────────────────────────────┐
│ Filter by: Zone (warehouse), Category_Code, Brand_Code          │
│ Group by: Business Unit (pricing), Item_Type                    │
│ Validate: Status_Clean ≠ Duplicate                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Open Questions for Confirmation

| # | Question | Answer |
|---|----------|--------|
| 1 | Is "CONTRACT" in Margins still used? | |
| 2 | Should Zone be stored or calculated? | Stored (recommended) |
| 3 | Apply Item_Type to existing composites? | Yes (recommended) |
| 4 | Who creates Zoho custom fields? | |
| 5 | Timeline for implementation? | |

---

## 6. Action Items

### Immediate (Before Zoho Changes)

- [ ] Confirm architecture decisions above
- [ ] Clarify CONTRACT business unit
- [ ] Decide who creates Zoho custom fields

### Phase 1: Zoho Setup ✅ COMPLETE (2026-02-05)

- [x] Create 5 custom fields in Zoho Inventory (Status_Clean deferred)
  - Category_Code (Text, Mandatory)
  - Brand_Code (Text, Mandatory, Default: OEM)
  - Zone (Dropdown: S/W/G/V, Mandatory)
  - Vendor_SKU (Text, Optional)
  - Item_Type (Dropdown: ITEM/COMP_OPS/COMP_SALES, Mandatory, Default: ITEM)
- [x] Set up dropdown values for Zone, Item_Type
- [ ] Test with 1 item manually

### Phase 2: Data Preparation ✅ COMPLETE (2026-02-05)

- [x] Generate mapping file: `ZOHO_BULK_UPDATE_MAPPING.xlsx`
- [x] Map 864 active items to Category_Code (660 need manual review)
- [x] Map all brands to Brand_Code (33 brands → codes)
- [x] Calculate Zone for all items with categories
- [x] Assign Item_Type = ITEM for all existing items

**Mapping File Stats:**
- Total Active Items: 1,524
- Items with Category_Code: 864 (57%)
- Items Needing Review: 660 (43%) — highlighted yellow

### Phase 3: Bulk Update

- [ ] Export Zoho items
- [ ] Merge with mapping file
- [ ] Import to Zoho (update mode)
- [ ] Validate counts match

### Phase 4: Composites

- [ ] Update Composite Master with new fields
- [ ] Validate all mapped SKUs exist
- [ ] Mark D- items as Inactive/Duplicate

---

*Review Date: 2026-02-05*
