# SharePoint Architecture for People Growth System

> Unified, multi-entity architecture for GROW/PTL performance tracking

**Status**: Proposed
**Last Updated**: 2026-02-02
**Entities**: Solartech, Hippos, WCI (50-150 employees)

---

## Current State Analysis

### People Growth Site
| List | Items | Status | Notes |
|------|-------|--------|-------|
| Grow Plan | 12 | Underutilised | Training tracking (not in use) |
| Commitment | 157 | Active | Goal commitments |
| 360-Degree Responses | 75 | Active | Feedback collection |
| KPIs | 27 | Active | Performance metrics |
| My Grow | 250 | Active | Individual growth tracking |
| Individual PTL Logs | 50+ | Fragmented | One list per employee (!!) |

**Key Problem**: 50+ individual employee lists create maintenance nightmare and no unified reporting.

### Talent & Ops Site
| Resource | Type | Status | Notes |
|----------|------|--------|-------|
| Employee Information.xlsx | Document | Stale (Apr 2020) | Not maintained |
| Job Applicants | List | Empty | Recruitment |
| Job Offer | List | 1 item | Recruitment |

**Key Finding**: No proper employee master list exists. The last employee data is 6 years old.

---

## Proposed Architecture

### Core Principle: Single Source of Truth

```
┌────────────────────────────────────────────────────────────────┐
│                    PLAYERS (Employee Master)                    │
│  ─────────────────────────────────────────────────────────────  │
│  Single list for ALL employees across ALL entities              │
│  • Entity field: Solartech | Hippos | WCI                       │
│  • Status: Active | On Leave | Exited                           │
│  • Links to: Supervisor, Department                             │
└────────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
    ┌──────────┐        ┌──────────┐        ┌──────────┐
    │ 121_Log  │        │ Grow_Log │        │  KR_Log  │
    │ 15 pts   │        │  15 pts  │        │  15 pts  │
    └──────────┘        └──────────┘        └──────────┘
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
                     ┌───────────────┐
                     │   PTL_Score   │
                     │  (Aggregated) │
                     │   45 points   │
                     └───────────────┘
```

---

## List Specifications

### 1. Players (Employee Master) - NEW

**Purpose**: Single source of truth for all employees across all entities.

| Column | Type | Notes |
|--------|------|-------|
| PlayerID | Auto Number | Primary key (e.g., P001) |
| Full_Name | Single line | Display name |
| Email | Single line | Work email (unique) |
| Entity | Choice | Solartech \| Hippos \| WCI |
| Department | Choice | Engineering \| Sales \| Operations \| etc. |
| Position | Single line | Job title |
| Supervisor | Person | Direct supervisor (lookup to M365) |
| Supervisor_ID | Lookup | Links to Players list (for self-referential) |
| Start_Date | Date | Employment start |
| Status | Choice | Active \| On Leave \| Exited |
| Exit_Date | Date | If exited |
| PTL_Period_Start | Date | Current 6-month period start |

**Migration**: Import from existing sources, validate with HR, establish as authoritative.

---

### 2. 121_Log - NEW (Schema from 121_FRAMEWORK.md)

**Purpose**: Track weekly peer engagement sessions.

| Column | Type | Notes |
|--------|------|-------|
| ID | Auto | Primary key |
| Meeting_Date | Date | When 121 occurred |
| Player_A | Lookup | → Players |
| Player_B | Lookup | → Players |
| A_Win_for_B | Multi-line | A's observation of B's win |
| A_Blocker_for_B | Multi-line | A's observation of B's blocker |
| A_Goal_Discussed | Single line | KR/Grow goal referenced |
| A_Commitment | Multi-line | Action A commits to help B |
| A_Submitted | DateTime | Timestamp |
| B_Validated_A | Yes/No | B confirms A's submission |
| B_Win_for_A | Multi-line | B's observation of A's win |
| B_Blocker_for_A | Multi-line | B's observation of A's blocker |
| B_Goal_Discussed | Single line | KR/Grow goal referenced |
| B_Commitment | Multi-line | Action B commits to help A |
| B_Submitted | DateTime | Timestamp |
| A_Validated_B | Yes/No | A confirms B's submission |
| A_Delivered | Yes/No | Week 2: B confirms A delivered |
| B_Delivered | Yes/No | Week 2: A confirms B delivered |
| Points_A | Number | 0 or 1 |
| Points_B | Number | 0 or 1 |
| Status | Choice | Draft \| Pending_B \| Pending_A_Validation \| Complete |

---

### 3. Grow_Log - REBUILD

**Purpose**: Track training/development completed (replaces fragmented Grow Plan + My Grow).

| Column | Type | Notes |
|--------|------|-------|
| ID | Auto | Primary key |
| Player | Lookup | → Players |
| Period | Lookup | → PTL_Periods (6-month window) |
| Activity_Type | Choice | Training \| Certification \| Book \| Course \| Workshop |
| Activity_Name | Single line | What was completed |
| Completion_Date | Date | When completed |
| Evidence_Link | URL | Link to certificate/proof |
| Points | Number | 1-3 based on activity weight |
| Verified | Yes/No | Supervisor verified |
| Verified_By | Person | Who verified |
| Verified_Date | DateTime | When verified |

