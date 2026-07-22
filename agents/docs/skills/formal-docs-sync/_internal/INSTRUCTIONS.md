# Formal Docs Sync — Internal Instructions

Authoritative common execution entry for `formal-docs-sync`. The public entry
gate and mode selection live in `../SKILL.md`. This file defines the common
eight-step host-site contract and routing to type-specific modules.

## Progressive Loading

After resolving the mode, identify the confirmed target document types. For a
single-type task, read this file plus exactly one matching module:

| `doc_type` | Type module |
| --- | --- |
| `api` | `types/api/INSTRUCTIONS.md` |
| `database` | `types/database/INSTRUCTIONS.md` |
| `design` | `types/design/INSTRUCTIONS.md` |
| `ops` | `types/ops/INSTRUCTIONS.md` |
| `product` | `types/product/INSTRUCTIONS.md` |

For a confirmed multi-type scope, load only the modules that occur in that
scope. Do not read the other type modules. The host files under
`docs/site/standards/templates/` are the only template source; these modules
contain evidence and output rules, not duplicate template bodies.

## Common Eight-Step Host-Site Contract

Run all eight steps in order for every mode.

### 1. Read the host standards entry

Verify the host already has `docs/site/`, its standards, and
`docs/site/standards/change-map.yaml`. Read
`docs/site/standards/index.md` or the host's equivalent standards entry before
proposing writes. If the foundation is absent, stop with zero site writes and
offer a `docs-site-bootstrap` handoff; do not create a partial site.

### 2. Read only the target-type templates and modules

For each confirmed target type, follow the host standards entry to its
corresponding file under `docs/site/standards/templates/`, then load the one
matching type module above. The host template, including its unique
`docs-scaffold` block, is authoritative. Never embed, reconstruct, or maintain
a second template body in this skill.

When a confirmed new page is needed and the host exposes `npm run new:doc`,
prefer that deterministic scaffold entry. Supply only confirmed frontmatter,
path, and optional change-map inputs; do not use it for Release Notes.

### 3. Apply the change map

Resolve candidate impact scope from the confirmed evidence chain in this
order when available: TRD `related_code`, TRD impacted modules/interfaces or
deployment surface, confirmed implementation-plan entries, then the actual
diff. Corroborate with current code, tests, schema, configuration, and command
results.

Read `docs/site/standards/change-map.yaml`, match confirmed code paths against
`code_glob`, and apply each entry's own `exclude`. Read only matched
`required_docs` and necessary indexes. If no mapping exists, propose the target
page, code glob, trigger, required docs, and exclusions together; do not infer
a wider site scope.

Merge entries with the same `code_glob`; preserve unknown fields and unrelated
entries; deduplicate and stably sort lists. An exclusion narrows only its own
glob. Treat repository-relative page paths as required, and exclude
`docs/site/.meta/**` from formal-page discovery and change-map targets.

### 4. Confirm the bounded candidate scope

Before writing, show the maintainer:

- selected mode and accepted entry basis;
- candidate pages and types;
- code paths and globs;
- evidence for each page;
- feature owner or owning team when the feature catalog provides one;
- proposed change-map, index, or host-required navigation delta;
- explicit exclusions, unresolved discrepancies, and out-of-batch scope.

Wait for confirmation. Treat every page and its corresponding change-map entry
as one atomic confirmed scope. Existing-system backfill runs one finite batch
at a time and requires a new confirmation before the next batch.

### 5. Write only the confirmed scope and read it back

Create or update only confirmed pages, their map entries, and necessary
indexes or host-required navigation. Preserve unrelated and manually
maintained content. Write the stable current state, replacing superseded
claims; never add implementation diaries, ticket timelines, before/after
narration, or unsupported future state.

Read every changed page and map entry back. Verify that page paths exist, map
globs and exclusions have the intended reach, lists are stable, and every
material statement is supported. Contradictory or missing evidence is a
blocker, not permission to guess.

### 6. Apply the shared contract and leave pages unverified

Read and consume, without redefining it:

`agents/docs/skills/docs-agent/_internal/_shared/frontmatter-contract.md`

Apply that contract to every created or updated formal page. Set
`last_verified_version: unverified` on every new or changed page. This skill
must not stamp a release version, redefine frontmatter fields, or add a dynamic
host schema.

### 7. Run host documentation checks

Read required commands from the host `docs/site/package.json`, repository
guidance, or CI. Run all host-required docs checks and record command, working
directory, exit status, and result. For an AI Hub-shaped VitePress host, run
`npm run test:docs` in `docs/site/`. Do not migrate or reproduce AI Hub-specific
non-VitePress logic.

If required dependencies are absent, use only the host's deterministic locked
installation path. A failed, missing, or unverifiable required check blocks
completion; do not repair unrelated code or deployment state to hide it.

