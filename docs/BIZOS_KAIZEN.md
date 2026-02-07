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

(none yet)

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
