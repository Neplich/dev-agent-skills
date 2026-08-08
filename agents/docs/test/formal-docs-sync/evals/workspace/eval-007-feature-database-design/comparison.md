# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-007-feature-database-design`.
- Fixture SHA-256: `de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81`
- Prompt SHA-256: `97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `289a3b63a3dcdcdc4cc6c4b994a40567f085f301732b94d5ab13b0e67247a316`
- Eval definition SHA-256: `dd84eeaf9ea9452e584f740ec00a1edde6c8e5bfae2ef83da4e9e416f2e769fe`
- Metadata SHA-256: `23140221449282820c7da53fcdbe46ce5ee1169aff6e90986ef0dbd09c5f9120`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_only_database_design_contracts` | NOT_EXERCISED | The locked evidence cannot prove the required read order or module-loading restriction. |
| `passes_design_closeout_gate` | NOT_EXERCISED | The required runtime-only per-page closeout matrix is not present in the locked evidence; the claimed gate pass cannot independently prove this hidden process requirement. |
| `creates_database_schema_domain_tree` | PASS | The delivered snapshot contains the database root, primary schema, workspace-access domain, relationship page, and three entity pages with hierarchical links. |
| `refreshes_confirmed_stable_path` | PASS | The stable database path is preserved, marked unverified, and refreshed with current uniqueness, roles, physical FK, and logical-reference facts. |
| `documents_current_entity_facts` | PASS | Entity snapshots accurately reflect schema, repository/service behavior, indexes, constraints, ownership, and lifecycle evidence. |
| `links_relationships_bidirectionally` | PASS | The relationship page links all three entity pages; each entity page links its domain, relationship overview, related entities, API authority, and database authority. |
| `distinguishes_physical_and_logical_relations` | PASS | The relationship Mermaid and prose distinguish cascading physical workspace FKs from the service-validated logical user reference. |
| `creates_domain_component_flow_tree` | PASS | The Design snapshot contains root and domain indexes, InvitationService, MembershipRepository, AuditWriter, invitation-acceptance, and authorization-boundary pages. |
| `keeps_reciprocal_and_authority_links` | PASS | Components link the acceptance flow, the flow links all three components, and Design pages link API/database authority pages without duplicating complete contracts. |
| `keeps_cross_domain_authority_unique` | PASS | The acceptance flow is explicitly authoritative under workspace-access; audit-log pages link to it without duplicating its正文. |
| `updates_atomic_map_and_unverified_pages` | PASS | The locked change-map preserves existing entries and stable paths, adds the database/design closure for each relevant code glob, and marks delivered pages unverified; candidate evidence reports a zero-missing-doc readback. |
| `runs_host_checks_and_handoffs_audit` | NOT_EXERCISED | The candidate reports all three npm checks passed, but the required docs-audit handoff is explicitly blocked by missing target release-version confirmation, so the later handoff step is not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=1a1411f380f4acb5acced4dbe035c4ad46b56de30424fe5f47a3e9db761c7d7e; snapshot_sha256=812dc34cf26e3eb716477d270282b502d87d8fdf64d73a5a830e6d4486334606
- Behavior: Delivered the requested database and design documentation trees with accurate current facts, reciprocal links, authority boundaries, and change-map updates; host checks were reported passed, while the final audit handoff remains blocked.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=9cb4f30def70e50fe7c1153eeeb55923522afd95565fde2fc5439072960d21a5; snapshot_sha256=d6445ec3bad367ceb6f27f94dfce6232d444a6541b8d5fdddc3a1184f448511f
- Behavior: Delivered a similar but less complete documentation tree, omitted the public build report, and reported pytest unavailable.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the target release version and complete the docs-audit handoff.
- Next: Capture runtime closeout-matrix and read-order evidence if those process assertions must be evaluated.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-007-feature-database-design`.
- Fixture SHA-256: `de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81`
- Prompt SHA-256: `97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dd84eeaf9ea9452e584f740ec00a1edde6c8e5bfae2ef83da4e9e416f2e769fe`
- Metadata SHA-256: `23140221449282820c7da53fcdbe46ce5ee1169aff6e90986ef0dbd09c5f9120`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_only_database_design_contracts` | NOT_EXERCISED | 该断言要求隐藏的读取顺序与加载范围；with_skill 锁定输出仅列出证据来源，无法证明实际读取顺序。 |
| `passes_design_closeout_gate` | NOT_EXERCISED | with_skill 在写入前识别范围冲突并暂停、请求确认；尚未进入可验证的 closeout 固化或写入阶段。 |
| `creates_database_schema_domain_tree` | NOT_EXERCISED | 候选尚未获得确认并执行写入，因此数据库子树未在 with_skill 交付中产生。 |
| `refreshes_confirmed_stable_path` | NOT_EXERCISED | with_skill 的 proposed batch 明确保留稳定路径，但尚未实际刷新或重定向文件。 |
| `documents_current_entity_facts` | NOT_EXERCISED | 实体页面尚未在 with_skill 交付中生成。 |
| `links_relationships_bidirectionally` | NOT_EXERCISED | 关系页与实体页尚未在 with_skill 交付中生成，链接无法验证。 |
| `distinguishes_physical_and_logical_relations` | NOT_EXERCISED | with_skill 提议数据库闭包，但尚未写入包含物理外键与逻辑引用区分的页面。 |
| `creates_domain_component_flow_tree` | NOT_EXERCISED | 设计范围已识别并列入 proposed batch，但尚未因待确认冲突而执行写入。 |
| `keeps_reciprocal_and_authority_links` | NOT_EXERCISED | 组件、流程与权威链接尚未在 with_skill 交付中产生。 |
| `keeps_cross_domain_authority_unique` | NOT_EXERCISED | with_skill 提议了跨域流程权威页与 audit-log 引用关系，但尚未写入或验证。 |
| `updates_atomic_map_and_unverified_pages` | NOT_EXERCISED | with_skill 明确提出完整 change-map 闭包与稳定路径保留，但尚未执行原子更新。 |
| `runs_host_checks_and_handoffs_audit` | NOT_EXERCISED | with_skill 明确记录 host checks 和 audit handoff 尚未执行；这些步骤依赖用户确认后的继续执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=e3fe7ce9f5cf0d08667ffa474c3fa99af6ebb8a1906cd1c23e8760427b074a4d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别 candidate-scope-confirmation.md 与 design-scope-confirmation.md 的范围冲突，在写入前暂停并请求用户确认；未进行未经确认的文件变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=b545f1d786c0845b83668beb5c670fd2e1bdb779bb334504bbea49c4bbd7894f; snapshot_sha256=ffc113d7625d6c7b8dca0b03dc7e0bd500f2bab2f6b9c6d935b25daff79e1868
- Behavior: 直接声称已完成文档同步并报告部分检查通过；对所需范围、原子更新和运行期门禁的完整证据不足。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 获得确认后继续执行文档同步、宿主检查与 docs-agent:docs-audit handoff。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `069691c0cf641c0197bfdbacac2d64c88a425f981a4a1790a532e131615e041e` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-007-feature-database-design`.
- Fixture SHA-256: `069691c0cf641c0197bfdbacac2d64c88a425f981a4a1790a532e131615e041e`
- Prompt SHA-256: `97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dd84eeaf9ea9452e584f740ec00a1edde6c8e5bfae2ef83da4e9e416f2e769fe`
- Metadata SHA-256: `a0174e62fc5ee1741a54f96a3dfafd22a8b0c46a51aa767a1e30458f73276359`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_only_database_design_contracts` | PASS | With-skill outputs modify only database/design documentation and mappings; API is referenced as an authority link and no API, ops, or product pages are changed. |
| `passes_design_closeout_gate` | FAIL | No runtime-only sync-report.md, per-page closeout matrix, generation time, or pre-write changed-path state is present. |
| `creates_database_schema_domain_tree` | PASS | Snapshot contains database/index.md, primary/index.md, the workspace-access domain index, relationships.md, and all three entity pages. |
| `refreshes_confirmed_stable_path` | PASS | database/workspace-access.md is retained, stale facts are replaced with current facts, last_verified_version is unverified, and the stable mapping is preserved. |
| `documents_current_entity_facts` | PASS | Entity pages record current fields, constraints, indexes, ownership/lifecycle behavior, membership uniqueness and roles, invitation token uniqueness, and expires_at. |
| `links_relationships_bidirectionally` | PASS | relationships.md links all three entity pages; each entity page links the domain index, relationships, related tables, and the workspace-access API authority. |
| `distinguishes_physical_and_logical_relations` | PASS | Relationship Mermaid and prose identify both workspace_id references as CASCADE physical FKs and user_id as a service-validated logical reference without a physical FK. |
| `creates_domain_component_flow_tree` | PASS | Snapshot contains the Design root, Workspace Access and Audit Log indexes, three component pages, invitation-acceptance flow, authorization-boundary page, and the legacy compatibility page. |
| `keeps_reciprocal_and_authority_links` | PASS | All three components link the acceptance flow, the flow links all three components, and Design pages link API/database authority pages without duplicating their contracts. |
| `keeps_cross_domain_authority_unique` | PASS | The acceptance flow is under Workspace Access; Audit Log pages link to it and explicitly state they do not duplicate the flow. |
| `updates_atomic_map_and_unverified_pages` | FAIL | The final snapshot has the required pages and unverified metadata, but there is no evidence of atomic write sequencing or read-back/stable-sort verification; the page-specific mappings are also broad full-closure mappings rather than demonstrated per-glob affected sets. |
| `runs_host_checks_and_handoffs_audit` | FAIL | Evidence reports frontmatter/version checks and unit tests, but full test:docs affected checking was blocked; no successful npm run test:docs, public/internal builds, complete visibility/link verification, or docs-agent:docs-audit handoff is shown. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=069691c0cf641c0197bfdbacac2d64c88a425f981a4a1790a532e131615e041e; output_sha256=34fb8daf0b89c7003de3a8cd801dd2048f7ba5d10313d5b2c032818cefe5519c; snapshot_sha256=03ea858b341e667a9fe0426d6493eeef572209e066b4e042ac7095182b8b0b7b
- Behavior: With-skill produced the requested database/design hierarchy and current facts with reciprocal authority links, but lacked required closeout timing evidence and complete host-check/handoff evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=069691c0cf641c0197bfdbacac2d64c88a425f981a4a1790a532e131615e041e; output_sha256=84908942a683edfdc2461787838844e9ba315694087582159cdc9bab86619fac; snapshot_sha256=b2a213d1bcc8b3fb980d22dedddbeafbff5142d06a0618543b061686801eac64
- Behavior: Fresh baseline created much of the database/design tree and refreshed facts, but lacked the complete mapping closure and reported incomplete checks.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- passes_design_closeout_gate failed because sync-report.md and per-page pre-write closeout evidence are absent.
- updates_atomic_map_and_unverified_pages failed because atomic sequencing/read-back evidence is absent and mapping precision is not demonstrated.
- runs_host_checks_and_handoffs_audit failed because required npm checks/builds, visibility/link verification, and handoff are not evidenced.
- Next: Create and preserve the required runtime-only sync-report.md before writes.
- Next: Run all required docs checks/builds and complete the docs-audit handoff with the full affected set.

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

