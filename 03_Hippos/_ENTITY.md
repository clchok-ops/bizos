# Hippos Operations

**Status:** 🟢 Data flowing | **Last:** 2026-02-06
**Type:** B2C retail/service (Super Hippo = solar water heaters)
**Systems:** Zoho CRM (org685901257), Inventory (TBD)
**Org ID:** 685901257 (separate from Solartech 798433294)
**Transition:** Moving to solar and energy management this year

**Related:** `TTL_KPIS.md`, `roles/`

---

## Daily Reports (9PM CSV)
1. Today's Enquiry → automation@solartech.com.my ✅
2. CRM Deals Report → automation@solartech.com.my
3. Inventory Summary → automation@solartech.com.my
4. Inventory Movements → automation@solartech.com.my
5. Analytics Dashboard → automation@solartech.com.my

## CRM Structure
- **Primary Module:** Enquiries (custom)
- **Fields:** Full Name, Enquiry Owner, Created Time, Enquiry Type, Focus Area, Status
- **Enquiry Types:** Troubleshooting, Opportunity
- **Focus Areas:** Solar Water Heater
- **Status Values:** In Progress, Junk, (others TBD)
- **Owners:** Nurul Najihah Ab Aziz, Izyan Mat Saman, Atie Hashim, FY Lim

## Latest Data (Feb 2, 2026)
- 7 enquiries (mostly troubleshooting)
- Focus: Solar Water Heater
- Primary owner: Nurul Najihah Ab Aziz

## Open Items
- [x] Map systems → Zoho CRM org685901257
- [x] Configure daily reports → 5 reports, 9PM
- [x] First daily data received → Feb 2
- [x] Initial architecture doc → HIPPOS_ARCHITECTURE.md v1.0
- [ ] Complete CRM module discovery (browser verification)
- [ ] Map full Enquiry pipeline/stages
- [ ] Document workflow rules
- [ ] Clarify Inventory relationship (shared vs separate)
- [ ] Set up API credentials for Hippos org
- [ ] Understand B2C pricing and job costing
- [ ] Document transition plan to solar/energy

## Learnings
- **CORRECTION:** Hippos has SEPARATE Zoho org (685901257) from Solartech (798433294)
- Inventory relationship unclear - may or may not be shared
- Email routing goes through shared automation@solartech.com.my
- "Enquiries" module is primary (not "Deals" like Solartech)
