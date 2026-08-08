# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-001-audit-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2` from `agents/docs/test/docs-audit/evals/workspace/eval-001-audit-mismatch`.
- Fixture SHA-256: `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2`
- Prompt SHA-256: `8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `fee749f35b3bf7110eb1c6f38c918db3407b1a46ffa3ff2613c15b835398219e`
- Metadata SHA-256: `23ce240f3f391bd560df8f9bbcf6e5d2ec76b8a3ffb73e38f416b3cdb2997a3a`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_mapped_page` | PASS | With-skill report maps src/catalog/** to docs/site/api/catalog.md based on the routes diff. |
| `classifies_direct_conflict_mismatch` | PASS | With-skill report records POST in the document, GET in src/catalog/routes.txt, evidence paths, user impact, and concludes mismatch. |
| `blocks_with_conflict_evidence` | PASS | With-skill result is blocked, cites the method conflict, requires documentation/version-surface remediation, and does not return ready_for_tag. |
| `does_not_stamp_blocked_set` | PASS | With-skill report states no page was stamped and no release metadata, candidate handoff, or tag was created or modified. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=c9658113cd41608c8e33495cb326508d5baf515c85cbef5403888429f78ed453; snapshot_sha256=83b673d9f70d108f49d095d6057bf496df9b75131473596dcdf1df1cf0629295
- Behavior: Produced and saved a bounded audit identifying the mapped page, direct mismatch, release-surface blockers, and no-stamp outcome.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=0059c0f11f1d25aedba0bcfff5a7277557756df91301c4b50fe341839dfbee85; snapshot_sha256=7fbdcb7a3d2fed6cef79652697d89569292e9755de9ca7a2d20db4735d023ad4
- Behavior: Identified the POST/GET conflict and stale verification version, but provided a less complete audit.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-001-audit-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2` from `agents/docs/test/docs-audit/evals/workspace/eval-001-audit-mismatch`.
- Fixture SHA-256: `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2`
- Prompt SHA-256: `8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `fee749f35b3bf7110eb1c6f38c918db3407b1a46ffa3ff2613c15b835398219e`
- Metadata SHA-256: `23ce240f3f391bd560df8f9bbcf6e5d2ec76b8a3ffb73e38f416b3cdb2997a3a`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_mapped_page` | PASS | with_skill 报告明确说明 src/catalog/** 命中 change-map，且将 docs/site/api/catalog.md 列入受影响正式页面。 |
| `classifies_direct_conflict_mismatch` | PASS | with_skill 报告保留文档 POST /catalog/items、代码证据 src/catalog/routes.txt 中的 GET /catalog/items，说明影响并将页面标为 mismatch。 |
| `blocks_with_conflict_evidence` | PASS | with_skill 报告阶段结果为 blocked，列出 API 方法冲突及修正文档、补齐版本来源等待办，明确不是 ready_for_tag。 |
| `does_not_stamp_blocked_set` | PASS | with_skill 报告明确 catalog.md remains at v1.0.0 and was not modified，且 releases.json 缺失、未执行统一版本标记或局部盖章。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=9a2ac0b51ed2e4fbaaa8848d79a018850aa530465b0f44fe3ab56a94d30df0e6; snapshot_sha256=6838804fd6ff1d25cdb60f5025e7b9ac63dc7d97187266ae27ce5bd1e941b3f8
- Behavior: Deterministically mapped the changed source to the formal page, verified the direct mismatch with evidence and impact, blocked the pre-tag audit, and avoided stamping.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=21dc2f1f228e47df265c86ea351bf9340d845a6faa3d93b044ca89d0b701edec; snapshot_sha256=016d3034cf000eee78358fb234effcd2ee255f42dac7ff725fa241632a44e8e9
- Behavior: Fresh baseline identified the POST/GET conflict and stale verification metadata, reported not ready, and saved a report.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-001-audit-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2` from `agents/docs/test/docs-audit/evals/workspace/eval-001-audit-mismatch`.
- Fixture SHA-256: `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2`
- Prompt SHA-256: `8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `fee749f35b3bf7110eb1c6f38c918db3407b1a46ffa3ff2613c15b835398219e`
- Metadata SHA-256: `23ce240f3f391bd560df8f9bbcf6e5d2ec76b8a3ffb73e38f416b3cdb2997a3a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_mapped_page` | PASS | With-skill report states the change-map maps src/catalog/** to docs/site/api/catalog.md and confirms the route file changed. |
| `classifies_direct_conflict_mismatch` | PASS | Report records POST in the document, GET in src/catalog/routes.txt, cites both paths, explains client impact, and concludes mismatch. |
| `blocks_with_conflict_evidence` | PASS | Report result is blocked, lists the POST/GET conflict, requires updating the API page and rerunning the audit, and explicitly says not to create the tag or return ready_for_tag. |
| `does_not_stamp_blocked_set` | PASS | Report records pre-stamp v1.0.0, states unified stamping cannot proceed, notes releases.json is absent, and instructs not to stamp documentation; git evidence shows no source or metadata changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=e1c893caccc7bade81d93956722e5d4ae22b61dc85f3e6a7a68bbda1393fbd3d; snapshot_sha256=352ed2817ed304d9145a1b3f86fd47ae98d0d8598f8cccd3817cd1fffb464672
- Behavior: Mapped the changed route to the required page, documented the evidence-backed mismatch and impact, blocked the pre-tag audit, and prevented stamping.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=907bc4dd98a5cd0f98747959426017a585846b57b47a95351ba3a1395e4de803; snapshot_sha256=cfe34adc4d607692625047ae71698e62dd29cb3bfe73d1b3bc10730707c93e5c
- Behavior: Identified the POST/GET mismatch and lack of version update, but did not establish the change-map impact or a blocked pre-tag audit workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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
- Eval: `eval-001-audit-mismatch`

## Test Set / Fixture Version

- Fixture version: docs-audit A2 / 2026-07-19
- Assertions: 4

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
| `includes_mapped_page` | PASS | PASS | 两条 lane 均确认 `src/catalog/routes.txt` 命中 `src/catalog/**`，并映射到 `docs/site/api/catalog.md`；with_skill 报告第 23–27 行，without_skill 报告第 48–50 行。 |
| `classifies_direct_conflict_mismatch` | PASS | PASS | 两条 lane 均保留文档 `POST /catalog/items`、代码 `GET /catalog/items`、证据路径及调用方影响，并将页面判为冲突；with_skill 报告第 38–46 行，without_skill 报告第 31–38 行。 |
| `blocks_with_conflict_evidence` | PASS | FAIL | with_skill 明确标记 `phase result: blocked`，列出冲突及修文档/核代码待办，且声明无 `ready_for_tag`；without_skill 仅给出 `FAIL`，未将阶段结果标记为 `blocked`，也未提出修文档或修代码的确认分支。 |
| `does_not_stamp_blocked_set` | PASS | PASS | with_skill 明确声明未执行版本 stamping；受审页面仍为 `last_verified_version: v1.0.0`，且不存在 `.meta/releases.json`。without_skill 同样显示页面仍为 `v1.0.0`，未生成版本同步文件。 |

未满足断言（with/without 任一 FAIL）：``blocks_with_conflict_evidence``



## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `includes_mapped_page` | PASS | `.eval/actual-diff.patch` 中的 `src/catalog/routes.txt` 命中 `src/catalog/**`，`catalog.md` 被纳入完整影响域。 |
| `classifies_direct_conflict_mismatch` | PASS | 报告并列保存 `POST /catalog/items`、`GET /catalog/items`、证据路径和调用影响，最终状态为 `mismatch`。 |
| `blocks_with_conflict_evidence` | PASS | 阶段结果为 `blocked`，要求负责方确认修文档还是修代码，未返回 `ready_for_tag`。 |
| `does_not_stamp_blocked_set` | PASS | 页面仍为 `v1.0.0`，未修改或创建 `.meta/releases.json`，没有局部盖章。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮 fresh session `019f7a73-2e16-7092-9d5d-a30bed3dd18c`，证据位于 `tmp/eval-runs/117/eval-001-audit-mismatch/with_skill/`。
- 候选写入契约路径 `docs/site/.meta/audit/audit-v1.1.0.md`，报告包含三项独立输入、影响域、冲突证据、blocker 和复核命令。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮独立 fresh session `019f7a77-66e9-7a00-a328-c2041378d9b0`，同一 prompt 与 pristine fixture，证据位于 `tmp/eval-runs/117/eval-001-audit-mismatch/without_skill/`；未复用历史 baseline。
- baseline 也识别冲突并阻塞，但报告写入非契约路径 `.eval/docs-audit-report.md`，结构化 release-surface 与审计协议证据较弱。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure。合成 refs 不在 Git object store 中，候选使用 fixture-authoritative `.eval/actual-diff.patch` 复现端点差异；这是已披露的 harness 限制，不是协议缺陷。

## Next Steps

- 保留本结果；docs-audit 冲突分类或 blocked 写入边界变化时重跑。

## Runtime Artifact Policy

- transcripts、候选输出、workspace 副本和 manifest 仅保留在 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
