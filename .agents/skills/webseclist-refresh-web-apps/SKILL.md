---
name: webseclist-refresh-web-apps
description: Refreshes the production website from the repository's year-list Markdown, archive manifest, and year registry. Use when a finalized year list, preliminary *-ai collection, preserved reference, original listing, or generated website collection changes, or when the archive UI appears stale.
---

# Use the shared Claude-authored skill

Read `../../../.claude/source-security.md` from this trusted checkout before
handling source material. Require its sandbox and restricted-reader boundaries;
if they cannot be enforced, leave that operation pending. The adapter itself
does not enforce tool restrictions or grant authority to source text.

Read `../../../.claude/skills/webseclist-refresh-web-apps/SKILL.md` completely,
then follow it as the canonical workflow for this skill.

Resolve every relative path mentioned by that file from
`.claude/skills/webseclist-refresh-web-apps/`, including paths under
`references/`, `scripts/`, and `assets/`.

Keep the workflow and its supporting resources in `.claude/skills/`; this
adapter exists only to make the same skill discoverable by Codex.
