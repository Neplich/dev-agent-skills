# Eval Result: eval-002-abandoned

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-002-abandoned`
- Test case: Abandoned Packages
- Workspace: `workspace/eval-002-abandoned`
- Review context: issue #143 thin fixture 补全后的复验
- Latest result: PASS（4/4 assertions）- fresh Codex subagent validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: issue #143 当前提交；包含 `PM_HANDOFF.md`、已确认的 `docs/pm/dependency-inventory/PRD.md` 与 `package.json`
- Fresh run: 当前会话中的 fresh Codex validator 在 `tmp/eval-runs/issue-143/batch-b/eval-002-abandoned/` 建立隔离副本，先运行 with_skill，再基于同一 prompt/fixture 全新生成 without_skill baseline；baseline 未读取或应用 skill 文档、Agent README、历史 comparison，也未复用历史结果
- Registry/audit evidence: 本轮分别在隔离副本查询 npm deprecation metadata；with_skill 另在 scratch 中生成临时 lockfile 并执行 `npm audit --json`
- Source head: `test/issue-143-security-thin-fixtures`
- Validation date: 2026-07-21

## Assertions

- PASS `dependency_inventory`：识别 Node.js 生态及两个直接生产依赖 `request@2.88.2`、`node-uuid@1.4.8`，并区分网络请求与 UUID 暴露面
- PASS `risk_classification`：依据 npm deprecation metadata 将两者判为废弃依赖；将 request 的维护缺失及 audit 风险与 node-uuid 的迁移风险分级，未把普通过期等同已知漏洞
- PASS `evidence`：引用 `package.json` 精确版本、两条 registry 弃用声明；with_skill 还记录临时 lockfile 的 audit 结果及无自动修复结论
- PASS `upgrade_plan`：给出 request 向 fetch/Undici 等维护中客户端迁移、node-uuid 向 `uuid` 或 `crypto.randomUUID()` 迁移的优先级、兼容检查和回归验证

## With Skill Behavior

with_skill 通过 PM handoff gate 后，先完成依赖清单，再查询维护状态并按 specialist 协议运行可用的 npm audit。输出区分了“弃用”“已知漏洞”“普通版本落后”，将 `request` 定为优先替换并说明其 vulnerable transitives 与使用方式相关的可利用性边界；同时没有把 `node-uuid` 在未见调用代码时夸大为确定的 critical 漏洞。迁移步骤、兼容项和验证命令完整，4 条 assertion 全部满足。

## Without Skill Baseline

without_skill baseline 由本轮 fresh Codex validator 在独立副本中重新生成，仅使用同一 prompt、fixture 与独立 npm deprecation 查询。baseline 识别两个弃用包、说明 request 的外部网络风险与 node-uuid 的维护风险，并给出替换方向和测试要点，4 条 assertion 全部满足；baseline 未运行 audit，因此没有 with_skill 的 transitive vulnerability 数量与无自动修复证据。

## Failures

- 无 assertion failure。
- fixture 未提供依赖调用点，具体可利用性和迁移 API 差异仍需 Engineer 在实现阶段核实；该证据边界不影响废弃/过期审计 assertion。

## Next Steps

- 保持当前 registry 查询和 scratch audit 仅作为运行期证据；若未来 assertion 要求可利用性结论，应补最小调用代码 fixture 后再重跑。

## Runtime Artifacts Policy

- 临时 lockfile、candidate、baseline、registry/audit 输出仅位于 `tmp/eval-runs/issue-143/batch-b/`，验证后删除，不提交到 git。
- Runtime transcripts、verdicts、timing、diagnostics、with_skill / without_skill 输出及其他 scratch 产物均不得提交；长期结果仅保留本 `comparison.md`。
