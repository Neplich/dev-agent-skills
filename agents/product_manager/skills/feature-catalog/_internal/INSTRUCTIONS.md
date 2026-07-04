# Feature Catalog — Internal Instructions

Detailed execution guidance for the `feature-catalog` skill. The public
contract lives in `../SKILL.md`; this file defines how to merge evidence, name
features, decide blocked states, and format the catalog and handoff outputs.

## 1. Evidence collection order

1. Existing `docs/pm/**/PRD.md` frontmatter: collect `feature`,
   `feature_path`, `parent_feature`, `feature_level`. These are the
   authoritative names. For legacy single-level PRDs whose frontmatter has
   no `feature_path`, derive `feature_path={directory name}`,
   `parent_feature=N/A`, `feature_level=1` — the same fallback the
   feature-path contract scanner uses — and treat them as existing
   features when suggesting paths and parents.
2. Project Profile `feature_inventory` from
   `engineer-agent:codebase-analyzer`.
3. README and other docs for business vocabulary.
4. Direct code entry points only as a fallback: route tables, page
   directories, API definitions, service modules, schema/model files,
   scheduled jobs, and test names.

Never re-run a deep codebase scan yourself when a Project Profile is
available; consume it. When no profile exists, run the lightweight scan
directly and draft from it — do not block on a `codebase-analyzer` handoff.
Keep the scan read-only and shallow (entry points, not implementations) and
cap every entry derived only from it at `confidence: low`. Suggest running
`codebase-analyzer` first only when the repository clearly exceeds a shallow
scan (many services or modules, unfamiliar stack, unresolvable evidence
conflicts), and phrase it as a recommendation, not a blocker.

## 2. Merging evidence into candidate features

- One candidate feature = one business capability a user can describe in a
  sentence ("订单退款", "成员权限管理"), not one code directory.
- Merge evidence categories that serve the same capability: a route, its
  page, its API endpoints, the backing service, models, jobs, tests, and
  docs belong to a single entry.
- Split an entry when evidence shows two independently owned capabilities
  even if they share a module.
- Every entry keeps `related_code_paths` so maintainers can audit the
  mapping.

## 3. feature_path suggestion rules

- Reuse first: if evidence maps to an existing PRD feature — including a
  legacy PRD resolved through the fallback above — reuse its `feature_path`
  exactly; a sub-capability nests under it as
  `{parent_feature_path}/{child-slug}`.
- New level-1 paths are allowed only when the capability clearly has no
  existing parent and the maintainer will confirm it.
- All segments are lower kebab-case.
- `parent_feature` is the path minus its last segment, or `N/A` for level 1;
  `feature_level` equals the segment count.
- When parent ownership, monorepo scope, or capability boundaries are
  unclear: `suggested_feature_path: unresolved`, record the blocking question
  in `open_questions`, and never emit a guessed parallel top-level path.

## 4. Confidence rubric

| Confidence | Condition |
| --- | --- |
| high | Two or more evidence categories corroborate the capability, or an existing PRD already owns it |
| medium | A single evidence category, or naming inference across categories |
| low | Directory-name or dependency guesses only, or fallback shallow scan without a Project Profile |

## 5. Blocked conditions

Output `blocked` plus exactly one smallest clarification question when:

- monorepo scope (which app/package/service) is undetermined
- a candidate could belong to two existing parents
- documented names and code names conflict and neither side is clearly
  current
- the maintainer has not confirmed the draft and asks to proceed to formal
  documents anyway

While blocked: no `docs/pm/FEATURE_CATALOG.md`, no
`docs/pm/{feature_path}/PRD.md`, no handoff packets for unresolved entries.
Confirmed entries may proceed while unresolved entries stay pending.

## 6. Catalog document template

Write `docs/pm/FEATURE_CATALOG.md` only after maintainer confirmation:

```markdown
---
title: "Feature Catalog"
type: FEATURE_CATALOG
feature: "feature-catalog"
version: "0.1.0"
status: Confirmed
date: "<confirmation date>"
last_updated: "<last update date>"
generated_by: "feature-catalog"
---

# Feature Catalog

## Confirmed Features

| feature | feature_path | parent_feature | feature_level | confidence |
| --- | --- | --- | --- | --- |

### <feature name>

- feature_path: ...
- evidence:
  - routes / pages / api_endpoints / services / data_models /
    background_jobs / tests / docs: ...
- related_code_paths: ...
- notes: ...

## Pending / Unresolved

| candidate_feature | reason | open_questions |
| --- | --- | --- |
```

Update the existing file surgically on later runs; append newly confirmed
features and move resolved entries out of the pending section. Do not create
versioned copies.

## 7. Handoff packet template

For each confirmed feature handed to `prd-gen` or `engineer-agent:trd-gen`:

```yaml
handoff_packet:
  feature: <feature name>
  feature_path: <confirmed path>
  parent_feature: <parent path or N/A>
  feature_level: <segment count>
  feature_path_evidence:
    - source: docs/pm/FEATURE_CATALOG.md
      reason: Maintainer-confirmed catalog entry for this feature
    - source: <representative evidence path, e.g. src/api/refund.ts>
      reason: <evidence category and why it maps this capability to the path>
  source_catalog: docs/pm/FEATURE_CATALOG.md
```

`feature_path_evidence` uses the shared handoff contract shape: a list of
`{source, reason}` entries. Build it from the confirmed catalog entry by
merging each non-empty evidence category into one entry — `source` is a
representative path from that category, `reason` states the category and why
it proves the path — plus one entry citing the confirmed catalog itself. The
full per-category evidence object lives only in `docs/pm/FEATURE_CATALOG.md`,
referenced via `source_catalog`; do not inline it in the packet or invent a
second evidence format. Downstream skills reference this packet instead of
rebuilding their own evidence.

## 8. Output behavior

- Draft outputs always carry a visible "pending confirmation" label and end
  with the confirmation question or the single blocked question.
- Confirmation outputs state the catalog path, the confirmed feature list,
  and the next handoff target per feature.
- Keep responses evidence-first: every claim about an existing feature cites
  at least one code path or doc.
