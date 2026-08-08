# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-confirmed-release-delivery`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `66f607dd2167ff47674a24a52b3b537cbd227a6a1b4a574ecfef674b38f3633c` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-confirmed-release-delivery`.
- Fixture SHA-256: `66f607dd2167ff47674a24a52b3b537cbd227a6a1b4a574ecfef674b38f3633c`
- Prompt SHA-256: `5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2432b0a8b94e9e5b987302b22f20b3a68797aef99cb1f7535f80c5f6d550ca58`
- Skill overlay SHA-256: `b8a032f2e0b3c1612e4ecd4d8c0404ffabac105e349deced7271302364bee3fd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6ba71c78dee7f69b879178b4307965fc8b664b773fca948482dc1711c289b5ad`
- Metadata SHA-256: `281089e0eacfd344cee9623295c4741f90652b2ae8ae709447ae5189db5a2ee5`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `delivers_confirmed_release_page` | PASS | with_skill 的交付快照包含 v1.0.0 页面，覆盖六类证据，frontmatter 合法且 last_verified_version 为 unverified。 |
| `updates_derived_surfaces_after_confirmation` | NOT_EXERCISED | 快照显示 index 与 metadata 正确更新、保留 v0.9.0 和 manualNote；但锁定证据无法证明这些更新发生在确认生效之后。 |
| `passes_host_docs_checks` | FAIL | with_skill 明确报告 npm run test:docs 被 check:affected 的 committed base 缺失和 spawn EPERM 阻塞，未全部通过。 |
| `returns_complete_ready_handoff` | FAIL | 未输出字段完整的 docs-agent:docs-audit pre-tag ready handoff，也未明确 downstream_target 和 release_execution_authorized: false；反而将 handoff 标为 blocked。 |
| `preserves_external_release_boundary` | PASS | git evidence 显示无提交、分支或 ref 变化，仅修改站内页面与 metadata，且页面和 index 仍为 unverified；无外部发布或盖章证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=66f607dd2167ff47674a24a52b3b537cbd227a6a1b4a574ecfef674b38f3633c; output_sha256=da23bf92fba57e8324c6670f05f58e3f7b84f0dcac735a156e030bc64947eebe; snapshot_sha256=e98bd42555f67154ba2ff1fd964819eb0ee6dcd3081eca3c05e53a6ceffcaa49
- Behavior: 正确创建并更新站内 Release Notes，保留 unverified 边界并如实报告 docs 检查阻塞，但未完成全部检查或输出要求的完整 ready handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=66f607dd2167ff47674a24a52b3b537cbd227a6a1b4a574ecfef674b38f3633c; output_sha256=df80062203eff1f160a1f30fdb1cd4691d6bfc21b904f93f69f226249598bd53; snapshot_sha256=b5723270312c1bb6306547cbe46042362d095b0ab19662de032fae7ebc593193
- Behavior: 创建页面并更新 index/metadata，声称构建和测试通过，但未提供完整的 pre-tag ready handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- passes_host_docs_checks
- returns_complete_ready_handoff
- Next: 在可执行宿主环境重新运行 npm run test:docs 并提供可核验结果。
- Next: 补充完整的 docs-agent:docs-audit pre-tag ready handoff，明确 downstream_target 与 release_execution_authorized: false。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-confirmed-release-delivery`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `66f607dd2167ff47674a24a52b3b537cbd227a6a1b4a574ecfef674b38f3633c` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-confirmed-release-delivery`.
- Fixture SHA-256: `66f607dd2167ff47674a24a52b3b537cbd227a6a1b4a574ecfef674b38f3633c`
- Prompt SHA-256: `5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `299c765e24bed3d47cd5f1165cb4e7dae973e90fb9c91e1e5e35950ac2fddd9f`
- Skill overlay SHA-256: `62aaaf9c8c05eac4d9d569c35ab001e055f2ecdc527f1e0c77f6bdc4eedf1246`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6ba71c78dee7f69b879178b4307965fc8b664b773fca948482dc1711c289b5ad`
- Metadata SHA-256: `281089e0eacfd344cee9623295c4741f90652b2ae8ae709447ae5189db5a2ee5`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `delivers_confirmed_release_page` | PASS | with_skill 的 delivery_snapshot 包含 docs/site/release-notes/v1.0.0.md；正文覆盖六类确认事实，frontmatter 合法，且 last_verified_version 为 unverified。 |
| `updates_derived_surfaces_after_confirmation` | PASS | 确认记录确认 v1.0.0 及完整正文；git_diff 仅更新 release-notes/index.md 与 .meta/releases.json，保留 v0.9.0 和 manualNote，未修改导航。 |
| `passes_host_docs_checks` | FAIL | with_skill 明确报告 npm run test:docs 未通过，原因是无法推导 Git strict base/执行 Git 子进程；因此不满足全部权威 checks 通过。 |
| `returns_complete_ready_handoff` | FAIL | 输出明确将 handoff 标为 blocked、尚不能报告 ready，且未提供要求的完整 docs-agent:docs-audit pre-tag ready 字段集合。 |
| `preserves_external_release_boundary` | PASS | git_evidence 显示无新提交、无 ref/tag 变化；delivery_snapshot 保持 last_verified_version 为 unverified，verifiedDocs 未加入 v1.0.0；输出未声称 GitHub Release、部署或盖章。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=66f607dd2167ff47674a24a52b3b537cbd227a6a1b4a574ecfef674b38f3633c; output_sha256=2ec10ed70c52cda74350141d18e5969469730a557934727f3d8d616ae8b7d6c9; snapshot_sha256=0ebb7d2d1171c52f3268d0af45deae542a45b34b0ad4b759194d799e4f11744a
- Behavior: 正确完成站内内容及派生面更新并保持发布边界，但权威 docs checks 未通过，handoff 为 blocked 而非 ready。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=66f607dd2167ff47674a24a52b3b537cbd227a6a1b4a574ecfef674b38f3633c; output_sha256=a0c6378a8c94e6c3f6725108d2ba0598d876a376806d5646bbfd79ac46169b5e; snapshot_sha256=29fe99a30313e21f5cb4b28c5c098e1c1c9de0708429437fb7a6798d8f6845c7
- Behavior: 完成页面、索引和 metadata 更新，但 test:docs 未全绿；未提供结构化 pre-tag handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- passes_host_docs_checks
- returns_complete_ready_handoff
- Next: 在具备正常 Git/临时目录权限的环境中重新执行宿主 docs checks。
- Next: 由 docs-audit 生成完整的 pre-tag ready handoff，并保持 release_execution_authorized: false。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-confirmed-release-delivery`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `66f607dd2167ff47674a24a52b3b537cbd227a6a1b4a574ecfef674b38f3633c` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-confirmed-release-delivery`.
- Fixture SHA-256: `66f607dd2167ff47674a24a52b3b537cbd227a6a1b4a574ecfef674b38f3633c`
- Prompt SHA-256: `5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2da7831c1e3b626979a3601984870e16015610b54d1ff8f08ff8c14d15f812ca`
- Skill overlay SHA-256: `d552bdbf1aa95d384d7132b02e78e69678457f53a15c3f49ddfae00094ce8ee0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6ba71c78dee7f69b879178b4307965fc8b664b773fca948482dc1711c289b5ad`
- Metadata SHA-256: `281089e0eacfd344cee9623295c4741f90652b2ae8ae709447ae5189db5a2ee5`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `delivers_confirmed_release_page` | PASS | with_skill 的 v1.0.0 页面包含六个证据类别章节、六个证据链接；frontmatter 合法，且 last_verified_version 保持 unverified。 |
| `updates_derived_surfaces_after_confirmation` | FAIL | 确认后正确更新了 index、latest 和 released，并保留 manualNote；但额外将 v1.0.0 写入 verifiedDocs。按规范该页面尚未完成 formal documentation audit，不能被标记为已验证。 |
| `passes_host_docs_checks` | FAIL | 宿主规范要求在 docs/site 执行 npm run test:docs 且全部成功；with_skill 明确报告该命令因无 committed base 被阻塞，未通过完整检查。 |
| `returns_complete_ready_handoff` | FAIL | 输出明确为 blocked，未提供字段完整的 ready handoff，且缺少明确的 downstream_target 与 release_execution_authorized: false。 |
| `preserves_external_release_boundary` | FAIL | 虽未报告 GitHub Release、tag、部署或修改 last_verified_version，但 diff 将 v1.0.0 加入 verifiedDocs，越过了 docs-audit 的验证边界。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=66f607dd2167ff47674a24a52b3b537cbd227a6a1b4a574ecfef674b38f3633c; output_sha256=e36571bfcf20f4c1cb1607d5fd4d9449112d524b13da2016d144ff3599cab3ef; snapshot_sha256=35b8c825f382c905c7c87758e540fd4f6121656d4e0468cec10ca949f0acd3d2
- Behavior: 生成并确认了完整页面，正确保持页面 unverified、未修改导航；但将页面写入 verifiedDocs，完整 npm run test:docs 被阻塞，输出为 blocked 而非字段完整的 ready handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=66f607dd2167ff47674a24a52b3b537cbd227a6a1b4a574ecfef674b38f3633c; output_sha256=60c563b29460a25b688210f17ec391eb84be5106dc708514fb1e61016150ad27; snapshot_sha256=6a8eded80556869b68c537202ab5db3f7ca76b971c1a9fa918318bd81e022175
- Behavior: 生成了完整页面并更新 index/latest/released，保留 unverified 和宿主字段；声称使用显式 HEAD 通过检查，但未形成完整 handoff，且未更新 verifiedDocs。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 将尚未完成 docs-audit 的 v1.0.0 写入 verifiedDocs。
- with_skill 未通过完整宿主文档检查。
- with_skill 未返回完整的 pre-tag ready handoff。
- Next: 在具备有效 Git 基线的 docs/site 工作目录重新执行 npm run test:docs。
- Next: 移除 verifiedDocs 中对 v1.0.0 的条目，待 docs-audit 完成后再登记。
- Next: 补充 downstream_target 与 release_execution_authorized: false 的完整 handoff。

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
- Eval: `eval-004-confirmed-release-delivery`
- Scenario: 维护者已确认目标版本与完整正文后的站内 Release Notes 成功交付
- Review context: PR #187 follow-up for issue #177

