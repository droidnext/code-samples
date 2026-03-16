# Priority Matrix

Use this matrix while triaging support requests.

## Severity definitions

- `sev1`: Service is down, major outage, or data loss risk.
- `sev2`: Core workflow broken for many users, no full outage.
- `sev3`: Partial issue, workaround exists, moderate impact.
- `sev4`: Minor issue, cosmetic issue, or low-impact question.

## Priority guidance

- `p0`: Immediate engineering response required now.
- `p1`: High urgency, should start in current work cycle.
- `p2`: Important but can be planned in normal backlog.
- `p3`: Low urgency or informational follow-up.

## Mapping rules

- If `sev1`, default to `p0`.
- If `sev2` and affected users are many, use `p1`.
- If `sev3`, use `p2` unless VIP customer and no workaround.
- If `sev4`, use `p3`.
