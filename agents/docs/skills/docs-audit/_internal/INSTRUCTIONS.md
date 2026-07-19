# Docs Audit — Internal Instructions

Detailed execution guidance for `docs-audit`. The public entry and release
gates live in `../SKILL.md`; this file defines two-phase baseline resolution,
the deterministic and factual layers, report persistence, unified stamping,
and release handoff.

## 1. Resolve Inputs and Audit Phase

Resolve the three independent audit inputs before computing impact:

1. Resolve `base_ref`, the code-comparison start. Use the caller-supplied ref
   when explicit; otherwise use the most recent release tag. It is a Git ref or
   commit only and does not describe publication state.
2. Resolve `target_ref`, the code-comparison end. Use the caller-supplied ref
   when explicit; otherwise use pending-release `HEAD`. It is a Git ref or
   commit only and is not the target release version.
3. Include confirmed working-tree changes when they are explicitly part of the
   audit scope.
4. Resolve `target_release_version` independently. It is the exact version
   whose documentation is being audited and the pre-tag unified-stamp anchor.
   A maintainer must confirm it explicitly; do not infer it from a ref, branch,
   filename, package metadata, or surrounding context, and do not accept
   `unknown`. The matching tag does not need to exist during pre-tag audit.

If `target_release_version` is missing, inferred, `unknown`, or lacks explicit
maintainer confirmation, return `blocked` before report persistence or any
write. If a default ref cannot be resolved, name the missing ref rather than
inventing a commit range.

Select exactly one phase:

- **Pre-tag:** tag creation is still pending. Run Sections 2-6 and return
  `ready_for_tag` only after the complete affected set and every required
  release-version surface pass.
- **Post-tag:** the actual tag exists. Run Section 7 against the persisted,
  still-valid pre-tag record. Do not rerun generation or unified stamping.

An existing tag normally selects post-tag. One narrow exception permits
pre-tag re-entry: post-tag has already classified the tag's content binding as
drifted, the maintainer has explicitly selected one of the remediation paths
in Section 7, and any required tag deletion or movement is performed by the
host maintainer outside docs-audit. Record that selection and the resulting
tag state before starting the complete pre-tag protocol; docs-audit never
deletes, moves, or creates a tag.

When no confirmed release version exists, a read-only diagnostic fact review
may still describe the affected pages, but the audit result remains `blocked`:
it cannot persist a versioned audit report, produce a phase success, or alter
stamps. Existing values remain unchanged and new pages remain `unverified`,
preserving issue #118 semantics.

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

Pages under `docs/site/standards/templates/**` are reusable template artifacts
with placeholder bodies. Keep them in the affected set for frontmatter and
structural-completeness validation, but do not perform the target `doc_type`'s
type-specific fact checks against their placeholder content. Template
placeholders alone never block a release.

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
valid frontmatter to the fact layer, except template artifacts under
`docs/site/standards/templates/**`, which proceed only to template structure
validation. `suspect` is a review priority label, not a fourth final status.

## 3. Fact Layer

Do not apply this layer's type-specific fact checks to
`docs/site/standards/templates/**`. For those reusable placeholder artifacts,
verify only the shared frontmatter contract and the expected template
structure; their target `doc_type` describes the page they help authors create,
not factual API, schema, deployment, or operations claims made by the template
itself. A placeholder value or absent implementation evidence in a template is
not a release blocker.

For every non-template affected page that is not already `stale` from invalid
frontmatter, build a claim-to-evidence checklist. Follow the shared trust model:

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

## 4. Pre-tag Audit

Run the pre-tag protocol in this order:

1. Confirm `base_ref`, `target_ref`, and the maintainer-confirmed
   `target_release_version` as separate inputs.
2. Use the complete `base_ref..target_ref` endpoint diff plus any explicitly
   included working-tree scope to resolve the full affected-page set through
   the deterministic layer.
3. Verify every affected document through the fact layer. Also verify the
   issue #116 ready handoff and its confirmed Release Notes page, the host's
   Release Notes index, `docs/site/.meta/releases.json`, and host version facts
   against `target_release_version`. Audit verifies these release surfaces; it
   does not generate Release Notes or create or maintain release metadata.
