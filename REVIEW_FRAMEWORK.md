# Review Framework

> **Purpose**: Define what metrics to review at each cadence to ensure operational and financial performance is on track.

**Last Updated**: 2026-02-02

---

## 02_Solartech (B2B Distribution)

**Data Source**: Zoho CRM (Deals export - 211 fields available)

### Daily Review (Fire-spotting)
| Metric | Formula/Source | Threshold | Action if breached |
|--------|----------------|-----------|-------------------|
| **High-risk deals moved** | Deals with risk_score ≥51, Stage changed | Any movement | Review if deteriorating or recovering |
| **Stuck deals alert** | Last Activity Time > 7 days, Amount > RM 50K | Any new | Escalate to owner |
| **New deals** | Created Time = today | Count | Awareness only |
| **Deals closing this week** | Closing Date within 7 days | Count + value | Ensure follow-up happening |

### Weekly Review (Trend-spotting)
| Metric | Formula/Source | Threshold | Action if breached |
|--------|----------------|-----------|-------------------|
| **Pipeline movement** | Sum(Amount) by Stage, week-over-week | < 5% movement | Investigate stagnation |
| **Win rate (rolling 4 weeks)** | Won deals / (Won + Lost) | < 30% | Review lost deal reasons |
| **New pipeline added** | Sum(Amount) where Created Time = this week | < RM 1M | Sales activity review |
| **Owner performance** | Win rate by Deal Owner | Any owner < 15% | Training/reassignment |
| **At-risk value change** | Sum(Amount) where risk_score ≥ 51 | Increase > 10% | Pipeline health review |

### Monthly Review (Performance)
| Metric | Formula/Source | Target | Action if missed |
|--------|----------------|--------|-----------------|
| **Revenue closed** | Sum(Amount) where Stage = Won, Closing Date = this month | vs Budget | Gap analysis |
| **Deals won** | Count where Stage = Won | vs Last month | Trend check |
| **Avg deal size** | Revenue / Deals won | > RM 200K | Mix analysis |
| **Sales cycle** | Avg(Sales Cycle Duration) for won deals | < 90 days | Process review |
| **Loss reasons** | Group by Reason For Loss | Top 3 | Address root causes |
| **Collection rate** | Total Collected Amount / Grand Total | > 80% | Cash flow alert |

### Quarterly Review (Strategic)
| Metric | Formula/Source | Review |
|--------|----------------|--------|
| **Customer concentration** | Top 10 accounts as % of pipeline | Risk if > 50% |
| **Product mix** | Revenue by Deal Type | Diversification |
| **Owner capacity** | Pipeline per owner vs historical close rate | Hiring/training needs |
| **Pipeline coverage** | Total pipeline / Quarterly target | Need > 3x |
| **Large deal performance** | Win rate on deals > RM 500K | Strategy adjustment |

---

## 03_Hippos (B2C Retail)

**Data Source**: Zoho CRM (Enquiries), Zoho Inventory, Zoho Analytics

### Daily Review (Fire-spotting)
| Metric | Formula/Source | Threshold | Action if breached |
|--------|----------------|-----------|-------------------|
| **New enquiries** | Count from Today's Enquiry report | < 3 | Marketing check |
| **Response time** | Time from Created to first activity | > 24 hours | Follow-up alert |
| **Enquiry source mix** | Group by Enquiry Source | Any source = 0 | Channel issue |
| **Troubleshooting volume** | Count where Enquiry Type = Troubleshooting | > 50% of total | Service quality issue |

### Weekly Review (Trend-spotting)
| Metric | Formula/Source | Threshold | Action if breached |
|--------|----------------|-----------|-------------------|
| **Conversion rate** | Opportunities won / Total enquiries | < 20% | Sales process review |
| **Lead source ROI** | Conversions by source | Any source = 0 conversions | Reallocate spend |
| **Owner workload** | Enquiries per owner | Imbalance > 3x | Redistribute |
| **Repeat enquiries** | Same customer, multiple enquiries | > 10% | Service quality issue |

### Monthly Review (Performance)
| Metric | Formula/Source | Target | Action if missed |
|--------|----------------|--------|-----------------|
| **Revenue** | Sum of closed deals | vs Budget | Gap analysis |
| **Jobs completed** | Count of completed jobs | vs Last month | Capacity check |
| **Avg job value** | Revenue / Jobs | > RM X | Pricing review |
| **Customer acquisition cost** | Marketing spend / New customers | < RM X | Efficiency review |
| **Gross margin** | (Revenue - COGS) / Revenue | > 40% | Pricing/cost review |

### Quarterly Review (Strategic)
| Metric | Formula/Source | Review |
|--------|----------------|--------|
| **Service mix** | Revenue by service type | Growth opportunities |
| **Geographic coverage** | Jobs by region | Expansion potential |
| **Seasonal patterns** | Month-over-month trends | Staffing/inventory planning |
| **NPS / Customer feedback** | Survey results | Service improvement |

---

## Implementation Priority

### Phase 1: Daily Alerts (This week)
- [ ] Solartech: High-risk deal movement check
- [ ] Solartech: Stuck deals alert
- [ ] Hippos: Daily enquiry count + source mix

### Phase 2: Weekly Dashboards (Next week)
- [ ] Solartech: Pipeline movement tracker
- [ ] Solartech: Owner performance scorecard
- [ ] Hippos: Conversion funnel

### Phase 3: Monthly Reports (End of month)
- [ ] Solartech: Full P&L review template
- [ ] Hippos: Full P&L review template

---

## Data Requirements

### Solartech (from Zoho CRM)
| Report | Frequency | Fields needed |
|--------|-----------|---------------|
| Deals Export | Daily | All 211 fields (for risk model) |
| Closed Won | Weekly | Amount, Closing Date, Owner, Sales Cycle |
| Closed Lost | Weekly | Amount, Reason For Loss, Owner |

### Hippos (from Zoho CRM)
| Report | Frequency | Fields needed |
|--------|-----------|---------------|
| Today's Enquiry | Daily | Full Name, Owner, Created Time, Type, Source, Status |
| Deals by Stage | Weekly | Amount, Stage, Owner, Created Time |
| Inventory Summary | Weekly | Item, Category, Quantity |

---

## Version History
- 2026-02-02: Initial framework for Solartech and Hippos
