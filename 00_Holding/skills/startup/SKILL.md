# Startup

Resume context for the session. Token-efficient by default.

## Command Reference

```
startup [brain] [focus] [+build]
```

| Command | Loads | Tokens | Use Case |
|---------|-------|--------|----------|
| `startup` | bizos lite | ~500 | Quick check-in |
| `startup solartech` | bizos + solartech | ~1,000 | Entity work |
| `startup hippos` | bizos + hippos | ~1,000 | Entity work |
| `startup kinme` | bizos + kinme | ~1,000 | Entity work |
| `startup wci` | bizos + wci | ~1,000 | Entity work |
| `startup bizos` | bizos full (all entities) | ~2,500 | Bizos infra work |
| `startup brain` | cto-brain + GLOBAL_STANDARDS | ~3,500 | Engineering rules |
| `startup trading` | trading brain | ~500 | Trading work |
| `startup build` | bizos + GLOBAL_STANDARDS | ~3,500 | Technical work |
| `startup [entity] build` | bizos + entity + GLOBAL_STANDARDS | ~4,000 | Technical + entity |
| `startup trading build` | trading + GLOBAL_STANDARDS | ~3,500 | Technical + trading |

**Modifiers:**
- `build` — adds GLOBAL_STANDARDS.md (works with any brain)
- `crm` — adds CRM mode reminder (Zoho MCP limitations)

---

## Parsing Logic

1. **Detect brain:**
   - `brain` → cto-brain
   - `trading` → trading brain
   - `bizos` → bizos full
   - anything else → bizos lite (default)

2. **Detect focus (bizos only):**
   - `solartech` → 02_Solartech/_ENTITY.md
   - `hippos` → 03_Hippos/_ENTITY.md
   - `kinme` → 05_Kinme/_ENTITY.md
   - `wci` → 04_WCI/_ENTITY.md

3. **Detect modifiers:**
   - `build` → add GLOBAL_STANDARDS.md
   - `crm` → add CRM reminder

4. **Special cases:**
   - `startup brain` implies build (engineering work needs standards)

---

## File Loading

### Bizos Lite (default)
```
bizos/_CONTEXT.md
```

### Bizos + Entity
```
bizos/_CONTEXT.md
bizos/[folder]/_ENTITY.md
```

### Bizos Full
```
bizos/_CONTEXT.md
bizos/01_Trading/_ENTITY.md
bizos/02_Solartech/_ENTITY.md
bizos/03_Hippos/_ENTITY.md
bizos/04_WCI/_ENTITY.md
bizos/05_Kinme/_ENTITY.md
```

### CTO Brain
```
cto-brain/_CONTEXT.md
cto-brain/GLOBAL_STANDARDS.md
```

### Trading Brain
```
trading/_CONTEXT.md
```

### + Build Modifier
Add to any of the above:
```
cto-brain/GLOBAL_STANDARDS.md
```

---

## Checklist

### 1. Mount ClaudeHub
```
~/Library/Mobile Documents/com~apple~CloudDocs/ClaudeHub
```

### 2. Parse command and read files
Use parallel `Read` calls for efficiency.

### 3. Check _INBOX (bizos only)
```bash
ls -la bizos/_INBOX/
ls -la bizos/_INBOX/zoho/
```

### 4. Report (keep tight)

```
## 🚀 [Brain] — [Mode]

**Resuming from [date].**

### Flags ([X] active)
[table]

### Focus
[next priority]

### _INBOX
[new files or skip if empty]

---
Ready. What's the focus?
```

---

## Mode Switching

Mid-session: `mode build`, `mode lite`, `mode crm`

- `mode build` → Read GLOBAL_STANDARDS if not loaded
- `mode lite` → Acknowledge
- `mode crm` → Remind: Zoho `list_open_deals` broken, use `get_deal_by_name`

---

## File Structure

```
ClaudeHub/
├── bizos/
│   ├── _CONTEXT.md          ← Slim (flags, focus, status)
│   ├── _archive/            ← Decisions, learnings (reference)
│   ├── _INBOX/              ← Drop files for processing
│   ├── 01_Trading/_ENTITY.md
│   ├── 02_Solartech/_ENTITY.md
│   ├── 03_Hippos/_ENTITY.md
│   ├── 04_WCI/_ENTITY.md
│   └── 05_Kinme/_ENTITY.md
├── cto-brain/
│   ├── _CONTEXT.md          ← Engineering work tracker
│   └── GLOBAL_STANDARDS.md  ← Rules (loaded with build)
└── trading/
    └── _CONTEXT.md          ← Trading brain
```

---

## Token Budget

| Mode | Est. Tokens | vs Old |
|------|-------------|--------|
| Lite | ~500 | -93% |
| Entity | ~1,000 | -86% |
| Bizos full | ~2,500 | -66% |
| Brain | ~3,500 | -53% |
| Build | ~3,500 | -53% |
| **Old startup** | **~7,400** | baseline |

Target: 80% of sessions use Lite or Entity mode.
