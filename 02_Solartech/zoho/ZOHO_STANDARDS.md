# Zoho Standards — Solartech

*Rules specific to the Zoho CRM and automation work for Solartech.*

**Last Updated:** 2025-01-28
**Total Rules:** 8

---

## Deluge Script Rules

### [Z-DEL-001] Verify Module Names Match Exactly
- **Severity:** 🔴 Critical
- **Added:** 2025-01-28
- **Origin:** Failure post-mortem [F-001]
- **Applied:** 0 times

**Rule:** Module names in Deluge must match Zoho's exact naming. Use "Contacts" not "Contact".

**How to verify:**
1. Go to Setup → Modules and Fields
2. Click on the module
3. Copy the API name exactly as shown

**Common gotchas:**
- "Contacts" (plural) not "Contact"
- "Deals" (plural) not "Deal"
- Custom modules: use API name, not display name

---

### [Z-DEL-002] Use getRecordById When You Have the ID
- **Severity:** 🟡 Important
- **Added:** 2025-01-28
- **Origin:** Review (performance)
- **Applied:** 0 times

**Rule:** When you already have a record ID, use `zoho.crm.getRecordById()` instead of search functions.

**Why:** Faster, more reliable, uses fewer API calls.

```deluge
// ✅ Good - direct lookup
record = zoho.crm.getRecordById("Contacts", contactId);

// ❌ Avoid - unnecessary search
records = zoho.crm.searchRecords("Contacts", "(id:equals:" + contactId + ")");
```

---

### [Z-DEL-003] Always Wrap CRM Operations in Try/Catch
- **Severity:** 🔴 Critical
- **Added:** 2025-01-28
- **Origin:** Review
- **Applied:** 0 times

**Rule:** Every `zoho.crm.*` operation must be wrapped in try/catch with meaningful error logging.

```deluge
try {
    response = zoho.crm.updateRecord("Contacts", recordId, updateMap);
    info "Update successful: " + response;
} catch (e) {
    info "ERROR updating contact " + recordId + ": " + e;
    // Handle error or notify
}
```

---

### [Z-DEL-004] Log Record IDs in All Operations
- **Severity:** 🟡 Important
- **Added:** 2025-01-28
- **Origin:** Review (debugging)
- **Applied:** 0 times

**Rule:** When logging CRM operations, always include the record ID for traceability.

```deluge
info "Processing contact ID: " + contactId + " - Name: " + contactName;
```

---

## Mail Merge Rules

### [Z-MM-001] Test Merge Fields with Special Characters
- **Severity:** 🔴 Critical
- **Added:** 2025-01-28
- **Origin:** Failure post-mortem
- **Applied:** 0 times

**Rule:** Before deploying mail merge, test with records containing special characters in merge fields (quotes, ampersands, accented characters).

---

### [Z-MM-002] Verify PDF Size Before Attachment
- **Severity:** 🔴 Critical
- **Added:** 2025-01-28
- **Origin:** Failure post-mortem [F-002]
- **Applied:** 0 times

**Rule:** Check generated PDF file size before attaching. Fail explicitly if over 5MB.

```deluge
if (pdfFile.get("file_size") > 5000000) {
    info "ERROR: PDF too large for attachment: " + pdfFile.get("file_size") + " bytes";
    // Handle oversized file
}
```

---

## Zoho Analytics Rules

### [Z-ANA-001] Use SQL Queries for Multi-Column Sorting
- **Severity:** 🟡 Important
- **Added:** 2025-01-28
- **Origin:** Review (workaround for limitation)
- **Applied:** 0 times

**Rule:** Zoho Analytics UI doesn't support multi-column sorting. Use SQL Query Tables instead.

```sql
SELECT * FROM "Sales Data"
ORDER BY Region ASC, Revenue DESC
```

---

### [Z-ANA-002] Use Formula Columns for Computed Sort Keys
- **Severity:** 🟢 Best Practice
- **Added:** 2025-01-28
- **Origin:** Review
- **Applied:** 0 times

**Rule:** When you need complex sorting logic, create a formula column that generates a sortable value, then sort by that column.

---

## Workflow Rules

### [Z-WF-001] Name Workflows with Module Prefix
- **Severity:** 🟢 Best Practice
- **Added:** 2025-01-28
- **Origin:** Review
- **Applied:** 0 times

**Rule:** Prefix workflow names with the module they operate on for easy identification.

Examples:
- `CONTACT_SendWelcomeEmail`
- `DEAL_UpdateStageNotification`
- `LEAD_AssignToSalesRep`

---

## Environment Details

**Domain Configuration:**
- Domain: waterhippos.com
- Email: Office 365
- SPF: Configured
- DKIM: Configured

**API Limits:**
- Be aware of daily API call limits
- Batch operations when possible
