---
name: maintain-skills
description: Manage role Skill and Agent lifecycle changes in this repository, including additions, modifications, renames, and required sync surfaces. Use for Skill contract or registration changes.
---

# Maintain Skills

Manage the repository's role-skill lifecycle without reimplementing its sync
surfaces. Treat this skill as the operator workflow for skill structure and
registration, `references/sync-surfaces.md` as the authoritative sync checklist,
and `references/change-types.md` as the change classification.

Read [references/change-types.md](references/change-types.md) before classifying a
request. Read [references/sync-surfaces.md](references/sync-surfaces.md) before
editing anything, and check every surface it lists against the final diff.

## Classify the Change

- Treat "新增 agent / skill" as **add**. A new skill lives inside an existing
  agent; a new agent adds the full `agents/{agent-name}/` skeleton.
- Treat "修改 skill 的 SKILL.md、frontmatter、结构、描述或共享契约副本" as **modify**.
  Judge the change tier against the tier contract in `AGENTS.md`（hotfix /
  standard / major）and record it before planning.
- Treat "重命名 skill 目录" as **rename**. Renames are path-contract changes:
  marketplace paths, router references, README references, and lockfile entries
  all move together.
- Classify first, then scan. Do not skip classification because the edit looks
  small.

## Scan the Impact

- Read `references/sync-surfaces.md` and list every surface the change touches:
  registration, routing, discovery, agent docs, top-level entry, process docs,
  and shared-contract copies.
- Check the high-risk surfaces named in the reference: discovery metadata,
  PM entry classification, and process-doc/diff consistency.
- State the forbidden files or areas for this change explicitly; do not edit
  anything outside the confirmed scope.

## Plan the Minimal Change

Before editing, output:

1. Change type and `change_tier` with the evidence that supports them.
2. The exact impact-surface list and forbidden areas.
3. A line-count order-of-magnitude expectation (e.g. "净新增约 150 行，不新增
   抽象").
4. The verification commands that will prove the change.

Only implement changes listed in the plan. If the plan grows beyond the expected
scale, stop and re-scope.

## Execute the Sync

- Registration: add or update the skill in `.claude-plugin/marketplace.json` and
  refresh its entry and `computedHash` in `skills-lock.json`. A new agent also
  creates `agents/{agent}/.claude-plugin/plugin.json` and adds its skills
  directory to `.kimi-plugin/plugin.json` (the contracts check path validity
  and version, not full agent coverage). Any tracked file change under a skill
  directory refreshes that skill's hash; a rename updates path and hash
  together.
- Routing: update the router SKILL.md sections that enumerate the specialist
  (Available Skills, Routing Signals, Specialist Gate Pointers, Default
  Routes, Role Boundary).
- Discovery: update the marketplace agent `description`, the router frontmatter
  `description`, and the root-routing pointer sentence in `AGENTS.md`.
- Agent docs: update `agents/{agent}/README.md` skills table, counts, and
  Routing Rules; mirror to `README_zh.md`.
- Top-level entry: update root `README.md` / `README_zh.md` (agent-table
  counts and capability descriptions, badges, agent name rows, router counts,
  install commands, Kimi directory counts, collaboration diagram, common
  flows, and the agent-doc index), the router listings in `.codex/INSTALL.md`
  and `docs/README.codex.md`, the agent counts and collaboration flow in
  `AGENTS.md`, and `pm-agent/SKILL.md` handoff targets, request classification
  lines, and Default Routes.
- Shared contracts: when extending an enum such as `doc_type`, update every
  copy: the authoritative definition, the consumer-skill copied tables, and the
  script assets and templates shipped by `docs-site-bootstrap`. Note in the PR
  that existing hosts must re-run bootstrap because shipped copies do not
  auto-upgrade.
- Process docs: keep PRD/TRD/implementation-plan touch tables and forbidden
  areas consistent with the actual diff.

## Verify the Final State

After the edits, run:

```bash
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
uv run --with pytest pytest <affected deterministic tests>
git diff --check
```

Stop and repair a static failure before considering the change done. Run the
deterministic tests that cover the touched surfaces (e.g. lockfile contract
tests).

## Report

Summarize for handoff: the change type and tier, files changed with the
sync-surface checklist result, verification results, and any leftover items.
