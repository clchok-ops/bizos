# BizOS

> AI-powered business operating system for portfolio management

## Overview

BizOS is a self-improving system for managing multiple business entities with automated monitoring, continuous learning, and AI-assisted decision-making.

## Entities

| Entity | Type | System | Status |
|--------|------|--------|--------|
| **Trading** | Investment (IBKR) | IBKR API | Active |
| **Solartech** | B2B Distribution | Zoho One | Active |
| **Hippos** | B2C Retail/Service | Zoho One | Active |
| **WCI** | Manufacturing | Odoo | Active |
| **Kinme** | F&B (Izakaya) | Eats365 | Active |

## Structure

```
BizOS/
├── _CONTEXT.md           # Claude's persistent memory
├── _INBOX/               # Drop zone for data imports
├── 00_Holding/           # Portfolio-level docs & config
├── 01_Trading/           # IBKR trading system
├── 02_Solartech/         # B2B solar/boiler/water distribution
├── 03_Hippos/            # B2C retail (Water Hippos → Solar)
├── 04_WCI/               # Boiler manufacturing
└── 05_Kinme/             # Japanese izakaya
```

## How It Works

1. **Data flows in** from source systems (Eats365, Zoho, Odoo, IBKR)
2. **n8n monitors** thresholds and flags anomalies
3. **Claude reads** `_CONTEXT.md` for persistent memory each session
4. **Learnings compound** through decision logs and cross-entity patterns
5. **Dashboards** track KPIs per entity

## Key Files

- `_CONTEXT.md` - Start here. Claude's memory and current state.
- `00_Holding/BIZOS_GUIDE.md` - Full documentation
- `00_Holding/SETUP_PLAYBOOK.md` - Integration setup instructions
- `00_Holding/thresholds.json` - Alert configuration

## Getting Started

1. Clone this repo
2. Read `_CONTEXT.md` for current state
3. Check `00_Holding/BIZOS_GUIDE.md` for full documentation
4. Export data from your systems → drop in `_INBOX/`

## Automation

See `00_Holding/N8N_AUTOMATIONS.md` for workflow specifications.

---

*Built with Claude | Self-improving by design*
