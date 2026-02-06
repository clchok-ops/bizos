# BizOS Structure

> Canonical map of what should exist. Validate at session start and end.

**Last Updated:** 2026-02-06

---

## Root Level

| File | Purpose | Required |
|------|---------|----------|
| `_CONTEXT.md` | Session memory - read at startup, update at end | ✓ |
| `STRUCTURE.md` | This file - canonical structure map | ✓ |
| `README.md` | Repo overview for humans | ✓ |

---

## Shared (00_Holding/)

| File | Purpose |
|------|---------|
| `BIZOS_GUIDE.md` | How bizos works |
| `PTL_FRAMEWORK.md` | Universal PTL scoring model |

---

## Entity Structure

Each entity folder (`[NN]_[Name]/`) should have:

### Required Files

| File | Purpose |
|------|---------|
| `_ENTITY.md` | **THE entry point** - status, org chart, open items, learnings |
| `TTL_KPIS.md` | Entity-level performance targets |
| `roles/` | Folder with role-specific Key Results KPIs |

### Optional Files

| File | Purpose |
|------|---------|
| `[domain]/` | Domain-specific subfolder (e.g., `pricing/`) |
| `COMPENSATION.md` | Compensation structure |
| `SALES_CHANNELS.md` | Sales channel definitions |

### Deprecated (move to _archive/)

| File | Replacement |
|------|-------------|
| `INDEX.md` | Merged into `_ENTITY.md` |
| `README.md` | Merged into `_ENTITY.md` |
| `*_SYSTEM.md` | Merged into `_ENTITY.md` |
| `*_ARCHITECTURE.md` | Move to `cto-brain/` if technical |

---

## Entities

| Folder | Name | Status |
|--------|------|--------|
| `01_Trading/` | Trading | Active |
| `02_Solartech/` | Solartech | Active |
| `03_Hippos/` | Hippos | Active |
| `04_WCI/` | WCI | Active |
| `05_Kinme/` | Kinme | Active |

---

## Special Folders

| Folder | Purpose |
|--------|---------|
| `_archive/` | Superseded/deprecated files |
| `_briefs/` | Daily brief outputs (if active) |
| `_INBOX/` | Processing queue |

---

## Validation Checklist

Run at session start and end:

```
For each entity in [01-05]:
  ✓ _ENTITY.md exists
  ✓ TTL_KPIS.md exists
  ✓ roles/ folder exists
  ✗ No INDEX.md (should be archived)
  ✗ No README.md in entity (should be archived)
  ✗ No *_SYSTEM.md (should be archived)
```

---

## Rules

- **G-DOC-005**: Before entity work, validate structure against this file. Resolve drift before proceeding.
- **Single entry point**: `_ENTITY.md` is THE source of truth per entity
- **No competing files**: Archive alternatives, don't maintain duplicates
