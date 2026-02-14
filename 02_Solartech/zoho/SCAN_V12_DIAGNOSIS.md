# WF-ZOHO-DEPLOY v1.2 Scan Diagnosis
**Run:** WFZD-2026-02-14-165018 | **API Calls:** 83 | **Modules:** 11

## What WORKED (200 OK)

| Endpoint | Coverage | Notable Findings |
|----------|----------|-----------------|
| Fields | 11/11 modules | Deals: 204 fields (176 custom) |
| Layouts | 11/11 modules | Deals: 4 layouts, Quotes: 2, Sales_Orders: 2, Invoices: 2, Accounts: 2, Delivery_Orders: 2 |
| Validation Rules | 11/11 modules | Deals: 4 rules, all others: 0 |
| Related Lists | 11/11 modules | T&C: 24 (most connected module) |
| Module Definitions | Full scan | 70+ modules/subforms/trackers discovered |
| Assignment Rules | Global | 1 rule: Leads Assignment (modified Oct 2024) |

## What FAILED

### Blueprints — 404 on all 11 modules
**Root cause:** No `/settings/blueprint` endpoint exists in Zoho CRM v8.
Blueprint data is ONLY available per-record: `GET /{module}/{record_id}/actions/blueprint`
There is no settings-level API to list all blueprint configurations.

### Workflow Rules — 401 on all 11 modules (both paths)
**Root cause:** OAuth refresh token missing scope `ZohoCRM.settings.workflow_rules.READ`
- Tried: `/settings/automation/workflow_rules?module=X` → 401
- Fallback: `/settings/workflow_rules?module=X` → 401

### Other Automation — 401
| Endpoint | Error | Missing Scope |
|----------|-------|--------------|
| Scoring Rules | 401 | ZohoCRM.settings.scoring_rules.READ |
| Wizards | 401 | Unknown (may need settings.ALL) |
| Webhooks | 401 | ZohoCRM.settings.webhooks.READ |
| Field Updates | 401 | ZohoCRM.settings.field_updates.READ |

### Not API-Scannable
- Kiosk Studio (UI-only)
- Custom Functions (no list endpoint)
- Zoho Flow (separate product)

## FIX: Regenerate OAuth Token

Current token scopes cover: fields, layouts, validation_rules, related_lists, modules, assignment_rules
Missing: workflow_rules, scoring_rules, webhooks, field_updates, wizards, blueprints (record-level)

### Steps to regenerate:
1. Go to https://api-console.zoho.com/
2. Select the Self Client
3. Generate new code with scope:
   ```
   ZohoCRM.settings.ALL,ZohoCRM.modules.ALL
   ```
4. Set duration: 10 minutes
5. Copy the authorization code
6. Exchange for refresh token:
   ```
   curl -X POST "https://accounts.zoho.com/oauth/v2/token" \
     -d "grant_type=authorization_code" \
     -d "client_id=1000.3P4K76L3PKHS6N11LX47NRIVDXOD2O" \
     -d "client_secret=02bebf901438c56f84979b825462b4dcef44ea2c78" \
     -d "code=YOUR_NEW_CODE_HERE"
   ```
7. Save the new refresh_token
8. Update WF-ZOHO-DEPLOY Set Metadata node with new token

### Blueprint Scanning Fix
After token update, use per-record approach:
1. Get one active record from each blueprint-enabled module
2. Call `GET /{module}/{record_id}/actions/blueprint`
3. This returns available transitions, required fields per transition, and current state