## Test Set / Fixture Version

- Fixture version: `confirmed release delivery v1`
- Validation time: `2026-07-29`（历史轮；本轮 #238 重跑来源见 Latest Result 块）
- Runtime: `tmp/eval-runs/issue-177/rng-eval-004/`
- 两条 candidate 使用同一 prompt 与独立 pristine fixture；with-skill 只额外读取
  Docs Agent 与目标 skill 协议，without-skill 未读取或应用 skill、Agent README、
  eval metadata、assertions、comparison、with-skill 输出或历史 lane。
- 独立 judge 读取 assertions、源 fixture 与两条当前 lane 产物逐条判定；候选运行时
  不可见 assertions。

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `PARTIAL`（with）/ `PARTIAL`（without）— 宿主检查因依赖缺失未执行
- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `PARTIAL`
- without_skill：Behavior `FAIL` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `delivers_confirmed_release_page` | PASS | PASS | 两条 lane 均生成 `docs/site/release-notes/v1.0.0.md`，包含六个证据章节；frontmatter 含 `doc_type: release` 且 `last_verified_version: unverified`。 |
| `updates_derived_surfaces_after_confirmation` | PASS | FAIL | with_skill 的 `releases.json` 保留 `v0.9.0` 验证记录并保留 `manualNote`；without_skill 额外写入 `verifiedDocs["release-notes/v1.0.0.md"] = "v1.0.0"`，与页面仍为 `unverified` 矛盾。 |
| `passes_host_docs_checks` | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 的 `npm run test:docs` 都因缺少 `fast-glob` 未启动完成；这是 runner 依赖阻塞，不是 skill 行为失败。 |
| `returns_complete_ready_handoff` | FAIL | FAIL | 两条 lane 只有非结构化结果摘要，均未完整提供 `downstream_target`、`release_execution_authorized: false`、确认来源、实际更新面等完整 handoff 字段。 |
| `preserves_external_release_boundary` | PASS | PASS | 两条 lane 均未创建或发布 GitHub Release、未创建 tag；页面和 index 保持 `last_verified_version: unverified`，并明确未授权外部发布或等待文档审计。 |

