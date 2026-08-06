# eval-008-pre-tag-success Comparison

## Evaluation target

- Agent: `docs-agent`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`
- Validation time: `2026-08-03 22:40:00 +0800`（fresh re-baseline，issue #188）
- Scope: full pre-tag candidate transaction, canonical inventory/genesis digests, actual-tag pending contract, two staged gates, anchor/discovery commits, integration readback, and post-FF CAS rollback.

## Test set and method

This is a fresh paired validation against the current 12 assertions. The
`with_skill` and `without_skill` runs (2026-08-03, #188) each started from their own pristine fixture copy in
isolated directories (`tmp/eval-runs/issue-188-docs/with_skill/` and `tmp/eval-runs/issue-188-docs/without_skill/`),
executed independently without reading each other's outputs. The `without_skill` baseline read only
the current eval definition, metadata, prompt, and fixture files, and did not read the Docs Agent README,
`docs-audit` skill instructions, prior comparison, or historical output. The `with_skill` run read
`agents/docs/skills/docs-audit/SKILL.md`, `agents/docs/skills/docs-audit/_internal/INSTRUCTIONS.md`, and
`agents/docs/README.md` before executing. The fresh judge then read the frozen bilateral candidates and
the assertions, and produced the verdict in `tmp/eval-runs/issue-188-docs/judge/verdict.md`.

## Latest result

Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
Overall result: BLOCKED
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `PARTIAL`
- without_skill：Behavior `FAIL` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| accepts_confirmed_version_without_tag | PASS | PASS | 两边均记录 `target_release_version: v1.2.0`、`base_ref: v1.1.0`、`target_ref: release-head`，并明确同名 tag 不存在；阻塞原因均为缺少 Git 仓库，而非 tag 不存在（两边 `result.txt` 第 5–11 行）。 |
| verifies_complete_set_and_surfaces | NOT_EXERCISED | NOT_EXERCISED | 未生成正式审计报告；两边均因无法解析 refs 而阻塞，未逐页产出 `verified` 结果。 |
| normalizes_mixed_version_forms | NOT_EXERCISED | NOT_EXERCISED | 未生成包含完整版本来源 inventory 的审计记录；without_skill 仅声称静态版本一致，未核验 `.meta/releases.json`。 |
| records_pre_stamp_values | NOT_EXERCISED | NOT_EXERCISED | with_skill 明确“未写入审计报告、版本戳”；两边均无审计报告文件。 |
| stamps_complete_set_atomically | NOT_EXERCISED | NOT_EXERCISED | 两边均未执行版本戳写入；with_skill 明确未写入版本戳。 |
| builds_isolated_candidate_transaction | NOT_EXERCISED | NOT_EXERCISED | 未产生隔离 worktree、临时分支或 candidate 产物；两边均报告当前工作区不是 Git 仓库。 |
| candidate_record_has_no_ready_result | NOT_EXERCISED | NOT_EXERCISED | 未生成 candidate record；两边仅返回 `blocked`，无法验证 schema、digest、inventory 等完整字段。 |
| validates_two_complete_staged_gates | NOT_EXERCISED | NOT_EXERCISED | 未执行或记录初稿/最终 raw metadata gate，也无 staged candidate 文件。 |
| confirms_anchor_commit_before_discovery | NOT_EXERCISED | NOT_EXERCISED | 未创建 anchor commit；两边均无法验证提交树、diff、blob 类型和 refs。 |
| persists_fixed_discovery_handoff | NOT_EXERCISED | NOT_EXERCISED | 未生成 `docs/site/.meta/audit/handoffs/pre-tag-v1.2.0.md` 或 handoff commit。 |
| returns_ready_only_after_integration | NOT_EXERCISED | NOT_EXERCISED | 未进入临时分支集成、FF、回读或 CAS 恢复路径。 |
| returns_ready_for_tag_not_published | FAIL | FAIL | 断言要求 pre-tag 返回 `ready_for_tag`，但两边 `result.txt` 均明确返回 `blocked`，并写明“不能返回 `ready_for_tag`”。 |

未满足断言（with/without 任一 FAIL）：`returns_ready_for_tag_not_published`

基础设施阻塞说明：Git 仓库缺失；对应断言不构成 skill 行为回归。



## Fixture Drift Notice

fixture 身份文本已于 2026-07-29 从 issue 编号更新为 skill 名，旧 PASS 反映变更前 run。**2026-08-03（#188）已对当前 fixture 完成 fresh re-baseline**（with/without 双侧验证，judge 独立判定，证据见 `tmp/eval-runs/issue-188-docs/`），BLOCKED 状态消解；本节保留作为历史记录。

## Historical results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 2026-07-20（fixture 身份文本变更前）：旧 run 结果，按 Fixture Drift Notice 不再作为当前证据。

## Canonical digest verification

The with-skill run reconstructed the exact six-field inventory rather than
trusting the fixture literals. It sorted **6 entries** by `source_id`:
`actual_tag`, `host_package`, `release_index`, `release_metadata`,
`release_notes`, and `target_version`. Each object contains exactly
`source_id`, `locator_kind`, `locator`, `selector`, `extractor`, and
`required_raw_form`; compact RFC 8259 JSON uses sorted object keys, UTF-8, no
insignificant whitespace, and no trailing newline.

- Recomputed v1.2.0 inventory digest:
  `sha256:bd935efb92eedfb3facbfe867542687802159c700fa73dee1d2a896deac041a8`
- Fixture inventory digest:
  `sha256:bd935efb92eedfb3facbfe867542687802159c700fa73dee1d2a896deac041a8`
- Recomputed empty prior-lineage digest from exact bytes `[]`:
  `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- Fixture genesis digest:
  `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`

