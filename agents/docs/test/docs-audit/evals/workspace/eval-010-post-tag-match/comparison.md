# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518` from `agents/docs/test/docs-audit/evals/workspace/eval-010-post-tag-match`.
- Fixture SHA-256: `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518`
- Prompt SHA-256: `47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143`
- Repository HEAD: `f34c1007244dc48cf04fcd5d073fc5949225f1bd`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7ed8638f6a80000c952068f188dbfe51d8ede83a52ee0b3635f473bf2d9da41d`
- Skill overlay SHA-256: `4183c2c4191ffb5278feb2ab2a6f8ac1fed136b346aab58bc7438d627c8d7660`
- Judge schema SHA-256: `f64d4542aa97d4b9bcd4bc655a5e70fec7d827a5ea9e9f63067fde8d7b819748`
- Eval definition SHA-256: `f4b575228474dd8bb2a93bb17a067f25252f9c293e1f78393d445c449385e8d2`
- Metadata SHA-256: `12f75879efa3cacf943ae19595239a747563947015e4033eed4ea7f4a51a5b47`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_pre_tag_authority_safely` | PASS | With_skill raw trace resolves refs/tags/v1.2.0 and refs/release-evidence/v1.2.0, performs a default clone, confirms no release-evidence refs in the clone, and reads the tag-contained handoff/audit while recognizing the fallback authority is incomplete. |
| `proves_released_tree_binding` | PASS | With_skill raw trace resolves the tag commit and tree, compares the release-evidence and tag trees, and inspects tag-tree blobs and clone-visible committed paths rather than relying only on commit identity. |
| `verifies_version_surfaces_from_release` | PASS | With_skill raw trace reads the four release surfaces from tag content, distinguishes v1.2.0 from package version 1.2.0, and does not treat the current worktree as successful release evidence. |
| `requires_durable_post_tag_evidence` | PASS | The with_skill output identifies the absent maintainer-confirmed result branch and expected head, notes the proposed ref has no decision, keeps both environments blocked, and does not convert content consistency into release_verified. |
| `preserves_upstream_release_artifacts` | PASS | Locked git evidence shows unchanged HEAD, branch, refs, worktree, index, reflog, and no result diffs; the with_skill output explicitly reports no ref, tag, or release-record mutations. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=5b68b76ff8d38b6845aa160e5ebd4129a8ef3acce18c822f2bf3bf928edbe2c9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performed the two-environment tag/tree review, identified incomplete authority and missing durable post-tag integration evidence, and preserved all upstream artifacts.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=b4160221f53b395300bffd430151f5f2b3bd49f51a10eb12381cee4ac35b69c7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reported tag and tree availability and artifact preservation, but incorrectly concluded the review could be independently completed without durable post-tag evidence and overclaimed tag-tree audit completeness.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain maintainer confirmation of the independent result branch and expected head.
- Next: Regenerate or supply complete committed pre-tag authority and missing code/test evidence, then rerun the post-tag review.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
