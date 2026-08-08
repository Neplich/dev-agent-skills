# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-001-route-ci-readiness`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756` from `agents/devops/test/devops-agent/evals/workspace/eval-1-route-ci-readiness`.
- Fixture SHA-256: `01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756`
- Prompt SHA-256: `0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4c5e2e817a46aa6aa63d1e8786af2b82affbb324db7f825fe732309004758885`
- Skill overlay SHA-256: `aded9ff26538c3b2aa5b54511df74fe874ce0fceb522bbdacfc566b61cb748d5`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bf26d801d111c094ffb06e4f6cd89e1f8a4b7c9a1e7fc76f302a33c493a411f4`
- Metadata SHA-256: `7dd2e52b200852fa05d4eb58b51c5b9cc7af5f7c62ced61947f3e3d4b9b7a2c0`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_cicd` | PASS | with_skill 明确将 `cicd-bootstrap` 作为第一步主 route，针对 GitHub Actions PR 门禁缺口。 |
| `keeps_deployment_context` | PASS | with_skill 明确基于现有仓库内容，并指出当前可见的 `deploy/docker/README.md`，未假设从零创建部署资产。 |
| `names_followups` | PASS | 明确将环境变量审计路由为 `env-config-auditor`，回滚文档路由为 `incident-playbook-writer`。 |
| `does_not_run_all_skills` | PASS | 区分当前 CI/CD 主 route 与后续环境变量、回滚检查，并明确本阶段不扩展其他部署范围。 |
| `does_not_write_workflow` | PASS | 输出明确表示本轮只做只读事实核对，且 git evidence 显示无文件、分支或提交变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d; fixture_sha256=01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756; output_sha256=480d4bc5d8cdbfcc187cedfbb0eba53e49bec9464c53dfc08ae2bd628d725070; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 将 `cicd-bootstrap` 设为主 route，保留 `deploy/docker` 上下文，明确后续两个 specialist route，并保持只读、不修改配置。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d; fixture_sha256=01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756; output_sha256=31f08e15a0da46f1760ea60e0b0de81070592cf393cfd1ba814f6f4c865d2c9d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出先盘点部署资产、再审计环境变量、设计 PR 门禁和补齐回滚文档；未使用指定 routes，主次顺序与目标不完全匹配。
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

# Eval Result: eval-001-route-ci-readiness

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-001-route-ci-readiness`
- Test case: `route-ci-readiness`
- Workspace: `agents/devops/test/devops-agent/evals/workspace/eval-1-route-ci-readiness`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: FAIL
- Coverage result: FULL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: FAIL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/devops-agent/evals/evals.json`
- Metadata: `agents/devops/test/devops-agent/evals/workspace/eval-1-route-ci-readiness/eval_metadata.json`
- Expected output: DevOps 路由决策，明确 CI/CD 是当前主 route，配置审计和 runbook 是后续检查，而不是一次性直接执行所有 DevOps skill。
- Fixture: `deploy/docker/README.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `routes_primary_to_cicd` | PASS | FAIL | with_skill-final 明确识别 CI/CD 为缺口，并在建议链中将 cicd-bootstrap 排在后续 DevOps 路由首位；without_skill 未进行路由决策。 |
| `keeps_deployment_context` | PASS | PASS | 两条 lane 均保留并读取 deploy/docker/README.md 上下文；with_skill-final 还明确指出该目录已存在。 |
| `names_followups` | PASS | FAIL | with_skill-final 明确列出 env-config-auditor 与 incident-playbook-writer，并按 CI/CD 后续链路排列；without_skill 仅直接编写文档，未命名这些后续 route。 |
| `does_not_run_all_skills` | FAIL | FAIL | with_skill-final 给出 pm-agent → cicd-bootstrap → env-config-auditor → incident-playbook-writer 的全链路执行建议，未清晰区分当前主 route 与后续检查；without_skill 实际直接新增 workflow、环境变量文档和回滚文档。 |
| `does_not_write_workflow` | PASS | FAIL | with_skill-status 的 changes.added/modified 均为空，且 with_skill lane 没有 .github/workflows 文件；without_skill-status 显示新增 .github/workflows/pr-checks.yml。 |

## With-Skill Behavior

- with_skill 成功识别 CI/CD 主方向、保留部署上下文并命名后续 route，也未写入 workflow；但其最终建议仍扩展为未区分主 route 与后续检查的全链路，因此 durable Behavior 为 FAIL。Coverage 为 FULL。without_skill 作为对照，直接实施了全部变更。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `.github/workflows/pr-checks.yml`, `deploy/docker/ENVIRONMENT.md`, `deploy/docker/ROLLBACK.md`；modified: `deploy/docker/README.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `does_not_run_all_skills`。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（5/5）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 按上表 with_skill failure 的共同根因建立后续修复项；本轮只记录结果，不修改 skill、eval 定义或 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
