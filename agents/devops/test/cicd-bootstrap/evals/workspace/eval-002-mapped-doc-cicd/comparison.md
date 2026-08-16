# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-002-mapped-doc-cicd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482` from `agents/devops/test/cicd-bootstrap/evals/workspace/eval-002-mapped-doc-cicd`.
- Identity schema: `2`
- target_skill_sha256: `b41596991874aec0c37e12acb656078a02504e51d6536f47c1befab8e1f38b4a`
- eval_definition_sha256: `68a87fb5d229c5c451c4b7081adb9e28c9c2e68f2832958c12f8d53464b0ae13`
- metadata_sha256: `7e07a230c7002251551f1819be2a41bc3021e8c2cf111ff3359550f2215bd97f`
- fixture_sha256: `b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `777451b1778a899115de1846bd3248acc1a8fef07fa6857039ca7e40cdac46e8`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace reads the mapped change-map, then docs/site/api/build-pipeline.md, and does not traverse unrelated site documents. |
| `verifies_against_code` | FAIL | Trace never reads src/build/pipeline.rules and reports the stale document command test as the only recommendation, without identifying the code-required verify command or its impact. |
| `treats_unverified_as_low_trust` | PASS | Trace explicitly identifies last_verified_version: unverified and treats the document as low-trust navigation, declining to promote test to a confirmed CI command. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4; fixture_sha256=b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482; output_sha256=d133e9ca06a198f2cb612eb64f93fad58126c1dec6ce2048dc7a61941a802d72; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Read the mapped documentation and correctly treated it as unverified, but failed to reread the code and therefore did not determine the actual command.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4; fixture_sha256=b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482; output_sha256=94dae005553ee8d06686ec7487a4f615e58f060c2dfb46363144e8863c87dab2; snapshot_sha256=572411d82fb534e72979f510e527b0a194a160b5a408b6d4d2f4141c2639c92e
- Behavior: Created a workflow using verify and corrected the documentation, but is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane stopped at an unsupported PM/DevOps handoff gate and omitted the required code verification, so it failed to determine the actual CI command verify.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
