# ADK Skills Demo

This is a complete Python project for demonstrating Google ADK file-based
skills, with `uv` support and runnable scripts.

## Skills in this demo

- `customer-support-triage`: Classify support requests, set severity/priority,
  and generate clear customer-facing responses.
- `sql-analytics-helper`: Convert analytics questions into safe SQL drafts with
  a quality checklist.

## Project layout

```text
adk_skills/
├── pyproject.toml
├── .python-version
├── .env.example
├── main.py
├── src/adk_skills_demo_agent/
│   ├── __init__.py
│   ├── agent.py
│   └── cli.py
├── scripts/
│   ├── setup.sh
│   ├── run_check.sh
│   ├── run_cli.sh
│   ├── run_web.sh
│   └── smoke_test.sh
├── customer-support-triage/
└── sql-analytics-helper/
```

## Quick start (uv)

1. `cd adk_skills`
2. `./scripts/setup.sh`
3. Edit `.env` and set `GOOGLE_API_KEY`
4. `./scripts/run_check.sh`

## Run the demo

- CLI mode: `./scripts/run_cli.sh`
- Web mode: `./scripts/run_web.sh`
- Familiar entrypoint check: `uv run python main.py`
- Smoke test: `./scripts/smoke_test.sh`

## Notes

- `root_agent` is defined in `src/adk_skills_demo_agent/agent.py`.
- `demo_agent.py` is kept as a compatibility entrypoint.
- For Vertex AI mode, uncomment and set the Vertex vars in `.env.example`.
