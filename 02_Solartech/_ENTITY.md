# Solartech Operations

**Status:** 🟡 CRM enforcement scan complete, layout walkthrough queued | **Last:** 2026-02-14
**Type:** Parent company, B2B distribution (solar/boiler/water)
**Systems:** Zoho CRM (MCP connected), Zoho Inventory, SalesIQ

---

## Organization Structure

```
GROUP LEVEL (Shared Services)
├── CEO: Dad
├── COO: Chok
├── Purchasing Lead: Kwan
├── XP Lead: Yee Xiang
├── People: Chui Geok
└── Admin

SOLARTECH
├── Sales
│   ├── B2C Specialists
│   │   ├── Pods (new structure, building)
│   │   └── Senior Solo: Bryan, Ted
│   │
│   └── B2B Specialists
│       ├── BD Lead - Housing: Olivia
│       ├── BD Lead - C&I: Bay
│       ├── BD Solo: Shafiq
│       └── Project Engineer
│
└── Operations (Head: Kima)
    ├── Projects
    └── Logistics
        └── Warehouse
```

**Related:** `TTL_KPIS.md`, `SALES_CHANNELS.md`, `COMPENSATION.md`, `roles/`, `zoho/ZOHO_STANDARDS.md`

---

## Business Context

**Domain:** waterhippos.com
**Primary CRM Use:** Sales pipeline, customer management, service tracking

**Key Workflows:**
- Community Project: Drone inspection assessment reports → PDF via mail merge email (active)
- Lead Assignment: Route incoming leads to sales reps (rules TBD)
- Pipeline Risk: Automated deal health scoring (building)

**Business Rules:**
- Profit margin threshold: 15% (flag if below)
- Daily kWp targets tracking
- Sales performance dashboards

**Stakeholders:**

| Role | Needs | Primary System |
|------|-------|----------------|
| Sales Team | Lead management, deal tracking | Zoho CRM |
| Operations | Installation scheduling, reports | Zoho CRM + Analytics |
| Management | Dashboards, KPIs | Zoho Analytics |

**Technical Constraints:**
- Must work within Zoho ecosystem
- Email: Office 365 (waterhippos.com, SPF + DKIM configured)
- Limited budget for external tools (prefer Zoho-native)

**Terminology:**

| Term | Definition |
|------|------------|
| kWp | Kilowatt-peak — measure of solar panel output |

**Historical Issues Resolved (Jan 2025):**
- Mail merge module name mismatch
- Email authentication (SPF/DKIM) configuration
- PDF attachment size limits
- Zoho Analytics multi-column sorting workaround

---

## Key Metrics
- Total Pipeline: RM 207.9M (4,209 deals)
- Active Pipeline: RM 114.8M (216 large deals >RM 50K)
- Win Rate: 37.8% overall, **20.9% on large deals** ⚠️
- At-Risk Value: **RM 20.5M** (24 high + 62 medium risk)

## Risk Model (92.8% accuracy)

| Signal | Points |
|--------|--------|
| Probability < 25% | +40 |
| No activity > 90 days | +25 |
| Sales cycle > 180 days | +15 |
| Stage = Idle/Tender | +10 |
| Owner win rate < 10% | +10 |

Thresholds: 0-20 Low | 21-50 Medium | 51-100 High

## 🚨 Urgent Deals
1. **PD-000127** (RM 1.59M) - Olivia Hwa - 347 days stuck
2. **8 Tenders** (RM 4.1M) - Olivia Hwa - Dormant since Dec 10
3. **PD-2160** (RM 55.6K) - Ahmad Shafiq - Owner 0% win rate

## Pipeline Concentration Risk
- Olivia Hwa + Siti Noor Bahiyah control 70% (RM 145M)
- Top: Ted Wong 52% win rate
- Bottom: Ahmad Shafiq, Chin Horng Liew 0%

## Open Items

**PTL 121 System:**
- [x] Flow 2: Partner response handler (Form 2 → SharePoint + email)
- [x] Flow 3: Final validation (email trigger → supervisor notification)
- [x] Flow 4: Weekly delivery check (scheduled Monday 9AM SGT)
- [ ] Flow 5: Delivery confirmation handler (Form 3 → points) ⚠️ **Implementation guide ready**
- [ ] End-to-end testing
- [ ] Pilot rollout

**Documentation (in cto-brain/modules/grow-ptl/):**
- PTL_Flow5_Implementation.md (step-by-step build guide)
- PTL_121_System_Overview.md (complete architecture diagram)

**CRM Enforcement Scan:**
- [x] Deploy WF-ZOHO-DEPLOY v1.2 enhanced scan
- [x] Fix OAuth scopes (settings.ALL + workflow_rules.ALL)
- [x] Scan complete — 57 workflow rules across 8 modules
- [ ] Walk through 4 Deals layouts (Direct, Project, Trading, Troubleshoot) with Chok
- [ ] Review blueprints + Kiosk Studio visually (no API)
- [ ] Map 57 rules to layouts, identify actual gaps
- [ ] Correct ROOT_CAUSE_ANALYSIS.md (currently says "zero enforcement" — wrong)

**Pipeline Risk:**
- [x] Map systems → Zoho
- [x] Export deals → 4,209 analyzed
- [x] Build risk model → 92.8% accuracy
- [x] Identify at-risk → RM 20.5M flagged
- [ ] Validate high-risk list with Chok
- [ ] Enable daily automated scan
- [ ] Test Zoho write access for auto-flagging

## Learnings

**Pipeline Risk:**
- Large deals have 20.9% win rate vs 37.8% overall
- Lost deals 67% larger than won (RM 392K vs RM 234K)
- Owner performance varies 52 percentage points

**PTL 121 Automation (2026-02-06):**
- Power Automate email To field has hidden mode switch for dynamic expressions
- Must click ⚙️ → "Use dynamic content" to accept expressions in loops
- Person-picker mode (default) silently rejects expressions - no error message
- Timezone must be Singapore Standard Time (UTC+08:00) for local business hours
