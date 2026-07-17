# Docs Audit — Internal Instructions

Detailed execution guidance for `docs-audit`. The public entry and release
gates live in `../SKILL.md`; this file defines baseline resolution, the
deterministic and factual layers, report persistence, unified stamping, and
release handoff.

## 1. Resolve Base, Target, and Version Anchor

Resolve the audit baseline before computing impact:

1. Use caller-supplied base and target when both are explicit and confirmed.
2. Otherwise use the most recent release tag as base and the pending-release
   `HEAD` as target.
3. Include confirmed working-tree changes when they are explicitly part of the
   audit scope.
4. Resolve the stampable version anchor independently from the diff endpoints:
   use the confirmed tag or GitHub Release for the pending release.

If there is no tag, Release, or explicit version anchor, continue auditing the
confirmed working scope. Set `version_anchor: unavailable`, identify the real
target commit when one exists, and never substitute `unknown`, a branch name,
or an inferred version. Do not stamp `last_verified_version` or write release
metadata without a usable tag or Release anchor. Existing pages retain their
current `last_verified_version`; new pages use `unverified`, and the field must
never be omitted.

Record the exact resolved base and target in the report. If a default base
cannot be resolved, state that directly rather than inventing a commit range;
use the confirmed working-scope evidence available for the audit.

## 2. Deterministic Layer

Run all six steps in order.

### Step 1: Compute changed files

Run or reproduce the semantics of:

```bash
git diff --name-status <base> <target>
```

Preserve change status and path. Add only those working-tree changes that were
confirmed as part of the scope. The combined set is the report's changed-files
inventory. Use the two-dot endpoint diff by default. Only when the caller
explicitly requests merge-base semantics, use
`git diff --name-status <base>...<target>` and state that three-dot semantic in
the report.

### Step 2: Match change-map entries

Parse `docs/site/standards/change-map.yaml`. When the change-map itself is in
the changed-files inventory, read its base and target versions and compare
entries by `code_glob`, recording every added, deleted, and modified mapping.
Match changed files against the union of base and target `code_glob` entries so
that a deleted or narrowed old entry still participates in this audit's impact
set. For every matched entry, apply that version's optional `exclude`; an
exclusion narrows only its owning `code_glob` and does not cancel another
matching entry. Record the changed file, map version, matched glob, trigger,
applied exclusions, and resulting match.

When the change-map delta adds a mapping or expands an entry's `required_docs`,
add every newly mounted required document directly to the affected-page set for
fact-layer review, even when no code file changed. A missing document or invalid
frontmatter is an evidence gap; a declaration proven out of date is `stale`.
Reporting only the map delta is not sufficient to release.

Treat the change-map delta itself as audit evidence. The report must include a
dedicated change-map changes section with each added, deleted, or modified
entry. For a deleted or narrowed entry, cite the reason and its source, such as
evidence that the corresponding code was deleted. A mapping narrowing without
a reasonable, verifiable source is a blocking item.

### Step 3: Resolve required documents

Union the matched entries' repository-root-relative `required_docs`,
deduplicate them, and check whether each page was updated in the same combined
diff. A required page that was not updated is a `suspect` for fact-layer
review, not an immediate `stale` conclusion.

### Step 4: Include documentation-only changes

Add every changed formal Markdown page under `docs/site/**/*.md` directly to
the affected-page set, excluding `docs/site/.meta/**`. This rule applies even
when there is no changed code or change-map match, so a documentation-only
claim cannot bypass fact verification.

Use each such page's frontmatter `related_code` to bound its code and test
evidence. The field must be a non-empty string array for every page, and the
audit always uses it to bound the code and test evidence scope. A missing or
empty `related_code` field is invalid frontmatter and makes the page `stale`
in Step 5.

### Step 5: Validate frontmatter

Validate every affected formal Markdown page and explicitly exclude
`docs/site/.meta/**`. The authoritative field rules live in
`agents/docs/skills/docs-agent/_internal/_shared/frontmatter-contract.md`.
Check the seven required fields and their constraints:

| Field | Validation |
| --- | --- |
| `title` | non-empty string |
| `visibility` | `public`, `internal`, or `both` |
| `doc_type` | `landing`, `release`, `design`, `api`, `database`, `ops`, or `product` |
| `stage` | `draft`, `dev`, `ops`, or `release` |
| `owners` | non-empty string array |
| `related_code` | non-empty string array of repository-relative paths or globs for every `doc_type` |
| `last_verified_version` | non-empty version anchor string or `unverified`; always required, including when the host has no version anchor |

An invalid field, invalid enum, invalid `related_code`, or invalid
version field makes the page `stale` immediately. The literal `unverified` and
an older release anchor are valid version values, not `stale` conclusions. They
lower trust and require broader code and test verification; after the complete
affected set is `verified`, the unified stamp step advances them to the current
version anchor.

### Step 6: Classify deterministic findings

Keep invalid-frontmatter pages as `stale`. Mark a matched `required_docs` page
that was not updated in the same diff only as `suspect` and send it to the fact
layer. Also send directly changed formal pages and other affected pages with
valid frontmatter to the fact layer. `suspect` is a review priority label, not
a fourth final status.

## 3. Fact Layer

For every affected page that is not already `stale` from invalid frontmatter,
build a claim-to-evidence checklist. Follow the shared trust model:

`agents/product_manager/skills/idea-to-spec/_internal/_shared/consumption-contract.md`

