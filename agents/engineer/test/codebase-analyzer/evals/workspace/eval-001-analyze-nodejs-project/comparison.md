# Eval Result: eval-001-analyze-nodejs-project

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-001-analyze-nodejs-project`
- Test case: analyze-nodejs-project
- Workspace: `workspace/eval-001-analyze-nodejs-project`
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Overall result: PASS

## Review Context

- Date: 2026-08-03（issue #188 A 维删除后 paired 回归）
- 变更：Step 3 技术栈 marker 表、Step 4 lint 工具表、Step 6 架构模式表已删除（L3 A 维实测确认磨平）
- Judge: fresh Codex validation agent，双侧 candidate 冻结后独立判定（`tmp/eval-runs/issue-188-regress/judge/verdict-paired.md`）

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: ENGINEERING_CONTEXT.md、package.json、eslint.config.js、.prettierrc.json、src/、test/
- With-skill evidence: `tmp/eval-runs/issue-188-regress/with_skill/codebase-analyzer-eval-001/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-188-regress/without_skill/codebase-analyzer-eval-001/candidate-output.md`

## Assertions

- PASS `assertion_1`：tech_stack 明确给出 JavaScript、Express 5.1.0、Node.js 22.x、npm 11.4.2；without-skill 同 PASS（runtime/stack 字段语义等价）
- PASS `assertion_2`：识别 `src/` 为源码目录、`test/` 为测试目录；without-skill 同 PASS
- PASS `assertion_3`：识别 ESLint 9.31.0 与规则、Prettier 3.6.2 与格式配置；without-skill 同 PASS
- PASS `yaml`：Project Profile 主体置于有效 YAML fenced block；without-skill 同 PASS

## With Skill Behavior

- 删除三张速查表后仍产出完整 Project Profile：技术栈（package.json 核证）、规范（lint/formatter 配置文件）、结构（src/test）、架构分类（单模块 HTTP 服务）、feature_inventory 候选与 pm-agent:feature-catalog 确认边界。

## Without Skill Baseline

- 来源：2026-08-03 fresh baseline（同 prompt/fixture，未读 skill）；4/4 assertions PASS。
- 原断言双侧零区分（baseline 已内化技术栈/lint/结构识别）；skill 增量在入口门禁、证据边界、feature inventory 等非断言内容，删除后无行为回归。

## Failures / Findings

- 无 with-skill assertion failure；无 NOT EXERCISED；Coverage FULL。
- 零区分度观察：原 4 条断言被 baseline 全部白捡，与 #188 删除决策一致（已删内容正是 baseline 内化的部分）；剩余增量（门禁/证据边界/feature inventory）不在本 eval 断言范围。

## Historical Results

- 2026-07-26（删除前）：PASS（4/4 assertions，fresh Codex paired validation；without-skill 3/4，`yaml` 断言失分）。该轮基于删除前 skill 内容，仅作历史记录。

## Next Steps

- 删除后后续修改 codebase-analyzer 时重新运行本 eval 与其他 eval（eval-002 monorepo 场景、eval-003 mapped 场景）。
- 原断言已无区分度；后续评估可考虑把断言钉在 skill 特有增量（feature_inventory 证据分组规则、suggested_feature_path 推导）上。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-188-regress/`（ignored 运行期目录，未提交）。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
