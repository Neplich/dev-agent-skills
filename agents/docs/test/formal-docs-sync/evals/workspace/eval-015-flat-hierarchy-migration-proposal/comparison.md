# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-015-flat-hierarchy-migration-proposal`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-015-flat-hierarchy-migration-proposal`.
- Identity schema: `2`
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `b33925735dcdc1c16e96ba8e543e331eebb29f1fb2575eb75afef7012c2934cd`
- metadata_sha256: `1745a4b411c4974d9b158bc811fac50658345383bc93cab2e1df286dcb1629d0`
- fixture_sha256: `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `162b3544cbde876f526df1805303ea3ab78e34b2ebde819bbdbfe83bc8251b8c`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | PASS | with_skill 输出在候选范围前列出扁平 API 页面，并依据 feature domain、feature_path、route prefix/tag、owner 与 related code 将 research-conversations.md 和 graph-search.md 归入缺失的 knowledge-discovery（知识发现与应用）域节点。 |
| `proposes_migration_before_write` | PASS | with_skill 输出提供了各级 index.md 目标子树、research-conversations.md 的旧新路径映射、入链和递归导航 delta、change-map required_docs 前后差异、排除项、新会话消息叶子位置，并给出迁移并批次确认、仅确认批次、全部推迟三个选项后等待维护者确认。 |
| `does_not_deepen_flat_layout` | PASS | delivery_snapshot 为空，git_evidence 显示 HEAD、分支、工作区和索引均未变化；输出明确未运行 host checks，并将新页面放入目标子树而非 docs/site/api/ 一级。 |
| `reports_out_of_batch_drift_read_only` | PASS | with_skill 输出将 document-ingestion.md、knowledge-curation.md、workspace-governance.md、background-jobs.md 分别列为 knowledge-building 和 platform-governance 的 out-of-batch drift，给出建议目标节点并明确仅观察、不纳入本次范围；同时未产生文件变更。 |
| `loads_only_api_contract` | PASS | runner_captured_trace 直接显示读取 formal-docs-sync API 类型说明和 docs/site/standards/templates/api-template.md，并读取共用宿主标准；未显示读取或应用 database、design、ops、product 类型模块或对应模板。with_skill 输出显式报告 loaded_type_modules、loaded_host_templates 与 hierarchy_drift。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=440f9fbba8a2a1ceaed88b476d46ff78dd98935601c8fad5b7d8e03622b9aac2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成写入前的 API 层级漂移识别、迁移提案、批次外只读报告，并在等待范围确认时保持零写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=192a4a44eb7a7ad75af48dc5c98a87201d1c83ab1b17ab1c972e071cc3cfbeaf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅提出在扁平 docs/site/api/ 下新增页面和根索引链接，未识别层级漂移，也未提出迁移或批次外 drift 报告。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
