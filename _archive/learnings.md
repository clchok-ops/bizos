# Learnings & Patterns

What we've learned that applies across entities. Reference only — not loaded at startup.

---

## Process Learnings
- Historical data eliminates "observation period" — can build models same day
- Backtesting on closed deals validates model before going live
- 4,209 deals → actionable risk model in <15 minutes

## What Worked
- Compressed timeline: Historical data analysis vs waiting to observe
- Risk scoring with specific thresholds (not vague "at risk" labels)
- Backtest validation (92.8% accuracy) before recommending
- ClaudeHub consolidation: single mount → all brains → local read/write → auto-sync

## What Didn't Work
- Zoho MCP `get_deal_by_name` and `list_open_deals` returning API errors
- Zoho CRM new UI causes browser automation timeouts
- Complex n8n/WorkDrive architecture → over-engineering
- Browser automation for Power Automate/Forms → blocked by React SPA
- Browser automation for GitHub file edits → CodeMirror blocks input
- Multiple "No response requested" moments when user needed commands

## Cross-Entity Patterns
- (Pending Hippos/WCI analysis for comparison)
