# Kinme System

> Japanese upmarket izakaya — sake, sashimi, grill

**Last Updated**: 2025-01-31
**Status**: Foundation phase

---

## Business Profile

| Attribute | Value |
|-----------|-------|
| Type | Upmarket Japanese Izakaya |
| Positioning | Premium (sake, sashimi, grill) |
| Key Differentiator | (To be documented) |
| Location(s) | (To be documented) |
| Covers/day | (To be documented) |
| Avg spend/head | (To be documented) |

---

## CFO Toolkit Components

### 1. Menu Engineering Matrix

Analyzes each menu item on two dimensions:
- **Popularity** (volume sold)
- **Profitability** (contribution margin)

| Category | Popularity | Profitability | Action |
|----------|------------|---------------|--------|
| **Stars** | High | High | Promote heavily |
| **Plow Horses** | High | Low | Reengineer or raise price |
| **Puzzles** | Low | High | Promote more |
| **Dogs** | Low | Low | Remove or reinvent |

### 2. Food Cost Master

For each menu item:
- Ingredients list with portions
- Cost per ingredient
- Total food cost
- Selling price
- Food cost %
- Contribution margin

**Target food cost %**: Typically 28-32% for upmarket

### 3. Daily P&L Tracker

- Revenue by category (food, sake, other drinks)
- Covers count
- Average spend
- Food cost (actual vs theoretical)
- Labor cost
- Daily contribution

### 4. Inventory & Waste Tracking

Critical for fresh ingredients (sashimi)
- Pars for key items
- Waste log
- Variance analysis

---

## Key Metrics

| Metric | Target | Current | Notes |
|--------|--------|---------|-------|
| Food Cost % | 28-32% | ? | Need data |
| Beverage Cost % | 20-25% | ? | Sake margin critical |
| Labor Cost % | 25-30% | ? | — |
| Prime Cost % | <65% | ? | Food + Labor |
| Avg Spend/Cover | ? | ? | Need benchmark |
| Covers/Service | ? | ? | — |

---

## Questions to Answer

- [ ] What's the current menu structure?
- [ ] What's the top 10 sellers by volume?
- [ ] What's the top 10 by margin?
- [ ] Any items with food cost > 35%?
- [ ] What's sake vs food revenue split?
- [ ] What's the waste situation (esp. sashimi)?
- [ ] How is inventory currently tracked?
- [ ] What POS system is in use?

---

## Data Needed

To build the full CFO toolkit, I need:

1. **Menu with prices** — Current menu, all items, selling prices
2. **Recipe/portion specs** — Ingredients and quantities per dish
3. **Ingredient costs** — Current supplier pricing
4. **Sales data** — Item-level sales (from POS)
5. **Inventory data** — Current stock, waste logs

---

## n8n Automation (Future)

- Daily: Pull POS sales data → calculate actual food cost
- Weekly: Menu engineering analysis → flag dogs
- Alert: Food cost % exceeds 35%
- Alert: Key ingredient price spike > 10%
- Monthly: Full P&L summary

---

## Files in This Folder

- `KINME_SYSTEM.md` — This file (overview)
- `menu_engineering.xlsx` — Menu analysis (to be created)
- `food_cost_master.xlsx` — Recipe costing (to be created)
- `daily_tracker.xlsx` — Daily P&L (to be created)

---

## Learnings (Kinme-Specific)

> What we learn about this business

### Pricing Insights
- (None yet)

### Cost Insights
- (None yet)

### Operational Insights
- (None yet)

---

*"The menu is not a list of dishes. It's a financial instrument."*
