# PTL System: First Principles Analysis

> Should we rebuild from scratch or extend existing infrastructure?

**Status**: Analysis Complete
**Date**: 2026-02-02
**Recommendation**: **EXTEND, DON'T REBUILD**

---

## Current State: What Exists

### Master Lists (KEEP)

| List | Items | Role | Health |
|------|-------|------|--------|
| **People** | 87 | Employee master | ✅ Healthy |
| **Roles** | 31 | Job classification master | ✅ Healthy |
| **Squad** | 5 | Organizational unit master | ✅ Healthy |
| **KPIs** | 27 | KPI definitions | ⚠️ Needs extension |
| **Grow Programmes** | 11 | Training programme master | ✅ Healthy |
| **121_Log** | 0 | 121 tracking (exists but empty) | ⚠️ Needs schema review |

### Current Relationships

```
People (87 employees)
├── Role (lookup) ────────────→ Roles (31)
│   │                              │
│   │                              ├── KPIs (multi-select) ──→ KPIs (27)
│   │                              │                              └── Team/Squad
│   │                              │                              └── KPI Targets (text only!)
│   │                              │
│   │                              ├── Grow Programme (multi-select) ──→ Grow Programmes (11)
│   │                              │
│   │                              └── Squad (lookup) ──→ Squad (5)
│   │
│   └── Reporting To (self-ref) ──→ Roles (org hierarchy)
│
├── Squad (lookup) ────────────→ Squad (5)
│
├── Company (choice) ──────────→ Entity (Solartech/Hippos/WCI)
│
├── Reporting Manager (Person) ─→ M365/Entra ID
│
└── Employment Status, MemberID, Mail Nickname, etc.
```

### The Fragmentation Problem

```
50+ Individual Employee Lists
├── Abdul Fiqri Azhar (0 items)
├── Abdul Halim Roslan (3 items)
├── Ahmad Mirza Ariff (0 items)
├── ... (47+ more)
└── Each = personal PTL tracking log
```

**Problem**: No unified view, no aggregation possible, maintenance nightmare.

---

## What's Missing for PTL

### Gap 1: KPI Threshold Structure

**Current**: KPIs list has only a text "KPI Targets" field
**Needed**: Per-KPI Grey/Red/Yellow/Green thresholds

The user requirement states:
> "each key result will need its own grey, red, yellow, green targets defined as some KPIs don't work well with %"

**Example**:
| KPI | Grey | Red | Yellow | Green |
|-----|------|-----|--------|-------|
| Junk Accuracy (%) | <50% | 50-65% | 66-80% | >80% |
| Case Action Time (Mins) | >30 | 20-30 | 10-19 | <10 |
| Case Stuck (Count) | >10 | 6-10 | 3-5 | <3 |

### Gap 2: Role-Specific KPI Targets

**Current**: KPIs are linked to Roles via multi-select
**Needed**: Junction table with per-role targets

Why? Same KPI may have different thresholds for different roles:
- Senior Engineer: Green if <5 bugs/month
- Junior Engineer: Green if <10 bugs/month

### Gap 3: Actuals Tracking (KR Progress)

**Current**: No structured place to record KPI actuals
**Needed**: KR_Progress list

| Player | KPI | Period | Actual | Computed_TL |
|--------|-----|--------|--------|-------------|
| Alice | Junk Accuracy | H1 2026 | 82% | 🟢 |
| Bob | Case Time | H1 2026 | 25 mins | 🔴 |

### Gap 4: PTL Periods

**Current**: No period definition
**Needed**: PTL_Periods list for 6-month windows

| Period | Start | End | Is_Current |
|--------|-------|-----|------------|
| H1 2026 | 2026-01-01 | 2026-06-30 | Yes |
| H2 2025 | 2025-07-01 | 2025-12-31 | No |

### Gap 5: Prorated Targets

**Current**: No mechanism
**Needed**: Start date-aware target calculation

