---
name: startup
description: "Session startup checklist. Use when user says 'startup', 'resume', 'start session', or at the beginning of any work session. Reads brain files from desktop folders (faster, more reliable). Falls back to Chrome only if folders unavailable."
---

# Startup

Resume context and check system health. **Desktop-first** (per G-WORK-001).

## Checklist

### 1. Mount Desktop Folders

Request both folders in sequence:

```
mcp__cowork__request_cowork_directory
```

**Expected mounts:**
| Folder | Host Path | VM Path |
|--------|-----------|---------|
| BizOS | `~/Library/Mobile Documents/com~apple~CloudDocs/BizOS` | `/sessions/*/mnt/BizOS` |
| cto-brain | `~/Library/Mobile Documents/com~apple~CloudDocs/cto-brain` | `/sessions/*/mnt/cto-brain` |

**If user cancels:** Ask them to select the folder manually, or fall back to Chrome tabs (Section 1b).

### 1b. Chrome Fallback (only if desktop unavailable)

Use `mcp__Claude_in_Chrome__tabs_context_mcp` to find GitHub tabs:

| File | GitHub URL Pattern |
|------|-------------------|
| _CONTEXT.md | `github.com/clchok-ops/bizos/blob/main/_CONTEXT.md` |
| ARCHITECTURE.md | `github.com/clchok-ops/cto-brain/blob/main/ARCHITECTURE.md` |
| GLOBAL_STANDARDS.md | `github.com/clchok-ops/cto-brain/blob/main/GLOBAL_STANDARDS.md` |

Read via `mcp__Claude_in_Chrome__get_page_text` if tabs found.

### 2. Read All Brain Files (Parallel)

Use the `Read` tool on all three files simultaneously:

```
Read: /sessions/*/mnt/BizOS/_CONTEXT.md
Read: /sessions/*/mnt/cto-brain/ARCHITECTURE.md
Read: /sessions/*/mnt/cto-brain/GLOBAL_STANDARDS.md
```

**Priority order:**
1. **_CONTEXT.md** — Entity states, flags, decisions, next session focus
2. **GLOBAL_STANDARDS.md** — Rules (critical ones marked 🔴)
3. **ARCHITECTURE.md** — System design, automation patterns

### 3. Check Git Status

Verify both repos are in sync:

```bash
cd /sessions/*/mnt/BizOS && git status
cd /sessions/*/mnt/cto-brain && git status
```

Flag if either is behind origin or has uncommitted changes.

### 4. Mini-Kaizen Scan

Check _CONTEXT.md for:
- Flags > 3 days old
- Stale timestamps > 7 days
- URGENT flags needing immediate attention
- Patterns appearing 3+ times without a standard

### 5. Report

```
## 🚀 Session Startup Complete

**Resuming from [date].**

### Open Flags ([X] active)
| Priority | Entity | Flag |
|----------|--------|------|
| 🔴 URGENT | ... | ... |
| 🟡 ACTIVE | ... | ... |

### Git Status
- BizOS: ✅ Up to date / ⚠️ [issue]
- cto-brain: ✅ Up to date / ⚠️ [issue]

### Brain Loaded
- ✅ _CONTEXT.md (Desktop)
- ✅ GLOBAL_STANDARDS.md (Desktop)
- ✅ ARCHITECTURE.md (Desktop)

### Current Priority
[from Next Session Focus in _CONTEXT.md]

### Mini-Kaizen Scan 🔍
[observations or "All clear"]
```

### 6. Ask How to Help

Offer options based on:
1. URGENT flags
2. Next Session Focus items
3. Kaizen observations
