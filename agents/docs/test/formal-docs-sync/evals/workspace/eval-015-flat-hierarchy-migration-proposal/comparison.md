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
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `b33925735dcdc1c16e96ba8e543e331eebb29f1fb2575eb75afef7012c2934cd`
- metadata_sha256: `1745a4b411c4974d9b158bc811fac50658345383bc93cab2e1df286dcb1629d0`
- fixture_sha256: `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `162b3544cbde876f526df1805303ea3ab78e34b2ebde819bbdbfe83bc8251b8c`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | PASS | with_skill 明确列出 research-conversations.md 与 graph-search.md，并依据 feature/catalog 归属及共同的 knowledge-discovery 域目标节点识别漂移。 |
| `proposes_migration_before_write` | FAIL | with_skill 提供了候选树、旧路径映射、导航 delta、排除项、批次新页面位置及三个确认选项，但 graph-search.md 行的 required_docs delta 仅写“同上”，未给出该 code_glob 的精确 before/after 清单。 |
| `does_not_deepen_flat_layout` | PASS | with_skill 将新页面放在 knowledge-discovery/conversations 下，明确不迁移既有页面；git evidence 显示无写入，且 trace 显示 host checks 未运行、流程等待维护者确认。 |
| `reports_out_of_batch_drift_read_only` | PASS | with_skill 将 knowledge-building 与 platform-governance 的页面分别列为批次外 drift，给出目标节点并明确只读观察和不纳入本次范围。 |
| `loads_only_api_contract` | PASS | with_skill 显式报告 loaded_type_modules: API 和 loaded_host_templates，并在 trace 中读取 API 类型模块及共用宿主规范/API 模板，未读取 database、design、ops、product 类型模板内容；同时显式给出 Hierarchy drift 字段。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=98c24c490e780c7011940232539bbfbff287b1d8a5ef0f2bd7ed63601888eac8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了扁平层级 drift，提出了带目标树和迁移选择的候选方案，将新页面置于层级目录并在维护者确认前保持只读等待。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=e11aad86de093370f5f92764d53a408bcc905a4af7aa69d42a78be45a464bed9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅提出扁平 API 根目录下的新页面和最小导航链接，未识别完整层级 drift，也未提出迁移方案。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- proposes_migration_before_write 未为 graph-search.md 提供精确的 change-map required_docs before/after delta，而是引用“同上”，且该页面属于不同 code_glob。
- Next: 补全 graph-search.md 所属 code_glob 的 required_docs before/after 精确 delta，然后重新请求维护者确认。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
