# Eval Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-generator`
- Eval: `eval-005-outline-sections-quality-exclusion`
- Latest result: **PASS**

验证 GitHub Release 完整预览是否严格采用 `release-outline.md` 规定的四节正文结构，排除内部质量证据，并完整保持站内 Release Notes 已确认的功能、架构、数据库、部署、资产、升级、兼容性与风险事实。

## Review Context

- Review scope: PR #147 第三轮 review，对应 issue #146。
- Final judge: 当前会话中的 fresh Codex validation agent；独立读取当前 skill、两份 reference、eval-005 定义、tracked fixture，以及第三轮隔离运行的 with-skill / without-skill 结果。
- 首次裁决的 `PARTIAL` 暴露了风险限定不够明确的问题；完成最小 reference 修复后，本轮使用新生成的两侧材料重新裁决。
- `attempt1` 仅属于未提交的诊断证据，不作为本轮断言裁决来源。本轮未读取旧运行结果。

## Test Set / Fixture Version

- Eval definition: `agents/product_manager/test/github-release-generator/evals/evals.json` 中 `eval-005-outline-sections-quality-exclusion`
- Durable workspace: `agents/product_manager/test/github-release-generator/evals/workspace/eval-005-outline-sections-quality-exclusion/`
- Runtime evidence: `tmp/eval-runs/issue-146-r3/{with_skill,without_skill}/eval-005-outline-sections-quality-exclusion/`
- Prompt: 根据 `release-package.md`、`docs/site/release-notes/v1.0.0.md` 和 `github-evidence.md` 生成 GitHub Release 完整预览，保持站内事实含义与范围且不执行写操作。
- Fixture inputs: `eval_metadata.json`、`release-package.md`、`github-evidence.md`、`docs/site/release-notes/v1.0.0.md`
- Boundary verification: with-skill 与 without-skill 两侧的四个 fixture 文件均与 tracked fixture 逐文件一致；两侧使用同一 eval prompt。without-skill worker 明确未读取或应用 skill、reference、Agent README、with-skill 结果或旧运行产物。

## Assertions

| Assertion | Result | Evidence |
| --- | --- | --- |
| `follows_outline_sections` | **PASS** | with-skill 的 GitHub Release 正文仅包含 `重点更新`、`其他改进`、`升级说明`、`变更明细` 四个二级小节；没有采用相邻材料建议的 `发布亮点`、`质量验证`、`维护者说明` 或其他约定外小节。 |
| `excludes_internal_quality_evidence` | **PASS** | 正文未包含 skill eval 结果、assertion 计数、review 轮次、QA 证据汇总，也未原样堆入额外 18 个维护 commit。引用的 PR #116、PR #117 和 commit `8b6a1f2` 仅用于支撑已确认事实。 |
| `preserves_confirmed_facts` | **PASS** | 预览分别保留文件卡片与失败消息原位重试；保留 `workflow_finished` 到统一附件模型、Web/Gateway 共享字段契约和旧文本消息兼容；保留 nullable JSONB `message_files`、先加列后回填、不改为 `NOT NULL`、删列会丢失附件元数据及备份要求；保留数据库迁移到 Gateway 再到 Web 的部署顺序、生产默认关闭开关、Web/Gateway 双架构镜像、静态 manifest file-card chunk、升级验证步骤及旧浏览器限制。 |

## With Skill Behavior

with-skill 结果完整生成标题、正文、事实来源、交接与审计状态、版本窗口、compare 链接、SemVer 与 latest/prerelease 保守判定，以及 preview-only 边界。正文严格遵循四节 outline，并把内部质量材料和不支撑新用户事实的 maintenance feed 排除在用户可见 Release 叙述之外。

风险限定得到明确保持：删除 `message_files` 列会丢失附件元数据，执行前必须备份，且不得将该回滚描述为无损或天然安全。未发现新增、遗漏或改写已确认事实；未执行 draft、publish、tag 或 docs 写操作。

## Without Skill Baseline

### 来源

baseline 由第三轮 fresh without-skill worker 基于同一 eval prompt、eval-005 定义和相同 fixture 独立生成。worker 未读取或应用 `github-release-generator/SKILL.md`、两份 reference、Agent README、with-skill 输出、现有 comparison、attempt1 或旧运行产物。

### 行为摘要

without-skill baseline 同样只使用四个约定正文小节，排除了内部质量证据，并保留了断言要求的全部已确认事实，因此三项断言也均可判定为 PASS。其正文内容正确，但相比 with-skill 缺少完整的 #116 / #117 gate 展示、current latest 缺失时的保守 flag 判定、预标签 compare 与最终 compare 的状态区分，以及后续 draft / publish 写入边界说明。

本 eval 的结论是 skill 结果满足全部可用性断言；baseline 同样通过说明 fixture 与断言本身已提供较强约束，不构成 with-skill 失败。

## Failures

无。本轮未发现断言失败、材料边界污染、事实遗漏、风险限定弱化或越权写操作。

## Next Steps

- 接受本轮 `PASS` 作为 PR #147 第三轮 eval-005 的 fresh validation 结论。
- 保留当前最小 reference 修复与该 fixture，后续修改 release outline、内部质量证据排除规则或风险事实转换规则时重新运行此 eval。

## Runtime Artifacts Policy

- 本轮运行期证据位于 `tmp/eval-runs/issue-146-r3/{with_skill,without_skill}/eval-005-outline-sections-quality-exclusion/`，包括 `candidate-output.md` 与 `worker-observations.md`。
- `with_skill/`、`without_skill/`、transcript、worker observations、diagnostics 和 attempt1 均为未提交运行期或诊断产物，不进入 durable fixture。
- 长期提交结果仅为本 `comparison.md`；运行期目录不得作为仓库长期结果提交。
