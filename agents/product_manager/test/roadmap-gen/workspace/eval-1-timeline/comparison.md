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
- Fixture SHA-256: `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165`
- Prompt SHA-256: `ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `74b972ac8dbd7706448e20025f6995b87c544e99309b65961f70d0e86a7bd191`
- Skill overlay SHA-256: `bddee41393bca0a60880eaa8d81044ec84f2c1d751e6af66c6178450b19850d3`
- Judge schema SHA-256: `c9231138562bec2ed562cf0d8c1ec94b96debb390ee547b6815473c326c64b09`
- Eval definition SHA-256: `d6df04c011109b2d27a14aaefa7802d9d9c0af801e4acce9ed37afdc4c26a731`
- Metadata SHA-256: `c374d15583cb501346d3285d30669c9dbaf58b19f95661d07d8aeac8332d8ba1`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | with_skill 的 roadmap.md 将有截止日期的 3.36.0、3.37.0、4.0.0 分为当前冲刺、近期计划和远期规划，并单列已完成 3.35.0。 |
| `undated_semantic_inference` | PASS | with_skill 对无日期的 3.38.0 基于当前版本 3.35.0 和后续 minor 版本语义暂列远期规划并要求确认；对无法匹配语义的 Rendering research 标记待维护者分类，未归入未排期且未捏造日期。 |
| `roadmap_artifacts` | PASS | with_skill 的 roadmap.md 包含 Unicode 进度条、Mermaid gantt、issue 的开放/关闭状态，以及 milestone 和 issue 的 GitHub 链接。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=5c560594e26c4cfa05c89d1dd1a03fe814daaa4a847be8d35ae99c4dee6fecb5; snapshot_sha256=f357b31aa25ac18efa1a0872e49b7df378c42f2b4d4f12a7a5f0c43ef68912ca
- Behavior: 生成了符合要求的 docs/roadmap.md，正确处理日期阶段、无日期 milestone 语义和路线图证据。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=f04ab3dbbb0d7f991a69f21648697629dae6320d99df6faebb389c2dd0a4fdf8; snapshot_sha256=1a1a4dbeb71a699d27ff46ed6ccb182c04f7d80952b83691d17133022c9e057f
- Behavior: 也生成了路线图，但将无日期 milestone 直接标为未排期，未提供 Mermaid Gantt，且进度汇总与原始快照计数不一致。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
