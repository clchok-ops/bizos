# BizOS Context File
> **Purpose**: This is Claude's persistent memory. Read this at the START of every session. Update it at the END of every session.

**Last Updated**: 2026-01-31
**Updated By**: Claude (Solartech risk model built)

---

## How To Use This File

### For Claude (me):
1. **START of session**: Read this entire file before responding to user
2. **DURING session**: Reference active decisions and entity states
3. **END of session**: Update relevant sections with new information, decisions, learnings
4. **Always**: Keep entries concise, actionable, and timestamped

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
| Trading (IBKR) | Investment | 🟡 Setting up | 2025-01-31 | — |
| Solartech | B2B Distribution | 🟡 Risk model active | 2026-01-31 | RM 20.5M at risk |
| Hippos | B2C Retail | 🟡 To map | — | — |
| WCI | Manufacturing | 🟡 To map | — | — |
| Kinme | F&B (Izakaya) | 🟢 Analyzed | 2026-01-31 | 2% avg discount |

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
**Status**: Systems identified
**Type**: B2C retail/service (currently Water Hippos)
**Systems**: Zoho CRM, Zoho Inventory, Zoho Analytics
**Transition**: Moving to solar and energy management this year

**Open Items**:
- [x] Map current systems → Zoho (CRM, Inventory, Analytics)
- [ ] Understand B2C pricing and job costing
- [ ] Document transition plan to solar/energy
- [ ] Export sample data from Zoho for analysis

**Recent Decisions**: None yet
**Learnings**: None yet

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
**Status**: CFO Toolkit built, needs food cost input
**Type**: Japanese upmarket izakaya (sake, sashimi, grill)
**Systems**: Eats365 (POS) - https://www.eats365pos.com/

**Key Metrics (2026-01-31)**:
- Net Sales: RM 10,643
- Covers: 26
- Avg Spend: RM 409 ✅
- Discount Rate: 21.7% ⚠️ HIGH

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

---

## Active Decisions

> Decisions pending input or action

| ID | Entity | Decision Needed | Context | Deadline | Owner |
|----|--------|-----------------|---------|----------|-------|
| — | — | No active decisions | — | — | — |

---

## Decision Log

> Record of decisions made and their outcomes

### 2025-01

**[2025-01-31] Architecture Decision**
- **Decision**: Adopt sustainable BizOS architecture with CONTEXT.md as persistent memory, n8n for automation, and integration with existing Zoho/Odoo systems
- **Rationale**: Static spreadsheets not sustainable; need system that learns and improves automatically without manual weekly reviews
- **Outcome**: Pending (just implemented)

---

## Learnings & Patterns

> What we've learned that applies across entities

### Process Learnings
- Historical data eliminates "observation period" - can build models same day
- Backtesting on closed deals validates model before going live
- 4,209 deals → actionable risk model in <15 minutes

### Cross-Entity Patterns
- (Pending Hippos/WCI analysis for comparison)

### What Worked
- Compressed timeline: Historical data analysis vs waiting to observe
- Risk scoring with specific thresholds (not vague "at risk" labels)
- Backtest validation (92.8% accuracy) before recommending

### What Didn't Work
- Zoho MCP `get_deal_by_name` and `list_open_deals` returning API errors
- Need to troubleshoot MCP connection for write access

---

## Process Improvements

> Automation candidates, friction points, efficiency gains

| Date | Area | Improvement | Status | Impact |
|------|------|-------------|--------|--------|
| — | — | None yet | — | — |

---

## Next Session Focus

> What to prioritize in the next working session

1. **Solartech: Validate high-risk deals** — Does the flagged list match reality?
2. **Solartech: Enable daily scan** — Automate risk detection via Zoho MCP
3. **Solartech: Test Zoho write access** — Can we auto-flag deals?
4. **Hippos: Export deals data** — Build parallel risk model
5. **Define first autonomous action** — What can Claude auto-do?
6. **n8n: Deploy first workflow** — Daily Solartech risk scan

---

## System Connections

> Integration points and credentials references (no actual credentials here)

| System | Used By | Integration Status | Notes |
|--------|---------|-------------------|-------|
| **Zoho CRM** | Solartech, Hippos | Active | Sales pipeline, contacts, deals |
| **Zoho Inventory** | Solartech, Hippos | Active | Stock management, orders |
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

## Quick Reference

**Folder Structure**:
```
BizOS/
├── _CONTEXT.md      ← You are here (Claude's memory)
├── _INBOX/          ← Drop files for Claude to process
├── 00_Holding/      ← Portfolio-level artifacts
├── 01_Trading/      ← IBKR (isolated)
├── 02_Solartech/    ← B2B distribution
├── 03_Hippos/       ← B2C retail
├── 04_WCI/          ← Manufacturing
└── 05_Kinme/        ← F&B
```

**Session Protocol**:
1. Claude reads `_CONTEXT.md`
2. Check `_INBOX/` for new items
3. Work on highest priority from "Next Session Focus"
4. Update `_CONTEXT.md` before session ends

---

*End of Context File*
