# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b` from `agents/qa/test/spec-based-tester/evals/workspace/eval-3-mapped-doc-acceptance`.
- Identity schema: `2`
- target_skill_sha256: `a902e30cb15a83b00f6e242ec0746a619c9c75741852be4c26efbe1dc710f3e3`
- eval_definition_sha256: `69ea284c249fd48ea67518dcbbbb4aff0b51c724f5aa24139bc9524759db6c7c`
- metadata_sha256: `dbcf12ca577304c6eedeb3847e29d69b72d051700655cd6bd5000bc1d6f7a9d9`
- fixture_sha256: `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `2ae6df1e5892f15e69faa5eb27f67247be532cf172f30b6323b139a66d25acc0`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows the change map was read before the mapped formal document, followed by direct code inspection; the delivered record names both paths. |
| `verifies_against_code` | PASS | The locked delivery snapshot records the 80-character documentation statement, the 64-character code value, both paths, and the 65–80-character acceptance impact. |
| `treats_unverified_as_low_trust` | PASS | The snapshot explicitly identifies last_verified_version: unverified and treats the document as navigation-level evidence while grounding conclusions in code/static validation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=0a6429b83919950761268bcbe0afd44d83e1490cfc4cf82ba6b59d69c4666467; snapshot_sha256=ca5498bb08d400586fc5cb5579a7d73f8bda2776532789b143a8b4a80bb2f324
- Behavior: Used the change map to locate the formal document, verified its 80-character claim against the 64-character rule, treated unverified documentation as low trust, and delivered a traceable validation matrix.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=5ba98bb3891bc756c31a00b4d4ea8f0217ef6e5c98e2d5f09ecc821c451a7a52; snapshot_sha256=2d1ba59cac3478adf48e7942e7a7225f68ddb06b2e9664ae4a4902a1b111ebfa
- Behavior: Also identified the 64-versus-80 mismatch and delivered a simpler requirements matrix, but provided less explicit low-trust treatment and validation-process detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