# Eval Comparison: Feature Database + Design Sync

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Mode / types: feature delivery / Database + Design

## Test Set / Fixture Version

- Fixture version: `issue-164 Database information architecture + issue-160 recursive Design information architecture`
- Evidence: Approved PRD, Confirmed TRD, closed implementation plan, actual
  diff, 11 named executable evidence rows / 12 pytest cases, schema, guarded
  invitation creation and consumption, authenticated-user membership
  persistence, real audit writer, stable-path seed, unrelated manual mapping,
  and arbitrary-depth sidebar infrastructure.
- Fresh paired run:
  `tmp/eval-runs/pr-165-multilevel-final-clean-20260723-170550/eval-007/`
- Generation method: both generators received the same prompt and current
  pristine fixture. Only with-skill received the Docs Agent, common contract,
  and Database/Design modules. Neither generator received assertions, this
  comparison, an earlier lane, or the other lane's output. The first
  with-skill attempt stalled on an empty nested-agent receiver before formal
  writes; the scored lane was rebuilt from pristine input with the same core
  prompt and a wrapper clarification that it was already the required fresh
  document-writing subagent.
- Judge method: a new independent `codex exec` judge first read the current 12
  assertions after generation, inspected both actual workspaces, and reran
  fixture pytest, 76 docs tests, both builds, recursive navigation, link, and
  per-glob closure checks.
