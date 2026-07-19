# Docs Audit — Internal Instructions

Detailed execution guidance for `docs-audit`. The public entry and release
gates live in `../SKILL.md`; this file defines two-phase baseline resolution,
the deterministic and factual layers, report persistence, unified stamping,
and release handoff.

## 1. Resolve Inputs and Audit Phase

Resolve the three independent audit inputs before computing impact:

1. Resolve `target_ref`, the code-comparison end. Use the caller-supplied ref
   when explicit; otherwise use pending-release `HEAD`. It is a Git ref or
   commit only and is not the target release version.
2. Resolve `target_release_version` independently. It is the exact version
   whose documentation is being audited and the pre-tag unified-stamp anchor.
   A maintainer must confirm it explicitly; do not infer it from a ref, branch,
   filename, package metadata, or surrounding context, and do not accept
   `unknown`. The matching tag does not need to exist during pre-tag audit.
3. Resolve `base_ref`, the code-comparison start. Use the caller-supplied ref
   when explicit. Otherwise walk the resolved target commit's first-parent
   history and select the nearest commit carrying exactly one strict,
   source-valid release SemVer tag whose normalized identity differs from
   `target_release_version`. A tag is eligible only when its peeled tree
   contains the fixed discovery path
   `docs/site/.meta/audit/handoffs/pre-tag-{tag-version}.md` and candidate path,
   and the discovery schema, candidate blob, cumulative lineage, reconstructed
   anchor tree, and final tag-tree binding all validate from that tree alone.
   This tag-tree test is the sole meaning of "previously verified" for default
   selection; do not consume a current branch, post-tag evidence branch,
   worktree, external classification, or unreachable old object. It therefore
   rejects drifted or incomplete tags without needing a mutable registry. A
   same-version remediation rerun must supply `base_ref` explicitly. Record the
   selected tag and peeled commit. Multiple tags on the nearest eligible
   commit, no eligible candidate, or an unresolvable tag is `blocked`; never
   choose by tagger date, lexical order, or loose version coercion.
4. Resolve both refs immediately to immutable commit SHAs. Working-tree,
   staged, untracked, or later branch content may be described only in a
   read-only diagnostic. If any such content falls within the audit scope,
   authorized write paths, or required evidence inventory, the phase is
   `blocked`: require the maintainer to commit it, update `target_ref`, and
   rerun the complete pre-tag audit. Passing evidence must be exact blobs from
   the resolved `target_ref` tree, not merely content that existed in an
   ancestor and not any current filesystem bytes.
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
pre-tag re-entry: post-tag has invalidated the pre-tag authority or tag binding
for any tree, locator, schema, blob, hash, type, lineage, or version reason;
the maintainer has selected a remediation path in Section 7; and the host
maintainer has deleted or moved the invalid tag outside docs-audit. Record that
selection and the now-absent/replaced tag state before the complete pre-tag
protocol. If the invalid tag still resolves to the target version, remain
post-tag `blocked`; docs-audit never deletes, moves, or creates a tag.

When no confirmed release version exists, a read-only diagnostic fact review
may still describe the affected pages, but the audit result remains `blocked`:
it cannot persist a versioned audit report, produce a phase success, or alter
stamps. Existing values remain unchanged and new pages remain `unverified`,
preserving issue #118 semantics.

### Release-version normalization

Validate each raw version fact against its owning source's required form, then
normalize it before any equality comparison. Do not compare the raw strings
across sources and do not silently repair a source that uses the wrong form.

| Source | Required raw form | Normalization input |
| --- | --- | --- |
| Maintainer-confirmed `target_release_version` and actual Git tag | `vX.Y.Z` (including valid SemVer pre-release or build suffixes) | Remove exactly one leading `v`. |
| Versioned Release Notes page and its version index entry | `vX.Y.Z` | Remove exactly one leading `v`. |
| `docs/site/.meta/releases.json` keys or fields whose values represent release versions | `vX.Y.Z` | Remove exactly one leading `v`; paths and other non-version values are not parsed as versions. |
| `.claude-plugin/marketplace.json` `metadata.version` | `X.Y.Z` without `v` | Use the raw value unchanged. This matches the host convention in `AGENTS.md`. |
| `package.json` `version` | `X.Y.Z` without `v` | Use the raw value unchanged. |