After host checks pass for an existing-site content batch, and before the audit
handoff, run the shared documentation-site deployment completeness recheck.
This remains read-only even when the content update did not intentionally touch
deployment files. Reuse the shared status and checklist, report unchanged
`integrated` evidence or drift, and do not create a second protocol here.

### 8. Handoff to docs audit

After all required checks pass, hand the complete affected set and evidence to
`docs-agent:docs-audit` (issue #117). Enter pre-tag audit only when a maintainer
has explicitly confirmed `target_release_version`; include that value and its
confirmation source in the handoff. Otherwise keep every changed page
`last_verified_version: unverified`, return a blocked handoff that explicitly
waits for confirmed release context, and never infer a version from refs,
branch names, or other context. A sync report is not a stamp or release
authorization. If checks fail, return a blocked handoff with the exact evidence.

## Mode Rules

### Feature delivery

Synchronize only implementation-affected API, database, design, and product
pages and their confirmed map/index/navigation deltas. A page is applicable
only when its type module's evidence checks pass. Design pages also require the
Design Delivery Closeout Gate below.

### Deployment verification

Synchronize ops runbooks, upgrade instructions, rollback instructions,
environment variables, startup methods, Helm/Compose behavior, and related
current operational facts only when confirmed configuration, commands, results,
and environment differences support them. Never turn a deployment plan or an
unexecuted command into current state.

### Release

Synchronize only affected product and ops pages and reconcile their material
claims with the confirmed release version evidence. Do not generate or edit a
Release Notes body, its index, `.meta/releases.json`, or Release Notes
navigation. Handoff all such work to `docs-agent:release-notes-generator`
(issue #116). For a direct Release Notes request, stop with zero site writes
and pass the confirmed version, scope, evidence, and requested site surfaces to
that specialist immediately; do not ask for separate permission to perform
the routing handoff. Do not prepare or operate a GitHub Release.

### Existing-system backfill

Support finite confirmed batches for all five types. Prefer a PM feature
catalog and the existing change map. Without a mapping, bounded discovery may
propose one coherent page group plus its map entries, but must not expand into
a repository-wide scan or full-site generation. Preserve the feature owner or
owning team from the catalog in the proposed batch when present. Execute one
confirmed batch, report remaining candidates, and wait for confirmation before
another batch.

## Design Delivery Closeout Gate

Before proposing a feature-delivery write to `docs/site/design/**`, verify all
of the following for the same `feature_path`:

1. Approved PRD;
2. Confirmed TRD with traceable impacted modules or `related_code`;
3. confirmed `IMPLEMENTATION_PLAN.md`;
4. all plan scope complete, with no pending, blocked, deferred, TODO, or stub;
5. actual code and diff cover the plan and TRD impact scope;
6. every required test, including applicable QA/E2E evidence, ran and passed;
7. the Step 4 candidate scope is confirmed.

Reuse `feature-implementor` closeout evidence; do not invent another format.
If any item is absent, conflicting, failed, skipped without explanation, or
unverifiable, report the failed item, owner, and next action and make zero
changes to both the design page and its change-map entry. A passing gate still
permits only current-state design evidenced by final code and passing tests.

## Trust and Boundaries

Follow the trust model in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/consumption-contract.md`:
formal docs guide discovery, while current code and tests are ground truth.
Lower trust for an older or `unverified` page and broaden verification. Preserve
document claim, code/test fact, evidence path, and impact for discrepancies.

This specialist does not define frontmatter, stamp versions, initialize or
deploy a site, edit Release Notes surfaces, create or move tags, create or
publish GitHub Releases, publish images, update Helm, deploy software, copy AI
Hub paths or business facts, migrate AI Hub non-VitePress logic, or introduce
dynamic schemas. It does not create duplicate type specialists.

## Report Shape

After each scope or backfill batch, report:

```markdown
## Formal docs sync result

- Mode: <feature delivery | deployment verification | release | existing-system backfill>
- Confirmed scope: <pages, code paths, globs, exclusions>
- Loaded type modules: <api / database / design / ops / product>
- Changed docs: <paths or none>
- Evidence and read-back: <sources checked and result>
- Change-map / index / navigation delta: <delta or none>
- Host docs checks: <commands, cwd, and results>
- Deployment completeness: <shared status, variants, evidence paths, missing
  links or drift, user decision, and next owner>
- Unresolved discrepancies: <items, owners, next evidence or none>
- Coverage and remaining batches: <summary>
- Handoff: <docs-audit (issue #117) ready, or blocked while waiting for confirmed
  target_release_version; include its maintainer confirmation source when
  available, or
  release-notes-generator (issue #116) with the confirmed version, scope,
  evidence, and requested site surfaces when applicable>
```