- Actual validation date: `2026-07-23`

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `loads_only_database_design_contracts` | FAIL | FAIL | 产物没有记录 standards/template/module 的实际读取轨迹；仅凭最终文档无法证明未加载 API、ops、product 规则。 |
| `passes_design_closeout_gate` | FAIL | FAIL | 两条 lane 均不存在 runtime-only `sync-report.md`，没有逐页 closeout matrix、生成时间或写前 changed-path 证据。 |
| `creates_database_schema_domain_tree` | PASS | PASS | 两条 lane 均存在并链接 `database/index.md`、Primary、Workspace Access 数据域、relationships 和三个实体页。 |
| `refreshes_confirmed_stable_path` | FAIL | FAIL | 两条 lane 均保留稳定路径并刷新正文，但 with_skill 页面仍为 `last_verified_version: v0.9.0`，without_skill 为 `v1.0.1`，均未标记 `unverified`。 |
| `documents_current_entity_facts` | PASS | PASS | 两条 lane 的实体页记录了 `(workspace_id, user_id)` 唯一约束、owner/editor/viewer、invitation token 唯一约束和 `expires_at`；对应 `schema.sql` 与测试一致。 |
| `links_relationships_bidirectionally` | PASS | PASS | 两条 lane 的 `relationships.md` Mermaid 指向三个实体页；实体页均反向链接数据域、关系页、相关表和 `api/workspace-access.md`。 |
| `distinguishes_physical_and_logical_relations` | PASS | PASS | 两条 lane 均明确 workspace 外键为 `ON DELETE CASCADE`，`workspace_memberships.user_id` 为 service 校验的逻辑引用且无物理 FK。 |
| `creates_domain_component_flow_tree` | PASS | PASS | 两条 lane 均生成 Design 根、Workspace Access、Audit Log、Invitation Service、Membership Repository、AuditWriter、invitation-acceptance 和 authorization-boundary 页面，并保留旧 flat 兼容入口。 |
| `keeps_reciprocal_and_authority_links` | PASS | PASS | 两条 lane 的三个组件页链接 invitation-acceptance，流程页反向链接三个组件；Design 页面链接 API 与数据库权威页，未复制完整 contract 表。 |
| `keeps_cross_domain_authority_unique` | PASS | PASS | 两条 lane 均将 invitation-acceptance 保留在 Workspace Access 下；Audit Log 仅通过链接引用流程，没有复制流程正文。 |
| `updates_atomic_map_and_unverified_pages` | FAIL | FAIL | with_skill 的稳定数据库页仍是 `v0.9.0`；without_skill 多个 Design/Database 页仍是 `v1.0.1`，且其 `src/audit/**` 映射未包含完整 Database 子树和互链闭包。 |
| `runs_host_checks_and_handoffs_audit` | FAIL | FAIL | with_skill 明确记录 `npm run test:docs` 被环境阻断且尚未 handoff；without_skill 记录自动化测试未成功，且没有三项宿主检查通过证据或 `docs-agent:docs-audit` handoff。 |

