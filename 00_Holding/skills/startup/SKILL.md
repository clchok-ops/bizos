# Startup

Resume context for the session. Token-efficient by default.

## Commands

| Command | Loads | Use Case |
|---------|-------|----------|
| `startup` | _CONTEXT.md only (~60 lines) | Quick check-in, planning |
| `startup [entity]` | _CONTEXT + entity/_ENTITY.md | Deep work on one entity |
| `startup build` | _CONTEXT + GLOBAL_STANDARDS | Technical/coding work |
| `startup crm` | _CONTEXT + CRM mode note | Pipeline/deal work |
| `startup full` | Everything | Rare, cross-system work |

**Entities:** `solartech`, `hippos`, `kinme`, `wci`, `trading`

**Brains:** `startup trading` loads trading/_CONTEXT.md instead of bizos

## Checklist

### 1. Mount ClaudeHub (if needed)

```
~/Library/Mobile Documents/com~apple~CloudDocs/ClaudeHub
```

### 2. Detect Command

Parse user input:
- No args → lite (context only)
- Entity name → context + that entity
- `build` → context + GLOBAL_STANDARDS.md
- `crm` → context + CRM mode reminder
- `full` → context + all entities + standards
- `trading` → switch to trading brain

### 3. Read Files

**Lite (default):**
```
bizos/_CONTEXT.md
```

**Entity focus (e.g., `startup solartech`):**
```
bizos/_CONTEXT.md
bizos/02_Solartech/_ENTITY.md
```

**Build mode:**
```
bizos/_CONTEXT.md
cto-brain/GLOBAL_STANDARDS.md
```

**CRM mode:**
```
bizos/_CONTEXT.md
+ remind: Zoho list_open_deals broken, use get_deal_by_name or exports
```

**Full mode:**
```
bizos/_CONTEXT.md
bizos/*/_ENTITY.md (all 5)
cto-brain/GLOBAL_STANDARDS.md
```

**Trading brain:**
```
trading/_CONTEXT.md
```

### 4. Check _INBOX (BizOS only)

```bash
ls -la bizos/_INBOX/
ls -la bizos/_INBOX/zoho/
```

Report new files with dates. Skip if empty.

### 5. Report

Keep it tight:

```
## 🚀 [Brain] — [Mode]

**Resuming from [date].**

### Flags ([X] active)
[table of flags]

### Focus
[next session priority]

### _INBOX
[new files or "Empty"]

---
Ready. What are we working on?
```

**Don't include:**
- Brain loaded checklist (obvious)
- Mini-kaizen scan (noise)
- Mode descriptions (user knows)

### 6. Mode Switching

User can say `mode build`, `mode lite`, `mode crm` mid-session.

When switching:
- `mode build` → Read GLOBAL_STANDARDS.md if not already loaded
- `mode lite` → Just acknowledge
- `mode crm` → Remind about Zoho MCP limitation

## File Locations

```
ClaudeHub/
├── bizos/
│   ├── _CONTEXT.md          ← Slim core (flags, focus, status)
│   ├── _archive/            ← Decisions, learnings, systems (reference)
│   ├── _INBOX/              ← Drop files for processing
│   ├── 01_Trading/_ENTITY.md
│   ├── 02_Solartech/_ENTITY.md
│   ├── 03_Hippos/_ENTITY.md
│   ├── 04_WCI/_ENTITY.md
│   └── 05_Kinme/_ENTITY.md
├── cto-brain/
│   └── GLOBAL_STANDARDS.md  ← Engineering rules (build mode)
└── trading/
    └── _CONTEXT.md          ← Trading brain
```

## Token Budget

| Mode | Est. Lines | Est. Tokens |
|------|------------|-------------|
| Lite | ~60 | ~500 |
| Entity | ~120 | ~1,000 |
| Build | ~420 | ~3,400 |
| Full | ~600 | ~4,800 |
| **Old startup** | **~930** | **~7,400** |

Target: 80% of sessions use Lite or Entity mode.
