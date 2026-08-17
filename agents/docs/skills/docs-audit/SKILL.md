---
name: docs-audit
description: "Audit formal documentation against code, tests, Git objects, version facts, and raw manual evidence for bounded pre-tag or post-tag verification. Use after docs-agent routes a confirmed version audit."
visibility: internal
---

# Docs Audit

Audits a host project's formal documentation through a deterministic impact
pass followed by fact verification. This file owns the entry and release gates;
load `_internal/INSTRUCTIONS.md` only after the entry basis and version baseline
are resolved.

## Mandatory Audit Transaction

Resolve the active installed `docs-audit` skill and load
`_internal/INSTRUCTIONS.md` after credentials are complete. Keep one
reproducible inventory binding immutable base/target objects, changed files,
change-map matches, affected pages, all release surfaces, normalized versions,
and each page's pre-stamp state.

Derive live index and worktree state only from current isolated Git/status
evidence. A supplied patch, name-status listing, or other captured change
artifact is content evidence, not proof that the current worktree is dirty.
Never add a worktree blocker that contradicts the locked Git state.

Persist that inventory as canonical sorted data with a reproducible identity
or digest during pre-tag, and make post-tag consume exactly the same bound
inventory. Any membership, locator, order, or identity drift—or an attempt to
replace it with a broad multi-version scan—blocks both publication readiness
and post-tag verification.

Report the inventory binding and integrity status in every audit conclusion,
including blocked reviews: state what pre-tag would bind, whether post-tag can
consume that exact identity, and which missing or changed element blocks it.
When sources use both prefixed and unprefixed version forms, explicitly state
whether they normalize to one complete identity while preserving prerelease,
build metadata, and case-sensitive components.

In pre-tag, verify the complete affected set against code/tests, classify
confirmed outdated claims with the literal final verdict `stale` rather than
the intermediate label `mismatch`, validate the shared frontmatter source, and stamp
all verified pages in one transaction. Persist the complete candidate producer
record, anchor it in a commit, discover it through the versioned path, integrate
by fast-forward, and read it back before returning `ready_for_tag`; never call
that published. On any failure, roll back only the current attempt and prove
HEAD, refs, index, worktree, and authoritative prior records were restored.
The producer record includes complete per-source locators, pre-candidate and
post-candidate staged inventories, and readback identity. Keep the candidate,
anchor, and handoff steps distinguishable in Git evidence; a single commit that
mixes candidate content, anchor, handoff, and unrelated page changes does not
prove the transaction.
The pre-tag transaction evidence explicitly records `source_locators`
(path/mode/type/blob/hash), `pre_candidate_inventory`,
`post_candidate_inventory`, `candidate_commit`, `anchor_commit`,
`handoff_commit`, `fast_forward_result`, and `readback_identity`. Stamp every
verified inventory member—including Release Notes page/index surfaces—in the
same transaction even when its body content did not otherwise change.
Derive locator fields, staged inventories, object identities, and digests from
the locked Git/source evidence. The inbound handoff does not need to prepopulate
this audit-protocol schema; block only when the underlying raw evidence is
absent or contradictory.
Before committing, validate the candidate against every Section 5 field group,
including the exact `canonical-json-rfc8259-sorted-v1` algorithm name, complete
locator contracts, both pre-candidate and post-candidate staged inventories,
and every post-stamp SHA-256. After the final atomic record write, recompute its
actual Git blob and copy that exact identity into the anchor, discovery handoff,
and external package; never reuse a draft-record digest. Record the distinct
candidate, anchor, and handoff commits plus post-fast-forward readback before
returning `ready_for_tag`.
The candidate record must not contain the literal token `ready_for_tag`
anywhere, including explanatory prohibitions. Every version-source entry must
render all six locator-contract keys (`source_id`, `locator_kind`, `locator`,
`selector`, `extractor`, `required_raw_form`), and every file-backed source also
renders its path/mode/type/blob/hash evidence. Render two separately named,
complete staged inventories—pre-candidate and post-candidate—before creating
the anchor. The handoff commit stages only the discovery handoff path, and the
external package reports that commit's tree/path/blob plus fast-forward and
integrated readback evidence.

In post-tag, select the trusted pre-tag authority before deterministic fallback,
bind the actual tag object/tree and every surface to the same inventory, and
persist `blocked` on mismatch without rewriting the authority. Manual-page
audits additionally verify every step screenshot file, navigation reachability,
and redaction-sensitive content from raw files.
Review the complete same-version attempt history, including directly
superseded attempts, before selecting authority. If persisting the current
result fails, state the recovery condition: restore write capability, persist
the blocked record, and verify it by readback without changing prior authority.
For manuals, treat referenced raster and vector image files as images, and
report redaction findings at an exact file plus line, element, or object
location.

## Entry Credentials

Require one confirmed audit entry basis:

- a release scope and pending-release version context;
- an explicit base and target for a bounded audit; or
- a PM handoff packet or equivalent confirmed documentation-audit scope.

