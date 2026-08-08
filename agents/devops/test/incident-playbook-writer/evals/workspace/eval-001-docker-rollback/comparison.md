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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `500941dffb48347901d3283054321002e2a4be37cb509882170d999b6f27485f`
- Skill overlay SHA-256: `322b6fc4de918cf45a54ef853b436aea4069d29a5654d65d9e002fe4543294d8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ef78ea6924e16ad4c29c668948468977eb007b3ff9fb4e26733caf7d332c338d`
- Metadata SHA-256: `aaf6d95692337cdac99edc2200f96e32a7dbdc444f3865d1a29464638703fbd4`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_evidence_based_rollback` | PASS | with_skill 的 deploy/ROLLBACK.md 使用 release record 中已知健康、不可变 SemVer tag，设置 APP_IMAGE_TAG，执行 pull 与 up -d app，并核对 ps、日志和 /health。 |
| `creates_scoped_incident_response` | PASS | with_skill 的 deploy/INCIDENT_RESPONSE.md 明确 P1 15 分钟、P2 30 分钟响应时限，使用 #ops-incidents，指定 incident commander 和 service owner，并覆盖调查、恢复验证及恢复后关闭/记录。 |
| `avoids_unsupported_procedures` | PASS | 文档明确排除数据库 migration 回滚、缓存清理和无证据操作；with_skill 的 git evidence 显示未执行回滚或产生提交，候选输出也明确未执行实际回滚。 |
| `omits_unrequested_playbooks` | PASS | with_skill 的 git 状态和 workspace manifest 仅显示新增 deploy/ROLLBACK.md 与 deploy/INCIDENT_RESPONSE.md，没有 TROUBLESHOOTING.md 或 ON_CALL.md。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=15d6992485ca55334c51febc927c4b7bc210f805060cfb3f82f95fdc5de06e0a; snapshot_sha256=24af926265b96cf81abc73d3bde6228bffb79f2f2e3cac778db01a227983b28e
- Behavior: 新增两份目标手册，基于 fixture 契约覆盖回滚、事故响应和限制，未执行实际回滚或额外文档生成。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=c4c9c80f6a000743bb76c388bb71f6e0ebbcf6f2f818b9e4cdce3e2b380e54b0; snapshot_sha256=5d8cb7ca4a84e78e36a7674c705111e01c76b8ccac65ac17f6d3db005929bf54
- Behavior: 新增两份目标手册，未执行回滚；内容满足请求，但仅作比较基线。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a3dcab32ca6f16ce18a6d001bf4e11cedd9e9fc11b26bd45c079c620b67ec959`
- Skill overlay SHA-256: `f49bc0517e51e913154134ad0435ffac724d99a1f33e11d0280d2294a9d5c8bd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ef78ea6924e16ad4c29c668948468977eb007b3ff9fb4e26733caf7d332c338d`
- Metadata SHA-256: `aaf6d95692337cdac99edc2200f96e32a7dbdc444f3865d1a29464638703fbd4`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_evidence_based_rollback` | PASS | with_skill 输出明确要求使用 release record 中的 last known healthy、不可变 SemVer tag，设置 APP_IMAGE_TAG，执行 pull app 与重建 app，并验证容器状态、health、日志和 /health。 |
| `creates_scoped_incident_response` | PASS | with_skill 的 INCIDENT_RESPONSE.md 覆盖 P1 15 分钟、P2 30 分钟、#ops-incidents、incident commander、service owner，以及调查、恢复和恢复后检查。 |
| `avoids_unsupported_procedures` | PASS | with_skill 文档明确排除数据库 migration 回滚、数据恢复及仓库未提供的凭据修复或镜像重建流程；git_evidence 显示未执行实际回滚或提交变更。 |
| `omits_unrequested_playbooks` | PASS | with_skill 的 git_status、workspace_manifest 和 delivery_snapshot 均显示仅新增 deploy/ROLLBACK.md 与 deploy/INCIDENT_RESPONSE.md，没有 TROUBLESHOOTING.md 或 ON_CALL.md。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=8ecbd508d560dfb4379221465f14992207485e3618bc30de5c5d371043b0fe61; snapshot_sha256=dc70bea08b7633fd5a3620fb1faf1a973b54fe1e2bb2d2b79e4aae34feea02c0
- Behavior: 新增两份目标手册，基于 fixture 证据细化 Docker Compose healthcheck、P1/P2 故障场景、回滚流程和恢复确认，未执行实际操作。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=a7cff7a64c2085f6b60a7a4068392dee24b425830d51d88d6973f95323a861ea; snapshot_sha256=fa204c6baf7b98bbe9d831de4eea8a122f5c5ef3693d50847379323eaa3f8fef
- Behavior: 新增两份目标手册，内容满足主要范围与回滚契约，并未执行实际操作。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
