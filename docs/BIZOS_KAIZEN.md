# BizOS — Kaizen Log

*Experiments to improve business operations across three layers.*

**Last Updated:** 2026-02-07

---

## Three Kaizen Layers

| Layer | What We Improve | Example |
|-------|----------------|---------|
| **System** | CRM setup, automation pipelines, data flows | "Migrate Solartech pipeline alerts from email to n8n" |
| **Process** | Review cadence, entity management, flag resolution | "Weekly entity review instead of ad-hoc flag checking" |
| **Model** | KPIs, PTL scoring, performance targets, comp models | "Adjust PTL weights for Hippos vs Solartech" |

---

## How to Log an Experiment

```
learn kaizen bizos: [experiment description]
```

Or manually add using the template below.

---

## Experiment Template

```markdown
### [K-BIZ-XXX] Experiment Title
**Date:** YYYY-MM-DD
**Layer:** System / Process / Model
**Entity:** Holding / Solartech / Hippos / WCI / Kinme / Cross-entity
**Status:** Proposed / Active / Completed / Dropped

**Hypothesis:**
If we [change], then [outcome] because [reasoning].

**Expected Result:**
[Measurable outcome]

**Duration:**
[How long to run the experiment]

**Actual Result:**
(filled after experiment completes)

**Learning:**
(filled after experiment completes)

**Decision:** Adopt / Iterate / Drop
```

---

## Active Experiments

### [K-BIZ-001] Zoho Infrastructure Agent — Cowork Skill for Solartech Zoho Platform Build-Out
**Date:** 2026-02-11
**Layer:** System
**Entity:** Solartech (first), then cross-entity
**Status:** Proposed

**Hypothesis:**
If we build a specialized Cowork skill (like the builder skill but for Zoho infrastructure) that reads Solartech business context + architecture audits + Zoho standards, and produces deployable artifacts (Deluge scripts, workflow rules, data migrations, API calls) + step-by-step guides (for UI-only config like Blueprints), then we can systematically resolve the 7 operational pain points in the quote-to-delivery pipeline faster than ad-hoc manual Zoho configuration.

**Expected Result:**
- Quoting time reduced (pricing in Zoho, no more spreadsheet calc)
- Quote-BOM alignment enforced (validation on quote save)
- Mandatory fields at stage transitions (prevent information loss at handoffs)
- SalesIQ response monitoring active
- Customer onboarding workflow triggered on deal close
- All changes tracked and logged via BUILD_LOG

**Duration:**
4 weeks: Week 1 — skill design + API access validation. Week 2-3 — pricing/quoting infrastructure. Week 4 — workplan handoff + validation gates.

**Risks Identified:**
1. Zoho API write access scope not yet verified (metadata endpoints for workflow rules, custom fields)
2. Data quality bottleneck — 660 items need manual category review by team (agent can't fix this)
3. LLM agnosticism — n8n intelligence layer should abstract LLM calls for provider flexibility
4. Zero workflows deployed since Feb 8 — risk of perpetual build mode without production deployment

**Actual Result:**
(pending)

**Learning:**
(pending)

**Decision:** (pending)

---

## Completed Experiments

(none yet)

---

## Dropped Experiments

(none yet)

---

## Experiment Candidates

*Ideas to test:*

- Process: Weekly entity flag review vs current ad-hoc approach — does structure improve resolution rate?
- Model: PTL weight calibration per entity — do Solartech and Hippos need different scoring weights?
- System: Automated flag aging alerts — does flagging overdue items improve resolution speed?
- Process: Role KPI targets as conversation starters in 1:1s — do specific numbers drive better performance conversations?

---

## Related Files

- `FAILURE_LOG.md` — post-mortems
- `BIZOS_RULES.md` — preventive rules
- `BIZOS_PATTERNS.md` — success patterns
- `cto-brain/kaizen/KAIZEN_LOG.md` — cross-system kaizen
- `_archive/decisions.md` — historical decisions (preserved)
