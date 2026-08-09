# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-005-feed-mode-completeness`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56` from `agents/product_manager/test/github-reader/evals/workspace/eval-005-feed-mode-completeness`.
- Fixture SHA-256: `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56`
- Prompt SHA-256: `733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `68da0ba1f028f581794447a220a41c2a7932596fc89598d52df4a3ae7cae05a7`
- Judge schema SHA-256: `4f066e3762e89c228d67c784e34a35c0c16edf603d99427b4a0ebdaa56519646`
- Eval definition SHA-256: `c049e8ab5f946f319bc21927957f6fda02a148471bd8950bd306a941a14167f6`
- Metadata SHA-256: `07ab98c6d1c3adcc9277e1cfe784f8d017e9650890973540f2c3871622f64ed2`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feed_yaml_present` | PASS | PASS: The with_skill output includes a `github_reader_data` YAML block with repository, timestamp, open issue/PR totals, and related fields. |
| `completeness_signals_consistent` | FAIL | FAIL: The report states all collections are complete and omits the fixture’s milestone reconciliation warning, even though milestone counters total 5 open issues while the exported issue detail contains only 3 milestone-linked issues. No corresponding incompleteness signal is provided. |
| `totals_not_fabricated` | PASS | PASS: YAML totals and `search_evidence.total_count` values match the fixture’s search totals: 4, 3, 2, and 5. They are not inferred solely from collection lengths. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=dd1fa12a2aaf1bfac80256871cede7fead6abbe729fd75db685adad0b3f307ed; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produces the requested Markdown report and YAML feed with correct search totals, but gives an inconsistent completeness assessment by omitting the milestone reconciliation warning.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=6de76c792801edfb0e0823ff6ed928589099f93d50a89f008e3bf4fb57eb2f32; snapshot_sha256=2ab70d9152e88d6c1f99652b5aeee29a0ec70178784a76765df64d37890a62c7
- Behavior: Creates a file-backed JSON status input and explicitly reports a warning about milestone totals versus issue detail, but does not provide the requested YAML feed block.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill report presents completeness as fully passing and fails to surface the milestone open-issue reconciliation inconsistency present in the raw evidence.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