未满足断言（with/without 任一 FAIL）：``updates_derived_surfaces_after_confirmation``、``returns_complete_ready_handoff``

未触发断言：`passes_host_docs_checks`。

基础设施阻塞说明：依赖缺失（fast-glob 等）；对应断言不构成 skill 行为回归。



## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `delivers_confirmed_release_page` | PASS | FAIL | 两侧均覆盖六类证据；with-skill 保持 `last_verified_version: unverified`，baseline 提前写入 `v1.0.0`。 |
| `updates_derived_surfaces_after_confirmation` | PASS | FAIL | with-skill 按新到旧更新 index，追加 metadata 且保留旧版本、旧 `verifiedDocs` 与 `manualNote`；baseline 提前登记 verifiedDocs、盖章 index，且索引顺序错误。 |
| `passes_host_docs_checks` | PASS | PASS | 两侧均在 `docs/site` 执行锁定依赖安装及权威 `npm run test:docs`，最终 75/75 tests、退出码 0。 |
| `returns_complete_ready_handoff` | PASS | FAIL | with-skill 输出完整 `docs-agent:docs-audit / pre-tag` ready handoff；baseline 缺少明确 handoff/downstream target、next gate、更新面、blockers 与 `release_execution_authorized: false`。 |
| `preserves_external_release_boundary` | PASS | FAIL | 两侧均未执行外部发布操作；baseline 仍越权完成页面、index 和 `verifiedDocs` 盖章。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 生成 `docs/site/release-notes/v1.0.0.md`，完整保留用户功能、架构、数据库、
  部署配置、交付资产、升级兼容与风险六类证据。
