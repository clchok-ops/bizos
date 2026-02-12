# Solartech CRM — First Principles Root Cause Analysis

**Date:** 2026-02-12
**Input:** Full CRM architecture scan (11 modules, 560+ fields), entity metrics, team pain points
**Purpose:** Identify WHY the team's operational problems exist, then rank solutions

---

## What a CRM Is Supposed to Do

Four jobs:

1. **Capture data** — Record what's happening with customers and deals
2. **Enforce process** — Guide people through the right steps in the right order
3. **Automate repetitive work** — Notifications, updates, calculations, follow-ups
4. **Surface insights** — What's working, what's at risk, where to focus

## What Your CRM Actually Does Today

1. **Capture data** — YES. 204 fields in Deals, 176 custom, 4 layouts, comprehensive T&C module, well-structured Quote → SO → Invoice → DO flow. The data model is solid.
2. **Enforce process** — NO. Zero blueprints. 4 validation rules (only on Direct and Troubleshoot layouts). A deal can jump from Qualification to Closed Won without filling in a single field.
3. **Automate repetitive work** — NO. Zero workflow rules. Every notification, reminder, status update, and follow-up depends on someone remembering to do it.
4. **Surface insights** — PARTIAL. Risk model built (92.8% accuracy) but not deployed in CRM. No automated dashboards or alerts.

**The gap between job 1 (done well) and jobs 2-4 (not done) is the root cause of every operational pain point.**

---

## The Seven Pain Points — Traced to Root Causes

### 1. Slow Quoting

- **Surface:** Sales reps use external spreadsheets to calculate quotes
- **Why:** 87% of SKUs have no pricing in Zoho
- **Why deeper:** Pricing data was never fully migrated into Zoho Inventory
- **Root cause:** DATA INFRASTRUCTURE — no pricing master data in the system

### 2. Stale Prices

- **Surface:** Prices in quotes don't match current supplier costs
- **Why:** No automated process to update prices when costs change
- **Why deeper:** No workflow rule flags when pricing is outdated
- **Root cause:** NO AUTOMATION — pricing lifecycle has no triggers or alerts

### 3. Hot vs Junk Leads

- **Surface:** Sales reps can't tell which leads are worth pursuing
- **Why:** No lead scoring or qualification criteria enforced in CRM
- **Why deeper:** No mandatory fields at Qualification stage, no scoring rules
- **Root cause:** NO PROCESS ENFORCEMENT — pipeline entry has no quality gate

### 4. Quote-BOM Disconnect

- **Surface:** What sales quotes ≠ what operations builds
- **Why:** 101 orphan composite mappings in Zoho Inventory
- **Why deeper:** Quote line items aren't validated against the operational BOM
- **Root cause:** DATA INFRASTRUCTURE + NO VALIDATION — broken master data and no cross-check

### 5. Workplan Missing Details

- **Surface:** Operations receives incomplete specs from sales
- **Why:** No mandatory fields required before the sales → ops handoff
- **Why deeper:** No stage-gate that blocks advancement without required information
- **Root cause:** NO PROCESS ENFORCEMENT — handoff points have no quality gates

### 6. Missed SalesIQ Messages

- **Surface:** Customer inquiries via SalesIQ go unanswered
- **Why:** SalesIQ isn't connected to CRM task/notification system
- **Why deeper:** No integration or workflow creates CRM tasks from SalesIQ events
- **Root cause:** SYSTEM INTEGRATION GAP — disconnected channels

### 7. No Customer Onboarding

- **Surface:** After deal won, no structured onboarding process kicks off
- **Why:** No workflow triggered by the "Deal Won" stage transition
- **Why deeper:** No task template, checklist, or automated sequence exists
- **Root cause:** NO AUTOMATION — post-sale process is entirely manual

---

## Three Root Causes Behind Everything

Every pain point traces back to one of three gaps:

### A. No Process Enforcement (→ Pain Points 3, 5, and contributes to 1, 4)

Your CRM has 29 stages across 4 layouts but ZERO blueprints. A deal can jump from any stage to any other stage without restriction. No mandatory fields are enforced at transitions. Information loss at every handoff is inevitable when there's nothing preventing it.

**The 29 stages aren't the problem — the lack of rules about how to move between them is.**

The stages actually serve different purposes:
- **Sales stages:** Qualification → Needs Analysis → Value Proposition → Negotiation → Deal Won
- **Regulatory stages:** CAS, ST & NEM, ST & TNB, Pre Application
- **Delivery stages:** Delivery, Fulfilment, Delivered
- **Lifecycle stages:** Onboarding, Feedback, Retention
- **Recovery stages:** Idle, Reactivate

These are parallel tracks, not a single pipeline. Different layouts (Direct, Project, Trading, Troubleshoot) should have different valid transitions. Without blueprints, all 29 stages are available to all layouts — which is chaos.

### B. No Automation (→ Pain Points 2, 6, 7, and contributes to all)

