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
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Fixture Drift Notice

fixture 身份文本已于 2026-07-29 从 issue 编号更新为 skill 名，旧 PASS 反映变更前 run。**2026-08-03（#188）已对当前 fixture 完成 fresh re-baseline**（with/without 双侧验证，judge 独立判定，证据见 `tmp/eval-runs/issue-188-docs/`），BLOCKED 状态消解；本节保留作为历史记录。

## Historical results

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

- `with_skill`: none。
- `without_skill`: 4/12 PASS（accepts_confirmed_version_without_tag、verifies_complete_set_and_surfaces、normalizes_mixed_version_forms、stamps_complete_set_atomically）；其余 8 条 FAIL（records_pre_stamp_values、builds_isolated_candidate_transaction、candidate_record_has_no_ready_result、validates_two_complete_staged_gates、confirms_anchor_commit_before_discovery、persists_fixed_discovery_handoff、returns_ready_only_after_integration、returns_ready_for_tag_not_published）——隔离事务、双 staged gate、anchor/discovery、FF 集成与阶段结果语义保持 with-skill 专属增量。

## Next steps

No skill change is required. Preserve exact canonical inventory fields and
ordering, actual-tag pending semantics, genesis bytes `[]`, and the guarded
post-FF CAS rollback language in future protocol edits.

## Runtime artifact policy

- Runtime artifacts（双侧 candidate、judge verdict、隔离目录执行产物）在本次 fresh re-baseline 中真实生成，位于被 gitignore 覆盖的 `tmp/eval-runs/issue-188-docs/`；未提交到 git。长期 durable 产物仅为本 `comparison.md`。
