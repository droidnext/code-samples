"""Smoke test for the ADK skills demo agent."""

from __future__ import annotations

import os
import time

from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from google.genai.errors import ServerError

from .agent import root_agent


def _extract_text(content: types.Content | None) -> str:
    if not content or not content.parts:
        return ""
    chunks: list[str] = []
    for part in content.parts:
        text = getattr(part, "text", None)
        if text:
            chunks.append(text)
    return "\n".join(chunks).strip()


def run_smoke_test() -> str:
    app_name = "adk_skills_smoke"
    user_id = "smoke_user"
    query = (
        "A customer says login is failing for all teammates since morning and "
        "their production launch is blocked. Triage this ticket."
    )
    followup = "Now provide the triage output using your template."

    session_service = InMemorySessionService()
    session = session_service.create_session_sync(app_name=app_name, user_id=user_id)
    runner = Runner(
        app_name=app_name,
        agent=root_agent,
        session_service=session_service,
    )

    def run_with_retry(message: str, attempts: int = 3):
        last_error: Exception | None = None
        for attempt in range(1, attempts + 1):
            try:
                user_message = types.Content(role="user", parts=[types.Part(text=message)])
                return list(
                    runner.run(
                        user_id=user_id,
                        session_id=session.id,
                        new_message=user_message,
                    )
                )
            except ServerError as exc:
                last_error = exc
                if attempt == attempts:
                    break
                time.sleep(attempt * 2)
        if last_error:
            raise last_error
        return []

    events = run_with_retry(query)
    texts = [_extract_text(event.content) for event in events]
    texts = [t for t in texts if t]

    if not texts:
        events = run_with_retry(followup)
        texts = [_extract_text(event.content) for event in events]
        texts = [t for t in texts if t]

    if not texts:
        raise RuntimeError(
            "No text response from agent after skill-load turn and follow-up turn."
        )
    return texts[-1]


def main() -> None:
    if not os.getenv("GOOGLE_API_KEY") and os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "").lower() != "true":
        raise RuntimeError(
            "Set GOOGLE_API_KEY in .env (or configure Vertex AI) before smoke test."
        )

    response = run_smoke_test()
    print("SMOKE_TEST_OK")
    print(response)


if __name__ == "__main__":
    main()
