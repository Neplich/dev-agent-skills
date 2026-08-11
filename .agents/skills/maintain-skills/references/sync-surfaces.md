# Skill Sync Surfaces

The authoritative checklist for role-skill and role-agent lifecycle changes. When
a change touches any surface below, update it in the same change; a missed
surface is not caught by contract scripts but makes the skill unreachable or
untrustworthy in practice.

| Surface | Required changes |
| --- | --- |
| Registration | `.claude-plugin/marketplace.json` `skills` array; `skills-lock.json` entry and `computedHash` |
| Routing | Router SKILL.md sections that enumerate the specialist: Available Skills, Routing Signals, Specialist Gate Pointers, Role Boundary |
| Discovery | `.claude-plugin/marketplace.json` agent `description`; router SKILL.md frontmatter `description`; the root-routing pointer sentence in `AGENTS.md` describing that router's routing scope |
| Agent docs | `agents/{agent}/README.md` skills table, counts, and Routing Rules; `README_zh.md` mirrored |
| Top-level entry | Root `README.md` / `README_zh.md` agent-table counts and capability descriptions; `pm-agent/SKILL.md` handoff targets, request classification lines, and Default Routes |
| Evals | The new skill's own evals; the router's routing evals; assertions of existing skills affected by the change and their durable `comparison.md` |
| Process docs | PRD/TRD/implementation-plan touch tables and forbidden areas must match the actual diff; parent PRD `child_features` and lines describing registration surfaces |

## High-Risk Surfaces

- Discovery metadata decides whether a client selects the skill before reading
  its body. Fully updating counts and bodies without the description leaves the
  capability nonexistent at the metadata layer.
- Router routing evals missing means a wrong routing branch can pass fully
  green.
- PM entry classification: `pm-agent` is the default user entry; every request
  without an explicit skill name goes through it. When a downstream router knows
  the new specialist but PM's classification vocabulary does not, the capability
  is unreachable for ordinary users.
- Existing skill evals and `comparison.md`: when a change affects contract
  asserted by the evals, the project-level `skill-eval-runner` must identify the
  affected scope and handle fresh evidence; do not reuse or hand-craft old
  conclusions.
- Process-doc/diff consistency: a forbidden area written in the plan but
  actually changed will make maintainers revert necessary edits later.

## Shared-Contract Copies

Extending a shared contract (e.g. the `doc_type` enum) requires syncing every
copy: the authoritative definition, the copied tables in consumer skills, and
the script assets and templates delivered to hosts by `docs-site-bootstrap`.
Copies shipped to hosts do not auto-upgrade with marketplace updates; existing
hosts must re-run bootstrap, and the PR must state this.

## Lockfile Notes

- `skills-lock.json` `computedHash` refreshes when the skill's SKILL.md changes.
- A rename updates both the entry path and the hash in the same change.
- The hash refresh is part of the same change as the SKILL.md edit; a contract
  check failing on a stale hash is a signal that the refresh was missed, not a
  request to stop and ask.
