# BizOS — Success Patterns

*Approaches that work well in business operations. Replicate these.*

**Last Updated:** 2026-02-12
**Total Patterns:** 4

---

## How Patterns Are Created

```
Success observed → learn pattern bizos: [what worked]
               → BIZOS_PATTERNS.md (this file)
```

Patterns can also be graduated from candidates after validation.

---

## Pattern Format

```markdown
### [P-BIZ-XXX] Pattern Name
**Added:** YYYY-MM-DD
**Layer:** System / Process / Model
**Entity:** Holding / Solartech / Hippos / WCI / Kinme / Cross-entity

**The Pattern:**
[What to do]

**Why It Works:**
[Why this is effective]

**Evidence:**
[Data or observation]

**When to Use:**
[Situations where this applies]
```

---

## Logged Patterns

### [P-BIZ-001] Fix Infrastructure Before Building Monitors
**Added:** 2026-02-11
**Layer:** System
**Entity:** Solartech

**The Pattern:**
When operational pain points emerge (slow quoting, missed billing, customer dissatisfaction), investigate root cause before building monitoring bots. In Solartech's case, 7 pain points across the quote-to-delivery pipeline (slow quoting, stale prices, hot vs junk leads, quote-BOM disconnect, workplan missing details, missed SalesIQ msgs, no customer onboarding) traced back to Zoho configuration gaps and data quality issues — not missing alerts.

**Why It Works:**
Monitoring bots on top of broken infrastructure just give fancier alerts about the same mess. Fixing the source (pricing data, composite mappings, stage gating, mandatory fields) prevents failures rather than reporting them.

**Evidence:**
- 87% of SKUs have no pricing in Zoho → forces manual spreadsheet calc for every quote
- 101 orphan composite mappings → quote line items disconnect from ops BOM
- No mandatory fields at stage transitions → information lost at every handoff
- All 7 pain points trace to data/config gaps, not missing visibility

**When to Use:**
Any time operational breakdowns are identified across an entity. Always map the full process pipeline and identify whether the fix is infrastructure (config, data, process gates) vs monitoring (alerts, dashboards, reports). Infrastructure first, monitoring second.

---

### [P-BIZ-002] Zoho CRM API v8 Enables Programmatic Infrastructure Deployment
**Added:** 2026-02-11
**Layer:** System
**Entity:** Solartech

**The Pattern:**
Zoho CRM API v8 supports creating custom fields, workflow rules, email notifications, and deploying Deluge functions programmatically. Zoho Inventory API supports full CRUD on items, composites, and price lists. This means an agent can deploy Zoho infrastructure via API — not just generate guides for manual UI work.

**Why It Works:**
Reduces dependency on manual UI configuration. An agent can produce AND deploy Deluge scripts, workflow rules, data migrations, and validation functions. Only Blueprints require initial UI creation (API can modify existing ones only).

**Evidence:**
- CRM API v8: custom fields ✓, workflow rules ✓, email notifications ✓, Deluge functions ✓
- Inventory API: items ✓, composites ✓, price lists ✓
- Blueprints: UI-only for creation, API for modification
- SalesIQ: partial API (visitor tracking, chat config), bot creation UI-only
- Forms: data-focused API only, form creation UI-only

**When to Use:**
When scoping any Zoho automation project. Classify each piece of work as API-deployable vs UI-only. Design agent outputs accordingly — API artifacts for automatable work, step-by-step guides for UI-only work.

---

### [P-BIZ-003] End-Session Handoffs Must Include Setup Steps for Next Session
**Added:** 2026-02-12
**Layer:** Process
**Entity:** Cross-entity

**The Pattern:**
Every end-session handoff should include a "Setup for Next Session" section with concrete manual steps Chok needs to complete before the next session starts. These are things that require human hands — importing a flow to Power Automate, testing in a browser portal, creating test data in SharePoint, verifying a deployment in Zoho, etc. The section should be actionable (not vague), ordered by priority, and indicate what's blocking vs nice-to-have.

**Why It Works:**
Claude builds artifacts but can't always deploy them — many platforms require manual import, browser interaction, or portal access. Without an explicit list of manual steps, the next session wastes time re-discovering what's pending, re-reading the BUILD_LOG, or asking "where were we?" The setup steps bridge the gap between what Claude produced and what's ready for the next build cycle.

