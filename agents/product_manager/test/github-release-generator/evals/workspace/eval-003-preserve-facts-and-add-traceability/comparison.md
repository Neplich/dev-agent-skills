# Eval Result: github-release-generator-preserve-facts-and-add-traceability

## Evaluation Target

- Skill: `github-release-generator`
- Test case: fact preservation and curated GitHub traceability
- Latest result: PASS - 2026-07-21 issue #146 fresh paired validation 完成，with-skill 4/4 assertions 通过

## Review Context

- Review issue: #146
- Final judge: 当前会话中的 fresh Codex validation agent
- 两条 lane 分别由全新 worker 生成；judge 在两侧完成前未读取历史 `comparison.md`。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped confirmed release page、pre-tag audited range、intended final compare 与 curated GitHub evidence
- Runtime evidence: `tmp/eval-runs/issue-146/{with_skill,without_skill}/eval-003-preserve-facts-and-add-traceability/`

## Assertions

- PASS `preserves_confirmed_release_facts`: 文件卡片、原位重试、统一附件模型与旧文本兼容、nullable JSONB 与删列风险、部署顺序与开关、双架构资产、升级和旧浏览器限制均逐项保留。
- PASS `adds_verified_traceability_links`: 使用 fixture 范围内 compare、PR #116/#117、direct commit `8b6a1f2` 与贡献者链接，并区分 pre-tag audited endpoint 与 tag 存在后的 final endpoint。
- PASS `curates_instead_of_dumping`: 围绕站内事实组织说明，仅选代表性维护链接，未粘贴其余 18 个格式化、依赖与测试 commit。
- PASS `blocks_on_fact_conflict`: 明确 GitHub 证据冲突或暴露新事实时返回 `docs-agent:release-notes-generator`，不在 GitHub Release 中覆盖站内事实。

## With Skill Behavior

- 以 confirmed site page 为唯一版本事实源，GitHub evidence 仅用于 compare 与代表性维护链接增强。
- 在 pre-tag 状态使用 `v0.9.0...8b6a1f2` 作为当前已审计 compare，同时把 `v0.9.0...v1.0.0` 标为实际 tag 存在后的 final compare。
- 对 fixture 未提供的 current latest 使用 `--latest=false` 安全回退，只生成 preview，未扩张为写入。

## Without Skill Baseline

- 2026-07-21 使用同一 prompt、assertions、expected output、metadata 与 fixture 全新生成；未读取 skill、Agent README、with-skill 证据或历史 comparison。
- baseline 同样 4/4 assertions PASS，完整保留事实、精选链接并声明冲突回流。
- 主要差异：baseline 直接使用 intended final compare `v0.9.0...v1.0.0`；with-skill 按当前 pre-tag 证据区分 audited compare 与 future final compare，阶段语义更严格。当前 assertions 的区分度为 0/4。

## Failures

- 无 assertion failure 或 blocker。
- 非阻塞 finding：assertions 与 fixture 已直接给出事实清单、精选链接和冲突处理要求，fresh baseline 同样全部通过，未证明 skill 相对 baseline 的断言增益。

## Next Steps

- 当事实源优先级、pre-tag/final compare 规则或 traceability outline 变化时重新执行 paired validation。
- 若要提升区分度，可让 baseline 从较少提示的维护 feed 自行判断事实边界与冲突回流。

## Runtime Artifacts Policy

- 本轮 candidate、worker observations 与 manifest 仅位于 `tmp/eval-runs/issue-146/`，作为短期运行期证据。
- 不提交 transcript、candidate、worker observations、manifest、verdict、outputs、timing 或 diagnostics；长期结果仅保留本 `comparison.md`。
