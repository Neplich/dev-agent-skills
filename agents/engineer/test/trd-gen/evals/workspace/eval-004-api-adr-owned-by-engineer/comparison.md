# Eval Result: eval-004-api-adr-owned-by-engineer

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`
- Test case: api-adr-owned-by-engineer
- Workspace: `workspace/eval-004-api-adr-owned-by-engineer`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: PM 已确认 docs/pm/chat-interface/history-search/PRD.md。请为聊天历史搜索补技术方案、API 文档和一份搜索索引选型 ADR。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `engineer_owns_api_and_adr`: workspace 中 API.md 与 ADR 确实写在 Engineer 路径；但 final.md 和 agent_message 未明确说明由 `engineer-agent:trd-gen` 负责、且不是 PM 内部生成器负责。
- PASS `writes_all_engineer_docs_under_feature_path`: file_change 记录及 workspace 均显示三份文件位于 `docs/engineer/chat-interface/history-search/`；final.md 也列出对应路径。
- PASS `preserves_related_prd_and_metadata`: TRD.md、API.md、ADR.md 的 frontmatter 均包含 `feature_path: chat-interface/history-search`、`parent_feature: chat-interface`、`feature_level: 2` 和 `related_prd: docs/pm/chat-interface/history-search/PRD.md`。
- PASS `does_not_use_pm_generators`: with_skill transcript 未记录调用 `api-gen` 或 `adr-gen`，file_change 仅新增 Engineer TRD/API/ADR 三份文档。
- PASS `no_plan_or_code`: with_skill workspace 未产生 IMPLEMENTATION_PLAN.md 或代码/测试文件；file_change 仅涉及三份 Engineer 文档，final.md 说明实现代码尚不存在。

## With Skill Behavior

三份 Engineer 文档已正确写入目标目录，frontmatter 和 hash 均与实际 workspace 内容一致；但最终输出未明确声明 API/ADR 的 `engineer-agent:trd-gen` 归属。exit_code 为 0。

## Without Skill Baseline

without_skill 生成了 PM 路径下的 TECHNICAL-SPEC.md、API.md 和 ADR，未满足 Engineer-owned 产物边界；仅作对照，不影响逐条判定。其记录的 hash 与 workspace 文件一致，exit_code 为 0。

## Failures / Findings

- engineer_owns_api_and_adr：缺少明确的 `engineer-agent:trd-gen` ownership 声明及对 PM 内部生成器的排除说明。
- Root cause: 实现产物和路径边界正确，但 final/transcript 的责任归属表述不完整，未提供该 assertion 要求的明确 ownership 证据。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-004-api-adr-owned-by-engineer

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`
- Test case: api-adr-owned-by-engineer
- Workspace: `workspace/eval-004-api-adr-owned-by-engineer`
- Evaluation date: 2026-07-26
- Latest result: PASS - 本轮由当前会话中同一个 fresh Codex subagent 按 no-answer-key 顺序重新生成并锁定 `with_skill` 与新的 `without_skill` baseline；fresh judge 判定 `with_skill` 满足 5/5 assertions，baseline 满足 3/5。skill 的增益体现在明确的 Engineer ownership、完整路径元数据与 `related_prd` 契约。
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture classification: (a) fixture 已经足够，只缺可信的 fresh baseline，不需要补文件。
- Fixture evidence: `docs/pm/chat-interface/history-search/PRD.md` 为 `status: Approved` 的嵌套 PRD，已提供 `feature_path: chat-interface/history-search`、`parent_feature: chat-interface`、`feature_level: 2`、API 上下文和搜索索引选型的决策上下文；`README.md` 明确要求 Engineer 文档集且不进入实现。
- 本轮没有修改 fixture、`eval_metadata.json`、skill 或 assertions。

## No-Answer-Key Fresh Pair Protocol

1. `with_skill` 生成前只读取 workspace `eval_metadata.json` 中的原 prompt、fixture `README.md`、Approved PRD，以及 `agents/engineer/README.md` 和 `agents/engineer/skills/trd-gen/SKILL.md`。
2. 在未读取 `evals.json`、expected output、assertions 或旧 `comparison.md` 的条件下生成并锁定 `with_skill` 候选。
3. 同一个 fresh Codex subagent 随后仅依据已经锁定的原 prompt、fixture `README.md` 和 Approved PRD 生成新的 `without_skill` baseline；此阶段明确不应用 Engineer Agent README 或 `trd-gen` SKILL，仍未读取 `evals.json`、expected output、assertions 或旧 comparison。
4. 两份候选锁定后，judge 才首次读取 `evals.json` assertions 和旧 comparison，逐项判定。