**Evidence:**
- PA01 flow built this session but needs manual import + SP connection mapping + test data creation before the next session can verify or iterate on it
- Previous sessions had similar gaps (WF03 needed credential re-linking, Deluge function needed manual paste)
- Setup steps take 5-15 min of Chok's time but save 10-20 min of next session's context-building

**When to Use:**
Every `end session` command. The end-session skill should always produce a "Setup for Next Session" section in the handoff file, listing what Chok needs to do manually before the next session picks up the thread.

---

### [P-BIZ-004] Full Architecture Scan Before Any Solution Design
**Added:** 2026-02-12
**Layer:** Process
**Entity:** Cross-entity (Solartech proven, applies to Hippo's Zoho + all platforms)

**The Pattern:**
Before proposing any changes to a live platform (validation rules, workflow rules, blueprints, field modifications, automation), run a comprehensive architecture scan that dumps every module, field, layout, relationship, picklist, and existing rule. Analyze the full picture BEFORE designing anything. Never assume you understand a CRM's architecture from documentation or partial exploration — scan the actual system.

Sequence:
1. **Build a reusable scanner** — API-based tool that dumps the entire platform config in one call (e.g., WF-ZOHO-DEPLOY v1.1 `scan` action: 11 modules × 4 endpoints + blueprints + workflow rules = 54 API calls, 161KB of data)
2. **Analyze comprehensively** — Map every module's fields (types, picklists, lookups), cross-module relationships, existing validation/workflow rules, layouts, and pipelines
3. **Document the architecture** — Produce a reference report covering module stats, relationship maps, business process insights, and picklist value sets
4. **Only then design** — Propose changes informed by the actual architecture, not assumptions

**Why It Works:**
The CRM scan revealed that 3 of 4 proposed validation rules were wrong. We assumed deals follow a single linear pipeline — the scan showed 29 stages serving fundamentally different purposes (sales stages, regulatory/compliance stages like CAS/NEM/ST&TNB, delivery stages, lifecycle stages like Idle/Reactivate/Retention) across 4 distinct layouts (Direct, Project, Trading, Troubleshoot). Stage-gate validation rules (which assume linearity) would have broken live deals on a production system.

The scan also revealed 0 workflow rules (team doing everything manually), T&C as a master data hub with 3-way relationships, and 176 custom fields in Deals alone — none of which was visible from partial API exploration.

**Evidence:**
- Pre-scan: 3 of 4 proposed validation rules INVALID — would have broken live CRM
- Post-scan: clear picture of 29 stages as parallel processes per layout, not a single pipeline
- Architecture report: 1,349 lines covering 11 modules, 560+ fields, 50+ lookup relationships
- Reusable scanner: WF-ZOHO-DEPLOY v1.1 `scan` action works for any Zoho CRM instance
- Time investment: ~45 min to build scanner + run + analyze. Time saved: avoided deploying 3 breaking changes to production

**When to Use:**
Every time before proposing changes to ANY live platform — Zoho CRM, Zoho Inventory, SharePoint, Power Automate, n8n, or any system with complex configuration. Build the scanner once per platform, reuse for every entity (Solartech today, Hippo's Zoho tomorrow). The scanner is an investment that pays dividends across every future engagement with that platform.

**Cross-reference:** cto-brain S-019 (cross-system version of this pattern)

---

## Pattern Candidates

*Migrated from `_archive/learnings.md` — need validation before graduating to full patterns:*

- **Historical data eliminates observation period** — can build models same day instead of waiting to observe. Used Solartech's 4,209 closed deals to build a risk model in <15 minutes.
- **Backtesting on closed deals validates model before going live** — Solartech risk model showed 92.8% accuracy on historical data before any live deployment.
- **Risk scoring with specific thresholds beats vague labels** — "Score below 45 = at risk" is actionable. "At risk" without a number is not.
- **Compressed timeline via historical data analysis** — Historical data analysis lets you skip the observation period entirely. Applies to any entity with CRM deal history.
- **Single entity entry point (_ENTITY.md)** — One file per entity as the source of truth eliminates competing INDEX.md / README.md / *_SYSTEM.md files (see F-012).

---

## Related Files

- `FAILURE_LOG.md` — failures (the negative counterpart)
- `BIZOS_RULES.md` — preventive rules
- `BIZOS_KAIZEN.md` — experiments to improve
- `cto-brain/SUCCESS_PATTERNS.md` — cross-system patterns
- `_archive/learnings.md` — original pre-structured learnings (preserved)
