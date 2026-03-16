"""Simple entrypoint wrapper for the ADK skills demo.

This keeps a familiar `main.py` in the project root while the actual agent
definition remains in the package module.
"""

from adk_skills_demo_agent.agent import root_agent


def main() -> None:
    print("ADK Skills Demo")
    print(f"Agent: {root_agent.name}")
    print(f"Model: {root_agent.model}")
    print("Use one of these commands to run the agent:")
    print("- uv run adk run src/adk_skills_demo_agent")
    print("- uv run adk web src")


if __name__ == "__main__":
    main()
