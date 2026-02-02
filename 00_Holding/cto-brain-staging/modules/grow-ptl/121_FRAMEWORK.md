# 121 Framework

> Peer-to-peer engagement system for PTL scoring

**Status**: Draft
**Last Updated**: 2026-02-01
**PTL Weight**: 15 points (6-month rolling)

---

## Purpose

Weekly peer meetings that build psychological safety, mutual understanding, and active support — driving team performance through genuine connection, not checkbox compliance.

**Inspired by**:
- Google's Project Aristotle (psychological safety as #1 team success factor)
- BNI's 121 system (focus on helping the OTHER person succeed)

---

## Core Principles

1. **Psychological Safety** — Safe to be vulnerable, share blockers, ask for help
2. **Equal Turn-Taking** — Both parties share equally, neither dominates
3. **Other-Focused** — Goal is to help your partner, not yourself
4. **Action-Oriented** — Every 121 ends with a concrete commitment
5. **Verified Impact** — Points only awarded when actions are delivered

---

## Who Pairs With Whom

- **Anyone in the organisation** — cross-entity encouraged
- **All players are peers** — no hierarchy in 121s
- **Rotation encouraged** — build breadth of relationships

---

## Meeting Structure (30 min weekly)

| Phase | Time | Focus |
|-------|------|-------|
| **Check-in** | 5 min | How are you? (personal + work) |
| **Partner A shares** | 10 min | Wins, blockers, goals |
| **Partner B shares** | 10 min | Wins, blockers, goals |
| **Commit** | 5 min | Each commits ONE action to help the other |

---

## Feedback Form

Both parties submit **independently** after meeting. Forms remain locked until both submit, then unlock for mutual viewing.

### Questions

```
1. What's one WIN your partner had this week?

2. What's one BLOCKER they're facing?

3. Which of your partner's KEY RESULTS or GROW goals did you discuss?

4. What's ONE action YOU commit to help them this week?

5. [Week 2+] Did your partner deliver on last week's commitment?
   [ ] Yes - they followed through
   [ ] No - it wasn't completed
   [ ] N/A - first 121 together
```

### Validation Rules

- All questions required (no blank/N/A except Q5 on first meeting)
- Minimum 20 characters for Q1-Q4 (prevents "good" / "none" answers)
- Q3 must reference actual Key Result or Grow goal

---

## Scoring

**1 point per qualified 121** (max 1 per week)

### Point Qualification Criteria

| # | Requirement | Validated By |
|---|-------------|--------------|
| 1 | Meeting completed | Both forms submitted |
| 2 | Quality responses | Character minimums met |
| 3 | Linked to performance | Q3 references KR/Grow goal |
| 4 | Action committed | Q4 answered |
| 5 | Action delivered | Partner confirms Yes in following week |

**Point awarded only after Step 5** — partner must confirm delivery.

### 6-Month Target

- 15 points = 15 qualified 121s over 26 weeks
- Allows ~11 weeks buffer for leave, travel, illness

### Thresholds

| Score | Status |
|-------|--------|
| 12-15 | 🟢 Green |
| 8-11 | 🟡 Amber |
| <8 | 🔴 Red |

---

## Supervisor Visibility

After each 121, both supervisors receive a copy of the completed log.

**Purpose**: Reference for growth coaching (not approval)

**Contains**:
- Date and participants
- Wins and blockers shared
- Goals discussed
- Action commitments
- Delivery confirmation (following week)

**Supervisor action**: None required. View-only for coaching context.

---

## Anti-Gaming Measures

| Risk | Mitigation |
|------|------------|
| Collusion ("I'll say X, you say Y") | Blind submission until both complete |
| Generic answers | Minimum character count |
| Trivial commitments | Partner validates actual delivery |
| Same partner always | Rotation encouraged, supervisor visibility |
| Inflated self-rating | No self-rating; partner + supervisor visibility |

**Key insight**: Gaming now requires your partner to lie AND your supervisor to ignore patterns. Social cost makes gaming harder than compliance.

---

## Flow Diagram (Sequential Handoff)

```
┌─────────────────── WEEK 1 ───────────────────┐
│                                              │
│  Partners meet (30 min)                      │
│         │                                    │
│         ▼                                    │
│  Player A submits form about B               │
│         │                                    │
│         ▼                                    │
│  Player B receives notification              │
│  → Validates A's submission                  │
│  → Submits own form about A                  │
│         │                                    │
│         ▼                                    │
│  Player A receives notification              │
│  → Validates B's submission                  │
│         │                                    │
│         ▼                                    │
│  Both validated → Supervisors receive log    │
│                                              │
└──────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────── WEEK 2 ───────────────────┐
│                                              │
│  Next 121 form includes Q5:                  │
│  "Did partner deliver on commitment?"        │
│         │                                    │
│         ▼                                    │
│  Both confirm Yes → Point awarded (Week 1)   │
│  Either confirms No → No point (Week 1)      │
│                                              │
└──────────────────────────────────────────────┘
```

