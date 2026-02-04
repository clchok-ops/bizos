# BizOS Context File
> **Purpose**: This is Claude's persistent memory. Read this at the START of every session. Update it at the END of every session.

> **SESSION SNAPSHOT** (Quick Read)
> **Last:** 2026-02-04 | **Flags:** 8 | **Task:** PTL 121 Flow 2
> **Summary:** Built and tested Flow 2 (121-OnPartnerResponse). Form 2 submission now updates SharePoint and emails Player A. Fix: Used Compose action to pass Record ID to Get item (dynamic content workaround).

**Last Updated**: 2026-02-04
**Updated By**: Claude (PTL 121 Flow 2 complete)
---


## How To Use This File


### For Claude (me):
1. **On "startup" command**: Read this file + GLOBAL_STANDARDS.md, check _INBOX, report status
2. **During session**: Reference as needed (don't re-read or re-report)
3. **On "end session" command**: Update relevant sections with new info, decisions, learnings


### For Chok:
- You can read this anytime to see current state
- Drop notes in `_INBOX/` folder if you want me to process something
- Don't worry about formatting—I'll maintain structure


### For n8n (automation):
- Automated workflows append to `## Flags & Anomalies` section
- Format: `- [YYYY-MM-DD] [ENTITY] [FLAG_TYPE]: Description`


---


## Portfolio Overview


| Entity | Type | Status | Last Reviewed | Key Metric |
|--------|------|--------|---------------|------------|
| Trading (IBKR) | Investment | 🟡 Setting up | 2026-01-31 | — |
| Solartech | B2B Distribution | 🟡 Risk model active | 2026-01-31 | RM 20.5M at risk |
| Hippos | B2C Retail | 🟢 Data flowing | 2026-02-02 | 5 enquiries/day |
| WCI | Manufacturing | 🟡 To map | — | — |
| Kinme | F&B (Izakaya) | 🟢 Jan analyzed | 2026-02-02 | RM 227K/month |


**Legend**: 🟢 Healthy | 🟡 Needs attention | 🔴 Critical


---


## Entity States


### 01_Trading (IBKR)
**Status**: Journal created, ready to use
**Approach**: Learn and build methodology before committing to strategies
**Current Focus**: Start logging trades, observe patterns

**Open Items**:
- [x] Set up trading journal structure → trading_journal.xlsx created
- [ ] Define what "success" looks like (metrics, risk tolerance)
- [ ] Connect IBKR API for automated tracking
- [ ] Establish review cadence
- [ ] First trade logged

**Tools Available**:
- Trade Journal (log every trade with thesis + lesson)
- Performance Metrics (auto-calculated from journal)
- Equity Curve Tracker
- Strategy Lab (test hypotheses)
- Lessons Log

**Recent Decisions**: None yet
**Learnings**: None yet

---

### 02_Solartech Operations
**Status**: RISK MODEL ACTIVE - Daily monitoring enabled
**Type**: Parent company, B2B distribution for solar/boiler/water
**Systems**: Zoho CRM (MCP connected), Zoho Inventory, SalesIQ

**Key Metrics (2026-01-31)**:
- Total Pipeline: RM 207.9M (4,209 deals)
- Active Pipeline: RM 114.8M (216 large deals >RM 50K)
- Win Rate: 37.8% overall, **20.9% on large deals** ⚠️
- At-Risk Value: **RM 20.5M** (24 high-risk + 62 medium-risk deals)

**Risk Model (92.8% accuracy)**:
| Signal | Points |
|--------|--------|
| Probability < 25% | +40 |
| No activity > 90 days | +25 |
| Sales cycle > 180 days | +15 |
| Stage = Idle/Tender | +10 |
| Owner win rate < 10% | +10 |

Risk Thresholds: 0-20 Low | 21-50 Medium | 51-100 High

**🚨 URGENT DEALS (High Risk)**:
1. PD-000127 (RM 1.59M) - Olivia Hwa - 347 days stuck
2. 8 Tenders (RM 4.1M) - Olivia Hwa - Dormant since Dec 10
3. PD-2160 (RM 55.6K) - Ahmad Shafiq - Owner 0% win rate

**Pipeline Concentration Risk**:
- Olivia Hwa + Siti Noor Bahiyah control 70% (RM 145M)
- Top performer Ted Wong: 52% win rate
- Bottom performers (Ahmad Shafiq, Chin Horng Liew): 0% win rate

**Open Items**:
- [x] Map current systems → Zoho (CRM, Inventory, SalesIQ)
- [x] Export deals data → 4,209 deals analyzed
- [x] Build risk scoring model → 92.8% accuracy
- [x] Identify at-risk deals → RM 20.5M flagged
- [ ] Validate high-risk list with Chok
- [ ] Enable daily automated scan via Zoho MCP
- [ ] Test Zoho write access for auto-flagging
- [ ] Expand to Hippos (same Zoho instance?)

**Recent Decisions**:
- [2026-01-31] Built risk model from historical data (backtest vs wait approach)

**Learnings**:
- Large deals (>RM 50K) have 20.9% win rate vs 37.8% overall
- Lost deals are 67% larger than won deals (RM 392K vs RM 234K)
- Historical data enables same-day model building (no observation period needed)
- Owner performance varies 52 percentage points (training/assignment issue)

---

### 03_Hippos Operations
**Status**: Data flowing, first analysis complete
**Type**: B2C retail/service (Super Hippo = solar water heaters)
**Systems**: Zoho CRM, Zoho Inventory, Zoho Analytics
**Transition**: Moving to solar and energy management this year

**Daily Reports Configured (9PM CSV)**:
1. CRM Deals Report → automation@solartech.com.my
2. Inventory Summary → automation@solartech.com.my
3. Inventory Movements → automation@solartech.com.my
4. Analytics Dashboard → automation@solartech.com.my

**Latest Data (Feb 1, 2026)**:
- 5 new enquiries
- 2 Opportunities (Solar Water Heater)
- 3 Troubleshooting requests
- Owners: Atie Hashim (4), FY Lim (1)

**Open Items**:
- [x] Map current systems → Zoho (CRM, Inventory, Analytics)
- [x] Configure daily automated reports → 4 reports, 9PM daily
- [x] First daily data received and analyzed → Feb 2
- [ ] Understand B2C pricing and job costing
- [ ] Document transition plan to solar/energy

**Recent Decisions**:
- [2026-02-01] Configured 4 Zoho reports to send daily CSV to automation email

**Learnings**:
- Hippos uses same Zoho instance as Solartech (shared CRM/Inventory)

---

### 04_WCI (Water-Care Industries)
**Status**: Systems identified
**Type**: Boiler manufacturer
**Systems**: Odoo (MRP, Inventory, Sales/CRM)

**Open Items**:
- [x] Map current systems → Odoo (Manufacturing, Inventory, Sales)
- [ ] Understand production costing and BOMs
- [ ] Document supply relationships to Solartech/Hippos
- [ ] Export sample data from Odoo for analysis

**Recent Decisions**: None yet
**Learnings**: None yet

---

### 05_Kinme
**Status**: January data analyzed, monitoring active
**Type**: Japanese upmarket izakaya (sake, sashimi, grill)
**Systems**: Eats365 (POS) - https://www.eats365pos.com/

**Key Metrics (January 2026 - Full Month)**:
- Net Sales: RM 227,519 (RM 7,339/day avg)
- Covers: 1,728 (56/day avg)
- Avg Spend: RM 131.69 ✅
- Discount Rate: 2.43% ✅ (Jan 31 was anomaly)
- Best Day: Thursday (RM 12,477 avg)
- Worst Day: Tuesday (RM 3,992 avg) ⚠️

**Open Items**:
- [x] Identify POS system → Eats365 (confirmed)
- [x] Export sales data → Done (1 day)
- [x] Build CFO Toolkit → kinme_cfo_toolkit.xlsx created
- [ ] Request Eats365 API developer access
- [ ] Export 30 days historical data for trends
- [ ] Input food costs into toolkit (yellow cells)
- [ ] Investigate high discount rate (21.7%)

**Recent Decisions**: None yet
**Learnings**:
- Discount rate at 21.7% needs investigation
- Food costs not tracked in POS - need manual input
- Seasonal items (Hokkaido Kegani, crabs) drive 65% revenue

---

## Flags & Anomalies

> Auto-populated by n8n workflows. Manual entries welcome.

| Date | Entity | Type | Flag | Status |
|------|--------|------|------|--------|
| 2026-01-31 | Solartech | RISK | RM 20.5M at risk (24 high + 62 medium risk deals) | **ACTIVE** |
| 2026-01-31 | Solartech | RISK | PD-000127 (RM 1.59M) stuck 347 days - needs intervention | **URGENT** |
| 2026-01-31 | Solartech | RISK | 70% pipeline concentrated in 2 owners | Open |
| 2026-01-31 | Solartech | RISK | Large deal win rate 20.9% vs 37.8% overall | Open |
| 2026-01-31 | Kinme | COST | Discount rate 2% avg (21.7% was anomaly day) | Resolved |
| 2026-01-31 | Kinme | DATA | Food costs not tracked in POS - need inventory solution | Open |
| 2026-01-31 | Kinme | OPS | Tuesday lowest revenue day - opportunity for promo | Open |
| 2026-02-02 | Kinme | STOCK | ⚠️ Premium whisky low: Hibiki 21, Yamazaki 12, Hakushu 18 LE = 1 bottle each | **ACTIVE** |
| 2026-02-02 | Kinme | STOCK | House umeshu 2020 (5L pour) out of stock | **ACTIVE** |
| 2026-02-02 | Kinme | STOCK | Sapporo cans out of stock | Open |
| 2026-02-01 | Infrastructure | SETUP | Configure cto-brain auto-sync (mirror bizos pattern) | ✅ Done |
| 2026-02-03 | Infrastructure | ARCH | ClaudeHub migration complete — all 3 brains consolidated | ✅ Done |
| 2026-02-01 | Hippos | BUILD | GROW/PTL architecture mapped - see cto-brain/modules/grow-ptl/ | Open |

---

## Active Decisions

> Decisions pending input or action

| ID | Entity | Decision Needed | Context | Deadline | Owner |
|----|--------|-----------------|---------|----------|-------|
| — | — | No active decisions | — | — | — |

---

## Decision Log

> Record of decisions made and their outcomes

### 2026-02

**[2026-02-04] Kaizen Architecture v1**
- **Decision**: Redesign BizOS from task-management to kaizen engine
- **Problem**: Previous architecture was "well-documented manual system masquerading as automated" — flags accumulated without action, rules existed without enforcement, learning was documented but not applied
- **Solution**: 6-layer architecture (Observation → Classification → Response → Review → Kaizen → Learning) with:
  - Continuous monitoring (entity + system + supply chain)
  - Context-aware classification (CRITICAL/COLLECT/SUPPRESS)
  - Scheduled reviews (weekly + monthly)
  - Built-in kaizen mechanisms for self-improvement
- **Entity Model**: Solartech (parent/distributor) ← WCI (manufacturing) → Hippos (residential B2C distribution partner)
- **Outcome**: Design documented, infrastructure files created
- **Implementation**: Phased build starting with Zoho API foundation
- **Docs**: `cto-brain/designs/KAIZEN_ARCHITECTURE_v1.md`

**[2026-02-04] Old Brain Folder Cleanup**
- **Decision**: Delete legacy brain folders from iCloud root (pre-migration remnants)
- **Deleted**:
  - `~/iCloud/bizos/` — Only had PRICING_RULES_WORKBOOK.xlsx (already in ClaudeHub) + empty _INBOX
  - `~/iCloud/trading-brain/` — Older _CONTEXT.md (99 lines vs 119 in ClaudeHub)
  - `~/iCloud/trading-brain-backup/` — Redundant backup
- **Outcome**: iCloud Drive cleaned up. All active work now exclusively in `~/iCloud/ClaudeHub/`

**[2026-02-03] ClaudeHub Architecture Migration**
- **Decision**: Consolidate all 3 brains (bizos, cto-brain, trading) into single ClaudeHub folder with unified auto-sync
- **Rationale**: Browser automation for GitHub editing fundamentally broken (CodeMirror blocks input). Local file access = instant, reliable. Single mount point = simpler workflow.
- **Outcome**: Implemented — see G-ARCH-001 in cto-brain/GLOBAL_STANDARDS.md
- **Components**:
  - `~/iCloud/ClaudeHub/` — Single folder with all repos
  - `~/Automation/scripts/sync_all.sh` — Unified sync script
  - `com.claudehub.sync.plist` — launchd job (every 30s)

**[2026-02-01] 360° Loop Architecture**
- **Decision**: Use existing email→iCloud routing (automation@solartech.com.my → _INBOX/) instead of complex n8n/WorkDrive setup
- **Rationale**: Simpler = more reliable. Email routing already works. Avoid over-engineering.
- **Outcome**: Configuration guide created (`02_Solartech/REPORT_CONFIGURATION.md`)
- **Action Required**: Chok to manually update Zoho report frequencies from Weekly → Daily

### 2025-01

**[2025-01-31] Architecture Decision**
- **Decision**: Adopt sustainable BizOS architecture with CONTEXT.md as persistent memory, n8n for automation, and integration with existing Zoho/Odoo systems
- **Rationale**: Static spreadsheets not sustainable; need system that learns and improves automatically without manual weekly reviews
- **Outcome**: Implemented

---

## Learnings & Patterns

> What we've learned that applies across entities

### Process Learnings
- Historical data eliminates "observation period" - can build models same day
- Backtesting on closed deals validates model before going live
- 4,209 deals → actionable risk model in <15 minutes
- **[G-WORK-001] Efficiency-first**: Always find most efficient path before starting work. Avoid browser automation for config UIs (Power Automate, Forms, Power BI) — prefer copy-paste guides, JSON configs, CLI tools. Browser wrestling = 20min, artifact creation = 2min.

### Cross-Entity Patterns
- (Pending Hippos/WCI analysis for comparison)

### What Worked
- Compressed timeline: Historical data analysis vs waiting to observe
- Risk scoring with specific thresholds (not vague "at risk" labels)
- Backtest validation (92.8% accuracy) before recommending
- **[G-ARCH-001]** ClaudeHub consolidation: single mount → access to all brains → local read/write → auto-sync to GitHub. Eliminated all browser wrestling.

### What Didn't Work
- Zoho MCP `get_deal_by_name` and `list_open_deals` returning API errors
- Need to troubleshoot MCP connection for write access
- Zoho CRM new UI causes browser automation timeouts (forms don't respond reliably)
- Complex n8n/WorkDrive architecture → over-engineering when email routing already exists
- Browser automation for Power Automate/Forms → blocked by React SPA security, wasted 20+ min before switching to artifact approach
- **[G-WORK-002]** Browser automation for GitHub file edits → CodeMirror editor blocks all programmatic input (form_input, JS setValue, typing). Solution: local file edits + auto-sync
- **[G-WORK-003]** [2026-02-04] Claude guidance gaps — Multiple "No response requested" moments when user needed explicit commands. User asked "guide me" and got no immediate response. User confused about what to follow. **Fix:** Always provide copy-pasteable terminal commands proactively. Never assume user knows next step.

---

## Process Improvements

> Automation candidates, friction points, efficiency gains

| Date | Area | Improvement | Status | Impact |
|------|------|-------------|--------|--------|
| 2026-02-01 | Data Flow | Use email routing vs complex n8n | Implemented | Simpler, reliable |
| 2026-02-01 | Reports | Change Weekly → Daily | Pending (Chok) | Faster feedback loop |
| 2026-02-01 | Format | XLS → CSV for all reports | Pending (Chok) | Easier parsing |

---

## Next Session Focus

> What to prioritize in the next working session

### Immediate — PTL 121 System Remaining Flows
1. **Flow 3 (121-OnFinalValidation)** — Email reply triggers completion + supervisor notification
2. **Flow 4 (121-WeeklyDeliveryCheck)** — Monday scheduled flow for delivery confirmation
3. **Flow 5 (121-OnDeliveryConfirmed)** — Award points based on Form 3 submission

### Parked
- **Kaizen Architecture Phase 1** — entity_monitor.py, system_monitor.py
- **[CHOK] Update Zoho CRM/Inventory reports to Daily** — See `02_Solartech/REPORT_CONFIGURATION.md`

### Completed This Session
- ✅ **PTL 121 Flow 1 FIXED** — 121-OnSubmission now working end-to-end
  - Root cause: Compose was outside For each loop, couldn't access Create_item outputs
  - Fix: Added Compose 1 + Send an email (V2) 1 INSIDE the For each loop
  - Compose 1 expression: `concat('https://forms.office.com/...&r121id=', string(outputs('Create_item')?['body/ID']))`
  - Test: Form submitted → Flow ran successfully → Email sent with correct Form 2 URL
- ✅ Deleted old broken Compose and For each 1 actions outside loop
- ✅ Flow saved and tested with green "Your flow ran successfully" confirmation

### Previously Completed
- ✅ Kaizen Phase 0 — Zoho CRM + Inventory API working
- ✅ CRM: read deals ✅, write tasks ✅
- ✅ Inventory: read items ✅, org_id captured
- ✅ Credentials stored: ~/Automation/config/zoho.env
- ✅ zoho_client.py exists with retry logic

### Blocked
- Zoho MCP connector — broken (missing criteria param), using direct API instead
- Eats365 API access — pending developer account request

---

## System Connections

> Integration points and credentials references (no actual credentials here)

| System | Used By | Integration Status | Notes |
|--------|---------|-------------------|-------|
| **Zoho CRM** | Solartech, Hippos | ✅ API Ready | Read/write via zoho_client.py, refresh token in zoho.env |
| **Zoho Inventory** | Solartech, Hippos | ✅ API Ready | Read via direct API, org_id=833030419 |
| **Zoho Analytics** | Solartech, Hippos | Active | Dashboards and reporting |
| **Odoo (MRP)** | WCI | Active | Manufacturing, BOMs, work orders |
| **Odoo (Inventory)** | WCI | Active | Warehouse management |
| **Odoo (Sales)** | WCI | Active | Customer management, quotations |
| **Eats365** | Kinme | Pending API | POS - need to request developer access |
| **IBKR** | Trading | Not connected | Will need API setup for automation |
| **iCloud** | All | Active | BizOS folder synced here |
| **n8n** | Automation | To be configured | Key for continuous improvement |

### System-Entity Map
```
Solartech ──► Zoho (CRM, Inventory, Analytics)
Hippos    ──► Zoho (CRM, Inventory, Analytics)
WCI       ──► Odoo (MRP, Inventory, Sales)
Kinme     ──► Eats365 (API access pending)
Trading   ──► IBKR
```

---

## 360° Loop Architecture

> Automated feedback loop for continuous improvement

### Data Flow
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Zoho CRM      │    │  Zoho Inventory │    │    Eats365      │
│   (Solartech)   │    │   (Solartech)   │    │    (Kinme)      │
└────────┬────────┘    └────────┬────────┘    └────────┬────────┘
         │                      │                      │
         │ Daily CSV            │ Daily CSV            │ Manual
         │ Reports              │ Reports              │ (API pending)
         │                      │                      │
         └──────────┬───────────┴──────────────────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │ automation@solartech │
         │     .com.my          │
         └──────────┬───────────┘
                    │
                    │ Auto-forward
                    │
                    ▼
         ┌──────────────────────┐
         │  BizOS/_INBOX/       │
         └──────────┬───────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │  Claude Analysis     │
         │  (Risk, KPIs, Flags) │
         └──────────┬───────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │  _CONTEXT.md         │
         └──────────────────────┘
```

### Configuration Status
| System | Report Frequency | Format | Status |
|--------|------------------|--------|--------|
| Zoho CRM | 3 Weekly, 1 Daily | XLS | **NEEDS UPDATE → Daily CSV** |
| Zoho Inventory | 3 Weekly | CSV | **NEEDS UPDATE → Daily** |
| Eats365 | Manual | Excel | API access pending |

**Config Guide**: `02_Solartech/REPORT_CONFIGURATION.md`

---

## Quick Reference

**Folder Structure**:
```
~/iCloud/ClaudeHub/           ← Mount this in Cowork
├── bizos/                    ← Business systems brain
│   ├── _CONTEXT.md           ← You are here (Claude's memory)
│   ├── _INBOX/               ← Drop files for Claude to process
│   ├── 01_Trading/ → 05_Kinme/
│   └── ...
├── cto-brain/                ← Shared engineering rules
│   ├── GLOBAL_STANDARDS.md   ← Rules (read at startup)
│   └── modules/grow-ptl/
└── trading/                  ← Trading systems brain
    ├── _CONTEXT.md
    └── ARCHITECTURE.md
```

**Startup Protocol** (only when user says "startup"):
1. Read `_CONTEXT.md` + `GLOBAL_STANDARDS.md`
2. Check `_INBOX/` for new files
3. Report status and offer to help

**During Session**: Reference context as needed. Update `_CONTEXT.md` at end.

**Commands**:
| Command | What it does |
|---------|--------------|
| `startup` | Full startup: read brain, check _INBOX, report status |
| `brief` | Generate daily briefs in `_briefs/daily/{date}/` |

**Brief Generation** (when user says "brief"):
1. Process any new _INBOX files first
2. Generate `_briefs/daily/{date}/_CTO_SUMMARY.md`
3. Generate entity briefs: `02_Solartech/BRIEF.md`, `03_Hippos/BRIEF.md`
4. Generate person briefs for flagged individuals
5. Update `_FLAG_TRACKER.md` with new/aged flags
6. Report summary to user

**_INBOX File Types**:
| Source | Pattern | Action |
|--------|---------|--------|
| Zoho CRM | `*Deals*.csv`, `*Enquiry*.csv` | Update risk model |
| Zoho Inventory | `*Inventory*.csv` | Check stock levels |
| Eats365 | `*.xls` | Update Kinme metrics |

---

*End of Context File*
