# Brand & Category Code Master

**Version:** 1.0
**Date:** 2026-02-05
**Status:** ✅ Approved (Kwan)
**Source:** PRICING_RULES_CONFIRM (Kwan tab)

---

## Purpose

Single source of truth for:
- 3-letter brand codes for `Brand_Code` field
- 3-letter category codes for `Category_Code` field
- Zone assignments (S/W/G/V)

---

## 1. Approved Brand Codes

### Actively Traded Brands (from Kwan)

| Code | Brand Name | Primary Category | Notes |
|------|------------|------------------|-------|
| HOY | Hoymiles | INV, ESS, BOS | Hybrid, Microinverters, Energy Storage & DC Components |
| GRO | Growatt | INV | String, Hybrid |
| HUA | Huawei | INV, ESS, BOS | String Inverters, Energy Storage & DC Components |
| SOL | Solis | INV, BOS | String Inverters & DC Components |
| APS | APsystems | INV, BOS | Microinverters, DC Component |
| TRI | Trina | MOD | PV Modules |
| SPS | Solarspace | MOD | PV Modules |
| KIN | Kinetico | WTS | Water Treatment |
| WCI | Water-Care Industries | WTS, WCN | Systems & Components |
| CAL | Calgon | WCN | Filtration media |
| SUM | Summer | HWS | Solar water heater |
| ELT | Elton | HWS | Heating elements |
| JOV | Joven | HWS | Heating elements |
| PEC | Pecol | HWS | Heating elements |
| THW | Thermowatt | HWS | Heating elements |
| KGF | Kingfeels | MNT | PV Mounting |
| EST | Esteel | HWS | Large Storage Tanks |
| HEL | Helukabel | BOS | DC Cable |
| BMG | BMG | HWS | Hot Water Tank |
| TNB | TNB | SVC | Services & Labor |
| STL | Solartech | SVC | Services & Labor (in-house) |
| OEM | Generic/Unbranded | — | Various |
| LAB | Labor | SVC | Services & Labor |
| AVT | Aventura | WCN | Water Consumables |
| BMI | BMI | HWS | Hot Water Tank |
| CMD | Commando | BOS | Combiner Box |
| FEO | FEEO | BOS | DC Components |
| HAO | Haohua | WCN | Water Consumables |
| MRU | MERU | HWS | Hot Water Heater |
| MTW | METHEWE | BOS | Smart Meter |
| MSG | MSIG | SVC | Insurance Plan |
| HTF | HeatFirst | HWS | HeatPump |
| WIN | Winstar | MNT | PV Mounting |

### Brand Name Standardization

| ❌ Incorrect | ✅ Correct | Code |
|--------------|------------|------|
| Apsystem | APsystems | APS |
| Commandor | Commando | CMD |
| Themowatt | Thermowatt | THW |
| S - Solar PV | *(remove — not a brand)* | — |

### Brands Pending Review

| Brand | Found In | Action |
|-------|----------|--------|
| Sunglow | Item Master | Add code OR mark inactive |
| Vartex | Item Master | Add code OR mark inactive |

---

## 2. Category Codes

| Code | Category Name | Zone | Description |
|------|---------------|------|-------------|
| INV | Inverters | S | Solar inverters & microinverters |
| ESS | Energy Storage | S | Battery systems |
| BOS | Balance of System | S | Cables, connectors, combiner boxes |
| MOD | PV Modules | S | Solar panels |
| HWS | Hot Water Systems | W | Solar & electric water heaters |
| WTS | Water Treatment | W | Filtration & purification systems |
| WCN | Water Consumables | W | Filters, cartridges, media |
| MEC | Mechanical | G | Pumps, valves, piping |
| ELE | Electrical | G | Wiring, breakers, meters |
| FAS | Fasteners | G | Nuts, bolts, mounting hardware |
| CNS | Consumables | G | General consumables |
| TOL | Tools & PPE | G | Installation tools, safety gear |
| MNT | Mounting & Structure | G | Rails, clamps, structures |
| SVC | Services & Labor | V | Installation, maintenance, fees |

### Legacy Category Mapping

| Old Category (Item Master) | New Code |
|----------------------------|----------|
| 1. Inverters | INV |
| 2. Energy Storage | ESS |
| 3. BOS & Protection | BOS |
| 4. PV Modules | MOD |
| 5. Hot Water Systems | HWS |
| 6. Water Treatment | WTS |
| 7. Water Consumables | WCN |
| 9. Consumables | CNS |
| 10. Tools & PPE | TOL |
| 11. Mechanical Infra | MEC |
| 13. Mounting & Structure | MNT |
| 14. Services | SVC |
| Labour & Fees | SVC |
| Equipment Rental | SVC |

---

## 3. Zone Codes

| Zone | Code | Business Units |
|------|------|----------------|
| Solar | S | Solar: Residential, Commercial, Infrastructure |
| Water | W | Water: Residential, Commercial, Infrastructure, Recurring Care |
| General | G | Mechanical, Electrical, Tools, Consumables |
| Services | V | Labour & Fees, Equipment Rental |

---

## 4. SKU Prefixes

| Prefix | Meaning | Brand Code |
|--------|---------|------------|
| COMP- | Component (vendor) | WCI |
| SMFG- | Solartech manufacturing | STL |
| D- | Duplicate (to disable) | *(skip)* |
| T- | Legacy item | *(leave blank)* |
| PART- | Generic part | OEM |
| RAWM- | Raw material | OEM |
| PKG- | Packaging | OEM |
| PURC- | Purchased item | *(leave blank)* |

---

## 5. Architecture Rules

### Rule A1: New Items Must Have Codes
All new items require:
- `Category_Code` from approved list
- `Brand_Code` from approved list (or OEM if unbranded)

### Rule A2: Brand Name Standardization
Use canonical spelling from this document. Fix before import:
- APsystems (not Apsystem)
- Commando (not Commandor)
- Thermowatt (not Themowatt)

### Rule A3: No Duplicate SKUs
SKU must be unique. Use `D-` prefix to mark items for deactivation.

### Rule A4: Composite Validation
All `Mapped Item SKU` in Composite Master must exist in Item Master.

### Rule A5: Zone Consistency
Zone must match Business Unit:
- Solar business units → Zone S
- Water business units → Zone W
- Services → Zone V

---

## Change Log

| Date | Change | By |
|------|--------|-----|
| 2026-02-05 | v1.0 — Approved brand list from Kwan tab | CTO Bot |
| 2026-02-03 | Draft v0.1 — Initial brand list | CTO Bot |

---

*Authoritative source: PRICING_RULES_CONFIRM.xlsx (Kwan tab)*
