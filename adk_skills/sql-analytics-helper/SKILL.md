---
name: sql-analytics-helper
description: Converts analytics questions into safe SQL drafts and validation checks. Use when users ask for SQL queries, KPI breakdowns, funnel analysis, or reporting metrics.
---

# SQL Analytics Helper Skill

## Goal

Generate correct and reviewable SQL for analytics tasks.

## Workflow

1. Restate the metric in plain language.
2. Identify tables, join keys, filters, and date window assumptions.
3. Produce SQL with clear aliases and readable CTEs.
4. Add a validation checklist before finalizing.
5. If schema details are missing, ask focused questions first.

## SQL style rules

- Prefer CTEs over nested subqueries.
- Use explicit column lists (avoid `SELECT *`).
- Keep aggregation logic and filtering logic in separate steps.
- Add comments only where logic is not obvious.

## Output template

Use this format:

```text
Metric Intent: <plain language statement>
Assumptions:
- <assumption 1>
- <assumption 2>

SQL Draft:
  -- sql here

Validation Checklist:
- [ ] Time window matches request
- [ ] Filters applied correctly
- [ ] Join keys avoid duplication
- [ ] Aggregation level matches KPI definition
```

## Additional references

- See `references/QUERY_CHECKLIST.md` for a deeper query quality checklist.
