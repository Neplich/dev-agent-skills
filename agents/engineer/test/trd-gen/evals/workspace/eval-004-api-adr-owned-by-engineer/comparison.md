# Eval Result: eval-004-api-adr-owned-by-engineer

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`
- Test case: api-adr-owned-by-engineer
- Workspace: `workspace/eval-004-api-adr-owned-by-engineer`
- Evaluation date: 2026-07-26
- Latest result: PARTIAL - 本轮按 no-answer-key 顺序重新生成 fresh pair；`with_skill` 与新的 `without_skill` baseline 均满足 3/5 assertions。两者都遗漏了 assertion 要求的完整 ownership 明示与 `related_prd` 元数据，不能沿用旧 comparison 的 5/5 PASS。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture classification: (a) fixture 已经足够，只缺可信的 fresh baseline，不需要补文件。
- Fixture evidence: `docs/pm/chat-interface/history-search/PRD.md` 为 `status: Approved` 的嵌套 PRD，已提供 `feature_path: chat-interface/history-search`、`parent_feature: chat-interface`、`feature_level: 2`、API 上下文和搜索索引选型的决策上下文；`README.md` 明确要求 Engineer 文档集且不进入实现。
- 本轮没有修改 fixture、`eval_metadata.json`、skill 或 assertions。

## No-Answer-Key Fresh Pair Protocol

1. `with_skill` 生成前只读取 workspace `eval_metadata.json` 中的原 prompt、fixture `README.md`、Approved PRD，以及 `agents/engineer/README.md` 和 `agents/engineer/skills/trd-gen/SKILL.md`。
2. 在未读取 `evals.json`、expected output、assertions 或旧 `comparison.md` 的条件下生成并锁定 `with_skill` 候选。
3. 新启动 `fork_turns=none` 的 fresh Codex subagent；该隔离上下文只收到原 prompt、fixture `README.md` 和 Approved PRD，明确禁止读取或应用 Agent README、SKILL、`evals.json`、assertions、expected output 和旧 comparison，并独立生成、锁定 baseline。
4. 两份候选锁定后，judge 才首次读取 `evals.json` assertions 和旧 comparison，逐项判定。

旧 comparison 所称 baseline 使用 expected output 和 assertions 的做法不符合 fresh baseline 隔离要求，本轮结论不复用该 baseline 或其 5/5 判断。

## With Skill

- Fresh run source: 当前会话中新启动的 Codex subagent 按上述隔离顺序生成；未复用历史输出。
- Entry gate: 识别 Approved PRD 已提供稳定 PM scope 与明确 `feature_path`，进入 Engineer TRD 阶段。
- Paths: 列出 `docs/engineer/chat-interface/history-search/TRD.md`、`docs/engineer/chat-interface/history-search/API.md` 和 `docs/engineer/chat-interface/history-search/ADR-001-search-index-strategy.md`。
- Boundary: 明确本阶段只处理 TRD、API 和 ADR，不创建 `IMPLEMENTATION_PLAN.md`，不编写代码；Engineer 文档确认后才移交 `feature-implementor`。
- Missing evidence: 候选虽以 Engineer TRD 阶段和 Engineer 产物表述职责，但没有明确写出 API / ADR 由 `engineer-agent:trd-gen` 负责；也没有完整声明三个 Engineer 文档均保留 `feature_path`、`parent_feature`、`feature_level` 和 `related_prd`。

## Without Skill / Baseline

- Fresh baseline source: 独立的 `fork_turns=none` Codex subagent 只使用原 prompt、fixture `README.md` 和 Approved PRD；未读取或应用 Engineer Agent README、`trd-gen` SKILL、`evals.json`、expected output、assertions 或旧 comparison，未复用历史 baseline。
- Baseline 独立列出三个 `docs/engineer/chat-interface/history-search/` 目标路径，生成 TRD、API 和 Proposed ADR，并明确不进入实施计划或代码。
- Baseline 的三个文档 frontmatter 均保留 `feature_path`、`parent_feature` 和 `feature_level`，但未设置 `related_prd`。
- Baseline 没有把工作路由给 PM `api-gen` / `adr-gen`，但也没有明确声明 API / ADR 由 `engineer-agent:trd-gen` 负责。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judge conclusion |
| --- | --- | --- | --- |
| `engineer_owns_api_and_adr` | FAIL | FAIL | 两者都处于 Engineer 阶段，但都没有按 assertion 明确写出 API / ADR 由 `engineer-agent:trd-gen` 负责而非 PM 内部生成器。 |
| `writes_all_engineer_docs_under_feature_path` | PASS | PASS | 两者均给出 TRD、API 和 ADR 的 `docs/engineer/chat-interface/history-search/` 路径。 |
| `preserves_related_prd_and_metadata` | FAIL | FAIL | with-skill 未完整声明四项要求；baseline 保留三项路径 metadata，但缺少 `related_prd: docs/pm/chat-interface/history-search/PRD.md`。 |
| `does_not_use_pm_generators` | PASS | PASS | 两者均未调用或路由至 PM `api-gen` / `adr-gen`。 |
| `no_plan_or_code` | PASS | PASS | 两者都明确停在 Engineer 文档阶段，没有进入实现计划、代码、测试或交付。 |

## Failures

- `with_skill` 与 baseline 都没有明确写出 `engineer-agent:trd-gen` 对 API / ADR 的 ownership。
- `with_skill` 没有完整声明 Engineer 文档所需的路径 metadata 和 `related_prd`；baseline 虽写出三项路径 metadata，但遗漏 `related_prd`。
- 因此本轮可信 fresh pair 的结论是 3/5，而不是旧 comparison 的 5/5。

## Risks

- Fixture 足以支持本 eval，不需要为了提高结果而补造额外证据；当前 PARTIAL 来自候选输出不完整，而非 fixture 缺失。
- Prompt 和 fixture 已直接给出 Engineer 阶段、三个文档类型及嵌套 PRD 路径，因此 baseline 也能通过路径和边界 assertions；本 eval 对 skill 增益的区分度有限。
- 本轮只纠正 durable evidence，不修改 `trd-gen` 行为或放宽 assertions。

## Next Steps

- 保留本轮 PARTIAL 作为可信 no-answer-key 结果；如需恢复 PASS，应由后续新的、同样隔离的 fresh pair 验证候选明确满足 ownership 与完整 metadata / `related_prd`，不能只改写 comparison 结论。

## Runtime Artifacts Policy

- 本轮仅把 fresh judge 的持久结论汇总到此 canonical `comparison.md`。
- Runtime transcripts、candidate outputs、verdicts、timing、diagnostics 和其他运行期 outputs 不提交到 git。