For new employee starting March 1 in H1 period:
- Full period = 6 months, they have 4 months
- Target adjustment factor = 4/6 = 0.67
- Or: grace period with different thresholds

### Gap 6: Grow Progress Tracking

**Current**: Grow Plan (12), Completed Grow Plan (17), Enrollments (3) exist but fragmented
**Needed**: Unified Grow_Progress with period scoping

### Gap 7: 121 Progress Tracking

**Current**: 121_Log exists but empty (0 items)
**Needed**: Verify schema matches 121_FRAMEWORK.md, populate

### Gap 8: PTL Score Aggregation

**Current**: Individual employee lists (no aggregation)
**Needed**: PTL_Score view/list

| Player | Period | KR_TL | Grow_TL | 121_TL | Overall_TL |
|--------|--------|-------|---------|--------|------------|
| Alice | H1 2026 | 🟢 | 🟡 | 🟢 | 🟢 |
| Bob | H1 2026 | 🔴 | 🟢 | 🔴 | 🔴 |

---

## First Principles: Extend vs Rebuild

### Why NOT Rebuild from Scratch

1. **People list is production** - Used for M365 user provisioning
2. **Roles list is complete** - 31 roles with KPI linkages
3. **KPIs list has content** - 27 KPIs defined
4. **Relationships exist** - Lookups already configured
5. **User familiarity** - Team knows current structure
6. **Risk** - Rebuilding introduces data migration errors

### Why EXTEND is Better

1. **Preserve investment** - Months of data entry preserved
2. **Incremental adoption** - Roll out features gradually
3. **Lower risk** - No big-bang migration
4. **Faster delivery** - Build on existing foundation
5. **Compatibility** - M365 integrations continue working

---

## Recommended Architecture

### Phase 1: Foundation (Extend Existing)

#### 1A. Extend KPIs List

Add columns to existing KPIs list:

| New Column | Type | Purpose |
|------------|------|---------|
| Grey_Threshold | Text | Threshold definition |
| Red_Threshold | Text | Threshold definition |
| Yellow_Threshold | Text | Threshold definition |
| Green_Threshold | Text | Threshold definition |
| Threshold_Type | Choice | Numeric_Higher_Better / Numeric_Lower_Better / Percentage / Custom |
| Unit | Text | %, mins, count, etc. |

**OR** (if per-role thresholds needed):

#### 1B. Create Role_KPI Junction List (NEW)

| Column | Type | Purpose |
|--------|------|---------|
| Role | Lookup → Roles | Which role |
| KPI | Lookup → KPIs | Which KPI |
| Grey_Threshold | Number/Text | Role-specific threshold |
| Red_Threshold | Number/Text | Role-specific threshold |
| Yellow_Threshold | Number/Text | Role-specific threshold |
| Green_Threshold | Number/Text | Role-specific threshold |
| Weight | Number | If KPIs have different weights |

**Recommendation**: Start with 1A (extend KPIs), graduate to 1B if role-specific thresholds needed.

#### 1C. Create PTL_Periods List (NEW)

| Column | Type |
|--------|------|
| Period_Name | Text (e.g., "H1 2026") |
| Start_Date | Date |
| End_Date | Date |
| Is_Current | Yes/No |

### Phase 2: Progress Tracking

#### 2A. Create KR_Progress List (NEW)

| Column | Type | Purpose |
|--------|------|---------|
| Player | Lookup → People | Who |
| KPI | Lookup → KPIs | Which metric |
| Period | Lookup → PTL_Periods | When |
| Target_Value | Number | Expected (can be prorated) |
| Actual_Value | Number | Achieved |
| Prorated | Yes/No | New employee flag |
| Start_Date_In_Period | Date | For proration calc |
| Computed_TL | Choice | Grey/Red/Yellow/Green (calculated) |
| Notes | Multi-line | Context |
| Last_Updated | DateTime | Audit |

#### 2B. Create Grow_Progress List (NEW)

