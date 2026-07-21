# Eval Result: github-release-generator-outline-sections-quality-exclusion

## Evaluation Target

- Skill: `github-release-generator`
- Test case: outline 四节结构、内部质量证据排除与风险事实保持
- Latest result: **PASS** - 2026-07-22 issue #154 r2 fresh paired validation；with-skill 3/3、without-skill 3/3 assertions 通过

## Review Context

- Review issue: #154
- Final judge: 当前会话中的 fresh Codex validation agent
- Judge 独立读取当前 skill、两份 reference、eval-005 定义/metadata/fixture 和 issue #154 r2 fresh 双侧 candidate；verdict 完成前未读取 durable `comparison.md` 或旧首轮 tmp。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed site Release Notes、curated GitHub evidence、adjacent presentation suggestions 与 internal quality evidence
- With-skill evidence: `tmp/eval-runs/issue-154/r2-final/with_skill/eval-005-outline-sections-quality-exclusion/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-154/r2/without_skill/eval-005-outline-sections-quality-exclusion/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-154/r2-final/judge/verdict.md`

## Assertions

- PASS `follows_outline_sections`: 双侧 Release body 都仅有 `重点更新`、`其他改进`、`升级说明`、`变更明细` 四个 H2；with-skill 的 H3 重点细分不构成额外 peer section。
- PASS `excludes_internal_quality_evidence`: 双侧都未包含 skill eval、assertion 数、review 轮次、QA 汇总或相邻材料建议的额外小节。
- PASS `preserves_confirmed_facts`: 双侧都保留文件卡片与原位重试、统一附件兼容链路、nullable JSONB/backfill/删列风险、部署顺序与开关、双架构/static asset、升级步骤及旧浏览器限制。

## With Skill Behavior

- 生成 release title/date 与严格四节正文，仅用代表性 PR/commit 支撑已确认事实。
- 明确保留删列丢失附件元数据与备份要求，没有把 rollback 描述为无损或安全。
- 排除全部内部质量材料，并在 latest 证据缺失时给出保守 flags；本轮只读无写入。

## Without Skill Baseline

- 来源：issue #154 fresh baseline，基于同一 prompt 和 fixture；未读取或应用 skill、reference、Agent README、with-skill 输出或历史 comparison。
- 行为：同样 3/3 assertions PASS，严格使用四个 H2，排除内部质量证据并保持全部确认事实。
- 差异：baseline 缺少 release-outline 的 title/date framing、handoff/window 与 latest/prerelease evidence；不影响本 eval 三项 targeted assertions。

## Failures / Findings

- 无 with-skill assertion failure、事实遗漏、风险弱化或越权写操作。
- 非阻塞 finding：fixture 与 assertions 对四节结构和排除内容提示较强，fresh baseline 同样全部通过。

## Next Steps

- 保留当前 outline 与风险限定规则；修改 release outline、质量证据排除或风险转换规则时重新运行。
- 若需衡量完整 gate/flags 展示的增益，应使用独立 assertions 覆盖，而不是扩大本用例既有结论。

## Runtime Artifacts Policy

- issue #154 双侧 candidates 与 judge verdict 位于上列精确 r2 scratch 路径，属于未提交运行期诊断产物。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、manifest、verdict、outputs、timing、run status 或 diagnostics。
