# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-002-detect-monorepo`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f` from `agents/engineer/test/codebase-analyzer/evals/workspace/eval-002-detect-monorepo`.
- Fixture SHA-256: `f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f`
- Prompt SHA-256: `4a44a53303527788f0fdde89c2cf0711930adcb2731bd7176d57421ed0f8220c`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `de6d27a82a6affa1d54b83f57c4eb1889c4977944cd8849112c1a97798fbfd77`
- Skill overlay SHA-256: `2437579eab93080a360f91c28589c43439611fa078f69b97d2ce2bd37e59a941`
- Judge schema SHA-256: `34f896897fd86f962fdde3e8fbee4d88ed3d89310d32aa50bf9d05459ebc08b8`
- Eval definition SHA-256: `9a583203eacc9eba1f7a8bc21f635feb6ed3d4608d62de30920ed955c3d1edca`
- Metadata SHA-256: `c7ae12e62e0a39a4d07a2a609b69c812f1e0369799ab62ccf27310eb616d8c85`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `monorepo_classified` | PASS | with_skill 明确写出“这是一个 monorepo”，与 fixture 的 package.json 和 pnpm-workspace.yaml 中的 workspace 配置一致。 |
| `workspace_projects_listed` | PASS | with_skill 完整列出 apps/web、apps/api 和 packages/shared，覆盖 fixture 中所有 workspace 子项目路径。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4a44a53303527788f0fdde89c2cf0711930adcb2731bd7176d57421ed0f8220c; fixture_sha256=f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f; output_sha256=96bce92c0667c1271ed83748199615d5f409b2e7999fb57944c625e96fc43d10; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 明确判断仓库为 monorepo，并完整列出 2 个应用和 1 个共享包及其路径。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4a44a53303527788f0fdde89c2cf0711930adcb2731bd7176d57421ed0f8220c; fixture_sha256=f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f; output_sha256=2b517b7c8e40b8a03dc29b63639a2528840e47680aa3df922fc3437fce086950; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样正确判断为 monorepo，并列出全部 workspace 子项目；作为新鲜基线表现完整。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
