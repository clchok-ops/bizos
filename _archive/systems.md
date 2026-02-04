# System Connections

Integration points and architecture diagrams. Reference only.

---

## System-Entity Map

```
Solartech ──► Zoho (CRM, Inventory, Analytics)
Hippos    ──► Zoho (CRM, Inventory, Analytics)
WCI       ──► Odoo (MRP, Inventory, Sales)
Kinme     ──► Eats365 (API access pending)
Trading   ──► IBKR
```

## Integration Status

| System | Used By | Status | Notes |
|--------|---------|--------|-------|
| Zoho CRM | Solartech, Hippos | ✅ API Ready | zoho_client.py, refresh token in zoho.env |
| Zoho Inventory | Solartech, Hippos | ✅ API Ready | org_id=833030419 |
| Zoho Analytics | Solartech, Hippos | Active | Dashboards |
| Odoo | WCI | Active | MRP, Inventory, Sales |
| Eats365 | Kinme | Pending | Need developer access |
| IBKR | Trading | Not connected | API setup needed |

## 360° Data Flow

```
Zoho/Eats365 → Daily CSV → automation@solartech.com.my → _INBOX/ → Claude → _CONTEXT.md
```

## Credentials Reference

| System | Location |
|--------|----------|
| Zoho API | ~/Automation/config/zoho.env |
| n8n | localhost:5678 |
