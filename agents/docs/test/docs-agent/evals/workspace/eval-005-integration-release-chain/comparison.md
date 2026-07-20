# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`
- Scenario: AI Hub-shaped formal-docs release chain from host contract through GitHub Release handoff

## Test Set / Fixture Version

- Fixture: `issue-115-ai-hub-shaped-v1`
- Fresh run: `tmp/eval-runs/115/fresh-r2-20260720-0958/`
- Source head: `65111551229143ca7ec39e513f33908249125772` plus the issue #115 working tree
- Harness: with-skill received complete `agents/docs/`, `github-release-generator`, and PM shared contracts; without-skill received the same prompt/fixture with zero skill or Agent README; a separate fresh judge reviewed the frozen outputs.

## Latest Result

**PASS（with-skill 8/8 assertions；without-skill 2/8）** — with-skill completed the shared frontmatter and template checks, API/change-map reconciliation, confirmed site Release Notes handoff, pre-tag `ready_for_tag`, post-tag `release_verified`, and the gated `pm-agent:github-release-generator` handoff while preserving zero tag/Release mutation.

## With-Skill Behavior

- `validates_shared_frontmatter_contract`: PASS. Checked all 19 formal Markdown pages, the seven-field contract and enums; the five templates use target doc types and received structure-only placeholder exemption.
- `uses_host_templates_and_scaffold`: PASS. Treated the host's five templates, `scaffold-doc.mjs`, `npm run new:doc`, manifest, and package scripts as the single writing foundation.
- `reconciles_api_sync_and_change_map`: PASS. Reconciled Approved PRD, Confirmed TRD/plan, `GET /api/search` code/tests, the API page, and the precise change-map rule.
- `accepts_confirmed_site_release_notes_handoff`: PASS. Verified the confirmed page, metadata, index, docs checks, frozen version inventory, evidence, and Docs/PM ownership boundary.
- `completes_pre_tag_ready_for_tag`: PASS. Used immutable refs, the full affected set, unified stamp set, candidate/discovery anchors, convergence, post-commit confirmation, and integration readback before `ready_for_tag`.
- `completes_post_tag_release_verified`: PASS. Bound the simulated peeled tag tree to the trusted handoff tree, reused the exact inventory, normalized source-specific version forms, and returned an independent `release_verified` result without regeneration or restamping.
- `hands_off_three_gates_to_github_release`: PASS. The handoff names `pm-agent:github-release-generator`, carries the confirmed site handoff, `ready_for_tag`, and `release_verified`, and still requires separate current maintainer publish approval.
- `preserves_no_mutation_boundaries`: PASS. Reported zero real tag and GitHub Release writes.

## Without-Skill Baseline

- Source: freshly generated from the same prompt and pristine R2 fixture after the with-skill output was frozen; it read no skill, Agent README, harness, comparison, R1, historical baseline, or with-skill content.
- Passed 2/8 assertions: API/change-map reconciliation and zero mutation.
- It did not fully establish the shared frontmatter/template contract, #122 single-template source, site Release Notes ownership and frozen inventory, pre-tag candidate/discovery transaction, post-tag same-inventory/no-restamp result, or PM-owned three-gate handoff.

## Failures

- Assertion failures in with-skill: none.
- Harness contamination: none observed.
- R1 was discarded rather than reused: it correctly exposed an invalid fixture value in `.meta/releases.json`; after changing `verifiedDocs` from `unverified` to `v1.4.0`, the corrected fixture passed host `npm run test:docs` with 73/73 tests, and R2 regenerated both candidates from scratch.
- Non-blocking limitation: candidate/discovery/post-tag fixed-path records were represented in the semantic candidate output rather than physically persisted as independent runtime files. A future deterministic Git runner should cover actual object/tree persistence and readback.
- Assertion granularity risk: assertions 1, 5, 6, and 7 combine multiple independently failing conditions; this did not make the R2 decision ambiguous.

## Next Steps

- Keep the result `PASS` for issue #115 integration coverage.
- If persistence behavior changes, add a deterministic temporary-Git runner and split the compound assertions before using the eval for object-level transaction regression.

## Runtime Artifact Policy

- R1/R2 candidate outputs, runner reports, judge verdict, dependency installs, transcripts, timing, and diagnostics stay under `tmp/eval-runs/115/` and are not committed.
- This `comparison.md` is the only durable model-eval result.
