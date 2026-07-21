# Eval Result: github-release-generator-site-less-degraded-gate

## Evaluation Target

- Skill: `github-release-generator`
- Test case: site-less host degraded gate with confirmed and missing fact-source scenarios
- Latest result: **PASS** - 2026-07-22 issue #154 r2 fresh paired validation；with-skill 4/4、without-skill 4/4 assertions 通过

## Review Context

- Review issue: #154
- Final judge: 当前会话中的 fresh Codex validation agent
- Judge 在未读取 durable `comparison.md` 或旧首轮 tmp 的前提下，先审阅当前 skill、两份 reference、eval-006 定义/metadata/fixture 与 issue #154 r2 fresh 双侧 candidate，并写出独立 verdict。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: site-less host with confirmed `v1.4.0` changelog/version-bump evidence，以及缺少 confirmed fact source 的第二场景
- With-skill evidence: `tmp/eval-runs/issue-154/r2-final/with_skill/eval-006-site-less-degraded-gate/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-154/r2/without_skill/eval-006-site-less-degraded-gate/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-154/r2-final/judge/verdict.md`

## Assertions

- PASS `proceeds_without_handoff_when_site_absent`: 双侧都证明 `docs/site/` 与 #116 capability chain 不存在后，将 #116/#117 handoff 判为不适用，并从可信事实源生成完整 preview。
- PASS `records_downgrade_basis`: 双侧都明确记录正式站点未初始化、两项缺失、confirmed changelog、version bump、tag/ref/range 与无冲突证据。
- PASS `still_requires_maintainer_approval`: 双侧都只生成 preview，未执行 draft/publish/tag/docs 写入；说明每次未来远端写入都要取得明确、当前批准；with-skill 还明确逐次重新验证降级依据和版本状态。
- PASS `blocks_without_confirmed_fact_source`: 双侧都对第二场景明确 blocked，拒绝从 proposed version、commit subjects 或 unconfirmed summary 臆造事实。

## With Skill Behavior

- 严格以“无 `docs/site/` 且无 #116 capability chain”作为降级的双重依据，不从 handoff 缺失本身推断降级。
- 使用维护者确认的 changelog 与一致的 version-bump evidence，生成四节 outline preview，并计算稳定 `1.4.0 > 1.3.2` 的 `--prerelease=false --latest` 决定。
- 对无可信事实源场景保持 blocked，并完整报告批准、revalidation 与零写入边界。

## Without Skill Baseline

- 来源：issue #154 fresh baseline，基于同一 prompt、eval 定义、metadata 与 fixture；未读取或应用 skill、Agent README、with-skill 输出或历史 comparison。
- 行为：四项 assertions 同样 PASS；记录双重降级依据、可信 changelog/version evidence、逐次批准要求，并阻塞无可信事实源场景。
- 差异：baseline 把兼容性与风险并入 `变更明细`，没有显式 latest/prerelease 决定；with-skill 的四节 outline 更接近 reference，并给出 exact flags。两者均满足 eval-006 当前四项 assertions。

## Failures / Findings

- 无 with-skill assertion failure 或 blocker。
- 非阻塞 finding：fresh baseline 也满足 4/4 targeted assertions；其 flags 缺口与风险信息编排差异提示 eval-006 尚未覆盖完整 preview outline/decision 协议。

## Next Steps

- 保留 issue #154 的 host-applicability 与 confirmed fallback fact-source 门禁实现。
- 若要求每个 site-less 完整 preview 都严格遵循四节 outline 并展示 exact latest/prerelease evidence，新增针对性 assertions 后重新执行 paired validation。

## Runtime Artifacts Policy

- issue #154 双侧 candidates 与 `tmp/eval-runs/issue-154/r2-final/judge/verdict.md` 都是运行期诊断产物，不得提交。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、manifest、verdict、outputs、timing、run status 或 diagnostics。
