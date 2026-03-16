# Query Checklist

Use this checklist to verify analytics SQL quality.

## Correctness

- Metric definition is explicit and unambiguous.
- Time grain is explicit (day, week, month, etc.).
- Filters match the user request exactly.
- Null handling is intentional.

## Join safety

- Join keys are complete and typed correctly.
- Join direction preserves the intended row set.
- Duplication risks are checked before aggregation.

## Performance basics

- Date filter is pushed down as early as possible.
- Large joins are reduced with pre-aggregation where possible.
- Unused columns are removed.

## Readability

- CTE names describe business meaning.
- Final `SELECT` is short and understandable.