- 页面应用合法 release frontmatter，审计前保持
  `last_verified_version: unverified`。
- 确认记录成立后更新 Release Notes index 与 release metadata，不手工修改自动
  生成导航，不覆盖既有版本、verifiedDocs 或宿主自有字段。
- 最终 `npm run test:docs` 通过：75/75 tests，退出码 0。
- 输出字段完整的 pre-tag ready handoff，并明确
  `downstream_target: pm-agent:github-release-gen` 与
  `release_execution_authorized: false`。
- 未执行 GitHub Release、tag、部署、镜像操作、Git 写入或 docs-audit 盖章。
- Response SHA-256:
  `39f842d0317c1fdce8182598600a5ae2811691236a5d1600a5e1286f2c5878b0`。

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- baseline 能生成六类证据正文、更新 index/metadata，并真实通过宿主 docs checks。
- baseline 把页面和 index 的 `last_verified_version` 提前写成 `v1.0.0`，同时把
  新页面加入 `verifiedDocs`，越过 docs-audit 盖章时序。
- baseline 的 index 未保持宿主要求的新到旧排序；handoff 虽表达 ready_for_audit，
  但缺少完整目标、授权边界、更新面与 blockers 字段。
- Response SHA-256:
  `d049d1f7a8d878c4f26acb4044d621e34f369ad0ffe2c5acae8b0b249a0f38d7`。

## Failures And Limitations

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- With-skill assertion failures: none.
- Infrastructure or credential blockers: none.
- Baseline failures: 审计前盖章、派生面排序/verifiedDocs 错误、pre-tag handoff
  字段与授权边界不完整。
- 当前 fixture 在候选启动前已保存维护者对完整正文事实类别的确认，因此能验证
  确认后的正确 delta，但“确认前派生面零变化”依赖源 fixture 初态与最终差异作
  间接判定；交互式确认时序继续由既有 confirmation-gate eval 覆盖。
- lane 的读取隔离依据 run log 和产物边界，不是操作系统级 file-access audit。

## Next Steps

- 保留本用例作为成功交付路径回归，继续由 eval-001/002/003 覆盖入口版本确认、
  正文确认和站点 foundation 门禁。
- 每次运行从只读源 fixture 重建 lane workspace，不原地复用已修改的 index 或
  release metadata。

## Runtime Artifact Policy

- 当前 lane 的 workspace、依赖、生成站点、response、handoff、run log、judge
  verdict 与作废轮次只保留在 `tmp/eval-runs/issue-177/rng-eval-004/`，不提交。
- 只提交 eval 定义、fixture、metadata 与本 durable `comparison.md`。