| Column | Type |
|--------|------|
| Player | Lookup → People |
| Period | Lookup → PTL_Periods |
| Programme | Lookup → Grow Programmes |
| Completion_Date | Date |
| Evidence | URL |
| Points | Number |
| Verified | Yes/No |
| Verified_By | Person |

#### 2C. Verify/Extend 121_Log (EXISTING)

Check if existing 121_Log matches 121_FRAMEWORK.md schema.
If not, extend columns as needed.

### Phase 3: Aggregation

#### 3A. Create PTL_Score List or View (NEW)

| Column | Type |
|--------|------|
| Player | Lookup → People |
| Period | Lookup → PTL_Periods |
| KR_Points | Calculated/Number |
| KR_TL | Choice |
| Grow_Points | Calculated/Number |
| Grow_TL | Choice |
| 121_Points | Calculated/Number |
| 121_TL | Choice |
| Total_Points | Calculated |
| Overall_TL | Calculated |

### Phase 4: Deprecation

1. Archive 50+ individual employee lists
2. Migrate any valuable data to new unified lists
3. Delete after verification period

---

## Traffic Light Calculation Logic

### KR Traffic Light (Per Player Per Period)

```
For each KPI assigned to Player's Role:
  1. Get Player's actual value from KR_Progress
  2. Get KPI thresholds (from KPIs or Role_KPI)
  3. Compare actual to thresholds
  4. Assign TL: Grey/Red/Yellow/Green

Average all KPI TLs (numerically):
  Grey = 0, Red = 1, Yellow = 2, Green = 3

Final KR_TL:
  0-0.5 = Grey (0-50%)
  0.51-1.3 = Red (51-65%)
  1.31-2.4 = Yellow (66-80%)
  2.41-3 = Green (81%+)
```

### Prorated Target Logic

```
If Player.Start_Date > Period.Start_Date:
  Months_In_Period = (Period.End_Date - Player.Start_Date) / 30
  Proration_Factor = Months_In_Period / 6

  For cumulative KPIs (e.g., total sales):
    Adjusted_Target = Base_Target × Proration_Factor

  For rate KPIs (e.g., accuracy %):
    No proration needed (rate is rate)
```

---

## Implementation Sequence

```
Week 1-2: Foundation
├── Extend KPIs list with threshold columns
├── Create PTL_Periods list
├── Define H1 2026 period
└── Populate threshold values for all 27 KPIs

Week 3-4: Progress Tracking
├── Create KR_Progress list
├── Create Grow_Progress list
├── Verify 121_Log schema
└── Build data entry forms (Microsoft Forms / Power Apps)

Week 5-6: Automation
├── Power Automate: Calculate Computed_TL on KR_Progress save
├── Power Automate: Period rollover notifications
└── Power Automate: Prorated target calculation

Week 7-8: Aggregation & Rollout
├── Create PTL_Score aggregation (list or Power BI)
├── Build supervisor dashboard view
├── Migrate data from individual lists
├── Train users
└── Archive/deprecate old individual lists
```

---

## Decision Summary

| Question | Answer |
|----------|--------|
| Rebuild from scratch? | **No** |
| Keep People list? | **Yes** (production, M365 integrated) |
| Keep Roles list? | **Yes** (31 roles, relationships intact) |
| Keep KPIs list? | **Yes, extend** (add threshold columns) |
| Keep Grow Programmes? | **Yes** (11 programmes defined) |
| Keep 121_Log? | **Yes, verify schema** |
| Create new lists? | **Yes** (PTL_Periods, KR_Progress, Grow_Progress, PTL_Score) |
| Deprecate individual lists? | **Yes** (after migration) |

---

## Next Steps

1. **Confirm threshold approach**: Simple (extend KPIs) or Complex (Role_KPI junction)?
2. **Define threshold values**: For all 27 KPIs, what are Grey/Red/Yellow/Green?
3. **Confirm proration rules**: Cumulative vs rate KPIs?
4. **Begin Phase 1**: Extend KPIs list, create PTL_Periods

---

*Analysis completed 2026-02-02*
