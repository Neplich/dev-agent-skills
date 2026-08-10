# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-003-block-bootstrap-conflict`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-003-block-bootstrap-conflict`.
- Fixture SHA-256: `67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a`
- Prompt SHA-256: `7e27a0b4acbeb0bbab6d1ce4f4eaef1707f80d3f366d62ddd92d0e2d6f621f17`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `b193497852920517172f09f5d68ba6d13d4646f7f71948ca300566e66c51cb59`
- Judge schema SHA-256: `8fb0a4310aa73072ce3915bd9569df86e49409cfb5df2e41bfa626f79fa1e1ef`
- Eval definition SHA-256: `ef71b65d8d90e0a7a85b11140f77333b6bccfac4b39b25f67875d33153f0ebea`
- Metadata SHA-256: `dd91ae0a6e0ac8c19ffeb9b16bf575dc1d6e559c0626e7027f9e04c671f270d0`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_complete_conflict_list` | PASS | With_skill raw trace reports the complete inventory: 39 missing, 2 identical, and exactly one conflict at docs/site/standards/index.md; it marks the conflict blocked and records no writes or success manifest state. |
| `does_not_overwrite_conflict` | PASS | With_skill delivery and git evidence show the fixture file content remains unchanged, with empty git status and git diff; the candidate explicitly states no scaffold files were written before resolution. |
| `offers_explicit_resolution_choices` | PASS | The with_skill output explicitly offers overwrite, merge, and keep-existing choices, and requests user selection; no kept-as-is manifest entry is recorded before selection. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7e27a0b4acbeb0bbab6d1ce4f4eaef1707f80d3f366d62ddd92d0e2d6f621f17; fixture_sha256=67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a; output_sha256=c861a859cf0a1746327a8931dcf91a16181f5a6641fe98048e0def0ec555eb8f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Detected the complete inventory and the sole conflict, blocked progress, preserved the host file, and requested an explicit overwrite, merge, or keep-existing decision.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7e27a0b4acbeb0bbab6d1ce4f4eaef1707f80d3f366d62ddd92d0e2d6f621f17; fixture_sha256=67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a; output_sha256=fba6a9d5d0be6bb3f1d807899496a95f380b2456a944a3af0db643edb5c187db; snapshot_sha256=00a1c659831425c6ca7b19a89dbc7f6a607c5fbb9812f9d1b9a93d33f15c17e7
- Behavior: Applied the scaffold and recorded a preserved-existing manifest state without presenting the required blocked conflict workflow or explicit resolution choices.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
