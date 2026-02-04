# Decision Log

Historical record of decisions made. Reference only — not loaded at startup.

---

## 2026-02

**[2026-02-04] Kaizen Architecture v1**
- **Decision**: Redesign BizOS from task-management to kaizen engine
- **Problem**: Previous architecture was "well-documented manual system masquerading as automated" — flags accumulated without action, rules existed without enforcement, learning was documented but not applied
- **Solution**: 6-layer architecture (Observation → Classification → Response → Review → Kaizen → Learning)
- **Docs**: `cto-brain/designs/KAIZEN_ARCHITECTURE_v1.md`

**[2026-02-04] Old Brain Folder Cleanup**
- **Decision**: Delete legacy brain folders from iCloud root
- **Deleted**: `~/iCloud/bizos/`, `~/iCloud/trading-brain/`, `~/iCloud/trading-brain-backup/`
- **Outcome**: All active work now in `~/iCloud/ClaudeHub/`

**[2026-02-03] ClaudeHub Architecture Migration**
- **Decision**: Consolidate all 3 brains into single ClaudeHub folder with unified auto-sync
- **Rationale**: Browser automation for GitHub fundamentally broken. Local file access = instant, reliable.
- **Components**: `~/iCloud/ClaudeHub/`, `~/Automation/scripts/sync_all.sh`, launchd job every 30s

**[2026-02-01] 360° Loop Architecture**
- **Decision**: Use email→iCloud routing instead of complex n8n/WorkDrive setup
- **Rationale**: Simpler = more reliable. Email routing already works.

---

## 2025-01

**[2025-01-31] Architecture Decision**
- **Decision**: Adopt sustainable BizOS with CONTEXT.md as persistent memory, n8n for automation
- **Rationale**: Static spreadsheets not sustainable; need system that learns
