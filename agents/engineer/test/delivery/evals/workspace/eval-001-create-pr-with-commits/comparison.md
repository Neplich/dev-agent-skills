# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e` from `agents/engineer/test/delivery/evals/workspace/eval-001-create-pr-with-commits`.
- Identity schema: `2`
- target_skill_sha256: `35b932d926c847250a65fcd91030100edda1fbe4469e964b40943b406212ff53`
- eval_definition_sha256: `7e02d3842aadb84c2bf63d29c927cc522ebed52b96eed1878122982c38563924`
- metadata_sha256: `6195fe8fa63ec704ffc4c5d4393b601e3bddd8538af8edff5e40ff8efed24331`
- fixture_sha256: `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `eaac8d5ec4179daca7a6c1c98e4847ae0114d9d33168a84593f70ca6474abe10`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `3bdd529a8630a74d53998f41a91c8989c63920095616267cbc63cd5952755e2a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feature_branch_created` | PASS | git_evidence shows branch changed from main to fix/notification-status, with a new reachable commit on that branch. |
| `meaningful_commit_created` | PASS | The new commit is f063291 with message `fix: support archived notification status`, satisfying Conventional Commits style. |
| `pr` | PASS | The candidate accurately reports PR creation blocked, provides a preview with title, issue reference, PM document, changed files, and test status, and does not claim a PR was created. Push failure due to missing origin is recorded in the trace. |
| `ci` | PASS | No PR exists; the candidate reports CI unavailable, explains the delivery blocker, and supplies the recovery/readback command `gh pr checks <pr-number> --watch` without fabricating CI results. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=e16e36ba46720b8c3fdbdc121812935cf5ddc6c04dd279c130cc02ca8b0c6980; snapshot_sha256=9d68bebad688eff59c6b7d8fdc578654dcd01d09e466fa530ccb2144b2cca7d4
- Behavior: Created a correctly named feature branch, made a Conventional Commit, verified tests, and produced an evidence-backed blocked PR preview with CI recovery instructions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=2619ed5194aa24c64dd6c1a081cea1558aaaf3173f5c10c7e9ca5ada2e6c57ed; snapshot_sha256=31c7a883309134fb39b588d17ffb881de687a17efc95456a3b70a7ffce384ddb
- Behavior: Committed directly on main with a non-Conventional message and reported the PR blocker without providing the required equivalent PR preview or CI recovery details.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Add the correct origin remote, push fix/notification-status, create the PR for Issue #123, then run gh pr checks <pr-number> --watch.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
