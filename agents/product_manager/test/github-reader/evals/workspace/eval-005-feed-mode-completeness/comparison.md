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
- Fixture SHA-256: `740d701b2570cd48dc39895eb6dad24e4e63318905be6af74ad27b07c8129f82`
- Prompt SHA-256: `733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `b0004c5792dae6a7d4050cf6839b7073909210717e4fcd3dd4b28188da158276`
- Judge schema SHA-256: `4f066e3762e89c228d67c784e34a35c0c16edf603d99427b4a0ebdaa56519646`
- Eval definition SHA-256: `c049e8ab5f946f319bc21927957f6fda02a148471bd8950bd306a941a14167f6`
- Metadata SHA-256: `07ab98c6d1c3adcc9277e1cfe784f8d017e9650890973540f2c3871622f64ed2`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feed_yaml_present` | PASS | With_skill output contains a Markdown report followed by a `github_reader_data` YAML block, including `open_issues_total: 4` and other key totals. |
| `completeness_signals_consistent` | PASS | The report states all four searches are complete and not truncated; YAML has empty `truncated_collections` and `incomplete_totals`, `incomplete_results: false`, and matching fetched/total counts. |
| `totals_not_fabricated` | PASS | YAML totals match the fixture’s search `total_count` values: open issues 4, open PRs 3, merged PRs 14d 2, and closed issues 14d 5; the report also identifies them as raw totals. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5; fixture_sha256=740d701b2570cd48dc39895eb6dad24e4e63318905be6af74ad27b07c8129f82; output_sha256=2f6af592864a675bbd4fa3e9fcc7f640d337fae63a04750e30c4ed75d1be29d9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced the requested Markdown report plus complete Feed mode YAML, with consistent completeness signals and search-derived totals.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5; fixture_sha256=740d701b2570cd48dc39895eb6dad24e4e63318905be6af74ad27b07c8129f82; output_sha256=696d2e69cfb55d270d0ac9af9c10afec26ed87d7c5b3ce3c6edd6c8448091089; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced structured JSON and accurate counts but omitted the required `github_reader_data` YAML Feed mode block.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
