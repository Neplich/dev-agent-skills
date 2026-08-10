# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-001-unreleased-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-001-unreleased-mode`.
- Fixture SHA-256: `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17`
- Prompt SHA-256: `43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `53f035563de038125d09b7a8997f87e900d099e00223f427a7c690e11ebbe449`
- Skill overlay SHA-256: `9534a5bf71391ac48cfd6a48ca8f80e93da520d6ea9d2026741fd864da0cb720`
- Judge schema SHA-256: `e87b7560e9b11fe6dfc954d0faa2696f04b98bb48f59af2eb521a8e8cfed4660`
- Eval definition SHA-256: `f643e5a44adc95dee4686543e115df7acb899ebc5dec146519d9991e82db553d`
- Metadata SHA-256: `95c0dae43621d97267d71f9000473df424f0f20875022c90f8a0826f1615ee52`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `unreleased` | PASS | with_skill delivery_snapshot contains `## [Unreleased]`. |
| `pr` | PASS | Both included entries contain GitHub PR links with `(#310)` and `(#311)`. |
| `bot_pr_dependabot` | PASS | PR #312 by `dependabot[bot]` is absent from the locked delivered file. |
| `chore_ci_test` | PASS | Chore dependency PR #312 and internal CI PR #313 are absent from the locked delivered file. |
| `versioned_changelog_file` | PASS | with_skill delivery_snapshot directly contains the file at `docs/changelog/changelog-unreleased.md`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=48df9d25dc0492ad2b3e6c970accc092e7d19985499886500761dde01f3bd7d0; snapshot_sha256=43039ce65dda406efc363a36408cbdaac9130194336a569957665ae7747abf77
- Behavior: Generated the requested Unreleased changelog file with user-visible Added and Fixed entries, PR links, and excluded bot/dependency/internal CI changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=832d54f42ce83b072fcad15d2e3e54b04993409084f664b2b8954b702763e1cc; snapshot_sha256=773a004a177e2ad2b3f336a901cb504f98499aae518030526b15f89e62428bd9
- Behavior: Also generated the requested changelog content and exclusions; serves as comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
