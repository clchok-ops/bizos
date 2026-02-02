# Review Framework v2

> **Purpose**: Define what to monitor, when, for whom, and what action to take.

**Last Updated**: 2026-02-02
**Version**: 2.0 (rebuilt with feedback loops, escalation, rollups)

---

## Table of Contents
1. [Architecture](#architecture)
2. [Cadence & Rollups](#cadence--rollups)
3. [Entity Metrics](#entity-metrics)
4. [Escalation Protocol](#escalation-protocol)
5. [Resolution Tracking](#resolution-tracking)
6. [Brief Templates](#brief-templates)
7. [Implementation](#implementation)

---

## Architecture

### Folder Structure
```
BizOS/
├── _briefs/
│   │
│   ├── _RESOLUTION_LOG.md         ← Closed flags + outcomes
│   ├── _FLAG_TRACKER.md           ← Active flags with age
│   │
│   ├── daily/
│   │   └── 2026-02-03/
│   │       ├── _CTO_SUMMARY.md    ← 30-sec rollup
│   │       ├── _CROSS_ENTITY.md   ← Systemic patterns
│   │       │
│   │       ├── 02_Solartech/
│   │       │   ├── BRIEF.md       ← Entity health
│   │       │   └── people/
│   │       │       ├── olivia_hwa.md
│   │       │       ├── ted_wong.md
│   │       │       └── siti_noor.md
│   │       │
│   │       └── 03_Hippos/
│   │           ├── BRIEF.md
│   │           └── people/
│   │               ├── atie_hashim.md
│   │               └── fy_lim.md
│   │
│   ├── weekly/
│   │   └── 2026-W06/
│   │       ├── _CTO_SUMMARY.md    ← Week trends
│   │       ├── 02_Solartech.md
│   │       └── 03_Hippos.md
│   │
│   └── monthly/
│       └── 2026-02/
│           ├── _CTO_SUMMARY.md    ← Month performance
│           ├── 02_Solartech.md
│           └── 03_Hippos.md
```

### Information Flow
```
Daily Data (Zoho/Eats365)
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│ DAILY PROCESSING                                        │
│                                                         │
│  1. Ingest new data from _INBOX                        │
│  2. Calculate metrics vs benchmarks                     │
│  3. Check thresholds → generate flags                   │
│  4. Update _FLAG_TRACKER.md (age existing flags)       │
│  5. Generate daily briefs by entity & person           │
│  6. Generate CTO summary + cross-entity view           │
└─────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│ WEEKLY ROLLUP (Every Monday)                           │
│                                                         │
│  1. Aggregate daily metrics → weekly trends            │
│  2. Compare vs previous week                            │
│  3. Identify patterns across the week                   │
│  4. Flag stale issues (>7 days unresolved)             │
└─────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│ MONTHLY ROLLUP (1st of month)                          │
│                                                         │
│  1. Performance vs targets                              │
│  2. Resolution rate on flags                            │
│  3. Trend analysis (improving/declining)               │
│  4. Recommendations for next month                      │
└─────────────────────────────────────────────────────────┘
```

---

## Cadence & Rollups

### Daily (Fire-spotting)
**Question**: What needs attention TODAY?
**Output**: `daily/{date}/_CTO_SUMMARY.md`

| Component | Content |
|-----------|---------|
| 🔴 Escalate | Issues requiring immediate action |
| 🟡 Monitor | Issues to watch, not yet critical |
| 🟢 Wins | Positive events to acknowledge |
| Cross-Entity | Patterns spanning multiple entities |

### Weekly (Trend-spotting)
**Question**: Are we moving in the right direction?
**Output**: `weekly/{week}/_CTO_SUMMARY.md`

| Component | Content |
|-----------|---------|
| Trend Summary | Key metrics vs last week |
| Flag Resolution | What got resolved, what's stale |
| Team Performance | Week-over-week by person |
| Next Week Focus | What to prioritize |

### Monthly (Performance Review)
**Question**: Did we hit our goals? Why or why not?
**Output**: `monthly/{month}/_CTO_SUMMARY.md`

| Component | Content |
|-----------|---------|
| Scorecard | Actuals vs targets |
| Win/Loss Analysis | What worked, what didn't |
| Flag Effectiveness | Were alerts useful or noise? |
| Recommendations | Changes for next month |

### Quarterly (Strategic Review)
**Question**: Should we change course?
**Output**: Manual review session, not auto-generated

| Topic | Review |
|-------|--------|
| Customer concentration | Risk assessment |
| Team capacity | Hiring/training needs |
| Process effectiveness | What to change |
| Goal setting | Next quarter targets |

---

## Entity Metrics

### 02_Solartech (B2B Distribution)

**Data Source**: Zoho CRM Deals Export (211 fields)

#### Daily Metrics
| Metric | Calculation | Benchmark | Alert If |
|--------|-------------|-----------|----------|
| High-risk deal movement | Risk score ≥51, stage changed | — | Any movement (review) |
| Newly stuck | Last Activity >7d, Amount >RM 50K, first time | — | Any new |
| Closing this week | Closing Date within 7 days | — | Value >RM 500K |
| New deals added | Created Time = today | 2/day | < 1/day for 3 days |

#### Weekly Metrics
| Metric | Calculation | Benchmark | Alert If |
|--------|-------------|-----------|----------|
| Pipeline movement | Total pipeline WoW change | ±5% | Movement < 2% |
| Win rate (rolling 4w) | Won / (Won + Lost) | 32% | < 25% |
| New pipeline value | Sum(Amount) created this week | RM 2M | < RM 1M |
| At-risk value change | Sum(risk ≥51) WoW | — | Increase > 10% |
| Owner performance | Win rate by owner | 32% | Any owner < 15% |

#### Monthly Metrics
| Metric | Calculation | Target | Alert If |
|--------|-------------|--------|----------|
| Revenue closed | Sum(Won deals) | Budget | < 80% of target |
| Avg deal size | Revenue / Deals won | RM 200K | < RM 150K |
| Sales cycle (won) | Avg(Sales Cycle Duration) | 90 days | > 120 days |
| Collection rate | Collected / Billed | 85% | < 75% |
| Lost deal reasons | Top 3 Reason For Loss | — | Any reason > 30% |

#### Quarterly Metrics
| Metric | Review | Risk If |
|--------|--------|---------|
| Customer concentration | Top 10 as % of pipeline | > 50% |
| Pipeline coverage | Pipeline / Quarterly target | < 3x |
| Large deal win rate | Win rate on >RM 500K | < 15% |
| Owner capacity | Pipeline per owner | > RM 30M (overloaded) |

---

### 03_Hippos (B2C Retail)

**Data Source**: Zoho CRM Enquiries, Zoho Inventory

#### Daily Metrics
| Metric | Calculation | Benchmark | Alert If |
|--------|-------------|-----------|----------|
| New enquiries | Count from daily report | 5/day | < 3 (excl. Sunday) |
| Response time | Created → First activity | 4 hours | > 8 hours |
| Troubleshooting ratio | Troubleshooting / Total | 30% | > 50% |
| Source mix | By Enquiry Source | — | Any major source = 0 |

#### Weekly Metrics
| Metric | Calculation | Benchmark | Alert If |
|--------|-------------|-----------|----------|
| Conversion rate | Won / Total enquiries | 25% | < 20% |
| Lead source ROI | Conversions by source | — | Spend with 0 conversion |
| Owner workload | Enquiries per owner | Even split | Imbalance > 3x |
| Repeat enquiries | Same customer returns | < 5% | > 10% |

#### Monthly Metrics
| Metric | Calculation | Target | Alert If |
|--------|-------------|--------|----------|
| Revenue | Sum(Won deals) | Budget | < 80% of target |
| Jobs completed | Count of completions | — | < last month |
| Avg job value | Revenue / Jobs | RM 2,000 | < RM 1,500 |
| Gross margin | (Revenue - COGS) / Revenue | 40% | < 35% |

#### Quarterly Metrics
| Metric | Review | Risk If |
|--------|--------|---------|
| Service mix | Revenue by service type | Single service > 70% |
| Geographic spread | Jobs by region | Single region > 80% |
| Seasonal pattern | MoM variance | Unpredicted swings |

---

## Escalation Protocol

### Flag Lifecycle
```
┌─────────────────────────────────────────────────────────────────┐
│ DAY 1: Flag Created                                             │
│ → Appears in person brief                                       │
│ → Action: Owner should address                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼ (no action)
┌─────────────────────────────────────────────────────────────────┐
│ DAY 4-7: Flag Aging                                             │
│ → Highlighted in entity brief                                   │
│ → Tagged as "AGING" in CTO summary                             │
│ → Action: Entity manager should intervene                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼ (no action)
┌─────────────────────────────────────────────────────────────────┐
│ DAY 8+: Flag Stale                                              │
│ → 🔴 STALE in CTO summary                                       │
│ → Listed in weekly rollup as unresolved                        │
│ → Action: CTO direct intervention required                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼ (resolved or closed)
┌─────────────────────────────────────────────────────────────────┐
│ RESOLUTION                                                      │
│ → Logged in _RESOLUTION_LOG.md                                 │
│ → Outcome recorded (Won/Lost/Closed/Other)                     │
│ → Days to resolve tracked                                       │
└─────────────────────────────────────────────────────────────────┘
```

### Escalation Matrix
| Flag Age | Visibility | Responsible | Action Required |
|----------|------------|-------------|-----------------|
| Day 1-3 | Person brief | Owner | Address or update status |
| Day 4-7 | Entity brief (highlighted) | Entity Manager | Follow up with owner |
| Day 8+ | CTO summary (🔴 STALE) | CTO | Direct intervention |

### Flag Severity
| Severity | Criteria | Max Age Before Escalate |
|----------|----------|-------------------------|
| 🔴 Critical | Value > RM 500K or systemic | 3 days |
| 🟡 Warning | Value > RM 100K or recurring | 7 days |
| 🟢 Watch | Below thresholds | 14 days |

---

## Resolution Tracking

### _FLAG_TRACKER.md (Active Flags)
```markdown
# Active Flags

| ID | Date | Entity | Person | Issue | Value | Age | Status |
|----|------|--------|--------|-------|-------|-----|--------|
| F-001 | Feb 1 | Solartech | Olivia | PD-000127 stuck 354d | RM 1.59M | 2d | 🟡 Aging |
| F-002 | Feb 2 | Hippos | - | Enquiries down 60% | - | 1d | 🟢 New |
| F-003 | Jan 28 | Solartech | Siti | PD-2341 no response | RM 890K | 6d | 🟡 Aging |
```

### _RESOLUTION_LOG.md (Closed Flags)
```markdown
# Resolution Log

## 2026-02

| ID | Opened | Closed | Entity | Issue | Resolution | Outcome | Days |
|----|--------|--------|--------|-------|------------|---------|------|
| F-000 | Jan 25 | Feb 1 | Solartech | PD-2298 stuck | Called customer | Won RM 420K | 7 |

## Summary Stats
- Avg days to resolve: 6.2
- Resolution rate: 78%
- Outcome breakdown: 45% Won, 30% Lost, 25% Closed
```

---

## Brief Templates

### CTO Summary Template
```markdown
# 🌅 Morning Brief - {DATE}

**Generated**: {TIMESTAMP}

---

## 🔴 Escalate ({COUNT})

| Entity | Issue | Owner | Value | Age | Action |
|--------|-------|-------|-------|-----|--------|
| {ENTITY} | {ISSUE} | {OWNER} | {VALUE} | {AGE}d | {ACTION} |

## 🟡 Monitor ({COUNT})

| Entity | Issue | Trend | Context |
|--------|-------|-------|---------|
| {ENTITY} | {ISSUE} | {↑↓→} | {CONTEXT} |

## 🟢 Wins

- {ENTITY}: {WIN_DESCRIPTION}

---

## Cross-Entity Patterns

| Pattern | Entities Affected | Total Value |
|---------|-------------------|-------------|
| {PATTERN} | {ENTITIES} | {VALUE} |

---

## Stale Flags (>7 days)

| ID | Entity | Issue | Days | Last Action |
|----|--------|-------|------|-------------|
| {ID} | {ENTITY} | {ISSUE} | {DAYS} | {LAST_ACTION} |
```

### Entity Brief Template
```markdown
# {ENTITY} Daily Brief - {DATE}

## Health Scorecard

| Metric | Today | Benchmark | Trend | Status |
|--------|-------|-----------|-------|--------|
| {METRIC} | {VALUE} | {BENCH} | {↑↓→} | {🟢🟡🔴} |

## Flags Requiring Action

### 🔴 Critical

**{DEAL_ID}** ({VALUE}) - {OWNER}
- **Status**: {STATUS_DESCRIPTION}
- **Days flagged**: {DAYS}
- **Last action**: {LAST_ACTION}
- **Recommended action**:
  1. {SPECIFIC_ACTION_1}
  2. {SPECIFIC_ACTION_2}
- **Escalate to**: {MANAGER} if no update by {DEADLINE}

### 🟡 Warning

...

## Team Performance

| Owner | Pipeline | Win Rate | vs Benchmark | Trend (12w) | Stuck Deals |
|-------|----------|----------|--------------|-------------|-------------|
| {OWNER} | {PIPELINE} | {RATE}% | {DIFF} | {↑↓→} | {COUNT} |

## Yesterday's Activity

- {ACTIVITY_1}
- {ACTIVITY_2}
```

### Person Brief Template
```markdown
# {PERSON_NAME} - {DATE}

## Your Scorecard

| Metric | You | Team Avg | Gap | Trend (12w) |
|--------|-----|----------|-----|-------------|
| Pipeline | {VALUE} | {AVG} | {GAP} | {↑↓→} |
| Win Rate | {VALUE}% | {AVG}% | {GAP}% | {↑↓→} |
| Avg Cycle | {VALUE}d | {AVG}d | {GAP}d | {↑↓→} |
| Stuck Deals | {VALUE} | {AVG} | {GAP} | {↑↓→} |

## Action Required Today

### 1. {DEAL_ID} ({VALUE})
- **Why flagged**: {REASON}
- **Days since last activity**: {DAYS}
- **Required action**: {SPECIFIC_ACTION}
- **Deadline**: {DATE}
- **If no response**: {FALLBACK_ACTION}

### 2. ...

## This Week's Closes

| Deal | Value | Expected Date | Confidence | Notes |
|------|-------|---------------|------------|-------|
| {DEAL} | {VALUE} | {DATE} | {HIGH/MED/LOW} | {NOTES} |

## Your Wins This Week

- {WIN_1}
```

### Weekly Rollup Template
```markdown
# Week {WEEK} Summary - {ENTITY}

**Period**: {START_DATE} to {END_DATE}

## Week at a Glance

| Metric | This Week | Last Week | Change | Target | Status |
|--------|-----------|-----------|--------|--------|--------|
| {METRIC} | {VALUE} | {PREV} | {CHANGE}% | {TARGET} | {🟢🟡🔴} |

## Flag Activity

| Status | Count |
|--------|-------|
| New flags raised | {COUNT} |
| Flags resolved | {COUNT} |
| Flags still open | {COUNT} |
| Stale (>7 days) | {COUNT} |

## Resolution Outcomes

| Outcome | Count | Value |
|---------|-------|-------|
| Won | {COUNT} | {VALUE} |
| Lost | {COUNT} | {VALUE} |
| Closed (no action) | {COUNT} | {VALUE} |

## Team Highlights

**Top performer**: {NAME} - {ACHIEVEMENT}
**Needs support**: {NAME} - {ISSUE}

## Focus for Next Week

1. {PRIORITY_1}
2. {PRIORITY_2}
```

---

## Implementation

### Phase 1: Foundation (This Week)
- [x] Define metrics and thresholds
- [x] Define escalation protocol
- [x] Create templates
- [ ] Create folder structure
- [ ] Build daily brief generation logic
- [ ] Generate first real brief

### Phase 2: Tracking (Next Week)
- [ ] Implement _FLAG_TRACKER.md
- [ ] Implement _RESOLUTION_LOG.md
- [ ] Add flag aging logic
- [ ] Test escalation flow

### Phase 3: Rollups (Week 3)
- [ ] Build weekly rollup logic
- [ ] Build monthly rollup logic
- [ ] Add trend calculations

### Phase 4: Refinement (Ongoing)
- [ ] Tune thresholds based on feedback
- [ ] Remove noisy alerts
- [ ] Add new metrics as needed

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2026-02-02 | 1.0 | Initial framework |
| 2026-02-02 | 2.0 | Added: escalation protocol, resolution tracking, rollups, cross-entity view, prescriptive actions, trend tracking |
