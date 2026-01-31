# BizOS Setup Checklist

> Track your progress here. Check off as you complete each step.

---

## Phase 1: API Access (Do First)

### EatPOS365 (Kinme)
- [ ] Log into EatPOS365 admin
- [ ] Find API/Integrations section
- [ ] Generate API key
- [ ] Test API with curl/Postman
- [ ] Document available endpoints
- [ ] **OR** Set up manual CSV export process

**API Key Generated**: ☐ Yes / ☐ No API available
**Base URL**: `_______________________________`

### Zoho One (Solartech/Hippos)
- [ ] Go to https://api-console.zoho.com
- [ ] Create Self Client application
- [ ] Note Client ID and Secret
- [ ] Generate authorization code
- [ ] Exchange for refresh token
- [ ] Test CRM API
- [ ] Test Inventory API
- [ ] Get Organization ID

**Client ID**: `1000.________________`
**Refresh Token**: ☐ Obtained

### Odoo (WCI)
- [ ] Log into Odoo as admin
- [ ] Enable Developer Mode
- [ ] Generate API key (Settings → Users → Preferences)
- [ ] Note database name
- [ ] Test XML-RPC connection
- [ ] Verify access to mrp.production model
- [ ] Verify access to stock.quant model

**URL**: `https://________________.odoo.com`
**Database**: `________________`
**API Key**: ☐ Generated

### IBKR (Trading)
- [ ] Log into Account Management
- [ ] Enable Client Portal API
- [ ] Download Client Portal Gateway
- [ ] Run gateway locally
- [ ] Test authentication
- [ ] Test positions endpoint
- [ ] **OR** Set up Flex Web Service

**Account ID**: `U________`
**Gateway Running**: ☐ Yes

---

## Phase 2: n8n Setup

### Installation
- [ ] Choose deployment (Cloud / Self-hosted)
- [ ] Create n8n account/instance
- [ ] Access n8n dashboard
- [ ] Note instance URL

**n8n URL**: `https://________________`

### Credentials
- [ ] Add EatPOS365 credential (HTTP Header Auth)
- [ ] Add Zoho CRM OAuth2 credential
- [ ] Add Zoho Inventory credential
- [ ] Add Odoo credential (HTTP Request)
- [ ] Add IBKR credential
- [ ] Add Email/SMTP credential for alerts

### File Access
- [ ] Connect BizOS folder to n8n
  - [ ] Option A: Mount folder (self-hosted)
  - [ ] Option B: Use cloud storage node (n8n Cloud)
- [ ] Test: Write a test file to BizOS
- [ ] Test: Read _CONTEXT.md from BizOS

**BizOS Path in n8n**: `________________`

---

## Phase 3: Build Workflows

### Workflow 1: Kinme Daily Sales
- [ ] Create workflow in n8n
- [ ] Add Schedule Trigger (6 AM daily)
- [ ] Add EatPOS365 API call
- [ ] Add metrics calculation function
- [ ] Add threshold checking
- [ ] Add file write (daily log)
- [ ] Add CONTEXT.md update
- [ ] Add email alert
- [ ] Test manually
- [ ] Activate

### Workflow 2: Trading Daily Check
- [ ] Create workflow in n8n
- [ ] Add Schedule Trigger (4 PM weekdays)
- [ ] Add IBKR API call
- [ ] Add metrics calculation
- [ ] Add drawdown check
- [ ] Add journal append
- [ ] Add alert if threshold breached
- [ ] Test manually
- [ ] Activate

### Workflow 3: Zoho Pipeline Check
- [ ] Create workflow in n8n
- [ ] Add Schedule Trigger (Monday 8 AM)
- [ ] Add Zoho CRM node (Get Deals)
- [ ] Add stalled deal detection
- [ ] Add CONTEXT.md update
- [ ] Add alert for issues
- [ ] Test manually
- [ ] Activate

### Workflow 4: WCI Production Check
- [ ] Create workflow in n8n
- [ ] Add Schedule Trigger (Monday 8 AM)
- [ ] Add Odoo API call (manufacturing orders)
- [ ] Add inventory check
- [ ] Add on-time rate calculation
- [ ] Add CONTEXT.md update
- [ ] Test manually
- [ ] Activate

### Workflow 5: Weekly Rollup
- [ ] Create workflow in n8n
- [ ] Add Schedule Trigger (Sunday 9 PM)
- [ ] Add CONTEXT.md read
- [ ] Add rollup function
- [ ] Add CONTEXT.md write
- [ ] Add weekly digest email
- [ ] Test manually
- [ ] Activate

---

## Phase 4: Testing

### Integration Tests
- [ ] EatPOS365 → n8n: Data flows correctly
- [ ] Zoho → n8n: Deals retrieved correctly
- [ ] Odoo → n8n: MO data retrieved correctly
- [ ] IBKR → n8n: Positions retrieved correctly
- [ ] n8n → BizOS: Files created correctly
- [ ] n8n → Email: Alerts received

### Workflow Tests
- [ ] Kinme Daily: Manually trigger, verify output
- [ ] Trading Daily: Manually trigger, verify output
- [ ] Zoho Pipeline: Manually trigger, verify output
- [ ] WCI Production: Manually trigger, verify output
- [ ] Weekly Rollup: Manually trigger, verify output

### Alert Tests
- [ ] Trigger a threshold breach intentionally
- [ ] Verify alert email received
- [ ] Verify flag added to CONTEXT.md

---

## Phase 5: Go Live

### Pre-Launch
- [ ] All Phase 1-4 items complete
- [ ] Backup _CONTEXT.md
- [ ] Review threshold settings
- [ ] Confirm alert recipients

### Activation Schedule
- [ ] Week 1: Activate Kinme Daily
- [ ] Week 2: Activate Trading Daily
- [ ] Week 3: Activate Zoho Pipeline
- [ ] Week 4: Activate WCI Production
- [ ] Week 5: Activate Weekly Rollup

### Post-Launch Monitoring (First 2 Weeks)
- [ ] Day 1: Check all workflows executed
- [ ] Day 2: Check all workflows executed
- [ ] Day 3: Check all workflows executed
- [ ] Day 7: Review first week of data
- [ ] Day 14: Review, adjust thresholds if needed

---

## Completion Sign-Off

| Phase | Completed | Date | Notes |
|-------|-----------|------|-------|
| Phase 1: API Access | ☐ | | |
| Phase 2: n8n Setup | ☐ | | |
| Phase 3: Build Workflows | ☐ | | |
| Phase 4: Testing | ☐ | | |
| Phase 5: Go Live | ☐ | | |

**BizOS Fully Operational**: ☐

---

## Quick Contacts / Resources

| System | Support |
|--------|---------|
| EatPOS365 | |
| Zoho | https://help.zoho.com |
| Odoo | |
| IBKR | https://www.interactivebrokers.com/en/support |
| n8n | https://community.n8n.io |

---

*Update this checklist as you progress. This is your single source of truth for setup status.*
