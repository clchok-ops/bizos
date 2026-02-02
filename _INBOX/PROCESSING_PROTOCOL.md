# _INBOX Processing Protocol

> **Purpose**: Define how incoming data files should be processed by Claude (or n8n automation).

---

## File Types & Processing Rules

### Zoho CRM Reports
| Pattern | Entity | Processing |
|---------|--------|------------|
| `*Enquiry*.csv` | Hippos | Count by type, extract new leads, update Hippos metrics in _CONTEXT.md |
| `*Deals*.csv` | Solartech | Run risk model, flag high-risk deals, update pipeline metrics |
| `*Inventory*.csv` | Solartech/Hippos | Check stock levels, flag low items |

### Eats365 POS Reports
| Pattern | Entity | Processing |
|---------|--------|------------|
| `Sales_Summary*.xls` | Kinme | Calculate daily/weekly metrics, update _CONTEXT.md |
| `Sales_By_Item*.xls` | Kinme | Item performance analysis, flag anomalies |
| `Inventory.xls` | Kinme | Stock check, flag out-of-stock and low items |

### Other
| Pattern | Entity | Processing |
|---------|--------|------------|
| `*.zip` | Various | Extract, then process contents |
| Unknown files | — | Move to `_INBOX/unknown/`, await manual review |

---

## Processing Steps

1. **Identify** - Match file pattern to processing rule above
2. **Parse** - Read file, extract key metrics
3. **Analyze** - Apply business rules (risk model, thresholds, etc.)
4. **Flag** - Add entries to `_CONTEXT.md > Flags & Anomalies` if issues found
5. **Update** - Update relevant entity section in `_CONTEXT.md`
6. **Archive** - Move to `_INBOX/_processed/{entity}/` with date prefix

---

## Flag Thresholds

### Kinme
- **Stock alert**: Any item at 0 quantity that should be in stock
- **Premium alert**: Whisky/sake bottles ≤ 2 units
- **Revenue alert**: Daily net < RM 3,000 (below Tuesday avg)
- **Discount alert**: Daily discount rate > 10%

### Hippos
- **Lead volume**: Alert if < 3 enquiries/day (low activity)
- **Owner imbalance**: Alert if one owner has > 80% of enquiries

### Solartech
- **High risk deal**: Risk score ≥ 51
- **Stuck deal**: No activity > 90 days on deals > RM 50K
- **Owner performance**: Win rate < 10%

---

## Automation Options (Future)

### Option A: n8n Workflow
```
Trigger: New file in iCloud/_INBOX
→ Call Claude API with file + this protocol
→ Claude processes, updates _CONTEXT.md
→ Claude moves file to _processed/
```

### Option B: Scheduled Startup
```
Daily 7 AM: Claude startup skill auto-runs
→ Checks _INBOX
→ Processes new files
→ Generates morning summary
```

### Current: Manual Startup
```
User says "startup" or "resume"
→ Claude checks _INBOX (per Session Protocol)
→ Offers to process if files found
```

---

## Version History
- 2026-02-02: Initial protocol created