Parse every normalization input as strict SemVer without lossy coercion, and
compare the resulting normalized SemVer identities. Preserve pre-release and
build components in that identity. Identity equality is component-wise and
case-sensitive, including pre-release and build identifiers; SemVer precedence
that ignores build metadata is not sufficient. Sources requiring a prefix
accept exactly one lowercase `v`; `V`, `vv`, or a missing prefix is invalid.
Record both the raw source value and the normalized value in the audit
evidence. The confirmed entry or issue #116 handoff must also declare the
complete required version-source inventory as
`{source_id, locator_kind, locator, selector, extractor, required_raw_form}`.
For a Git file, `locator` is its repository path and `selector` is an exact
JSON Pointer, YAML/Markdown field identity, or unique index-entry key;
`extractor` names the deterministic parser and version. Non-file facts use an
immutable locator such as the tag ref/object, maintainer-confirmation id, or
handoff field. A missing/ambiguous selector, multiple matches, or an unknown
extractor is `blocked`; never scan a multi-version file and choose a plausible
value.
Pre-tag persists that inventory and post-tag consumes the same inventory; do
not silently add, drop, or substitute a source. A missing value, invalid SemVer,
source-form violation, or normalized inequality is `blocked` in both pre-tag
and post-tag audits even if another surface is valid. Report every failing
required source rather than stopping after the first one.

The inventory always includes the future actual-tag source. During pre-tag its
locator/selector/extractor/raw-form contract is persisted with
`pre_tag_value: pending_expected_absent`; absence is expected and is not a
version failure. Post-tag resolves that exact declared locator and replaces the
pending state with the raw tag value and normalized comparison result.

All protocol digests use one canonical algorithm. Serialize RFC 8259 JSON as
UTF-8 with object keys sorted lexicographically, arrays in the order specified
below, no insignificant whitespace, no trailing newline, exact case-sensitive
strings, and JSON base-10 integers. Omit absent optional members; never encode
them as `null`. Hash the resulting bytes with SHA-256 and persist lowercase
`sha256:<64-hex>`. The version inventory digest input is an array sorted by
`source_id`, each object containing exactly `source_id`, `locator_kind`,
`locator`, `selector`, `extractor`, and `required_raw_form`. The empty lineage
ledger therefore has a deterministic genesis digest. A completed prior lineage
entry contains exactly `attempt`, `commit`, `tree`, `record_path`,
`record_blob`, `handoff_blob`, and `previous_lineage_digest`; the array is
strictly ascending by integer `attempt`. The discovery current entry contains
exactly `attempt`, `anchor_commit`, `anchor_tree`, `record_path`, `record_blob`,
and `previous_lineage_digest`. `prior_lineage_digest` hashes only the completed
prior-entry array; discovery `lineage_digest` hashes that same array with the
current entry appended. Producer and consumer must recompute the bytes, not
trust a stored digest literal.

## 2. Deterministic Layer

Run all six steps in order.

### Step 1: Compute changed files

Run or reproduce the semantics of:

```bash
git diff --name-status <base> <target>
```

Preserve change status and path. Add only those working-tree changes that were
confirmed as diagnostic scope. The combined set is the report's changed-files
inventory, but any in-scope uncommitted entry blocks phase success and is never
passing fact evidence in pre-tag.
Use the two-dot endpoint diff by default. Only when the caller explicitly
requests merge-base semantics, use
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
Before reading bytes, inspect the resolved `target_ref` tree entry. Formal
pages, file-backed release surfaces, and audit records must be ordinary Git
blobs; a tree, gitlink, symlink mode `120000`, filesystem dereference, or
missing entry is `blocked`. Preserve each entry's mode and object type as
evidence. A stamp may modify an existing regular page only without changing its
mode or type; newly created audit records must use regular non-executable mode
`100644`.
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
itself. A template whose shared frontmatter and expected structure both pass
receives final status `verified`; otherwise it is `stale` or blocked by the
missing structural evidence. This status does not imply type-specific fact
checking. A placeholder value or absent implementation evidence in a template
is not a release blocker.

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

Use two fixed, version-addressed paths:

- candidate evidence: `docs/site/.meta/audit/audit-{target_release_version}.md`;
- discoverable final handoff:
  `docs/site/.meta/audit/handoffs/pre-tag-{target_release_version}.md`.

