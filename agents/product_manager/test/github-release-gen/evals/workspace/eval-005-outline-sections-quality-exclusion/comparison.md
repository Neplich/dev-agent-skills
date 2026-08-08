# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-005-outline-sections-quality-exclusion`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-005-outline-sections-quality-exclusion`.
- Fixture SHA-256: `f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79`
- Prompt SHA-256: `1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ebd2c00966a7932d251daeeef05573b0145183fe908cf102225636115f85820c`
- Skill overlay SHA-256: `2398a04c1c550bc8e45aa1564f5f42f6e629a29d1c1ed530494ae269f918d169`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5768440d836f6d58f2492f6254c4eaae18fe913a310437aaee98134c39857a50`
- Metadata SHA-256: `a9879c47e38cec76a35a3ff0087c5b764086d8e7ca04745f8977bbd30db8f459`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `follows_outline_sections` | PASS | 正文仅含“重点更新”“其他改进”“升级说明”“变更明细”四个二级小节。 |
| `excludes_internal_quality_evidence` | PASS | Release 正文未包含 skill eval、断言计数、QA、review 或其他内部审计证据。 |
| `preserves_confirmed_facts` | PASS | 正文保留了文件卡片、原位重试、统一附件模型、nullable JSONB 迁移与删列风险、部署顺序和开关、双架构资产、升级动作及旧浏览器限制等确认事实。 |
| `title_matches_gate` | PASS | 标题为“v1.0.0 - 文件卡片、失败消息重试与统一附件模型”，不是裸版本号。 |
| `upgrade_note_fixed_structure` | PASS | “升级说明”包含完整升级顺序、验证与开关步骤及风险收尾；未生成未确认的客户端或 plugin 小节。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79; output_sha256=35074e1497419536eb25973d680239c483858e2ac996ce736e2c4ccc429478b0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了符合四节结构的 Release 正文，排除内部审计内容，并完整保留确认事实与升级风险。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79; output_sha256=789584f865c3f539e695dc38fa94f18530ffe2bca546ba4e623f11112416f054; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 使用了非约定小节，并包含内部质量证据；部分事实结构与升级说明不符合门禁。
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

# Eval Result: eval-005-outline-sections-quality-exclusion

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-005-outline-sections-quality-exclusion`
- Test case: `outline 四节结构与内部质量证据排除`
- Prompt:

> 请根据 `release-package.md`、`docs/site/release-notes/v1.0.0.md` 和 `github-evidence.md` 准备 GitHub Release 预览。

- Expected output:

> 预览逐项保持已确认的功能、架构、数据库、部署、资产、升级与风险事实；标题不是仅版本号的无语义裸标题（本 fixture 为非 marketplace 宿主且未定义明确标题惯例，含事实主题概述或遵循宿主惯例均为合格）；正文只包含重点更新、其他改进、升级说明、变更明细四节，不采用相邻风格小节，也不包含 skill eval、assertion 计数、review 轮次或 QA 证据汇总；升级说明按固定结构完整呈现（简述与适用时的指令小节/收尾句），本 fixture 事实源未确认 coding-agent 客户端升级入口时不得生成空壳小节或臆造安装命令，plugin 更新类声明只在已确认事实源支持时使用（本 fixture 事实源不含 plugin 更新事实，不得臆造），不只写占位句。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `7c69c14e8240bc01c846c12bf7983be7360a5e3ed10a353f621b22dddf4d8177`（3 个可见文件；两侧逐字节一致）。
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
- With-skill summary: with_skill 实际加载 github-release-gen（status skill_load_hits=2；transcript 先读取 SKILL.md、参考规范，再读取三份事实材料），按四节生成预览，排除了内部质量证据，未执行写操作；快照前后一致。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载 github-release-gen（status skill_load_hits=2；transcript 先读取 SKILL.md、参考规范，再读取三份事实材料），按四节生成预览，排除了内部质量证据，未执行写操作；快照前后一致。

## Without-Skill Baseline

without_skill 仅作对照：生成了包含约定外小节和质量验证的预览，并写入了新文件。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `follows_outline_sections` | **PASS** | with_skill 正文仅含“重点更新”“其他改进”“升级说明”“变更明细”四个二级节；transcript 明确称相邻风格小节未纳入正文。 | FAIL：without_skill 预览包含“发布亮点”“架构与部署”“升级与风险”“质量验证”“维护者说明”等约定外小节。 |
| `excludes_internal_quality_evidence` | **PASS** | with_skill candidate 明确写出“内部评估、QA 和相邻风格小节未纳入用户正文”，正文未出现 skill eval、assertion 计数、review 轮次或 QA 汇总；transcript 也记录了排除行为。 | FAIL：without_skill 预览实际包含“质量验证”节，且其 agent_message 明确说明正文包含质量验证。 |
| `preserves_confirmed_facts` | **PASS** | with_skill 正文逐项保留文件卡片、失败消息原位重试、统一附件模型兼容链路、nullable JSONB message_files 迁移与删列风险、部署顺序与开关、amd64/arm64 资产、升级步骤及旧浏览器限制；内容与 release notes 及 release-package.md 一致。 | FAIL：without_skill 对 workflow_finished/统一附件模型作了泛化改写，并将多项事实重组为非目标结构；未完整按确认事实呈现。 |
| `title_matches_gate` | **PASS** | with_skill 标题为“v1.0.0 - 文件卡片、失败消息重试与统一附件模型”，不是裸版本号；fixture 为非 marketplace 且未定义明确命名惯例，符合门禁。 | PASS：without_skill 标题“AI Hub v1.0.0”也不是裸版本号。 |
| `upgrade_note_fixed_structure` | **PASS** | with_skill 的“升级说明”包含备份简述、数据库迁移/部署/验证/开关顺序及回滚风险收尾；未生成 Claude Code、Codex、Kimi Code 空壳小节或安装命令，也未臆造 plugin 更新。fixture 事实源不含 plugin 更新事实，candidate 与之相符。 | FAIL：without_skill 使用“升级与风险”而非固定“升级说明”节，且未按固定升级说明结构完整呈现。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- 无；本轮覆盖全部 assertions。

## Next Steps

- 保留当前回归覆盖；目标 skill、fixture 或 assertion 契约变化时重新执行 fresh paired validation。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `116.363s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `69.8s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `73.025s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
