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
- Identity schema: `2`
- target_skill_sha256: `c9fd11f6d83f8ba28a8e7797fde5b9dd25e2a04cb6c37589ec154de48aa8548c`
- eval_definition_sha256: `9a583203eacc9eba1f7a8bc21f635feb6ed3d4608d62de30920ed955c3d1edca`
- metadata_sha256: `033e6d4711141e6651acfe52a20a70eb12e8a0ec903be9ebf2806e8f26550c71`
- fixture_sha256: `f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `34f896897fd86f962fdde3e8fbee4d88ed3d89310d32aa50bf9d05459ebc08b8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `4a44a53303527788f0fdde89c2cf0711930adcb2731bd7176d57421ed0f8220c`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `1f817d88b8e507da0a311c9d5e0c0422e91854cfcc0cc72bf66b96f5b16560f6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `monorepo_classified` | PASS | with_skill 输出明确写明“这是一个 pnpm monorepo”。 |
| `workspace_projects_listed` | PASS | with_skill 输出列出 apps/web、apps/api 和 packages/shared 三个 workspace 子项目路径，和 fixture 中的 workspace 配置及 manifests 一致。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4a44a53303527788f0fdde89c2cf0711930adcb2731bd7176d57421ed0f8220c; fixture_sha256=f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f; output_sha256=aec0f3d523f2cd46e72754b80cf6d63f33d613040385ed3d0958cc7f9f24fbca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 明确判断为 monorepo，并完整列出三个 workspace 子项目。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4a44a53303527788f0fdde89c2cf0711930adcb2731bd7176d57421ed0f8220c; fixture_sha256=f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f; output_sha256=cfdf27e44c13af96eddef7d778b36069b5e931e2a4132b568f8104ed14d690ca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样正确判断为 monorepo，并完整列出三个 workspace 子项目，作为 fresh baseline 对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