未满足断言（with/without 任一 FAIL）：``loads_only_database_design_contracts``、``passes_design_closeout_gate``、``refreshes_confirmed_stable_path``、``updates_atomic_map_and_unverified_pages``、``runs_host_checks_and_handoffs_audit``



## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `loads_only_database_design_contracts`: with-skill PASS；without-skill FAIL。
  Only with-skill loaded the standards entry, granularity, change map, and
  Database/Design modules.
- `passes_design_closeout_gate`: with-skill PASS；without-skill FAIL。
  With-skill captured the nine-page × seven-item matrix before any formal-page
  or map write; the baseline only produced a post-write summary.
- `creates_database_schema_domain_tree`: both PASS. Both generated the full
  Database root/schema/data-domain/relationship/entity tree.
- `refreshes_confirmed_stable_path`: with-skill PASS；without-skill FAIL。
  Both refreshed the stable page, but only with-skill retained it inside the
  broad glob's complete 19-page closure.
- `documents_current_entity_facts`: both PASS. Entity fields, constraints,
  owners, indexes, and lifecycles match schema and code.
- `links_relationships_bidirectionally`: with-skill PASS；without-skill FAIL。
  Only with-skill gave every entity the complete domain/relationship/related
  entity/feature API backlink set.
- `distinguishes_physical_and_logical_relations`: both PASS. Both distinguish
  CASCADE workspace foreign keys from the service-validated logical user
  reference.
- `creates_domain_component_flow_tree`: both PASS. Both generated the Design
  root, two domains, three components, flow, boundary, and compatibility page.
- `keeps_reciprocal_and_authority_links`: both PASS. Component/flow links are
  reciprocal and use stable API/Database authorities.
