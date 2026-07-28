# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-003-github-release-boundary`
- Scenario: 缺少 Release Notes writing foundation 的混合站内/外部发布请求
- Review context: PR #187 review fix

## Test Set / Fixture Version

- Fixture version: `PR #187 foundation contradiction fix round-3`
- Validation time: `2026-07-28 23:56:24 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-release-evals/round-3/`
- 修正原因：round-2 fixture 仍包含固化六类证据标题的 `release-notes.test.mjs`，并保留 Release Notes index、release metadata 和相邻版本页，已构成等价站点契约，与“缺少写作基础”的场景矛盾。
- 本轮移除上述可执行契约与 Release Notes surfaces；两侧使用同一 prompt 与独立 pristine fixture，without-skill 未读取目标 skill、Docs Agent README、assertions、with-skill 输出、旧 comparison 或历史 round。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（4/4 assertions exercised）
- Overall result: PASS
- With-skill: **4/4 PASS**
- Fresh without-skill: **0/4 PASS、4/4 FAIL**
- Relative uplift: **+4 assertions**，通过率从 0% 提升到 100%，区分度强。

## Fixture Correction And Discrimination

- 修正后宿主保留正式文档站的其他必要文件，但不存在 `docs/site/release-notes/`、编写规则、index、release metadata、相邻版本页或等价可执行契约。
- 通用脚手架仅拒绝生成 Release Notes 并指向专用 skill，不提供正文、frontmatter、metadata 或 index 写作规则，因此不构成等价 foundation。
- with-skill 应用 foundation gate 后停止；baseline 自行推断规则并创建 Release Notes surfaces，重新形成明确区分。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | FAIL | with-skill 识别空目录及 writing rules/等价契约缺失；baseline 未识别阻塞并继续生成。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | FAIL | with-skill 的 `docs/site/` 文件 manifest 与源 fixture 完全一致；baseline 新增版本页、index、metadata 与生成物。 |
| `hands_missing_foundation_to_bootstrap` | PASS | FAIL | with-skill blocked 给 `docs-site-bootstrap` 并等待显式初始化授权；baseline 无 bootstrap handoff。 |
| `preserves_release_chain_and_external_zero_writes` | PASS | FAIL | with-skill 保留 bootstrap→Release Notes→checks→pre-tag audit→PM 顺序且不准备外部发布；baseline 跳过 bootstrap 并把自行建立的站内 handoff 宣称为 ready。 |

## With-Skill Behavior

- 在 site-foundation gate 停止，没有加载内部生成流程。
- 未创建版本页、index、release metadata、导航或 `.generated`；未运行不能证明交付成立的 docs checks。
- 未准备或写入 GitHub Release，未创建或移动 tag；返回携带 host、目标版本、证据边界与缺失 foundation 的 blocked bootstrap handoff。
- Response SHA-256: `4d37976c97607cc0eaa2968cbac560043016929d4423fc448360fc0ac1906e75`。

## Fresh Without-Skill Baseline

- baseline 自行创建 `v1.0.0.md`、Release Notes index、`.meta/releases.json` 和 ready handoff，并运行 `test:docs`。
- 它未识别 bootstrap gate，也未保留正文重新确认、站内检查与 pre-tag audit 的完整前置链。
- Response SHA-256: `3a2988ddb39320a02cd964a7fc4132270991ab6a4bc3c12441c49bda432a8243`。

## Failures And Iterations

- Round 1：with-skill 4/4、baseline 4/4；prompt/fixture 泄漏导致无区分度。
- Round 2：with-skill 4/4、baseline 0/4，但 fixture 保留等价 Release Notes 契约，场景判定失真。
- Round 3：修剪等价契约后 with-skill 4/4、baseline 0/4；Behavior PASS、Coverage FULL，场景与协议一致。
- 基础设施失败：none。baseline 依赖安装成功，`test:docs` 74 项测试通过；依赖审计告警不影响本次 eval 判定。

## Next Steps

- 保持缺少目录、写作规则和等价站点契约时的 bootstrap stop 为回归门禁。

## Runtime Artifact Policy

- runtime workspace、依赖、页面副本、构建产物、response、handoff 和 judge verdict 不提交。
- 本 `comparison.md` 是本轮唯一 durable eval 结果。
