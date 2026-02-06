# Hippos Architecture

> **Version:** 2.0
> **Last Updated:** 2026-02-05
> **Status:** ✅ Browser Verified
> **Owner:** CTO Brain

---

## 1. Business Overview

### 1.1 Entity Profile

| Field | Value |
|-------|-------|
| **Company Name** | Super Hippo (Water Hippos) |
| **Business Model** | B2C Retail & Service |
| **Primary Product** | Solar Water Heaters |
| **Parent Relationship** | Partner of Solartech Group |
| **CRM Org ID** | 685901257 |
| **Admin Email** | super.hippo@waterhippos.com |

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
| **Inventory** | Zoho Inventory | Products, Stock |
| **Accounting** | Xero (via integration) | Invoicing, financials |
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
| **Org Name** | Water Hippos |
| **Org ID** | 685901257 |
| **Separate from Solartech?** | ✅ Yes (completely separate org) |
| **Super Admin** | Super Hippo (super.hippo@waterhippos.com) |
| **Admin Added By** | CL Chok (15 Sep 2020) |

### 3.2 Modules (Browser Verified ✅)

**Critical Discovery:** Hippos uses heavily customized module names. The "Display Name" shown in the UI differs from the underlying "API Name".

| Display Name | API Name | Purpose | Status |
|--------------|----------|---------|--------|
| **Enquiries** | Leads | Primary B2C enquiry tracking | ✅ Active |
| **Case** | Deals | Case/ticket management (CS codes) | ✅ Active |
| **People** | Contacts | Customer database | ✅ Active |
| **Company** | Accounts | Business accounts | ✅ Active |
| **Solution Proposal** | Quotes | Quotations | ✅ Active |
| **Invoices** | SalesOrders | Sales order tracking | ✅ Active |
| **Delivery Receipts** | Invoices | Delivery documentation | ✅ Active |
| **Accounts*** | CustomModule5 | Custom module | ✅ Active |
| **Housing Development*** | CustomModule9 | Property tracking | ✅ Active |
| **Goods S/N*** | CustomModule6 | Serial number tracking | ✅ Active |
| **T and C*** | LinkingModule9 | Terms & Conditions linking | ✅ Active |
| **Care History*** | LinkingModule14 | D.R. x S/N linking | ✅ Active |
| **Phones** | Cases | Phone/support cases | ✅ Active |
| **Care Plans*** | CustomModule2 | Service plans | ✅ Active |
| **Tasks** | Tasks | Follow-up actions | ✅ Active |
| **Meetings** | Meetings | Calendar events | ✅ Active |
| **Calls** | Calls | Call logging | ✅ Active |
| **Products** | Products | Product catalog | ✅ Active |
| **Vendors** | Vendors | Supplier management | ✅ Active |
| **Purchasing** | PurchaseOrders | Purchase orders | ✅ Active |

*Modules marked with * are custom modules specific to Hippos.*

### 3.3 Pipeline Configuration

| Layout | Pipeline Status |
|--------|-----------------|
| **Case (Standard)** | ❌ No pipelines configured |

*Note: Unlike Solartech which has 4 deal layouts with full pipeline stages, Hippos does not use pipeline stages in the Case module.*

### 3.4 Enquiries Module (Primary)

**Purpose:** Track all B2C enquiries from initial contact through resolution.

**API Name:** Leads

#### 3.4.1 Fields Identified (from CSV export)

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

#### 3.4.2 Enquiry Types

| Type | Description |
|------|-------------|
| **Troubleshooting** | Post-sale service/repair |
| **Opportunity** | New sales enquiry |

#### 3.4.3 Focus Areas

| Focus Area | Description |
|------------|-------------|
| **Solar Water Heater** | Primary product line |

#### 3.4.4 Enquiry Status Values

| Status | Description |
|--------|-------------|
| **In Progress** | Active, being worked |
| **Junk** | Invalid/spam enquiry |

### 3.5 Case Module

**API Name:** Deals

Codes like `CS20916` and `CS20915-SP22859` appear in records.

**Pattern:** `CS{5digits}` or `CS{5digits}-SP{5digits}`

---

## 4. Users & Roles (Browser Verified ✅)

### 4.1 Identified Users

