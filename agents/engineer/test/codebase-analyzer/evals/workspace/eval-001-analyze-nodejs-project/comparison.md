# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-001-analyze-nodejs-project`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522` from `agents/engineer/test/codebase-analyzer/evals/workspace/eval-001-analyze-nodejs-project`.
- Identity schema: `2`
- target_skill_sha256: `c9fd11f6d83f8ba28a8e7797fde5b9dd25e2a04cb6c37589ec154de48aa8548c`
- eval_definition_sha256: `dad930e2f7ff239d93a7a9675b382ce2b702f6090d6d7cc66b26e7ea598351d6`
- metadata_sha256: `b09b2e34a1bc5ec08902e953078b6e50b9b3e493d87817195c6c1c1de0770c57`
- fixture_sha256: `70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4a44af8c4f43ac2a76bbdbb1c44519dabd549bb54a1dc48487259a1d80539946`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `1f817d88b8e507da0a311c9d5e0c0422e91854cfcc0cc72bf66b96f5b16560f6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `technology_stack_identified` | PASS | with_skill 的 YAML Project Profile.tech_stack 明确包含 language、framework、package_manager。 |
| `project_structure_mapped` | PASS | with_skill 的 architecture 明确包含 source_dirs: ["src"] 和 test_dirs: ["test"]。 |
| `coding_conventions_identified` | PASS | with_skill 的 conventions 明确包含 linter 和 formatter 配置信息。 |
| `structured_profile_output` | PASS | with_skill 将项目概况放在 YAML 代码块中，内容为结构化 Project Profile。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=e992423281abfd7d222d2016ec9a6f92199e2d2de6fa31e5ba33b78db3ad850a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整输出了符合要求的 YAML 项目概况，覆盖技术栈、目录结构和编码规范。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=46f2de12846ef7d5896d1a80909869da7b0ece664ff3e56e4896a6f8fca78378; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样满足四项断言，但结构化字段命名较不直接，例如使用 source_directory/test_directory 而非 source_dirs/test_dirs。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
