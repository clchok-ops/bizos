# BizOS Complete Guide

> Your AI-powered business operating system

**Version**: 1.0
**Created**: 2025-01-31
**Author**: Claude + Chok

---

## Table of Contents

1. [What is BizOS?](#what-is-bizos)
2. [Architecture Overview](#architecture-overview)
3. [Folder Structure](#folder-structure)
4. [How to Work with Claude](#how-to-work-with-claude)
5. [Entity Breakdown](#entity-breakdown)
6. [The Automation Layer (n8n)](#the-automation-layer-n8n)
7. [Setting Up Integrations](#setting-up-integrations)
8. [The Continuous Improvement Loop](#the-continuous-improvement-loop)
9. [Daily/Weekly Rituals](#dailyweekly-rituals)
10. [Troubleshooting & FAQ](#troubleshooting--faq)
11. [Quick Reference](#quick-reference)

---

## What is BizOS?

BizOS is an AI-powered operating system for managing your portfolio of businesses:

| Entity | Type | Primary System |
|--------|------|----------------|
| **Trading** | Investment (IBKR) | IBKR API |
| **Solartech** | B2B Distribution | Zoho One |
| **Hippos** | B2C Retail/Service | Zoho One |
| **WCI** | Manufacturing | Odoo |
| **Kinme** | F&B (Izakaya) | EatPOS365 |

### Core Principles

1. **Separation of Concerns** — Each entity has its own space, tools, and metrics
2. **Persistent Memory** — Claude remembers context via `_CONTEXT.md`
3. **Automated Monitoring** — n8n watches for anomalies so you don't have to
4. **Cross-Learning** — Insights from one entity improve others
5. **Execution Focus** — Tools for doing, not just planning

### What Problems This Solves

| Problem | BizOS Solution |
|---------|----------------|
| "I brief Claude every session" | `_CONTEXT.md` = persistent memory |
| "I forget to check metrics" | n8n alerts when thresholds breach |
| "Spreadsheets everywhere" | Centralized, structured folder system |
| "No time for weekly reviews" | Automated rollups and flags |
| "Insights don't transfer between businesses" | Cross-learning engine captures patterns |

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         YOUR SYSTEMS                            │
│                                                                 │
│   Zoho One          Odoo           EatPOS365        IBKR        │
│   (Solartech,       (WCI)          (Kinme)          (Trading)   │
│    Hippos)                                                      │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│                         n8n WORKFLOWS                          │
│                                                                │
│   • Scheduled data pulls (daily/weekly)                        │
│   • Threshold monitoring                                       │
│   • Anomaly detection                                          │
│   • Auto-update CONTEXT.md                                     │
│   • Alert notifications                                        │
└───────────────────────────────┬───────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│                        BizOS (iCloud)                          │
│                                                                │
│   _CONTEXT.md ◄──── Single source of truth                     │
│   _INBOX/     ◄──── Drop zone for Claude                       │
│   00_Holding/ ◄──── Portfolio-level artifacts                  │
│   01-05_XXX/  ◄──── Entity-specific tools & data               │
└───────────────────────────────┬───────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│                          CLAUDE                                │
│                                                                │
│   1. Reads _CONTEXT.md at session start                        │
│   2. Checks _INBOX/ for new items                              │
│   3. Works on priorities                                       │
│   4. Updates _CONTEXT.md at session end                        │
│   5. Learnings compound over time                              │
└───────────────────────────────────────────────────────────────┘
```

---

## Folder Structure

```
BizOS/                          ← Root folder (synced to iCloud)
│
├── _CONTEXT.md                 ← Claude's persistent memory
│                                  READ THIS FIRST EVERY SESSION
│
├── _INBOX/                     ← Drop files here for Claude
│   └── README.md                  - Exports, screenshots, notes
│                                  - Claude checks this each session
│
├── 00_Holding/                 ← Portfolio-level (Holding Company)
│   ├── BIZOS_GUIDE.md             - This guide
│   ├── N8N_AUTOMATIONS.md         - Automation specifications
│   ├── thresholds.json            - Alert threshold config
│   ├── portfolio_dashboard.xlsx   - (future) Cross-entity view
│   └── decision_log.md            - (future) Major decisions
│
├── 01_Trading/                 ← IBKR Trading (ISOLATED)
│   ├── TRADING_SYSTEM.md          - Methodology & philosophy
│   ├── journal.xlsx               - (future) Trade log
│   ├── performance.xlsx           - (future) Metrics dashboard
│   └── strategies/                - (future) Strategy docs
│
├── 02_Solartech/               ← B2B Distribution
│   ├── pricing_master.xlsx        - (future) Product pricing
│   ├── margin_analysis.xlsx       - (future) Margin tracking
│   └── pipeline.xlsx              - (future) Sales pipeline
│
├── 03_Hippos/                  ← B2C Retail (Water Hippos → Solar)
│   ├── pricing_master.xlsx        - (future) Service pricing
│   ├── job_costing.xlsx           - (future) Job profitability
│   └── customer_tracker.xlsx      - (future) B2C customers
│
├── 04_WCI/                     ← Manufacturing
│   ├── production_costing.xlsx    - (future) BOM & production costs
│   ├── transfer_pricing.xlsx      - (future) Intercompany pricing
│   └── inventory_tracker.xlsx     - (future) Stock levels
│
└── 05_Kinme/                   ← Japanese Izakaya
    ├── KINME_SYSTEM.md            - CFO toolkit framework
    ├── menu_engineering.xlsx      - (future) Menu analysis
    ├── food_cost_master.xlsx      - (future) Recipe costing
    └── daily_tracker.xlsx         - (future) Daily P&L
```

### File Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| System docs | `UPPERCASE_NAME.md` | `TRADING_SYSTEM.md` |
| Data files | `lowercase_name.xlsx` | `menu_engineering.xlsx` |
| Logs | `YYYY-MM-DD_description.md` | `2025-01-31_weekly_review.md` |
| Configs | `lowercase.json` | `thresholds.json` |

---

## How to Work with Claude

### Starting a Session

**Option A: Fresh conversation**
Just start talking. Claude will read `_CONTEXT.md` and know the current state.

```
You: "Let's work on Kinme pricing"
Claude: [Reads _CONTEXT.md] [Knows Kinme uses EatPOS365, current status, open items]
```

**Option B: Provide context explicitly**
If Claude seems unfamiliar, say:
```
You: "Read the BizOS context file first"
```

### Context Switching Between Entities

Be explicit about which entity you're working on:

```
✅ "Let's focus on Trading"
✅ "Switch to Kinme"
✅ "What's the status of WCI?"

❌ "What about the inventory?" (which entity?)
❌ "Check the sales" (which business?)
```

### Using the INBOX

Drop files in `_INBOX/` for Claude to process:

1. Export data from EatPOS365 → drop CSV in `_INBOX/`
2. Screenshot of Zoho dashboard → drop PNG in `_INBOX/`
3. Voice memo transcription → drop TXT in `_INBOX/`
4. Any document you want analyzed → drop in `_INBOX/`

Claude checks `_INBOX/` at the start of each session.

### Requesting Updates

```
You: "Update the context file with what we discussed"
Claude: [Updates _CONTEXT.md with decisions, learnings, next steps]
```

### Ending a Session

Claude should update `_CONTEXT.md` automatically, but you can prompt:

```
You: "Let's wrap up - update context and summarize"
```

---

## Entity Breakdown

### 01_Trading (IBKR)

**Philosophy**: Learn first, systematize later. No rules until patterns emerge from data.

**Key Files**:
- `TRADING_SYSTEM.md` — Methodology, journal structure, metrics
- `journal.xlsx` — Every trade logged with rationale and outcome
- `performance.xlsx` — Metrics dashboard (win rate, drawdown, etc.)

**Key Metrics**:
| Metric | Description | Target |
|--------|-------------|--------|
| Win Rate | % trades profitable | >40% |
| R-Multiple | Risk-adjusted return | >1.5 avg |
| Max Drawdown | Peak-to-trough decline | <5% |
| Profit Factor | Gross profit / gross loss | >1.5 |

**Thresholds** (see `thresholds.json`):
- Drawdown >5% → Alert
- Daily loss >2% → Alert
- 5 consecutive losses → Alert

---

### 02_Solartech (B2B Distribution)

**Type**: Parent company distributing solar, boiler, water products to B2B customers.

**System**: Zoho One (CRM, Inventory, Analytics)

**Key Files**:
- `pricing_master.xlsx` — Product catalog with costs, margins, prices
- `margin_analysis.xlsx` — Margin by product line, customer, deal
- `pipeline.xlsx` — Sales pipeline tracker

**Key Metrics**:
| Metric | Description | Target |
|--------|-------------|--------|
| Gross Margin | (Revenue - COGS) / Revenue | >25% |
| Pipeline Value | Total value of open deals | Track trend |
| Win Rate | Deals won / deals closed | >30% |
| Inventory Turnover | COGS / Avg Inventory | >4x/year |

**Intercompany**: Buys boilers from WCI. Track transfer pricing.

---

### 03_Hippos (B2C Retail)

**Type**: B2C retail/service. Currently "Water Hippos" (boiler/water). Transitioning to solar and energy management.

**System**: Zoho One (CRM, Inventory, Analytics)

**Key Files**:
- `pricing_master.xlsx` — Service packages, pricing tiers
- `job_costing.xlsx` — Cost and margin per job
- `customer_tracker.xlsx` — Customer database, repeat business

**Key Metrics**:
| Metric | Description | Target |
|--------|-------------|--------|
| Job Margin | Profit per job | >25% |
| CAC | Customer acquisition cost | Track |
| Repeat Rate | % customers who return | >30% |
| Avg Job Value | Revenue per job | Track trend |

**Transition Plan**: Document move from water/boiler to solar/energy.

---

### 04_WCI (Manufacturing)

**Type**: Boiler manufacturer. Supplies Solartech and Hippos.

**System**: Odoo (MRP, Inventory, Sales)

**Key Files**:
- `production_costing.xlsx` — BOM costs, labor, overhead
- `transfer_pricing.xlsx` — Prices to Solartech/Hippos
- `inventory_tracker.xlsx` — Raw materials, WIP, finished goods

**Key Metrics**:
| Metric | Description | Target |
|--------|-------------|--------|
| On-Time Delivery | Orders delivered on time | >90% |
| Scrap Rate | Waste / total production | <3% |
| Production Backlog | Days of pending orders | <7 days |
| Unit Cost | Fully-loaded cost per unit | Track trend |

**Intercompany**: Sells to Solartech (B2B) and Hippos (B2C). Transfer pricing critical.

---

### 05_Kinme (F&B)

**Type**: Japanese upmarket izakaya. Sake, sashimi, grill.

**System**: EatPOS365 (POS)

**Key Files**:
- `KINME_SYSTEM.md` — CFO toolkit framework
- `menu_engineering.xlsx` — Stars/Puzzles/Plow Horses/Dogs analysis
- `food_cost_master.xlsx` — Recipe costing, ingredient prices
- `daily_tracker.xlsx` — Daily revenue, covers, food cost

**Key Metrics**:
| Metric | Description | Target |
|--------|-------------|--------|
| Food Cost % | Food COGS / Food Revenue | 28-32% |
| Beverage Cost % | Bev COGS / Bev Revenue | 20-25% |
| Prime Cost % | (Food + Labor) / Revenue | <65% |
| Avg Spend/Cover | Revenue / Covers | Track trend |
| Covers/Service | Guest count per shift | Track trend |

**Menu Engineering Matrix**:
| Category | Popularity | Profitability | Action |
|----------|------------|---------------|--------|
| Stars | High | High | Promote |
| Plow Horses | High | Low | Reengineer |
| Puzzles | Low | High | Market more |
| Dogs | Low | Low | Remove |

---

## The Automation Layer (n8n)

### What n8n Does

n8n is the automation brain that:
1. **Pulls data** from your systems on schedule
2. **Monitors thresholds** and flags anomalies
3. **Updates CONTEXT.md** automatically
4. **Sends alerts** when intervention needed

### Workflow Catalog

| Workflow | Trigger | Source | Action |
|----------|---------|--------|--------|
| Kinme Daily Sales | 6 AM daily | EatPOS365 | Calculate metrics, flag anomalies |
| Kinme Weekly Food Cost | Monday 7 AM | EatPOS365 | Analyze food cost %, flag issues |
| Solartech/Hippos Pipeline | Monday 8 AM | Zoho CRM | Pipeline health, stalled deals |
| WCI Production | Monday 8 AM | Odoo | On-time rate, backlog, inventory |
| Trading Daily | 4 PM daily | IBKR | Positions, P&L, drawdown |
| Weekly Rollup | Sunday 9 PM | All | Compile summaries, clear old flags |

### Threshold Configuration

Edit `00_Holding/thresholds.json` to adjust alert triggers:

```json
{
  "kinme": {
    "food_cost_pct_max": 0.35,    // Alert if food cost >35%
    "revenue_drop_pct": 0.20      // Alert if revenue drops >20%
  },
  "trading": {
    "max_drawdown_pct": 0.05,     // Alert if drawdown >5%
    "daily_loss_limit_pct": 0.02  // Alert if daily loss >2%
  }
}
```

### How Flags Work

When a threshold is breached, n8n appends to `_CONTEXT.md`:

```markdown
## Flags & Anomalies

| Date | Entity | Type | Flag | Status |
|------|--------|------|------|--------|
| 2025-02-01 | Kinme | COST | Food cost hit 37% (threshold: 35%) | Open |
| 2025-02-01 | Trading | RISK | Drawdown at 6% (threshold: 5%) | Open |
```

**You only engage when there's a flag.** No flag = everything within tolerance.

---

## Setting Up Integrations

### Step 1: EatPOS365 (Kinme)

1. **Check API availability**
   - Log into EatPOS365 admin
   - Look for "API" or "Integrations" or "Developer" section
   - If no API, check if they support data export (CSV)

2. **Get credentials**
   - API key or OAuth setup
   - Store securely (not in BizOS)

3. **Test in n8n**
   - Create HTTP Request node
   - Test pulling transactions endpoint

4. **Fallback: Manual export**
   - Export daily/weekly CSV
   - Drop in `_INBOX/`
   - Claude processes manually

### Step 2: Zoho One (Solartech, Hippos)

1. **Enable API access**
   - Zoho Developer Console: https://api-console.zoho.com/
   - Create a "Self Client" application
   - Get Client ID and Client Secret

2. **Configure OAuth in n8n**
   - Add Zoho CRM credentials
   - Authorize access to CRM, Inventory, Analytics

3. **Test endpoints**
   - Pull deals from CRM
   - Pull inventory levels
   - Pull analytics reports

### Step 3: Odoo (WCI)

1. **Enable API access**
   - Odoo Settings → Technical → Database Structure
   - Or use XML-RPC (built into Odoo)

2. **Get credentials**
   - Database name
   - Username + API key (or password)
   - Server URL

3. **Configure in n8n**
   - Use HTTP Request with XML-RPC
   - Or use community Odoo node

### Step 4: IBKR (Trading)

1. **Enable Client Portal API**
   - IBKR Account Management → Settings → API
   - Generate API keys

2. **Or use TWS API**
   - Download TWS or IB Gateway
   - Enable socket connections

3. **Start with paper trading**
   - Test all integrations on paper account first
   - Validate data accuracy before live

### Step 5: Connect n8n to BizOS Folder

**Option A: Direct file system (if n8n runs locally)**
- Point n8n to iCloud path
- Use "Read/Write File" nodes

**Option B: iCloud API (if n8n is cloud-hosted)**
- Use iCloud Drive API
- Requires Apple Developer setup

**Option C: Sync folder alternative**
- Use Dropbox/OneDrive instead
- Native n8n nodes available

---

## The Continuous Improvement Loop

### How Learning Compounds

```
┌─────────────────────────────────────────────────────────────┐
│                    CONTINUOUS IMPROVEMENT                   │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   ┌─────────┐          ┌─────────┐          ┌─────────┐
   │ OBSERVE │          │ DECIDE  │          │ RECORD  │
   │         │          │         │          │         │
   │ n8n     │    ──►   │ You +   │    ──►   │ Claude  │
   │ pulls   │          │ Claude  │          │ logs to │
   │ data    │          │ analyze │          │ CONTEXT │
   └─────────┘          └─────────┘          └─────────┘
        │                                         │
        │                                         │
        │         ┌─────────────────┐             │
        └────────►│     LEARN       │◄────────────┘
                  │                 │
                  │ Patterns emerge │
                  │ Rules form      │
                  │ Processes       │
                  │ improve         │
                  └─────────────────┘
                          │
                          ▼
                  ┌─────────────────┐
                  │   SYSTEMATIZE   │
                  │                 │
                  │ Update          │
                  │ thresholds,     │
                  │ workflows,      │
                  │ playbooks       │
                  └─────────────────┘
```

### What Gets Captured

| Type | Where Logged | Example |
|------|--------------|---------|
| Decisions | `_CONTEXT.md` → Decision Log | "Raised sake prices 10%" |
| Outcomes | `_CONTEXT.md` → Entity State | "No volume drop after price increase" |
| Learnings | `_CONTEXT.md` → Learnings | "Kinme customers are price-insensitive on premium sake" |
| Process Improvements | `_CONTEXT.md` → Process Improvements | "Automated daily food cost calc saves 30 min" |
| Flags | `_CONTEXT.md` → Flags & Anomalies | "Food cost spiked—investigate supplier pricing" |

### Cross-Entity Learning

Insights from one business can apply to others:

| Learning Source | Learning | Applicable To |
|-----------------|----------|---------------|
| Kinme | "Premium pricing works when quality is visible" | Solartech B2B, Hippos B2C |
| Trading | "Cutting losses early preserves capital for winners" | All businesses (kill failing initiatives fast) |
| WCI | "Buffer stock prevents delivery delays" | Solartech inventory |

---

## Daily/Weekly Rituals

### Daily (Automated)

| Time | Action | Who |
|------|--------|-----|
| 6:00 AM | Kinme daily sales summary | n8n |
| 4:00 PM | Trading position check | n8n |
| Continuous | Threshold monitoring | n8n |

**You do nothing daily** unless there's a flag.

### Weekly (Minimal Manual)

| Day | Action | Who |
|-----|--------|-----|
| Sunday 9 PM | Weekly rollup compiled | n8n |
| Monday AM | Review flags in CONTEXT.md | You (5 min) |
| Monday AM | Address any flagged issues | You + Claude |

**Weekly review is 5-10 minutes** unless there are issues.

### Monthly (Strategic)

| Action | Who |
|--------|-----|
| Review Decision Log outcomes | You + Claude |
| Adjust thresholds if needed | You + Claude |
| Cross-entity learning synthesis | Claude |
| System improvements | You + Claude |

### Quarterly (Portfolio)

| Action | Who |
|--------|-----|
| Full portfolio review | You + Claude |
| Capital allocation decisions | You |
| Major strategic shifts | You + Claude |
| System architecture review | Claude |

---

## Troubleshooting & FAQ

### "Claude doesn't remember our last conversation"

**Solution**: Ask Claude to read `_CONTEXT.md`:
```
You: "Read the BizOS context file and continue where we left off"
```

### "The automation isn't updating CONTEXT.md"

**Check**:
1. Is n8n running?
2. Are credentials still valid?
3. Is the file path correct?
4. Check n8n execution logs for errors

### "I'm getting too many alerts"

**Solution**: Adjust thresholds in `thresholds.json`:
```json
"food_cost_pct_max": 0.35  // Raise to 0.38 if 35% triggers too often
```

### "How do I add a new business entity?"

1. Create folder: `06_NewEntity/`
2. Create system doc: `NEWENTITY_SYSTEM.md`
3. Add to `_CONTEXT.md` → Portfolio Overview
4. Add to `_CONTEXT.md` → Entity States
5. Add thresholds to `thresholds.json`
6. Create n8n workflows

### "The data in CONTEXT.md is wrong"

**Solution**: You can manually edit `_CONTEXT.md` anytime. It's just a markdown file. Claude will pick up your changes next session.

### "I want to change the folder structure"

Go ahead. Just update:
1. The actual folders
2. `_CONTEXT.md` → Quick Reference section
3. This guide's Folder Structure section

### "How do I share access with a team member?"

1. Share the iCloud folder with them
2. Create their own Claude account
3. They follow the same session protocol

Note: Consider which sections should be shared (maybe not Trading?).

---

## Quick Reference

### Session Checklist

```
□ Claude reads _CONTEXT.md
□ Claude checks _INBOX/
□ Work on highest priority
□ Log decisions and learnings
□ Update _CONTEXT.md before ending
```

### Key Files

| File | Purpose | Location |
|------|---------|----------|
| `_CONTEXT.md` | Claude's memory | `/BizOS/` |
| `thresholds.json` | Alert triggers | `/00_Holding/` |
| `N8N_AUTOMATIONS.md` | Workflow specs | `/00_Holding/` |
| `TRADING_SYSTEM.md` | Trading methodology | `/01_Trading/` |
| `KINME_SYSTEM.md` | F&B CFO toolkit | `/05_Kinme/` |

### Entity-System Map

```
Trading   → IBKR
Solartech → Zoho (CRM, Inventory, Analytics)
Hippos    → Zoho (CRM, Inventory, Analytics)
WCI       → Odoo (MRP, Inventory, Sales)
Kinme     → EatPOS365
```

### Threshold Defaults

| Entity | Metric | Threshold |
|--------|--------|-----------|
| Kinme | Food Cost % | <35% |
| Kinme | Revenue Drop | <20% |
| Trading | Max Drawdown | <5% |
| Trading | Daily Loss | <2% |
| WCI | On-Time Delivery | >90% |

### Commands for Claude

```
"Read the BizOS context"          → Load current state
"Focus on [Entity]"               → Switch context
"Update context with this"        → Save decisions/learnings
"What's flagged?"                 → Review anomalies
"Process the inbox"               → Handle dropped files
"Create the [X] spreadsheet"      → Build a tool
```

---

## Next Steps

### Immediate (This Week)

1. [ ] Verify EatPOS365 API access
2. [ ] Export Kinme sales data (last 30 days)
3. [ ] Export Kinme menu with prices
4. [ ] Get ingredient costs for top 10 dishes
5. [ ] Set up first n8n workflow (Kinme daily)

### Short-Term (This Month)

1. [ ] Complete Kinme CFO toolkit
2. [ ] Create Trading journal spreadsheet
3. [ ] Connect Zoho APIs for Solartech/Hippos
4. [ ] Connect Odoo API for WCI
5. [ ] All 6 n8n workflows operational

### Medium-Term (This Quarter)

1. [ ] Full automation running hands-free
2. [ ] Cross-entity dashboard in 00_Holding
3. [ ] First quarterly review with data
4. [ ] Refine thresholds based on experience
5. [ ] Document playbooks for common decisions

---

*"The best operating system is one you don't notice running."*

---

**End of Guide**
