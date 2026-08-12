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
- target_skill_sha256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- eval_definition_sha256: `b33925735dcdc1c16e96ba8e543e331eebb29f1fb2575eb75afef7012c2934cd`
- metadata_sha256: `1745a4b411c4974d9b158bc811fac50658345383bc93cab2e1df286dcb1629d0`
- fixture_sha256: `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `162b3544cbde876f526df1805303ea3ab78e34b2ebde819bbdbfe83bc8251b8c`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | PASS | 识别 `research-conversations.md` 与 `graph-search.md` 均归属 `knowledge-discovery`，并以 feature catalog、feature_path、route prefix/tag、owner 与 related_code 为依据。 |
| `proposes_migration_before_write` | PASS | 写入前给出完整目标树、迁移映射、入链/递归导航 delta、required_docs delta、排除项及三个确认选项，并等待维护者确认。 |
| `does_not_deepen_flat_layout` | PASS | 候选输出和 git/raw trace 均显示零写入、未移动旧页、未在一级 API 目录追加页面，且 host checks 未运行。 |
| `reports_out_of_batch_drift_read_only` | PASS | 列出知识建设与维护、平台治理与运行的批次外页面及目标节点，并明确不纳入本次范围且不修改。 |
| `loads_only_api_contract` | PASS | raw trace 仅读取 API 类型指令与 API 模板，未读取其他四类类型模块或模板；最终报告显式包含 `loaded_type_modules`, `loaded_host_templates` 与 `hierarchy_drift`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=1da0bbc84f1ad1c0e83f9019d35b671d50512b7d3c603324bb6050cf1b644710; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成只读核验，识别层级 drift，提出迁移与本批次范围的原子确认方案，并等待确认；未写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=641841494f93a2cad35730761183a6d38280517fd8ab3e98cbb963cfa70d8ad6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出扁平一级叶子页方案，未识别层级 drift 或迁移需求；保持零写入。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
