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
- target_skill_sha256: `41cf810393df0fdc64cc71f6ce5757c78fe5ad5c36eeff2140239588b7aedce4`
- eval_definition_sha256: `9a583203eacc9eba1f7a8bc21f635feb6ed3d4608d62de30920ed955c3d1edca`
- metadata_sha256: `033e6d4711141e6651acfe52a20a70eb12e8a0ec903be9ebf2806e8f26550c71`
- fixture_sha256: `f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `34f896897fd86f962fdde3e8fbee4d88ed3d89310d32aa50bf9d05459ebc08b8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `4a44a53303527788f0fdde89c2cf0711930adcb2731bd7176d57421ed0f8220c`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `c866a1fd5261fa544cd5ead0d94e8cdbb452e17b33cb77d4568d44490e6053bf`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `monorepo_classified` | PASS | with_skill 明确写出“结论：是 monorepo”，且与根 package.json、pnpm-workspace.yaml 和 ENGINEERING_CONTEXT.md 一致。 |
| `workspace_projects_listed` | PASS | with_skill 列出了全部子项目路径：apps/web、apps/api、packages/shared；与 workspace 配置及各 package.json 一致，并说明未发现其他子项目。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4a44a53303527788f0fdde89c2cf0711930adcb2731bd7176d57421ed0f8220c; fixture_sha256=f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f; output_sha256=6dce94823d07bb0a2a37a7d59f8770b5ff2cc1b74bc3168b130e3d32f6eeb403; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确判断为 monorepo，并完整列出两个应用和一个共享包。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4a44a53303527788f0fdde89c2cf0711930adcb2731bd7176d57421ed0f8220c; fixture_sha256=f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f; output_sha256=3dbd4bc1e8f2449c1ea979887d3de2bb50c0d27d9b5144786b1ed5532d7ed0f1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样准确判断为 monorepo，并完整列出两个应用和一个共享包，作为一致的基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
