# BizOS Context
> Claude's working memory. Read at startup. Update at session end.

**Last:** 2026-02-07 | **Flags:** 8 active | **Mode:** 💬 Lite

> **SESSION SNAPSHOT** (Quick Read)
> **Last:** 2026-02-07 | **Flags:** 8 | **Task:** Full ClaudeHub conflict audit + structural fixes
> **Mode:** 💬 Lite | **Suggested next:** 💬 Lite
> **Summary:** Full ClaudeHub audit: removed 01_Trading from bizos (personal trading → trading/ repo), cleaned root orphans, fixed GLOBAL_STANDARDS (malformed code, rule count 14→20, added G-DOC-004/005), created Kinme roles/, fixed Pydantic v2 mismatch, documented read-only bridge for personal-finance, added `startup finance` command

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

**Immediate:** Fill in role KPI targets
- Solartech roles have templates, need actual RM targets
- Hippos/WCI need role definitions

**Completed:**
- PTL 100-pt framework (bizos/00_Holding/PTL_FRAMEWORK.md)
- Role-based KPI structure for all 3 entities
- Bizos structure cleanup + STRUCTURE.md
- Structure validation in startup/end-session skills (staged)
- F-012, F-013 logged + G-DOC-005, G-SKILL-001 added

**Cleanup backlog** (fix opportunistically while working in this space):
- [ ] `REVIEW_FRAMEWORK.md` at bizos root — not documented in STRUCTURE.md. Add to STRUCTURE.md or move to 00_Holding/
- [ ] `automation/` folder at bizos root — Zoho Python client, not in STRUCTURE.md. Document in STRUCTURE.md under a new "Automation" section
- [ ] Hippos, WCI, Kinme roles/ — scaffolded only (_ROLES_INDEX.md). Populate when doing entity work
- [ ] 00_Holding/ has extra files (N8N_AUTOMATIONS, SETUP_CHECKLIST, SETUP_PLAYBOOK, thresholds.json) not listed in STRUCTURE.md

**Parked:** PTL 121 Flow 5, Kaizen Architecture Phase 1

---

## Entity Status

| Entity | Status | Last | Quick Note |
|--------|--------|------|------------|
| Solartech | 🟢 Structured | Feb 6 | Org chart, roles/, TTL_KPIS.md added |
| Hippos | 🟢 Structured | Feb 6 | TTL_KPIS.md, roles/ scaffolded |
| WCI | 🟢 Structured | Feb 6 | TTL_KPIS.md, roles/ scaffolded |
| Kinme | 🟢 Analyzed | Feb 2 | RM 227K/mo, stock alerts active |

> **Note:** Trading removed from bizos 2026-02-07. Managed in separate `trading/` repo.

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
- Learning docs: `docs/` (FAILURE_LOG, BIZOS_RULES, BIZOS_PATTERNS, BIZOS_KAIZEN)
- Historical decisions/learnings: `_archive/` (preserved, migrated to docs/)
- Standards: `cto-brain/GLOBAL_STANDARDS.md`
