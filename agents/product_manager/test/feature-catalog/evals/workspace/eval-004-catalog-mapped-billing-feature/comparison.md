# Consumption Regression Comparison

## Latest Fresh Evaluation — 2026-08-07

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-004-catalog-mapped-billing-feature`
- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: FAIL — 2/3 assertions passed.
- Coverage result: FULL — all 3 assertion scenarios were exercised.
Overall result: FAIL

### Assertion Results

- `reads_mapped_docs_first`: FAIL — the tool trace read `service.txt` and enumerated files before reading `change-map.yaml` and the mapped billing page.
- `verifies_against_code`: PASS — code showed monthly only, and the response preserved the annual-plan documentation conflict with its impact.
- `treats_unverified_as_low_trust`: PASS — the unverified page was treated as low trust and checked against code.

### With-Skill / Baseline Comparison

The with-skill response produced a pending, evidence-backed billing draft and correctly handled the document/code conflict, but violated the prescribed mapped-doc-first read order. The baseline showed the same ordering weakness.

### Failures / Next Steps

- From the task path, read `change-map.yaml`, then the mapped billing page, and only then return to `src/billing/service.txt` for verification.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-004-catalog-mapped-billing-feature/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Skill: `feature-catalog`
- Eval: `eval-004-catalog-mapped-billing-feature`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

**PASS** — with-skill 输出满足全部 3 条断言：精准读取映射文档、回到代码核证年付差异，并将 `unverified` 文档按最低信任处理。

## With-Skill Behavior

- 仅引用映射文档 `docs/site/api/billing.md` 与代码事实 `src/billing/service.txt`，未引入无关文档。
- 明确保留文档声明、代码事实、版本新鲜度与影响，未把年付列为已实现能力。
- 所有关键目录结论均由代码证据支撑，候选功能置信度保持为 `low`。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，使用同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 也识别了月付/年付差异及 `unverified` 风险，并回到代码核证；本 fixture 下未形成明显行为差距，但不影响 with-skill 全断言通过。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 扩展可增加无关文档干扰，以提高消费契约差异的辨识度。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
