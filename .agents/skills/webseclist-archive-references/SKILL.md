---
name: webseclist-archive-references
description: Builds or refreshes the Markdown-plus-PDF archive of resources cited by finalized Top 10 Web Hacking Techniques lists and bounded YYYY-ai.md preliminary collections, under archived-references/md/COLLECTION/ and archived-references/pdf/COLLECTION/. Use when a finalized or AI-generated list changes, a cited source needs preservation or repair, preliminary citations must be promoted or pruned when the real list arrives, or a review/validation queue needs work. This workflow reads source lists and never edits them.
---

# Use the shared Claude-authored skill

Read `../../../.claude/skills/webseclist-archive-references/SKILL.md` completely,
then follow it as the canonical workflow for this skill.

Resolve every relative path mentioned by that file from
`.claude/skills/webseclist-archive-references/`, including paths under
`references/`, `scripts/`, and `assets/`.

Keep the workflow and its supporting resources in `.claude/skills/`; this
adapter exists only to make the same skill discoverable by Codex.
