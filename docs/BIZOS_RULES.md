# BizOS — Preventive Rules

*Rules generated from business operations failures and near-misses. Prevents recurring mistakes.*

**Last Updated:** 2026-02-07
**Total Rules:** 0

---

## How Rules Are Created

```
Failure occurs → learn bizos: [what happened]
             → FAILURE_LOG.md (post-mortem)
             → BIZOS_RULES.md (this file — preventive rule)
```

---

## Rule Format

Rules are tagged by layer and category:

| Prefix | Layer | Example |
|--------|-------|---------|
| R-BIZ-SYS-XXX | System | CRM config, automation pipelines, data architecture |
| R-BIZ-PROC-XXX | Process | Review cadence, entity management, reporting |
| R-BIZ-MOD-XXX | Model | KPIs, PTL scoring, performance targets |

---

## System Rules (R-BIZ-SYS)

(none yet)

---

## Process Rules (R-BIZ-PROC)

(none yet)

---

## Model Rules (R-BIZ-MOD)

(none yet)

---

## Cross-References

Rules that apply across all repos live in `cto-brain/CRITICAL_RULES.md`. Key cross-system rules relevant to bizos:

- G-DOC-001: Check ARCHITECTURE_INDEX.md before creating new docs
- G-DOC-004: Audit existing files before creating new ones
- G-DOC-005: Validate bizos structure at session start/end per STRUCTURE.md
- G-VERIFY-001: Never claim something works until end-to-end verified

## Related Files

- `FAILURE_LOG.md` — post-mortems that generated these rules
- `BIZOS_PATTERNS.md` — success patterns (the positive counterpart)
- `BIZOS_KAIZEN.md` — experiments to improve
