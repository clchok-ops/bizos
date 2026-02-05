# Hippos Architecture

> **Version:** 1.0
> **Last Updated:** 2026-02-05
> **Status:** Initial Discovery — Requires Browser Verification
> **Owner:** CTO Brain

---

## 1. Business Overview

### 1.1 Entity Profile

| Field | Value |
|-------|-------|
| **Company Name** | Super Hippo |
| **Business Model** | B2C Retail & Service |
| **Primary Product** | Solar Water Heaters |
| **Parent Relationship** | Partner of Solartech Group |
| **CRM Org ID** | 685901257 |

### 1.2 Entity Role in Group

```
┌─────────────────────────────────────────────────────────────────┐
│                      SOLARTECH GROUP                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌───────────┐         ┌─────────────┐         ┌───────────┐  │
│   │    WCI    │ ──────► │  SOLARTECH  │ ──────► │  HIPPOS   │  │
│   │ (Sister)  │ supplies│  (Parent)   │ supplies│ (Partner) │  │
│   └───────────┘         └─────────────┘         └───────────┘  │
│   Manufacturing         B2B Distributor         B2C Retail     │
│   Solar panels          Commercial sales        Residential    │
│                         Project sales           Water heaters  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.3 Business Lines

| Line | Type | Description |
|------|------|-------------|
| **Solar Water Heaters** | Primary | Installation, maintenance, repair |
| **Troubleshooting** | Service | Post-sale support and repairs |
| **Solar (Emerging)** | Future | Full solar systems (transition planned) |

### 1.4 Supplier Relationships

| Supplier | Products | Relationship |
|----------|----------|--------------|
| **WCI** | Solar water heater equipment | Manufacturing partner |
| **Solartech** | Solar panels, components | Group distribution |

---

## 2. Technology Stack

### 2.1 System Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| **CRM** | Zoho CRM (org685901257) | Enquiries, Contacts, Cases |
| **Inventory** | Zoho Inventory (shared?) | Products, Stock |
| **Source of Truth** | GitHub (bizos repo) | _CONTEXT.md, entity docs |
| **Local Sync** | iCloud (ClaudeHub) | Mac Mini ↔ Cloud |
| **AI Assistant** | Cowork (Claude) | Analysis, monitoring |

### 2.2 Data Flow

```
┌──────────────────────────────────────┐
│          ZOHO CRM (Super Hippo)      │
│  Enquiries, Contacts, Tasks, Cases   │
└─────────────────┬────────────────────┘
                  │ Scheduled Reports (9PM)
                  ▼
┌──────────────────────────────────────┐
│     Email: automation@solartech      │
│     Daily CSV reports                │
└─────────────────┬────────────────────┘
                  │ Auto-sorted
                  ▼
┌──────────────────────────────────────┐
│        _INBOX/zoho/                  │
│  2026-02-02_Todays_Enquiry.csv       │
└─────────────────┬────────────────────┘
                  │ Git auto-sync
                  ▼
┌──────────────────────────────────────┐
│     Mac Mini (ClaudeHub/bizos)       │
│     03_Hippos/ entity folder         │
└─────────────────┬────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────┐
│        Cowork (Claude)               │
│  Processing, Analysis, Actions       │
└──────────────────────────────────────┘
```

---

## 3. CRM Architecture

### 3.1 Organization Details

| Field | Value |
|-------|-------|
| **Org Name** | Super Hippo |
| **Org ID** | 685901257 |
| **Separate from Solartech?** | ⚠️ Yes (different org) — verify relationship |
| **Admin Contact** | TBD |

### 3.2 Modules Identified

| Module | API Name | Purpose | Status |
|--------|----------|---------|--------|
| **Enquiries** | CustomModule? | Primary B2C enquiry tracking | ✅ Confirmed |
| **Contacts** | Contacts | Customer database | ✅ Confirmed |
| **Tasks** | Tasks | Follow-up actions | ✅ Confirmed |
| **Cases** | CustomModule? | CS codes seen (CS20916) | ⚠️ Needs verification |
| **Accounts** | Accounts | Company records | ⚠️ Assumed |

### 3.3 Enquiries Module (Primary)

**Purpose:** Track all B2C enquiries from initial contact through resolution.

#### 3.3.1 Fields Identified (from CSV export)

| Field | Type | Description |
|-------|------|-------------|
| **Full Name** | Text | Customer/enquiry name |
| **Enquiry Owner** | Lookup (Users) | Assigned staff member |
| **Created Time** | DateTime | When enquiry was logged |
| **Enquiry Type** | Picklist | Type of request |
| **Problem (More Info)** | Text Area | Issue description |
| **Focus Area** | Picklist | Product category |
| **Enquiry Status** | Picklist | Current stage |
| **Enquiry Source** | Picklist | Lead source |
| **How did they find us?** | Text | Attribution detail |

#### 3.3.2 Enquiry Types

| Type | Description |
|------|-------------|
| **Troubleshooting** | Post-sale service/repair |
| **Opportunity** | New sales enquiry |
| *(Others TBD)* | Needs verification |

#### 3.3.3 Focus Areas

| Focus Area | Description |
|------------|-------------|
| **Solar Water Heater** | Primary product line |
| *(Others TBD)* | Needs verification |

#### 3.3.4 Enquiry Status Values

| Status | Description |
|--------|-------------|
| **In Progress** | Active, being worked |
| **Junk** | Invalid/spam enquiry |
| *(Others TBD)* | Needs verification |

### 3.4 Tasks Module

#### 3.4.1 Task Types Identified

| Task Type | Purpose |
|-----------|---------|
| **Field Care Troubleshooting Action** | On-site service follow-up |
| **Check Account Status** | Account verification |

### 3.5 Cases/Tickets (⚠️ Needs Verification)

Codes like `CS20916` and `CS20915-SP22859` appear in "Related To" field.

**Pattern:** `CS{5digits}` or `CS{5digits}-SP{5digits}`

This suggests either:
- Custom "Cases" module
- Deal/opportunity numbers with prefix

---

## 4. Users & Roles

### 4.1 Identified Users

| Name | Role | Primary Module |
|------|------|----------------|
| **Nurul Najihah Ab Aziz** | Enquiry Owner | Enquiries |
| **Izyan Mat Saman** | Enquiry Owner | Enquiries |
| **Atie Hashim** | Enquiry Owner | Enquiries |
| **FY Lim** | Enquiry Owner | Enquiries |

### 4.2 Role Structure (⚠️ Needs Verification)

```
Super Hippo
└── Operations Lead
    └── Enquiry Specialists
        ├── Nurul Najihah Ab Aziz
        ├── Izyan Mat Saman
        ├── Atie Hashim
        └── FY Lim
