# Eval Result: eval-001-analyze-nodejs-project

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-001-analyze-nodejs-project`
- Test case: analyze-nodejs-project
- Workspace: `workspace/eval-001-analyze-nodejs-project`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: engineer-agent 已确认需要 repo-level Project Profile，入口依据见 workspace `ENGINEERING_CONTEXT.md`。分析这个 Node.js 项目的代码库结构、技术栈和编码规范
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `assertion_1`: with_skill final.md 的 YAML 明确包含 language: JavaScript、framework: Express 5.1.0、package_manager: npm 11.4.2；transcript 显示实际读取 package.json、源码和配置。
- PASS `assertion_2`: with_skill final.md 的 architecture 明确包含 source_dirs: [src] 和 test_dirs: [test]；transcript 的目录扫描及实际 workspace 文件确认存在 src/ 与 test/。
- PASS `assertion_3`: with_skill final.md 的 conventions 明确包含 ESLint 规则及 Prettier 配置；transcript 实际读取 eslint.config.js、.prettierrc.json，并尝试执行 lint/format。
- PASS `yaml`: with_skill final.md 使用 YAML 代码块并以 project_profile 为根结构，符合 expected_output 的 YAML Project Profile 要求。

## With Skill Behavior

with_skill 成功完成 repo-level 分析，exit_code 为 0；读取了工程上下文、项目清单、源码、测试、配置及额外 skill 文件，未修改 workspace。输出覆盖技术栈、目录、规范、依赖和架构。

## Without Skill Baseline

without_skill 使用同一基础 fixture，读取了工程上下文、项目清单、源码、测试和配置，exit_code 为 0，输出同样为 YAML Project Profile；其 input/output hashes 一致。

## Failures / Findings

- None.
- Root cause: with_skill 相比 baseline 读取并利用了额外的 codebase-analyzer 规则文件，生成了更丰富的角色化 Project Profile，但两者均满足全部 assertions。

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-001-analyze-nodejs-project

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-001-analyze-nodejs-project`
- Test case: analyze-nodejs-project
- Workspace: `workspace/eval-001-analyze-nodejs-project`
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

- Historical result: PASS

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
