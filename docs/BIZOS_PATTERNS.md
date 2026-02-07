# BizOS — Success Patterns

*Approaches that work well in business operations. Replicate these.*

**Last Updated:** 2026-02-07
**Total Patterns:** 0

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

(none yet)

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
