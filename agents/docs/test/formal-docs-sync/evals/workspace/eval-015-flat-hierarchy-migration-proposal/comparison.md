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

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

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
