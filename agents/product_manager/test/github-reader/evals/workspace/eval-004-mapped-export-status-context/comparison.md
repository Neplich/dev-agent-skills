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