| Name | Role(s) | Email | Status |
|------|---------|-------|--------|
| **Super Hippo** | Super Admin, Administrator | super.hippo@waterhippos.com | Active |
| **Abdul Halim Roslan** | Transition Cell Lead, Field Care Buddy | abdulhalim.roslan@waterhippos.com | Active |
| **Alif Aisar Abdul Hai** | Care Buddy Trainee, Associates | alifaisar.abdul@waterhippos.com | Active |
| **Amirul Hafiz Azahari** | Care Buddy Trainee, Support Buddy | amirulhafiz@waterhippos.com | Active |
| **Atie Hashim** | Care Support Lead, Support Lead | atie.hashim@waterhippos.com | Active |
| **Catherine Lim** | Executive Assistant, Specialist Lead | catherine.l@solartech.com.my | Active |
| **Chui Geok Ong** | TBD | chuigeok.ong@waterhippos.com | Active |

### 4.2 Role Hierarchy (Browser Verified ✅)

```
Water Hippos (Organization)
└── Admin
    ├── Talent and Ops
    │   └── Commercial Lead
    │       └── Commercial Specialist
    │
    ├── External CFO
    │
    ├── Home Care Lead
    │   ├── Specialist Care Lead
    │   │   └── Care Specialist Trainee
    │   │
    │   ├── Care Support Lead
    │   │   ├── Care Buddy Trainee
    │   │   └── Care Support Buddy
    │   │
    │   └── Field Care Lead
    │       └── Field Care Cell Lead
    │           ├── Field Care Buddy
    │           └── Transition Cell Lead
    │
    ├── Care Buddy
    │
    ├── Care XP
    │
    ├── Head of Marketing
    │
    └── Executive Assistant
```

**Total Roles:** 17+

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

## 6. Automation (Browser Verified ✅)

### 6.1 Email Routing

| Source | Destination |
|--------|-------------|
| Daily Zoho reports | automation@solartech.com.my |
| automation@solartech | _INBOX/zoho/ |

### 6.2 Workflow Rules (17 Total)

| # | Rule Name | Module | Trigger | Status | Modified |
|---|-----------|--------|---------|--------|----------|
| 1 | Send webhook | Delivery Receipts | Create or Edit | ❌ Inactive | 16/07/2020 |
| 2 | Send webhook | Accounts | Create or Edit | ✅ Active | 19/08/2019 |
| 3 | Person created | People | Create or Edit | ✅ Active | 07/12/2020 |
| 4 | Total Discount | Solution Proposal | Create or Edit | ✅ Active | 19/12/2024 |
| 5 | Total Quantity DR | Invoices | Create or Edit | ✅ Active | 22/10/2019 |
| 6 | Send to related | Purchasing | Modified | ❌ Inactive | 20/07/2020 |
| 7 | Update Case number | Case | Create or Edit | ✅ Active | 04/01/2024 |
| 8 | Update Warranty | Goods S/N | Create or Edit | ✅ Active | 04/06/2021 |
| 9 | Unlock Company | Company | Modified | ✅ Active | 07/12/2020 |
| 10 | Update Care Plan | Care Plans | Create or Edit | ✅ Active | 09/06/2021 |
| 11 | Create Xero Item | Products | Create | ✅ Active | 14/05/2024 |
| 12 | Total Discount | Delivery Receipts | Create or Edit | ✅ Active | 23/07/2020 |
| 13 | SP Total Amount | Solution Proposal | Create or Edit | ✅ Active | 22/10/2019 |
| 14 | Event Update | Meetings | Start DateTime | ✅ Active | 04/06/2021 |
| 15 | Invoice Subject | Invoices | Create or Edit | ✅ Active | 29/03/2023 |
| 16 | Update Account | Accounts | Create or Edit | ✅ Active | 19/07/2020 |
| 17 | Update OriCase | Case | Create or Edit | ✅ Active | 24/07/2020 |

**Summary:** 15 Active, 2 Inactive

### 6.3 Key Integrations

| Integration | Purpose | Status |
|-------------|---------|--------|
| **Xero** | Accounting sync (Create Xero Item) | ✅ Active |
| **Webhooks** | External notifications | Partially Active |

### 6.4 n8n Workflows

**Status:** None configured for Hippos specifically.

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
| **Zoho Inventory** | ✅ Confirmed | Separate dashboard accessed |
| **Xero Sync** | ✅ Active | Via "Create Xero Item" workflow |
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
| No pipeline visibility | Blind spots | Consider adding pipeline stages |
| No win rate tracking | Can't optimize | Add conversion tracking |

---

