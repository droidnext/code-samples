# Doc Sync — Keep AI Agent Context Fresh

AI coding agents (Cursor, Claude Code) rely on project documentation (`CLAUDE.md`, `.cursor/rules/*.mdc`) to understand your codebase. These docs go stale fast — renamed modules, new dependencies, changed patterns — and stale docs cause agents to generate wrong code with high confidence.

This is a two-part system that detects documentation drift and fixes it.

## How It Works

### 1. The Tripwire — `doc-sync-reminder.mdc`

An always-on Cursor rule. After any structural change (new directories, renamed modules, changed patterns, added/removed dependencies), the agent nudges you:

> "You may want to run the **sync-project-docs** skill to update project documentation."

It stays quiet for routine changes that follow existing patterns (new endpoint, new component, new test). No noise.

### 2. The Fixer — `sync-project-docs/SKILL.md`

A reusable Cursor Skill that runs a 6-step audit when triggered:

1. **Detect agent** — auto-detects Cursor vs Claude Code
2. **Discover docs** — globs for `CLAUDE.md` and `.cursor/rules/*.mdc` (no hardcoded paths)
3. **Gather code state** — directory structure, dependencies, entry points
4. **Detect drift** — categorizes as must-update, should-update, or skip
5. **Surgical edits** — targeted updates, not full rewrites, keeping diffs small and reviewable
6. **Report summary** — tells you what changed and why

## Installation

### Cursor

Copy the files into your project:

```
# The always-on rule
cp doc-sync-reminder.mdc  <your-project>/.cursor/rules/doc-sync-reminder.mdc

# The skill
mkdir -p <your-project>/.cursor/skills/sync-project-docs
cp sync-project-docs/SKILL.md  <your-project>/.cursor/skills/sync-project-docs/SKILL.md
```

### Claude Code

The `SKILL.md` works with Claude Code as well — it auto-detects the agent. You can invoke it by referencing the file path, or adapt the workflow into your `CLAUDE.md`.

## Design Decisions

- **Discovery over configuration** — the skill globs for doc files rather than maintaining a list. Add a new sub-project with a `CLAUDE.md`? It just picks it up.
- **Targeted updates, not rewrites** — full regeneration loses voice, structure, and nuance. Surgical edits keep diffs reviewable.
- **Signal over noise** — routine changes get ignored. Only architectural drift gets flagged.
