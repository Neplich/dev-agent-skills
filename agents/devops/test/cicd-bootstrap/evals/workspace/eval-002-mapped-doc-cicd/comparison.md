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
- Fixture SHA-256: `b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482`
- Prompt SHA-256: `08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `86f7228d11d9f7ad3ec145d83be1c28f8a4bb93afea61016f55ed2860069bc68`
- Skill overlay SHA-256: `c8eba5ff7fa14d3a9d17d2f0e6e7ee710355737a3424af1c887580cc79ea33c4`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `68a87fb5d229c5c451c4b7081adb9e28c9c2e68f2832958c12f8d53464b0ae13`
- Metadata SHA-256: `a6802835ad6096782cd89b2c4280b4422a56ff9be96ac885a939daae8583297c`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill 的锁定 trace 显示先读取 pipeline.rules，再读取 change-map.yaml，随后精准读取 build-pipeline.md；未遍历无关站点文档。 |
| `verifies_against_code` | PASS | with_skill 明确指出文档写的是 test，而代码配置为 validation_command = verify，并据此要求执行 verify、拒绝执行 test，说明了错误命令不能作为实际流水线命令。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 识别构建文档的 last_verified_version 为 unverified，并以代码配置核证 verify，同时明确未发现执行器证据、不臆造安装步骤。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4; fixture_sha256=b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482; output_sha256=67a7b2d5644ca39e43c1004563a8ce9499e997990b741c7ce26c58b78e01c599; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确完成映射文档读取、代码核验和低信任处理；给出 verify 及最小 CI job，并保留执行器与交接边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4; fixture_sha256=b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482; output_sha256=ab0f6ecdba87fc2ea7baf30559820c5a8804690bed724da3b5251d842a0c3067; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 也识别出 verify 与文档 test 的冲突并给出命令，但未呈现同等完整的证据边界。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
