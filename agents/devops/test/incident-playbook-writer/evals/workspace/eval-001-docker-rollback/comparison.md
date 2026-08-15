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
- Identity schema: `2`
- target_skill_sha256: `50cae2b4bb9c10d0d200f08d68ca4dd9d27b329f1a2b94cb2b8cb7333b3815ce`
- eval_definition_sha256: `ef78ea6924e16ad4c29c668948468977eb007b3ff9fb4e26733caf7d332c338d`
- metadata_sha256: `fe85f6eb6336802a8ad0f9268aaeda74d6a32f5dafcd0a67b8753f30859c10b1`
- fixture_sha256: `f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `82478d5bfcdfccbe67817c9bfae394096b57b2c317a4413eadf1808b946de6d0`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `f3eab55f60df9bb2b74211b8616c657af594a2e8a1c83328a335347ab9dd3bf1`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_evidence_based_rollback` | PASS | with_skill 的 deploy/ROLLBACK.md 使用 release record 的已知健康不可变 SemVer tag，设置 APP_IMAGE_TAG，执行 pull 与 up -d app，并核对 ps、日志和 /health。 |
| `creates_scoped_incident_response` | PASS | with_skill 的 deploy/INCIDENT_RESPONSE.md 明确 P1/P2 的 15/30 分钟响应目标、#ops-incidents、incident commander、service owner，以及调查、恢复和恢复后关闭检查。 |
| `avoids_unsupported_procedures` | PASS | 文档明确排除数据库 migration 回滚和未确认 tag；locked raw evidence 显示未执行实际 Docker 回滚或服务变更。 |
| `omits_unrequested_playbooks` | PASS | with_skill 仅交付 deploy/ROLLBACK.md 与 deploy/INCIDENT_RESPONSE.md，未生成 TROUBLESHOOTING.md 或 ON_CALL.md。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=ee78d902dc17f26228b5246679bb2972afaab4d299f4ced03c5e9f0229268c95; snapshot_sha256=91287b3bd3583a190f3083564ca9a118eee8bffde378cd4cd8004d1ff76ae2cd
- Behavior: 生成了两份基于现有 Docker Compose 契约的目标手册，范围受控且未执行实际回滚。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=7ebc940f19b13782e4a0f9c7ed550ec59aa60ff82ee7d603fbd889ea7adf8cf0; snapshot_sha256=ff8ec10450fe4d191db0ef828cf1a41a967c6d82d0b7d0d5381d619ad4648b44
- Behavior: 同样生成了两份符合要求的手册，作为 fresh baseline 与 with_skill 行为基本一致。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
