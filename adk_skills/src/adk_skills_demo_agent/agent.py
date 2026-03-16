"""ADK demo agent wired with two file-based skills."""

import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk import Agent
from google.adk.skills import load_skill_from_dir
from google.adk.tools import skill_toolset


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

triage_skill = load_skill_from_dir(PROJECT_ROOT / "customer-support-triage")
sql_skill = load_skill_from_dir(PROJECT_ROOT / "sql-analytics-helper")

skills = skill_toolset.SkillToolset(skills=[triage_skill, sql_skill])

root_agent = Agent(
    model=os.getenv("ADK_MODEL", "gemini-2.5-flash"),
    name="adk_skill_demo_agent",
    description="Demo agent using file-based ADK skills.",
    instruction=(
        "You are a helpful assistant. Use customer support triage skill for "
        "ticket classification and sql analytics helper skill for query drafting."
    ),
    tools=[skills],
)
