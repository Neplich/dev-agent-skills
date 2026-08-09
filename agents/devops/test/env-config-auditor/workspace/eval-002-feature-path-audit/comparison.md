# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-002-feature-path-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a481b5374544e745048b6d91a89eb4240f2b8d26afa6409ed21d0c822a29f8c9` from `agents/devops/test/env-config-auditor/workspace/eval-002-feature-path-audit`.
- Fixture SHA-256: `a481b5374544e745048b6d91a89eb4240f2b8d26afa6409ed21d0c822a29f8c9`
- Prompt SHA-256: `45dd97708d4498ba2c5e31fb882b1692d7db80756c144b5c54d249bddbdf8a4b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- Skill overlay SHA-256: `ce7aff0f7795c878221dac5c9435b88a48e75e2799c5f15832edbd27f5f6796f`
- Judge schema SHA-256: `542a3960b92dfab31d619dba36f1b4cd7435eaeb67ca74c65c1e8dc7cd584d0a`
- Eval definition SHA-256: `6efcde24d7900ac81923c70a8eb454a7b5687569fc19e166e7a2702223bf20b8`
- Metadata SHA-256: `ed9d0f761d7a235166a80b0e2724cd90628f15321561b77d0b2d2233a2c87014`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_confirmed_feature_path` | PASS | The delivered report uses feature_path `chat-interface/messages/history/search` and names both required Engineer documents: `TRD.md` and `IMPLEMENTATION_PLAN.md`. |
| `writes_nested_devops_report` | PASS | The delivery snapshot contains `docs/devops/chat-interface/messages/history/search/ENV_AUDIT.md`, exactly matching the required nested path. |
| `does_not_invent_feature_directory` | PASS | The confirmed feature directory exists in the fixture, both required Engineer documents are present, and the report preserves that path without inventing a top-level synonym. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=45dd97708d4498ba2c5e31fb882b1692d7db80756c144b5c54d249bddbdf8a4b; fixture_sha256=a481b5374544e745048b6d91a89eb4240f2b8d26afa6409ed21d0c822a29f8c9; output_sha256=0df65549c69908b3b63a65769da643ef51ac42fec492c8cb12dd9ccfb911c040; snapshot_sha256=4fdfd60988b4ef873ac96086ee94a4fa07ca0f736689c7cd305bd2188ef5320f
- Behavior: Produced the required DevOps audit at the confirmed nested feature path and grounded it in the matching PM/Engineer documents.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=45dd97708d4498ba2c5e31fb882b1692d7db80756c144b5c54d249bddbdf8a4b; fixture_sha256=a481b5374544e745048b6d91a89eb4240f2b8d26afa6409ed21d0c822a29f8c9; output_sha256=9b19907b36ec30705ad8e44597c8b2bd45855686e4435a4c81dbebfa19d70a64; snapshot_sha256=08dbd1d1b993094bc004deeacf6043649abfdeb9b0900cfb723f01a919745827
- Behavior: Produced an audit under the Engineer directory instead of the required nested DevOps report path.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
