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
- Identity schema: `2`
- target_skill_sha256: `2ba8dad890b4a470e045fac5a77553d35f40494dd4f5ee0df778eda64ba0f881`
- eval_definition_sha256: `f643e5a44adc95dee4686543e115df7acb899ebc5dec146519d9991e82db553d`
- metadata_sha256: `95c0dae43621d97267d71f9000473df424f0f20875022c90f8a0826f1615ee52`
- fixture_sha256: `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `e87b7560e9b11fe6dfc954d0faa2696f04b98bb48f59af2eb521a8e8cfed4660`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `f75f5f8b8869cc572a0f69646861f4a54c0e1cb5775b8c2dac040f714114c1c9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `unreleased` | PASS | with_skill delivery snapshot contains `## [Unreleased]`. |
| `pr` | PASS | with_skill entries include linked PR references `[#310](...)` and `[#311](...)`. |
| `bot_pr_dependabot` | PASS | with_skill snapshot includes only PRs #310 and #311; bot dependency PR #312 is absent. |
| `chore_ci_test` | PASS | with_skill snapshot excludes the chore/dependency and CI-only internal changes (#312 and #313). |
| `versioned_changelog_file` | PASS | with_skill delivery snapshot directly records `docs/changelog/changelog-unreleased.md` with file content. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=a03035b9e43fb52ec3393158f458a2bc2c9b90b5e5b1d479b29c5ba1121a17c5; snapshot_sha256=6e767afde2693f1bc204321e2d592c9f3ddd959601c219bd5980b89ef48241aa
- Behavior: Generated the requested Unreleased changelog with user-facing Added and Fixed entries, PR links, and excluded internal maintenance.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=baa4d62a90d0fce35044b5de0a36ac8b813ab61efb0d3786c3694d8169007318; snapshot_sha256=8d6c64a032ae626ecca1f2f2c3a8701ba143efe51ebb60f892269f71644f42fa
- Behavior: Also generated a valid changelog with the same user-facing entries and exclusions; behavior is comparable baseline context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
