# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-007-frontmatter-contract-fixtures`
- Fresh validation: `tmp/eval-runs/124-round3/eval-007-frontmatter-contract-fixtures/`

## Test Set / Fixture Version

- Fixture: `frontmatter-contract-v2`
- Entry basis: `release-entry.md` with pending release `v0.4.0`, base `4a1b2c3`, target `7c9e2af`, and a maintainer-confirmed evidence inventory
- Contract: `agents/docs/skills/docs-agent/_internal/_shared/frontmatter-contract.md`
- Assertions: 8

## Latest Result

**PASS — 8 / 8 assertions passed.**

上一轮 durable 结果虽为 PASS，但只记录了 7 条 assertions，且没有把 `release-entry.md` 的等效确认入口凭据作为独立 assertion 判定，入口凭据覆盖存在缺陷。本轮 fresh judge 使用更新后的原始 prompt、完整 fixture 和新增入口 assertion 重跑；with-skill 接受了 release entry，正确得到 `1 verified / 4 stale`，release blocked 且未局部盖章。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | with-skill 明确接受 `release-entry.md` 为有效等效入口，并解析 pending release `v0.4.0`、base `4a1b2c3`、target `7c9e2af`、two-dot 语义和证据清单。 |
| `rejects_standard_doc_type` | PASS | `invalid-standard-doc-type.md` 因 `doc_type: standard` 不在共享契约合法枚举中判为 `stale`。 |
| `rejects_empty_related_code` | PASS | `invalid-empty-related-code.md` 因 `related_code: []` 不是非空字符串数组判为 `stale`。 |
| `rejects_missing_last_verified_version` | PASS | `invalid-missing-last-verified-version.md` 因缺少无条件必填的 `last_verified_version` 判为 `stale`。 |
| `rejects_empty_owners` | PASS | `invalid-empty-owners.md` 因 `owners: []` 不是非空字符串数组判为 `stale`。 |
| `accepts_valid_api_page` | PASS | `valid-catalog.md` 的七个必填字段通过校验，并进入事实层；`GET /catalog/items`、`200` 和 `items` 数组均与 `src/catalog/routes.txt` 一致，最终 `verified`。 |
| `blocks_release_for_invalid_frontmatter` | PASS | 完整影响域保留四个 `stale` 页面，release 明确 blocked、不得 `proceed`，且不得给合法页局部盖章或更新 `.meta/releases.json`。 |
| `uses_shared_contract_source` | PASS | with-skill 明确以 docs-agent 的 `frontmatter-contract.md` 为真源，并实际对比 docs-site-bootstrap 内嵌 validator，确认七字段、枚举、非空数组和版本字段逻辑一致。 |

## With-Skill Behavior

- 来源：本轮独立 `codex exec`，工作目录为 `tmp/eval-runs/124-round3/eval-007-frontmatter-contract-fixtures/with_skill/`。
- Harness 提供完整 `agents/docs/README.md` 和 `agents/docs/skills/`，并提供 PM 共享 `skill-map.md` 与 `consumption-contract.md`；候选实际读取 docs-agent、docs-audit、docs-site-bootstrap 及其 `_internal`。
- 候选先验证等效入口，再应用共享 frontmatter 真源逐页分类，并将合法 API 页面送入事实层。
- 候选实际比较 bootstrap 内嵌 validator 与共享契约，补齐上一轮只证明分类结果、入口凭据未单列验证的证据缺口。

## Without-Skill Baseline

- 来源：本轮另一独立 `codex exec`，工作目录为 `tmp/eval-runs/124-round3/eval-007-frontmatter-contract-fixtures/without_skill/`；使用同一原始 prompt 和 fixture。
- Harness 未提供任何 Agent README、skill 文档或共享契约；baseline 明确声明未读取或应用这些材料。
- baseline 也从 fixture 的显著信号得到 1 个合法页、4 个非法页和 release blocked，但不能证明 `release-entry.md` 满足 docs-audit 的正式入口 gate，也不能证明审计端与 bootstrap 生成端同源。
- with-skill 的可观测增益是入口 gate、共享契约真源和生成端 validator 一致性均有可复核证据。

## Failures

- 本轮无 assertion failure。
- 隔离 fixture 不包含可解析的真实 Git refs，因此候选无法执行实际 `git diff`；`release-entry.md` 已明确确认 bounded base/target、two-dot 语义和证据清单，本 eval 只验证入口与 frontmatter 契约判定，此限制不影响 8 条 assertions。

## Next Steps

- 保留本结果。后续若修改 docs-audit 入口 gate、共享 frontmatter 契约或 bootstrap validator，使用同一完整 harness 重跑 eval-007，并重新生成 fresh without-skill baseline。

## Runtime Artifact Policy

- 候选结果与 transcripts 仅位于 `tmp/eval-runs/124-round3/eval-007-frontmatter-contract-fixtures/`，不提交到 git。
- Durable 结果仅为本 `comparison.md`；`candidate-output.md`、`transcript.txt` 和并发录制诊断均属于运行期产物。