- `keeps_cross_domain_authority_unique`: both PASS. The shared flow has one
  authority page and Audit Log links to it.
- `updates_atomic_map_and_unverified_pages`: with-skill PASS；without-skill
  FAIL。Only with-skill gives all six participating globs the independently
  complete, stable 19-page closure.
- `runs_host_checks_and_handoffs_audit`: with-skill PASS；without-skill FAIL。
  Both passed host checks and recursive visibility, but only with-skill handed
  the complete set to `docs-agent:docs-audit` and blocked on the missing target
  version.

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Loaded the exact common/Database/Design contracts and no unrelated type
  module.
- Preserved pre-write page-level closeout evidence, refreshed the stable
  Database authority, and generated complete nested Database/Design trees.
- Kept entity/relationship and component/flow links reciprocal, with direct
  links to stable API/Database authority pages.
- Applied identical 19-page closures to all six participating broad/exact
  globs and preserved the unrelated manual entry.
- Passed recursive internal navigation at maximum depth four while public
  navigation correctly excluded all internal Database/Design pages.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Source: a new pristine fixture copy with the same prompt. It did not read or
  apply the target skill, Agent README, assertions, this comparison, with-skill
  output, or a historical baseline.
- Result: 6/12 PARTIAL. It generated the main page trees and current facts, but
  failed contract loading, pre-write closeout, stable-path subtree mapping,
  entity reverse links, per-glob atomic closure, and the `docs-agent:docs-audit` gate.
- Skill-specific uplift: +6 assertions, or +50.0 percentage points.

## Required Test Reproduction

- The judge ran
  `PYTHONDONTWRITEBYTECODE=1 uv run --with pytest python -m pytest tests/test_workspace_access.py -q -p no:cacheprovider`
  in both lanes; each returned `12 passed`.
- It reran `npm run test:docs`, `npm run build:public`, and
  `npm run build:internal`; each lane passed 76/76 docs tests and both builds.
- Internal navigation contained 16 Database/Design routes at maximum depth
  four; public contained zero internal routes. Independent parsing found zero
  broken links.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- With-skill assertion failures: none.
- Without-skill assertion failures: `loads_only_database_design_contracts`,
  `passes_design_closeout_gate`, `refreshes_confirmed_stable_path`,
  `links_relationships_bidirectionally`,
  `updates_atomic_map_and_unverified_pages`, and
  `runs_host_checks_and_handoffs_audit`.
- Existing VitePress directory-asset and chunk-size warnings were
  non-blocking; both builds and independent link resolution succeeded.
- The first with-skill infrastructure attempt was not scored: it never reached
  a receiver or formal-page write. Its diagnostic lane remains runtime-only;
  the independent judge verified the final pristine retry and recorded this
  caveat separately from assertion results.

## Targeted Regression Verification (2026-08-05)

- Trigger: issue #225 added a flat-hierarchy drift check whose in-batch tier
  treats a single evidenced root-level page as drift. This fixture keeps
  `docs/site/database/workspace-access.md` at the type root by explicit
  confirmation while the same batch writes `database/primary/`, so the new rule
  could have demanded a migration proposal for a path whose non-migration was
  already confirmed.
- Method: one fresh `codex exec` with-skill lane on an isolated copy of this
  fixture, using the existing eval prompt.
- Result: no spurious proposal. The lane refreshed the stable page in place,
  reported `Hierarchy drift` as the confirmed stable page plus the confirmed
  Design compatibility entry with no unhandled root-level page, and left the
  stable path unmoved. Host checks ran after `npm ci`.
- Scope: this is a targeted regression check for one risk, not a revalidation.
  No new `without_skill` baseline was generated and the twelve assertions were
  not rejudged, so `Latest Result` above is unchanged and this section does not
  restate it.

## Next Steps

- Keep arbitrary-depth sidebar generation and its deterministic test shared by
  bootstrap and both hierarchy fixtures.
- Keep the page-level closeout, stable authority, entity backlink, and per-glob
  closure checks together as the Design/Database regression unit.
- Keep the shallow current Design fixture structure; recursive support does not
  require inventing deeper subsystem levels without confirmed ownership
  evidence.

## Runtime Artifact Policy

- Both lanes, dependencies, generated sites, generator events, judge events,
  final outputs, verdict, and diagnostics remain under `tmp/eval-runs/` and are
  not submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, diagnostics, generated-site, cache, or run-status
  artifact is committed.