4. Define the unified stamp set as the union of the complete affected-page set
   and every Markdown release-version surface verified by this run that carries
   `last_verified_version`, including the target-version Release Notes page and
   its Markdown index. Deduplicate paths. Non-Markdown release metadata and host
   version facts remain verified, hashed, read-only surfaces.
5. Record each unified-stamp page's current `last_verified_version` in the
   audit report before any stamp write. This is the historical baseline for
   this run; do not add `baseline_verified_version` or any other baseline
   frontmatter.
6. Only when every page in the unified stamp set is factually `verified`, all
   evidence is complete, and all release surfaces agree may Section 6 update
   every unified-stamp page's `last_verified_version` together to
   `target_release_version`.
7. Permit that unified stamp even when no matching tag exists yet.
8. After read-back proves the complete stamp, compute SHA-256 over the exact
   post-stamp bytes of every unified-stamp page and every other file-backed
   release-version surface,
   including the confirmed Release Notes page, its version index,
   `docs/site/.meta/releases.json`, the issue #116 handoff when file-backed,
   and each file backing the host version facts.
9. Atomically replace the same persisted pre-tag record with the successful
   stamp result: unified-stamp page list, each page's pre-stamp and post-stamp
   `last_verified_version`, post-stamp page hashes, other release-surface
   hashes, audited `target_ref`, final `ready_for_tag`, and result time.
10. Stage the complete unified-stamp set and that successful audit-record update
    together and create one ordinary commit on the host release PR branch (the
    **post-stamp commit**). The stamp and successful record must be introduced
    by that same commit, not left only in the working tree or split across
    commits. After Git creates the commit, persist a trusted pre-tag handoff
    anchor containing the post-stamp commit SHA, its resolved Git tree hash,
    the record path, and that path's Git blob hash. The committed record itself
    must contain every unified-stamp page's post-stamp content hash; it cannot
    self-contain its own commit or tree identity. Read the record back from the
    anchored commit with `git show <post-stamp-commit>:<record-path>`, verify its
    blob hash and the handoff's commit/tree anchor, and only then return
    `ready_for_tag`. A working-tree state is never a valid anchor. This means
    ready for tag creation, never already published or released.

Return `blocked` with no stamp when any of the following is true:

- `target_release_version` is missing;
- the target version was inferred from a branch name, `target_ref`, or context;
- the target version is `unknown`;
- the target version lacks explicit maintainer confirmation;
- any affected page is `stale`, `mismatch`, remains unverified after fact
  review, or lacks sufficient evidence; or
- Release Notes, the version index, release metadata, or host version facts do
  not match `target_release_version`.

Here, “remains unverified” is a factual verification outcome caused by missing
evidence; the valid frontmatter value `last_verified_version: unverified` does
not itself make a page stale or block it from becoming factually `verified`.

Never stamp only a `verified` subset. If `target_release_version` changes after
the audit, the report, unified stamp conclusion, and `ready_for_tag` result are
immediately invalid; rerun the complete pre-tag audit for the new value.
If stamping, page read-back, hashing, atomic record replacement, post-stamp
commit creation, or committed-record read-back fails, return `blocked`. The persisted record may retain
diagnostic or pre-stamp evidence, but it must not contain a successful stamp
conclusion, `ready_for_tag`, or a success time.

### Final page status

Assign final statuses from this table after fact verification:

| Status | Decision rule | Pre-tag effect |
| --- | --- | --- |
| `verified` | Every material declaration has current code or test evidence and no omission was found. | Eligible for unified-set evaluation; stamp only when every page in the unified stamp set is verified. |
| `stale` | Fact-layer review confirms that a material declaration is no longer synchronized with current code, or a frontmatter field is invalid. An older release anchor or `unverified` only lowers trust and broadens verification; it is advanced by unified stamping after the complete unified stamp set is verified. | Blocked; synchronize and re-audit the documentation. |
| `mismatch` | A document declaration directly conflicts with current code or test fact. | Blocked; confirm whether documentation or implementation must change, then re-audit. |

