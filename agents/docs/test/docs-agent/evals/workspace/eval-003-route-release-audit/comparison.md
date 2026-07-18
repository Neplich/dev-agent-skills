# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- 评估提交：`c9a0093`
- Harness：B4 完整 router harness

## Latest Result

**PASS** — fresh with-skill validation 接受了等效已确认 release chain，保留
release scope 与证据，正确路由到 `docs-audit`，并仅引用权威 specialist
gate 路径。

## With-Skill Behavior

- 来源：本轮 fresh Codex sub-agent 使用隔离 fixture 与完整
  `_skill/agents/docs/` 目录；该目录包含 Docs Agent README、router、3 个
  specialist skill 及其 `_internal/**`。Harness 还按仓库相对路径提供了
  PM 共享 `consumption-contract.md` 与 `skill-map.md`。
- `accepts_equivalent_chain`：PASS。将 `release-entry.md` 识别为等效已确认
  入口，保留 release scope、`v0.4.0` tag、已 review changelog、contract 与 CI
  证据、正式站点与审计请求。
- `routes_docs_audit`：PASS。选择 `docs-audit`，保留版本与 release 证据，
  并将审计执行交给 specialist。
- `references_audit_gate_only`：PASS。仅指向
  `agents/docs/skills/docs-audit/SKILL.md` 及其内部指令，并明确未复制
  base/target、确定性层、事实层、状态判定或版本盖章协议。

## Without-Skill Baseline

- 来源：同一 fresh Codex sub-agent 在不含任何 skill 或 Agent README 的隔离
  workspace 中，仅使用原 prompt 与 fixture 重新生成 baseline；未复用历史
  baseline。
- baseline 也选择了 `docs-audit` 并保留主要 release 证据。显式 expected
  output 与 assertions 使通用 baseline 也较容易命中要求；这不改变
  with-skill PASS 判定。

## Previous Partial Result

- 上一轮为 `PARTIAL`，原因是 with-skill runner 仅提供了 docs-agent router
  文档，缺少验证权威 `docs-audit` gate 指针所需的 specialist skill 文档。
- B4 已按 eval runner contract 修正该执行环境问题，无需修改 router
  `SKILL.md`。

## Failures

- 无。

## Next Steps

- 后续 docs-agent routing eval 继续使用完整 router harness，使 specialist gate
  可直接验证。

## Runtime Artifact Policy

- 运行期产物仅保留在 `tmp/eval-runs/`，不提交到 git。
