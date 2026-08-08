# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-007-frontmatter-contract-fixtures`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f` from `agents/docs/test/docs-audit/evals/workspace/eval-007-frontmatter-contract-fixtures`.
- Fixture SHA-256: `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f`
- Prompt SHA-256: `49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6bde344495a08502946e81bb93f2ae1c40e1aff64c95e853b673dd5a307e9ade`
- Metadata SHA-256: `ac5c625c3b447eed92814a4915de66331bf3c2449cbef00676c3c687ad5d80de`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | 接受 release-entry.md 中确认的 v0.4.0、base_ref 4a1b2c3、target_ref 7c9e2af、pre-tag 阶段和证据清单。 |
| `rejects_standard_doc_type` | PASS | 将 catalog-search.md 因 doc_type: standard 不在允许枚举中判为 stale。 |
| `rejects_empty_related_code` | PASS | 将 catalog-export.md 因 related_code: [] 判为 stale。 |
| `rejects_missing_last_verified_version` | PASS | 将 catalog-status.md 因缺少必需的 last_verified_version 判为 stale。 |
| `rejects_empty_owners` | PASS | 将 catalog-bulk-update.md 因 owners: [] 判为 stale。 |
| `accepts_valid_api_page` | FAIL | 虽核对了 catalog-items.md 和 routes.txt，但将该页面判为“未完成验证，阻塞”，未确认其七个必填字段和值合法并通过 frontmatter 校验进入事实层。 |
| `blocks_release_for_invalid_frontmatter` | PASS | 将四个非法页面保留为 stale，结论为 blocked，并明确不能返回 ready_for_tag 或执行统一版本戳更新。 |
| `uses_shared_contract_source` | FAIL | 未明确以 docs-agent 的 frontmatter-contract.md 为判定真源，也未确认与 docs-site-bootstrap 的 check-frontmatter.mjs 逻辑一致。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=9607fb23554bb8d43dd7f789eb88039da2a4a8b25caf7d564eb5391a6212b8fd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确接受审计入口并识别四个非法页面、代码证据缺口及 blocked 结果，但未接受合法 catalog-items 页面进入事实层，也未明确共享合同真源。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=7e6b2e61a131daca2632073a9ad425c5fc8d2168db9ff5638039c64152b3a294; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出 NO-GO、若干 frontmatter 和证据问题，但未给出 blocked 阶段结论，也未完整执行合同层审计。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- accepts_valid_api_page 未满足对 catalog-items.md 七个必填字段合法性、frontmatter 通过及进入事实层的确认。
- uses_shared_contract_source 未提及 frontmatter-contract.md 或 check-frontmatter.mjs 的同源一致性。
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
- Eval: `eval-007-frontmatter-contract-fixtures`

## Test Set / Fixture Version

- Fixture version: docs-audit A3 / 2026-08-05
- Assertions: 8

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

Overall result: FAIL

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | PASS | 两条 lane 均读取并采用 `release-entry.md` 中维护者确认的 `v0.4.0`、`4a1b2c3`、`7c9e2af`、pre-tag 请求及证据清单。 |
| `rejects_standard_doc_type` | PASS | PASS | 两条报告均将 `invalid-standard-doc-type.md` 判为 stale/失败；文件含 `doc_type: standard`。 |
| `rejects_empty_related_code` | PASS | PASS | 两条报告均将 `invalid-empty-related-code.md` 判为 stale/失败；文件含 `related_code: []`。 |
| `rejects_missing_last_verified_version` | PASS | PASS | 两条报告均将 `invalid-missing-last-verified-version.md` 判为 stale/失败；文件缺少 `last_verified_version`。 |
| `rejects_empty_owners` | PASS | PASS | 两条报告均将 `invalid-empty-owners.md` 判为 stale/失败；文件含 `owners: []`。 |
| `accepts_valid_api_page` | PASS | PASS | `valid-catalog.md` 七个必填字段均合法；其 API 声明与 `src/catalog/routes.txt` 的 `GET /catalog/items -> 200 {"items":[]}` 一致，两条报告均确认该页有效。 |
| `blocks_release_for_invalid_frontmatter` | PASS | FAIL | with_skill 明确结果为 `blocked`、不得 `ready_for_tag`，且未写入 stamp；without_skill 虽给出整体 NO-GO，但把合法页单独标为“通过”，构成断言禁止的局部盖章。 |
| `uses_shared_contract_source` | FAIL | FAIL | 两条 lane 都未能确认 `docs-agent` 的 `frontmatter-contract.md` 与 `check-frontmatter.mjs` 存在或同源一致；with_skill 明确报告“版本面证据缺失”。 |

未满足断言（with/without 任一 FAIL）：``blocks_release_for_invalid_frontmatter``、``uses_shared_contract_source``



## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | 从 `release-entry.md` 分别解析 `v0.4.0`、base `4a1b2c3`、target `7c9e2af`、pre-tag 请求和证据清单，未从 ref 推断版本。 |
| `rejects_standard_doc_type` | PASS | 在旧七项合法枚举契约下，`doc_type: standard` 不在合法枚举中，页面判 `stale`。 |
| `rejects_empty_related_code` | PASS | `related_code: []` 违反非空字符串数组契约，页面判 `stale`。 |
| `rejects_missing_last_verified_version` | PASS | 缺少无条件必填的 `last_verified_version`，页面判 `stale`。 |
| `rejects_empty_owners` | PASS | `owners: []` 违反非空字符串数组契约，页面判 `stale`。 |
| `accepts_valid_api_page` | PASS | 合法页七字段通过，并以 `routes.txt` 核对 GET/200/items 后判 `verified`。 |
| `blocks_release_for_invalid_frontmatter` | PASS | 完整集合含 4 个 stale，阶段 `blocked`，合法页保持 `unverified`，没有局部盖章。 |
| `uses_shared_contract_source` | PASS | 报告明确以 `frontmatter-contract.md` 为真源，并说明判定与 bootstrap 宿主 validator 应实现的共享契约一致；fixture 不含脚本，未虚构执行。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮成功 fresh rerun，证据位于 `tmp/eval-runs/117/eval-007-frontmatter-contract-fixtures/with_skill/`；首次并发尝试未产出最终候选，已从判定证据中排除。
- 候选只新增 `audit-v0.4.0.md`，未修复 fixture、修改页面 stamp 或创建 metadata。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮独立 fresh baseline，使用同一 prompt 与 pristine fixture，证据位于 `tmp/eval-runs/117/eval-007-frontmatter-contract-fixtures/without_skill/`；未复用历史 baseline。
- baseline 也得到 1 合法/4 stale 与 blocked，但零写入，且无法提供 docs-audit 入口 gate、共享契约真源和契约报告持久化的同等证据。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure。fixture 的合成 refs 不可解析且未附 patch；候选按维护者确认的 evidence inventory 复现影响集合并明确限制。本 eval 核心是入口与 frontmatter 契约，故为 harness 限制而非协议缺陷。

## Next Steps

- 使用当前包含 `manual` 的八项枚举契约重跑 fresh with-skill lane、同轮 fresh without-skill baseline 与独立 judge；验证后再替换 `BLOCKED`。

## Runtime Artifact Policy

- 本轮候选、transcripts、workspace 副本与失败尝试诊断仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
