# Eval Result: eval-004-api-adr-owned-by-engineer

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`
- Test case: api-adr-owned-by-engineer
- Workspace: `workspace/eval-004-api-adr-owned-by-engineer`
- Evaluation date: 2026-07-26
- Latest result: PASS - 本轮 fresh Codex subagent 成对生成了 `with_skill` 与新的 `without_skill` baseline；两者均满足 5/5 assertions，`with_skill` 额外给出了当前 `trd-gen` entry gate、Engineer ownership 和 handoff 边界的协议依据。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture classification: (a) fixture 已经足够，只缺 fresh baseline，不需要补文件。
- Fixture evidence: `docs/pm/chat-interface/history-search/PRD.md` 为 `status: Approved` 的嵌套 PRD，已提供 `feature_path: chat-interface/history-search`、`parent_feature: chat-interface`、`feature_level: 2`、API 上下文和搜索索引选型的决策上下文；`README.md` 明确本场景要求 Engineer 文档集且不进入实现。
- Expected output: `trd-gen` owns TRD, API, and ADR docs under `docs/engineer/chat-interface/history-search/` and does not enter implementation.

## With Skill

- Fresh run source: 当前会话中新启动的 Codex subagent 读取 `agents/engineer/README.md`、`agents/engineer/skills/trd-gen/SKILL.md`、eval item 和 fixture 后重新生成；未复用历史输出。
- Entry gate: 已批准 PRD 提供稳定 PM scope 与明确 `feature_path`，因此允许进入 `engineer-agent:trd-gen`，无需退回 PM。
- Ownership: 明确由 `engineer-agent:trd-gen` 负责 TRD、API 文档和搜索索引选型 ADR，不调用 PM 内部 `api-gen` / `adr-gen`。
- Paths: 目标为 `docs/engineer/chat-interface/history-search/TRD.md`、`docs/engineer/chat-interface/history-search/API.md` 和 `docs/engineer/chat-interface/history-search/ADR-*.md`。
- Metadata: 保留 `feature_path: chat-interface/history-search`、`parent_feature: chat-interface`、`feature_level: 2`，并设置 `related_prd: docs/pm/chat-interface/history-search/PRD.md`。
- Boundary: 仅生成 Engineer 文档集并等待确认；不创建 `IMPLEMENTATION_PLAN.md`，不修改代码、补测试或进入交付。

## Without Skill / Baseline

- Fresh baseline source: 同一 fresh Codex subagent 在隔离条件下重新生成，仅使用相同 prompt、fixture PRD / README、expected output 和 assertions，不读取或应用 `trd-gen` skill / Engineer README，也未复用历史 baseline。
- Baseline 根据 prompt 中已确认的 PRD 路径、明确的 Engineer 阶段和“不写实现计划或代码”约束，正确列出了三个 `docs/engineer/chat-interface/history-search/` 目标路径。
- Baseline 从 PRD frontmatter 正确保留 `feature_path`、`parent_feature`、`feature_level` 和 `related_prd`。
- Assertions 本身明确给出 `engineer-agent:trd-gen` ownership 及不得使用 PM 内部生成器，因此 baseline 也明确保留 Engineer ownership、不调用 `api-gen` / `adr-gen`，并停在 Engineer 文档阶段。
- 该 baseline 满足 5/5 assertions；它证明 fixture 与 eval 定义本身已足以约束正确结果，但不提供当前 skill entry gate 和 handoff 协议的独立依据。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judge conclusion |
| --- | --- | --- | --- |
| `engineer_owns_api_and_adr` | PASS | PASS | 两者均明确 API / ADR 属于 `engineer-agent:trd-gen`；with-skill 由当前 ownership 协议支撑，baseline 由 assertions 直接约束。 |
| `writes_all_engineer_docs_under_feature_path` | PASS | PASS | 两者均使用三个要求的 `docs/engineer/chat-interface/history-search/` 路径。 |
| `preserves_related_prd_and_metadata` | PASS | PASS | 两者均保留三项路径 metadata，并让 `related_prd` 指向已批准 PRD。 |
| `does_not_use_pm_generators` | PASS | PASS | 两者均未路由至 PM `api-gen` / `adr-gen`。 |
| `no_plan_or_code` | PASS | PASS | 两者均停在 Engineer 文档阶段，没有进入计划、代码、测试或交付。 |

## Failures

- 本轮 fresh pair 无 assertion failure。
- 历史 PARTIAL 的唯一证据缺口（没有 actual `without_skill` baseline）已补齐。

## Risks

- Prompt、expected output 和 assertions 已直接给出大部分目标路径与 ownership 约束，因此 baseline 同样可达 5/5；本 eval 主要验证 skill 没有偏离当前 Engineer 文档 ownership 和边界，不能单独证明相对于无 skill 的增益。
- Fixture 是最小文档规划场景，不验证实际生成的 TRD / API / ADR 内容质量；这不影响本 eval 当前 assertions。

## Next Steps

- Keep this eval as Engineer coverage for API / ADR ownership and feature path mirroring.

## Runtime Artifacts Policy

- 本轮仅把 fresh judge 的持久结论汇总到此 canonical `comparison.md`。
- Runtime transcripts、candidate outputs、verdicts、timing、diagnostics 和其他运行期 outputs 不提交到 git。
