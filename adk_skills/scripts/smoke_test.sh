#!/usr/bin/env bash
set -euo pipefail

ADK_MODEL="${ADK_MODEL:-gemini-2.5-flash}" uv run python -m adk_skills_demo_agent.smoke_test
