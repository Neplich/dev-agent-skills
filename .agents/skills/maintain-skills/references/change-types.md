# Skill Change Types

Classify every role-skill lifecycle request before planning. Each type has a
different sync footprint.

## Add

A new skill inside an existing agent, or a whole new agent.

New skill inside an existing agent:

1. Create `agents/{agent}/skills/{skill-name}/SKILL.md`; create
   `agents/{agent}/test/{skill-name}/evals/evals.json` unless the project-level
   `skill-eval-runner` has registered a manual-only exception; create
   `_internal/` only when staged loading is needed.
2. Register the skill in `.claude-plugin/marketplace.json` and refresh
   `skills-lock.json`.
3. Update the router, discovery metadata, agent READMEs, root READMEs, and
   `pm-agent` handoff targets per `sync-surfaces.md`.
4. Author evals and run fresh paired comparison via `skill-eval-runner`.

New agent:

1. Create `agents/{agent-name}/{skills,test}`.
2. Create `agents/{agent-name}/README.md` following an existing agent.
3. Create each skill's SKILL.md and eval per the new-skill steps.
4. Register the agent in `.claude-plugin/marketplace.json`, refresh
   `skills-lock.json`, and add the agent's skills directory to
   `.kimi-plugin/plugin.json`.
5. Add evals for regularly evaluable skills and record real usage feedback for
   manual-only skills via `skill-eval-runner`, then check every sync surface.

## Modify

A change to an existing skill's SKILL.md, frontmatter, structure, description,
or shared-contract copies.

1. Classify `change_tier` against the tier contract in `AGENTS.md`.
2. Scan the impact per `sync-surfaces.md`; the surface set depends on what the
   modification touches (description changes hit discovery, routing changes hit
   router evals, and so on).
3. Refresh `skills-lock.json` `computedHash` for the skill when any tracked
   file under its directory changes (SKILL.md, `references/`, `_internal/`).
4. Route eval-impact analysis to `skill-eval-runner`.

## Rename

A skill directory rename. This is a path-contract change: all references move
together.

- marketplace path in `.claude-plugin/marketplace.json`
- `skills-lock.json` entry path and hash
- router references in the owning router SKILL.md
- README references in agent and root READMEs
- eval fixture paths under `agents/{agent}/test/{skill-name}/`
- any process docs that name the path

Rename first, then scan for remaining references with a repo-wide search, then
re-run the static contracts.
