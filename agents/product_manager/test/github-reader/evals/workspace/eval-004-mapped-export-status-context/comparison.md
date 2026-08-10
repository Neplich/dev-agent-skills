# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-004-mapped-export-status-context`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63` from `agents/product_manager/test/github-reader/evals/workspace/eval-004-mapped-export-status-context`.
- Fixture SHA-256: `b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63`
- Prompt SHA-256: `c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `b0004c5792dae6a7d4050cf6839b7073909210717e4fcd3dd4b28188da158276`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `c9320af546c098adb51ac45faa524e2216c221f13ecd2b33fb2f8f822f024522`
- Metadata SHA-256: `d12a4df00a2f5f04d2bf0e553078ba3dc62e403dd0f77a037fb5796abdce7123`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill 的锁定 trace 先读取 change-map，随后读取其命中的 docs/site/api/export.md；未执行全库文档内容遍历。 |
| `verifies_against_code` | PASS | 最终输出以 src/export/handler.txt 的 supported_format: csv、status: ready 核证，并明确指出文档声称 CSV/JSON 与代码侧 CSV-only 的分歧及交付风险。 |
| `treats_unverified_as_low_trust` | PASS | 最终输出明确将 API 文档和 change-map 中的 last_verified_version: unverified 视为低信任，未将 JSON 文档声明当作已交付能力。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c; fixture_sha256=b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63; output_sha256=ec1fb5e3985f04a9cc55aee38bab5c36d180cb4775c3e36ffc7507b6261b1212; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 按 change-map 定位并核验 API 文档，再回代码确认 CSV/JSON 分歧；正确按 unverified 降低文档信任并报告风险。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c; fixture_sha256=b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63; output_sha256=4668d64f4c2dfd1b198c087053a9e5e0408b52d9a834850ee3fe7380dbc0b887; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 也识别了 CSV/JSON 分歧和 unverified 状态，作为 fresh baseline 与 with_skill 结果一致。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