Resolve `target_release_version` to its strict canonical source form before
substitution. Do not add timestamps or branch names. A same-version rerun
reuses these paths. The candidate embeds the cumulative ordered prior-attempt
ledger and its digest. The discovery copies that ledger and appends the current
anchor/record tuple plus a new chain digest; its current entry omits its own
handoff blob to avoid self-reference, while the external package supplies that
blob. The current entry names the immediately superseded attempt. Old blobs
remain immutable in history when available, but fallback validation does not
require a squash-discarded commit.

Run the protocol in this order:

1. Resolve immutable `base_ref` and `target_ref` commits, the confirmed target
   version, required version-source inventory, release branch ref, and any
   prior active anchor. Capture the host branch, index, worktree, and relevant
   path fingerprints before any write. Re-resolve the branch before integration;
   movement from `target_ref` is a blocker.
2. Compute the complete impact set and run every fact check from exact blobs in
   the `target_ref` tree. Any in-scope staged, unstaged, or untracked content is
   diagnostic-only and blocks success until committed into a new `target_ref`
   and the complete audit is rerun.
3. Verify the issue #116 handoff, every declared version source, and every
   affected page. Define the unified stamp set as the affected-page set union
   every verified Markdown release surface carrying `last_verified_version`.
   Record pre-stamp values. Non-Markdown sources remain read-only hashed facts.
4. Create an isolated temporary worktree and temporary branch from the exact
   `target_ref` commit, with an index initialized from that tree. Never build the
   candidate in or inherit the caller's worktree/index. The host branch remains
   unchanged until every candidate check passes.
5. In the isolated candidate, write all stamps together and create the candidate
   evidence record. Read back every page and hash exact Git-candidate bytes for
   every stamped page and file-backed version source. The record may state only
   `candidate_verified`; it must not contain `ready_for_tag`, a success time,
   its containing commit/tree identity, or a claim that post-commit confirmation
   already passed.
6. Stage only the unified-stamp pages and fixed candidate-record path. Validate
   the complete staged delta with raw metadata, name status with rename/copy
   folding disabled, summary, and full binary patch. A stamp page must remain at
   the same path as an ordinary blob, preserve its exact mode, have status `M`,
   and change only the single `last_verified_version` field line. The candidate
   record may be `A` or `M` only at its fixed path and must be a `100644` ordinary
   blob with the complete schema from Section 5. Reject `R`, `C`, `D`, `T`,
   mode-only changes, executable-bit changes, symlinks, gitlinks, path swaps,
   and every other path or content hunk.
7. After atomically replacing the final candidate record, stage it again and
   repeat the same full staged gate. This second gate proves the exact final
   record, its source inventory, hashes, candidate conclusion, and difference
   inventory; an earlier draft check never authorizes the final bytes.
8. Create the ordinary **post-stamp anchor commit** on the temporary branch.
   Re-run the same raw metadata, status, type, mode, path, and content checks for
   `target_ref..anchor_commit`; verify `anchor_commit^{tree}`, the candidate
   record blob, and `git show <anchor_commit>:<record-path>`. Any failure makes
   the candidate invalid and produces no final handoff.
9. Only after step 8 passes, write the fixed discoverable handoff file. It must
   contain `schema_version`, `attempt`, `phase: pre-tag`,
   `target_release_version`, immutable `base_ref`/`target_ref` commits,
   `phase_result: ready_for_tag`, result time, version-source inventory digest,
   anchor commit/tree, candidate record path/blob, post-commit confirmation
   result/time, the handoff path's prior mode/blob or `absent`, and optional
   copied prior `lineage` entries
   `(attempt, commit, tree, record_path, record_blob, handoff_blob,
   previous_lineage_digest)`, a current entry
   `(attempt, anchor_commit, anchor_tree, record_path, record_blob,
   previous_lineage_digest)` without a self-referential handoff blob, a
   recomputed `lineage_digest`, and the immediately superseded attempt id when
   applicable. The external package supplies the current discovery blob.
   The anchor commit SHA is therefore stored in a committed, version-addressed
   discovery record without requiring a Git self-reference.
10. Stage only that handoff path. Require a `100644` ordinary blob and an `A` or
    `M` status, reject every other delta, then create the **handoff commit**.
    Confirm the anchor-to-handoff delta with the same raw/status/type/mode/patch
    checks, validate the handoff schema and blob, and record the handoff commit
    and tree in the external release handoff package. The file cannot contain
    its own containing commit/tree; the package supplies those two identities.
