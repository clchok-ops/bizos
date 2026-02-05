---
name: startup
description: "Session startup checklist. Use when user says 'startup', 'startup bizos', 'startup solartech', 'startup brain', or 'startup trading'. Reads from local ClaudeHub folder."
---

# Startup

Resume context for the session. Token-efficient by default.

## Command Reference

```
startup [brain] [focus] [+build]
```

| Command | Loads | Tokens | Use Case |
|---------|-------|--------|----------|
| `startup` | bizos lite + critical rules | ~700 | Quick check-in |
| `startup solartech` | bizos + solartech + critical | ~1,200 | Entity work |
| `startup hippos` | bizos + hippos + critical | ~1,200 | Entity work |
| `startup kinme` | bizos + kinme + critical | ~1,200 | Entity work |
| `startup wci` | bizos + wci + critical | ~1,200 | Entity work |
| `startup bizos` | bizos full + critical | ~2,700 | Bizos infra work |
| `startup brain` | cto-brain + GLOBAL_STANDARDS | ~3,700 | Engineering rules |
| `startup trading` | trading + critical | ~700 | Trading work |
| `startup build` | bizos + GLOBAL_STANDARDS | ~3,700 | Technical work |

**Always loaded:** `cto-brain/CRITICAL_RULES.md` (~200 tokens)

**Modifiers:**
- `build` — adds full GLOBAL_STANDARDS.md
- `crm` — adds CRM mode reminder (Zoho MCP limitations)

---

## Parsing Logic

1. **Always load first:**
   - `cto-brain/CRITICAL_RULES.md` (every startup, every brain)

2. **Detect brain:**
   - `brain` → cto-brain
   - `trading` → trading brain
   - `bizos` → bizos full
   - anything else → bizos lite (default)

3. **Detect focus (bizos only):**
   - `solartech` → 02_Solartech/_ENTITY.md
   - `hippos` → 03_Hippos/_ENTITY.md
   - `kinme` → 05_Kinme/_ENTITY.md
   - `wci` → 04_WCI/_ENTITY.md

4. **Detect modifiers:**
   - `build` → add GLOBAL_STANDARDS.md
   - `crm` → add CRM reminder

5. **Special cases:**
   - `startup brain` implies build (engineering work needs full standards)

---

## File Loading

### Always (every startup)
```
cto-brain/CRITICAL_RULES.md
```

### Bizos Lite (default)
```
+ bizos/_CONTEXT.md
```

### Bizos + Entity
```
+ bizos/_CONTEXT.md
+ bizos/[folder]/_ENTITY.md
```

### Bizos Full
```
+ bizos/_CONTEXT.md
+ bizos/01_Trading/_ENTITY.md
+ bizos/02_Solartech/_ENTITY.md
+ bizos/03_Hippos/_ENTITY.md
+ bizos/04_WCI/_ENTITY.md
+ bizos/05_Kinme/_ENTITY.md
```

### CTO Brain
```
+ cto-brain/_CONTEXT.md
+ cto-brain/GLOBAL_STANDARDS.md
```

### Trading Brain
```
+ trading/_CONTEXT.md
```

### + Build Modifier
```
+ cto-brain/GLOBAL_STANDARDS.md
```

---

## Checklist

### 1. Mount ClaudeHub (REQUIRED)

**ALWAYS request mount first:**
```
mcp__cowork__request_cowork_directory
```

User selects: `~/Library/Mobile Documents/com~apple~CloudDocs/ClaudeHub`

The tool returns the VM path like `/sessions/xxx/mnt/ClaudeHub/` — **use this exact path** for all subsequent Read calls.

**STOP if mount fails or folder is empty.** Cannot proceed without ClaudeHub access.

### 2. Read files using the mounted path

Example for `startup solartech`:
```
Read: [VM_PATH]/cto-brain/CRITICAL_RULES.md
Read: [VM_PATH]/bizos/_CONTEXT.md
Read: [VM_PATH]/bizos/02_Solartech/_ENTITY.md
```

Use parallel Read calls. Always include CRITICAL_RULES.md.

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

## Improvement Loop

When failures happen mid-session:
```
learn "[what failed and why]"
```

This triggers the learn skill which:
1. Logs to FAILURE_LOG.md
2. Extracts rule → adds to CRITICAL_RULES.md
3. Rule active on next startup

---

## File Structure

```
ClaudeHub/
├── bizos/
│   ├── _CONTEXT.md          ← Slim (flags, focus, status)
│   ├── _archive/            ← Decisions, learnings (reference)
│   ├── _INBOX/              ← Drop files for processing
│   └── [entity]/_ENTITY.md  ← Entity-specific context
├── cto-brain/
│   ├── _CONTEXT.md          ← Engineering work tracker
│   ├── CRITICAL_RULES.md    ← 13 critical rules (ALWAYS loaded)
│   └── GLOBAL_STANDARDS.md  ← Full rules (build mode)
└── trading/
    └── _CONTEXT.md          ← Trading brain
```

---

## Token Budget

| Mode | Est. Tokens | vs Old |
|------|-------------|--------|
| Lite | ~700 | -91% |
| Entity | ~1,200 | -84% |
| Bizos full | ~2,700 | -64% |
| Brain | ~3,700 | -50% |
| Build | ~3,700 | -50% |
| **Old startup** | **~7,400** | baseline |

Critical rules add ~200 tokens but prevent repeat failures.
