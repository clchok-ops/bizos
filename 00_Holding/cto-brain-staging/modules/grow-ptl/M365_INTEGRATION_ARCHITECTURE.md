# M365-Integrated People Growth Architecture

> Leveraging the full Microsoft 365 platform for GROW/PTL

**Status**: Proposed
**Last Updated**: 2026-02-02

---

## Current Asset: People List

The existing **People** list in People Growth site is already a robust employee master with M365 integration:

| Column | Type | M365 Integration |
|--------|------|------------------|
| MemberID | Text | Entity prefix (SSS/WHO) |
| Reporting Manager | Person | ✅ Links to Entra ID |
| Mail Nickname | Text | ✅ Used for M365 user provisioning |
| Email | Text | ✅ M365 email address |
| Company | Choice | Entity (Solartech/Hippos/WCI) |
| Squad | Lookup | Organizational unit |
| Role | Lookup | Job classification |
| Employment Status | Choice | Active/Probation/etc |
| Grow Checklist | URL | Existing GROW integration |

**Decision**: Use People list as-is. No new "Players" list needed.

---

## M365 Platform Possibilities

### 1. Azure AD / Entra ID Integration

**Current State**: People list creates M365 users via Mail Nickname
**Opportunity**: Pull user attributes FROM Entra ID instead of maintaining separately

| Attribute | Source | Benefit |
|-----------|--------|---------|
| Manager | Entra ID | Auto-sync from HR system |
| Department | Entra ID | Single source of truth |
| Job Title | Entra ID | No duplicate maintenance |
| Photo | Entra ID | Rich user experience |

**How**: Power Automate + Graph API connector
```
Trigger: When People list item created/modified
Action: Update Entra ID user profile
OR
Trigger: Scheduled (daily)
Action: Sync Entra ID → People list
```

### 2. Viva Suite Integration

#### Viva Goals (OKR Tracking)
**Replaces**: KR_Log list
**Native Features**:
- OKR hierarchy (Company → Team → Individual)
- Progress tracking with check-ins
- Alignment visualization
- Integration with Teams

**Consideration**: Requires Viva Goals license. If not available, use SharePoint KR_Log.

#### Viva Learning (Training Tracking)
**Replaces**: Grow_Log list
**Native Features**:
- Learning content aggregation
- Completion tracking
- Manager recommendations
- Integration with LinkedIn Learning

**Consideration**: Requires Viva Learning license. If not available, use SharePoint Grow_Log.

#### Viva Insights (Collaboration Analytics)
**Enhances**: 121 system
**Native Features**:
- Meeting habits analysis
- Collaboration patterns
- Focus time tracking

**Consideration**: Could validate 121 participation patterns.

### 3. Power Platform Integration

#### Power Automate Flows

| Flow | Trigger | Actions |
|------|---------|---------|
| **121 Sequential Handoff** | Form submission | Update 121_Log → Notify Player B → Set deadline |
| **121 Delivery Check** | Scheduled (weekly) | Check commitments → Send reminders |
| **PTL Score Calculator** | 121_Log/Grow_Log change | Aggregate scores → Update dashboard |
| **Traffic Light Alert** | PTL score < 15 | Notify supervisor + HR |
| **New Employee Onboarding** | People list item created | Create M365 user → Assign licenses → Add to Teams |

#### Power Apps

| App | Purpose | Users |
|-----|---------|-------|
| **121 Mobile App** | Quick 121 entry on the go | All employees |
| **PTL Dashboard** | View scores, history, trends | Employees + Supervisors |
| **Admin Console** | Manage periods, run reports | HR/Admin |

#### Power BI

| Report | Audience | Key Metrics |
|--------|----------|-------------|
| **PTL Overview** | Leadership | Traffic light distribution, trends |
| **Team Performance** | Supervisors | Team scores, individual details |
| **121 Engagement** | HR | Participation rates, completion rates |
| **Growth Analytics** | L&D | Training completion, skill gaps |

### 4. Microsoft Teams Integration

| Feature | Implementation |
|---------|---------------|
| **121 Reminders** | Adaptive Card via Power Automate |
| **PTL Dashboard Tab** | Embed Power BI in Teams channel |
| **Recognition Bot** | Post 121 wins to team channel |
| **Coaching Channel** | Private channel for supervisor+employee |

### 5. SharePoint Architecture (Refined)

Given M365 integration, simplified SharePoint structure:

