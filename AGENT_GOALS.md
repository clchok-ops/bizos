# BizOS Agent Goals
> Domain-specific goals for BizOS autonomous agents. Defines what each agent session works toward.
> Created: 2026-02-10

---

## CRM Ops Agent

**Mission:** Drive deal effectiveness — speed of processes, win rate, traceability, and customer feedback.

### Primary Metrics

| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| Win rate (overall) | 37.8% small, 20.9% large | 45% / 30% | Zoho closed-won / total closed |
| Deal velocity (avg days to close) | TBD | Reduce 20% | Zoho stage duration analysis |
| Follow-up compliance | Unknown | 95% within SLA | Zoho activity staleness check |
| Customer feedback score | Not tracked | Establish baseline | Post-close survey (to build) |
| Pipeline concentration risk | 70% in 2 owners | <50% in top 2 | Zoho owner distribution |

### Entity Scope

**Solartech** (primary — RM 20.5M pipeline):
- Stalled deal intervention (PD-000127 stuck 347 days)
- Deal stage transition monitoring
- Owner workload balancing
- Follow-up automation for aging deals
- Risk scoring and early warning alerts (WF03)

**Hippos** (secondary — structure in place, ops data needed):
- CRM usage adoption tracking
- Deal entry quality checks
- Basic pipeline health monitoring

### Agent Behaviors

**Phase 1 (Current):** Observe and alert via Telegram
- Daily pipeline risk scan → alert on stalled deals, concentration risk
- Weekly win/loss ratio summary
- Flag deals approaching stage SLA

**Phase 2 (Next):** Prepare + approve actions
- Draft follow-up emails for stalled deals → owner approves via Telegram
- Propose deal stage updates when evidence suggests progression
- Generate weekly team performance summary with recommendations

**Phase 3 (Future):** Auto-execute proven patterns
- Auto-send templated follow-ups after N consecutive approvals
- Auto-flag and reassign deals from overloaded owners (with notification)

### Data Sources
- Zoho CRM (deals, contacts, activities, notes)
- _INBOX/zoho/ (daily Ongoing Deals reports)
- Entity KPIs (TTL_KPIS.md)

---

## Performance Management Agent (TTL/PTL)

**Mission:** Build and iterate the TTL/PTL performance system across all entities — using SharePoint as the data home and Power Automate for workflows. Drive accountability, measure outcomes, and enable team improvement through the 100-point PTL framework.

### System Context

**Data Home:** SharePoint People Growth (waterhippos.sharepoint.com/sites/PeopleGrowth)
**Workflows:** Power Automate (via O365 PA Agent — see `cto-brain/designs/O365_PA_AGENT_ARCHITECTURE.md`)
**Framework:** PTL 100-pt model (bizos/00_Holding/PTL_FRAMEWORK.md)
**Specs + Scripts:** `cto-brain/modules/grow-ptl/`

### Primary Metrics

| Level | Metric | Scope | Target |
|-------|--------|-------|--------|
| TTL | Entity health score | All 4 entities | Composite (revenue + process + team + customer) → drives bonus pool (0/10/15/20%) |
| PTL | Key Results (20pts) | Per role | 80% of roles at Yellow (≥75%) or above |
| PTL | Grow (15pts) | Per player | Active development plans for all players |
| PTL | 121 (15pts) | Per player | 95% 121 meeting compliance |
| PTL | Kaizen (25pts) | Per player | ≥1 improvement contribution/quarter |
| PTL | Customer (25pts) | Per player | Entity-specific customer satisfaction targets |

### Entity Scope

**All entities** (02_Solartech, 03_Hippos, 04_WCI, 05_Kinme):

| Entity | TTL Status | Roles Status | Key System |
|--------|-----------|-------------|------------|
| Solartech | Draft — proposed metrics, no targets | 7 role files (B2B Lead, B2C PodLead, etc.) — targets TBD | Zoho CRM |
| Hippos | Draft — proposed metrics only | Scaffolded only (_ROLES_INDEX.md) | Zoho CRM (Enquiries) |
| WCI | Draft — proposed metrics only | Scaffolded only (_ROLES_INDEX.md) | Odoo (MRP) |
| Kinme | Draft — financial + ops KPIs set, no PTL targets | Scaffolded (Restaurant Mgr, Head Chef, Floor Staff) — not created | Eats365 POS |

### Deliverables

1. **SharePoint lists** — 121 logs, PTL scores, KPI targets, review records (per entity)
2. **Power Automate flows** — 121 submission → scoring → notification → delivery confirmation pipeline
3. **Role KPI targets** — Actual RM/metric targets for Key Results area, per role, per entity
4. **Review templates** — Quarterly review framework using PTL scores (SharePoint + Forms)
5. **Entity health dashboard** — TTL composite scoring (future: Power BI)
6. **Accountability workflows** — Automated 121 check-ins, target vs actual, escalation

### Agent Behaviors

**Phase 1:** Complete 121 system + populate role targets
- Build remaining PA flows (Flow 5 fix, delivery confirmation)
- Populate actual KPI targets for Solartech roles (RM values, % targets)
- Create role files for WCI and Kinme (from _ROLES_INDEX.md templates)
- Deploy SharePoint lists for all 4 entities

**Phase 2:** Automated tracking + scoring
- Monthly TTL entity health reports via Telegram
- Quarterly PTL score summaries per player
- Flag underperformance early (player drops to Red/Grey before quarterly review)
- 121 compliance tracking (missed meetings → escalation)

**Phase 3:** Proactive recommendations
- Suggest KPI target adjustments based on historical achievement data
- Generate training plans based on PTL area gaps (e.g., low Kaizen → improvement workshops)
- Cross-entity performance benchmarking

### Write Zones (Parallel Safety)

This agent writes to:
- `cto-brain/modules/grow-ptl/` — specs, scripts, flow definitions
- `cto-brain/designs/O365_PA_AGENT_ARCHITECTURE.md` — architecture doc
- SharePoint (via Power Automate) — lists, forms, flows
- `bizos/[entity]/roles/` — role KPI files (READ from entity files, WRITE only to roles/)
- `bizos/[entity]/TTL_KPIS.md` — TTL target updates

**No conflict with CRM Ops Agent** — CRM writes to Zoho and `bizos/[entity]/_ENTITY.md`. Perf Mgmt writes to SharePoint and `roles/` + `TTL_KPIS.md`. Different files within same entity folders.

**Caution:** If both agents are active on same entity, coordinate via _SESSIONS/active/ registry. CRM owns _ENTITY.md; Perf Mgmt owns roles/ and TTL_KPIS.md.

### Data Sources
- SharePoint People Growth (121 logs, PTL scores, review records)
- Entity _ENTITY.md + TTL_KPIS.md files (READ)
- Role definitions: roles/ in each entity
- PTL Framework: bizos/00_Holding/PTL_FRAMEWORK.md
- O365 PA Architecture: cto-brain/designs/O365_PA_AGENT_ARCHITECTURE.md
- grow-ptl module: cto-brain/modules/grow-ptl/ (specs, scripts, flow definitions)
- Zoho CRM activity data (for sales role KPIs)
- Eats365 POS data (for Kinme ops role KPIs)
- Odoo MRP data (for WCI production role KPIs)

---

## Shared Standards

All BizOS agents follow:
- cto-brain/CORE_RULES.md (universal engineering rules)
- bizos/STRUCTURE.md (file organization)
- Session coordination via _SESSIONS/ (no parallel writes to same entity)
- Learning logged via `learn bizos:` prefix