11. Integrate the validated temporary branch by a normal fast-forward only when
    the host release branch still equals `target_ref` and its captured
    worktree/index fingerprints are unchanged. Verify the integrated branch
    resolves to the handoff commit/tree and committed discovery blob. Only then
    expose the external package and return `ready_for_tag` to issue #120. A
    squash or merge may later change commit identity, but the released tree must
    preserve the validated tree semantics in Section 7. If post-FF readback
    fails, update the host branch back to `target_ref` only when compare-and-
    swap proves it still equals the just-integrated handoff commit; then restore
    captured index/worktree state and verify the ref and every fingerprint. If
    the branch moved concurrently, do not overwrite it: remain `blocked`, name
    the residual ref/commit and exact maintainer recovery command, and prohibit
    tag creation.

Every failure, including post-integration readback, is transactional: delete
the isolated worktree and temporary ref, perform the guarded branch rollback
from step 11 when integration occurred, restore accidentally touched authorized host
path and index entry to the captured pre-write bytes/mode/type, remove this
attempt's untracked drafts, and verify branch SHA, `git status --porcelain=v2`,
staged/unstaged raw diffs, modes, types, and per-path hashes match the captured
state. Never restore or overwrite unrelated user changes. If restoration itself
cannot be proven, remain `blocked`, list the exact residual paths/index entries
and manual recovery commands, and prohibit tag creation. In particular, a
staged convergence failure must leave no stamp, record draft, candidate commit,
handoff, or half-staged state in the host worktree.

Return `blocked` and do not return `ready_for_tag` for any missing/ambiguous
input, in-scope worktree content, non-`target_ref` fact evidence, non-regular or
symlink input, factual blocker, version-source failure, schema gap, hash/readback
failure, mode/type/path/content convergence failure, temporary commit failure,
handoff failure, branch movement, integration failure, or incomplete rollback.

Here, “remains unverified” is a factual verification outcome caused by missing
evidence; the valid frontmatter value `last_verified_version: unverified` does
not itself make a page stale or block it from becoming factually `verified`.

Never stamp only a `verified` subset. If `target_release_version` changes after
the audit, the report, unified stamp conclusion, and `ready_for_tag` result are
immediately invalid; rerun the complete pre-tag audit for the new value.
The candidate record is immutable evidence, not a final success authority.
`ready_for_tag` is authoritative only through a validated discovery record and
external package after integration. A failed temporary attempt is cleaned up;
it does not require a supplemental success-looking record in host history.

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

The candidate record path and discoverable handoff path are fixed in Section 4.
Both are `100644` ordinary blobs under `.meta/` and do not use standard page
frontmatter. The candidate record must contain every field consumed later:

| Field group | Required candidate-record content |
| --- | --- |
| Identity | `schema_version`, `attempt`, `phase: pre-tag`, immutable `base_ref` and `target_ref` commits, confirmed `target_release_version`, diff semantics, ordered prior-attempt `lineage`, prior `lineage_digest`, and optional immediately superseded attempt id; the current tuple is added only by discovery after the candidate blob exists |
| Impact | raw/name-status changed-file inventory, change-map matches/delta, affected and unified-stamp sets |
| Per-page evidence | path, target-tree mode/type/blob, pre/post stamp value, claims, exact target-ref code/test blob evidence, final status, post-stamp SHA-256 |
| Version sources | complete required inventory with locator kind/value, selector and extractor identity, raw form, normalized case-sensitive SemVer identity, target-tree path/mode/type/blob when file-backed, SHA-256, comparison result, canonical inventory JSON algorithm/version and recomputed digest; the actual-tag entry is `pending_expected_absent` only in pre-tag |
| Convergence | both staged-gate inventories with raw old/new mode, object type, status with rename/copy disabled, full-patch decision, and zero unauthorized delta |
| Candidate conclusion | `candidate_verified`, stamp read-back result, blockers, reproducible commands; never `ready_for_tag`, success time, containing commit/tree, or post-commit result |

