# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-013-deployment-aggregate-migration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-013-deployment-aggregate-migration`.
- Identity schema: `2`
- target_skill_sha256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- eval_definition_sha256: `2adf472912fe37066628cc2da23affed241d146a6c7c80728c7df93b4f2fccc7`
- metadata_sha256: `1730a36a001d532f328500208fe2ccb136183d8551b840ea714421749b8365ea`
- fixture_sha256: `b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `cb68cc7396b4ed1007a2bd5b5970baa015053110168fade98a969dbebc84c1b1`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | FAIL | 旧聚合页已删除并创建新页面树，但根索引仍重复写入 APP_PORT=8080 和 /healthz 等共享环境事实。 |
| `repairs_inbound_and_internal_links` | PASS | 快照显示 ops/index.md、product/runtime.md 已更新；各子页的相对环境引用和根索引链接均可解析，原始链接检查报告 broken=0。 |
| `updates_change_map_without_data_loss` | PASS | change-map 已按部署类别更新为稳定、去重列表，并保留 custom_owner_field、exclude 及 src/product 无关映射；原始检查确认列表均唯一且稳定排序。 |
| `updates_navigation_atomically` | PASS | 文件变更包含页面移动、导航、链接和 change-map；runner 原始命令显示 npm run test:docs 2/2 通过，残留旧路径扫描无结果，内部 Markdown 链接 broken=0。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e; output_sha256=c6df08b3eee2ef65e704a12f60b8cca791a571d71ffff0c77504f4572544db55; snapshot_sha256=3c68258a50adeded2a583824dd8b9b1daba187fa2269b6732ab2d6d20825d4ff
- Behavior: 完成迁移、链接修复、映射更新和测试，但根索引保留共享环境事实，未完全满足去重要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=b9cf5f02e5624842eefaa770fff8e84ccfc602f0eed28accf48a25400705d39e; output_sha256=03413915ef27a24173fd858cef273ae3eef3786e79930fe93f0e2020281589de; snapshot_sha256=8bcd183de6bd71505351de1dc9ff0dee4811e146de692b96e54740b2067c27d7
- Behavior: 报告完成了迁移、链接修复、映射保留和测试；作为比较基线，缺少 with_skill 的详细同步决策与验证证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- migrates_aggregate_path：根索引复制了应仅保留在 environment-reference.md 的共享环境事实。
- Next: 将根索引中的 APP_PORT 和 /healthz 共享事实移除，仅保留指向 environment-reference.md 的导航说明。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
