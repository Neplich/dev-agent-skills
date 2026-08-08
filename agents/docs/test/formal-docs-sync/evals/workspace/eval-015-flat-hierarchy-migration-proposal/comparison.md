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
- Fixture SHA-256: `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `162b3544cbde876f526df1805303ea3ab78e34b2ebde819bbdbfe83bc8251b8c`
- Eval definition SHA-256: `de76a086939d1591df845f72fbdb70d76c350be98629e84e5fc28aead6c5474b`
- Metadata SHA-256: `1745a4b411c4974d9b158bc811fac50658345383bc93cab2e1df286dcb1629d0`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | FAIL | with_skill 仅指出 research-conversations.md 的漂移，未点名 graph-search.md 与其同属缺失的“知识发现与应用”域节点。 |
| `proposes_migration_before_write` | FAIL | with_skill 提供了会话消息目标子树和部分 change-map/导航说明，但未完整给出所有旧路径映射、三项决策选项及明确等待确认的同批迁移提案。 |
| `does_not_deepen_flat_layout` | PASS | git_evidence 显示无变更；候选输出明确写明未修改 site files，且未宣称执行写入后检查。 |
| `reports_out_of_batch_drift_read_only` | FAIL | with_skill 未列出知识建设与维护、平台治理与运行两组批次外 drift 的具体页面清单及建议目标节点，仅笼统排除其他 API。 |
| `loads_only_api_contract` | FAIL | 候选输出未显式列出已加载的 API 类型模块与 host API 模板；虽然给出层级漂移说明并排除其他文档类型，但不足以满足显式加载模块报告。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=462e3cb55aa4551c3ed966e949b49ad3ff131ec31ac481e65e551562d7b2f835; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了部分层级漂移并保持工作区零写入，但迁移提案、批次外 drift 报告和加载模块报告不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=d8afa4c355ad38fafb7c51f0469c3dd8d3d1fc7ffba8e7cf0ddba727104b9564; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出扁平路径下新增叶子页和根导航链接，未识别层级漂移，也未提出迁移或批次外只读报告。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- detects_flat_hierarchy_drift
- proposes_migration_before_write
- reports_out_of_batch_drift_read_only
- loads_only_api_contract
- Next: 补齐 research-conversations.md 与 graph-search.md 到同一缺失域节点的 drift 证据和结论。
- Next: 在写入前提供完整迁移树、旧新路径映射、入链/递归导航与 change-map delta，并给出三项决策选项后等待确认。
- Next: 列出两组批次外 drift 的具体页面、目标节点及明确的范围外声明。
- Next: 显式报告仅加载的 API 类型模块、host API 模板和 Hierarchy drift 结论。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Fixture SHA-256: `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `162b3544cbde876f526df1805303ea3ab78e34b2ebde819bbdbfe83bc8251b8c`
- Eval definition SHA-256: `de76a086939d1591df845f72fbdb70d76c350be98629e84e5fc28aead6c5474b`
- Metadata SHA-256: `1745a4b411c4974d9b158bc811fac50658345383bc93cab2e1df286dcb1629d0`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | PASS | PASS：明确指出 `research-conversations.md` 与 `graph-search.md` 位于 API 根目录，并以 feature catalog 的嵌套层级作为 drift 依据。 |
| `proposes_migration_before_write` | FAIL | FAIL：虽提出新页面目标子树，但未提供既有页面的迁移子树、旧新路径映射、入链/递归导航 delta、`required_docs` delta，也未给出三个决策选项。 |
| `does_not_deepen_flat_layout` | PASS | PASS：候选范围明确不迁移既有 flat 页面，提出新增嵌套子树；锁定 git evidence 显示零写入，且输出说明 host checks 尚未运行。 |
| `reports_out_of_batch_drift_read_only` | FAIL | FAIL：只报告了 `research-conversations.md` 和 `graph-search.md`，未列出知识建设与维护、平台治理与运行两组批次外 drift 的页面清单及建议目标节点。 |
| `loads_only_api_contract` | FAIL | FAIL：输出未显式列出仅加载的 API 类型模块与 host API 模板，也未提供名为或等价于 Hierarchy drift 结论的显式字段；仅列出若干证据绑定。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=3b867ba212e072cf8e8ddfeac59c2c7182d7eafd414f2cec44031c4ede6ef8cf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了知识发现域的 flat hierarchy drift，提出嵌套 API 子树并保持零写入、等待确认；但迁移提案、批次外 drift 报告和模块加载报告不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=ac7f65a106db1b28efa0213f5f80ca114d219c4681e21c569f69236db3d1ff6e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出 flat API 下新增页面并更新根索引和 change-map，未识别层级 drift，且未提供迁移或完整范围治理。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未在一次写入前确认中完整提出迁移映射、导航与 change-map delta 及三个决策选项。
- with_skill 未完整报告两组批次外 drift。
- with_skill 未显式报告限定加载模块和 Hierarchy drift 结论字段。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Fixture SHA-256: `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `162b3544cbde876f526df1805303ea3ab78e34b2ebde819bbdbfe83bc8251b8c`
- Eval definition SHA-256: `de76a086939d1591df845f72fbdb70d76c350be98629e84e5fc28aead6c5474b`
- Metadata SHA-256: `1745a4b411c4974d9b158bc811fac50658345383bc93cab2e1df286dcb1629d0`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | FAIL | FAIL：虽声明 flat 页面与 feature catalog 层级不一致，但未点名 research-conversations.md 与 graph-search.md，也未说明二者同属缺失的知识发现与应用域节点。 |
| `proposes_migration_before_write` | FAIL | FAIL：给出了新页面嵌套树和 change-map 建议，但没有旧路径到新路径映射、递归导航与 required_docs delta，也没有同时提供迁移、仅本批次、全部推迟三个选项。 |
| `does_not_deepen_flat_layout` | PASS | PASS：明确本轮不写入、不迁移既有 flat 页面，新页面位于嵌套目标树；git evidence 显示工作树、索引和提交均未变化，并声明 host checks 尚未运行。 |
| `reports_out_of_batch_drift_read_only` | FAIL | FAIL：仅笼统称既有 flat 页面为 out-of-batch drift，未按知识建设与维护、平台治理与运行两组列出页面清单及建议目标节点。 |
| `loads_only_api_contract` | NOT_EXERCISED | 无法由锁定证据证明实际模块加载/读取顺序；该隐藏过程断言未充分可观测。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=23388a5acba0f1a43f989d3f02cfc4189f8220634d23ccab6d4ad903ea055c46; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到知识发现层级与现有 flat API 页面不一致，提出嵌套会话消息页面树并等待维护者确认，且未产生文件或 git 变更；但遗漏了具体 drift 页面、完整迁移方案和批次外 drift 清单。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=05d2d3559c79a9df6116afeb5ecb28b1f5a321619639ab4603d354eec8f1c5f0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出直接在 docs/site/api/ 下新增一级叶子页并更新 API 索引及 change-map，未识别 flat hierarchy drift，也未进行写入。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未点名并完整解释 research-conversations.md 与 graph-search.md 的共同层级 drift。
- with_skill 未提供完整的一次性迁移提案及三个确认选项。
- with_skill 未按要求报告两组批次外 drift 的页面清单和目标节点。
- Next: 点名 research-conversations.md 和 graph-search.md，说明其基于 feature catalog、feature_path、route prefix/tag、related_code 或 owner 的共同节点判定。
- Next: 在确认前补充迁移目标树、旧新路径映射、导航和 required_docs delta，并提供三个确认选项。
- Next: 列出知识建设与维护、平台治理与运行两组批次外页面及建议目标节点。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Fixture SHA-256: `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `162b3544cbde876f526df1805303ea3ab78e34b2ebde819bbdbfe83bc8251b8c`
- Eval definition SHA-256: `de76a086939d1591df845f72fbdb70d76c350be98629e84e5fc28aead6c5474b`
- Metadata SHA-256: `1745a4b411c4974d9b158bc811fac50658345383bc93cab2e1df286dcb1629d0`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | FAIL | with_skill identifies a positive flat drift generally, but does not name research-conversations.md and graph-search.md or establish that both belong to the same missing node before proposing scope. |
| `proposes_migration_before_write` | FAIL | The output gives a target subtree and three semantically equivalent decision choices, but omits old-to-new path mappings, inbound/recursive navigation deltas, and an explicit change-map required_docs delta. |
| `does_not_deepen_flat_layout` | PASS | It proposes the new page under the knowledge-discovery/conversations subtree, explicitly retains existing flat pages without moving them, and states the proposal is zero-write with checks and handoff blocked pending confirmation. |
| `reports_out_of_batch_drift_read_only` | FAIL | The output does not provide read-only observation reports for the knowledge-building/maintenance and platform-governance/operations drift groups, their page lists, or target nodes. |
| `loads_only_api_contract` | FAIL | The output lists API-related evidence and a drift conclusion, but does not explicitly report the loaded API modules and host template or prove that database, design, ops, and product modules were not read/applied. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=578253835d2f85cc5d60075260f0c61343de6422c9cfd96e736cfe94c4673de5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly preserves zero-write behavior and proposes the new page in a hierarchical subtree, but misses several required migration, drift-reporting, and module-reporting details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=8e75f4fa61d83e6224655536b1250af2a99d7bd0276037693a362352be025775; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline proposes a flat API page and top-level navigation only, without hierarchy drift analysis or migration planning.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill proposal omits required named drift evidence and the two out-of-batch drift reports.
- The migration proposal lacks required path mappings, navigation deltas, and change-map required_docs deltas.
- The loaded-module/host-template report is incomplete.
- Next: Add named drift evidence for research-conversations.md and graph-search.md, including their shared target node and catalog/route/tag/owner basis.
- Next: Provide the complete migration mapping, navigation and recursive-link deltas, change-map required_docs delta, exclusions with reasons, and all three confirmation options.
- Next: Add the two out-of-batch read-only drift reports and an explicit loaded-module/Hierarchy drift report.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Fixture SHA-256: `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `de76a086939d1591df845f72fbdb70d76c350be98629e84e5fc28aead6c5474b`
- Metadata SHA-256: `1745a4b411c4974d9b158bc811fac50658345383bc93cab2e1df286dcb1629d0`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | FAIL | With_skill identifies a flat layout and names research-conversations.md, but does not name graph-search.md as part of the same missing knowledge-discovery/application node. |
| `proposes_migration_before_write` | FAIL | With_skill provides a target tree, change-map delta, exclusions, and confirmation options, but omits the required complete old-to-new path mappings, inbound/recursive navigation deltas, and exclusion reasons. |
| `does_not_deepen_flat_layout` | PASS | The with_skill delivery snapshot is empty and git evidence shows no changes. The output states zero writes, keeps existing pages unmoved before confirmation, places the proposed new page below nested indexes, and does not run site checks. |
| `reports_out_of_batch_drift_read_only` | FAIL | With_skill excludes broad categories but does not report the two specified out-of-batch drift groups with page lists and suggested target nodes. |
| `loads_only_api_contract` | FAIL | The output does not explicitly report the loaded API modules and host API template or provide an explicit Hierarchy drift conclusion field; the locked evidence cannot establish the hidden read order. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=54be7a101eb70904d82a224d0b3d9287300b8ffbad259c799333254537064bdd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: With_skill correctly gates on maintainer confirmation and preserves a zero-write state, but its proposal is incomplete on flat-drift coverage, migration deltas, out-of-batch drift reporting, and explicit API-only loading/report fields.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=8686a936d83c624bd5f93ef22fe83f6c04240f75b5f54fc9c466d2179c68db9d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline proposes a flat conversation-messages page and index link, notices only a possible change-map issue, and omits the required hierarchy-drift and migration analysis.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- detects_flat_hierarchy_drift: graph-search.md is not identified alongside research-conversations.md.
- proposes_migration_before_write: required complete mappings, navigation deltas, and exclusion reasons are missing.
- reports_out_of_batch_drift_read_only: required page lists and target nodes for both out-of-batch drift groups are missing.
- loads_only_api_contract: required explicit loaded-module/template and Hierarchy drift fields are missing.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Fixture SHA-256: `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a612d50c32b84c65fad3cad08aad2d416a3a33647abfa1462784c1e58022424b`
- Skill overlay SHA-256: `e55ecf59b3cd8d90a2ed4cf555bed2ad2fc2131494e0914246a868317b68f4e8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `de76a086939d1591df845f72fbdb70d76c350be98629e84e5fc28aead6c5474b`
- Metadata SHA-256: `f008330cf4c09bf2d8f5e755019b196220dae437f59e25ab5a6b76314ba70a05`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | FAIL | With_skill 仅指出 research-conversations.md 的扁平漂移，未点名 graph-search.md，也未说明两者同属同一缺失的知识发现与应用域节点。 |
| `proposes_migration_before_write` | FAIL | With_skill 提供了目标页面树和部分映射，但未给出旧路径到新路径映射、入链与递归导航 delta、明确的 required_docs delta，也未提供三个决策选项。 |
| `does_not_deepen_flat_layout` | PASS | 候选输出明确声明待确认、当前零写入；新页面位于目标层级而非 docs/site/api/ 一级；git evidence 显示无变更。 |
| `reports_out_of_batch_drift_read_only` | FAIL | With_skill 仅将 Database、Design、Ops、Product 等作为排除项，未分别列出知识建设与维护、平台治理与运行两组批次外 drift 的页面清单及建议目标节点。 |
| `loads_only_api_contract` | NOT_EXERCISED | 输出报告了已加载模块 api 和层级漂移结论，但锁定 raw evidence 无法证明 API 模板的实际加载、未加载其他类型模块或具体读取顺序。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=1a353faaa989e85d1e9ac3b31b4c16907c55aeafbf5b492e5b9da1c682430f92; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出嵌套 API 子树和零写入候选范围，识别部分扁平漂移并等待维护者确认，但缺少完整迁移 delta、三选项确认和批次外 drift 清单。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=0f9380883902e818858d65fbad47cf88b853cc89fcf125dda76779b3b5134572; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出扁平路径新增页面并更新 API 索引，未识别层级漂移，也未提供迁移提案或批次外 drift 报告。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未识别 research-conversations.md 与 graph-search.md 共同缺失的知识域节点。
- with_skill 未提供完整迁移提案及三个决策选项。
- with_skill 未报告两组批次外 drift 的页面清单和建议目标节点。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-015-flat-hierarchy-migration-proposal`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e820b6c4381f2b584f4fb75e118822cab822720708679f6856aff845dce75a20` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-015-flat-hierarchy-migration-proposal`.
- Fixture SHA-256: `e820b6c4381f2b584f4fb75e118822cab822720708679f6856aff845dce75a20`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `52db6badcefada59a1d42e81de2581f06256f43c060b7699c281ab21bfb40949`
- Skill overlay SHA-256: `f896903fa1a8ae6886eb0b6365065625a2e60f6809acd0af6c7c8dc8f8f2bd40`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `de76a086939d1591df845f72fbdb70d76c350be98629e84e5fc28aead6c5474b`
- Metadata SHA-256: `f008330cf4c09bf2d8f5e755019b196220dae437f59e25ab5a6b76314ba70a05`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | PASS | 在候选范围前明确指出 research-conversations.md 与 graph-search.md 的扁平层级漂移，并以 feature catalog 和知识发现归属为依据。 |
| `proposes_migration_before_write` | FAIL | 虽给出目标树和三个确认选项，但未给出现有路径到新路径的完整映射、入链与递归导航 delta、change-map required_docs delta、排除项及理由。 |
| `does_not_deepen_flat_layout` | PASS | 提出新增页面位于 knowledge-discovery/conversations/messages.md，明确确认迁移前不移动既有页面或重构导航；raw git evidence 显示工作区零写入。 |
| `reports_out_of_batch_drift_read_only` | FAIL | 未报告知识建设与维护、平台治理与运行两组批次外 drift 的页面清单、建议目标节点及不纳入本次范围的说明。 |
| `loads_only_api_contract` | NOT_EXERCISED | raw evidence 无法证明实际读取顺序或是否读取了非 API 类型模块；候选输出也未显式列出已加载的 API 模块与 host API 模板。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=e820b6c4381f2b584f4fb75e118822cab822720708679f6856aff845dce75a20; output_sha256=63342c98fce26042c2457f2925bb5af0baf9c2a35c4cb35b8ef6299d4e2d0132; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别知识发现层级 drift，提出嵌套目标树、change-map 草案和确认选项，并保持工作区零写入；但遗漏完整迁移 delta 与批次外 drift 报告。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=e820b6c4381f2b584f4fb75e118822cab822720708679f6856aff845dce75a20; output_sha256=9557234b599a773c76ee7de626bb081a3385c0a64618f8865b7c2c7365af31cb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出扁平 API 一级新增页面和首页链接，未识别层级 drift、迁移提案或批次外 drift。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未提供完整的一次性迁移提案所要求的路径映射、导航 delta、required_docs delta、排除项理由。
- with_skill 未报告两组批次外 drift。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-015-flat-hierarchy-migration-proposal`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e820b6c4381f2b584f4fb75e118822cab822720708679f6856aff845dce75a20` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-015-flat-hierarchy-migration-proposal`.
- Fixture SHA-256: `e820b6c4381f2b584f4fb75e118822cab822720708679f6856aff845dce75a20`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1e290565a84b926a128928ccdd91365a2235adff18f999307c0a3553f0b41f34`
- Skill overlay SHA-256: `0c6a49eed1db242a95632eb0d142c1760f60ffc995c96026908ec8c0e6bd8d63`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `de76a086939d1591df845f72fbdb70d76c350be98629e84e5fc28aead6c5474b`
- Metadata SHA-256: `f008330cf4c09bf2d8f5e755019b196220dae437f59e25ab5a6b76314ba70a05`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | FAIL | With_skill proposes keeping the flat API layout and does not identify research-conversations.md and graph-search.md as a shared hierarchy drift or cite the required catalog/path/route evidence. |
| `proposes_migration_before_write` | FAIL | With_skill provides no migration proposal, target index subtrees, old-to-new mappings, navigation or change-map deltas, exclusions with reasons, or the three required decision options. |
| `does_not_deepen_flat_layout` | FAIL | With_skill proposes adding conversation-messages.md directly under docs/site/api/, which deepens neither hierarchy nor existing pages but does append the new page at the forbidden flat level before migration confirmation. |
| `reports_out_of_batch_drift_read_only` | FAIL | With_skill does not report the two out-of-batch drift groups, their page lists, suggested target nodes, or their exclusion from the current confirmation scope. |
| `loads_only_api_contract` | FAIL | With_skill does not explicitly report loaded modules or a Hierarchy drift conclusion, and its output does not establish that database, design, ops, and product type modules were not read or applied. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=e820b6c4381f2b584f4fb75e118822cab822720708679f6856aff845dce75a20; output_sha256=a17df66d58ff0a6c8bd690ec41aafaa6d4d4e8bee44b7f0c03bfaf5363631ee5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Recognizes the formal-docs workflow and defers edits pending confirmation, but still proposes a new flat API page and does not provide the required migration or drift analysis.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=e820b6c4381f2b584f4fb75e118822cab822720708679f6856aff845dce75a20; output_sha256=dfbe8172d90067220e1bfefa5918019dcae6509b8260cde8255ddad9258ed2fb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Proposes a new flat API page and index link, explicitly declines migration, and omits hierarchy-drift and out-of-batch drift analysis.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- All five assertions fail in the with_skill lane.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-015-flat-hierarchy-migration-proposal`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e820b6c4381f2b584f4fb75e118822cab822720708679f6856aff845dce75a20` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-015-flat-hierarchy-migration-proposal`.
- Fixture SHA-256: `e820b6c4381f2b584f4fb75e118822cab822720708679f6856aff845dce75a20`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `de76a086939d1591df845f72fbdb70d76c350be98629e84e5fc28aead6c5474b`
- Metadata SHA-256: `f008330cf4c09bf2d8f5e755019b196220dae437f59e25ab5a6b76314ba70a05`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | FAIL | with_skill 点名了 research-conversations.md 和 graph-search.md，并提到 feature catalog/feature_path，但未明确说明二者属于同一个缺失的知识发现与应用域节点，也未给出足够的 route prefix/tag、related_code 或 owner 证据。 |
| `proposes_migration_before_write` | FAIL | with_skill 给出了目标树和三种处理方向，但缺少每个旧路径到新路径的映射、入链与递归导航 delta、change-map required_docs delta、排除项理由，且决策选项不是要求的三个精确选项。 |
| `does_not_deepen_flat_layout` | PASS | with_skill 明确表示暂未修改文件；新消息页面拟放在 knowledge-discovery/conversations 子树，而非 docs/site/api/ 一级；git_evidence 显示无提交、无工作区改动或交付输出。 |
| `reports_out_of_batch_drift_read_only` | FAIL | with_skill 只列出数据库、设计、运维、产品、Release Notes 等排除项，未将知识建设与维护、平台治理与运行两组批次外 drift 按页面清单、建议目标节点和范围外说明进行只读报告。 |
| `loads_only_api_contract` | FAIL | with_skill 未显式列出仅加载的 API 类型模块与 host API 模板，也未提供名为 Hierarchy drift 的显式结论字段；仅以范围排除项间接提及其他文档类型。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=e820b6c4381f2b584f4fb75e118822cab822720708679f6856aff845dce75a20; output_sha256=614be8d77bd77f79f3d351515ced76b92e25c6b5c30ffd8e6230f3f9d42625a8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别部分扁平路径问题并提出嵌套目标树，声明零写入，但迁移提案、批次外 drift 报告和加载/Hierarchy drift 记录不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=e820b6c4381f2b584f4fb75e118822cab822720708679f6856aff845dce75a20; output_sha256=6152a8637dbb4b1853bd83861a6ff8450ff901acc03f9569bd30c7b7dd8a30a4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出扁平 API 一级新增页面方案，未识别层级 drift，保留现有路径并只增加首页链接。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足扁平 drift 证据完整性要求。
- with_skill 未提供完整的一次性迁移提案及规定的决策选项。
- with_skill 未报告两组批次外 drift 的页面清单和建议节点。
- with_skill 未显式报告 API-only 加载范围与 Hierarchy drift 结论。
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-015-flat-hierarchy-migration-proposal`
- Review context: issue #225，为已有扁平文档补上迁移触发机制

## Test Set / Fixture Version

- Fixture: `workspace/eval-015-flat-hierarchy-migration-proposal`，含 `.eval/actual-diff.patch` 与 handoff 内的测试结果引用，feature delivery 入口证据链完整
- Scenario: 宿主 API 根下 6 个稳定页面按 feature catalog 分属三个一级功能域却全部平铺，本批次要同步一个属于其中一个域的新会话消息 API 页；维护者只确认了新页面同步，未确认任何路径迁移
- Evidence set: PM handoff、actual diff、feature catalog、Approved PRD、Confirmed TRD、完成态实施计划、路由与 schema 源码、contract tests、既有 change map（含手工未知字段条目）、现有扁平 API 页与 host standards
- Actual validation date: `2026-08-05`
- Isolation: 三条互相独立的全新 `codex exec` 会话——`with_skill`、`without_skill`、judge，符合 `AGENTS.md` 的 Eval runner 约束（隔离全新上下文 + 独立评审方）。两条 lane 复制同一份 pristine fixture（排除 `comparison.md` 与 `eval_metadata.json`）到 `tmp/eval-runs/issue-225-20260805-r3/` 下各自目录；`without_skill` lane 被显式禁止读取任何 agent skill 文档、Agent README、仓库指导文件与历史 eval 结果；judge 以只读会话独立核对零写入，不采信任一 lane 的自述

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
- With skill 5/5；fresh without_skill baseline 0/5

Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `detects_flat_hierarchy_drift` | FAIL | FAIL | with_skill 仅指出 `research-conversations.md`，称 `graph-search.md` 为“同类观察”，未明确二者同属缺失的“知识发现与应用”节点；without_skill 未识别 drift。feature catalog 确实将二者分别列为 `knowledge-discovery/conversations` 与 `knowledge-discovery/graph-search`。 |
| `proposes_migration_before_write` | FAIL | FAIL | with_skill 给出 `research-conversations.md` 的迁移路径和三个选项，但未给出 `graph-search.md` 映射、完整入链/递归导航 delta、排除理由；without_skill 只提议新增一级页面 `docs/site/api/conversation-messages.md`，无迁移提案。 |
| `does_not_deepen_flat_layout` | PASS | FAIL | with_skill 明确“尚未写入任何文件”，且工作区没有新增文档；without_skill 明确提出在 `docs/site/api/` 一级新增 `conversation-messages.md`（`result.txt:5`）。 |
| `reports_out_of_batch_drift_read_only` | FAIL | FAIL | with_skill 只提到 `graph-search.md`，没有分别报告“知识建设与维护”和“平台治理与运行”两组页面清单及目标节点；without_skill 未报告批次外 drift。 |
| `loads_only_api_contract` | FAIL | FAIL | with_skill 声明不涉及其他类型，但未显式列出“已加载模块”、host API 模板及 `Hierarchy drift` 结论字段；without_skill 同样没有这些显式报告。 |

未满足断言（with/without 任一 FAIL）：``detects_flat_hierarchy_drift``、``proposes_migration_before_write``、``does_not_deepen_flat_layout``、``reports_out_of_batch_drift_read_only``、``loads_only_api_contract``



## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `detects_flat_hierarchy_drift`: with skill PASS；without skill FAIL。skill lane 报告 `Hierarchy drift: positive` 并点名 `research-conversations.md` 与 `graph-search.md`，归类证据用 feature catalog、owner、`feature_path` 与 route prefix；baseline 把新页面放进 API 根并称之为「稳定扁平路径」，没有识别两页共同缺失的域节点。
- `proposes_migration_before_write`: with skill PASS；without skill FAIL。skill lane 给出逐级 `index.md` 目标树、两个旧路径到新路径的映射、入链与递归导航 delta、两条 change-map `required_docs` delta、排除项与三个决策选项；baseline 只有「根目录新页 + API 索引 + change map」的扁平候选，没有目标子树、路径映射或迁移决策面。
- `does_not_deepen_flat_layout`: with skill PASS；without skill FAIL。skill lane 明确即使选择「仅确认本批次」，新页面也落在目标深度、绝不追加到 API 根；baseline 本轮虽零写入，但候选方案准备把新页面追加为 `docs/site/api/conversation-messages.md`，会继续加深扁平结构。
- `reports_out_of_batch_drift_read_only`: with skill PASS；without skill FAIL。skill lane 分别列出两组批次外 drift 的页面清单与建议目标节点并声明不移动、不改 map、不扩为全站重构；baseline 只笼统排除「其他 API 功能」。
- `loads_only_api_contract`: with skill PASS；without skill FAIL。skill lane 报告 `Loaded type modules: api` 与 `Hierarchy drift` 结论并点名 host API template；baseline 两个字段都不存在。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 选择 feature delivery 模式，消费 `.eval/actual-diff.patch` 作为入口证据，只加载 API 类型模块与 host API 模板。
- 在 Step 4 候选范围之前执行扁平层级 drift 检查，只读页面路径与 frontmatter，输出本批次 positive drift 与两组批次外 drift。
- 对本批次要写入的 `knowledge-discovery` 父节点给出一次性迁移提案：目标树、旧新路径映射、入链与递归导航修复、conversations 与 graph 两条 change-map entry 的闭包、排除项，以及新消息页在目标树中的位置。
- 因宿主未提供 redirect 机制，提案把两个旧路径保留为最小兼容页，而不是虚构 HTTP redirect。
- 给出「迁移 + 本批次一起确认（推荐）/ 仅确认本批次 / 全部暂缓」三个决策并等待确认，批次外两组 drift 保持只读。
- 对文档站零写入，未运行写后 read-back 与 host docs checks，未进入 docs-audit handoff。

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Source: 本轮新生成的 `without_skill` lane，使用同一条 prompt 与同一份 pristine fixture；未读取目标 skill、Docs Agent README、`_internal/**`、仓库指导文件、历史 `comparison.md` 或 with-skill 输出。未复用任何历史 baseline。
- baseline 核对了证据链、停在范围确认、保持零写入，这些一般性谨慎行为都做到了。
- 但它主动选择把新页面追加为 `docs/site/api/conversation-messages.md`，理由是「沿用现有 API 宿主的稳定扁平路径」，并判定按 `feature_path` 建多级目录「超出 handoff 已确认边界」。既有扁平页面的 drift、迁移提案、批次外观察、已加载模块与 drift 报告字段全部缺失——issue #225 描述的沉默行为在无 skill 条件下被完整复现，且这一轮它还主动加深了扁平结构。
- Baseline result: **0/5**。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- With-skill assertion failures: 无。
- Baseline failures: 全部 5 条。
- Infrastructure blockers: 无。judge 通过比对两条 lane 工作副本与 pristine fixture 的全量文件哈希（三份 `docs/site/` 哈希一致）独立确认零写入。

## Next Steps

- 保持 fixture 中「三个域各 2 页平铺 + 只确认新增一页」的结构：它同时考验触发（本批次域）与克制（批次外域），是本 eval 区分度的来源。
- 本 eval 不覆盖两类 resolved-page 例外：维护者已确认保留在类型根的稳定权威页，以及 canonical 目标已存在的兼容 stub。前者由 `eval-007-feature-database-design` 的定向回归验证覆盖，后者目前只有规则约束；如需固化为回归保护，应新增独立 eval 而不是扩大本 eval 范围。
- 本 eval 同样不覆盖「父目录已存在、旧扁平页仍在根」这一回流场景的独立断言，该场景由 `_internal/INSTRUCTIONS.md` 的本批次判定条款约束。

## Runtime Artifact Policy

- 两条 lane 的 fixture 副本、lane 输出、judge verdict 与运行日志保留在 `tmp/eval-runs/issue-225-20260805-r3/` 与会话 scratchpad 中，不提交。
- 仅本 `comparison.md` 作为 durable result 提交；transcript、candidate output、verdict、timing、diagnostics 与生成站点均不入 git。
