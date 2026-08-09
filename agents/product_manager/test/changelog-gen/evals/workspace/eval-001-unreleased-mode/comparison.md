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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `53f035563de038125d09b7a8997f87e900d099e00223f427a7c690e11ebbe449`
- Skill overlay SHA-256: `9534a5bf71391ac48cfd6a48ca8f80e93da520d6ea9d2026741fd864da0cb720`
- Judge schema SHA-256: `e87b7560e9b11fe6dfc954d0faa2696f04b98bb48f59af2eb521a8e8cfed4660`
- Eval definition SHA-256: `f643e5a44adc95dee4686543e115df7acb899ebc5dec146519d9991e82db553d`
- Metadata SHA-256: `95c0dae43621d97267d71f9000473df424f0f20875022c90f8a0826f1615ee52`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `unreleased` | PASS | with_skill delivery_snapshot contains `## [Unreleased]`. |
| `pr` | PASS | Entries for PRs #310 and #311 include GitHub PR links with `(#number)` format. |
| `bot_pr_dependabot` | PASS | Raw evidence identifies #312 as authored by dependabot[bot]; it is absent from the with_skill file. |
| `chore_ci_test` | PASS | Raw evidence identifies #313 as CI-only internal maintenance; it is absent from the with_skill file. |
| `versioned_changelog_file` | PASS | with_skill delivery_snapshot directly contains `docs/changelog/changelog-unreleased.md`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=6a7129e162585b080cf049f1ecf331bdf61c3b14ef1684054c2485602de1b092; snapshot_sha256=68018826ff931ee3733f3af5ff445d5478f936b6e83cf72e81efe455cf6c1700
- Behavior: Generated the requested Unreleased changelog with user-facing PRs #310 and #311 while excluding dependency-bot and CI-only changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=a16c0fd13876947021e5df412cd6e7f6b04625cb1958edaec2967750b5ace9e7; snapshot_sha256=43d5eb13a1d02f71f5ceadd9de7e6a39d79931dac65f722043367da3b3476e2a
- Behavior: Generated a changelog containing user-facing PRs plus the dependency update #312; it excluded the CI-only change.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