```

---

## 5. Daily Reports

### 5.1 Configured Reports

| # | Report | Schedule | Recipient |
|---|--------|----------|-----------|
| 1 | **Today's Enquiry** | Daily 9PM | automation@solartech.com.my |
| 2 | CRM Deals Report | Daily 9PM | automation@solartech.com.my |
| 3 | Inventory Summary | Daily 9PM | automation@solartech.com.my |
| 4 | Inventory Movements | Daily 9PM | automation@solartech.com.my |
| 5 | Analytics Dashboard | Daily 9PM | automation@solartech.com.my |

### 5.2 Report Fields (Today's Enquiry)

```csv
Full Name, Enquiry Owner, Created Time, Enquiry Type,
Problem (More Info), Focus Area, Enquiry Status,
Enquiry Source (Select one), How did they find us?
```

### 5.3 Report Status

| Report | First Received | Status |
|--------|----------------|--------|
| Today's Enquiry | 2026-02-02 | ✅ Active |
| CRM Deals | TBD | ⚠️ Verify |
| Inventory Summary | TBD | ⚠️ Verify |
| Inventory Movements | TBD | ⚠️ Verify |
| Analytics Dashboard | TBD | ⚠️ Verify |

---

## 6. Automation

### 6.1 Email Routing

| Source | Destination |
|--------|-------------|
| Daily Zoho reports | automation@solartech.com.my |
| automation@solartech | _INBOX/zoho/ |

### 6.2 n8n Workflows

**Status:** None configured for Hippos specifically.

*Note: Hippos-specific automations TBD. May be handled within Zoho or needs setup.*

### 6.3 Workflow Rules (⚠️ Needs Browser Verification)

| Rule | Module | Trigger | Actions |
|------|--------|---------|---------|
| TBD | TBD | TBD | TBD |

---

## 7. Inventory Integration

### 7.1 Product Categories (Expected)

| Category | Examples |
|----------|----------|
| **Solar Water Heaters** | 44G, 100G, 300L models |
| **Accessories** | Mounting, connectors |
| **Service Parts** | Replacement components |

### 7.2 Integration Status

| System | Status | Notes |
|--------|--------|-------|
| **Zoho Inventory** | ⚠️ Verify | May be shared with Solartech |
| **Stock Sync** | TBD | Need to confirm |
| **Pricing** | TBD | B2C pricing structure |

---

## 8. Metrics & Monitoring

### 8.1 Current Metrics (from _ENTITY.md)

| Metric | Value | Date |
|--------|-------|------|
| **Daily Enquiries** | ~5 | Feb 2, 2026 |
| **Primary Type** | Troubleshooting | |
| **Secondary Type** | Opportunities | |

### 8.2 Operational KPIs (Framework from HIPPOS_SYSTEM.md)

| Metric | Target | Current |
|--------|--------|---------|
| Lead-to-Customer Conversion | TBD | Unknown |
| First-Time Fix Rate | TBD | Unknown |
| Average Job Value | TBD | Unknown |
| Repeat Customer Rate | 40%+ | Unknown |
| LTV:CAC Ratio | 3:1+ | Unknown |

### 8.3 Monitoring Gaps

| Gap | Impact | Recommendation |
|-----|--------|----------------|
| No automated deal monitoring | Manual follow-up | Implement entity_monitor for Hippos |
| No pipeline visibility | Blind spots | Map Enquiry stages to pipeline |
| No win rate tracking | Can't optimize | Add conversion tracking |

---

## 9. Integration with Solartech

### 9.1 Relationship Status

| Aspect | Status | Notes |
|--------|--------|-------|
| **CRM** | Separate orgs | Hippos: 685901257, Solartech: 798433294 |
| **Inventory** | ⚠️ Unclear | May be shared — needs verification |
| **Automation** | Shared email routing | automation@solartech.com.my |
| **GitHub** | Shared (bizos repo) | Same source of truth |

### 9.2 Data Sharing

```
Solartech Zoho (798433294)    Super Hippo Zoho (685901257)
├── B2B Deals                  ├── B2C Enquiries
├── Project Pipeline           ├── Service Tickets
├── Inventory (?)  ←─────────? ├── Inventory (?)
└── Reports                    └── Reports
         │                              │
         └──────────┬───────────────────┘
                    ▼
            automation@solartech.com.my
                    │
                    ▼
            _INBOX/zoho/ (shared)
