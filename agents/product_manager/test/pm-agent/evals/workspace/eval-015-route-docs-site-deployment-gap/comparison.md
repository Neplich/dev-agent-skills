# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-015-route-docs-site-deployment-gap`
- Review context: PR #204 eval assertion alignment and fresh paired validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0; current prompt, restored `routes_devops_ordered_chain` assertion, and current evidence fixture
- Validation date: 2026-08-01
- with_skill source: fresh Codex validator，完整读取并应用当前 `agents/product_manager/README.md`、`agents/product_manager/skills/pm-agent/SKILL.md` 与共享 handoff/closeout 契约后，读取独立 fixture copy。
- without_skill source: 同一原始 prompt 与另一份独立 fixture copy 的全新 Codex baseline；未读取或应用目标 README/skill，未复用旧 baseline、旧 comparison 或 with_skill 输出。
- Runtime root: `tmp/eval-runs/pr-204-eval-015-ordered-20260801-102733/pm-agent/eval-015-route-docs-site-deployment-gap/`。

## Latest Result

- Behavior result: **PASS**（3/3 assertions PASS）
- Coverage result: **FULL**（3/3 assertions 均被当前场景触发并完成判定）
- Overall result: PASS

## Assertions

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unknown_evidence` | PASS | with_skill 对最初缺少 CI 与生产 Helm 权限的报告保持 `unknown`，明确真实配置证据缺口，未推断 integrated 或构造 ready handoff。 |
| `builds_repo_wide_deployment_packet` | PASS | 用户确认纳入后，with_skill 生成 `request_type: deployment` packet，全部 feature fields 为 `N/A`、`feature_path_evidence: []`，并在 `source_documents` / `blockers_risks` 保留 `evidence.md`、Internal 未集成和写操作未授权事实。 |
| `routes_devops_ordered_chain` | PASS | with_skill 精确按 `deployment-planner` → `cicd-bootstrap` → `env-config-auditor` → `formal-docs-sync` handoff，并明确最终 Docs 只同步已落地且验证的运维事实。 |

## With-Skill Behavior

with_skill 严格区分初始证据不足的 `unknown`、补证后的 `partial` 与用户确认纳入后的 ready routing。它建立完整 repo-wide deployment packet，同时保留 commit、push、镜像发布和部署均未获授权的边界；随后按权威契约给出四段依赖链及逐阶段 gate，当前只交接到 `devops-agent:deployment-planner`。

## Fresh Without-Skill Baseline

fresh baseline 也满足本轮三条 assertions：保留初始 `unknown`，在补证和用户确认后生成 N/A feature scope 的 deployment packet，并给出相同的四段依赖顺序和最终 Docs 限制。其 packet 相对简化，缺少 with_skill 中的 `change_tier`、`parent_feature`、`feature_level`、`downstream_owner` 与 `required_output`，但这些字段不在本轮三条 assertion 的判定范围内。

## Failures

- 无。

## Next Steps

- 无 eval 行为修复项；with_skill 已满足恢复后的有序链契约，不触发 pm-agent `SKILL.md` 条件修复分支。

## Runtime Artifacts Policy

- 本轮 candidate、fresh baseline、fixture copies 与 judge 仅位于 `tmp/eval-runs/pr-204-eval-015-ordered-20260801-102733/pm-agent/eval-015-route-docs-site-deployment-gap/`，不提交到 git。
- 提交范围仅包含 canonical `comparison.md`；不提交 with_skill / without_skill、transcript、verdict、timing、diagnostics 或其他运行期文件。
