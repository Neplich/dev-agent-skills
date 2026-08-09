# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-002-single-version-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-002-single-version-mode`.
- Fixture SHA-256: `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88`
- Prompt SHA-256: `d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `53f035563de038125d09b7a8997f87e900d099e00223f427a7c690e11ebbe449`
- Skill overlay SHA-256: `9534a5bf71391ac48cfd6a48ca8f80e93da520d6ea9d2026741fd864da0cb720`
- Judge schema SHA-256: `609660421781976ec561327c947a31da6f7d421bc63e99d2f3f00692dcdf763a`
- Eval definition SHA-256: `e34f2dddfabba5be49382d984bac6785776f7fb5fa22e37126ed32d1f44a81df`
- Metadata SHA-256: `814184c8bd7a959b3f0695c85bef4dd34c73bd316a08d00ccc354207f37fabc9`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `v_version_yyyy_mm_dd` | PASS | with_skill 文件包含 `## [v0.120.2] - 2026-08-05`。 |
| `release_tag` | PASS | with_skill 文件版本号为 `v0.120.2`，与 fixture 的 target_release.tagName 一致。 |
| `pr_conventional_commit` | PASS | PR #300、#301、#302 的标题均已去除 `fix(client):`、`docs:`、`feat!:` 前缀。 |
| `breaking_change_breaking` | PASS | PR #302 条目带有 `⚠️ **BREAKING**` 标记。 |
| `section` | PASS | 输出仅包含有内容的 `Changed` 和 `Fixed` sections。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=fe04769f803c1ba7bfd404232032681cfca22f7ec0ad5f0c3af897bbc37afabc; snapshot_sha256=c165a4a9a2c9ccd41858db324fda5280162727a78e510a626368977497b6a8d3
- Behavior: 成功写入包含正确版本、日期、全部 PR、清洗后标题和 breaking 标记的 changelog 文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=88091684ce05bada07c92db609134c52fff730aff45a278b21afb8ac4c523a71; snapshot_sha256=e78bf12223329d28baed7861f0bd439c62c987071972ce91e1da976d23751b60
- Behavior: 也写入了 changelog，但版本标题缺少 v 前缀，breaking change 未使用要求的 ⚠️ BREAKING 前缀。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
