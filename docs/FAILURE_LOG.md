# BizOS — Failure Log

*Post-mortems of business operations failures. Each failure generates a preventive rule.*

**Last Updated:** 2026-02-07
**Total Failures Logged:** 1

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

### [F-BIZ-001] Hallucinated Zoho API Endpoints in Skill Reference File
**Date:** 2026-02-11
**Severity:** 🟡 Important
**Layer:** System
**Entity:** Solartech

**What Broke:**
Built the zoho-infra skill v1 with a reference file (ZOHO_API_PATTERNS.md) that included a fabricated API endpoint (`POST /crm/v8/settings/functions`) for creating Deluge custom functions — this endpoint doesn't exist. Also used wrong paths (`/settings/workflow_rules` instead of verified `/settings/automation/workflow_rules`, `/settings/alerts` instead of `/settings/automation/email_notifications`).

**Root Cause:**
Generated the reference file from general LLM knowledge rather than grounding it in the verified deployment matrix from the previous session (cowork-20260211-024957-e672). That session had already confirmed exactly which Zoho operations are API-deployable vs UI-only, with correct endpoint paths — but this verified context wasn't carried forward into artifact generation.

**Why We Didn't Catch It:**
No verification step between "generate reference file" and "package as skill." The skill was packaged and presented before cross-referencing endpoints against verified facts from the prior session. Chok caught it by asking "are we still aligned" and quoting the deployment matrix.

**Preventive Rule Added:**
[R-BIZ-SYS-002] in BIZOS_RULES.md

**Lessons:**
- When a previous session has verified API capabilities (tested endpoints, confirmed what works/doesn't), those verified facts are the source of truth — never regenerate from scratch
- Reference files in skills are particularly dangerous to hallucinate because they get loaded into context and trusted as authoritative
- This is the same error class as F-004 (claimed something works without verification) — but for API specifications rather than automation outcomes
- The user's alignment check ("just to confirm we are still aligned") was the safety net. Build this into the process: always re-read verified deployment matrices before generating API reference docs

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
| CRM/Zoho | 1 | New |
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
