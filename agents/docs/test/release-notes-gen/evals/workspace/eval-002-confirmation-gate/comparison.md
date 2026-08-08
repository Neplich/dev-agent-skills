# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-002-confirmation-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `96f3ebd893045bcb6258f448d567899e41ff3b23e37c5a73f9e213fdf3f448ee` from `agents/docs/test/release-notes-gen/evals/workspace/eval-002-confirmation-gate`.
- Fixture SHA-256: `96f3ebd893045bcb6258f448d567899e41ff3b23e37c5a73f9e213fdf3f448ee`
- Prompt SHA-256: `7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2432b0a8b94e9e5b987302b22f20b3a68797aef99cb1f7535f80c5f6d550ca58`
- Skill overlay SHA-256: `b8a032f2e0b3c1612e4ecd4d8c0404ffabac105e349deced7271302364bee3fd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `734d8912f6102b866e236fb845ac847f11fde3651b05c29ee143e730ba9a8ce3`
- Metadata SHA-256: `913e8a90d405fa7666ae23e665c2d55b7740272554f1234087ce53fcb62d5aad`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_derived_surfaces_unchanged` | PASS | with_skill reports .meta/releases.json, the Release Notes index, and navigation were not modified; git evidence shows only the new draft is untracked, and it says updates wait for正文确认. |
| `reports_unconfirmed_not_ready` | PASS | with_skill explicitly reports confirmation_status: unconfirmed and handoff: blocked, with no ready claim. |
| `waits_for_explicit_confirmation` | FAIL | It links to the generated draft and summarizes its coverage, but does not present the complete candidate正文 or identify the source evidence documents in the user-visible output. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=96f3ebd893045bcb6258f448d567899e41ff3b23e37c5a73f9e213fdf3f448ee; output_sha256=ee91b82500f8ecb5f4690e75cdbfca1fe5f2e7d32f6d9ce410ce7d7ef6511f4b; snapshot_sha256=b5ce73f11fa77f4a33947f96b4507c809cb1468f000ee15c71a4197b29c0238b
- Behavior: Created a comprehensive untracked draft, preserved derived surfaces, explicitly marked the handoff blocked and confirmation unconfirmed, and requested正文 confirmation before updates; presentation omitted full正文 and source-evidence details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=96f3ebd893045bcb6258f448d567899e41ff3b23e37c5a73f9e213fdf3f448ee; output_sha256=4cfbb5d2caf02bad54e8af71947be85bd87c15f0c5255b255a0424c2bf494669; snapshot_sha256=664affe84aa80cd9852dffec8a5123143385951a7d18561c48f76a93f5d45849
- Behavior: Created an untracked draft and preserved derived surfaces, but did not report explicit confirmation_status/handoff_status or clearly request confirmation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output does not user-visibly present the complete candidate正文 and source evidence required before requesting confirmation.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-002-confirmation-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `96f3ebd893045bcb6258f448d567899e41ff3b23e37c5a73f9e213fdf3f448ee` from `agents/docs/test/release-notes-gen/evals/workspace/eval-002-confirmation-gate`.
- Fixture SHA-256: `96f3ebd893045bcb6258f448d567899e41ff3b23e37c5a73f9e213fdf3f448ee`
- Prompt SHA-256: `7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `299c765e24bed3d47cd5f1165cb4e7dae973e90fb9c91e1e5e35950ac2fddd9f`
- Skill overlay SHA-256: `62aaaf9c8c05eac4d9d569c35ab001e055f2ecdc527f1e0c77f6bdc4eedf1246`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `734d8912f6102b866e236fb845ac847f11fde3651b05c29ee143e730ba9a8ce3`
- Metadata SHA-256: `913e8a90d405fa7666ae23e665c2d55b7740272554f1234087ce53fcb62d5aad`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_derived_surfaces_unchanged` | PASS | With-skill git evidence shows only the candidate page as untracked; index.md, .meta/releases.json, and navigation files are unchanged. Output states they have not been modified, and the candidate says confirmation precedes indexing/metadata updates. |
| `reports_unconfirmed_not_ready` | PASS | With-skill output says the page is awaiting maintainer confirmation, explicitly says no ready handoff was produced, and identifies missing confirmation and release evidence. |
| `waits_for_explicit_confirmation` | FAIL | The with-skill output provides only a link and category summary, not the complete candidate body, source evidence, or a concrete post-confirmation path plan. It does state that maintainer confirmation is pending. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=96f3ebd893045bcb6258f448d567899e41ff3b23e37c5a73f9e213fdf3f448ee; output_sha256=ef752beaf512fc58a74bf5a6ddf0cc47935b187032760c642613652a791b0b2e; snapshot_sha256=5ff31aff49ca8270e0bf7c41fed5ae89df15a50e43545ed891c9f65493cb2550
- Behavior: Preserved derived surfaces and clearly kept the work awaiting confirmation, but the handoff output omitted the complete candidate body, source evidence, and concrete confirmation-follow-up paths.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=96f3ebd893045bcb6258f448d567899e41ff3b23e37c5a73f9e213fdf3f448ee; output_sha256=9088f9989a61ff21496c29ba3271c8c0956950dce3ef8c500b258c9ddba93568; snapshot_sha256=744d0c4251763965f6d20203b46e5fff0e1363b3356ea60ea8b594ade2b0c7d5
- Behavior: Created an untracked candidate and preserved derived surfaces, but did not provide explicit structured not-ready handoff or the requested complete body, evidence, and confirmation plan.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane fails the explicit confirmation handoff requirement by not displaying the complete candidate body, source evidence, and planned post-confirmation paths.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-002-confirmation-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `96f3ebd893045bcb6258f448d567899e41ff3b23e37c5a73f9e213fdf3f448ee` from `agents/docs/test/release-notes-gen/evals/workspace/eval-002-confirmation-gate`.
- Fixture SHA-256: `96f3ebd893045bcb6258f448d567899e41ff3b23e37c5a73f9e213fdf3f448ee`
- Prompt SHA-256: `7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2da7831c1e3b626979a3601984870e16015610b54d1ff8f08ff8c14d15f812ca`
- Skill overlay SHA-256: `d552bdbf1aa95d384d7132b02e78e69678457f53a15c3f49ddfae00094ce8ee0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `734d8912f6102b866e236fb845ac847f11fde3651b05c29ee143e730ba9a8ce3`
- Metadata SHA-256: `913e8a90d405fa7666ae23e665c2d55b7740272554f1234087ce53fcb62d5aad`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_derived_surfaces_unchanged` | FAIL | with_skill 明确称未修改 releases.json、Release Notes 索引或导航，但没有明确说明这些路径必须等正文确认后才能修改。 |
| `reports_unconfirmed_not_ready` | PASS | with_skill 报告 confirmation_status: unconfirmed，并说明未输出 ready handoff；git evidence 也显示仅新增候选页面，派生面未变更。 |
| `waits_for_explicit_confirmation` | FAIL | with_skill 请求确认，但只提供候选正文的文件链接和主题摘要，没有在输出中展示完整候选正文、来源证据及确认后计划修改的具体路径。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=96f3ebd893045bcb6258f448d567899e41ff3b23e37c5a73f9e213fdf3f448ee; output_sha256=edec040ee1755b905f3e1ae60227bdfc0df8a830b0fffe9298fdac3694bf08a4; snapshot_sha256=ef22ae718596494c8b6003a3f737cff4c451344c040a6c83773041e6b97f4b05
- Behavior: 保持派生面未修改，明确 unconfirmed、未输出 ready handoff，并请求确认；但未明确派生路径须等待确认，也未展示完整正文、来源证据和确认后路径。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=96f3ebd893045bcb6258f448d567899e41ff3b23e37c5a73f9e213fdf3f448ee; output_sha256=8433041d558c25db941bf0ddd02fca77db9efdb41570a011935331e97f488c74; snapshot_sha256=0696ddb122d0f40321ca0c23d1d3bfa0932e22ce0dcf955cb0f14d6071b58817
- Behavior: 创建候选版本页并标注待确认，称未修改索引、metadata 或导航；未报告结构化 unconfirmed/blocked 状态，也未展示完整正文或确认后路径。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 keeps_derived_surfaces_unchanged 的显式等待条件。
- with_skill 未满足 waits_for_explicit_confirmation 对完整正文、来源证据和确认后路径的展示要求。
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
- Eval: `eval-002-confirmation-gate`
- Review context: issue #150

