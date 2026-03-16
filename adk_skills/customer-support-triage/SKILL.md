---
name: customer-support-triage
description: Classifies customer support issues, sets priority, and recommends the next action. Use when handling tickets, incidents, outages, bugs, refunds, or customer complaint triage.
---

# Customer Support Triage Skill

## Goal

Help the agent respond consistently to support requests by:

1. Classifying the issue type.
2. Assigning severity and business priority.
3. Returning an actionable, empathetic response.

## Workflow

1. Extract key facts from the user message:
   - product area
   - user impact
   - urgency indicators
   - blocking status
2. Assign labels:
   - category: `bug`, `billing`, `access`, `feature-request`, `other`
   - severity: `sev1`, `sev2`, `sev3`, `sev4`
   - priority: `p0`, `p1`, `p2`, `p3`
3. Draft a response:
   - acknowledge impact
   - state immediate next step
   - request any missing required details
4. If details are missing, ask only for the minimum needed to proceed.

## Output template

Use this format:

```markdown
Category: <category>
Severity: <sev1|sev2|sev3|sev4>
Priority: <p0|p1|p2|p3>
Reasoning: <1-2 sentences>
Next Action: <specific action>
Customer Reply: <short user-facing response>
```

## Additional references

- See `references/PRIORITY_MATRIX.md` for severity and priority rules.
