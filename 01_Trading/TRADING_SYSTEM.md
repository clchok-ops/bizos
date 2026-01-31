# Trading System (IBKR)

> Building from neutral. Learn first, systematize second.

**Last Updated**: 2025-01-31
**Status**: Foundation phase

---

## Philosophy

We're not starting with strategies or rules. We're starting with:
1. **Observation** — What happens in markets?
2. **Recording** — What did I do and why?
3. **Reviewing** — What worked? What didn't?
4. **Systematizing** — What patterns emerge?

Only after sufficient data do we formalize rules.

---

## Trading Journal Structure

Every trade gets logged:

| Field | Purpose |
|-------|---------|
| Date/Time | When |
| Symbol | What |
| Direction | Long/Short |
| Size | How much |
| Entry Price | Where in |
| Exit Price | Where out |
| P&L | Result |
| R-Multiple | Risk-adjusted result |
| **Setup** | Why did I take this? |
| **Thesis** | What was I expecting? |
| **Actual** | What actually happened? |
| **Lesson** | What did I learn? |
| **Grade** | Was this a good trade regardless of outcome? |

The last 5 fields matter most. P&L is noise. Process is signal.

---

## Metrics We'll Track

### Performance Metrics
- Total P&L
- Win Rate (% of trades profitable)
- Average Win vs Average Loss
- Profit Factor (gross profit / gross loss)
- Maximum Drawdown
- Sharpe Ratio (if applicable)

### Process Metrics
- Trades per week/month
- % of trades following rules (once we have rules)
- Grade distribution (A/B/C/D trades)
- Lesson recurrence (are we repeating mistakes?)

---

## Review Cadence

| Frequency | Focus |
|-----------|-------|
| After each trade | Quick log (5 min) |
| Weekly | Pattern review, grade trades |
| Monthly | Metrics analysis, strategy refinement |
| Quarterly | System overhaul, major adjustments |

---

## Current Questions to Explore

- [ ] What markets/instruments am I drawn to and why?
- [ ] What time horizons suit my personality and lifestyle?
- [ ] What's my real risk tolerance (not theoretical)?
- [ ] What's my edge going to be? (No edge = no trade)
- [ ] How much time can I realistically dedicate?

---

## Rules (To Be Developed)

> Empty by design. Rules emerge from data, not theory.

### Entry Rules
- (None yet — observing first)

### Exit Rules
- (None yet)

### Position Sizing
- (None yet)

### Risk Management
- (None yet)

---

## Strategy Lab

> Hypotheses to test

| ID | Hypothesis | Status | Result |
|----|------------|--------|--------|
| — | None yet | — | — |

---

## n8n Automation (Future)

Once we have a system:
- Daily: Pull IBKR positions and P&L
- Weekly: Generate performance summary
- Alert: Drawdown exceeds threshold
- Alert: Position size exceeds limits

---

## Files in This Folder

- `TRADING_SYSTEM.md` — This file (methodology)
- `journal.xlsx` — Trade log (to be created)
- `performance.xlsx` — Metrics dashboard (to be created)
- `strategies/` — Strategy documentation (future)

---

*"The goal isn't to make money. It's to make good decisions. The money follows."*
