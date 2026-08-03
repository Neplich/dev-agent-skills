# Eval Result: github-release-generator-site-less-degraded-gate

## Evaluation Target

- Skill: `github-release-generator`
- Test case: site-less host degraded gate with confirmed and missing fact-source scenarios
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Overall result: PASS

## Review Context

- Issue: #190（Release 标题与升级说明质量门禁修复）
- Date: 2026-08-03
- Final judge: 当前会话中的 fresh Codex validation agent
- Judge 独立读取当前 skill、两份 reference、eval 定义/metadata/fixture 与 issue-190 fresh 双侧 candidate；verdict 完成前未读取 durable `comparison.md` 或旧 run tmp。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: site-less host with confirmed `v1.4.0` changelog/version-bump evidence，以及缺少 confirmed fact source 的第二场景
- With-skill evidence: `tmp/eval-runs/issue-190/with_skill/eval-006-site-less-degraded-gate/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-190/without_skill/eval-006-site-less-degraded-gate/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-190/judge/verdict.md`

## Assertions

- PASS `proceeds_without_handoff_when_site_absent`：证明 `docs/site/` 与站内 Release Notes 能力链均不存在后，将双态审计 handoff 判为不适用，并从可信事实源生成完整 preview；without-skill 同 PASS
- PASS `records_downgrade_basis`：明确记录正式站点未初始化、两项缺失、confirmed changelog、version bump、tag/ref/range 与无冲突证据；without-skill 同 PASS
- PASS `still_requires_maintainer_approval`：只生成 preview，未执行 draft/publish/tag/docs 写入，并说明每次未来远端写入都要取得明确、当前、不可复用的批准；without-skill 同 PASS
- PASS `blocks_without_confirmed_fact_source`：对第二场景明确 blocked，拒绝从 proposed version、commit subjects 或 unconfirmed summary 臆造事实；without-skill 同 PASS

## With Skill Behavior

- 严格以「无 `docs/site/` 且无站内 Release Notes capability chain」作为降级双重依据，不从 handoff 缺失本身推断降级。
- 使用维护者确认的 changelog 与一致的 version-bump evidence，生成四节 outline preview，并计算稳定 `1.4.0 > 1.3.2` 的 `--prerelease=false --latest` 决定。
- 对无可信事实源场景保持 blocked，并完整报告批准、revalidation 与零写入边界。

## Without Skill Baseline

- 来源：issue-190 fresh baseline（2026-08-03），基于同一 eval prompt 与 fixture；未读取或应用 skill、reference、Agent README、with-skill 输出或历史 comparison。
- 行为：4/4 assertions PASS；降级语义与 with-skill 一致。未见规则泄漏迹象，属模型可从 fixture 显式事实推导的通用门禁。

## Failures / Findings

- 无 assertion failure。
- 非阻塞 finding：本 eval 为「模型已内化」用例（without-skill 全过），区分度低但无泄漏；可作为 #188 正增量审查的数据点。

## Next Steps

- 保留 host-applicability 与 confirmed fallback fact-source 门禁实现；后续修改降级判据时重新执行 paired validation。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-190/`，属于未提交运行期诊断产物。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
