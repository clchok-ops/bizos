---
name: startup
description: "Session startup checklist. Use when user says 'startup', 'startup bizos', 'startup solartech', 'startup brain', or 'startup trading'. Reads from local ClaudeHub folder."
---

# Startup

Resume context for the session.

## Commands

| Command | Loads |
|---------|-------|
| `startup` | CRITICAL_RULES + bizos/_CONTEXT.md |
| `startup solartech` | above + 02_Solartech/_ENTITY.md |
| `startup hippos` | above + 03_Hippos/_ENTITY.md |
| `startup kinme` | above + 05_Kinme/_ENTITY.md |
| `startup wci` | above + 04_WCI/_ENTITY.md |
| `startup bizos` | above + all _ENTITY.md files |
| `startup brain` | CRITICAL_RULES + cto-brain context + GLOBAL_STANDARDS |
| `startup trading` | CRITICAL_RULES + trading/_CONTEXT.md |
| `startup build` | adds GLOBAL_STANDARDS to any above |

---

## Steps

### Step 1: Request mount

Call this tool:
```
mcp__cowork__request_cowork_directory
```

User selects `ClaudeHub` folder. Tool returns VM path like:
```
/sessions/xxx/mnt/ClaudeHub
```

Save this path — use it for ALL file reads.

### Step 2: Read files (parallel)

For `startup solartech`, read these 3 files in parallel:
```
[VM_PATH]/cto-brain/CRITICAL_RULES.md
[VM_PATH]/bizos/_CONTEXT.md
[VM_PATH]/bizos/02_Solartech/_ENTITY.md
```

For `startup` (no args), read:
```
[VM_PATH]/cto-brain/CRITICAL_RULES.md
[VM_PATH]/bizos/_CONTEXT.md
```

For `startup brain`, read:
```
[VM_PATH]/cto-brain/CRITICAL_RULES.md
[VM_PATH]/cto-brain/_CONTEXT.md
[VM_PATH]/cto-brain/GLOBAL_STANDARDS.md
```

### Step 3: Check _INBOX

```bash
ls [VM_PATH]/bizos/_INBOX/zoho/
```

### Step 4: Report

```
## 🚀 [Brain] — [Mode]

**Resuming from [date].**

### Flags
[from _CONTEXT.md]

### Focus
[from _CONTEXT.md]

---
Ready.
```

---

## Entity Mapping

| Entity | Folder |
|--------|--------|
| solartech | 02_Solartech |
| hippos | 03_Hippos |
| kinme | 05_Kinme |
| wci | 04_WCI |

---

## Troubleshooting

If Read fails after mount:
1. User may have selected wrong folder
2. Ask user to confirm they selected `ClaudeHub` (not a subfolder)