Both comparisons are exact matches. The `actual_tag` entry is
`git-ref / refs/tags/v1.2.0 / tag-name / git-tag-name-v1 / vX.Y.Z`; its
pre-tag value remains `pending_expected_absent`. Tag absence is expected and
does not represent publication or a failed version comparison.

## Assertion results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | without_skill | with_skill | Evidence summary |
| --- | --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | PASS | 双侧都分别记录 `v1.1.0`、`release-head` 与维护者确认的 `v1.2.0`，并把同名 tag 不存在视为正常 pre-tag 状态。 |
| `verifies_complete_set_and_surfaces` | PASS | PASS | 双侧均覆盖 change-map 命中的两张 API 页、release-notes handoff、Release Notes、索引、只读 releases metadata 与宿主版本；with-skill 逐页记录 target blob 和 verified 事实。 |
| `normalizes_mixed_version_forms` | PASS | PASS | 双侧均校验 `v1.2.0` 与 `package.json` 的 `1.2.0` 来源形态，并在规范化后判等。 |
| `records_pre_stamp_values` | FAIL | PASS | with-skill 精确记录四页章前值 `v1.1.0 / unverified / unverified / v1.1.0`，且页面未新增 `baseline_verified_version`；without-skill 只列最终 stamp，未持久化四个章前值。 |
| `stamps_complete_set_atomically` | PASS | PASS | 双侧实际四页均更新为 `v1.2.0` 且 releases metadata 未改；with-skill anchor commit 显示四页各只改一行 stamp 并与 candidate 同批提交。 |
| `builds_isolated_candidate_transaction` | FAIL | PASS | with-skill 存在从精确 target commit 建立的 `.git/audit-worktree-v1.2.0` 与独立 branch/index，宿主仅在最终 FF 后移动；without-skill 只是普通复制目录，无 worktree/target-tree index/宿主指纹证据。 |
| `candidate_record_has_no_ready_result` | FAIL | PASS | with-skill 固定 record 含完整逐页证据/hash、actual-tag pending inventory、canonical/prior-lineage digest、差异 inventory 与命令，且全文无 `ready_for_tag`、结果时间、anchor 或 post-commit 字段；without-skill record 缺完整 producer/gate/回读内容。 |
| `validates_two_complete_staged_gates` | FAIL | PASS | with-skill 留存 gate1 与最终 gate2 full-index patch，只含四张 100644 stamp 页和固定 candidate；without-skill 未执行或持久化两次 staged gate。 |
| `confirms_anchor_commit_before_discovery` | FAIL | PASS | with-skill anchor 的 parent 是精确 target，candidate blob、tree 与 target→anchor delta 均可回读，discovery 只在后续 commit 出现；without-skill 无 anchor 或 discovery。 |
| `persists_fixed_discovery_handoff` | FAIL | PASS | with-skill 固定 discovery 实际存在，含 phase/version/refs、`ready_for_tag`、时间、inventory digest、anchor/candidate identity、post-commit confirmation、preimage、current 与 lineage digest，handoff commit 只新增该 100644 blob；without-skill 无此产物与提交。 |
| `returns_ready_only_after_integration` | FAIL | PASS | with-skill 宿主分支最终同指 handoff commit，candidate 记录 FF 前指纹复核、FF 后 commit/tree/blob 回读及失败时 CAS 边界，随后才返回 ready；without-skill 未集成也未返回 ready。 |
| `returns_ready_for_tag_not_published` | FAIL | PASS | with-skill 最终为 `ready_for_tag`，并明确仅允许创建 tag、不是 published 或 `release_verified`；without-skill 仅返回 `candidate_verified`，不满足成功场景的阶段结果。 |

