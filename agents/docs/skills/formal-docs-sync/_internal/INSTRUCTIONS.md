# Formal Docs Sync — Internal Instructions

Detailed execution guidance for `formal-docs-sync`. The public contract lives
in `../SKILL.md`; this file defines node evidence, scope derivation,
current-state writing, backfill batching, change-map growth, and reporting.

## 1. Three-Node Protocol

| Node | Entry credentials and evidence | Product target output | MVP output |
| --- | --- | --- | --- |
| Feature delivery | Approved PRD; Confirmed TRD impact evidence from frontmatter `related_code` or the impacted modules/interfaces section; confirmed `IMPLEMENTATION_PLAN.md`; actual diff and tests | API, database, and design docs plus change-map updates | API docs and API `code_glob` entries only |
| Deployment verification | TRD deployment surface; deployment configuration; verification commands and results; environment differences | Operations runbook and necessary release-preparation entries | Future iteration; not part of MVP acceptance |
| Release | Release scope; verified version or tag; changelog and release-process documents; audit conclusion | Product manual; release-note content is produced by `pm-agent:release-notes-generator`, and sync only verifies that the existing release notes are placed under the formal site when present and agree with the version context | Future iteration; not part of MVP acceptance |

Existing-system backfill is the fourth execution mode in Section 3. It does not
require a feature implementation plan and shares the same evidence, writing,
map-growth, and confirmation disciplines.

## 2. Five-Step Synchronization Protocol

Run these steps for feature delivery, deployment verification, and release.

### Step 1: Establish the candidate impact scope

Start with the handoff and resolve candidate code scope in this order:

1. TRD frontmatter `related_code`, when present
2. the TRD impacted-module, interface, or deployment-surface sections
3. confirmed `IMPLEMENTATION_PLAN.md` scope entries
4. the actual diff

Use actual code, diff, tests, schemas, routes, deployment configuration, and
verification results to corroborate the scope. Process documents and formal
docs do not replace current code and test facts.

If all four impact-scope sources are absent, stop and send a gap packet to
`engineer-agent:trd-gen`. Name the missing impact evidence and affected node;
do not infer a scope ad hoc. If evidence conflicts, report each source and the
conflict, then stop before writing until the owning role resolves it.

### Step 2: Resolve affected formal docs

Read `docs/site/standards/change-map.yaml` and match the confirmed code paths
against its `code_glob` keys while applying each entry's `exclude` list. Read
only the matched `required_docs` and the indexes needed to locate them.

When no entry exists, select the target document type from the node protocol,
propose a target page and a new `code_glob`, and include both in the scope
confirmation. Do not broaden the request into unrelated documentation.

### Step 3: Confirm and write the bounded scope

Before writing, present:

- target node and accepted entry basis
- candidate code paths and globs
- formal pages to create or update
- evidence sources to verify each page
- explicit exclusions and unresolved discrepancies

Wait for maintainer confirmation. Then update only the confirmed affected
pages and preserve unrelated pages. Rewrite the body as the current stable
system state: remove statements superseded by current facts and do not append
a chronological "what changed in this update" narrative.

### Step 4: Read back and verify facts

Read back the generated or updated pages and compare every material claim with
the current evidence. Depending on the node, verify routes, methods, auth,
path/query/body parameters, schemas, response and error shapes, fields, tests,
deployment steps, commands, environment differences, and release/version
context.

For new or changed formal pages, use `last_verified_version: unverified` until
the audit capability verifies the complete affected set. Sync must not stamp a
release version. Unsupported or contradictory claims remain unresolved and
block completion of that page rather than being guessed.

### Step 5: Grow the map and report the handoff

Add or correct the confirmed change-map entries, then read the file and changed
pages back to verify:

- each glob matches the intended code scope
- exclusions narrow only their own glob
- every `required_docs` path exists and belongs to the confirmed scope
- map ordering and lists are stable

Report changed docs, evidence, map delta, unresolved discrepancies, and the
recommended next lifecycle node or collaboration owner.

## 3. Existing-System Backfill Protocol

Backfill creates a reviewed current-state API baseline in bounded batches.

1. **Prefer the feature catalog.** If a PM `feature-catalog` artifact exists,
   use its feature to code-path to owner relationships as the first scope map.
   Verify every referenced path against the current repository.
2. **Discover before proposing when no catalog exists.** Scan API entry points,
   schema definitions, handlers, and contract tests to form a candidate module
   list. Do not generate repository-wide docs from the scan.
