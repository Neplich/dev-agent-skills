# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator` → `release-notes-gen`（改名后新入口待重跑验证）
- Eval: `eval-003-github-release-boundary`
- Scenario: 缺少 Release Notes writing foundation 的混合站内/外部发布请求
- Review context: self-review convergence

## Test Set / Fixture Version

- Fixture version: `foundation cleanup consistency round-4`
- Validation time: `2026-07-29 01:07:33 CST`
- Runtime: `tmp/eval-runs/issue-177/self-review/`
- 修正原因：round-3 已移除等价 Release Notes 契约与 surfaces，但 `execution_cleanup` 没有覆盖被删除的 Release Notes 目录、release metadata 和可执行测试；复用 scratch 时可能被旧产物重新污染。
- 本轮补齐 cleanup 后，两侧使用同一 prompt 与独立 pristine fixture；without-skill 未读取目标 skill、Docs Agent README、eval metadata、assertions、with-skill 输出、旧 comparison 或历史 round，独立 judge 也未读取旧 comparison。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（4/4 assertions exercised）
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

- With-skill: **4/4 PASS**
- Fresh without-skill: **0/4 PASS、4/4 FAIL**
- Relative uplift: **+4 assertions**，通过率从 0% 提升到 100%，区分度强。

## Fixture Correction And Discrimination

- 修正后宿主保留正式文档站的其他必要文件，但不存在 `docs/site/release-notes/`、编写规则、index、release metadata、相邻版本页或等价可执行契约。
- 通用脚手架仅拒绝生成 Release Notes 并指向专用 skill，不提供正文、frontmatter、metadata 或 index 写作规则，因此不构成等价 foundation。
- `execution_cleanup` 现在覆盖整个 `docs/site/release-notes`、`docs/site/.meta/releases.json` 与 `docs/site/scripts/__tests__/release-notes.test.mjs`，防止旧 runtime 产物伪造 foundation。
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
- Response SHA-256: `2e12af318ce600cda34001d30ac9de7c8a91a65239bd2f693417eff1d8391eec`。

## Fresh Without-Skill Baseline

- baseline 自行创建 `v1.0.0.md` 与 Release Notes index，运行 frontmatter 检查和 public/internal builds，并把站内 pre-tag handoff 描述为已完成；它没有修改 `.meta/releases.json`。
- 它未识别 bootstrap gate，也未保留正文重新确认、站内检查与 pre-tag audit 的完整前置链。
- Response SHA-256: `a9ed33574b0b964611a2bb8e88723c0ea1620f79261b4a2f05a80aa67850c0df`。

## Failures And Iterations

- Round 1：with-skill 4/4、baseline 4/4；prompt/fixture 泄漏导致无区分度。
- Round 2：with-skill 4/4、baseline 0/4，但 fixture 保留等价 Release Notes 契约，场景判定失真。
- Round 3：修剪等价契约后 with-skill 4/4、baseline 0/4；Behavior PASS、Coverage FULL，场景与协议一致。
- Round 4：补齐删除 surface 的 cleanup 后重新 fresh 成对验证；with-skill 4/4、baseline 0/4，Behavior PASS、Coverage FULL，独立 judge 确认区分度保持。
- 基础设施失败：none。runtime 未保留 lane transcript、显式读取清单或结构化命令日志，降低读取边界的可审计性，但 workspace diff、响应和 baseline 构建产物足以覆盖本轮 4 条行为 assertion。

## Next Steps

- 保持缺少目录、写作规则和等价站点契约时的 bootstrap stop 为回归门禁。

## Runtime Artifact Policy

- `tmp/eval-runs/issue-177/self-review/` 下的 workspace、依赖、页面副本、构建产物、response、handoff 和 judge verdict 不提交。
- 本 `comparison.md` 是本轮唯一 durable eval 结果。