---

## Edge Cases

| Scenario | Rule |
|----------|------|
| Partner absent/leaves | Pair with someone else; no penalty |
| Scheduling conflict | 2 missed weeks allowed per 6-month period |
| New joiner mid-period | Pro-rated target: (weeks remaining ÷ 26) × 15 |
| Dispute on delivery | Supervisor reviews log, makes call |
| First 121 with new partner | Q5 = N/A, point based on Q1-Q4 only |

---

## Tech Stack (Office 365)

| Component | Tool |
|-----------|------|
| Feedback form | Microsoft Forms |
| Sequential flow logic | Power Automate |
| 121 Log storage | SharePoint List |
| Supervisor notifications | Power Automate → Outlook |
| Meeting scheduling | Teams calendar |

---

## Implementation Spec

### SharePoint List Schema: `121_Log`

| Column | Type | Notes |
|--------|------|-------|
| ID | Auto | Primary key |
| Date | Date | Meeting date |
| Player_A | Person | First submitter |
| Player_B | Person | Second submitter |
| A_Win_for_B | Text (multi) | A's observation of B's win |
| A_Blocker_for_B | Text (multi) | A's observation of B's blocker |
| A_Goal_Discussed | Text | KR/Grow goal discussed |
| A_Commitment | Text (multi) | Action A commits to for B |
| A_Submitted | DateTime | Timestamp |
| B_Validated_A | Yes/No | B confirms A's submission accurate |
| B_Win_for_A | Text (multi) | B's observation of A's win |
| B_Blocker_for_A | Text (multi) | B's observation of A's blocker |
| B_Goal_Discussed | Text | KR/Grow goal discussed |
| B_Commitment | Text (multi) | Action B commits to for A |
| B_Submitted | DateTime | Timestamp |
| A_Validated_B | Yes/No | A confirms B's submission accurate |
| Supervisor_A | Person | A's supervisor (auto-lookup) |
| Supervisor_B | Person | B's supervisor (auto-lookup) |
| A_Delivered | Yes/No | Week 2: B confirms A delivered |
| B_Delivered | Yes/No | Week 2: A confirms B delivered |
| Points_A | Number | 0 or 1 |
| Points_B | Number | 0 or 1 |
| Status | Choice | Draft / Pending_B / Pending_A_Validation / Complete |

### Power Automate Flows

**Flow 1: On A Submission**
- Trigger: Form submitted
- Actions:
  1. Create SharePoint list item (Status = Pending_B)
  2. Email B: "Your 121 partner has submitted. Please validate and add your feedback."
  3. Include link to validation form

**Flow 2: On B Validation + Submission**
- Trigger: B's form submitted
- Actions:
  1. Update SharePoint item (Status = Pending_A_Validation)
  2. Email A: "Your partner has responded. Please validate their feedback."
  3. Include link to validation form

**Flow 3: On A Validation**
- Trigger: A validates
- Actions:
  1. Update SharePoint item (Status = Complete)
  2. Email Supervisor_A: 121 log summary
  3. Email Supervisor_B: 121 log summary

**Flow 4: Weekly Delivery Check**
- Trigger: Scheduled (Monday)
- Actions:
  1. Find 121s from previous week where Status = Complete
  2. Email both parties: "Did your partner deliver on their commitment?"
  3. Link to delivery confirmation form

**Flow 5: On Delivery Confirmation**
- Trigger: Delivery form submitted
- Actions:
  1. Update A_Delivered or B_Delivered
  2. If both = Yes, set Points_A = 1, Points_B = 1
  3. If either = No, set relevant Points = 0

---

## Implementation Phases

### Phase 1: Manual Pilot
- Paper/spreadsheet tracking
- Manual supervisor sharing
- Test with 1 team for 4 weeks

### Phase 2: Forms + Basic Automation
- Microsoft Forms live
- Power Automate for notifications
- SharePoint logging

### Phase 3: Full Automation
- Blind lock/unlock logic
- Auto-scoring
- Dashboard integration

---

## Success Metrics

| Metric | Target |
|--------|--------|
| 121 completion rate | >90% weekly |
| Action delivery rate | >80% |
| Cross-entity 121s | >20% of pairings |
| Supervisor review rate | Spot-check monthly |

---

## References

- [Google Project Aristotle](https://rework.withgoogle.com/guides/understanding-team-effectiveness)
- [BNI 121 Best Practices](https://www.bni.com)
- [Effective 1:1 Meetings - Asana](https://asana.com/resources/one-on-one-meeting)

---

*Framework designed 2026-02-01*
