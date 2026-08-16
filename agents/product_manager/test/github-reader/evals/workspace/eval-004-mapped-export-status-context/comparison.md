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
- Identity schema: `2`
- target_skill_sha256: `99ea82f9c285d0cd51090c481c0892adf1bdf20367a2866bf82eabffdc17f4c7`
- eval_definition_sha256: `c9320af546c098adb51ac45faa524e2216c221f13ecd2b33fb2f8f822f024522`
- metadata_sha256: `d12a4df00a2f5f04d2bf0e553078ba3dc62e403dd0f77a037fb5796abdce7123`
- fixture_sha256: `b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `a9770b603fd249fd7f80da3e56ab1a6acb6432c1ad6dff3ad5cfc0e089124eab`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | with_skill 的锁定 trace 先读取 change-map，但同一命令随后先读取 handler.txt，再读取 export.md；因此未按映射文档优先于代码核证的顺序执行。 |
| `verifies_against_code` | PASS | 输出明确引用 handler.txt 的 supported_format: csv/status: ready，并指出 API 文档声称 CSV/JSON，结构化说明了文档与代码分歧及交付风险。 |
| `treats_unverified_as_low_trust` | PASS | 输出将 API 文档和 change-map 的 last_verified_version: unverified 视为证据新鲜度不足，未把 JSON 作为已交付能力。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c; fixture_sha256=b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63; output_sha256=5d8000c6522ed23f811d2fef1adf4ba17e4be745443076810a8d0535e7bc6740; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核证了 CSV/JSON 分歧并按 unverified 降低文档信任，但映射文档优先读取顺序失败。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c; fixture_sha256=b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63; output_sha256=6eb2069d908b926d4c16ba13463c8a830e4f370bad1802e2697e4d70eff45f1d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 独立识别了 CSV 与文档声明的 JSON 不一致及未验证风险；仅作基线对照，不影响 with_skill 判定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 的原始工具事件显示映射命中的 API 文档是在代码文件之后读取的，未满足优先读取映射文档的顺序要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