3. **Split and confirm batches.** With a catalog, default to one catalog module
   per batch. Without one, default to one API surface, normally a top-level
   route group. A batch should cover about one business module or no more than
   roughly five API pages. For each batch, present its `code_glob` values,
   proposed API pages, evidence entry points, and out-of-batch scope, then wait
   for maintainer confirmation.
4. **Generate the current-state baseline.** For the confirmed batch only,
   extract real paths, methods, authentication, request parameters and bodies,
   success responses, error structures, and supporting tests. Mark unsupported
   claims unresolved instead of guessing them.
5. **Seed and read back the change map.** Write API `code_glob` seed entries in
   the same batch. Read them back and verify the globs match the intended code
   and `required_docs` point to the generated API pages.
6. **Report and request the next batch.** Report coverage, exclusions,
   unresolved evidence, and remaining candidate batches. Request confirmation
   before starting the next batch; never silently expand the confirmed scope.

If no reliable API fact can be established from routes, schemas, handlers, or
contract tests, stop before writing that page and report the batch as
unresolved with the evidence needed to continue.

## 4. Change-Map Write Rules

Apply these rules to `docs/site/standards/change-map.yaml`:

- Merge entries that use the same `code_glob`; do not create duplicate keys.
- Merge, deduplicate, and stably sort `required_docs`.
- Preserve an existing `trigger` and `exclude` unless confirmed evidence
  requires a scoped correction; make any correction visible in the map delta.
- Stably sort new list values so repeated execution does not reorder them.
- Never delete unknown or manually maintained entries merely because the
  current scope did not produce them.
- Treat every `required_docs` path as repository-root relative.
- An `exclude` list narrows only the entry that owns it.
- Exclude `docs/site/.meta/**` from formal-page discovery, navigation,
  frontmatter processing, and `required_docs` update decisions. `.meta/` is a
  machine-consumption area, not a formal documentation page set.

After every write, parse and read back the map rather than relying only on the
edit operation's success.

## 5. Latest-State (Current-State) Discipline and Trust Model

Follow the shared consumption contract maintained by pm-agent at:

`agents/product_manager/skills/idea-to-spec/_internal/_shared/consumption-contract.md`

Apply its trust model while producing formal docs:

- Use formal documentation as a map to relevant context, while treating code
  and tests as ground truth for current behavior.
- If a document claim conflicts with code or test facts, preserve the document
  path, claim, code fact, and impact in the discrepancy report. Do not let the
  document override the fact and do not silently ignore the conflict.
- Compare `last_verified_version` with the current version context. If the
  anchors differ or cannot be compared, lower trust and broaden code/test
  verification instead of rejecting the document outright.
- Treat `last_verified_version: unverified` as the lowest-trust state and
  verify every material claim against code or tests.

Write pages as latest/current state:

- State stable behavior, interfaces, constraints, and operations directly.
- Replace obsolete claims when current evidence supersedes them.
- Do not add implementation diaries, ticket timelines, author conversations,
  or "before/after" release narration to a formal reference page.
- Keep uncertainty explicit as an unresolved item with its required evidence
  and owner; never turn an assumption into a current-state fact.

## 6. Missing-Site Behavior

Before proposing writes, verify that the host has the formal documentation
foundation under `docs/site/`, including its standards and change map. If it is
absent, explain that synchronization cannot safely write into an undefined
site structure and offer an explicit `docs-site-bootstrap` handoff.

Do not initialize the site, copy a scaffold, or create partial formal-doc paths
without the user's explicit bootstrap request and the bootstrap specialist's
own gate.

## 7. Per-Batch Report

Use this minimum report shape after each synchronization scope or backfill
batch:

```markdown
## Formal docs sync result

- Mode / node: <feature | deployment | release | backfill>
- Confirmed scope: <code paths, globs, pages, exclusions>
- Changed docs: <paths or none>
- Evidence: <code, tests, deployment, or release sources checked>
- Change-map delta: <added, merged, corrected, or none>
- Read-back verification: <glob and required-doc result>
- Unresolved discrepancies: <claim, fact, impact, owner, unblock evidence>
- Coverage and remaining gaps: <completed and deferred surfaces>
- Recommended next step: <next batch, lifecycle node, or collaboration owner>
```

Do not begin the next backfill batch from this report without maintainer
confirmation. Role-level `auto-continue` may automate cross-role handoff, but
it does not waive the specialist's explicit per-batch confirmation gate.
