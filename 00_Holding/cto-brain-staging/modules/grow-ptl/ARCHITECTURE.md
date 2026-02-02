# GROW/PTL System Architecture

> Performance Traffic Light system for people growth across all entities

**Status**: In Build
**Last Updated**: 2026-02-01
**Data Home**: SharePoint People Growth (waterhippos.sharepoint.com/sites/PeopleGrowth)

---

## System Purpose

A multi-factor traffic light system that provides at-a-glance performance visibility:
- **Individual PTL**: Per-employee performance status
- **Team PTL**: Per-entity health (drives company bonus pool)

**Intent**: Drive consistent culture across all 5 entities through unified measurement.

---

## Scoring Model

### 5 Key Areas (85 total points)

| Area | Max Points | What It Measures |
|------|------------|------------------|
| Key Results | 15 | Achievement of assigned KPIs |
| Grow | 15 | Personal development progress |
| 121 | 15 | 1:1 meeting quality & follow-through |
| Kaizen | 20 | Continuous improvement contributions |
| Customer | 20 | Customer satisfaction metrics |

**Note**: Team was removed from individual PTL. Team performance is measured separately at entity level.

### Thresholds Per Area

| Area | Green (High) | Yellow (Alert) | Red (Failed) |
|------|--------------|----------------|--------------|
| Key Results | ≥12 | 8-11 | <8 |
| Grow | ≥12 | 8-11 | <8 |
| 121 | ≥12 | 8-11 | <8 |
| Kaizen | ≥16 | 11-15 | <11 |
| Customer | ≥16 | 11-15 | <11 |

### Overall PTL Status

| Total Score | Status | Meaning |
|-------------|--------|---------|
| ≥25 | Passed | On track |
| <25 | Failed | Needs intervention |

### Traffic Light Colors

| Color | Meaning |
|-------|---------|
| 🟢 Green | Passed / High performance |
| 🟡 Yellow | Alert / Needs attention |
| 🔴 Red | Failed / Requires action |
| ⚫ Grey | Under Observation (new/transitioning) |

---

## Data Structure

### Per-Employee Files
`Results Log_[Name]_[Month].xlsx`

| Sheet | Purpose |
|-------|---------|
| Scoreboard | Summary dashboard |
| PTL | Overall traffic light status |
| Grow | Personal development tracking |
| Key Results | KPI achievement |
| 121 | 1:1 meeting logs |
| Kaizen | Improvement initiatives |
| Customer | Customer feedback/scores |
| Team Play | (Archived - now at entity level) |
| PTL Guide | Scoring reference (has hidden rows/columns) |

### SharePoint Lists
- **Grow Plan**: Employee master data
- **Teammates KPIs**: Performance tracking

---

## Architecture Decisions

### Decided
1. **Same 5 areas across all entities** - drives consistent culture
2. **Same weights across entities** - unified measurement
3. **Team removed from individual PTL** - measured at entity level for bonus pool
4. **Data home = SharePoint** - PeopleGrowth site
5. **Update cadence = Continuous** - not batch/periodic

### Not Yet Decided
1. **CTO oversight model** - How does CTO view across entities?
2. **Data entry mechanism** - Who enters what, how?
3. **Automation level** - Manual vs auto-pull from systems?
4. **Alert routing** - Who gets notified when status changes?

---

## Gaps (To Build)

| Gap | Priority | Notes |
|-----|----------|-------|
| Data entry mechanism | HIGH | Critical: who enters what, how? |
| KPIs per role | HIGH | Need role-specific KPI definitions |
| Customer metrics source | MEDIUM | Where does this data come from? |
| CTO dashboard | MEDIUM | Cross-entity visibility |
| Automation hooks | LOW | Can wait until manual process stable |

---

## Data Flow (Target State)

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Zoho CRM      │    │  SharePoint     │    │   Manual        │
│   (Sales KPIs)  │    │  (Grow/121)     │    │   (Kaizen)      │
└────────┬────────┘    └────────┬────────┘    └────────┬────────┘
         │                      │                      │
         └──────────────────────┼──────────────────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │  Results Log Excel    │
                    │  (Per Employee)       │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │  PTL Calculation      │
                    │  (Formula-driven)     │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │  Traffic Light        │
                    │  Dashboard            │
                    └───────────────────────┘
```

---

## Next Steps

1. **Design data entry mechanism** - Most critical gap
2. **Define KPIs per role** - What does "Key Results" mean for each position?
3. **Build CTO dashboard** - Cross-entity visibility
4. **Pilot with one entity** - Validate before rollout

---

## Related Files

- `Results Log_Name_Month.xlsx` - Employee template (latest version)
- SharePoint: waterhippos.sharepoint.com/sites/PeopleGrowth

---

*Architecture mapped by Claude on 2026-02-01*
