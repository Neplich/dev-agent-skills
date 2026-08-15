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
- target_skill_sha256: `c0b1e18b3568600a341fb92e0707fa60519d894609db128400ea4504b1db7cdd`
- eval_definition_sha256: `7e02d3842aadb84c2bf63d29c927cc522ebed52b96eed1878122982c38563924`
- metadata_sha256: `6195fe8fa63ec704ffc4c5d4393b601e3bddd8538af8edff5e40ff8efed24331`
- fixture_sha256: `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `eaac8d5ec4179daca7a6c1c98e4847ae0114d9d33168a84593f70ca6474abe10`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `dfabcb8a58e3d266746b53d78f0ea389e3a5922e474255e9b923da1ebd7a697b`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feature_branch_created` | PASS | git_evidence shows branch changed from main to fix/notification-status, a project-conformant feature branch. |
| `meaningful_commit_created` | NOT_EXERCISED | No commit was created because Git identity was unavailable; the requirement could not be exercised. |
| `pr` | PASS | With no remote or gh, the candidate explicitly reported the blockers and provided a PR preview containing title, issue reference, scope, PRD/evidence references, and test status without claiming a PR existed. |
| `ci` | PASS | No PR existed, so CI was not read; the candidate explicitly reported CI unavailable, explained the blockers, and provided a recovery/readback command. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=b5ee47ff4bbf5336fa543775b8b8e659d4c7389eef8e88a521cd993a64d3e2e1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Created a correctly named feature branch, staged the scoped changes, verified tests, and produced an accurate blocked-delivery PR/CI preview.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=4dc2fedd3f182c5f01b04e0410d796895eb990645b61eeb922e500977034b6d6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Verified tests but stopped at the missing Git identity and remote, without creating a branch or providing the required PR preview and CI recovery details.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Configure Git identity, create the meaningful commit, configure a remote, push the feature branch, create the PR, and then read CI status.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