Atomically replace the candidate record in the isolated worktree, read it back,
validate this schema, and re-run final staged convergence before committing it.
The discoverable handoff file is produced only after committed candidate
confirmation and uses the exact schema listed in Section 4 step 9. The external
package adds the handoff commit/tree/path/blob identities that the handoff file
cannot self-contain. Post-tag rejects unknown schema versions, missing fields,
ambiguous attempts, non-monotonic or duplicate attempt ids, a broken cumulative
lineage digest, a current tuple that disagrees with the ledger, or any other
tuple inconsistency. When older commits were removed by squash, the current
tag-anchored cumulative ledger is the validation source; do not require an old
object that is no longer reachable and never reconstruct missing current fields
from the worktree.

## 6. Unified Version Stamp

Stamp only during a valid pre-tag audit and only when all conditions are true:

1. every page in the unified stamp set has a final `verified` conclusion
   and there is no unresolved evidence gap; and
2. Release Notes, the version index, `docs/site/.meta/releases.json`, and host
   version facts all satisfy their required source forms and equal the
   maintainer-confirmed `target_release_version` after SemVer normalization.

Then, in one audit operation:

- update every page in the unified stamp set (the affected-page set union all
  verified Markdown release surfaces carrying `last_verified_version`) from
  `unverified` or an older anchor to `target_release_version`; and
- read all unified-stamp pages back to verify that the complete stamp is consistent;
- hash the exact post-stamp bytes of every unified-stamp page and file-backed
  release-version surface; and
- build, validate, commit, confirm, discoverably anchor, and integrate the
  candidate through the isolated transaction in Section 4. Both staged and
  committed gates inspect paths, contents, statuses, modes, object types,
  rename/copy/delete/type changes, symlinks, and gitlinks; and
- return `ready_for_tag` only from the final integrated discovery record and
  external package. The candidate record itself never expresses final success.

Do not stamp a verified subset when another page is `stale`, `mismatch`, remains
factually unverified after review, or has missing evidence. The literal
frontmatter value `unverified` is not by itself a blocker. The matching tag is not required
for this pre-tag write. Do not modify `.meta/releases.json`; issue #116 owns
that content, while this audit only verifies it. Outside a valid pre-tag audit,
keep each page's existing value; new pages remain `unverified`, and the field
must not be omitted.

## 7. Post-tag Audit

Run the post-tag protocol in this order:

1. Resolve the actual tag twice: once at entry and once immediately before
   result integration. Record and compare
   `(tag_ref_target_object_id, peeled_commit, peeled_tree)`. For an annotated
   tag the first member is the tag-object id; for a lightweight tag it is the
   directly referenced commit id. Both forms are supported. Missing, moved,
   unpeelable, or tuple-mismatched tags are `blocked`.
   Also require a caller- or maintainer-confirmed `release_evidence_branch_ref`
   and resolve its exact `release_evidence_expected_head` commit. This branch is
   the sole integration target for the independent post-tag result; never infer
   it from the current branch, the tag, or `HEAD`.
2. Locate pre-tag authority. Prefer the external package and validate its
   handoff commit/tree/path/blob plus the committed discovery file. If the
   package is absent or its commit is unavailable after squash/fresh clone,
   read exactly
   `docs/site/.meta/audit/handoffs/pre-tag-{target_release_version}.md`
   from the peeled tag tree. Validate its complete schema and blob. Reconstruct
   the anchor tree by replacing that handoff path with its recorded prior
   mode/blob or removing it when the preimage is `absent`; the reconstructed
   tree must equal the recorded anchor tree. If a supplied package conflicts
   with the tag artifact, block rather than silently falling back. The fixed
   discovery must resolve exactly one current pre-tag attempt. Its cumulative
   prior ledger may contain multiple strictly monotonic, unique historical
   attempts; only the current attempt can become release-active after final
   tag-tree binding. Zero or multiple current attempts are ambiguous and
   `blocked`.
3. Validate the anchor four ways when its commit object is available:
   commit-to-tree, commit/path-to-record-blob, discovery tuple, and tag tree.
   When squash makes the commit unavailable, the deterministic reconstructed
   tree, tag-tree candidate record blob, discovery schema, and full convergence
   evidence are the equivalent fallback. In both paths, the actual tag tree
   must equal the package's handoff tree or be exactly the reconstructed anchor
   tree plus the single validated discovery-path delta. Commit identity may
   differ; any other tree delta is `blocked`.