Every audit requires `target_release_version`, the exact version
whose documentation is being verified. A maintainer must confirm this value
explicitly. Never infer it from `target_ref`, a branch name, a filename, or any
other context, and never accept `unknown`. If it is missing, inferred, unknown,
or not maintainer-confirmed, return `blocked` before writing a report, stamping
pages, or changing version metadata.

The PM packet definition lives in
the plugin-local generated `../docs-agent/_internal/_generated/shared-contracts/handoff-contract.md`.
Direct invocation does not waive this gate. If the audit scope is ambiguous,
stop before writing a report or version metadata and return the missing scope
to `docs-agent` or `pm-agent`.

## Audit Phase Selection

Select exactly one phase after the entry credentials are complete:

- **Pre-tag:** the release PR is pending and the target tag may not exist yet.
  Compare `base_ref..target_ref`, verify the complete affected set and all
  release-version surfaces, then return `ready_for_tag` only after one unified
  stamp to the confirmed `target_release_version`.
- **Post-tag:** the actual tag exists. Read the valid pre-tag record and verify
  that the tag and every release-version surface still match the same
  `target_release_version`; locate the anchor by the trusted handoff first and
  otherwise by the deterministic versioned discovery path defined internally.
  Do not regenerate or restamp content.

`ready_for_tag` means the documentation and version facts are ready for tag
creation. It exists only after committed candidate validation, discoverable
handoff validation, and branch integration all pass; a working-tree or
candidate-record value is never sufficient. It must never be described as
published or released.
`release_verified` means the post-tag consistency check passed. Any missing,
invalid, inconsistent, or insufficient evidence returns `blocked`.

## Authoritative Execution Gates

Before auditing or writing:

1. Resolve `base_ref`, `target_ref`, and the maintainer-confirmed
   `target_release_version` independently. Default `target_ref` to the
   pending-release `HEAD`. Resolve a default `base_ref` deterministically from
   that immutable target commit as defined internally; never use tagger date,
   lexical order, or either ref as the target release version.
2. Run the deterministic layer before fact verification. It establishes the
   changed files, change-map matches, affected formal pages, frontmatter
   validity, and suspect pages; it does not turn a missing same-diff document
   update directly into `stale`.
3. Verify every affected page against current code or test evidence under the
   trust model in
   the plugin-local generated `../docs-agent/_internal/_generated/shared-contracts/consumption-contract.md`.
   Code and tests are ground truth; preserve each conflicting document claim,
   code fact, and impact.
4. Treat `stale`, `mismatch`, a page that remains unverified after fact review,
   and insufficient evidence as release blockers. The literal frontmatter value
   `unverified` remains valid and is not by itself a factual conclusion. Only a
   complete affected set whose conclusions are all `verified` may receive one
   unified pre-tag stamp; never stamp a verified subset.
5. `last_verified_version` records the version against which page content was
   verified; it is not publication state. Record every page's value before the
   pre-tag stamp. Do not add a persistent `baseline_verified_version` field.
6. Outside a valid pre-tag release audit, a page without a stampable confirmed
   version keeps its current value, and a new page keeps `unverified`, as
   required by the shared frontmatter contract. Never invent a version merely
   to replace `unverified`.

The exact two-layer protocol, status semantics, report format, stamp update,
and release handoff live in `_internal/INSTRUCTIONS.md`. Load that file only
after this gate passes; do not replace it with an ad hoc audit workflow.

## Missing Documentation Site

If `docs/site/standards/change-map.yaml` or the formal site foundation is
absent, do not initialize it silently. Report the missing audit foundation and
offer an explicit handoff to `docs-site-bootstrap`; wait for confirmation.

## Output

Report:

- selected phase, resolved `base_ref`, `target_ref`, and confirmed
  `target_release_version`
- changed files, change-map matches, and affected formal pages
- each page's pre-stamp `last_verified_version`, document claims, and code or
  test evidence
- `verified`, `stale`, or `mismatch` conclusions
- for a `suspect` page whose accurate contract survived a pure implementation
  refactor, `documentation_change_required: false` and the evidence-backed
  reason that no no-op page edit is needed
- in post-tag, the selected current attempt, its directly superseded attempt
  when present, their same-version relationship, and the authority-selection
  result
- for any blocked post-tag result that cannot be persisted, the concrete
  persistence recovery condition and readback required before any success
  state can exist, while preserving the prior authority unchanged
- for a blocker caused by staged, unstaged, or untracked paths, every affected
  path and its required disposition, the updated reference to audit, proof that
  both index and worktree are clean, and the full audit restart required after
  cleanup; an untracked required artifact must be explicitly preserved and
  committed or moved outside the audited worktree
- blockers, review commands, and any unified stamp update
- phase result: `ready_for_tag`, `release_verified`, or `blocked` with a
  concrete to-do list

At closeout, return the audit conclusion to the release handoff and follow the
safety-net behavior in
the plugin-local generated `../docs-agent/_internal/_generated/shared-contracts/closeout-contract.md`.
Wait for confirmation before another role acts unless the user has enabled the
applicable continuation.

Reuse and refresh the shared documentation-site deployment completeness state
only when the audit establishes a material change to a documentation build
target, navigation or assets, release scope, or runtime entry. Otherwise
preserve the prior state without starting a second check protocol.
