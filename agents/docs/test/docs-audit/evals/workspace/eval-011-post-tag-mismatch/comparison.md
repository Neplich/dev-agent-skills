# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86` from `agents/docs/test/docs-audit/evals/workspace/eval-011-post-tag-mismatch`.
- Fixture SHA-256: `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- Metadata SHA-256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | 明确解析 pre-tag authority 的 commit/tree，并以已提交 handoff 为依据；将未提交的 worktree audit 副本认定为不可用发布证据。 |
| `validates_current_attempt_history` | PASS | 核对 committed pre-tag handoff 的 attempt 2、superseded attempt 1 和 v1.2.0 关系，并因 worktree 改写 authority/result 而保持 blocked。 |
| `rejects_complete_release_tree_drift` | PASS | 明确指出实际 pre-tag 到 tag 的完整差异新增 src/catalog/export-v2.py，并据此保持 blocked。 |
| `offers_safe_maintainer_recovery` | PASS | 提供修复当前 v1.2.0 或确认新版本两类选择，要求重新执行 pre-tag/post-tag 审计，并将操作限定为维护者流程。 |
| `persists_blocked_without_corrupting_authority` | FAIL | 说明本次未写入或修改 authority，但未明确说明失败的 blocked 结果持久化的恢复条件，也未完整表述未完成写入不会产生成功状态。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=c2809ba2d90c1f00b857f770e3dc61c446ab411fe3caee03cd2e7ac3e1ec90ee; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 以 pre-tag authority 为准，核对提交历史和完整 tree diff，拒绝漂移副本与 release_verified，并提出安全恢复选项；未充分处理结果持久化失败条件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=23c711dd195f752a0c7d066ba152cdaeaeb8bece53aaf4a9e908a6569fe6a5d2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了未提交 audit 副本、tag 差异和缺失 post-tag 记录，但未按要求以 immutable pre-tag authority 和完整 tree 绑定为核心，且给出可打 tag 的倾向性结论。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 persists_blocked_without_corrupting_authority：缺少持久化故障恢复条件及未完成写入不会产生成功状态的明确说明。
- Next: 补充 blocked 结果持久化失败时的恢复条件，并明确任何未完成写入都不会生成成功状态或修改既有 authority。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9e3866c8bd3113bab586de6d712d224d3718fa740e3b1e2887b2b51725369b40` from `agents/docs/test/docs-audit/evals/workspace/eval-011-post-tag-mismatch`.
- Fixture SHA-256: `9e3866c8bd3113bab586de6d712d224d3718fa740e3b1e2887b2b51725369b40`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- Metadata SHA-256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | FAIL | The output identifies the pre-tag commit and notes the modified worktree copy, but does not demonstrate resolving the pre-tag commit and tree refs, reading audit/handoff with git show, or explicitly isolating the M copy as non-authoritative. |
| `validates_current_attempt_history` | FAIL | It reports attempt 2 and the blocked state, but does not explicitly verify same-version attempt history or that attempt 1 was directly superseded. |
| `rejects_complete_release_tree_drift` | PASS | It keeps the result blocked and identifies the tag-versus-pre-tag added file src/catalog/export-v2.py as the decisive unreviewed tree difference. |
| `offers_safe_maintainer_recovery` | PASS | It provides same-version remediation through correcting/removing the tag and rerunning pre-tag audit, plus abandoning v1.2.0 and establishing a new version; it also states the required valid handoff/audit prerequisites and assigns documentation work to named owners. |
| `persists_blocked_without_corrupting_authority` | FAIL | It separates the blocked conclusion from the uncommitted worktree record and states no writes occurred, but does not explain recovery conditions for the failed persistence attempt or explicitly guarantee that incomplete writes cannot create success or alter existing authority. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=9e3866c8bd3113bab586de6d712d224d3718fa740e3b1e2887b2b51725369b40; output_sha256=8c3c43a30ecbe53ff86cb2bebfb63699c58d186c507ff2ca58dd97c79f1238ce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Returns blocked, identifies the decisive tree drift and uncommitted audit copy, and offers recovery choices, but omits explicit evidence for immutable ref reads, superseded-attempt validation, and persistence-failure recovery guarantees.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=9e3866c8bd3113bab586de6d712d224d3718fa740e3b1e2887b2b51725369b40; output_sha256=4db052e0d6f679b672ee6aef7e5230f7afae062cf43e5eed85c608714f8ecb94; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the added source drift and uncommitted post-tag copy, but uses a weaker tag_exists_with_evidence_gap conclusion and does not establish the full authority and attempt-history controls.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output fails the immutable authority-read requirement.
- The with_skill output fails to explicitly validate attempt 1 supersession and same-version history.
- The with_skill output fails to state persistence-failure recovery and no-corruption guarantees.
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

- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`
- Scenario: same-version history、当前副本漂移与未审计 tag 增量
- Review context: issue #177 sub-batch 4b

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-1`
- Validation time: `2026-07-28 22:48:16 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-audit/round-1/`
- Assertions: 5，全部实际触发

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | PASS | 两者均区分 `.eval/committed-audit-v1.2.0.md` 与被篡改的 `docs/site/.meta/audit/audit-v1.2.0.md`，并引用 `.eval/release-context.md` 的可信提交记录。 |
| `validates_current_attempt_history` | FAIL | FAIL | fixture 含 `current_pre_tag_attempt: 2`、历史 attempt lineage；两者均未明确核对累计历史与当前 attempt 的一致性，仅直接采信 `candidate_verified`。 |
| `rejects_complete_release_tree_drift` | PASS | PASS | 两者均引用 `.eval/tag-tree-diff.name-status` 的 `A src/catalog/export-v2.py`，指出 tag 含未审计增量并保持 `blocked`。 |
| `offers_safe_maintainer_recovery` | PASS | FAIL | with_skill 明确针对同一 `v1.2.0` 修正 tag 或确认新版本并重新审计，且指定维护者边界；without_skill 虽提供两种路径，但未明确“同版本修复”与“改用新版本”的版本确认边界。 |
| `persists_blocked_without_corrupting_authority` | FAIL | PASS | with_skill 仅说未写入，未说明 `.eval/release-context.md` 所述 staged 后提交失败及恢复条件；without_skill 明确说明 staged 写入失败、post-tag 记录不存在、未产生成功状态且未执行写入。 |

未满足断言（with/without 任一 FAIL）：``validates_current_attempt_history``、``offers_safe_maintainer_recovery``、``persists_blocked_without_corrupting_authority``



## Leakage Surface Analysis

重做前，prompt、assertions 和 release context 直接提供 immutable record 选择、strict tree equality、lineage digest 算法、两条 remedy、re-entry 条件、blocked record 事务和 rollback 清单。

重做后，fixture 只保留两份 repository-state bytes、raw tag tuple、raw tree diff、committed candidate/discovery 和一次 staged 写入失败事件。显眼 tree delta 仍对 baseline 可见，但维护者版本选择契约不再出现在生成输入中。

## Redesign

- prompt 只要求给出结论、决定性差异、可持久化结果和维护者后续选择。
- assertions 改为 immutable authority、attempt history、complete tree、maintainer recovery 和 blocked persistence 五个语义结果。
- 删除 equality、active attempt、lineage rule、CAS policy 与标准答案 prose。
- 在 committed discovery 的 current tuple 中引入单字符 `previous_lineage_digest` 冲突，与 visible code-tree drift 形成两个独立 blocker。
- 清理历史 issue 身份引用，并重算 inventory/candidate/discovery object identities；只保留刻意的 lineage 冲突。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | PASS | 两臂均使用 committed evidence 并隔离 checkout 副本。 |
| `validates_current_attempt_history` | PASS | PASS | 两臂均识别 `33adb` / `03adb` lineage 冲突。 |
| `rejects_complete_release_tree_drift` | PASS | PASS | 两臂均以完整 tree mismatch 和新增源文件阻塞。 |
| `offers_safe_maintainer_recovery` | PASS | FAIL | baseline 未明确提供同版本重跑与维护者确认新版本两类路径及完整重入前置。 |
| `persists_blocked_without_corrupting_authority` | PASS | PASS | 两臂均分离 blocked 结果与 pre-tag authority，并确认 staged 故障未形成持久成功。 |

## Fresh Validation Method

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- 两臂锁定前只读取同一 prompt/fixture，未读取 assertions、expected output 或旧 comparison。
- with-skill arm读取完整 Docs/docs-audit 指令；without-skill arm隔离这些内容和 with-skill 输出。
- fresh judge 在 response SHA-256 锁定后才读取 assertions。
- with-skill SHA-256：`2412c4e8a8e2e5bd31127afebcf852a0efb175da33596b35b084deec73e3aa9e`；without-skill：`f572067d3b6d05c6b55803129c2ceaaadcb5c4f1f8d941e180eeea0f0adfbc89`。

## Failures And Limitations

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- with-skill 无失败；Coverage FULL。
- raw tree diff 与 committed records 仍让 baseline 恢复 4/5；可测量差距集中在 specialist 的维护者救济边界。
- 第一轮即达到区分度，无需第二轮。

## Runtime Artifact Policy

- runtime responses 和 judge verdict 仅保存在 `tmp/eval-runs/issue-177/docs-audit/round-1/`，不提交。
- 本 `comparison.md` 是唯一 durable 结果。

## Next Steps

- 本 assertion 措辞在本轮 review 后做了澄清性对齐，判定语义与已记录的 fresh run 一致，未重新执行 eval。
