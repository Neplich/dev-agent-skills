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
- target_skill_sha256: `99ea82f9c285d0cd51090c481c0892adf1bdf20367a2866bf82eabffdc17f4c7`
- eval_definition_sha256: `c049e8ab5f946f319bc21927957f6fda02a148471bd8950bd306a941a14167f6`
- metadata_sha256: `07ab98c6d1c3adcc9277e1cfe784f8d017e9650890973540f2c3871622f64ed2`
- fixture_sha256: `740d701b2570cd48dc39895eb6dad24e4e63318905be6af74ad27b07c8129f82`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4f066e3762e89c228d67c784e34a35c0c16edf603d99427b4a0ebdaa56519646`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `a9770b603fd249fd7f80da3e56ab1a6acb6432c1ad6dff3ad5cfc0e089124eab`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feed_yaml_present` | PASS | With-skill output includes a Markdown `github_reader_data` YAML block with repository, raw search totals, fetched counts, and key status fields. |
| `completeness_signals_consistent` | PASS | With-skill report states all search results are complete/not truncated and milestones are complete; YAML has matching counts, `truncated_collections: []`, `incomplete_totals: []`, and `milestones_complete: true`. |
| `totals_not_fabricated` | PASS | YAML exposes `raw_search_totals` matching the fixture's search `total_count` values (4, 3, 2, 5), while separately reporting fetched counts. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5; fixture_sha256=740d701b2570cd48dc39895eb6dad24e4e63318905be6af74ad27b07c8129f82; output_sha256=041972b6bc550bf1abf5e7f851e7a51e1f8a915677c7ce6f81e2cdf05c5b9ac9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced the requested status report followed by a complete, internally consistent Feed mode YAML block grounded in the fixture.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5; fixture_sha256=740d701b2570cd48dc39895eb6dad24e4e63318905be6af74ad27b07c8129f82; output_sha256=0a054e4c0bddd0c9f23068856ebf2151e7c7f2a073e6517b7d3c8832948dbe2b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a structurally detailed JSON status input but omitted the requested Markdown report plus `github_reader_data` YAML block.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
