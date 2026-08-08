# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-001-analyze-nodejs-project`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522` from `agents/engineer/test/codebase-analyzer/evals/workspace/eval-001-analyze-nodejs-project`.
- Fixture SHA-256: `70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522`
- Prompt SHA-256: `cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `de6d27a82a6affa1d54b83f57c4eb1889c4977944cd8849112c1a97798fbfd77`
- Skill overlay SHA-256: `0fb9a99c8b6a885ab74bb6a43bc122826a529476b9651a4d99df59ab056dab90`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dad930e2f7ff239d93a7a9675b382ce2b702f6090d6d7cc66b26e7ea598351d6`
- Metadata SHA-256: `5ca1d6325e7d73a97605eeb110ddc4062765b77075b5da8df9a904201e44cb60`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `technology_stack_identified` | PASS | with_skill 输出包含 language、framework、runtime、package_manager、module_system 等技术栈信息。 |
| `project_structure_mapped` | PASS | with_skill 输出在 architecture 下明确识别 source_dirs 为 src、test_dirs 为 test。 |
| `coding_conventions_identified` | PASS | with_skill 输出包含 ESLint 及规则、Prettier 版本和格式约定。 |
| `structured_profile_output` | PASS | with_skill 使用 YAML 代码块输出 Project Profile。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=4f85a1c9395be709e33102d190c068f723ab9532f5c92ede96503c294b8d2b4b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 直接输出结构化 YAML 项目概况，覆盖全部要求字段，并补充关键文件和验证状态。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=ffbb570e3442ac61395dfb73bc079b46d95c7a47a20743993584860ce21230e6; snapshot_sha256=1ea5df8385dd8ca78e51f97c4bc8a1df2948e9f094d9c63b67484e5902e79e79
- Behavior: 生成了较完整的 PROJECT_PROFILE.yaml 文件，内容覆盖技术栈、目录、规范等，但候选回复本身主要是交付摘要而非直接 YAML。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-001-analyze-nodejs-project`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522` from `agents/engineer/test/codebase-analyzer/evals/workspace/eval-001-analyze-nodejs-project`.
- Fixture SHA-256: `70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522`
- Prompt SHA-256: `cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4ef5dda23bd378b639722b86e7dbea1f7e09912544ca0c5fef4a87033ad825db`
- Skill overlay SHA-256: `d7b973d9b32cc5f2454374d2a337486c02a7f09a3b2d983c8c66b6ce00c56177`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dad930e2f7ff239d93a7a9675b382ce2b702f6090d6d7cc66b26e7ea598351d6`
- Metadata SHA-256: `5ca1d6325e7d73a97605eeb110ddc4062765b77075b5da8df9a904201e44cb60`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `technology_stack_identified` | PASS | with_skill 输出的 YAML 包含 language、framework、runtime、package_manager、module_system 等技术栈信息。 |
| `project_structure_mapped` | PASS | with_skill 输出包含 architecture.source_dirs: ["src/"] 和 architecture.test_dirs: ["test/"]，与 fixture 目录一致。 |
| `coding_conventions_identified` | PASS | with_skill 输出的 conventions 明确包含 linter（ESLint 9.31.0）和 formatter（Prettier 3.6.2）及其规则。 |
| `structured_profile_output` | PASS | with_skill 使用 project_profile YAML 代码块输出项目概况。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=95f610e5df441b43e19b0b7ea89843da546aa25b6ce8a4e6857c8e8d1f199dda; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了结构化 YAML Project Profile，覆盖技术栈、源代码与测试目录、编码规范及格式化和 lint 配置。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=8f96f9cf602e3c35a215377fc19e7adf4337ea3ed1dae2f2e25394fc01e8ced5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了较完整的项目分析和 YAML 输出，但使用了不同的顶层结构，未按要求明确提供 source_dirs 和 test_dirs 字段。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-001-analyze-nodejs-project`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522` from `agents/engineer/test/codebase-analyzer/evals/workspace/eval-001-analyze-nodejs-project`.
- Fixture SHA-256: `70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522`
- Prompt SHA-256: `cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4f1332611648af165a59b99f871678f4c900534d4d5d1fcedda6f815a3b3d5ed`
- Skill overlay SHA-256: `de5de93c0f76ae4be6410327fbb42d3bdbd9dfa29aa0e5edc91c3ed04528aee5`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dad930e2f7ff239d93a7a9675b382ce2b702f6090d6d7cc66b26e7ea598351d6`
- Metadata SHA-256: `5ca1d6325e7d73a97605eeb110ddc4062765b77075b5da8df9a904201e44cb60`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `technology_stack_identified` | PASS | with_skill 输出包含 tech_stack.language、framework、package_manager 等字段，且内容与 package.json 一致。 |
| `project_structure_mapped` | PASS | with_skill 输出在 architecture 下明确列出 source_dirs: [src/] 和 test_dirs: [test/]。 |
| `coding_conventions_identified` | PASS | with_skill 输出包含 conventions.linter 及其 eslint.config.js 配置，并包含 conventions.formatter 及其 .prettierrc.json 配置。 |
| `structured_profile_output` | PASS | with_skill 输出以 YAML 代码块呈现，且包含 project_profile 根节点。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=06215a39578d8c60487515434e474520257c06d6a76e1474132c250f166c8cfb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 输出 YAML Project Profile，明确覆盖技术栈、source_dirs、test_dirs、linter、formatter 及其配置，且与 fixture 原始证据一致。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=3c49dadcb6138d196e41af517e00f6342919a7d06e3fa2c4ecb686d920558064; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了较完整的 YAML 项目概况，包含技术栈、结构、规范和依赖；但目录字段使用 src/test 而非明确的 source_dirs/test_dirs。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

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
