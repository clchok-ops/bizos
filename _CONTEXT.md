# BizOS Context File
> **Purpose**: This is Claude's persistent memory. Read this at the START of every session. Update it at the END of every session.

**Last Updated**: 2025-01-31
**Updated By**: Claude (initial setup)

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
| Solartech | B2B Distribution | 🟡 To map | — | — |
| Hippos | B2C Retail | 🟡 To map | — | — |
| WCI | Manufacturing | 🟡 To map | — | — |
| Kinme | F&B (Izakaya) | 🟡 Setting up | 2025-01-31 | — |

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
**Status**: Systems identified
**Type**: Parent company, B2B distribution for solar/boiler/water
**Systems**: Zoho CRM, Zoho Inventory, Zoho Analytics

**Open Items**:
- [x] Map current systems → Zoho (CRM, Inventory, Analytics)
- [ ] Understand product lines and pricing structure
- [ ] Identify intercompany relationships with WCI/Hippos
- [ ] Export sample data from Zoho for analysis

**Recent Decisions**: None yet
**Learnings**: None yet

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
| 2026-01-31 | Kinme | COST | Discount rate at 21.7% - investigate discount policy | Open |
| 2026-01-31 | Kinme | DATA | Food costs not tracked in POS - need manual input | Open |
| 2026-01-31 | Kinme | DATA | Only 1 day of data - need 30 days for trends | Open |

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
- (None yet)

### Cross-Entity Patterns
- (None yet)

### What Worked
- (None yet)

### What Didn't Work
- (None yet)

---

## Process Improvements

> Automation candidates, friction points, efficiency gains

| Date | Area | Improvement | Status | Impact |
|------|------|-------------|--------|--------|
| — | — | None yet | — | — |

---

## Next Session Focus

> What to prioritize in the next working session

1. **Kinme: Input food costs** — Fill yellow cells in CFO Toolkit
2. **Kinme: Export 30 days data** — For proper trend analysis
3. **Kinme: Investigate discounts** — Why 21.7%?
4. **Trading: Log first trade** — Start the learning loop
5. **n8n: Build first workflow** — Kinme daily sales automation
6. **API: Request Eats365 developer access** — Email sent?

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
