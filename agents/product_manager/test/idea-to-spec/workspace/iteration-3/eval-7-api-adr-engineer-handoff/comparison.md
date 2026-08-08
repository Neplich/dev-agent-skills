# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-007-api-adr-engineer-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116` from `agents/product_manager/test/idea-to-spec/workspace/iteration-3/eval-7-api-adr-engineer-handoff`.
- Fixture SHA-256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- Prompt SHA-256: `2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7638558b96730ed626879bcffd4a606d3ed390013a41acf29ade725d210e3f4e`
- Skill overlay SHA-256: `12aaaef0d075d133bbbdc681f598fd09807b211a4377dcfbc6cbbfcaa30909e0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `02e5d899a7687cd28d5b7fe3ed85f267cd9ce62f15d9844aa4281eff90859ac1`
- Metadata SHA-256: `6b28964c95e54c379988fdfd7c54f486a5c872824039a926ede4358e3117f378`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `does_not_use_pm_api_adr_generators` | PASS | With-skill output assigns generation to engineer-agent:trd-gen and states that the PM agent does not handle API/ADR. |
| `routes_to_trd_gen` | PASS | With-skill output explicitly names engineer-agent:trd-gen as the generator and next step. |
| `engineer_paths_mirror_feature_path` | PASS | With-skill output places API.md and ADR-001-search-index-strategy.md under docs/engineer/chat-interface/history-search/. |
| `handoff_contains_feature_path_evidence` | FAIL | The output includes feature_path and the PRD path, but omits parent_feature, feature_level, and explicit API/ADR decision-background evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=1a413d0f23493d5cd3c0cbe571ee6413ed52eee028affdaa4ed9345ba175fe83; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes work to engineer-agent:trd-gen and uses the required mirrored Engineer paths, but omits required handoff metadata and decision-background fields.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=71cb30057f5820f0389a8bf6f312b51ce77e5cda5820f8c8e8a46b368adc3b09; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Identifies separate API and ADR owners but routes outputs outside the required Engineer path and does not provide the required trd-gen handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- handoff_contains_feature_path_evidence is not satisfied: required parent_feature, feature_level, and API/ADR decision-background evidence are absent.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-007-api-adr-engineer-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116` from `agents/product_manager/test/idea-to-spec/workspace/iteration-3/eval-7-api-adr-engineer-handoff`.
- Fixture SHA-256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- Prompt SHA-256: `2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a2e446c3d8d5f02d34cd5e3954e55500a6eaf296bcb868f9d3dbe27d39c64b91`
- Skill overlay SHA-256: `14328c4af5595e19e21331fb22dcc6dda56844ee6c4f2ee6382997e7ffe0af37`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `02e5d899a7687cd28d5b7fe3ed85f267cd9ce62f15d9844aa4281eff90859ac1`
- Metadata SHA-256: `6b28964c95e54c379988fdfd7c54f486a5c872824039a926ede4358e3117f378`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `does_not_use_pm_api_adr_generators` | FAIL | 说明了不能由 PM 文档生成流程负责，但未明确指出 PM 内部 `api-gen` 或 `adr-gen` 不能直接生成。 |
| `routes_to_trd_gen` | PASS | 明确写出由 `engineer-agent:trd-gen` 负责 Engineer 文档阶段。 |
| `engineer_paths_mirror_feature_path` | PASS | API.md 和 ADR 文件均位于 `docs/engineer/chat-interface/history-search/`。 |
| `handoff_contains_feature_path_evidence` | FAIL | 包含 `feature_path` 和 PRD 路径，但缺少 `parent_feature`、`feature_level` 及 API/ADR 决策背景。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=0fd4749e245165ac082c4886ffe3b34e558fcf5435b6e2d292b5d95a96f92321; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确路由到 `engineer-agent:trd-gen`，并使用镜像 Engineer 路径；但未完整提供生成器限制和 handoff 字段/决策背景。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=4966306055ef9b96a6f57e7a45ce87508b801a0b2aecc6a50361a51aec077e3f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 将 API 和 ADR 分别路由到通用 API/架构 agent 及非 Engineer 路径，未提供所需 Engineer 交接信息。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未明确禁止 PM 内部 `api-gen` 或 `adr-gen` 直接生成。
- with_skill 输出缺少 `parent_feature`、`feature_level` 和 API/ADR 决策背景，未满足完整 handoff 要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-007-api-adr-engineer-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116` from `agents/product_manager/test/idea-to-spec/workspace/iteration-3/eval-7-api-adr-engineer-handoff`.
- Fixture SHA-256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- Prompt SHA-256: `2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9c3b136c6958582b2c5c3d552759bbe4fd3ef24876075804e91c5b21980a34af`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `02e5d899a7687cd28d5b7fe3ed85f267cd9ce62f15d9844aa4281eff90859ac1`
- Metadata SHA-256: `6b28964c95e54c379988fdfd7c54f486a5c872824039a926ede4358e3117f378`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `does_not_use_pm_api_adr_generators` | FAIL | The with_skill output says PM does not write Engineer documents, but does not explicitly state that API/ADR are Engineer-owned or prohibit PM `api-gen`/`adr-gen`. |
| `routes_to_trd_gen` | PASS | It explicitly assigns ownership to `engineer-agent` and says to invoke its `trd-gen` skill for generation. |
| `engineer_paths_mirror_feature_path` | PASS | It specifies `docs/engineer/chat-interface/history-search/API.md` and a matching ADR path, mirroring the PRD feature path. |
| `handoff_contains_feature_path_evidence` | FAIL | The output includes the PRD path and feature-path-related context, but does not include `parent_feature`, `feature_level`, or the required API/ADR decision-background evidence in a handoff package. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=96f71110a9f62fb91c56ea2031b8258b82dad660611287a006eee97051cf42ba; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routed work to engineer-agent/trd-gen and mirrored the Engineer paths, but omitted explicit generator prohibitions and required handoff metadata/background.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2ab3ca8b74dd55c90856f6dfac8c03932d3fb9eacb469271c944f9a989eec4b0; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=081774e59954e60a327f5e33eef597679c9bc5551bd27fbcf785553bbdbd2890; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Suggested API/ADR ownership and paths, but routed to generic API/ADR locations and omitted the required Engineer handoff route and metadata.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output fails the explicit PM generator prohibition assertion.
- The with_skill output lacks required handoff metadata and decision-background evidence.
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

# Eval Result: eval-007-api-adr-engineer-handoff

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: FAIL — 2/4 assertions passed.
- Coverage result: FULL — all 4 assertion scenarios were exercised.
Overall result: FAIL

### Assertion Results

- `does_not_use_pm_api_adr_generators`: FAIL — it said the artifacts are Engineer-owned but did not explicitly reject PM internal `api-gen` / `adr-gen`.
- `routes_to_trd_gen`: PASS — routed both artifacts to `engineer-agent:trd-gen`.
- `engineer_paths_mirror_feature_path`: PASS — used `docs/engineer/chat-interface/history-search/`.
- `handoff_contains_feature_path_evidence`: FAIL — the handoff omitted explicit `parent_feature` and `feature_level` fields.

### With-Skill / Baseline Comparison

The with-skill response preserved Engineer ownership and correct paths without writing API/ADR files. The baseline proposed unrelated `docs/api/` and `docs/adr/` paths.

### Failures / Next Steps

- Explicitly state that PM internal API/ADR generators are not used.
- Emit a complete handoff packet with the full feature-path metadata and decision background.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-007-api-adr-engineer-handoff/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-007-api-adr-engineer-handoff`
- Workspace: `workspace/iteration-3/eval-7-api-adr-engineer-handoff`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; confirmed PM PRD at `docs/pm/chat-interface/history-search/PRD.md`, with stale Engineer paths excluded by `execution_cleanup`.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-007-api-adr-engineer-handoff/`

## Latest Result

- Behavior result: PASS — all 4 assertions passed.
- Coverage result: FULL — 4/4 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `does_not_use_pm_api_adr_generators`: PASS — states that API and ADR are Engineer-owned and PM must not generate them.
- `routes_to_trd_gen`: PASS — explicitly hands off to `engineer-agent:trd-gen`.
- `engineer_paths_mirror_feature_path`: PASS — requires `API.md` and `ADR-*.md` under the full Engineer feature path.
- `handoff_contains_feature_path_evidence`: PASS — includes the feature metadata, approved PRD path, API needs, and ADR decision context.

## With-Skill Behavior

The response preserves the PM/Engineer boundary, uses the confirmed PRD as the source of product truth, and leaves unknown technical constraints as blockers rather than fabricating them. It does not use BRD as a handoff source or lifecycle stage.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and cleaned fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It retained general Engineer ownership but omitted the precise `engineer-agent:trd-gen` route and preferred a non-canonical ADR subdirectory.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no ownership, path, or handoff regression.

## Next Steps

- Keep this eval as coverage for Engineer-owned API/ADR handoff from a confirmed PRD.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-007-api-adr-engineer-handoff/` and are not committed.
