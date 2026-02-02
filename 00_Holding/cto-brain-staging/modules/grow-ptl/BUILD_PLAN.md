# PTL System Build Plan

**Status**: APPROVED - Ready to Build
**Date**: 2026-02-02
**Approach**: Hybrid (Keep site, isolate old from new)

---

## Decisions Made

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Rebuild vs Extend? | **Extend** | Preserve production People list, M365 integration |
| KPI Thresholds | **Option B: Role-specific** | Same KPI, different targets per role level |
| New site vs existing? | **Same site, isolate** | Archive old lists, create new alongside |
| Mass data entry | **Excel Sync** | Two-way sync for bulk updates |

---

## Site Structure

```
People Growth Site
│
├── 📁 MASTERS (Existing - Keep)
│   ├── People (87)
│   ├── Roles (31)
│   ├── Squad (5)
│   ├── KPIs (27)
│   └── Grow Programmes (11)
│
├── 📁 PTL_SYSTEM (New)
│   ├── PTL_Periods
│   ├── Role_KPI
│   ├── KR_Progress
│   ├── Grow_Progress
│   ├── 121_Log (extend)
│   └── PTL_Score
│
└── 📁 ARCHIVE_2026 (Move old here)
    └── 50+ individual employee lists
```

---

## List Schemas

### PTL_Periods

| Column | Type | Required | Notes |
|--------|------|----------|-------|
| Title | Text | Yes | e.g., "H1 2026" |
| Start_Date | Date | Yes | Period start |
| End_Date | Date | Yes | Period end |
| Is_Current | Yes/No | Yes | Only one active |
| Status | Choice | Yes | Draft/Active/Closed |

### Role_KPI (Junction Table with Thresholds)

| Column | Type | Required | Notes |
|--------|------|----------|-------|
| Title | Text | Yes | Auto: "{Role} - {KPI}" |
| Role | Lookup → Roles | Yes | Which role |
| KPI | Lookup → KPIs | Yes | Which metric |
| Grey_Min | Number | No | Lower bound for Grey |
| Grey_Max | Number | No | Upper bound for Grey |
| Red_Min | Number | No | Lower bound for Red |
| Red_Max | Number | No | Upper bound for Red |
| Yellow_Min | Number | No | Lower bound for Yellow |
| Yellow_Max | Number | No | Upper bound for Yellow |
| Green_Min | Number | No | Lower bound for Green |
| Green_Max | Number | No | Upper bound for Green |
| Threshold_Direction | Choice | Yes | Higher_Better / Lower_Better |
| Weight | Number | No | Default 1, for weighted average |
| Is_Active | Yes/No | Yes | Enable/disable without delete |

### KR_Progress (Actuals Tracking)

| Column | Type | Required | Notes |
|--------|------|----------|-------|
| Title | Text | Yes | Auto: "{Player} - {KPI} - {Period}" |
| Player | Lookup → People | Yes | Who |
| Role_KPI | Lookup → Role_KPI | Yes | Which metric+thresholds |
| Period | Lookup → PTL_Periods | Yes | Which period |
| Target_Value | Number | No | Can be prorated |
| Actual_Value | Number | Yes | Achieved value |
| Computed_TL | Choice | Yes | Grey/Red/Yellow/Green |
| Is_Prorated | Yes/No | No | New employee flag |
| Proration_Factor | Number | No | e.g., 0.67 for 4/6 months |
| Notes | Multi-line | No | Context |
| Evidence_URL | URL | No | Link to proof |
| Last_Updated | DateTime | Yes | Audit |
| Updated_By | Person | Yes | Audit |

### Grow_Progress

| Column | Type | Required | Notes |
|--------|------|----------|-------|
| Title | Text | Yes | Auto: "{Player} - {Programme}" |
| Player | Lookup → People | Yes | Who |
| Period | Lookup → PTL_Periods | Yes | Which period |
| Programme | Lookup → Grow Programmes | Yes | Which training |
| Status | Choice | Yes | Not Started/In Progress/Completed |
| Completion_Date | Date | No | When finished |
| Evidence_URL | URL | No | Certificate/proof |
| Points | Number | No | Credit earned |
| Verified | Yes/No | No | Manager confirmed |
| Verified_By | Person | No | Who verified |
| Notes | Multi-line | No | Comments |

### PTL_Score (Aggregation)

| Column | Type | Required | Notes |
|--------|------|----------|-------|
| Title | Text | Yes | Auto: "{Player} - {Period}" |
| Player | Lookup → People | Yes | Who |
| Period | Lookup → PTL_Periods | Yes | Which period |
| KR_Score | Number | No | Average KR points (0-3) |
| KR_TL | Choice | No | Grey/Red/Yellow/Green |
| Grow_Score | Number | No | Training completion % |
| Grow_TL | Choice | No | Grey/Red/Yellow/Green |
| 121_Score | Number | No | 121 completion rate |
| 121_TL | Choice | No | Grey/Red/Yellow/Green |
| Total_Score | Number | No | Weighted average |
| Overall_TL | Choice | No | Final traffic light |
| Last_Calculated | DateTime | No | When aggregated |

---

## KPIs List Extension

Add to existing KPIs list:

| New Column | Type | Notes |
|------------|------|-------|
| Unit | Text | %, mins, count, $, etc. |
| Threshold_Type | Choice | Percentage/Count/Time/Currency/Custom |
| Default_Direction | Choice | Higher_Better/Lower_Better |

---

## Traffic Light Scoring Logic

### Numeric Values
- Grey = 0
- Red = 1
- Yellow = 2
- Green = 3

### KR Traffic Light Calculation
```
For each KPI in Player's Role:
  1. Get actual from KR_Progress
  2. Get thresholds from Role_KPI
  3. Compare: actual vs thresholds
  4. Assign TL (0-3)

KR_Score = Average of all KPI TLs

Final KR_TL:
  0.00-0.50 → Grey (0-50%)
  0.51-1.30 → Red (51-65%)
  1.31-2.40 → Yellow (66-80%)
  2.41-3.00 → Green (81%+)
```

### Overall PTL Calculation
```
Total_Score = (KR_Score × 0.5) + (Grow_Score × 0.25) + (121_Score × 0.25)

Or configurable weights per organization.
```

---

## Build Sequence

```
Phase 1: Lists (Today)
├── Create PTL_Periods
├── Create Role_KPI
├── Create KR_Progress
├── Create Grow_Progress
├── Create PTL_Score
└── Extend KPIs with new columns

Phase 2: Data Setup
├── Define H1 2026 period
├── Populate Role_KPI thresholds
└── Set up Excel sync

Phase 3: Archive
├── Create ARCHIVE_2026 folder
├── Move 50+ individual lists
└── Update navigation

Phase 4: Automation (Future)
├── Power Automate: TL calculation
├── Power Automate: Period rollover
└── Power BI dashboard
```

---

## Excel Sync Setup

Each list will have:
1. "Export to Excel" for offline editing
2. "Edit in grid view" for quick browser edits
3. Sync back capability for bulk updates

---

*Build plan approved 2026-02-02*
