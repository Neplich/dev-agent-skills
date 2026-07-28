# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-009-release-product-ops`
- Scenario: release 模式下未确认的 Product 原子 mapping closure 与冲突 Ops 证据
- Review context: PR #187 review follow-up

## Test Set / Fixture Version

- Fixture version: `issue-177 release evidence consistency fix round-3`
- Validation time: `2026-07-29 00:54:06 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-release-evals/round-3-eval-009/`
- 修正原因：旧 fixture 把 release coordination 的 `v1.5.0` 候选期望误述成 `deploy/dashboard.env` 的 checked-in 状态，而实际配置为 `v1.4.0`。本轮把该 bullet 改为候选配置描述，保留“候选 `v1.5.0` 尚未与 checked-in `v1.4.0` 配置及 runtime 验证调和”的冲突语义。
- with-skill 与 fresh baseline 使用同一修正后 fixture 和 prompt；with-skill 读取目标 skill、Docs README 及 Product/Ops 模块，fresh baseline 不读取或应用这些材料、assertions、旧 comparison、历史 baseline 或 with-skill 输出。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（5/5 assertions exercised）
- Overall result: PASS
- With-skill: **5/5 PASS**
- Fresh without-skill baseline: **5/5 PASS**
- Relative uplift: **0 assertions**，通过率同为 100%。
- Discrimination: **本轮无 assertion 级区分度**。

## Fixture Consistency Repair

- `release-evidence.md` 不再声称 checked-in `deploy/dashboard.env` 已 pin `v1.5.0`。
- release coordination 仍明确提出把 `AI_HUB_IMAGE` 提升到 `v1.5.0` 的候选期望。
- checked-in `deploy/dashboard.env` 保持 `AI_HUB_IMAGE=registry.example/ai-hub:v1.4.0`，且测试证据仍没有 runtime 配置检查。
- 因此 Ops blocker 现在来自清晰的“候选期望 vs checked-in 配置 vs 缺失 runtime 验证”三方未调和事实，不再依赖自相矛盾的摘要表述。

## Assertion Results

| Assertion | With skill | Fresh baseline | Fresh judgment |
| --- | --- | --- | --- |
| `detects_unconfirmed_product_mapping_closure` | PASS | PASS | 两侧都识别 Product 叶子虽有实现/验收证据，但维护者未确认 ancestor index、直接导航和 expanded change-map closure，因此 Product 零写入。 |
| `keeps_conflicting_ops_candidate_unchanged` | PASS | PASS | 两侧都识别候选 `v1.5.0`、checked-in `v1.4.0` 和缺失 runtime 检查之间的冲突，并保持 Ops 页面及 mapping 不变。 |
| `preserves_release_notes_surfaces` | PASS | PASS | 两侧都保留独立 Release Notes owner，未修改正文、索引、metadata 或导航。 |
| `keeps_entire_site_zero_diff` | PASS | PASS | 两侧最终 `docs/site` 的 43 个文件逐项一致，没有正式页面、index、change map、Release Notes surface 或脚本差异。 |
| `separates_scope_and_technical_blockers` | PASS | PASS | 两侧都分别返回 Product scope confirmation 与 Ops runtime evidence blocker，并只描述解除 blocker 后的未来审计路径。baseline 的额外检查是零写入后的只读诊断，不构成写后成功检查或成功审计 handoff。 |

## With-Skill Behavior

- 在 Step 4 写前候选确认门禁停止，Product、Ops、ancestor index、change map 与 Release Notes surfaces 均保持 pristine。
- 明确要求逐 `code_glob` 的 leaf、ancestor、直接导航、authority link 和 `required_docs` 原子闭包。
- 分开报告 Product scope-confirmation gap 和 Ops evidence gap，没有运行写后宿主检查，也没有输出成功审计 handoff。
- Response SHA-256: `5925b23a6caad5e863b5d85710743e32c4cc99eaffd7b083b0176a7c2de648c0`。

## Fresh Without-Skill Baseline

- baseline 独立识别 Product ancestor/index closure 未确认，并把实际可写范围收缩为零。
- baseline 独立识别候选 `v1.5.0` 与 checked-in `v1.4.0` 冲突以及缺失 runtime 配置验证，保持 Ops 零写入。
- baseline 运行 frontmatter、站点单元测试和显式版本检查作为未变站点的只读诊断；它没有把这些检查用于验证写入或形成成功审计 handoff。
- Response SHA-256: `2229a3739b37ccfa9554281b70be551c111faf0e13e6c3b2fb9ac7ab0658cf69`。

## Failures And Iterations

- Round 1：with-skill 5/5、baseline 5/5；原始场景无区分度。
- Round 2：with-skill 5/5、baseline 1/5；但后续 review 发现 release evidence 把 checked-in `v1.4.0` 配置误述为 `v1.5.0`，fixture 自相矛盾。
- Round 3：修正证据表述后，with-skill 5/5、fresh baseline 5/5；行为正确性保持 PASS，但 assertion 级区分度降为 0。
- Round 3 首次 baseline 因初始路径枚举暴露了 with-skill 运行期文件名而作废；替换用的全新 baseline 从独立 workspace 起步，未读取或列举禁读路径，其结果才用于本 comparison。
- 基础设施失败：none。

## Next Steps

- 保持本 fixture 的证据一致性修复，避免验证者把候选 `v1.5.0` 误读为 checked-in 事实。
- 本轮无行为回归，但现有 assertions 无法区分 skill 与 fresh baseline；后续若要恢复区分度，应单独 redesign prompt/fixture/assertions，并重新执行完整 paired validation，不能恢复旧的矛盾表述。

## Runtime Artifact Policy

- responses、workspace 副本、依赖、日志和 judge verdict 仅位于 gitignored `tmp/eval-runs/issue-177/docs-release-evals/round-3-eval-009/`，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
