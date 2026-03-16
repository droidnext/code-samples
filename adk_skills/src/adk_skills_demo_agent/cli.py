"""Utility CLI commands for local demo setup checks."""

import os

from .agent import root_agent


def check() -> None:
    has_api_key = bool(os.getenv("GOOGLE_API_KEY"))
    print("ADK skills demo check")
    print(f"- Agent name: {root_agent.name}")
    print(f"- Model: {root_agent.model}")
    print(f"- GOOGLE_API_KEY set: {has_api_key}")
    if not has_api_key and os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "").lower() != "true":
        print(
            "- Warning: set GOOGLE_API_KEY in .env, or enable Vertex AI vars before running."
        )


def print_info() -> None:
    print("ADK skills demo project")
    print("- Module: adk_skills_demo_agent")
    print("- Skills: customer-support-triage, sql-analytics-helper")
