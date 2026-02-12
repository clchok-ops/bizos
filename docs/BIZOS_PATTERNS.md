# BizOS — Success Patterns

*Approaches that work well in business operations. Replicate these.*

**Last Updated:** 2026-02-12
**Total Patterns:** 3

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