Any `stale`, `mismatch`, page that remains unverified after fact review, or
unresolved evidence gap blocks the release audit.
Return a concrete to-do item with an owner or required evidence for every
blocker. A complete set of `verified` conclusions is necessary but not
sufficient for `ready_for_tag`: all release-version surfaces must also agree
with the confirmed `target_release_version`.

## 5. Persist the Audit Report

Write the report under `docs/site/.meta/audit/` as
`audit-{target_release_version}.md`. The version comes only from the explicit,
maintainer-confirmed input. Do not derive the filename from a branch or ref.
Audit reports are in `.meta/` and do not require the standard seven-field
frontmatter.

Include at least:

```markdown
# Formal documentation audit

- Audit phase: pre-tag
- base_ref: <resolved base ref and commit>
- target_ref: <resolved target ref and commit>
- target_release_version: <maintainer-confirmed version>
- Diff semantics: <two-dot endpoint diff or explicitly requested three-dot merge-base diff>
- Changed files: <name-status inventory>
- Change-map matches: <file, code_glob, exclude, trigger, required_docs>

## Change-map changes

<added, deleted, and modified entries; reasons and sources for deletions or narrowing; blockers or none>

## Per-document evidence

<page, pre-stamp last_verified_version, claims, code/test evidence, impact, deterministic findings, final status>

## Release-version surfaces

<#116 handoff, Release Notes, version index, releases.json, and host version facts; persist each file-backed path and its exact-byte SHA-256>

## Successful unified stamp record

- Hash algorithm: SHA-256 over exact file bytes
- Audited target_ref: <resolved target_ref commit>
- Record path: <repository-relative audit record path committed with the stamp>
- Stamped pages: <path, pre-stamp last_verified_version, post-stamp last_verified_version, post-stamp SHA-256>
- Release-surface content evidence: <surface, path, post-stamp SHA-256>
- Stamp read-back: <complete / failed>
- Committed record read-back: <git show from post-stamp commit complete / failed>
- Ready result time: <timestamp written only on success>

## Conclusion

- Status summary: <verified / stale / mismatch counts and evidence gaps>
- Blocking items: <to-do list or none>
- Phase result: <ready_for_tag or blocked; success is written only after stamp, hashes, atomic replacement, and read-back succeed>
- Review commands: <commands sufficient to reproduce diff, validation, and evidence checks>
```

Read the report back after writing and verify the three independent inputs,
inventory, pre-stamp baselines, release surfaces, evidence, statuses, blockers,
commands, and phase result.

After the ordinary post-stamp commit is created, persist its commit SHA, tree
hash, this record path, and this record's Git blob hash in the trusted pre-tag
handoff. This external anchor avoids a Git self-reference: the record cannot
contain the identity of the commit or tree that contains the record.

## 6. Unified Version Stamp

Stamp only during a valid pre-tag audit and only when all conditions are true:

1. every page in the unified stamp set has a final `verified` conclusion
   and there is no unresolved evidence gap; and
2. Release Notes, the version index, `docs/site/.meta/releases.json`, and host
   version facts all match the maintainer-confirmed `target_release_version`.

Then, in one audit operation:

- update every page in the unified stamp set (the affected-page set union all
  verified Markdown release surfaces carrying `last_verified_version`) from
  `unverified` or an older anchor to `target_release_version`; and
- read all unified-stamp pages back to verify that the complete stamp is consistent;
- hash the exact post-stamp bytes of every unified-stamp page and file-backed
  release-version surface; and
- atomically write the successful stamp fields and `ready_for_tag` result back
  to the same pre-tag record; and
- commit the full stamp set and successful record together as one ordinary
  post-stamp commit on the host release PR branch, then verify the committed
  record and persist the trusted handoff tuple `(post-stamp commit SHA, tree
  hash, record path, record blob hash)`. Do not use an uncommitted working tree
  as the successful record anchor.

Do not stamp a verified subset when another page is `stale`, `mismatch`, or
blocked by `unverified` or missing evidence. The matching tag is not required
for this pre-tag write. Do not modify `.meta/releases.json`; issue #116 owns
that content, while this audit only verifies it. Outside a valid pre-tag audit,
keep each page's existing value; new pages remain `unverified`, and the field
must not be omitted.

## 7. Post-tag Audit

Run the post-tag protocol in this order:

1. Read the actual tag and resolve its peeled commit; a missing tag or
   unresolvable tag commit is a blocker.
2. Take the post-stamp commit SHA from the trusted pre-tag handoff and read the
   persisted pre-tag record from that anchor with
   `git show <post-stamp-commit>:<record-path>`. Do not use the working-tree
   record or a later revision as the authority. If the current-path copy differs
   from the committed record, report the difference and continue with the
   committed record. Require the exact fields written by the successful pre-tag
   path: `base_ref`, audited `target_ref` commit,
   `target_release_version`, unified-stamp page list, per-page
   pre/post `last_verified_version`, every post-stamp page and release-surface
   SHA-256, `ready_for_tag`, and its result time. Missing fields are evidence
   gaps, not values to reconstruct from current files. Independently require
   the trusted handoff's post-stamp tree hash, record path, and record blob hash;
   verify that the `git show` bytes match that blob before consuming the record.
3. Bind the tag commit to the recorded audited content:
   - Fast path: resolve the peeled tag commit's Git tree hash. Binding holds
     only when that tree hash equals the recorded post-stamp tree hash. Commit
     identity alone is not a separate fast-path condition.
   - General path: at the peeled tag commit, read every recorded affected page
     and release-surface path (for example with
     `git show <tag-commit>:<path>`), recompute SHA-256 over those exact bytes,
     and require every path and hash to match the pre-tag record exactly.
   Use the general path whenever the fast path does not establish binding;
   never compare only the tag name and version strings.
4. Verify that the actual tag name, `target_release_version`, confirmed Release
   Notes, version index, `docs/site/.meta/releases.json`, and host version facts
   also match exactly.
5. Return `release_verified` only when content binding succeeds, the pre-tag
   record remains valid, and all evidence is complete and consistent.
6. Return `blocked` when any recorded path is missing or any content hash
   drifts, including when the tag name is correct. The report must present two
   maintainer-selected remediation paths: (a) the host maintainer deletes or
   moves the incorrect tag, reruns the complete pre-tag audit with the same
   `target_release_version`, and the old record is marked `superseded`; or (b)
   the maintainer abandons that version, confirms a new
   `target_release_version`, and reruns the complete pre-tag audit. docs-audit
   records and adjudicates the selected path only; it never deletes, moves, or
   creates a tag. Also return `blocked` when the tag is missing, the pre-tag
   record was invalidated, or evidence is missing.

Post-tag audit performs final consistency verification only. Do not regenerate
Release Notes, indexes, release metadata, documentation, GitHub Release
content, or unified stamps.

Persist or append a post-tag section to the same audit record without erasing
the pre-tag evidence. Record the actual tag, checked surfaces, evidence,
blockers, review commands, and `release_verified` or `blocked` result.

## 8. Release Handoff and Responsibility Boundaries

Return the persisted audit report and exactly one phase result:

- **`ready_for_tag`:** pre-tag audit passed and the complete unified stamp set
  was stamped to `target_release_version`; do not call the version published.
- **`release_verified`:** post-tag audit proved the actual tag and all release
  surfaces match the still-valid pre-tag record.
- **Blocked:** list every `stale`, `mismatch`, and evidence-gap item with the
  document, fact, impact, required action, and responsible owner when known.

Issue #116 owns Release Notes generation and confirmation, its index and
required navigation, and release metadata content; consume its ready handoff
as evidence. Issue #118 owns the shared frontmatter contract, including the
required `last_verified_version` field and `unverified` value. Issue #120 may
prepare a GitHub Release draft only after `ready_for_tag`, and may publish only
after the actual tag exists, this audit returns `release_verified`, and the
maintainer approves publication. The host repository owns target-version
confirmation, tag creation, deterministic CI, and release execution.

This audit does not generate Release Notes, maintain `.meta/releases.json`,
create or publish a GitHub Release, create or move tags, modify an AI Hub
workflow, invent a dynamic host-version schema, or treat
`last_verified_version` as publication state. Route documentation repair to
`formal-docs-sync`, product ambiguity to `pm-agent`, and implementation
ambiguity to the appropriate engineering owner; wait for confirmation unless
applicable `auto-continue` authorization already exists.
