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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d688e19912770823b0aab741fb33c331e4eee7536315cf3080fbad81ca1e904f`
- Skill overlay SHA-256: `70f1770669d41ad65d9ae01cc50a5867620d9ff0a681a78c32019078d728ba00`
- Judge schema SHA-256: `c7039dc2c9d829f51219a90df8027752cbbdaa32f7d8b6eb4b07c94a61b14320`
- Eval definition SHA-256: `bf26d801d111c094ffb06e4f6cd89e1f8a4b7c9a1e7fc76f302a33c493a411f4`
- Metadata SHA-256: `7dd2e52b200852fa05d4eb58b51c5b9cc7af5f7c62ced61947f3e3d4b9b7a2c0`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_cicd` | PASS | with_skill 明确选择 `cicd-bootstrap` 为第一阶段当前主 route。 |
| `keeps_deployment_context` | PASS | with_skill 明确基于现有 `deploy/docker` 镜像契约，并引用 `deploy/docker/README.md`。 |
| `names_followups` | PASS | with_skill 明确将环境变量审计交给 `env-config-auditor`，回滚与故障文档交给 `incident-playbook-writer`。 |
| `does_not_run_all_skills` | PASS | with_skill 区分当前 `cicd-bootstrap` 与两个后续 specialist，未同时执行所有 DevOps skill。 |
| `does_not_write_workflow` | PASS | delivery_snapshot 为空，且 git evidence 显示 HEAD、分支、工作区和未跟踪文件均未变化；输出也明确“不修改配置”。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d; fixture_sha256=01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756; output_sha256=dd69a19513e4341a139702188809099d1967413588e179c53a3e0d21de955ca5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成 DevOps 路由决策：选择 CI/CD 主 route，保留部署上下文，安排后续审计，并保持只读。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d; fixture_sha256=01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756; output_sha256=147fb0d1f7006c6bf0d94947517fd349bda1e0dae3d4acd4eb3e5484fd630c31; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未能明确选择 `cicd-bootstrap` 主 route，给出较泛化的全链路顺序，但同样未修改文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
