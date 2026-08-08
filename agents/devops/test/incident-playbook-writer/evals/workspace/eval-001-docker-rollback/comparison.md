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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `500941dffb48347901d3283054321002e2a4be37cb509882170d999b6f27485f`
- Skill overlay SHA-256: `8bcf98d79219616ab4a2e4bf38f41850dabf91363c7e81c3766a5503c4452405`
- Judge schema SHA-256: `82478d5bfcdfccbe67817c9bfae394096b57b2c317a4413eadf1808b946de6d0`
- Eval definition SHA-256: `ef78ea6924e16ad4c29c668948468977eb007b3ff9fb4e26733caf7d332c338d`
- Metadata SHA-256: `aaf6d95692337cdac99edc2200f96e32a7dbdc444f3865d1a29464638703fbd4`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_evidence_based_rollback` | PASS | Locked deploy/ROLLBACK.md selects the last known healthy immutable SemVer tag from the release record, changes APP_IMAGE_TAG, pulls and recreates app with the repository Compose file, then checks status, logs, and /health. |
| `creates_scoped_incident_response` | PASS | Locked deploy/INCIDENT_RESPONSE.md specifies P1/15-minute and P2/30-minute response, #ops-incidents, incident commander and service owner roles, investigation, recovery, and post-recovery checks. |
| `avoids_unsupported_procedures` | PASS | The locked documents explicitly exclude database migration rollback, floating or guessed tags, unsupported runtime changes, and destructive actions; git evidence shows no rollback execution or commits. |
| `omits_unrequested_playbooks` | PASS | Locked git status shows only deploy/ROLLBACK.md and deploy/INCIDENT_RESPONSE.md as new files; no troubleshooting or on-call playbooks were delivered. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=e731b4de4056836c4162933fc7988c67f038676cd0997278848a8b0e9b96c7e8; snapshot_sha256=06810d04a9a51339888e42bc042341dd8319dac6ac33e7ab1f7ad1e51aa78190
- Behavior: Delivered both requested evidence-grounded Docker Compose handbooks with explicit operational boundaries and verification steps.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=18d38285572cda2a473a79904f01f995f4b6132457312dc446ee505aa91bac2b; snapshot_sha256=943403b7824dda0ddcf2a921c39a770b196b90ba77a07eec0e47fa0ba250ee25
- Behavior: Also delivered the two requested handbooks, serving as a comparison baseline; its behavior does not alter the with_skill verdicts.
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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `500941dffb48347901d3283054321002e2a4be37cb509882170d999b6f27485f`
- Skill overlay SHA-256: `8bcf98d79219616ab4a2e4bf38f41850dabf91363c7e81c3766a5503c4452405`
- Judge schema SHA-256: `82478d5bfcdfccbe67817c9bfae394096b57b2c317a4413eadf1808b946de6d0`
- Eval definition SHA-256: `ef78ea6924e16ad4c29c668948468977eb007b3ff9fb4e26733caf7d332c338d`
- Metadata SHA-256: `aaf6d95692337cdac99edc2200f96e32a7dbdc444f3865d1a29464638703fbd4`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_evidence_based_rollback` | PASS | with_skill 的 deploy/ROLLBACK.md 要求从 release record 选择已知健康不可变 SemVer tag，更新 APP_IMAGE_TAG，执行 compose pull/up -d app，并核对 ps、日志和 /health。 |
| `creates_scoped_incident_response` | PASS | with_skill 的 deploy/INCIDENT_RESPONSE.md 覆盖 P1/P2 时限、#ops-incidents、incident commander、service owner、证据调查、恢复判定及事件关闭后的记录检查。 |
| `avoids_unsupported_procedures` | PASS | 两份手册均明确不执行数据库 migration 回滚，使用的 Docker Compose 命令与 fixture 中的运行契约一致；git evidence 显示未执行回滚且未改变提交。 |
| `omits_unrequested_playbooks` | PASS | with_skill lane 仅新增 deploy/ROLLBACK.md 和 deploy/INCIDENT_RESPONSE.md，未生成 TROUBLESHOOTING.md 或 ON_CALL.md。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=40ddad7f474daefba700be0492508c6cde43c6dfc1596204b1a9c98a7a30b28d; snapshot_sha256=bdb931fae1f9918af024c1d32716bbb60970a74709cf10ec9ae38acd6bf4601e
- Behavior: 交付两份范围内手册，内容与 Docker 契约和故障响应要求一致，未执行回滚或生成额外 playbook。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=e3ce2185574161af1b0a57efc4ab50df8059cd5b1e7b31faaa2eab80224b4c90; snapshot_sha256=a585eb64de37107908a0fb74dcb0c540c5edd868e294004e50b0f515e1ba104a
- Behavior: 同样交付两份符合要求的手册，覆盖核心 Docker 回滚及事件响应约定；作为对照，其结果未影响 with_skill 断言判定。
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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `500941dffb48347901d3283054321002e2a4be37cb509882170d999b6f27485f`
- Skill overlay SHA-256: `8bcf98d79219616ab4a2e4bf38f41850dabf91363c7e81c3766a5503c4452405`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ef78ea6924e16ad4c29c668948468977eb007b3ff9fb4e26733caf7d332c338d`
- Metadata SHA-256: `aaf6d95692337cdac99edc2200f96e32a7dbdc444f3865d1a29464638703fbd4`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_evidence_based_rollback` | PASS | with_skill delivery_snapshot contains deploy/ROLLBACK.md using a previous known-healthy immutable SemVer tag, APP_IMAGE_TAG update, docker compose pull app, recreation, and checks for status, logs, healthcheck, and /health. |
| `creates_scoped_incident_response` | PASS | with_skill delivery_snapshot contains deploy/INCIDENT_RESPONSE.md covering P1/P2 response times, #ops-incidents, incident commander, service owner, investigation, recovery, and closure checks. |
| `avoids_unsupported_procedures` | PASS | The locked with_skill documents explicitly exclude database migration rollback, unsupported remediation, broad deployment changes, and Helm; git evidence shows no commits or repository mutations, and the candidate reports no rollback execution. |
| `omits_unrequested_playbooks` | PASS | with_skill git status and workspace manifest show only deploy/ROLLBACK.md and deploy/INCIDENT_RESPONSE.md as new deliverables; no TROUBLESHOOTING.md or ON_CALL.md is present. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=dca636410e5a65f91f624e1b56cddafa20dafc9656ee743d044409bb4078762a; snapshot_sha256=f9d1e47964df7c6b0117bf4971badaffa4ed8a95f7418d0bebf133af30625735
- Behavior: Produced both scoped manuals with evidence-based Docker Compose procedures, explicit unsupported-operation boundaries, and no repository commit or reported rollback execution.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=5ad90c17365f5f1e91fd0b82272e71b24aceee3289061b5d856a3f0287c79b02; snapshot_sha256=2262b9195d31a537487984abf35ab341485f0e8509e258d2fbce402ba1379af5
- Behavior: Produced both requested manuals with relevant coverage and no reported rollback execution.
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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `500941dffb48347901d3283054321002e2a4be37cb509882170d999b6f27485f`
- Skill overlay SHA-256: `322b6fc4de918cf45a54ef853b436aea4069d29a5654d65d9e002fe4543294d8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ef78ea6924e16ad4c29c668948468977eb007b3ff9fb4e26733caf7d332c338d`
- Metadata SHA-256: `aaf6d95692337cdac99edc2200f96e32a7dbdc444f3865d1a29464638703fbd4`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_evidence_based_rollback` | PASS | with_skill 的 deploy/ROLLBACK.md 使用 release record 中已知健康的不可变 SemVer tag，设置 APP_IMAGE_TAG，执行 pull 与 up -d app，并核对容器状态、日志和 /health。 |
| `creates_scoped_incident_response` | PASS | with_skill 的 deploy/INCIDENT_RESPONSE.md 覆盖 P1/P2 响应时限、#ops-incidents、incident commander、service owner、调查、恢复及恢复后验证和关闭记录。 |
| `avoids_unsupported_procedures` | PASS | with_skill 明确排除数据库 migration 回滚和未经证据支持的 tag/告警阈值；git evidence 显示未执行实际回滚，且仅记录文档中的受支持 Compose 操作。 |
| `omits_unrequested_playbooks` | PASS | with_skill 的 git_status 和交付快照仅显示 deploy/ROLLBACK.md 与 deploy/INCIDENT_RESPONSE.md，未生成 TROUBLESHOOTING.md 或 ON_CALL.md。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=7e162a31cf7a15831f7a57c4a58dbca2b012fbd301360fd70cbe94ad2dbd1789; snapshot_sha256=3a80e472ed7037f51868c931738d727e60f88dfe7e8bcbe680a6e9c9fb564625
- Behavior: 创建了两份目标手册，复用 Docker/健康检查契约，覆盖事件响应边界，并未执行回滚。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=91c9c4ace96a6d6b14a62573c6a794b6ffeeffc015e5498c65c0332451620980; snapshot_sha256=ae89b0ecaa0ea464c28cde177af7b9dcd22ff4dabd2fc06962ea460105aac602
- Behavior: 创建了两份目标手册，未执行回滚；内容总体满足请求。
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