## Test Set / Fixture Version

- Fixture version: `issue-150 fresh-paired group-b v1`
- Actual validation date: `2026-07-21`
- Fresh run: `tmp/eval-runs/issue-150/group-b/eval-002-confirmation-gate/`
- Both lanes started from independent copies of the same pristine fixture.

## Latest Result

- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| keeps_derived_surfaces_unchanged | PASS | PASS | with_skill 的 `releases.json` 仍为 `latest: v0.9.0`，未新增索引/导航文件；without_skill 同样仅新增 `v1.0.0.md`，派生面保持原状。 |
| reports_unconfirmed_not_ready | PASS | PASS | with_skill 明确 `confirmation_status: unconfirmed`、`handoff_status: blocked`；without_skill 正文标注“待确认”，并明确确认前不纳入版本索引、metadata 或站点导航，属于未 ready 状态。 |
| waits_for_explicit_confirmation | PASS | FAIL | with_skill 展示完整候选正文、列出 `evidence/01` 至 `evidence/06` 来源，并写明“请确认该正文”及确认后更新 metadata/索引；without_skill 仅写“待确认”，未列出来源证据，也未明确等待确认后的修改计划路径。 |

未满足断言（with/without 任一 FAIL）：`waits_for_explicit_confirmation`



## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `keeps_derived_surfaces_unchanged`: PASS。结果与 pristine fixture 的 `release-notes/index.md`、`.meta/releases.json` 字节一致，未修改 navigation。
- `reports_unconfirmed_not_ready`: PASS。明确 `confirmation_status: unconfirmed` 与 `handoff_status: blocked`，未把候选页存在描述为 ready。
- `waits_for_explicit_confirmation`: PASS。展示完整六类候选正文与来源，列出确认后计划路径，明确等待用户或维护者确认，未模拟确认。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 候选页采用七字段 release frontmatter，并保持 `last_verified_version: unverified`。
- 未运行确认后的派生写入或 ready 流程，也未执行 GitHub Release、tag、部署或 #117 盖章。

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- 来源：同一 prompt/assertions 与独立 pristine fixture 的本轮 fresh `without_skill`；生成期间未读取目标 skill/Agent 指令、旧 comparison 或历史输出。
- baseline 也保持三类派生面零变化，输出 blocked/unconfirmed，完整展示正文、证据与确认后路径。
- 结果：3/3 PASS；未复用历史 baseline。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- With-skill assertion failures: none。
- Without-skill assertion failures: none。
- Comparative limitation: prompt、README 与 assertions 直接声明未确认时的零写入门禁。

## Next Steps

- 保持“完整候选展示 + 明确确认”作为任何派生写入与 ready handoff 的前置门禁。
- 如需测 uplift，加入含模糊批准语句或正文修订后旧确认失效的 case。

## Runtime Artifact Policy

- 候选页、响应与 isolated workspace 仅位于 `tmp/eval-runs/issue-150/group-b/eval-002-confirmation-gate/`，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。

## 磨平记录（2026-07-29）

维护者裁定本 eval 的零区分度属于模型能力进步磨平（(b) 类），批次 4 的重写已回滚。该 eval 作为 [issue #188](https://github.com/neplich/dev-agent-skills/issues/188) 的 skill 能力审查标本保留原样；在 #188 得出审查结论前不重做本 eval。
