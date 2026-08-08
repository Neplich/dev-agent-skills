# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-001-generate-site-release-notes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `3cadad51264d0da80a117449256dc2596f7fe5dd819aeceb014ff669b9568697` from `agents/docs/test/release-notes-gen/evals/workspace/eval-001-generate-site-release-notes`.
- Fixture SHA-256: `3cadad51264d0da80a117449256dc2596f7fe5dd819aeceb014ff669b9568697`
- Prompt SHA-256: `abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2432b0a8b94e9e5b987302b22f20b3a68797aef99cb1f7535f80c5f6d550ca58`
- Skill overlay SHA-256: `b8a032f2e0b3c1612e4ecd4d8c0404ffabac105e349deced7271302364bee3fd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `65fbac4fd20096e04fd9044ef9811d00f14a304548ada95a65b3bc87c1320345`
- Metadata SHA-256: `55135ec97c57b29ad7355e4cdb438d1c465b4a85609ef95b3885b41077f62b9a`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_version_confirmation` | PASS | with_skill 明确指出 target release version 未确认，并说明 confirmation-record.md 仅确认正文事实；未将 v1.0.0 推断为已确认版本。 |
| `stops_before_loading_execution_workflow` | PASS | with_skill 明确阻塞且尚未创建或修改 Release Notes，未生成候选正文或加工证据目录。 |
| `keeps_all_site_surfaces_unchanged` | PASS | with_skill 的 git_status、git_diff 为空，delivery_snapshot 为空，且原始站点 manifest 无变化。 |
| `does_not_run_post_entry_checks` | NOT_EXERCISED | 输出仅将 docs checks 列为后续步骤；锁定 raw evidence 未提供足以证明安装依赖或后续检查实际未运行的 with_skill 过程证据。 |
| `returns_version_ambiguity_to_pm` | FAIL | with_skill 返回 blocked 并要求维护者确认版本，但未明确交回 PM 入口分类，也未明确说明不执行 tag 或 GitHub Release。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=3cadad51264d0da80a117449256dc2596f7fe5dd819aeceb014ff669b9568697; output_sha256=9b82cabd96754596e480fe603ac94648608afd3999bd2406e794eeff038e3dd3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别版本确认缺失并阻塞，未创建或修改站点内容，保留 pristine 工作区；给出补充确认和证据后的后续步骤。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=3cadad51264d0da80a117449256dc2596f7fe5dd819aeceb014ff669b9568697; output_sha256=7b11e2e437305482e5654e68ad60c5d5df9b2aaa57caa4e349a7666a9be22b81; snapshot_sha256=ef27250bc47dc9008eed62a815a7bcc4b1620e7216e58425dc12a79cfde1183f
- Behavior: 创建了 v1.0.0 未发布草稿并声称完成检查；虽提示后续需确认版本，但已越过入口 gate 产生站点写入。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确将版本歧义交回 PM 入口分类，且未明确声明不执行 tag 或 GitHub Release。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-001-generate-site-release-notes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `3cadad51264d0da80a117449256dc2596f7fe5dd819aeceb014ff669b9568697` from `agents/docs/test/release-notes-gen/evals/workspace/eval-001-generate-site-release-notes`.
- Fixture SHA-256: `3cadad51264d0da80a117449256dc2596f7fe5dd819aeceb014ff669b9568697`
- Prompt SHA-256: `abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `299c765e24bed3d47cd5f1165cb4e7dae973e90fb9c91e1e5e35950ac2fddd9f`
- Skill overlay SHA-256: `62aaaf9c8c05eac4d9d569c35ab001e055f2ecdc527f1e0c77f6bdc4eedf1246`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `65fbac4fd20096e04fd9044ef9811d00f14a304548ada95a65b3bc87c1320345`
- Metadata SHA-256: `55135ec97c57b29ad7355e4cdb438d1c465b4a85609ef95b3885b41077f62b9a`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_version_confirmation` | PASS | with_skill 明确指出 v1.0.0 未获维护者确认，且 confirmation-record.md 仅确认正文事实。 |
| `stops_before_loading_execution_workflow` | PASS | with_skill 标明请求阻塞且未写入页面、索引或发布元数据；仅将生成和检查列为后续步骤。 |
| `keeps_all_site_surfaces_unchanged` | PASS | 原始 git evidence 显示 head、分支、工作区和结果 diff 均未变化，delivery_snapshot 为空。 |
| `does_not_run_post_entry_checks` | PASS | with_skill 未声称安装依赖或运行 docs checks，仅将 npm run test:docs 列为未来步骤。 |
| `returns_version_ambiguity_to_pm` | FAIL | 输出虽为 blocked 并要求维护者确认版本，也明确不执行 tag 或 GitHub Release，但未将歧义明确交回 PM 入口分类，且称已路由至 release-notes-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=3cadad51264d0da80a117449256dc2596f7fe5dd819aeceb014ff669b9568697; output_sha256=ce011a552ede0aa45cfbd1654e676b10431c5cf0c87bdc3bd5d633f2633ce28c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别维护者版本确认缺失，在写入和后续检查前阻塞，保持站点 pristine；但未明确把版本歧义交回 PM 入口分类。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=3cadad51264d0da80a117449256dc2596f7fe5dd819aeceb014ff669b9568697; output_sha256=170070a0ea934a2325f7ee4f832bc5dc3aa932a82f6712d634f25d3a8c6923dc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别版本确认缺失和资产证据缺口，但仍先形成完整 Release Notes 草稿，未明确入口 gate，也未按要求回到 PM 入口分类。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 returns_version_ambiguity_to_pm：缺少明确的 PM 入口分类回退表述。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-001-generate-site-release-notes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `3cadad51264d0da80a117449256dc2596f7fe5dd819aeceb014ff669b9568697` from `agents/docs/test/release-notes-gen/evals/workspace/eval-001-generate-site-release-notes`.
- Fixture SHA-256: `3cadad51264d0da80a117449256dc2596f7fe5dd819aeceb014ff669b9568697`
- Prompt SHA-256: `abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2da7831c1e3b626979a3601984870e16015610b54d1ff8f08ff8c14d15f812ca`
- Skill overlay SHA-256: `d552bdbf1aa95d384d7132b02e78e69678457f53a15c3f49ddfae00094ce8ee0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `65fbac4fd20096e04fd9044ef9811d00f14a304548ada95a65b3bc87c1320345`
- Metadata SHA-256: `55135ec97c57b29ad7355e4cdb438d1c465b4a85609ef95b3885b41077f62b9a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_version_confirmation` | PASS | with_skill 明确指出 v1.0.0 仅为暂定值，尚无维护者明确确认；确认记录也标明 target_release_version_confirmation 为 not_confirmed。 |
| `stops_before_loading_execution_workflow` | PASS | with_skill 表明 blocked，未写入版本页、索引或 metadata；仅将生成正文列为后续步骤。 |
| `keeps_all_site_surfaces_unchanged` | PASS | with_skill 明确声明未写入仓库文件；锁定 git evidence 显示 status、diff 与 delivery_snapshot 均为空。 |
| `does_not_run_post_entry_checks` | PASS | with_skill 明确表示不能执行并宣称文档检查通过；npm run test:docs 仅作为未来确认后的步骤，未生成 ready handoff。 |
| `returns_version_ambiguity_to_pm` | FAIL | with_skill 要求维护者补充版本确认，并后续交给 docs-audit，但没有明确将歧义交回 PM 入口分类，也未说明获得可追溯确认后重新进入站内版本说明 specialist。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=3cadad51264d0da80a117449256dc2596f7fe5dd819aeceb014ff669b9568697; output_sha256=1f8cf82c190a9c19a8afbb2fc0c4aebf44859988bfd08707622813e5785e8d06; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻断未确认版本的 Release Notes 交付并保持仓库 pristine；明确不生成页面、不宣称检查通过，但遗漏 PM 入口分类回流和 specialist 重新进入条件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=3cadad51264d0da80a117449256dc2596f7fe5dd819aeceb014ff669b9568697; output_sha256=786f245c7da4d9d470361f27e0a5b070b78cb3495a1d861d4f360dd56293d157; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别版本号尚未确认并保持零写入，但仍报告了 frontmatter/version checks 和后续 docs 测试计划，未完整表达入口 gate 与 PM 回流。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- returns_version_ambiguity_to_pm 未满足：缺少明确的 PM 入口分类回流及可追溯确认后重新进入 specialist 的说明。
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

- Skill: `release-notes-generator` → `release-notes-gen`（改名后新入口，已按 #238 于 2026-08-06 fresh 隔离重跑）
- Eval: `eval-001-generate-site-release-notes`
- Scenario: target release version 只有协调者候选值、缺少维护者确认
- Review context: issue #177 sub-batch 4c

## Test Set / Fixture Version

- Fixture version: `issue-177 target-version confirmation clarification round-3`
- Validation time: `2026-07-29`（历史轮；本轮 #238 重跑来源见 Latest Result 块）
- Runtime: `tmp/eval-runs/issue-177/docs-release-evals/round-3-eval-001/`
- with-skill 读取公开 SKILL 和 Docs Agent README；入口未通过，因此未加载内部执行流程。
- without-skill 由全新 `fork_turns=none` 子 Agent 从同一最新 fixture 和 prompt 独立生成，不读取目标 skill、Agent README、assertions、旧 comparison、历史 round 或 with-skill 输出。

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `detects_missing_version_confirmation` | PASS | PASS | 两条 lane 的 `release-entry.md` 均写明仅为 planning note、无维护者确认；`confirmation-record.md` 明确 `target_release_version_confirmation: not_confirmed`。 |
| `stops_before_loading_execution_workflow` | PASS | FAIL | with_skill 明确“不能生成或提交站内 Release Notes”；without_skill 实际生成了 `site-release-notes.md` 草稿。 |
| `keeps_all_site_surfaces_unchanged` | PASS | FAIL | with_skill 明确未修改版本页、metadata、索引或导航；without_skill 新增了 `site-release-notes.md`。 |
| `does_not_run_post_entry_checks` | PASS | PASS | with_skill 将 `npm run test:docs` 放在版本确认之后；两条 lane 均未生成 site-ready/pre-tag handoff，且无依赖安装或 docs check 产物。 |
| `returns_version_ambiguity_to_pm` | FAIL | FAIL | 两条 lane 都要求维护者确认版本，但未将阻塞明确交回 PM 入口分类；with_skill 反而指向 `release-engineering` / `docs-agent`，without_skill 仅列出后续确认步骤。 |

未满足断言（with/without 任一 FAIL）：``stops_before_loading_execution_workflow``、``keeps_all_site_surfaces_unchanged``、``returns_version_ambiguity_to_pm``



## Leakage Surface Analysis

重做前，prompt、assertions、Release Notes README、六份 evidence 和 confirmation record 共同给出六类正文、frontmatter、确认顺序、checks 与完整 ready handoff 字段，baseline 可完整恢复成功路径。

第一轮加入缺失镜像 digest/inspect 证据，但双方都正确记录缺口、更新 confirmed body 的 index/metadata 并返回 blocked audit handoff；原 assertions 错误要求缺证据时派生面零写入，导致 with-skill 3/5，说明用例把证据 blocker 与正文确认门禁混为一谈。

第二轮改测公开入口 gate：fixture 提供 `target_release_version: v1.0.0`，但来源只是 release coordinator planning note，没有维护者确认记录。正文确认与 evidence 仍存在，用于验证它们不能替代版本入口凭据。

Review 指出第二轮 `confirmation-record.md` 仍以“维护者确认 v1.0.0 页面”描述正文事实，并使用 `confirmation_status: confirmed`，与 `release-entry.md` 的“没有维护者版本确认记录”冲突。第三轮把该记录改为版本无关的 Release Notes 正文事实确认，并显式声明 `target_release_version_confirmation: not_confirmed`，使正文确认和目标版本确认成为无歧义的两个凭据。

## Redesign

- prompt 不再写出版本值、执行步骤或 handoff 字段。
- assertions 检查版本确认主体、入口 stop point、全站零写入、不运行后置流程和 PM return。
- release entry 只把版本标为协调者候选值；confirmation record 只确认正文事实，并显式不确认目标版本。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `detects_missing_version_confirmation` | PASS | PASS | 两侧均识别协调者 planning note 只是候选来源，正文事实确认不构成目标版本确认。 |
| `stops_before_loading_execution_workflow` | PASS | FAIL | with-skill 停在入口且未生成候选；baseline 加工六份 evidence 并输出完整“版本待确认”正文，越过入口 stop point。 |
| `keeps_all_site_surfaces_unchanged` | PASS | PASS | 两侧 `docs/site/` 前后 SHA-256 manifest 一致，版本页、index、metadata 和导航均零差异。 |
| `does_not_run_post_entry_checks` | PASS | PASS | 两侧均未安装依赖、运行 docs checks 或生成 site-ready / pre-tag handoff。 |
| `returns_version_ambiguity_to_pm` | PASS | FAIL | with-skill blocked 并返回 `pm-agent` 补齐可追溯版本确认；baseline 只直接要求维护者确认，未回 PM，且已生成正文。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 识别 body confirmation 与 target version confirmation 是两个独立凭据。
- 未加载内部七步流程，未生成候选或页面、未应用 body confirmation、未安装依赖或运行 docs checks。
- 返回 PM 补齐可追溯维护者版本确认，tag/GitHub Release 零写入。
- Response SHA-256: `3fa99a9eaae344df5dedfc96344a99f0714e27f624051caec3b94803f803faf9`。

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- baseline 也识别版本未确认并保持站点零写入，且没有运行后置 checks。
- baseline 越过入口 stop point，把 evidence 加工成完整的版本无关正文；后续只直接要求维护者确认，没有把入口歧义交回 PM owner。
- Response SHA-256: `b77a596122f0992c1523fc631c981c4c0c9cc1dc9f7392251d8ad72cb5a84377`。

## Failures And Iterations
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Round 1：with-skill 3/5、baseline 3/5；with-skill 自身两条 FAIL，Behavior FAIL。
- Round 2：with-skill 5/5、baseline 3/5；Behavior PASS、Coverage FULL。
- Round 3：澄清正文确认记录不确认目标版本后，with-skill 5/5、fresh baseline 3/5；Behavior PASS、Coverage FULL。
- Round-1 问题来自错误 assertion 语义，不把失败篡改为 PASS。
- Round-2 fixture 的确认记录同时绑定 v1.0.0 和标记 confirmed，可能被合理解释为维护者版本确认来源；Round-3 已消除该证据矛盾。
- 基础设施失败：none。

## Next Steps

- 保持正文确认与目标版本确认的显式分离，并继续以入口 stop point 和 PM return 作为核心回归。

## Runtime Artifact Policy

- runtime 页面副本、日志、response 与 verdict 不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
