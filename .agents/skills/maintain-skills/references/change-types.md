# Skill Change Types

Classify every role-skill lifecycle request before planning. Each type has a
different sync footprint.

## Add

A new skill inside an existing agent, or a whole new agent.

New skill inside an existing agent:

1. Create `agents/{agent}/skills/{skill-name}/SKILL.md` with the contract
   required frontmatter: `name` (equal to the skill directory), `description`,
   and `visibility: internal` (all skills except `pm-agent`); create
   `_internal/` only when staged loading is needed.
2. Register the skill in `.claude-plugin/marketplace.json` and refresh
   `skills-lock.json`.
3. Update the router, discovery metadata, agent READMEs, root READMEs, and
   `pm-agent` handoff targets per `sync-surfaces.md`.

New agent:

1. Create `agents/{agent-name}/skills/`.
2. Create `agents/{agent-name}/README.md` following an existing agent.
3. Create each skill's SKILL.md per the new-skill steps. The entry
   router skill name must equal the marketplace plugin name.
4. Register the agent in `.claude-plugin/marketplace.json` with
   `"source": "./agents/{agent-name}"` and `"strict": true` (every existing
   plugin uses both), refresh `skills-lock.json`, create
   `agents/{agent}/.claude-plugin/plugin.json`, and add the agent's skills
   directory to `.kimi-plugin/plugin.json`.
5. Check every sync surface.

## Modify

A change to an existing skill's SKILL.md, frontmatter, structure, description,
or shared-contract copies.

1. Classify `change_tier` against the tier contract in `AGENTS.md`.
2. Scan the impact per `sync-surfaces.md`; the surface set depends on what the
   modification touches (description changes hit discovery, and so on).
3. Keep each frontmatter `description` within 500 Unicode characters. Treat
   this as a hard ceiling, not a writing target: preserve the minimal discovery
   contract while moving detailed process and exhaustive lists into the body.
4. Refresh `skills-lock.json` `computedHash` for the skill when any tracked
   file under its directory changes (SKILL.md, `references/`, `_internal/`).

## Rename

A skill directory rename. This is a path-contract change: all references move
together.

- marketplace path in `.claude-plugin/marketplace.json`
- `skills-lock.json` entry path and hash
- the skill's `SKILL.md` frontmatter `name` (the contract requires it to match
  the skill directory)
- router references in the owning router SKILL.md
- README references in agent and root READMEs
- any process docs that name the path

Rename first, then scan for remaining references with a repo-wide search, then
re-run the static contracts.