本轮不复用任何历史候选、baseline 或判断。

## With Skill

- Fresh run source: 当前会话中的 fresh Codex subagent 按上述隔离顺序生成并锁定；未复用历史输出。
- Entry gate: 识别 Approved PRD 已提供稳定 PM scope 与明确 `feature_path`，进入 Engineer TRD 阶段。
- Ownership: 明确 TRD、API 和 ADR 都是 `engineer-agent:trd-gen` 负责的 Engineer 产物，不路由到 PM 内部生成器。
- Paths: 列出 `docs/engineer/chat-interface/history-search/TRD.md`、`docs/engineer/chat-interface/history-search/API.md` 和 `docs/engineer/chat-interface/history-search/ADR-001-search-index-strategy.md`。
- Metadata: 要求三份 Engineer 文档一致保留 `feature_path: chat-interface/history-search`、`parent_feature: chat-interface`、`feature_level: 2`，并以 `related_prd: docs/pm/chat-interface/history-search/PRD.md` 追溯已批准 PRD。
- Boundary: 明确本阶段只处理 TRD、API 和 ADR，不创建 `IMPLEMENTATION_PLAN.md`，不编写代码；Engineer 文档确认后才移交 `feature-implementor`。

## Without Skill / Baseline

- Fresh baseline source: 同一个 fresh Codex subagent 在锁定 `with_skill` 后，只使用原 prompt、fixture `README.md` 和 Approved PRD；不应用 Engineer Agent README 或 `trd-gen` SKILL，且生成时仍未读取 `evals.json`、expected output、assertions 或旧 comparison。
- Baseline 独立推断出三个 `docs/engineer/chat-interface/history-search/` 目标路径，生成 TRD、API 和 Proposed ADR，并明确不进入实施计划或代码。
- Baseline 的三个文档 frontmatter 均保留 `feature_path`、`parent_feature` 和 `feature_level`，但未设置 `related_prd`。
- Baseline 没有把工作路由给 PM `api-gen` / `adr-gen`，但也没有明确声明 API / ADR 由 `engineer-agent:trd-gen` 负责。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judge conclusion |
| --- | --- | --- | --- |
| `engineer_owns_api_and_adr` | PASS | FAIL | with-skill 明确声明 API / ADR 由 `engineer-agent:trd-gen` 负责且不路由至 PM 内部生成器；baseline 仅按一般任务生成文档，没有给出该角色归属契约。 |
| `writes_all_engineer_docs_under_feature_path` | PASS | PASS | 两者均给出 TRD、API 和 ADR 的 `docs/engineer/chat-interface/history-search/` 路径。 |
| `preserves_related_prd_and_metadata` | PASS | FAIL | with-skill 完整声明三项路径 metadata 与 `related_prd`；baseline 保留三项路径 metadata，但缺少 `related_prd: docs/pm/chat-interface/history-search/PRD.md`。 |
| `does_not_use_pm_generators` | PASS | PASS | 两者均未调用或路由至 PM `api-gen` / `adr-gen`。 |
| `no_plan_or_code` | PASS | PASS | 两者都明确停在 Engineer 文档阶段，没有进入实现计划、代码、测试或交付。 |

## Failures

- baseline 没有明确写出 `engineer-agent:trd-gen` 对 API / ADR 的 ownership。
- baseline 虽写出三项路径 metadata，但遗漏 `related_prd`。
- with-skill 没有 assertion failure；本轮可信 fresh pair 的结论是 with-skill 5/5、baseline 3/5。

## Risks

- Fixture 足以支持本 eval，不需要补造额外证据。
- Prompt 和 fixture 已直接给出 Engineer 阶段、三个文档类型及嵌套 PRD 路径，因此 baseline 也能通过路径和边界 assertions；本 eval 对 skill 增益的区分度有限。
- 本轮 PASS 依赖 skill 对 ownership 和完整文档元数据的明确约束；后续若这些契约变化，应重新执行同样隔离的 fresh pair。
- 本轮只更新 durable evidence，不修改 `trd-gen` 行为或放宽 assertions。

## Next Steps

- 保留本轮 PASS 作为当前可信 no-answer-key 结果；任何后续重跑仍须先锁定成对候选，再读取 assertions 进行判断。

## Runtime Artifacts Policy

- 本轮仅把 fresh judge 的持久结论汇总到此 canonical `comparison.md`。
- Runtime transcripts、candidate outputs、verdicts、timing、diagnostics 和其他运行期 outputs 不提交到 git。
