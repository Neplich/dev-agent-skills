# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`
- Scenario: AI Hub-shaped formal-docs release chain from host contract through GitHub Release handoff

## Test Set / Fixture Version

- Fixture: `issue-115-ai-hub-shaped-v3-batch-polish`
- Fresh run: `tmp/eval-runs/130-batch-polish/fresh-r7-20260720/`
- Source: PR #130 head `e4d8e27d0f77792be4a5201d354c2e8de1d3bf0e` plus the current batch-polish working tree
- Runtime Git: `.eval/setup-git-fixture.sh` creates isolated, resolvable base/target/anchor/handoff commits, a lightweight synthetic tag, and an evidence branch with an independent post-tag result commit. Pre-tag and post-tag records are built on temporary transaction branches; release refs move only through expected-old-value compare-and-swap and exact commit/tree/path/blob readback. Both candidates independently recomputed the object, inventory, lineage, entry/pre-integration tag tuple, command evidence, expected-head and final readback evidence.
- Harness: with-skill read the Docs/PM skills and shared contracts; only after it completed, without-skill was copied again from the current pristine fixture and received the same prompt but no skill, Agent README, internal instructions, old comparison, historical baseline or with-skill output. A third fresh judge reviewed only the frozen r7 outputs, current assertions, fixture and authoritative contracts. The judge accepted the runner's isolation/provenance record but did not perform process-level log forensics.

## Latest Result

**PASS（with-skill 8/8 assertions；without-skill 8/8）** — the independent judge accepted the complete pre-tag `ready_for_tag`, post-tag `release_verified`, and gated `pm-agent:github-release-generator` handoff from real runtime Git objects. Both lanes preserved zero host/remote tag and GitHub Release writes; only the isolated setup created its synthetic tag.

The two lanes performed identically in this fixture, so this run proves fixture fidelity and protocol executability but does not demonstrate a relative quality gain from the skill over the fresh baseline.

## With-Skill Behavior

- `validates_shared_frontmatter_contract`: PASS. Verified all 19 formal Markdown pages, the shared seven-field contract, enums, and structure-only treatment for the five typed templates.
- `uses_host_templates_and_scaffold`: PASS. Verified the five host templates, `scaffold-doc.mjs`, `npm run new:doc`, manifest and tests as one template source.
- `reconciles_api_sync_and_change_map`: PASS. The API page points to an implementation that explicitly defines `GET /api/search`, handler and `SearchItem`; the executable `test:api` evidence asserts registration, 200/400 bodies, lower/upper clamping, fractional/NaN/Infinity rejection and blank-query rejection; change-map coverage is exact.
- `accepts_confirmed_site_release_notes_handoff`: PASS. Verified the confirmed page, metadata, index, rerun docs checks, six-source inventory, evidence and Docs/PM ownership boundary.
- `completes_pre_tag_ready_for_tag`: PASS. Resolved the eight-path base/target diff, built candidate/anchor/handoff outside the fixture release branch, validated the complete schema and four-path convergence, then advanced the release branch from the immutable target only after object and record readback passed.
- `completes_post_tag_release_verified`: PASS. Bound the lightweight tag tree to the handoff tree, reused the exact stamped blobs and inventory, persisted reproducible commands, re-resolved and compared the tag tuple immediately before integration, then used an isolated result branch plus expected-head CAS and final evidence ref/blob readback before accepting `release_verified`.
- `hands_off_three_gates_to_github_release`: PASS. The handoff carries confirmed site Release Notes, `ready_for_tag`, `release_verified`, and a separate current maintainer publish-approval requirement.
- `preserves_no_mutation_boundaries`: PASS. No host/remote tag or GitHub Release write occurred.

## Without-Skill Baseline

- Source: freshly generated from the same prompt and pristine v3 fixture after the batch-polish repair; it read no skill, Agent README, internal instructions, old comparison, historical baseline or with-skill content.
- Result: 8/8 assertions PASS.
- It independently resolved the same Git object chain, recomputed the inventory/lineage/tag-tuple evidence, reran `test:api` and `test:docs`, verified the pre-tag and post-tag expected-head transactions and produced the same gated handoff and mutation boundary.
- No historical baseline was reused.

## Failures

- Assertion failures in with-skill: none.
- Assertion failures in without-skill: none.
- Independent judge blockers: none.
- Fixture `npm run test:api`: passed in both lanes.
- Fixture `docs/site` `npm run test:docs`: 73/73 passed in both lanes.
- Non-blocking dependency diagnostic: both isolated `npm ci` runs reported 2 moderate and 1 high audit findings from the committed fixture lockfile; no eval assertion depends on dependency-vulnerability remediation.
- Comparative limitation: the baseline also passed 8/8, so the eval currently measures object-level release-chain correctness rather than skill-specific uplift.

## Next Steps

- Keep the durable result `PASS` for fixture fidelity and protocol executability.
- If future changes need to measure skill uplift, add a separate ambiguity or missing-evidence case where the correct behavior depends on the skill's blocking and handoff rules rather than on a fully specified executable fixture.

## Runtime Artifact Policy

- Candidate outputs, runtime Git repositories, dependency installs, transcripts, timing, diagnostics and the judge verdict remain under `tmp/eval-runs/130-batch-polish/fresh-r7-20260720/` and are not committed.
- This `comparison.md` is the only durable model-eval result.
