# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-004-catalog-mapped-billing-feature`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-004-catalog-mapped-billing-feature`.
- Fixture SHA-256: `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa`
- Prompt SHA-256: `18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e4cd9b0e262233f5d6a944962f6bf7c4c1323776752d0c1e41ea8bac4c33f829`
- Skill overlay SHA-256: `3f39f62240fb387c41fff7ebe0f42bb66e13cd2eda97d0b2c78636c06bb45d87`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8d7030970f6fab5f1056baaa7f97792f12e093b11e3211055d5ae790cf0d3bc2`
- Metadata SHA-256: `b6e639db89ad7dc9c01b74ff5037844027a7f93b1a684864779b0328b14ee4bc`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | with_skill 输出声称按 change-map 读取 billing.md，但锁定的原始证据无法证明实际读取顺序或未遍历无关文档。 |
| `verifies_against_code` | PASS | 明确以 src/billing/service.txt 为代码依据，指出代码仅声明 monthly，而 docs/site/api/billing.md:13 声称支持 monthly 和 annual，并说明年付不能确认。 |
| `treats_unverified_as_low_trust` | PASS | 明确将 last_verified_version: unverified 视为不能单独证明实现，并将订阅创建列为低置信度、年付列为待核实项。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=62b9a20c6148cc4c8c4a16e742be859cb093308b3965e60f697fe05924dc7c8d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 输出了带证据、置信度和待确认事项的功能目录草案，回到代码核证了年付差异，并谨慎处理未验证文档。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=4262ec26fabe173eda3d05b75ed7c263baa6e8fd31fe4c58e9e174037703c3b2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了较完整的功能盘点，并识别月付代码事实与年付文档声明的差异。
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

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-004-catalog-mapped-billing-feature`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-004-catalog-mapped-billing-feature`.
- Fixture SHA-256: `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa`
- Prompt SHA-256: `18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c7dc67ac03b6fbf2bf69bb7af239cc79636a61220df238e51a6c8f891a2b2bbf`
- Skill overlay SHA-256: `5fabe64a432e7077b010b055323ac846ade69c047e7f21a1ce71459e61d31a42`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8d7030970f6fab5f1056baaa7f97792f12e093b11e3211055d5ae790cf0d3bc2`
- Metadata SHA-256: `b6e639db89ad7dc9c01b74ff5037844027a7f93b1a684864779b0328b14ee4bc`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill explicitly follows change-map.yaml for src/billing/** and identifies/reads docs/site/api/billing.md; no unrelated document content is used. |
| `verifies_against_code` | PASS | with_skill cites src/billing/service.txt:1-2 as the code authority, contrasts monthly-only code with billing.md:13's monthly-and-annual claim, preserves both paths and the resulting conflict/impact. |
| `treats_unverified_as_low_trust` | PASS | with_skill explicitly treats last_verified_version: unverified as unconfirmed, assigns low confidence, and keeps annual subscription as a verification item rather than an implemented capability. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=8016e7da31144c675f9cf8d59912182a7bdebf3a67c8d530d0fceb023190fab3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Uses the change map, reads the mapped billing documentation, verifies claims against service.txt, and conservatively marks unverified annual support as low confidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=65c7b4c4ff1da322d704add95f6ba54cb0118c2aa35a177201f5a9db42b9a501; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a generally accurate inventory and recognizes the annual-plan documentation/code conflict, but does not demonstrate the mapped-document-first workflow or the same structured low-trust handling.
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

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-004-catalog-mapped-billing-feature`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-004-catalog-mapped-billing-feature`.
- Fixture SHA-256: `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa`
- Prompt SHA-256: `18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `807b576a5130a49581d58f258e32f9a7f916850f2f335e3a48ede3a7886a942b`
- Skill overlay SHA-256: `96eaf3768827f13d232245de107b17f5e814bef969da3eb231f62d9287d9d070`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8d7030970f6fab5f1056baaa7f97792f12e093b11e3211055d5ae790cf0d3bc2`
- Metadata SHA-256: `b6e639db89ad7dc9c01b74ff5037844027a7f93b1a684864779b0328b14ee4bc`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill 明确说明依据 change-map.yaml 关联读取 docs/site/api/billing.md，并仅围绕相关代码、映射文档和 API 文档组织盘点。 |
| `verifies_against_code` | PASS | with_skill 以 src/billing/service.txt 为直接事实来源，指出代码为 operation=create_subscription、supported_plan=monthly，并与 docs/site/api/billing.md 声称支持 monthly 和 annual 的内容对照，明确年付未被代码证实。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 明确指出文档 last_verified_version=unverified，且将年付仅作为未验证声明；最终确认范围回到代码中的订阅创建和月度计划。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=b24d9f9cdd76469b73589b04e132d574cfacd4baa0ae8e9e1d8614ee2d2984cb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 按映射关联文档，并以代码核证文档声明，明确区分已确认的月付订阅创建与未验证的年付声明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=32d894438c31002859d14023e38c6f949eac34e2e5c5abf1ac5ba9a568ec63dd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了月付代码事实和未验证的年付文档声明，但未体现先依据 change-map 读取映射文档的流程，盘点也较泛化。
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