## With-skill behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

The skill-guided run validates the full affected set and release surfaces from
the exact target tree, applies the four-page stamp only after all evidence and
version identities pass, and builds a fixed-path candidate whose positive
conclusion is only `candidate_verified`. Its exact canonical inventory and
genesis digests match the fixture values; any mismatch would instead be
`blocked` and fail this eval.

Both staged gates inspect raw modes, object types, unfolded statuses, summary,
and full binary patch. Anchor confirmation precedes discovery; the discovery
handoff is committed separately and anchored by an external package. The host
branch is fast-forwarded only if its ref and captured worktree/index
fingerprints remain unchanged. Final authority appears only after integrated
commit/tree/discovery-blob readback.

If that readback fails after fast-forward, rollback to `target_ref` is allowed
only when compare-and-swap proves the branch still equals the just-integrated
handoff commit. The process then restores and verifies every captured
fingerprint. A concurrent move is never overwritten: the result remains
`blocked`, names the residual ref/commit and exact maintainer recovery command,
and prohibits tag creation.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `with_skill`: none。
- `without_skill`: 4/12 PASS（accepts_confirmed_version_without_tag、verifies_complete_set_and_surfaces、normalizes_mixed_version_forms、stamps_complete_set_atomically）；其余 8 条 FAIL（records_pre_stamp_values、builds_isolated_candidate_transaction、candidate_record_has_no_ready_result、validates_two_complete_staged_gates、confirms_anchor_commit_before_discovery、persists_fixed_discovery_handoff、returns_ready_only_after_integration、returns_ready_for_tag_not_published）——隔离事务、双 staged gate、anchor/discovery、FF 集成与阶段结果语义保持 with-skill 专属增量。

## Next steps

No skill change is required. Preserve exact canonical inventory fields and
ordering, actual-tag pending semantics, genesis bytes `[]`, and the guarded
post-FF CAS rollback language in future protocol edits.

## Runtime artifact policy

- Runtime artifacts（双侧 candidate、judge verdict、隔离目录执行产物）在本次 fresh re-baseline 中真实生成，位于被 gitignore 覆盖的 `tmp/eval-runs/issue-188-docs/`；未提交到 git。长期 durable 产物仅为本 `comparison.md`。
