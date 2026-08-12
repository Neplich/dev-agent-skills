# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-001-timeline`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165` from `agents/product_manager/test/roadmap-gen/workspace/eval-1-timeline`.
- Identity schema: `2`
- target_skill_sha256: `74b972ac8dbd7706448e20025f6995b87c544e99309b65961f70d0e86a7bd191`
- eval_definition_sha256: `d6df04c011109b2d27a14aaefa7802d9d9c0af801e4acce9ed37afdc4c26a731`
- metadata_sha256: `c374d15583cb501346d3285d30669c9dbaf58b19f95661d07d8aeac8332d8ba1`
- fixture_sha256: `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c9231138562bec2ed562cf0d8c1ec94b96debb390ee547b6815473c326c64b09`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | 有截止日期的 3.36.0、3.37.0、4.0.0 分别归入当前冲刺、近期计划和远期规划；已关闭的 3.35.0 单列为已完成。 |
| `undated_semantic_inference` | PASS | 无日期的 3.38.0 基于当前版本 3.35.0 和 minor 版本语义归入近期计划并注明需确认；无法匹配的 Rendering research 单列待维护者分类，未捏造日期或静默归入未排期。 |
| `roadmap_artifacts` | PASS | 交付文件直接包含进度条、Mermaid Gantt、带状态复选框的 issue，以及 milestone 和 issue 的 GitHub 链接。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=85c31c6e651690c360dab0e9ce9a9ca851efa81ae5403012f970af21bbe7732c; snapshot_sha256=5a91475d0241069ccaf63eaa5b864b26a0296c24be4f07a349b8f189a6a57b1f
- Behavior: 生成了完整路线图，正确处理有日期和无日期 milestone，并保留所需路线图证据与链接。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=994a8eb9be96c5a282daaf54a08b8e966818508c408341793aa2e7704bf88763; snapshot_sha256=d0b2deb8e503d3d0671982342049802d6ba131413e85fa3ad642d9e643d5130e
- Behavior: 也生成了内容丰富的路线图并正确记录阶段和语义规划，但未见 Mermaid Gantt 等完整证据工件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
