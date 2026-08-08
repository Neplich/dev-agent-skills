# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b1af296f57c9472641aa2fbf552cc05b76e8658e900bc4d5f0a34e60133977ab` from `agents/docs/test/docs-audit/evals/workspace/eval-008-pre-tag-success`.
- Fixture SHA-256: `b1af296f57c9472641aa2fbf552cc05b76e8658e900bc4d5f0a34e60133977ab`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9e8cd9d72ce0e98552272f26978823af26e642ab29487b2f1519c46898c21493`
- Metadata SHA-256: `8bf9eed51fb7f0c370d32001c1771329090952db5672ea9c398b67465aa72d50`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | with_skill records base_ref, target_ref, confirmed v1.2.0, and absent tag; it blocks for missing handoff/inventory rather than tag absence. |
| `verifies_complete_set_and_surfaces` | FAIL | It verifies the four listed pages, but does not establish the complete required surface set or successful handoff, metadata, and host-version verification. |
| `normalizes_mixed_version_forms` | FAIL | It notes an incomplete version-source inventory and does not demonstrate required raw-form validation, normalization, or SemVer equality. |
| `records_pre_stamp_values` | PASS | It records the exact required pre-stamp values for all four pages. |
| `stamps_complete_set_atomically` | NOT_EXERCISED | The output explicitly says no document fields were modified because the audit was blocked. |
| `builds_isolated_candidate_transaction` | NOT_EXERCISED | No isolated candidate transaction or temporary build is reported; the audit stopped before construction. |
| `candidate_record_has_no_ready_result` | NOT_EXERCISED | No candidate record was created or reported. |
| `validates_two_complete_staged_gates` | NOT_EXERCISED | No staging, raw metadata gate, or candidate replacement gate was performed. |
| `confirms_anchor_commit_before_discovery` | NOT_EXERCISED | No anchor commit or post-stamp confirmation was created. |
| `persists_fixed_discovery_handoff` | NOT_EXERCISED | The output explicitly says no audit record or handoff was created. |
| `returns_ready_only_after_integration` | NOT_EXERCISED | Integration and downstream ready handoff were not reached because the audit was blocked. |
| `returns_ready_for_tag_not_published` | FAIL | The output returns blocked rather than the required pre-tag ready_for_tag result. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=b1af296f57c9472641aa2fbf552cc05b76e8658e900bc4d5f0a34e60133977ab; output_sha256=398e5f83753be86170ff333d79b71d66251164b780867e05af976ee7880965be; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepted the confirmed pre-tag version and absent tag, verified the four listed pages and pre-stamp values, then blocked on missing release-notes handoff and incomplete version-source inventory.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=b1af296f57c9472641aa2fbf552cc05b76e8658e900bc4d5f0a34e60133977ab; output_sha256=2b16be09888ad63a1d710e91fccfe240755b1009b7b08ef88744e422973f9abb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline misclassified the release metadata as a blocking publication conflict and did not perform the required audit workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The complete required surface and source-normalization verification were not demonstrated.
- The required ready_for_tag result was not returned.
- Next: Provide the required Release Notes handoff and complete version-source inventory, then rerun the full pre-tag workflow.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `588924b9e745bd0282560429ce305f14ce4c254eb94edfc5269a128aff4ece1b` from `agents/docs/test/docs-audit/evals/workspace/eval-008-pre-tag-success`.
- Fixture SHA-256: `588924b9e745bd0282560429ce305f14ce4c254eb94edfc5269a128aff4ece1b`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9e8cd9d72ce0e98552272f26978823af26e642ab29487b2f1519c46898c21493`
- Metadata SHA-256: `8bf9eed51fb7f0c370d32001c1771329090952db5672ea9c398b67465aa72d50`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | with_skill 明确记录 base_ref、target_ref、维护者确认的 v1.2.0，并确认同名 tag 不存在且未因此阻塞。 |
| `verifies_complete_set_and_surfaces` | FAIL | 虽列出两张 API 页面及两份 Release Notes 为 verified，但未验证 release-notes-gen handoff，且将 .meta/releases.json 的状态矛盾作为阻塞。 |
| `normalizes_mixed_version_forms` | FAIL | 仅记录 v1.2.0，未分别核对带 v、无 v 的来源形态并规范化比较。 |
| `records_pre_stamp_values` | FAIL | 未在审计结果中逐页记录四页的盖章前值。 |
| `stamps_complete_set_atomically` | FAIL | 明确表示未执行统一 stamp。 |
| `builds_isolated_candidate_transaction` | FAIL | 未构建隔离 candidate 事务，也未提供相关工作树、分支或 index 证据。 |
| `candidate_record_has_no_ready_result` | FAIL | 未生成 candidate record。 |
| `validates_two_complete_staged_gates` | FAIL | 未执行初稿和最终 candidate 的完整 raw metadata gate。 |
| `confirms_anchor_commit_before_discovery` | FAIL | 未创建或确认 post-stamp anchor commit。 |
| `persists_fixed_discovery_handoff` | FAIL | 未写入固定 discovery handoff。 |
| `returns_ready_only_after_integration` | FAIL | 未进行临时分支集成、handoff 回读或 CAS 条件验证。 |
| `returns_ready_for_tag_not_published` | FAIL | 结果为 blocked，未返回 ready_for_tag。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=588924b9e745bd0282560429ce305f14ce4c254eb94edfc5269a128aff4ece1b; output_sha256=a45a3c4acd5b72016a062f78253ede63f0a4de14dc1e8fe824dd0ba8cb82ed48; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确接受已确认版本和不存在的 tag，并识别影响页面；但因 handoff、版本源清单和发布元数据问题错误阻塞，未完成 pre-tag 事务或返回 ready_for_tag。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=588924b9e745bd0282560429ce305f14ce4c254eb94edfc5269a128aff4ece1b; output_sha256=e235a73d9646053f8c746bfa2b819574c83f013b509a71e85d091be8fba89804; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别 refs、版本和缺失 tag，但错误地将 .meta/releases.json 的预发布状态作为阻塞。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- verifies_complete_set_and_surfaces
- normalizes_mixed_version_forms
- records_pre_stamp_values
- stamps_complete_set_atomically
- builds_isolated_candidate_transaction
- candidate_record_has_no_ready_result
- validates_two_complete_staged_gates
- confirms_anchor_commit_before_discovery
- persists_fixed_discovery_handoff
- returns_ready_only_after_integration
- returns_ready_for_tag_not_published
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

