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
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | FAIL | with_skill 明确指出 API 根目录扁平漂移并列出 research-conversations.md、graph-search.md 及其目标路径，但没有明确说明二者共同属于同一个缺失的知识发现与应用域节点，也未为两者分别给出足够的已确认证据依据。 |
| `proposes_migration_before_write` | FAIL | with_skill 给出了目标子树、会话页面位置、research-conversations.md 的路径映射、导航变化和部分 change-map delta，并提供三个决策选项；但迁移映射只覆盖 research-conversations.md，未覆盖已识别的其他 drift 页面，因此未满足每个旧路径的完整迁移提案要求。 |
| `does_not_deepen_flat_layout` | PASS | with_skill 的交付快照为空，git 状态与 diff 均无变更；输出明确表示等待范围确认，未执行写入后的 host checks 或完成审计交接，也未把新页面追加到 docs/site/api/ 一级。 |
| `reports_out_of_batch_drift_read_only` | PASS | with_skill 列出了 document-ingestion.md、knowledge-curation.md、workspace-governance.md、background-jobs.md 及建议目标节点，并通过“本批次相关的漂移是 research-conversations.md”和排除其他 API 功能表明这些批次外事项仅作观察、不纳入本次范围。 |
| `loads_only_api_contract` | PASS | runner_captured_trace 显示读取了 formal-docs-sync 的 API 类型说明、API 模板及共用宿主标准，未读取 database、design、ops、product 类型模块或对应模板；最终输出显式给出 loaded_type_modules: api、loaded_host_templates 和 hierarchy_drift 字段。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=e95af4e176a110745bbc01478d82034887e4fae31f97c56b8097748e6a9501b3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 只读完成范围确认，保留现有文件不变；识别了 API 扁平漂移并提出分层页面树与部分迁移方案，但 drift 归属论证和完整迁移映射不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=eedd9a1d3f24b95da81205ef42fe31b145bd90ca5b5b598253dbc54d672125bd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出了一级扁平 API 新页面和索引入口，明确不迁移既有页面；未识别层级 drift，也未提出迁移决策或批次外 drift 报告。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整识别并论证 research-conversations.md 与 graph-search.md 共同归属的缺失知识发现与应用域节点。
- with_skill 的迁移提案未覆盖所有已识别扁平 drift 页面到目标路径的映射。
- Next: 补充 research-conversations.md 与 graph-search.md 共同归属缺失 knowledge-discovery 节点的 feature catalog、feature_path、route prefix/tag、related_code 或 owner 证据。
- Next: 为所有已识别 drift 页面补齐旧路径到新路径、入链、递归导航及 change-map required_docs 的完整迁移 delta。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
