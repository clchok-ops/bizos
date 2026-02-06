# PTL Framework (Player Traffic Lights)

**Applies to:** All entities (Solartech, Hippos, WCI)
**Related:** TTL (Team Traffic Lights) for entity-level bonus pool
**Last Updated:** 2026-02-06

---

## Overview

PTL is a 5-area performance system that gives at-a-glance visibility into individual (Player) performance. Combined with TTL (Team Traffic Lights), it drives bonus allocation.

**Flow:**
```
TTL (Entity KPIs) → Unlocks bonus pool (0% / 10% / 15% / 20%)
PTL (Individual)  → Distributes share from pool
```

---

## Hierarchy

```
Team (Company/Entity)
└── Divisions / Departments
    └── Pods / Cells
        └── Players
```

---

## Role-Based KPIs

**Principle:** Framework is universal. Distinction is in role and responsibility.

- All players use the same 5 areas with same weightings
- Key Results KPIs are role-specific (what "success" means differs by role)
- Grow, 121, Kaizen, Customer apply equally to all levels

**Structure per entity:**
```
bizos/[entity]/
├── _ENTITY.md           ← Org chart, TTL targets
├── TTL_KPIS.md          ← Entity-level performance targets
└── roles/
    └── [Role].md        ← Key Results KPIs for that role
```

**Example:** A Pod Lead's Key Results include team metrics; an Associate's are individual targets. Both are measured on the same 20-point scale.

---

## Scoring Model

### 5 Key Areas (100 points total)

| Area | Max Points | What It Measures |
|------|------------|------------------|
| Key Results | 20 | Achievement of assigned KPIs |
| Grow | 15 | Personal development progress |
| 121 | 15 | 1:1 meeting quality & follow-through |
| Kaizen | 25 | Continuous improvement contributions |
| Customer | 25 | Customer satisfaction metrics |

**Weighting:** Customer + Kaizen = 50 pts (culture emphasis)

---

## Scoring Rules

1. All points in **strict 5-point increments** (0, 5, 10, 15, 20, 25)
2. **<50% of max = Grey band** (under observation)
3. Each increment represents progress toward mastery

---

## Zone Thresholds

### 15-point areas (Grow, 121)

| Score | Zone | % of Max |
|-------|------|----------|
| 0 | Grey | 0% |
| 5 | Red | 33% |
| 10 | Yellow | 67% |
| 15 | Green | 100% |

### 20-point areas (Key Results)

| Score | Zone | % of Max |
|-------|------|----------|
| 0 | Grey | 0% |
| 5 | Grey | 25% |
| 10 | Red | 50% |
| 15 | Yellow | 75% |
| 20 | Green | 100% |

### 25-point areas (Kaizen, Customer)

| Score | Zone | % of Max |
|-------|------|----------|
| 0 | Grey | 0% |
| 5 | Grey | 20% |
| 10 | Grey | 40% |
| 15 | Red | 60% |
| 20 | Yellow | 80% |
| 25 | Green | 100% |

---

## Traffic Light Meanings

| Color | Meaning | Action |
|-------|---------|--------|
| Green | Exceeding (81-100%) | Recognize, mentor others |
| Yellow | On track (66-80%) | Continue, minor adjustments |
| Red | Needs attention (51-65%) | Coach, identify blockers |
| Grey | Under observation (<50%) | New/transitioning, close support |

---

## TTL (Team Traffic Lights)

TTL operates at entity level and determines bonus pool funding:

| TTL Status | Pool Funded |
|------------|-------------|
| Grey | 0% |
| Red | 10% |
| Yellow | 15% |
| Green | 20% |

**TTL KPIs are entity-specific** - see:
- `bizos/02_Solartech/_ENTITY.md`
- `bizos/03_Hippos/_ENTITY.md`
- `bizos/04_WCI/_ENTITY.md`

---

## Implementation

**Technical docs:** `cto-brain/modules/grow-ptl/`
- ARCHITECTURE.md - System architecture
- 121_*.md - 121 meeting system
- DATA_ENTRY_MECHANISM.md - How data flows

**Data home:** SharePoint People Growth site

---

## Change Log

| Date | Change |
|------|--------|
| 2026-02-06 | Created canonical framework, aligned to 100-pt model with 5-pt increments |
| Previous | 85-pt model with variable thresholds (archived) |
