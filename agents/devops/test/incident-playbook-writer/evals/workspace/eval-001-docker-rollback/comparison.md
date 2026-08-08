# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-001-docker-rollback`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a` from `agents/devops/test/incident-playbook-writer/evals/workspace/eval-001-docker-rollback`.
- Fixture SHA-256: `f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a`
- Prompt SHA-256: `f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2ee427f056a8ac15cf9d4885d215c9ee8db1e2692beb4901545cf09914ace629`
- Skill overlay SHA-256: `c4126e3ccb08175ab528f594300ee6ab6305ac16fe0fbdfca38a793465cbc175`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ef78ea6924e16ad4c29c668948468977eb007b3ff9fb4e26733caf7d332c338d`
- Metadata SHA-256: `aaf6d95692337cdac99edc2200f96e32a7dbdc444f3865d1a29464638703fbd4`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_evidence_based_rollback` | PASS | with_skill delivery_snapshot contains deploy/ROLLBACK.md using the release record's last-known-healthy immutable SemVer tag, changing APP_IMAGE_TAG, pulling and recreating app, then checking status, logs, and /health. |
| `creates_scoped_incident_response` | PASS | with_skill delivery_snapshot contains deploy/INCIDENT_RESPONSE.md covering P1/P2 15/30-minute response targets, #ops-incidents, incident commander, service owner, investigation, recovery, and closure checks. |
| `avoids_unsupported_procedures` | PASS | The with_skill manuals explicitly prohibit database migration rollback, floating tags, deleting volumes, and unsupported actions; git_evidence shows no commits or executed rollback changes. |
| `omits_unrequested_playbooks` | PASS | with_skill git_status and workspace_manifest show only deploy/ROLLBACK.md and deploy/INCIDENT_RESPONSE.md added; no TROUBLESHOOTING.md or ON_CALL.md. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=9acefd8d1a1d0bfa933a88b832be3cf59717daae27c65907b7a42f91c4645ad4; snapshot_sha256=24492482dc875c27bd418a63ca8c729443cd38cdbf5284811e1e390dfeda98eb
- Behavior: Produced both requested manuals with Docker-contract-specific rollback, incident roles/timelines, recovery validation, and explicit exclusions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=fab50f34ef61556ab978e1cc2f8926cff055b5b16f930b3e02894953a3b509d4; snapshot_sha256=6a99c5a48df49e3de613c365a0af9a6983799ef025c386e954315b52c6a6aebb
- Behavior: Fresh baseline also produced the two requested manuals and avoided execution; with_skill provided more detailed evidence-based procedures and scoped recovery guidance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

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

# Eval Result: eval-001-docker-rollback

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-001-docker-rollback`
- Test case: `docker-rollback`
- Workspace: `agents/devops/test/incident-playbook-writer/evals/workspace/eval-001-docker-rollback`

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
- Eval definition: `agents/devops/test/incident-playbook-writer/evals/evals.json`
- Metadata: `agents/devops/test/incident-playbook-writer/evals/workspace/eval-001-docker-rollback/eval_metadata.json`
- Expected output: 仅生成用户明确请求且有仓库证据支撑的回滚与故障响应手册，不默认生成排查和值班文档
- Fixture: `PM_HANDOFF.md`, `deploy/docker/docker-compose.yml`, `deploy/docker/.env.example`, `deploy/docker/README.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `deploy_rollback_md` | PASS | PASS | 两条 lane 均实际生成 deploy/ROLLBACK.md。 |
| `rollback_md_docker` | PASS | PASS | 两条 lane 的 ROLLBACK.md 均包含 Docker Compose 拉取镜像、重建 app、状态/日志/health 验证等命令。 |
| `deploy_incident_response_md` | PASS | PASS | 两条 lane 均实际生成 deploy/INCIDENT_RESPONSE.md。 |
| `incident_response_md` | PASS | PASS | 两条 lane 的 INCIDENT_RESPONSE.md 均覆盖应用不可用、healthcheck 失败、容器重启/启动失败、发布后降级等常见故障场景。 |
| `does_not_generate_unrequested_playbooks` | FAIL | FAIL | 两条 lane 均额外生成 deploy/TROUBLESHOOTING.md 和 deploy/ON_CALL.md；实际输出明确称生成四份手册，违反仅生成回滚与故障响应手册的断言。 |

## With-Skill Behavior

- with_skill 的五条断言均可核对，Coverage 为 FULL；但额外生成未请求的 TROUBLESHOOTING.md 与 ON_CALL.md，因此 durable Overall 按 binding_result_model 判定为 FAIL。without_skill 同样失败，仅作为对照。
- Workspace changes: added: `deploy/INCIDENT_RESPONSE.md`, `deploy/ON_CALL.md`, `deploy/ROLLBACK.md`, `deploy/TROUBLESHOOTING.md`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `deploy/INCIDENT_RESPONSE.md`, `deploy/ON_CALL.md`, `deploy/ROLLBACK.md`, `deploy/TROUBLESHOOTING.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `does_not_generate_unrequested_playbooks`。
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
