# BizOS Context
> Claude's working memory. Read at startup. Update at session end.

**Last:** 2026-02-08 | **Flags:** 8 active | **Mode:** 💬 Lite

> **SESSION SNAPSHOT** (Quick Read)
> **Last:** 2026-02-08 | **Flags:** 8 | **Task:** Deploy @chokops_bot + WF02 to n8n
> **Mode:** 🔧 Build | **Suggested next:** 🔧 Build
> **Summary:** Deployed @chokops_bot Telegram bot to n8n. Fixed WF02 chatId bug (invalid $credentials → $vars.TELEGRAM_CHAT_ID). Created Telegram + Anthropic credentials in n8n. WF02 imported. Eats365 API access pending (Merchant Portal → Integration → Developer Portal). Logged F-019 + G-BUILD-001. ⚠️ iCloud sync wiped builder/ files — need to recreate BUILD_LOG, CHECKLIST, RULES, specs, runbooks next session.

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

**Immediate:** Builder Agent generates all 7 n8n workflows
- Builder skill running `build all` — generates workflow JSONs from specs
- Import generated workflows into n8n on Railway
- ~~Add Telegram bot credentials to n8n~~ ✅ Done (telegram_bot_token + TELEGRAM_CHAT_ID variable)
- Request Eats365 API access (Merchant Portal → Integration → Developer Portal → Connect New App)
- Recreate builder/ files wiped by iCloud sync (BUILD_LOG, CHECKLIST, RULES, WF02 JSON, runbooks, specs)
- Test first workflow (Kinme Daily Sales) end-to-end
- Remaining workflow specs needed: Solartech Pipeline, Hippos/WCI Weekly, Trading Daily, Finance Listener, Morning Brief, Watchdog

**Then:** Fill in role KPI targets
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

**Agent Infrastructure (new):**
- Strategy: `cto-brain/designs/AGENT_STRATEGY_v1.md`
- Builder: `cto-brain/builder/` (BUILD_LOG, CHECKLIST, RULES, specs/, artifacts/, runbooks/)
- n8n: `https://n8n-production-f0e6.up.railway.app` (Railway, Asia/Kuala_Lumpur TZ)
- Telegram: @chokops_bot (chat ID: 8412712971)
- Builder skill: installed in Cowork (invoke with `builder`)

---

## Entity Status

| Entity | Status | Last | Quick Note |
|--------|--------|------|------------|
| Solartech | 🟢 Structured | Feb 7 | Zoho context merged into _ENTITY.md, zoho/ZOHO_STANDARDS.md created |
| Hippos | 🟢 Structured | Feb 6 | TTL_KPIS.md, roles/ scaffolded |
| WCI | 🟢 Structured | Feb 6 | TTL_KPIS.md, roles/ scaffolded |
| Kinme | 🟢 Structured | Feb 7 | TTL_KPIS.md created, RM 227K/mo, stock alerts active |

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
