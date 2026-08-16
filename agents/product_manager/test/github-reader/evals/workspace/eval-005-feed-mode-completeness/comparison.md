# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-005-feed-mode-completeness`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `740d701b2570cd48dc39895eb6dad24e4e63318905be6af74ad27b07c8129f82` from `agents/product_manager/test/github-reader/evals/workspace/eval-005-feed-mode-completeness`.
- Identity schema: `2`
- target_skill_sha256: `d3991eb6cbaa175b6a277fc4b5fcfd2722f7236109022f8336344db1c65d4b7e`
- eval_definition_sha256: `c049e8ab5f946f319bc21927957f6fda02a148471bd8950bd306a941a14167f6`
- metadata_sha256: `07ab98c6d1c3adcc9277e1cfe784f8d017e9650890973540f2c3871622f64ed2`
- fixture_sha256: `740d701b2570cd48dc39895eb6dad24e4e63318905be6af74ad27b07c8129f82`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4f066e3762e89c228d67c784e34a35c0c16edf603d99427b4a0ebdaa56519646`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `e4717fcaf9f805711dd56f954fc18d08364c40568c6f66db73a7888140ce8305`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feed_yaml_present` | PASS | with_skill 输出在 Markdown 报告后包含 `github_reader_data` YAML 块，并含 `open_issues_total`、`open_prs_total` 等关键字段。 |
| `completeness_signals_consistent` | PASS | with_skill 报告声明无截断且所有 `incomplete_results` 为 false；YAML 的 `truncated_collections: []`、`incomplete_totals: []`、`milestones_complete: true` 与 fixture 一致。 |
| `totals_not_fabricated` | PASS | YAML 总数分别为 4、3、2、5，并逐一对应 fixture 中 search 的 `total_count`，同时保留了 `query_evidence`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5; fixture_sha256=740d701b2570cd48dc39895eb6dad24e4e63318905be6af74ad27b07c8129f82; output_sha256=8dfa16f4ec286cf74425480d3c7875c0f06d53e87d9794c4d73f9a7db50a7d01; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了带完整性信号的 Markdown 状态报告及 Feed mode YAML，数量与原始快照一致。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5; fixture_sha256=740d701b2570cd48dc39895eb6dad24e4e63318905be6af74ad27b07c8129f82; output_sha256=53aba91bad18f6dd36584365734ae066e0bcbf2593f58ad8005c5b1d090e8996; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了结构化 JSON 状态摘要，但未提供要求的 `github_reader_data` YAML Feed 块。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