## 9. Integration with Solartech

### 9.1 Relationship Status

| Aspect | Status | Notes |
|--------|--------|-------|
| **CRM** | ✅ Separate orgs | Hippos: 685901257, Solartech: 798433294 |
| **Inventory** | ✅ Separate | Different Zoho Inventory instances |
| **Automation** | Shared email routing | automation@solartech.com.my |
| **GitHub** | Shared (bizos repo) | Same source of truth |
| **Accounting** | Xero integration | Via workflow rules |

### 9.2 Data Sharing

```
Solartech Zoho (798433294)    Super Hippo Zoho (685901257)
├── B2B Deals                  ├── B2C Enquiries (Leads)
├── Project Pipeline           ├── Cases (Deals)
├── Inventory                  ├── Inventory (separate)
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

### 10.1 Documentation Gaps (Updated)

| Gap | Severity | Status |
|-----|----------|--------|
| Full CRM module list | 🟢 Resolved | ✅ Browser verified |
| Pipeline stages | 🟡 Low | No pipelines configured |
| Workflow rules | 🟢 Resolved | ✅ 17 rules documented |
| User roles | 🟢 Resolved | ✅ Full hierarchy captured |
| Inventory relationship | 🟢 Resolved | ✅ Separate instance confirmed |

### 10.2 Operational Gaps

| Gap | Impact | Recommendation |
|-----|--------|----------------|
| No entity_monitor | Manual oversight | Build Hippos monitor |
| No automated alerts | Missed follow-ups | Configure alert rules |
| No KPI dashboard | No visibility | Implement tracking |
| No pipeline stages | Limited tracking | Consider adding stages to Case module |

### 10.3 vs. Solartech Architecture Coverage

| Section | Solartech | Hippos | Gap |
|---------|-----------|--------|-----|
| Business Overview | ✅ Complete | ✅ Complete | None |
| Technology Stack | ✅ Complete | ✅ Complete | None |
| CRM Modules | ✅ Complete | ✅ Complete | None |
| Pipeline | ✅ 4 layouts | ❌ None configured | Consider adding |
| Users & Roles | ✅ Complete | ✅ Complete | None |
| Automation | ✅ 17 workflows | ✅ 17 workflows | None |
| Monitoring | ✅ Complete | ⚠️ Needs work | Medium |
| Integration | ✅ Complete | ✅ Complete | None |

---

## 11. Next Steps

### 11.1 Completed ✅

- [x] All modules documented via browser
- [x] Workflow rules captured (17 rules)
- [x] User roles hierarchy documented
- [x] Pipeline status confirmed (none)
- [x] Inventory relationship clarified (separate)

### 11.2 Short-term (Build)

1. **Implement Hippos entity_monitor.py** with:
   - Enquiry age alerts
   - Stale ticket detection
   - Daily summary

2. **Create Hippos KPI dashboard** tracking:
   - Enquiry volume
   - Resolution time
   - Owner workload

3. **Consider pipeline stages** for Case module:
   - New → In Progress → Scheduled → Completed → Closed

### 11.3 Long-term (Optimize)

1. **Unified Kaizen architecture** across:
   - Solartech (B2B)
   - Hippos (B2C)
   - Cross-entity insights

2. **API Access Setup:**
   - Generate OAuth credentials for org685901257
   - Enable automated monitoring

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

## Appendix C: Module Name Mapping

This is critical for API development - the UI shows "Display Names" but the API requires "API Names":

| Display Name (UI) | API Name (Code) |
|-------------------|-----------------|
| Enquiries | Leads |
| Case | Deals |
| People | Contacts |
| Company | Accounts |
| Solution Proposal | Quotes |
| Invoices | SalesOrders |
| Delivery Receipts | Invoices |
| Phones | Cases |
| Purchasing | PurchaseOrders |

---

## Changelog

| Date | Version | Change |
|------|---------|--------|
| 2026-02-05 | 1.0 | Initial architecture document from discovery |
| 2026-02-05 | 2.0 | Browser verification complete - modules, workflows, roles documented |

---

## Verification Checklist

Before this document is marked complete, verify:

- [x] All modules listed in Section 3.2
- [x] Module name mapping (Display → API)
- [x] Pipeline status documented
- [x] Workflow rules captured (17 total)
- [x] User roles confirmed (17+ roles)
- [x] Inventory relationship clarified
- [ ] API credentials for Hippos org (pending)
