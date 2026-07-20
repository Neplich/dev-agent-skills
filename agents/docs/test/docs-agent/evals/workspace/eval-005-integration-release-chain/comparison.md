# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`
- Scenario: AI Hub-shaped formal-docs release chain from host contract through GitHub Release handoff

## Test Set / Fixture Version

- Fixture: `issue-115-ai-hub-shaped-v5-sha1-pinned`
- Fresh run: with-skill `/tmp/pr130-sha1-fresh-with-Hl4G4q/`; without-skill `/tmp/pr130-sha1-fresh-without-bUSWDG/`; independent judge `/tmp/pr130-sha1-fresh-judge-0eBegq/`.
- Source: PR #130 head `3e376bca414658d2367aced42d6799dad6b198ed` plus the current SHA-1 object-format pin working tree.
- Runtime Git: `.eval/setup-git-fixture.sh` explicitly initializes the fixture with `--object-format=sha1` because its raw-delta gates intentionally validate 40-character object IDs. Under `GIT_DEFAULT_HASH=sha256`, all three fresh runs completed setup with object format `sha1` and 40-character commit/tree/blob IDs. The existing isolated base/target/anchor/handoff, synthetic tag, evidence branch, source-binding and final readback gates remained intact.
- Harness: with-skill and without-skill were copied independently from the same current pristine fixture. With-skill read the Docs/PM skills and shared contracts; without-skill received the same prompt and assertions but read no skill, Agent README, internal instructions, old comparison, historical baseline or with-skill output. A third fresh judge reviewed only these two frozen outputs, current assertions, fixture and authoritative contracts, then independently reran setup, `test:api` and `test:docs` in a third pristine copy.

## Latest Result

**PASS（with-skill 8/8 assertions；without-skill 8/8）** — the independent judge accepted the SHA-1 pin under a SHA-256 default environment, complete pre-tag `ready_for_tag`, evidence-before-conclusion post-tag `release_verified`, three-way source binding, and gated `pm-agent:github-release-generator` handoff from real runtime Git objects. Both lanes preserved zero host/remote tag and GitHub Release writes; only isolated setup copies created synthetic local tags.

The two lanes performed identically in this fixture, so this run proves fixture fidelity and protocol executability but does not demonstrate a relative quality gain from the skill over the fresh baseline.

## With-Skill Behavior

- `validates_shared_frontmatter_contract`: PASS. Verified all 19 formal Markdown pages, the shared seven-field contract, enums, and structure-only treatment for the five typed templates.
- `uses_host_templates_and_scaffold`: PASS. Verified the five host templates, `scaffold-doc.mjs`, `npm run new:doc`, manifest and tests as one template source.
- `reconciles_api_sync_and_change_map`: PASS. The API page points to an implementation that explicitly defines `GET /api/search`, handler and `SearchItem`; the executable `test:api` evidence asserts registration, 200/400 bodies, lower/upper clamping, fractional/NaN/Infinity rejection and blank-query rejection; change-map coverage is exact.
- `accepts_confirmed_site_release_notes_handoff`: PASS. Verified the confirmed page, metadata, index, rerun docs checks, six-source inventory, evidence and Docs/PM ownership boundary.
- `completes_pre_tag_ready_for_tag`: PASS. With `GIT_DEFAULT_HASH=sha256`, the explicitly SHA-1 fixture produced 40-character OIDs accepted by the raw-delta regexes. It resolved the eight-path base/target diff, built candidate/anchor/handoff outside the fixture release branch, validated the complete schema and four-path convergence, then advanced the release branch from the immutable target only after object and record readback passed. Candidate version-source binding, discovery current-entry and canonical lineage are derived from one target version/source anchor/digest group; the final self-check re-reads all three committed records and recomputes lineage SHA-256.
- `completes_post_tag_release_verified`: PASS. Bound the lightweight tag tree to the handoff tree, reused the exact stamped blobs and inventory, then collected and validated the second tag tuple and observed/expected evidence head before invoking the guarded success renderer. The successful and blocked templates both place decision evidence before conclusion; the blocked sample contains only `phase_result: blocked`. The isolated result branch then passed single-path staged/committed gates, expected-head CAS and final evidence ref/blob readback.
- `hands_off_three_gates_to_github_release`: PASS. The handoff carries confirmed site Release Notes, `ready_for_tag`, `release_verified`, and a separate current maintainer publish-approval requirement.
- `preserves_no_mutation_boundaries`: PASS. No host/remote tag or GitHub Release write occurred.

## Without-Skill Baseline

- Source: freshly generated from the same prompt and pristine v5 fixture after the SHA-1 pin; it read no skill, Agent README, internal instructions, old comparison, historical baseline or with-skill content.
- Result: 8/8 assertions PASS.
- It independently resolved the same Git object chain, recomputed inventory/lineage/tag-tuple evidence, verified evidence-before-conclusion ordering and the committed three-way source-binding self-check, reran `test:api` and `test:docs`, and produced the same gated handoff and mutation boundary.
- No historical baseline was reused.

## Failures

- Assertion failures in with-skill: none.
- Assertion failures in without-skill: none.
- Independent judge blockers: none; verdict PASS and comparison update allowed. The judge independently reproduced the previously failing `GIT_DEFAULT_HASH=sha256` environment and confirmed setup exit 0, object format `sha1`, and 40-character critical OIDs.
- Fixture `npm run test:api`: passed in both lanes.
- Fixture `docs/site` `npm run test:docs`: 73/73 passed in both lanes.
- Non-blocking dependency diagnostic: both isolated `npm ci` runs reported 2 moderate and 1 high audit findings from the committed fixture lockfile; no eval assertion depends on dependency-vulnerability remediation.
- Evidence limitation: the without-skill lane's no-skill claim relies on its execution declaration plus independent workspace/output evidence; no external file-read telemetry was available.
- Comparative limitation: the baseline also passed 8/8, so the eval currently measures object-level release-chain correctness rather than skill-specific uplift.

## Next Steps

- Keep the durable result `PASS` for fixture fidelity and protocol executability.
- If future changes need to measure skill uplift, add a separate ambiguity or missing-evidence case where the correct behavior depends on the skill's blocking and handoff rules rather than on a fully specified executable fixture.

## Runtime Artifact Policy

- Candidate outputs, runtime Git repositories, dependency installs, transcripts, timing, diagnostics and the judge verdict remain in the three `/tmp/pr130-sha1-fresh-*` directories listed above and are not committed.
- This `comparison.md` is the only durable model-eval result.
