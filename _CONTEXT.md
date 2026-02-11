# BizOS Context
> Claude's working memory. Read at startup. Update at session end.

**Last:** 2026-02-11 | **Flags:** 13 | **Mode:** 🔧 Build

> **SESSION SNAPSHOT** (Quick Read)
> **Last:** 2026-02-11 | **Flags:** 13 | **Task:** WF-PA-HEALTHCHECK v1 operational — gate open for PTL 121 flows
> **Mode:** 🔧 Build | **Suggested next:** 🔧 Build
> **Summary:** Healthcheck gate passed. schemaVersion fix (F-035→G-BUILD-005), n8n error body stripping learned (F-036→G-BUILD-006). Custom security role gap open (F-036, System Admin interim). Next: PTL 121 scoring & delivery flows.

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
| ⚪ Open | System | _INBOX pipeline has zero monitoring — add staleness check to WF08 Watchdog (48hr threshold) | 0d |
| 🟡 ACTIVE | System | O365 PA Agent — WF-PA-HEALTHCHECK v1 operational (full mode HEALTHY, 1 warning). Phase 1 gate open. | 0d |
| 🟡 ACTIVE | System | F-036: Custom Dataverse security role cannot create cloud flows — System Admin interim, exact missing privilege TBD | 0d |
| ✅ RESOLVED | System | Token efficiency restructure — rules split done, skills installed, validated in perf startup | 0d |
| ⚪ Backlog | System | Performance Management structure — deferred, medium priority per TOKEN_EFFICIENCY_AUDIT.md Section 4.7 | 0d |

---

## Next Focus

**Immediate:**
- ~~Phase 0 O365 PA Agent — Chok-owned~~ ✅ Done — Azure AD app reg, Dataverse security role, n8n credential setup, PnP CLI install. Claude creates runbook.
- Resume builder work and performance management
  - ~~Install skills~~ ✅ Done — startup_v2 + builder_v3 installed, validated in perf startup
  - ~~Test new startup~~ ✅ Done — profile-aware loading working (CORE_RULES.md loaded, perf mode correct)
  - Disable Control Chrome connector — Saves ~3-5K tokens/turn from duplicate browser tools
  - Verify rules split — Check for duplicate rule across CORE/BUILD/REFERENCE split (43 total vs 42 expected)
  - ~~Delete root orphans~~ ✅ Deleted by Chok between sessions
- ~~Phase 1 O365 PA Agent — Build WF-PA-HEALTHCHECK~~ ✅ Healthcheck v1 operational (6/6 checks pass)
- Phase 1 O365 PA Agent — Build PTL 121 scoring & delivery flows (healthcheck gate open)
- F-036 investigation — enumerate System Admin vs custom role privileges for cloud flow creation

**Then:** Resume builder work and performance management
- Performance management structure — Medium priority deliverable from TOKEN_EFFICIENCY_AUDIT.md Section 4.7
- Resume WF03 Solartech Pipeline Risk — Phase 2 reference implementation (originally deferred for efficiency audit)
  - Redesign WF03 for action-oriented workflow (not just alerts)
  - Two-way Telegram (alert + prepared action + inline buttons + callback)
  - Action execution (Zoho API: send email, create task, update deal stage)
- Fill in role KPI targets (Solartech roles have templates, need actual RM targets; Hippos/WCI need role definitions)

**Completed:**
- PTL 100-pt framework (bizos/00_Holding/PTL_FRAMEWORK.md)
- Role-based KPI structure for all 3 entities
- Bizos structure cleanup + STRUCTURE.md
- Structure validation in startup/end-session skills (staged)
- F-012, F-013 logged + G-DOC-005, G-SKILL-001 added

**Cleanup backlog** (fix opportunistically while working in this space):
- [x] `REVIEW_FRAMEWORK.md` at bizos root — ✅ Documented in STRUCTURE.md
- [x] `automation/` folder at bizos root — ✅ Documented in STRUCTURE.md (Special Folders)
- [ ] Hippos, WCI, Kinme roles/ — scaffolded only (_ROLES_INDEX.md). Populate when doing entity work
- [x] 00_Holding/ extra files — ✅ N8N_AUTOMATIONS, SETUP_CHECKLIST, SETUP_PLAYBOOK, thresholds.json added to STRUCTURE.md
- [ ] _INBOX pipeline has zero monitoring — was broken 7 days undetected (F-029). Add "last file received" staleness check to WF08 Watchdog. Threshold: alert if no _INBOX file in 48 hours.
- [x] `O365_PA_AGENT_ARCHITECTURE.md` — ✅ Already correctly in cto-brain/designs/ (not orphaned)
- [x] `_skill_installers/` at ClaudeHub root — ✅ Deleted
- [x] `startup_v2.skill` + `builder_v3.skill` at ClaudeHub root — ✅ Deleted
- [ ] 1 duplicate rule across CORE/BUILD/REFERENCE split (43 total vs 42 expected) — minor, needs grep to identify
- [ ] cto-brain/builder/artifacts/_test_dv_create.sh — diagnostic script, safe to delete manually

**Parked:** PTL 121 Flow 5, Kaizen Architecture Phase 1

**Agent Infrastructure:**
- Strategy: `cto-brain/designs/AGENT_STRATEGY_v2.md` (action-oriented, cross-domain learning)
- Domain goals: `bizos/AGENT_GOALS.md` (to be created), `trading/AGENT_GOALS.md`, `personal-finance/AGENT_GOALS.md`
- Builder: `cto-brain/builder/` (BUILD_LOG, CHECKLIST, RULES, specs/, artifacts/, runbooks/)
- n8n: `https://n8n-production-f0e6.up.railway.app` (Railway, Asia/Kuala_Lumpur TZ)
- Telegram: @chokops_bot — 7 domain chats (Solartech, Hippos, WCI, Kinme, Trading, Finance, System)
- Builder skill: installed in Cowork (invoke with `builder`)
- Build sequence: WF03 Solartech → WF04 Hippos → WF05 WCI → WF06 Trading → WF07 Finance → WF02 Kinme → WF08 Watchdog

---

## Entity Status

| Entity | Status | Last | Quick Note |
|--------|--------|------|------------|
| Solartech | 🟡 In Progress | Feb 9 | WF03 credentials clean, using n8n native credentials. Ready for e2e test. |
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
