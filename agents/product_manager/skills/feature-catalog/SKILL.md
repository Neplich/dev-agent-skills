---
name: feature-catalog
description: "Build a feature catalog and project feature profile when taking over an existing project. Use this skill whenever the user inherits a codebase mid-way and needs to map existing routes, pages, APIs, services, data models, background jobs, tests, and docs into a maintainer-confirmable feature directory with evidence and confidence before any PRD work. Trigger on phrases like '建立功能目录', '功能画像', '接手项目先梳理功能', '这个项目现在有哪些功能', 'build a feature catalog', 'map the existing features', 'feature inventory for this repo', or any request to establish a feature directory for an inherited project."
---

# Feature Catalog

Turn an inherited project's code, docs, and business entry points into a
maintainable feature catalog. The skill produces a draft catalog with evidence
and confidence first, runs a maintainer confirmation gate on every
`feature_path`, and only then writes the formal catalog document and hands the
confirmed features to the existing PRD/TRD chain.

`feature_path` is the feature ownership key shared across PM, Engineer,
Design, QA, DevOps, and Security docs. This skill exists so take-over projects
get one confirmed feature map instead of ad-hoc names invented per request.

Detailed execution guidance lives in `_internal/INSTRUCTIONS.md`.

## When to Use

- The user takes over an existing project and asks what features it has today
- A feature catalog or project feature profile is needed before new PRD/TRD
  work on an inherited codebase
- Existing `docs/pm/**/PRD.md` coverage is partial and the user wants the
  remaining features mapped with evidence
- Another PM skill needs a confirmed `feature_path` tree for a legacy project

## Do NOT Use

- To shape a new idea or converge requirements — that is `pm-agent:idea-to-spec`
- To scan tech stack, dependencies, or conventions — that is
  `engineer-agent:codebase-analyzer`; this skill consumes its Project Profile
- To write PRD/BRD/DECISIONS content — confirmed features go to `prd-gen`
  (inside `idea-to-spec`)
- To design or implement code, tests, or deployment for the cataloged features

## Inputs

- Project Profile with `feature_inventory` from
  `engineer-agent:codebase-analyzer` (preferred evidence source)
- Existing `docs/pm/**/PRD.md`, `DECISIONS.md`, and README files
- Code scan results: routes, pages, API endpoints, services, data models,
  background jobs, tests

If no Project Profile or `feature_inventory` is available yet, request an
explicit handoff to `engineer-agent:codebase-analyzer` to generate one. If
that skill is unavailable in the current environment, degrade to a lightweight
read-only scan of README, routes, and API entry points, and mark every entry
derived this way as `confidence: low`.

## Protocol

### Step 1 — Read existing feature context

Before proposing any name, read what already exists:

1. Scan `docs/pm/**/PRD.md` and collect every existing `feature_path`,
   `parent_feature`, and `feature_level`. For legacy single-level PRDs
   whose frontmatter has no `feature_path`, apply the feature-path-contract
   fallback: treat `docs/pm/{feature}/PRD.md` as `feature_path={feature}`,
   `parent_feature=N/A`, `feature_level=1`.
2. Read README and any feature-level docs for business vocabulary.
3. Load the Project Profile and its `feature_inventory` entries.

Existing feature paths — explicit or derived through the legacy fallback —
are authoritative: evidence that maps to an existing feature must reuse its
`feature_path`, never fork a parallel top-level directory.

### Step 2 — Draft the feature catalog

Produce a draft catalog, explicitly labeled as pending confirmation. Each
entry contains:

```yaml
- candidate_feature: <human-readable business capability>
  suggested_feature_path: <lower-kebab path or unresolved>
  parent_feature: <existing parent path or N/A or unresolved>
  feature_level: <segment count or unresolved>
  evidence:
    routes: []
    pages: []
    api_endpoints: []
    services: []
    data_models: []
    background_jobs: []
    tests: []
    docs: []
  confidence: high | medium | low
  open_questions: []
  related_code_paths: []
```

Naming principles:

- Name features by business capability a user can understand; do not copy
  code directory names mechanically.
- Code directories, routes, APIs, and data models are evidence only.
- Legacy single-level feature directories stay valid as level-1 features;
  propose `feature_path`, `parent_feature`, and `feature_level` backfill only
  for entries being created or substantially updated.

### Step 3 — Confirmation gate

Present the draft and stop:

- Ask the maintainer to confirm, rename, merge, or drop candidate entries.
- If parent ownership or monorepo scope is unclear, output `blocked` with the
  single smallest clarification question. Do not create a new parallel
  top-level directory and do not guess.
- Never batch-generate PRDs from the draft, and never write the formal
  catalog document before confirmation.

### Step 4 — Write the confirmed catalog

After the maintainer confirms the `feature_path` set, write
`docs/pm/FEATURE_CATALOG.md` containing the confirmed feature tree, each
feature's evidence and confidence, and any remaining unresolved entries kept
in a pending section. Follow the catalog template in
`_internal/INSTRUCTIONS.md`.

### Step 5 — Handoff to the spec chain

For each confirmed feature the user wants documented:

- Hand off to `prd-gen` (via `pm-agent:idea-to-spec`) to create or update
  `docs/pm/{feature_path}/PRD.md` and `DECISIONS.md`. This skill supplies the
  confirmed context; it does not write PRD content itself.
- After the PM docs are confirmed, state the explicit handoff to
  `engineer-agent:trd-gen` to mirror `docs/engineer/{feature_path}/TRD.md`.

Every handoff packet must include `feature_path`, `feature`,
`parent_feature`, `feature_level`, and `feature_path_evidence`.
`feature_path_evidence` follows the shared handoff contract: a list of
`{source, reason}` entries derived from the confirmed catalog entry — merge
each non-empty evidence category into one entry whose `source` is a
representative path and whose `reason` explains why it proves the path, and
keep one entry citing `docs/pm/FEATURE_CATALOG.md`. The full per-category
evidence object stays in the catalog document referenced by the packet's
`source_catalog` field; never inline it as `feature_path_evidence`.

If a handoff target skill (`codebase-analyzer`, `idea-to-spec`/`prd-gen`, or
`trd-gen`) is missing in the current environment, stop at the confirmed
catalog, state which handoff target is unavailable, and describe the required
next step instead of performing that role's work yourself.

## Handoff Boundaries

| Concern | Owner |
| --- | --- |
| Tech stack, conventions, `feature_inventory` scan | `engineer-agent:codebase-analyzer` |
| Feature catalog draft, confirmation gate, `docs/pm/FEATURE_CATALOG.md` | `feature-catalog` (this skill) |
| Requirement shaping, PRD/BRD/DECISIONS creation and updates | `pm-agent:idea-to-spec` (`prd-gen`) |
| Engineer TRD mirroring under `docs/engineer/{feature_path}/` | `engineer-agent:trd-gen` |

## Edge Cases

- **Legacy project with no docs**: build the draft entirely from code and
  README evidence; expect more `medium`/`low` confidence entries and surface
  open questions instead of forcing a complete tree.
- **Child feature under an existing parent PRD**: nest the suggested path
  under the existing parent `feature_path`; never propose the child as a new
  top-level feature.
- **Monorepo with unclear scope**: if the user has not said which app,
  package, or service to catalog, output `blocked` and ask one scope
  question before drafting.
- **Conflicting names between code and docs**: prefer the documented business
  name; record the code-side name inside evidence and open questions.