4. Read the candidate record only from the anchor commit or the byte-identical
   record blob in the peeled tag tree. Validate all Section 5 fields,
   `candidate_verified`, cumulative lineage and chain digest, convergence evidence, and discovery
   `ready_for_tag`. Never read a working-tree/later-branch copy as passing
   evidence. A dirty current copy is diagnostic only and cannot repair a gap.
5. From the peeled tag commit, use Git object reads for every stamped page and
   required version-source path. Verify ordinary-blob type/mode, existence,
   exact SHA-256, raw form, and component-wise case-sensitive SemVer identity
   against the persisted inventory. Missing or substituted sources are
   `blocked`; current filesystem bytes cannot support `release_verified`.
6. On tree inequality, report raw old/new mode, type, object identity,
   name-status with rename/copy folding disabled, summary, and full relevant
   patch. Per-path hashes are diagnostic and can never override tree inequality.
7. Only after all applicable decision checks complete, build the fixed independent record
   `docs/site/.meta/audit/audit-{target_release_version}-post-tag.md` in an
   isolated transaction. Include attempt/lineage, tag-ref target object,
   peeled commit/tree,
   locator mode (`handoff` or `tag_fallback`), all anchor/tree/blob/schema/hash
   checks, version-source results, blockers, commands, and the candidate phase
   result (`release_verified` only when every check passed, otherwise
   `blocked`). Atomically replace, schema-check, stage only this `100644` ordinary
   path, apply the same metadata/content convergence rules, commit on the
   confirmed release-evidence branch from its expected head, read back its blob,
   then fast-forward that exact branch only if it still equals
   `release_evidence_expected_head` and its captured worktree/index state is
   unchanged. Verify the integrated commit/tree/path/blob. If verification
   after fast-forward fails, return the evidence branch to
   `release_evidence_expected_head` only when compare-and-swap proves it still
   equals the just-integrated result commit. Never overwrite a concurrent move;
   report the residual ref/commit and exact maintainer recovery command. Any
   write, stage, commit, readback, or integration failure cleans the isolated
   attempt, performs that guarded ref rollback when needed, restores touched
   host path/index fingerprints, verifies the restored ref and fingerprints,
   and returns `blocked`; it must not expose `release_verified` or a partial
   record.
8. Return `release_verified` only after the integrated post-tag record is
   committed and read back. Never append to or modify the anchored candidate or
   discovery blobs. Every rerun repeats locator and content checks.

Blocked outcomes have these required next steps:

| Trigger | Record and next step |
| --- | --- |
| Tag missing | Keep the valid pre-tag authority unchanged; host creates the correct tag at the validated integrated handoff/release tree (anchor plus validated discovery delta), then rerun post-tag. |
| Handoff missing/unresolvable | Run the fixed-path fallback. If it cannot uniquely validate, invalidate the attempted success and rerun complete pre-tag to create a new discoverable anchor. |
| Record/schema/blob/hash/type gap | Persist a post-tag blocked result when possible; repair the intended committed release content and complete pre-tag again. Never patch evidence from the worktree. |
| Tag tree, release branch, or version source drift | Maintainer chooses either: correct/delete/move the erroneous tag and rerun complete pre-tag for the same version, or abandon it and confirm a new version. Both use the actual intended content as new `target_ref`. |
| Same-version rerun | The new candidate/discovery records carry the cumulative chained lineage and identify the immediately superseded attempt; the post-tag blocked record stores the selected remedy. Old blobs are never edited. The fixed discovery path exposes exactly one current attempt whose ledger digest and final tag-tree binding must validate, including after squash. |
| Post-tag persistence failure | Restore/remove the partial post-tag result, keep the pre-tag anchor and tag unchanged, repair persistence, and rerun post-tag. No success state exists until durable readback passes. |

Post-tag audit performs final consistency verification only. Do not regenerate
Release Notes, indexes, release metadata, documentation, GitHub Release
content, unified stamps, or any tag.

## 8. Release Handoff and Responsibility Boundaries

Return the persisted audit report and exactly one phase result:

- **`ready_for_tag`:** pre-tag audit passed and the complete unified stamp set
  was stamped to `target_release_version`, committed, confirmed, discoverably
  anchored, and integrated; do not call the version published.
- **`release_verified`:** post-tag audit proved the actual tag and all release
  surfaces match the still-valid pre-tag candidate/discovery lineage, and the
  independent post-tag result was committed and read back.
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