Zero workflow rules. This means:
- Nobody gets alerted when a deal has been sitting at "Idle" for 90 days (PD-000127: 347 days)
- Nobody gets reminded when a collection is overdue (RM 10.77M outstanding across 70 deals)
- Nobody gets notified when a customer submits a SalesIQ message
- Nobody gets a task list when a deal hits "Deal Won"
- No fields update automatically when conditions change

Everything depends on individual memory and discipline. With a growing team and RM 207.9M pipeline, memory doesn't scale.

### C. Data Infrastructure Gaps (→ Pain Points 1, 4, and contributes to 2)

The foundation data that quoting and ordering depend on isn't in the system:
- 87% of SKUs have no pricing in Zoho → every quote is a manual spreadsheet exercise
- 101 orphan composite mappings → quote line items don't match what operations needs to build
- 43% of inventory items (660/1,524) still need manual category classification

You can't automate quoting if there's nothing to automate from. You can't validate quotes against BOM if the BOM data is broken.

---

## Why These Gaps Exist

This isn't a design failure — the CRM's data model is actually well-architected. The T&C module as a normalized master data hub, the 3-way lookup relationships, the 4 distinct layouts for different deal types — these are good architectural decisions.

The gap is between **structure** and **enforcement**. The team built a solid data model but hasn't layered process rules, automation, or validation on top of it. The CRM captures information but doesn't direct behavior.

This is common. It happens because:
1. Zoho CRM setup focuses on fields and layouts first (visible, tangible)
2. Blueprints, workflow rules, and validation come second (invisible, abstract)
3. As the team grows and deal volume increases, the manual processes that worked with 5 people break with 15

---

## The Financial Impact

What these gaps are costing right now:

| Gap | Financial Impact | Evidence |
|-----|-----------------|----------|
| No collection automation | RM 10.77M outstanding across 70 deals | Top 5 alone = RM 3.73M |
| No idle deal alerts | RM 20.5M at-risk pipeline (24 high, 62 medium risk deals) | PD-000127: RM 1.59M stuck 347 days |
| Slow quoting | 20.9% large deal win rate (vs 37.8% overall) | Slow quotes lose large deals to competition |
| No process gates | Information loss at handoffs → rework, delays | Workplan issues, BOM mismatch |

**Conservative estimate:** Improving large deal win rate by even 5 percentage points (20.9% → 25.9%) on RM 114.8M active pipeline = RM 5.74M additional revenue. Recovering 10% of outstanding collections = RM 1.08M.

---

## Solutions — Mapped to Root Causes

### For Root Cause A: No Process Enforcement

