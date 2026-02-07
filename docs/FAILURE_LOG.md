# BizOS — Failure Log

*Post-mortems of business operations failures. Each failure generates a preventive rule.*

**Last Updated:** 2026-02-07
**Total Failures Logged:** 0

---

## How to Log a Failure

Mid-session, use the learn skill:

```
learn bizos: [what failed and why]
```

This will:
1. Create a post-mortem entry here (F-BIZ-XXX)
2. Extract a preventive rule → BIZOS_RULES.md
3. If cross-system, also routes to cto-brain

---

## Failure Template

```markdown
### [F-BIZ-XXX] Title
**Date:** YYYY-MM-DD
**Severity:** 🔴 Critical / 🟡 Important / 🟢 Near miss
**Layer:** System / Process / Model
**Entity:** Holding / Solartech / Hippos / WCI / Kinme / Cross-entity

**What Broke:**
[Description of the failure]

**Root Cause:**
[Root cause]

**Why We Didn't Catch It:**
[What was missing]

**Preventive Rule Added:**
[R-BIZ-XXX] in BIZOS_RULES.md

**Lessons:**
- [Additional learnings]
```

---

## Logged Failures

(none yet)

---

## Historical Note

Prior failures from early BizOS sessions (pre-2026-02-07) were logged to `cto-brain/FAILURE_LOG.md` as cross-system issues. Relevant entries:

- F-004: Claimed automation working without verification
- F-006: Vague documentation
- F-007: Silent sync failure
- F-009: Duplicate architecture docs
- F-010: Power Automate email field issue
- F-011: Proposed new files without auditing existing
- F-012: Structure drift across sessions
- F-013: Skill files in multiple locations

See also: `_archive/learnings.md` for pre-structured learnings.

---

## Failure Categories

| Category | Count | Trend |
|----------|-------|-------|
| CRM/Zoho | 0 | - |
| Entity Ops | 0 | - |
| Automation | 0 | - |
| PTL/Performance | 0 | - |
| Documentation | 0 | - |

---

## Related Files

- `BIZOS_RULES.md` — preventive rules generated from failures
- `BIZOS_PATTERNS.md` — success patterns (what works)
- `BIZOS_KAIZEN.md` — experiments to improve
- `cto-brain/FAILURE_LOG.md` — cross-system failures