---

### 4. KR_Log - NEW/REBUILD

**Purpose**: Track Key Results achievement (integrates with existing KPIs list).

| Column | Type | Notes |
|--------|------|-------|
| ID | Auto | Primary key |
| Player | Lookup | → Players |
| Period | Lookup | → PTL_Periods |
| KR_Title | Single line | Key Result statement |
| Target_Value | Number | Quantified goal |
| Actual_Value | Number | Achieved value |
| Achievement_Pct | Calculated | Actual/Target × 100 |
| Points | Calculated | Based on achievement brackets |
| Status | Choice | On Track \| At Risk \| Achieved \| Missed |
| Notes | Multi-line | Context/blockers |
| Last_Updated | DateTime | Auto |

---

### 5. PTL_Score - AGGREGATED VIEW

**Purpose**: Consolidated traffic light score per player per period.

| Column | Type | Notes |
|--------|------|-------|
| Player | Lookup | → Players |
| Period | Lookup | → PTL_Periods |
| KR_Points | Calculated | Sum from KR_Log |
| Grow_Points | Calculated | Sum from Grow_Log |
| 121_Points | Calculated | Sum from 121_Log |
| Total_Points | Calculated | Sum of above |
| Traffic_Light | Calculated | 🔴 <15 \| 🟡 15-29 \| 🟢 30-45 |

---

### 6. PTL_Periods - REFERENCE

**Purpose**: Define 6-month scoring periods.

| Column | Type | Notes |
|--------|------|-------|
| Period_Name | Single line | e.g., "H1 2026", "H2 2026" |
| Start_Date | Date | Period start |
| End_Date | Date | Period end |
| Is_Current | Yes/No | Active period flag |

---

## Migration Plan

### Phase 1: Foundation (Week 1-2)
1. Create **Players** list
2. Import employee data from:
   - Existing individual PTL Log filenames
   - Microsoft 365 directory
   - HR validation
3. Create **PTL_Periods** reference list
4. Set up Entity filter views

### Phase 2: 121 System (Week 3-4)
1. Create **121_Log** list with full schema
2. Build Microsoft Forms for 121 entry
3. Build Power Automate flows:
   - Sequential handoff
   - Supervisor notifications
   - Weekly delivery check
4. Create test period with pilot group

### Phase 3: Grow & KR (Week 5-6)
1. Create **Grow_Log** list
2. Migrate data from My Grow + Grow Plan
3. Create **KR_Log** list
4. Integrate with existing KPIs list

### Phase 4: Aggregation (Week 7-8)
1. Create **PTL_Score** calculated view
2. Build Power BI dashboard
3. Deprecate individual PTL Log files
4. Full rollout to all entities

---

## Views by Role

### Player View
- My 121s this period
- My Grow activities
- My KR progress
- My PTL Score

### Supervisor View
- Team PTL overview
- 121 logs for coaching reference
- Pending verifications
- At-risk players (🔴 or 🟡)

### Admin View
- All players by entity
- Cross-entity analytics
- Period management
- Data quality checks

---

## Anti-Fragmentation Rules

1. **No individual employee lists** - All data goes to shared logs
2. **Entity as filter, not separate lists** - Single list, filtered views
3. **Player lookup required** - All scoring lists link to Players master
4. **Period scoping** - All scores are period-bound for clean history

---

## Technical Notes

### SharePoint Site Structure
```
People Growth (Site)
├── Lists
│   ├── Players (new)
│   ├── PTL_Periods (new)
│   ├── 121_Log (new)
│   ├── Grow_Log (rebuilt)
│   ├── KR_Log (new/rebuilt)
│   └── PTL_Score (view/calculated)
├── Forms (Microsoft Forms integration)
│   └── 121 Feedback Form
└── Pages
    └── PTL Dashboard (Power BI embed)
```

### Lookup Relationships
```
Players ←─────┬───── 121_Log
              │
              ├───── Grow_Log
              │
              ├───── KR_Log
              │
              └───── PTL_Score

PTL_Periods ←─┬───── 121_Log
              │
              ├───── Grow_Log
              │
              ├───── KR_Log
              │
              └───── PTL_Score
```

---

## What Gets Deprecated

| Current Resource | Action | Timeline |
|-----------------|--------|----------|
| 50+ Individual PTL Logs | Archive, then delete | After Phase 4 |
| Grow Plan list | Migrate to Grow_Log | Phase 3 |
| My Grow list | Migrate to Grow_Log | Phase 3 |
| Employee Information.xlsx | Replace with Players list | Phase 1 |

---

## Success Metrics

| Metric | Current | Target |
|--------|---------|--------|
| Employee lists | 50+ | 1 (Players) |
| Data entry locations | Multiple | Unified (Forms) |
| Cross-entity visibility | None | Full |
| Reporting time | Manual hours | Real-time dashboard |
| Data quality | Fragmented | Single source of truth |

---

*Architecture proposed 2026-02-02*
