# G-WORK-001: Always Find Most Efficient Path Before Starting Work

> **Add to**: GLOBAL_STANDARDS.md (before Appendix section)
> **Severity**: 🔴 Critical
> **Added**: 2026-02-03
> **Origin**: PTL automation session (browser wrestling inefficiency)

---

## Rule Text (copy to GLOBAL_STANDARDS.md)

```markdown
### [G-WORK-001] Always Find Most Efficient Path Before Starting Work
**Severity:** 🔴 Critical
**Added:** 2026-02-03
**Origin:** PTL automation session (browser wrestling inefficiency)
**Applied:** 0 times

**Rule:** Before starting any task, evaluate the most efficient execution path:

| Task Type | Avoid | Prefer |
|-----------|-------|--------|
| Config UIs (Power Automate, Forms, Power BI) | Browser automation | Copy-paste guides, JSON imports |
| Complex wizards | Click-by-click | Templates, CLI tools, scripts |
| Repetitive setup | Manual each time | Reusable artifacts |

**Why:** Browser automation for React/SPA apps is slow and error-prone. Creating artifacts (guides, configs) is faster and reusable.

**Bad:** 20 min browser wrestling with Power Automate UI
**Good:** 2 min creating a copy-paste setup guide
```

---

## Also Update

Line 6 of GLOBAL_STANDARDS.md: `**Total Rules:** 20` (increment from 19)
