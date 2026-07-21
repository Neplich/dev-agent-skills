# Eval Result: eval-001-npm-audit

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-001-npm-audit`
- Test case: NPM Dependency Audit
- Workspace: `workspace/eval-001-npm-audit`
- Review context: issue #143 thin fixture 补齐后的 Fresh Codex 复验
- Latest result: PASS（4/4 assertions）- fresh Codex paired validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: issue #143 当前 fixture；包含 `PM_HANDOFF.md`、`docs/pm/dependency-inventory/PRD.md` 与 `package.json`
- Fresh run: 当前会话中新启动的 fresh Codex validator 在 `tmp/eval-runs/issue-143/batch-a` 建立隔离副本；with_skill 读取当前 `dependency-risk-auditor` 与 Security Agent README，without_skill 对同 prompt/fixture 不读取或应用 skill/Agent README，并于本轮重新生成 baseline，未读取历史 comparison、未复用历史 baseline
- Audit evidence: 两侧隔离副本分别生成 scratch-only lockfile 并运行 `npm audit --json`；本轮均报告 2 个有风险的直接生产依赖（1 Critical、1 High）
- Source head: `test/issue-143-security-thin-fixtures` (`d70a8c4`)
- Validation date: 2026-07-21

## Assertions

- PASS `dependency_inventory`：识别 Node.js/npm 生态及直接生产依赖 `lodash@4.17.15`、`minimist@0.0.8`
- PASS `risk_classification`：将 minimist 原型污染判为 Critical、lodash 当前已知注入/原型污染/ReDoS 风险判为 High，并明确 fixture 无法支持“已废弃”结论
- PASS `evidence`：引用固定版本、`npm audit` 严重度、受影响范围和 GHSA 风险证据
- PASS `upgrade_plan`：给出 minimist `1.2.8` 与本轮 npm 报告的 lodash `4.18.1` 修复目标、SemVer/行为回归要求及短期输入限制和供应链控制

## With Skill Behavior

Fresh candidate 先确认 feature scope 和生产依赖清单，再按 skill 要求在隔离环境执行 npm 审计。结果区分直接依赖、已知漏洞、严重度与缺证据的 abandonment，不把未知维护状态写成事实；升级建议包含目标版本、breaking-change 风险、针对 CLI/object-path/template 使用的回归验证，以及无法立即升级时的输入限制、lockfile 和 CI audit 缓解。结论保持审查边界，依赖修改交 Engineer、构建控制交 DevOps、确认结论回 PM。

## Without Skill Baseline

本轮 fresh baseline 仅使用同一 prompt 与 fixture 独立生成，并单独运行 scratch `npm audit`；未读取 skill、Security Agent README 或历史 comparison。Baseline 也识别两个直接依赖、Critical/High 风险及升级/缓解措施，满足 4/4 assertions；但输出较短，未形成完整依赖审计结构，也未体现 Security→PM closeout 和跨角色交付边界。

## Failures

- 无 assertion failure。
- `npm audit` 需要 lockfile；本轮仅在两侧隔离 scratch 中生成，不修改或提交 fixture，因此不构成阻塞。

## Next Steps

- 当前 eval 无需修正；未来复验应继续在隔离副本实时生成审计证据，避免将可能变化的 advisory/fix target 固化为历史事实，并重新生成 without_skill baseline。

## Runtime Artifacts Policy

- 本轮隔离副本、临时 lockfile、npm audit 输出与 candidate/baseline 证据仅位于 `tmp/eval-runs/issue-143/batch-a`，验证后删除，不提交到 git。
- Runtime transcripts、verdicts、timing、diagnostics 及 with_skill / without_skill 目录均不得提交；durable 结果仅为本 `comparison.md`。
