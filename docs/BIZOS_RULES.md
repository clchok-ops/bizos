# BizOS — Preventive Rules

*Rules generated from business operations failures and near-misses. Prevents recurring mistakes.*

**Last Updated:** 2026-02-07
**Total Rules:** 0

---

## How Rules Are Created

```
Failure occurs → learn bizos: [what happened]
             → FAILURE_LOG.md (post-mortem)
             → BIZOS_RULES.md (this file — preventive rule)
```

---

## Rule Format

Rules are tagged by layer and category:

| Prefix | Layer | Example |
|--------|-------|---------|
| R-BIZ-SYS-XXX | System | CRM config, automation pipelines, data architecture |
| R-BIZ-PROC-XXX | Process | Review cadence, entity management, reporting |
| R-BIZ-MOD-XXX | Model | KPIs, PTL scoring, performance targets |

---

## System Rules (R-BIZ-SYS)

### [R-BIZ-SYS-001] Zoho OAuth Scopes Are Requested at Auth Flow, Not App Registration
**Severity:** 🟡 Important
**Added:** 2026-02-11
**Origin:** Zoho Infrastructure Agent setup — Zoho API Console UX mismatch with documentation

**Rule:** When registering a Server-based Application in Zoho API Console, there is no "scope" field. The console only asks for "Allowed HTTP Request Domains." Scopes (`ZohoCRM.settings.ALL`, `ZohoCRM.modules.ALL`, etc.) are requested during the OAuth authorization flow — typically handled by the client application (e.g., n8n's credential configuration).

**Setup pattern for n8n:**
1. Zoho API Console → Register app → add n8n domain to "Allowed HTTP Request Domains"
2. n8n → Add credential → Zoho CRM OAuth2 API → paste Client ID + Secret
3. Scopes configured in n8n's credential scope field (or passed during OAuth consent)
4. Click Connect → Zoho prompts for consent with requested scopes

**Credential:** `zoho_infra_settings` in n8n (verified 2026-02-11, read access to `/crm/v8/settings/fields` confirmed)

---

## Process Rules (R-BIZ-PROC)

(none yet)

---

## Model Rules (R-BIZ-MOD)

(none yet)

---

## Cross-References

Rules that apply across all repos live in `cto-brain/CRITICAL_RULES.md`. Key cross-system rules relevant to bizos:

- G-DOC-001: Check ARCHITECTURE_INDEX.md before creating new docs
- G-DOC-004: Audit existing files before creating new ones
- G-DOC-005: Validate bizos structure at session start/end per STRUCTURE.md
- G-VERIFY-001: Never claim something works until end-to-end verified

## Related Files

- `FAILURE_LOG.md` — post-mortems that generated these rules
- `BIZOS_PATTERNS.md` — success patterns (the positive counterpart)
- `BIZOS_KAIZEN.md` — experiments to improve
