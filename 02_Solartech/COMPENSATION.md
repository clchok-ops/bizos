# Solartech Compensation Structure

**Status:** Model (to be implemented)
**Last Updated:** 2026-02-06

---

## Components

### 1. Base Salary

Monthly fixed component by role tier.

| Tier | Description |
|------|-------------|
| Pod Lead | Team leader with direct reports |
| Senior (Solo) | High performer, equivalent earnings to Pod Lead |
| Associate | Pod member, developing |

*Specific amounts in payroll records*

---

### 2. Bonus Pool (TTL-Driven)

Entity performance unlocks bonus pool:

| TTL Status | Pool Funded |
|------------|-------------|
| Grey | 0% of target |
| Red | 10% of target |
| Yellow | 15% of target |
| Green | 20% of target |

---

### 3. Individual Allocation (PTL-Driven)

Player's share from pool based on PTL performance:

```
Individual Bonus = Pool × (Player PTL Score / Sum of All PTL Scores)
```

Higher PTL = larger share of available pool.

---

### 4. Unit Allocation System

From Org Context model:

| Role | Units | Notes |
|------|-------|-------|
| Pod Lead | Higher | Team responsibility |
| Senior Solo | Equivalent to Pod Lead | Solo capacity |
| Associate | Base | Developing |

Units determine proportion of bonus pool.

---

## Performance Metrics

### Traffic Light Bonus Modifier

| PTL Color | Bonus Impact |
|-----------|--------------|
| Green | Full share |
| Yellow | Partial share |
| Red | Reduced share |
| Grey | Observation period, base only |

---

## Current vs Target

| Metric | Current | Target |
|--------|---------|--------|
| Gross Margin | ~14.3% | 33.3% |
| Annual Opex | ~RM 10M | Optimize |
| Monthly Salaries | ~RM 500K | Maintain efficiency |

*"Bleeding" at current margin - bonus structure part of rebalancing*

---

## Related

- PTL Framework: `bizos/00_Holding/PTL_FRAMEWORK.md`
- Sales Channels: `SALES_CHANNELS.md`
- Payroll data: Org Context sheet