**Solution A1: Blueprints per Layout**
- Define the valid stage transitions for each of the 4 layouts (Direct, Project, Trading, Troubleshoot)
- Set mandatory fields at each stage gate
- Each layout gets its own pipeline flow reflecting its business reality
- Requires: Chok to define the stage flows (only he knows the business logic)
- Deploy: UI creation (Zoho Blueprints can't be created via API), then API modification
- Impact: Addresses pain points 3, 5 directly. Foundation for all other automation.

**Solution A2: Enhanced Validation Rules**
- Currently: 4 rules (2 on Direct, 1 on Direct for Payment Terms, 1 on Troubleshoot)
- Add layout-specific validation for critical fields (contact info, technical specs, financial data)
- Deploy: Via API through WF-ZOHO-DEPLOY
- Impact: Quick data quality improvement, lower effort than blueprints

### For Root Cause B: No Automation

**Solution B1: Notification Workflow Rules (Quick Wins)**
- Idle deal alert: Deal at "Idle" > 30 days → notify owner + manager
- Collection reminder: Payment overdue > 7 days → notify owner, escalate at 30/60/90 days
- Stage-stuck alert: Deal hasn't moved stages in 60 days → notify owner
- Document reminder: Required docs not uploaded within 14 days of stage change → notify
- Deploy: Via API through WF-ZOHO-DEPLOY
- Impact: Immediate visibility into stalled deals and overdue payments

**Solution B2: Payment/Collection Automation**
- Auto-calculate "Days Overdue" from Due for Collection date
- Tiered reminders: 7-day, 30-day, 60-day, 90-day
- Escalation: After 90 days, create task for manager
- Update risk score based on collection status
- Deploy: Workflow rules via API + possible Deluge function for calculation
- Impact: Direct attack on RM 10.77M outstanding

**Solution B3: Post-Sale Onboarding Workflow**
- Trigger: Deal stage changes to "Deal Won"
- Actions: Create task checklist (intro call, site survey confirmation, schedule installation, send welcome pack)
- Assign tasks to operations team based on deal type
- Deploy: Workflow rules + task templates via API
- Impact: Addresses pain point 7, improves customer experience

**Solution B4: SalesIQ → CRM Integration**
- Create CRM tasks when SalesIQ messages arrive
- Route to deal owner or service queue
- Deploy: Zoho Flow or Deluge function (SalesIQ API is limited)
- Impact: Addresses pain point 6

### For Root Cause C: Data Infrastructure

**Solution C1: Pricing Data Migration**
- Complete the 660-item manual categorization (team effort)
- Import pricing master data into Zoho Inventory
- Enable in-system quoting
- Deploy: Team does categorization → agent deploys via Inventory API
- Impact: Eliminates slow quoting (pain point 1), enables price management (pain point 2)
- Dependency: Requires team to complete the manual review first

**Solution C2: Composite/BOM Validation**
- Clean up 101 orphan composite mappings
- Build Deluge validation function on quote save
- Ensure quote line items map to valid BOM entries
- Deploy: Inventory API cleanup + CRM Deluge function
- Impact: Addresses pain point 4
- Dependency: Requires pricing/inventory data to be clean first

---

## Ranking — What to Build Next

Ranked by: immediate impact × feasibility ÷ dependencies

### Tier 1: Quick Wins (Next Session)

**#1 — Notification Workflow Rules (Solution B1)**
- WHY FIRST: Zero dependencies, deployable via API in one session, immediate value
- Idle deal alerts rescue the RM 20.5M at-risk pipeline
- Collection reminders attack the RM 10.77M outstanding
- Stage-stuck alerts prevent future PD-000127 situations (347-day stalls)
- Risk: Near zero — these ADD alerts without changing any existing process
- Effort: Medium (define rules, test, deploy via WF-ZOHO-DEPLOY)

### Tier 2: Foundation (Next 1-2 Sessions, Needs Chok's Input)

**#2 — Blueprint Design per Layout (Solution A1)**
- WHY SECOND: This is THE foundational fix, but needs Chok to define stage flows
- Each layout (Direct, Project, Trading, Troubleshoot) gets its own valid transitions
- Mandatory fields at each gate prevent information loss
- Must be created in UI first, then refined via API
- Risk: Medium — affects every future deal, needs careful testing
- Effort: High (design + UI creation + testing)
- PREP NEEDED: Chok maps out "what stages does a Direct deal go through?" for each layout

**#3 — Payment/Collection Automation (Solution B2)**
- WHY THIRD: Direct financial impact (RM 10.77M), builds on the notification rules from #1
- Can be deployed independently of blueprints
- Risk: Low — adds automation without changing process
- Effort: Medium

### Tier 3: Data Foundation (Parallel Track, Team-Dependent)

**#4 — Pricing Data Migration (Solution C1)**
- WHY HERE: Highest business impact (enables in-system quoting, fixes win rate issue)
- But blocked by 660 items needing manual team categorization
- This is a PARALLEL track — team does the categorization while we build #1-3
- Risk: Low (data migration, reversible)
- Effort: Team effort (categorization) + agent effort (import)

### Tier 4: Build on Foundation (After Tier 2 Deployed)

**#5 — Customer Onboarding Workflow (Solution B3)**
- Best built after blueprints exist (triggered by "Deal Won" transition in blueprint)
- Effort: Medium

**#6 — Composite/BOM Validation (Solution C2)**
- Depends on pricing data being clean (Tier 3)
- Depends on process being defined (Tier 2)
- Effort: High (Deluge development + testing)

**#7 — SalesIQ Integration (Solution B4)**
- Separate system, limited API, lowest pipeline impact
- Nice to have, not urgent
- Effort: Medium

---

## What NOT to Build

- **Linear pipeline validation rules** — The 29 stages aren't linear. Don't try to force linearity. Use blueprints per layout instead.
- **Complex lead scoring** — The bigger problem is losing deals you already have (RM 20.5M at risk), not finding better leads. Fix retention before acquisition.
- **Fancy dashboards** — Dashboards on top of broken processes just visualize the mess. Fix the process first.

---

## Prep for Next Session

For Chok to think about before we build:

1. **For each layout (Direct, Project, Trading, Troubleshoot):** What is the actual stage flow? Which stages does each type go through, and in what order? Which transitions are allowed?

2. **For mandatory fields:** At each stage transition, what MUST be filled in? (e.g., "Before moving from Specifying to Value Proposition, system size and roof type must be set")

3. **For collection reminders:** Who should get notified? Just the deal owner? Owner + manager? What escalation chain?

4. **For the 660 uncategorized items:** Can the team start this categorization work now? It's the bottleneck for in-system quoting.

---

## Summary

Your CRM is a well-built data warehouse running as a glorified spreadsheet. The data model is solid — the T&C master data hub, the 4 layouts, the comprehensive field set — these are good architectural decisions. What's missing is the process layer that turns data capture into business enforcement.

Three root causes (no process enforcement, no automation, data infrastructure gaps) produce all seven pain points. The fix sequence is: quick-win notifications first (immediate value, zero risk), then blueprints per layout (foundational, needs your input), then payment automation and pricing migration (financial impact, parallel track).
