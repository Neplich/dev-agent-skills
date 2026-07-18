# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-001-route-formal-docs-sync`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- 评估提交：`c9a0093`
- Harness：B4 完整 router harness

## Latest Result

**PASS** — fresh with-skill validation 接受了完整 PM handoff，保留了
所有 packet 字段，正确路由到 `formal-docs-sync`，并仅通过权威路径
引用 specialist gate 与共享 consumption contract。

## With-Skill Behavior

- 来源：本轮 fresh Codex sub-agent 使用隔离 fixture 与完整
  `_skill/agents/docs/` 目录；该目录包含 Docs Agent README、router、3 个
  specialist skill 及其 `_internal/**`。Harness 还按仓库相对路径提供了
  PM 共享 `consumption-contract.md` 与 `skill-map.md`。
- `routes_formal_docs_sync`：PASS。识别已完成 feature delivery 后的正式文档
  同步，选择 `formal-docs-sync`，并排除 bootstrap 与 release audit。
- `accepts_complete_handoff`：PASS。保留 `request_type`、`change_tier`、
  所有 feature scope 字段、`feature_path_evidence`、`source_documents`、
  `scope_decision`、`downstream_owner`、`required_output` 与 `blockers_risks`。
- `references_specialist_gate_only`：PASS。仅指向
  `agents/docs/skills/formal-docs-sync/SKILL.md` 及其内部指令，未复制证据
  顺序、同步步骤或 change-map 写入规则。
- `recognizes_shared_consumption_contract`：PASS。指向
  `agents/product_manager/skills/idea-to-spec/_internal/_shared/consumption-contract.md`
  作为 specialist trust model 权威来源，未复制契约正文。

## Without-Skill Baseline

- 来源：同一 fresh Codex sub-agent 在不含任何 skill 或 Agent README 的隔离
  workspace 中，仅使用原 prompt 与 fixture 重新生成 baseline；未复用历史
  baseline。
- baseline 也选择了 `formal-docs-sync` 并保留 handoff 上下文，但对来源
  文档状态做了更多概括。显式 expected output 与 assertions 使通用 baseline
  也较容易命中要求；这不改变 with-skill PASS 判定。

## Previous Partial Result

- 上一轮为 `PARTIAL`，原因是 with-skill runner 仅提供了 docs-agent router
  文档，缺少验证权威 gate 与 consumption-contract 指针所需的 specialist
  skill 文档与 PM 共享契约文件。
- B4 已按 eval runner contract 修正该执行环境问题，无需修改 router
  `SKILL.md`。

## Failures

- 无。

## Next Steps

- 后续 docs-agent routing eval 继续使用完整 router harness，使 specialist 与共享
  contract 指针可直接验证。

## Runtime Artifact Policy

- 运行期产物仅保留在 `tmp/eval-runs/`，不提交到 git。
