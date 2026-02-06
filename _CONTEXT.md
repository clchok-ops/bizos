# BizOS Context
> Claude's working memory. Read at startup. Update at session end.

**Last:** 2026-02-06 | **Flags:** 8 active | **Mode:** 🔧 Build

> **SESSION SNAPSHOT** (Quick Read)
> **Last:** 2026-02-06 | **Flags:** 8 | **Task:** PTL framework + bizos structure alignment
> **Mode:** 🔧 Build | **Suggested next:** 💬 Lite
> **Summary:** Documented PTL 100-pt model, created role-based KPI structure for all entities, major bizos cleanup (archived stale files, created STRUCTURE.md), added structure validation to skills, 3 new rules (G-DOC-005, G-SKILL-001)

---

## Flags

| Priority | Entity | Flag | Age |
|----------|--------|------|-----|
| 🔴 URGENT | Solartech | PD-000127 (RM 1.59M) stuck 347 days | 4d |
| 🟡 ACTIVE | Solartech | RM 20.5M at risk (24 high + 62 medium) | 4d |
| 🟡 ACTIVE | Kinme | Premium whisky low: Hibiki 21, Yamazaki 12, Hakushu 18 | 2d |
| 🟡 ACTIVE | Kinme | House umeshu 2020 out of stock | 2d |
| ⚪ Open | Solartech | 70% pipeline in 2 owners | 4d |
| ⚪ Open | Solartech | Large deal win rate 20.9% vs 37.8% | 4d |
| ⚪ Open | Kinme | Tuesday lowest revenue - promo opportunity | 4d |
| ⚪ Open | Kinme | Food costs not in POS | 4d |

---

## Next Focus

**Immediate:** PTL 121 remaining flows (3, 4, 5)
- Flow 3: 121-OnFinalValidation
- Flow 4: 121-WeeklyDeliveryCheck
- Flow 5: 121-OnDeliveryConfirmed

**Completed:**
- SOLARTECH_ARCHITECTURE.md v1.4 (100% Zoho CRM documented)
- Startup/learn/end-session skill redesign with kaizen loop

**Parked:** Kaizen Architecture Phase 1, Zoho report frequency updates

---

## Entity Status

| Entity | Status | Last | Quick Note |
|--------|--------|------|------------|
| Trading | 🟡 Setting up | Jan 31 | Journal ready, no trades logged |
| Solartech | 🟢 Documented | Feb 5 | Architecture v1.4 complete, API ready |
| Hippos | 🟢 Flowing | Feb 2 | 5 enquiries/day, daily reports on |
| WCI | 🟡 To map | — | Odoo identified |
| Kinme | 🟢 Analyzed | Feb 2 | RM 227K/mo, stock alerts active |

**Deep dive:** `startup [entity]` to load full entity context.

---

## Quick Ref

**Startup commands:**
- `startup` → This + CRITICAL_RULES (lite)
- `startup [entity]` → This + entity + CRITICAL_RULES
- `startup bizos` → Full bizos (all entities)
- `startup brain` → CTO brain + GLOBAL_STANDARDS
- `startup build` → This + GLOBAL_STANDARDS

**Mid-session:** `mode build`, `mode lite`, `mode crm`

**Locations:**
- Entity details: `[entity]/_ENTITY.md`
- Decisions/learnings: `_archive/`
- Standards: `cto-brain/GLOBAL_STANDARDS.md`