```
People Growth (Site)
├── Lists
│   ├── People (existing - employee master) ✅
│   ├── Squad (existing - org units) ✅
│   ├── Role (existing - job classifications) ✅
│   ├── 121_Log (new/extend)
│   ├── Grow_Log (new - if no Viva Learning)
│   ├── KR_Log (new - if no Viva Goals)
│   └── PTL_Periods (new - scoring windows)
│
├── Power Apps
│   └── 121 Entry App
│
└── Power BI
    └── PTL Dashboard
```

---

## Recommended Architecture

### Option A: Full M365 (If Licensed)

```
┌─────────────────────────────────────────────────────────────────┐
│                        ENTRA ID                                  │
│              (Source of truth for users)                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PEOPLE LIST                                  │
│            (Extended attributes, MemberID)                       │
└─────────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
    ┌──────────┐        ┌──────────┐        ┌──────────┐
    │ 121_Log  │        │   Viva   │        │   Viva   │
    │(SharePt) │        │ Learning │        │  Goals   │
    │ 15 pts   │        │  15 pts  │        │  15 pts  │
    └──────────┘        └──────────┘        └──────────┘
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
                     ┌───────────────┐
                     │   Power BI    │
                     │  PTL Dashboard│
                     └───────────────┘
                              │
                              ▼
                     ┌───────────────┐
                     │ Microsoft     │
                     │    Teams      │
                     │ (Embedded)    │
                     └───────────────┘
```

### Option B: SharePoint-Centric (Current Licenses)

```
┌─────────────────────────────────────────────────────────────────┐
│                     PEOPLE LIST                                  │
│              (Employee master with M365 Person fields)           │
└─────────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
    ┌──────────┐        ┌──────────┐        ┌──────────┐
    │ 121_Log  │        │ Grow_Log │        │  KR_Log  │
    │ 15 pts   │        │  15 pts  │        │  15 pts  │
    └──────────┘        └──────────┘        └──────────┘
          │                   │                   │
          │        Power Automate Flows          │
          └───────────────────┼───────────────────┘
                              ▼
                     ┌───────────────┐
                     │   Power BI    │
                     │  PTL Dashboard│
                     │ (or SP View)  │
                     └───────────────┘
```

---

## Implementation Approach

### Phase 1: Foundation (Week 1-2)
1. **Audit existing People list** - verify data quality
2. **Create PTL_Periods list** - define scoring windows
3. **Extend 121_Log list** - add all required columns
4. **Set up Person field lookups** - link to People list

### Phase 2: 121 System (Week 3-4)
1. **Build Microsoft Form** for 121 entry
2. **Create Power Automate flows**:
   - Form → 121_Log
   - Sequential handoff notifications
   - Weekly delivery reminders
3. **Build 121 Power App** (optional mobile entry)

### Phase 3: Grow & KR (Week 5-6)
1. **Evaluate Viva licenses** - determine approach
2. **Build Grow_Log** (if no Viva Learning)
3. **Build KR_Log** (if no Viva Goals)
4. **Create data entry forms/apps**

### Phase 4: Dashboard & Rollout (Week 7-8)
1. **Build Power BI dashboard**
2. **Embed in Teams** (PTL channel)
3. **Create Adaptive Card notifications**
4. **User training & documentation**
5. **Pilot with one entity** → Full rollout

---

## Key Questions to Resolve

| Question | Impact |
|----------|--------|
| Do you have Viva Goals license? | Determines if we build KR_Log or use Viva |
| Do you have Viva Learning license? | Determines if we build Grow_Log or use Viva |
| Do you have Power BI Pro/Premium? | Determines dashboard embedding options |
| Is People list synced from external HR system? | Determines data flow direction |
| What's the relationship between Squad list and Entra ID groups? | Determines automation possibilities |

---

## Benefits of M365-Native Approach

| Benefit | Description |
|---------|-------------|
| **Single Sign-On** | No separate logins, seamless experience |
| **Person Fields** | Automatic profile cards, org chart |
| **Teams Integration** | Notifications where people work |
| **Mobile Ready** | Power Apps works on any device |
| **Graph API** | Programmatic access to all M365 data |
| **Security** | Inherits M365 permissions model |
| **Audit Trail** | Built-in versioning and compliance |

---

## Anti-Patterns to Avoid

| Don't | Do Instead |
|-------|------------|
| Create duplicate employee list | Use existing People list |
| Store manager info separately | Use Person field linking to Entra ID |
| Build custom auth | Leverage M365 SSO |
| Email notifications only | Use Teams Adaptive Cards |
| Manual score calculation | Power Automate calculated columns |
| Excel dashboards | Power BI with live connection |

---

*Architecture proposed 2026-02-02*
