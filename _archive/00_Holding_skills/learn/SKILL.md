---
name: learn
description: "Log a failure and extract a preventive rule. Use when something breaks: 'learn [what happened]'. Updates FAILURE_LOG.md and CRITICAL_RULES.md."
---

# Learn

Capture failures and turn them into preventive rules. Closes the improvement loop.

## Trigger

```
learn [description of what failed]
```

**Examples:**
- `learn browser automation failed on Power Automate — React SPA blocked input`
- `learn forgot to use python3 on mac, command not found`
- `learn API call failed silently, no error logged`

---

## Process

### 1. Get Next Failure ID

Read `cto-brain/FAILURE_LOG.md`, find highest F-XXX, increment.

### 2. Analyze the Failure

From the description, extract:
- **What broke** — the symptom
- **Root cause** — why it happened
- **Preventive rule** — how to avoid next time

### 3. Determine Severity

| Severity | Criteria | Destination |
|----------|----------|-------------|
| 🔴 Critical | Caused data loss, wasted >10 min, or likely to recur | CRITICAL_RULES.md |
| 🟡 Important | Caused delay, caught before damage | GLOBAL_STANDARDS.md only |
| 🟢 Near miss | Almost happened, no impact | GLOBAL_STANDARDS.md only |

### 4. Update Files

**Always update:**
```
cto-brain/FAILURE_LOG.md  — Full post-mortem entry
cto-brain/GLOBAL_STANDARDS.md — Detailed rule (if new)
```

**If critical, also update:**
```
cto-brain/CRITICAL_RULES.md — One-liner for always-loaded rules
```

### 5. Confirm to User

```
## ✅ Logged: [F-XXX] [Title]

**Rule added:** [G-XXX-XXX] [rule summary]
**Files updated:** FAILURE_LOG.md, CRITICAL_RULES.md

This rule will load on next startup.
```

---

## File Formats

### FAILURE_LOG.md Entry

```markdown
### [F-XXX] Title
**Date:** YYYY-MM-DD
**Severity:** Critical / Important / Near miss

**What Broke:**
[Description]

**Root Cause:**
[Why]

**Preventive Rule Added:**
[G-XXX-XXX] in CRITICAL_RULES.md / GLOBAL_STANDARDS.md
```

### CRITICAL_RULES.md Entry

Add one row to the table:
```markdown
| G-XXX-XXX | [One-line rule] | [Origin reference] |
```

### GLOBAL_STANDARDS.md Entry

```markdown
### [G-XXX-XXX] Rule Title
**Severity:** 🔴 Critical / 🟡 Important / 🟢 Best Practice
**Added:** YYYY-MM-DD
**Origin:** Failure (F-XXX)
**Applied:** 0 times

**Rule:** [Full explanation]
```

---

## Rule ID Assignment

Check existing rules in GLOBAL_STANDARDS.md, use next available ID in category:

| Prefix | Category |
|--------|----------|
| G-API- | API & Integration |
| G-INT- | Integration |
| G-ERR- | Error Handling |
| G-AUTO- | Automation |
| G-CODE- | Code Quality |
| G-EMAIL- | Email |
| G-FILE- | File Handling |
| G-DOC- | Documentation |
| G-BRAIN- | Brain & Process |
| G-ENV- | Environment |
| G-WORK- | Claude Working Methods |
| G-ARCH- | Architecture |

---

## Quick Mode

For fast logging without full post-mortem:

```
learn quick: [rule to add]
```

This skips FAILURE_LOG and just adds to CRITICAL_RULES.md directly.
