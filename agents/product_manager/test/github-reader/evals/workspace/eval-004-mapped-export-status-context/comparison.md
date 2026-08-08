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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `cbc27cddf5543ee4c60ccd8f54bf10c1ec8b7799d5c9eb603008973679be6d9f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c9320af546c098adb51ac45faa524e2216c221f13ecd2b33fb2f8f822f024522`
- Metadata SHA-256: `d12a4df00a2f5f04d2bf0e553078ba3dc62e403dd0f77a037fb5796abdce7123`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 锁定原始证据无法证明候选的文档读取顺序。 |
| `verifies_against_code` | PASS | 明确以 handler.txt 的 CSV 声明核证文档的 CSV+JSON 声明，并结构化说明格式不一致及交付风险。 |
| `treats_unverified_as_low_trust` | PASS | 识别 last_verified_version: unverified，并明确不应据此认定 JSON 或整体实现已交付。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c; fixture_sha256=b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63; output_sha256=ba8b9a8df2f59bed024c9084429adac3a936d28e4fad27f216ddd868da4a1037; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成代码核证、冲突分析和低信任处理；读取顺序无法由锁定证据验证。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c; fixture_sha256=b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63; output_sha256=937330f8135ccff8c426bd20842c5e2c54cf7fa54eed084676c43053cad37875; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 CSV/JSON 声明冲突及未验证状态，但包含更强的未由当前锁定 fixture 直接支持的过程与仓库断言。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `6e29f2b22f72bb9078ec886f3bf0d4599e102bac697619f52f799318f68df6c7`
- Skill overlay SHA-256: `08b4455eaa3f2baaf8b11c20e163fe95beeff153e05846e54d69f650a80acb16`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c9320af546c098adb51ac45faa524e2216c221f13ecd2b33fb2f8f822f024522`
- Metadata SHA-256: `d12a4df00a2f5f04d2bf0e553078ba3dc62e403dd0f77a037fb5796abdce7123`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill cites the change-map and the mapped docs/site/api/export.md, with no evidence of full-repository document traversal. |
| `verifies_against_code` | PASS | with_skill explicitly verifies src/export/handler.txt as CSV-only and structures the conflict with the documentation’s CSV+JSON claim and associated delivery risk. |
| `treats_unverified_as_low_trust` | PASS | with_skill identifies last_verified_version as unverified and does not treat documented JSON support as delivered. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c; fixture_sha256=b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63; output_sha256=7dffc3e8d30287d69f7cff9db8dd690ef57f0c6daa32811fc3c09a1515797361; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Targeted the mapped documentation, cross-checked it against handler.txt, and treated unverified metadata as low trust.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c; fixture_sha256=b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63; output_sha256=88e01cdacc304f39201572f5fc76b1f6d7b32734a3a8724e6c56aee20ac19241; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a generally correct risk summary, but with less explicit evidence structure and verification detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `254cc92cf58649aa2c5bb2447fe35aa135bdc944368afe7a7cc119c6e2735ba1`
- Skill overlay SHA-256: `86a7dea13dce1a60e9d0c4442e983c46d3a33318b7a112994f13359d56bd6e12`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c9320af546c098adb51ac45faa524e2216c221f13ecd2b33fb2f8f822f024522`
- Metadata SHA-256: `d12a4df00a2f5f04d2bf0e553078ba3dc62e403dd0f77a037fb5796abdce7123`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill 明确引用并围绕 docs/site/api/export.md 评估 src/export/，同时提及变更映射规则，未显示全库文档遍历。 |
| `verifies_against_code` | PASS | with_skill 以 src/export/handler.txt 的 supported_format: csv 与 status: ready 核证，并明确指出文档声称 CSV/JSON 与实现不一致，结构化说明功能、契约和发布风险。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 将 last_verified_version: unverified 解释为未形成可追溯验证结论，未把文档中的 JSON 支持认定为已交付能力。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c; fixture_sha256=b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63; output_sha256=2066f5ed2443c3a3b203497578446670ed64b1503e45283c52627b8a29ef4a6c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样核对了文档与 handler.txt，明确按未验证证据降低信任，并更结构化地说明交付、契约、验证和发布风险。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c; fixture_sha256=b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63; output_sha256=2c324374ae3812c3135be7a048730475cc464e2e6f6081ed40c74de6df3ad91f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了 CSV 实现占位、文档中的 JSON/CSV 声明冲突及未验证风险，并给出不宜正式交付的结论。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-004-mapped-export-status-context

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-004-mapped-export-status-context`
- Test case: `结合映射文档汇总导出模块状态`
- Prompt:

> 请根据仓库内的现有证据，汇总 `src/export/` 模块当前的交付状态与风险。

- Expected output:

> 精准读取导出 API 文档，以代码核证实现状态并指出文档与实现不一致。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `6bf5af1937dcff508b0a43fc05937595b1549a6cf153cd58ae1400d8d7c6f166`（3 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Overall result: PASS
- With-skill summary: with_skill 实际加载 github-reader（status.json skill_load_hits=2；transcript item_1 读取 SKILL.md），按 change-map 定位并核验导出文档与代码，输出明确指出 CSV/JSON 分歧及 unverified 风险。未发现评测脚手架泄漏或写入行为。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载 github-reader（status.json skill_load_hits=2；transcript item_1 读取 SKILL.md），按 change-map 定位并核验导出文档与代码，输出明确指出 CSV/JSON 分歧及 unverified 风险。未发现评测脚手架泄漏或写入行为。

## Without-Skill Baseline

without_skill 未加载 skill（skill_load_hits=0），虽也识别出 CSV/JSON 不一致，但未遵循 with_skill 的映射优先读取证据链；仅作对照，不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `reads_mapped_docs_first` | **PASS** | transcript 先在 item_3 读取 docs/site/standards/change-map.yaml，命中 src/export/** 后读取 docs/site/api/export.md（item_14、item_15）；未成功执行全库文档内容遍历，item_4 的 README* 命令因无匹配直接失败。 | without_skill 的 transcript item_1 先检查 src/export/.github，之后才在 item_4 读取文档，且 status.json 的 skill_load_hits 为 0。 |
| `verifies_against_code` | **PASS** | transcript item_12 读取 src/export/handler.txt，输出 supported_format: csv；item_14 读取 export.md，输出 CSV and JSON。candidate.md 明确结构化说明“handler 仅支持 CSV”而文档声称 CSV 和 JSON，并指出交付风险。 | without_skill 也读取并描述了 handler.txt 与 export.md 的格式冲突，但未使用已加载 skill 的映射流程。 |
| `treats_unverified_as_low_trust` | **PASS** | change-map 与 export.md 均显示 stage: dev、last_verified_version: unverified；candidate.md 明确写为“尚未完成正式验证/发布确认”，并将 JSON 声明视为不能直接当作已验收交付。 | without_skill 同样将 dev/unverified 视为未完成验证，但其 skill_load_hits=0。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- 无；本轮覆盖全部 assertions。

## Next Steps

- 保留当前回归覆盖；目标 skill、fixture 或 assertion 契约变化时重新执行 fresh paired validation。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `63.643s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `55.778s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `90.567s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