- Behavior result: `PASS`（with）/ `PASS`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `PARTIAL`（with）/ `PARTIAL`（without）— Git 缺失导致 pre-tag 成功路径未执行
- Overall result: BLOCKED
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `PARTIAL`
- without_skill：Behavior `PASS` / Coverage `PARTIAL`

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
| returns_ready_for_tag_not_published | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 均因无 Git 无法进入 pre-tag 成功事务，正确停在 `blocked`；成功态 `ready_for_tag` 未执行。 |

未触发断言：除 `accepts_confirmed_version_without_tag` 外的 11 条成功路径断言。

基础设施阻塞说明：Git 仓库缺失；对应断言不构成 skill 行为回归。



## Fixture Drift Notice

fixture 身份文本已于 2026-07-29 从 issue 编号更新为 skill 名，旧 PASS 反映变更前 run。**2026-08-03（#188）已对当前 fixture 完成 fresh re-baseline**（with/without 双侧验证，judge 独立判定，证据见 `tmp/eval-runs/issue-188-docs/`），BLOCKED 状态消解；本节保留作为历史记录。

## Historical results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 2026-07-20（fixture 身份文本变更前）：旧 run 结果，按 Fixture Drift Notice 不再作为当前证据。

## Canonical digest verification

> ⚠️ 本节为 2026-08-03 #188 历史轮执行证据；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

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

> ⚠️ 本节为 2026-08-03 #188 历史轮后续建议；当前 #238 重跑因 Git 仓库缺失保持 `BLOCKED`。

No skill change is required. Preserve exact canonical inventory fields and
ordering, actual-tag pending semantics, genesis bytes `[]`, and the guarded
post-FF CAS rollback language in future protocol edits.

## Runtime artifact policy

> ⚠️ 本节仅描述 2026-08-03 #188 历史轮运行产物；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Runtime artifacts（双侧 candidate、judge verdict、隔离目录执行产物）在本次 fresh re-baseline 中真实生成，位于被 gitignore 覆盖的 `tmp/eval-runs/issue-188-docs/`；未提交到 git。长期 durable 产物仅为本 `comparison.md`。