Use formal docs as a map and current code and tests as ground truth. Preserve
the document path, exact material claim, code or test fact, evidence path, and
impact for every discrepancy. Do not let documentation override current facts
and do not silently ignore a conflict.

Review `suspect` pages first. Use the matched change-map entry's `trigger` as
semantic context, not as proof. If the change is a pure implementation
refactor or test-only change and every material declaration remains consistent
with current evidence, conclude `verified`; do not require a no-op document
edit merely because the map matched.

Documentation-only changes receive the same fact checks as code-triggered
pages. A changed assertion that conflicts with current behavior must be caught
even when the code diff is empty.

For every affected API page, verify at least:

- HTTP method and path
- authentication and authorization behavior
- path, query, and request-body parameters
- successful response status and body shape
- error status and error structure
- streaming behavior and file upload or download behavior, when applicable

Use routes, handlers, schemas, tests, and other direct implementation evidence.
For other document types, verify the material schema fields, environment
variables, deployment commands, and rollback steps that apply to the page.
When evidence is insufficient, record the evidence gap as a blocker and do not
guess a `verified` conclusion or stamp the affected set.

## 4. Final Status and Release Recommendation

Assign final statuses from this table after fact verification:

| Status | Decision rule | Release recommendation |
| --- | --- | --- |
| `verified` | Every material declaration has current code or test evidence and no omission was found. | Proceed for this item; stamp only when the complete affected set is verified. |
| `stale` | Fact-layer review confirms that a material declaration is no longer synchronized with current code, or a frontmatter field is invalid. An older release anchor or `unverified` only lowers trust and broadens verification; it is advanced by unified stamping after the complete affected set is verified. | Blocked; synchronize and re-audit the documentation. |
| `mismatch` | A document declaration directly conflicts with current code or test fact. | Blocked; confirm whether documentation or implementation must change, then re-audit. |

Any `stale`, `mismatch`, or unresolved evidence gap blocks the release audit.
Return a concrete to-do item with an owner or required evidence for every
blocker. A complete set of `verified` conclusions yields a proceed
recommendation for the audited scope. When its version anchor is unavailable,
keep the verified audit result but explicitly list establishing the release
anchor as outstanding release context; do not convert that gap into a fake
stamp.

## 5. Persist the Audit Report

Write the report under `docs/site/.meta/audit/`. Use:

- `audit-{version}.md` when a confirmed tag or Release version anchor exists;
- `audit-{target-short-sha}.md` when the version anchor is unavailable.

Use the real target commit's short SHA for the fallback. If the audited working
scope has no resolvable target commit, stop before inventing a filename and
report the missing target evidence. Audit reports are in `.meta/` and do not
require the standard seven-field frontmatter.

Include at least:

```markdown
# Formal documentation audit

- Base: <resolved base or unavailable>
- Target: <resolved target and short SHA>
- Version anchor: <tag/Release or unavailable>
- Diff semantics: <two-dot endpoint diff or explicitly requested three-dot merge-base diff>
- Changed files: <name-status inventory>
- Change-map matches: <file, code_glob, exclude, trigger, required_docs>

## Change-map changes

<added, deleted, and modified entries; reasons and sources for deletions or narrowing; blockers or none>

## Per-document evidence

<page, claims, code/test evidence, impact, deterministic findings, final status>

## Conclusion

- Status summary: <verified / stale / mismatch counts and evidence gaps>
- Blocking items: <to-do list or none>
- Release recommendation: <proceed or blocked>
- Review commands: <commands sufficient to reproduce diff, validation, and evidence checks>
```

In the stored report, use the machine-readable spelling
`version_anchor: unavailable` when no anchor exists, even if the surrounding
report is prose. Read the report back after writing and verify the endpoints,
inventory, evidence, statuses, blockers, and commands.

## 6. Unified Version Stamp

Stamp only when both conditions are true:

1. every page in the complete affected set has a final `verified` conclusion
   and there is no unresolved evidence gap; and
2. a confirmed tag or GitHub Release version anchor exists.

Then, in one audit operation:

- update every affected page's `last_verified_version` from `unverified` or an
  older anchor to the current tag or Release;
- synchronize `docs/site/.meta/releases.json` to the same verified version
  context, storing `verifiedDocs` as document-path keys mapped to verified
  version strings; and
- read all affected pages and release metadata back to verify that the stamp
  is complete and consistent.

Do not stamp a verified subset when another page is `stale`, `mismatch`, or
blocked by missing evidence. Do not partially update `.meta/releases.json`.
When the version anchor is unavailable, do not stamp
`last_verified_version` and do not alter release metadata. Keep each page's
existing value; new pages remain `unverified`, and the field must not be
omitted.

## 7. Release Handoff

Return the persisted audit report and one release recommendation:

- **Proceed:** every affected page is `verified`; identify whether unified
  stamping completed, or state that no stamp was written because the version
  anchor is unavailable.
- **Blocked:** list every `stale`, `mismatch`, and evidence-gap item with the
  document, fact, impact, required action, and responsible owner when known.

The audit conclusion is release-handoff evidence. It does not create release
notes, publish a release, or repair documentation or code on its own. Route
documentation synchronization to `formal-docs-sync`, product ambiguity to
`pm-agent`, and implementation ambiguity to the appropriate engineering
owner; wait for confirmation unless applicable `auto-continue` authorization
already exists.
