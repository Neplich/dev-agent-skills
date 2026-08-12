# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-005-mapped-cache-debug-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d` from `agents/engineer/test/debugger/evals/workspace/eval-005-mapped-cache-debug-evidence`.
- Identity schema: `2`
- target_skill_sha256: `218d8421a500762a8737dfd3f2bf066dd7538a5a365e0edae4e1ea20de7193fa`
- eval_definition_sha256: `793c3f5cce4575964aaa387ece63f94a0f71e528641010e1ee2d932bd04007a8`
- metadata_sha256: `296cf62658138bf9e31e0fd2b92d8abed954cf84bd5c6bd08af68865f72fdfc1`
- fixture_sha256: `5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b`
- Repository HEAD: `2ac10136f4ed18048058361915e66c52b4e038c5`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `fedd8e32348dc4f6f1f32b441d70612bfa38665135f0ba44f73fa280659d9268`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | With-skill trace shows a broad `rg --files -uu` traversal of unrelated `.agents/skills` documents before reading the mapped API document, so the no-unrelated-docs requirement is contradicted. |
| `verifies_against_code` | PASS | The with-skill report identifies `src/cache/ttl.txt` as `ttl_seconds: 60`, the API document as 300 seconds, runs a deterministic mismatch check showing a 240-second delta, and structures the code-versus-document discrepancy and conditional runtime conclusion. |
| `treats_unverified_as_low_trust` | FAIL | The with-skill report records both documents as `last_verified_version: unverified` and notes alignment uncertainty, but its reproduction and root-cause comparison still use the unverified document's 300-second claim and it does not explicitly treat that claim as lowest-trust evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b; fixture_sha256=5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d; output_sha256=dc9d0ba01d0cf0668343583e6bb176b1499195b915df09a0d06f2dde5211e0f2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a structured, read-only diagnosis with direct TTL mismatch evidence and correctly preserved uncertainty about whether the configuration is loaded at runtime, but violated the mapped-document read discipline and did not fully operationalize the unverified-document trust rule.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b; fixture_sha256=5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d; output_sha256=54dd5ba76a4cadb90e7beaf76d68739af74cd7f2f15538afcf363b42351be7c6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also found the 60-second versus 300-second mismatch and reported a plausible root cause, but did not explicitly address unverified-document trust or mapped-document-first process.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill lane traversed unrelated skill documents before reading the mapped document.
- The with-skill lane did not clearly assign lowest trust to the unverified document and relied on its 300-second claim in the reproduction/root-cause comparison.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
