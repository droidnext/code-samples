---
name: sync-project-docs
description: Detect the coding agent (Cursor or Claude Code), discover project doc files, and update stale ones to reflect the current codebase. Use when the user asks to sync project docs, audit CLAUDE.md, update cursor rules, or after significant refactoring.
---

# Sync Project Documentation

Detect which coding agent is running, discover the relevant documentation files, audit them against the actual codebase, and update any that are stale.

## Workflow

Copy this checklist and track progress:

```
Sync Progress:
- [ ] Step 1: Detect coding agent
- [ ] Step 2: Discover doc files
- [ ] Step 3: Gather current code state
- [ ] Step 4: Detect drift
- [ ] Step 5: Update stale files
- [ ] Step 6: Report summary
```

### Step 1: Detect coding agent

Determine which coding agent is currently executing this skill.

| Signal | Cursor | Claude Code |
|--------|--------|-------------|
| Invoked via `.cursor/skills/` path | Yes | No |
| Has Cursor-specific tools (StrReplace, Glob, ReadLints, etc.) | Yes | No |
| System prompt mentions "Cursor" or "Cursor IDE" | Yes | No |
| Running as `claude` CLI | No | Yes |
| Reads `CLAUDE.md` natively on entry to directories | No | Yes |

**Decision rule:**
- If you were invoked by reading this file from `.cursor/skills/` **or** your system prompt references "Cursor" → you are **Cursor**.
- If you are the `claude` CLI agent → you are **Claude Code**.
- If you cannot determine, ask the user.

Set `AGENT_TYPE` to `cursor` or `claude-code` and proceed.

### Step 2: Discover doc files

Do NOT use a hardcoded file list. Dynamically discover documentation files that exist in the repo:

1. **Glob for `CLAUDE.md`**: search `**/CLAUDE.md` to find all Claude Code doc files.
2. **Glob for `.mdc` rules**: search `.cursor/rules/*.mdc` to find all Cursor rule files.

Then filter based on `AGENT_TYPE`:

| Agent Type | Primary files to update | Secondary (update if present) |
|------------|------------------------|-------------------------------|
| `cursor` | `.cursor/rules/*.mdc` | `**/CLAUDE.md` |
| `claude-code` | `**/CLAUDE.md` | `.cursor/rules/*.mdc` |

- **Primary files**: always audit and update these.
- **Secondary files**: only update if they exist AND the drift is significant (must-update category). Do not create secondary files that don't already exist.

Read all discovered doc files.

### Step 3: Gather current code state

For each sub-project that has at least one doc file, collect:

1. **Directory structure** -- list top-level source directories and key files.
2. **Dependencies** -- read `pyproject.toml`, `setup.py`, or `package.json` for current deps and versions.
3. **Key entry points** -- check that referenced files (main.py, App.tsx, agent.py, etc.) still exist and match documented patterns.
4. **Recent changes** (optional) -- run `git diff main --stat` and `git log --oneline -20` to see what changed since last sync.

### Step 4: Detect drift

Compare docs against code. Flag items in these categories:

**Must update** (docs reference something that no longer exists or is wrong):
- Directories or files mentioned in docs that were renamed/removed
- Classes, functions, or patterns described that changed
- Dependencies added or removed
- Tech stack version changes (e.g., React 19 → 20, new major dep)

**Should update** (docs miss something new and significant):
- New top-level directories or modules
- New architectural patterns (new middleware, new state management, etc.)
- New conventions that other developers should follow

**Skip** (routine changes that follow existing documented patterns):
- New endpoint added following the existing endpoint pattern
- New React component following existing component conventions
- New test file following existing test conventions
- Minor version bumps in dependencies

### Step 5: Update stale files

For each file that needs changes:

1. Make targeted edits -- do not rewrite entire files. Use StrReplace (or the equivalent edit tool) to update specific sections.
2. Keep the same structure and tone as the existing file.
3. For `CLAUDE.md`: update directory layouts, key files, tech stack, conventions.
4. For `.mdc` rules: update patterns, conventions, key references. Keep under 50 lines.

### Step 6: Report summary

Tell the user what was found and changed:

```
## Documentation Sync Report

**Agent detected:** Cursor | Claude Code

### Files audited
- (list all discovered doc files and which were primary vs secondary)

### Files updated
- `wheel-strategy-advisor-api/CLAUDE.md` -- added new /trades endpoint pattern, updated deps
- `.cursor/rules/wheel-strategy-advisor-ui.mdc` -- added Zustand convention

### Files unchanged (still accurate)
- `wheel-strategy-advisor/CLAUDE.md`
- ...

### Notes
- [any observations about architectural drift or suggestions]
```

## Important

- Do NOT rewrite files from scratch. Make surgical edits to keep diffs small and reviewable.
- Do NOT document every single new file -- focus on patterns, conventions, and architecture.
- Do NOT create new doc files that don't already exist (e.g., don't create a `CLAUDE.md` if the project only uses `.mdc` rules, and vice versa).
- If unsure whether a change warrants a doc update, ask the user.
