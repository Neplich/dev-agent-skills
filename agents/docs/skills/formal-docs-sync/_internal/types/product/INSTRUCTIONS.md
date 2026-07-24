# Product Sync Instructions

Load this module only when a confirmed write scope or an explicitly requested
read-only candidate-planning scope contains `doc_type: product`.

## Evidence Checks

Use current user-facing implementation and acceptance evidence to verify, as
applicable:

- intended user roles, entry points, supported scenarios, and capability
  boundaries;
- current terms, objects, states, and constraints shown by the product;
- the real user flow from entry and configuration through result or recovery;
- role-based visibility, authorization, limits, validation, failure feedback,
  and recovery paths;
- UI, API, integration, acceptance, and E2E evidence for material behavior;
- in release mode, the confirmed version scope for every changed product fact.

Do not turn roadmap scope, a PRD target, or a Release Notes statement into
current product behavior without implementation and test evidence.

## Template and Output Rules

Read the product template linked from the host standards entry—normally
`docs/site/standards/templates/product-handbook.md`—and consume its single
`docs-scaffold` block for a new page. Do not copy the template into this skill.

Derive the hierarchy from the confirmed feature catalog, `feature_path`, user
entry points, acceptance evidence, and feature ownership. Treat every
non-leaf feature node as recursively nestable: product domain -> child feature
-> deeper child feature -> (continue for every confirmed `feature_path`
segment) -> user task or scenario leaf. The confirmed feature catalog and
multi-segment `feature_path` determine the depth; never cap it at a fixed
number of feature levels, invent intermediate levels, or derive the tree from
source folders, UI page count, or roles alone.

- `docs/site/product/index.md` is only the capability map, audience entry, and
  global navigation.
- Give every domain and every feature node that has children, at any depth, its
  own `index.md`. Each such index states that node's scope, applicable roles,
  owner, children, adjacent features, exclusions, and downward navigation
  without repeating descendant task content or substituting for a descendant
  index.
- Give each independently completable or understandable user task its own leaf
  page. Distinct entry points, permissions, outcomes, failure feedback, or
  recovery paths are executable split signals even when the combined page
  would be short.
- Split concepts, permissions / limits, or recovery guidance into a shared page
  only when several tasks reuse it and it has independent maintenance value;
  every consuming task links back to it.
- Treat roles as behavior and visibility evidence unless they have materially
  different entry points and lifecycles that justify separate branches.

For the candidate scope, show the complete parent-child tree and, per page,
reader task, owner, evidence, code glob, change-map delta, links, and
exclusions. For every leaf, enumerate the full ancestor chain from the Product
root through every confirmed non-leaf feature, create or update each ancestor
`index.md`, and verify every parent links its direct children. Every confirmed
feature and task must therefore be reachable from the Product root one level at
a time, regardless of nesting depth. Write for the confirmed audience and
describe existing behavior, constraints, permissions, failures, and recovery.
Link Design, API, Database, and Ops authority pages instead of duplicating
their contracts. Keep each page, all required ancestor indexes and links, and
its change-map entries in the same confirmed write/read-back scope. Release
Notes content, index, metadata, and navigation remain outside this module and
must be handed to `docs-agent:release-notes-generator`.
