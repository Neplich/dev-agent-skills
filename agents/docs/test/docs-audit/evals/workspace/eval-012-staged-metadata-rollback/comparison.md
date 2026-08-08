# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-012-staged-metadata-rollback`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620` from `agents/docs/test/docs-audit/evals/workspace/eval-012-staged-metadata-rollback`.
- Fixture SHA-256: `1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620`
- Prompt SHA-256: `4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `885108a0e0e9ce48751816455b91da0ec400a08bb7d3a722984a36e4221d1938`
- Metadata SHA-256: `86b2ab0ad4bcb3fb98728ca8ff1375ff58d1094876353cbeafc325bf7593eb63`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_non_content_candidate_drift` | PASS | with_skill cites staged.name-status, staged.summary, and staged.patch, identifying mode, symlink/type, rename, deletion, and path-target changes. |
| `rejects_every_unauthorized_transformation` | PASS | with_skill blocks publication and explicitly covers the executable-mode change, catalog-status symlink, release-note rename/deletion, and escaping unexpected symlink. |
| `rechecks_committed_candidate_boundaries` | FAIL | It says the unchanged host state does not prove candidate validity, but does not explicitly require rechecking the same authorization boundaries after candidate and handoff formation. |
| `rolls_back_only_the_failed_attempt` | FAIL | It recommends abandoning and regenerating the candidate, but does not explain isolating the failed attempt/draft, restoring the touched authorized host state, and preserving unrelated user changes. |
| `proves_host_state_restoration` | FAIL | It proves unchanged ref, index, and worktree hashes, but does not cover relevant path identities or provide residual/half-stamp cleanup handling. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620; output_sha256=f0063cabfb56fb43da621776b987500ce7bd27db7d4a1c5f1bf0975cd5d4c5ab; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks publication with stronger structural and evidence-integrity findings, but omits explicit final-boundary recheck and precise rollback/restoration requirements.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620; output_sha256=5651bcf79a98bf0e301f44059ac7604e077b1fe7339f927ee6d2ec3a2ba3b6af; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks publication and notes several structural issues, but misses mode drift and gives weaker boundary and cleanup reasoning.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill does not explicitly require rechecking committed candidate and handoff boundaries.
- with_skill does not precisely scope rollback to the failed attempt while preserving unrelated user changes.
- with_skill does not fully prove relevant path identity restoration or residual cleanup.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-012-staged-metadata-rollback`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4d1932ef946b48a83d2fe93fa9ff8ea85df4b26c8944c206493268c53de7692b` from `agents/docs/test/docs-audit/evals/workspace/eval-012-staged-metadata-rollback`.
- Fixture SHA-256: `4d1932ef946b48a83d2fe93fa9ff8ea85df4b26c8944c206493268c53de7692b`
- Prompt SHA-256: `4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `885108a0e0e9ce48751816455b91da0ec400a08bb7d3a722984a36e4221d1938`
- Metadata SHA-256: `86b2ab0ad4bcb3fb98728ca8ff1375ff58d1094876353cbeafc325bf7593eb63`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_non_content_candidate_drift` | FAIL | with_skill 识别了 catalog-status 符号链接和越界链接，但未覆盖 catalog-items 的 100644→100755 模式变化，也未识别 audit-v1.2.0.md 的符号链接语义。 |
| `rejects_every_unauthorized_transformation` | FAIL | with_skill 覆盖了删除、重命名、类型替换和越界链接，但遗漏了可执行模式变更等授权边界违反项，不能证明逐类拒绝全部越界转换。 |
| `rechecks_committed_candidate_boundaries` | FAIL | with_skill 阻止创建 tag/继续发布，但未说明后续 committed candidate 与 handoff 形成后必须重新验证同一授权边界。 |
| `rolls_back_only_the_failed_attempt` | PASS | with_skill 要求丢弃/重建候选暂存快照，并依据清理前后 host、index、worktree 哈希一致的证据说明清理未改变宿主；同时明确 notes/release-checklist.md 和 notes/local.txt 等无关用户修改仍保留。 |
| `proves_host_state_restoration` | PASS | with_skill 以清理前后 status、index diff、worktree diff 哈希一致以及相关路径记录证明没有宿主残留，并在缺少完整 authority 证明时继续 blocked，要求丢弃/重建候选并重新审计，而非宣称成功。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=4d1932ef946b48a83d2fe93fa9ff8ea85df4b26c8944c206493268c53de7692b; output_sha256=724c5a5235d476abdc0867f8231f31cdac8a892ab5b2b0f2f312a5490d3fe64d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻止发布并识别证据校验、删除、重命名、符号链接和宿主清理状态，但遗漏若干非文本语义变化，且未明确后续 candidate/handoff 复核要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=4d1932ef946b48a83d2fe93fa9ff8ea85df4b26c8944c206493268c53de7692b; output_sha256=86cb4f715e698d68d6fded51dbba1481d5cc42c0d4f41fbb2615c96ce24f04e3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 阻止发布并识别了大部分内容、模式、符号链接、断链和证据完整性问题，但未明确 committed candidate/handoff 的后续边界复核。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- detects_non_content_candidate_drift
- rejects_every_unauthorized_transformation
- rechecks_committed_candidate_boundaries
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-012-staged-metadata-rollback`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `56ccb183ce0a970ed157c6f0efa2f2e8e25742264f17604510b8d6ab06a81520` from `agents/docs/test/docs-audit/evals/workspace/eval-012-staged-metadata-rollback`.
- Fixture SHA-256: `56ccb183ce0a970ed157c6f0efa2f2e8e25742264f17604510b8d6ab06a81520`
- Prompt SHA-256: `4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `885108a0e0e9ce48751816455b91da0ec400a08bb7d3a722984a36e4221d1938`
- Metadata SHA-256: `86b2ab0ad4bcb3fb98728ca8ff1375ff58d1094876353cbeafc325bf7593eb63`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_non_content_candidate_drift` | PASS | with_skill 明确覆盖删除、重命名、普通文件到符号链接、仓库外符号链接和 100755 权限变化，并引用 staged.name-status、staged.raw、staged.patch、staged.summary。 |
| `rejects_every_unauthorized_transformation` | PASS | with_skill 逐类列出候选中的删除、重命名、链接转换、外部链接和可执行权限变化，并以不能继续发布、废弃候选为结论。 |
| `rechecks_committed_candidate_boundaries` | FAIL | with_skill 仅要求重新生成并复核发布快照，没有明确说明 candidate 与 handoff 形成后必须重新验证同一授权边界，也未明确否定早期 staged 结果作为最终 authority。 |
| `rolls_back_only_the_failed_attempt` | FAIL | with_skill 证明了清理前后状态哈希一致，但没有说明隔离 attempt、本次草稿、误触的授权宿主状态及无关用户变化之间的精确回滚边界。 |
| `proves_host_state_restoration` | FAIL | with_skill 提供 status、cached diff 和 worktree diff 的前后哈希，但未给出覆盖 ref、路径身份和残留状态的完整恢复证明；仅笼统声称未修改 ref。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=56ccb183ce0a970ed157c6f0efa2f2e8e25742264f17604510b8d6ab06a81520; output_sha256=4b800b98f76d5a2943e0e03197a263988a4c5c7e351852a86620ff68fdc5d3fd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了全部主要候选漂移并正确阻塞发布，但未完整说明最终 candidate/handoff 复核要求及精确、全面的恢复证明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=56ccb183ce0a970ed157c6f0efa2f2e8e25742264f17604510b8d6ab06a81520; output_sha256=6b2ac2644dbab41f9922fba734d5819d035ca1ed3799201335481c3c17571995; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了部分结构、链接和权限变化，并指出发布索引断链，但覆盖和边界证明较不完整。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确要求 committed candidate 与 handoff 形成后重新验证授权边界。
- with_skill 未精确界定仅回滚失败 attempt，同时保留无关用户变化。
- with_skill 未提供覆盖 ref、路径身份和残留状态的完整宿主恢复证明。
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

- Skill: `docs-audit`
- Eval: `eval-012-staged-metadata-rollback`
- Scenario: 非文本 candidate drift、committed boundary 与失败事务恢复
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
| `detects_non_content_candidate_drift` | FAIL | FAIL | 两条 lane 都识别了 staged hash 漂移、symlink 与 `160000` Gitlink，但未在最终输出中逐类覆盖 fixture 的 `100644→100755`、普通文件到 symlink、rename 和 delete 变更。 |
| `rejects_every_unauthorized_transformation` | FAIL | FAIL | 两条 lane 都阻止了 symlink 与 Gitlink，但没有明确把 snapshot A 中的模式变化、rename、delete 逐项纳入越界结论。 |
| `rechecks_committed_candidate_boundaries` | PASS | FAIL | with_skill 明确检查 hypothetical committed snapshot，并指出 `anchor_commit..handoff_commit` 的 `160000` Gitlink 不得提交；without_skill 仅说明当前没有 candidate/handoff，未明确要求后续 candidate 与 handoff 重新验证同一边界。 |
| `rolls_back_only_the_failed_attempt` | PASS | PASS | 两条 lane 都要求保留 `.eval/` 证据、恢复原始 staged snapshot，并明确保留 `notes/local.txt` 等无关用户变化。 |
| `proves_host_state_restoration` | PASS | PASS | 两条 lane 都基于 `prewrite-fingerprint.md` 识别 branch、unstaged 区、授权页面和无关文件未变，但 staged hash 仍为 `9999…`，因此没有虚构成功，并要求恢复后重新核验。 |

未满足断言（with/without 任一 FAIL）：``detects_non_content_candidate_drift``、``rejects_every_unauthorized_transformation``、``rechecks_committed_candidate_boundaries``



## Leakage Surface Analysis

重做前，prompt、assertions 和两份 fixture prose 直接列出两次 staged gate、两段 committed gate、所有拒绝类型、rollback 动作与完整恢复证明。

重做后，fixture 只保留 staged snapshot A/B、hypothetical committed snapshot 以及 before/after fingerprints。输入不再说明哪些 Git 维度必须检查、何时复检或恢复失败应如何裁定。

## Redesign

- prompt 只要求判断 attempt、决定性证据、清理范围与成功边界。
- assertions 改为 non-content drift、unauthorized transformations、committed recheck、attempt-scoped rollback 和 host restoration 五个语义结果。
- 将答案型 prose 改为 raw Git-like event log 和 fingerprint snapshot。
- 增加第二层阻塞：failed cleanup 后 branch/porcelain/unstaged/path identity 已恢复，但 staged raw digest 仍不等于 before snapshot。
- 保留 `notes/local.txt` 的一致 identity，用于验证不覆盖无关用户状态。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `detects_non_content_candidate_drift` | PASS | PASS | 两臂均覆盖 mode/type/path/object 语义。 |
| `rejects_every_unauthorized_transformation` | PASS | PASS | 两臂均报告 fixture 中全部转换类别。 |
| `rechecks_committed_candidate_boundaries` | PASS | FAIL | skill arm 将 anchor/handoff commit 级边界作为 staged 后的独立门禁；baseline 未建立该成功 authority 要求。 |
| `rolls_back_only_the_failed_attempt` | PASS | PASS | 两臂均限制 attempt-owned delta 并保留用户状态。 |
| `proves_host_state_restoration` | PASS | PASS | 两臂均因 staged digest 未恢复而继续 blocked。 |

## Fresh Validation Method

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- 两臂锁定前只读取同一 prompt 和两份 raw fixture，未读取 eval object、assertions 或旧 comparison。
- with-skill arm读取完整 Docs/docs-audit 指令；without-skill arm未读取或应用这些内容。
- response 锁定后才由 fresh judge 逐 assertion 判定。
- with-skill SHA-256：`eda6aa97bde26a253263458c4acb8148ea3ff37170cecde32f3c886ced8bed6a`；without-skill：`62b16aaf0056ac379c53eaca4a9571b9bad68779a42ac0193d6f53b7f9b95909`。

## Failures And Limitations

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- with-skill 无失败；Coverage FULL。
- raw log 仍直接暴露异常类型，因此 baseline 可恢复 4/5；差距集中在 committed confirmation 仍是独立 success authority。
- 第一轮即达到区分度，无需第二轮。

## Runtime Artifact Policy

- runtime responses 和 judge verdict 仅保存在 `tmp/eval-runs/issue-177/docs-audit/round-1/`，不提交。
- 本 `comparison.md` 是唯一 durable 结果。