```

---

## 10. Gap Analysis

### 10.1 Documentation Gaps

| Gap | Severity | Action Required |
|-----|----------|-----------------|
| Full CRM module list | 🔴 High | Browser verification needed |
| Pipeline stages | 🔴 High | Map Enquiry → Deal flow |
| Workflow rules | 🟡 Medium | Document via Zoho Setup |
| Field definitions | 🟡 Medium | Export field metadata |
| User permissions | 🟡 Medium | Map role hierarchy |
| Inventory relationship | 🟡 Medium | Confirm shared vs separate |

### 10.2 Operational Gaps

| Gap | Impact | Recommendation |
|-----|--------|----------------|
| No entity_monitor | Manual oversight | Build Hippos monitor |
| No automated alerts | Missed follow-ups | Configure alert rules |
| No KPI dashboard | No visibility | Implement tracking |

### 10.3 vs. Solartech Architecture Coverage

| Section | Solartech | Hippos | Gap |
|---------|-----------|--------|-----|
| Business Overview | ✅ Complete | ✅ Basic | Minor |
| Technology Stack | ✅ Complete | ✅ Basic | Minor |
| CRM Pipeline | ✅ 4 layouts, all stages | ⚠️ 1 module partial | **Major** |
| Lead Management | ✅ Complete | ❌ Missing | **Major** |
| Quotes Module | ✅ Complete | ❌ Not applicable | N/A |
| Org Structure | ✅ Complete | ⚠️ Basic | Medium |
| Automation | ✅ 17 workflows | ⚠️ Unknown | **Major** |
| Monitoring | ✅ Complete | ❌ Missing | **Major** |
| Integration | ✅ Complete | ✅ Basic | Minor |

---

## 11. Next Steps

### 11.1 Immediate (Browser Verification)

1. **Login to Zoho CRM (org685901257)** and document:
   - [ ] All modules via Setup → Customization → Modules
   - [ ] Enquiries layout fields
   - [ ] Enquiry Status picklist values
   - [ ] Pipeline/stages if any
   - [ ] Workflow rules
   - [ ] Scheduled reports

2. **Verify Inventory relationship:**
   - [ ] Same Zoho Inventory instance as Solartech?
   - [ ] Separate product catalog?
   - [ ] Shared vs dedicated stock?

### 11.2 Short-term (Build)

1. **Implement Hippos entity_monitor.py** with:
   - Enquiry age alerts
   - Stale ticket detection
   - Daily summary

2. **Create Hippos KPI dashboard** tracking:
   - Enquiry volume
   - Resolution time
   - Owner workload

### 11.3 Long-term (Optimize)

1. **Unified Kaizen architecture** across:
   - Solartech (B2B)
   - Hippos (B2C)
   - Cross-entity insights

---

## Appendix A: File Structure

```
ClaudeHub/bizos/03_Hippos/
├── _ENTITY.md              # Entity status (quick ref)
├── HIPPOS_ARCHITECTURE.md  # This document
├── HIPPOS_SYSTEM.md        # Business framework
├── DATA_REQUIREMENTS.md    # Zoho export specs
├── SETUP_CHECKLIST.md      # Implementation guide
├── INDEX.md                # File navigation
├── README.md               # Getting started
└── hippos_dashboard.xlsx   # Operational tracker
```

---

## Appendix B: API Access

### B.1 Current Status

Hippos uses **separate Zoho org** from Solartech.

| Credential | Status |
|------------|--------|
| Client ID | ⚠️ Need new OAuth for org685901257 |
| Client Secret | ⚠️ Need new OAuth |
| Refresh Token | ⚠️ Need new OAuth |

*Current bizos/.env credentials are for Solartech (org798433294).*

### B.2 Required Scopes

```
ZohoCRM.modules.ALL
ZohoCRM.settings.ALL
ZohoCRM.users.READ
```

---

## Changelog

| Date | Version | Change |
|------|---------|--------|
| 2026-02-05 | 1.0 | Initial architecture document from discovery |

---

## Verification Checklist

Before this document is marked complete, verify:

- [ ] All modules listed in Section 3.2
- [ ] Enquiries fields complete
- [ ] Status/stage picklists documented
- [ ] Workflow rules captured
- [ ] User roles confirmed
- [ ] Inventory relationship clarified
- [ ] API credentials for Hippos org
