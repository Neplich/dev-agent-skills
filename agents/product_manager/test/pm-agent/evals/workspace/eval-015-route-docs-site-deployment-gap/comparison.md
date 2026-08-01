# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-015-route-docs-site-deployment-gap`
- Review context: PR #204 eval assertion alignment and fresh paired validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0; current prompt, revised `routes_devops_main_route` assertion, and current evidence fixture
- Validation date: 2026-08-01
- with_skill source: fresh Codex validator，完整读取并应用当前 `agents/product_manager/README.md`、`agents/product_manager/skills/pm-agent/SKILL.md` 与共享 handoff/closeout 契约后，读取独立 fixture copy。
- without_skill source: 同一原始 prompt 与另一份独立 fixture copy 的全新 Codex baseline；未读取或应用目标 README/skill，未复用旧 baseline、旧 comparison 或 with_skill 输出。
- Runtime root: `tmp/eval-runs/pr-204-fix-round-20260801/pm-agent/eval-015-route-docs-site-deployment-gap/`。

## Latest Result

- Behavior result: **PASS**（3/3 assertions PASS）
- Coverage result: **FULL**（3/3 assertions 均被当前场景触发并完成判定）
- Overall result: PASS

## Assertions

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unknown_evidence` | PASS | with_skill 对最初缺少 CI 与生产 Helm 权限的报告保持 `unknown`，明确真实配置证据缺口，未推断 integrated 或构造 ready handoff。 |
| `builds_repo_wide_deployment_packet` | PASS | 用户确认纳入后，with_skill 生成 `request_type: deployment` packet，全部 feature fields 为 `N/A`、`feature_path_evidence: []`，并在 `source_documents` / `blockers_risks` 保留 `evidence.md`、Internal 未集成和写操作未授权事实。 |
| `routes_devops_main_route` | PASS | with_skill 路由到 `devops-agent` 主 route，声明 DevOps specialist 权威门禁与内部路由适用；未要求 pm-agent 点名或排序 specialist 内部链路。 |

## With-Skill Behavior

with_skill 严格区分初始证据不足的 `unknown`、补证后的 `partial` 与用户确认纳入后的 ready routing。它建立完整 repo-wide deployment packet，同时保留 commit、push、镜像发布和部署均未获授权的边界。按修订后的 router 指针契约，它只将工作交给 `devops-agent` 主 route，由 DevOps router 决定内部 specialist，不再把 specialist 内部顺序当作 PM router 的断言。

## Fresh Without-Skill Baseline

fresh baseline 正确保留初始 `unknown`，补证后识别 Public 已接入、Internal 缺失，并没有越过写操作授权边界。但它只泛化交给运维团队，未生成 schema 完整的 cross-role packet，也未表达 `N/A` feature scope、空 `feature_path_evidence` 或 specialist 权威门禁指针。with_skill 在可执行 handoff 和角色边界上有明确增益。

## Failures

- 无。

## Next Steps

- 无 eval 行为修复项；维持 PM router 只路由 DevOps 主 route、内部 specialist 顺序由 DevOps 权威契约管理的边界。

## Runtime Artifacts Policy

- 本轮 candidate、fresh baseline、fixture copies 与 judge 仅位于 `tmp/eval-runs/pr-204-fix-round-20260801/pm-agent/eval-015-route-docs-site-deployment-gap/`，不提交到 git。
- 提交范围仅包含 canonical `comparison.md`；不提交 with_skill / without_skill、transcript、verdict、timing、diagnostics 或其他运行期文件。
