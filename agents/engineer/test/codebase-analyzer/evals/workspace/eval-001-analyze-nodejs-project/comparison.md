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
- Fixture SHA-256: `70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522`
- Prompt SHA-256: `cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `de6d27a82a6affa1d54b83f57c4eb1889c4977944cd8849112c1a97798fbfd77`
- Skill overlay SHA-256: `be427177bb8618969a8c9c2b0aea6596dceb0dbc6a57e3c3bb5e1896d11ef1ed`
- Judge schema SHA-256: `4a44af8c4f43ac2a76bbdbb1c44519dabd549bb54a1dc48487259a1d80539946`
- Eval definition SHA-256: `dad930e2f7ff239d93a7a9675b382ce2b702f6090d6d7cc66b26e7ea598351d6`
- Metadata SHA-256: `5ca1d6325e7d73a97605eeb110ddc4062765b77075b5da8df9a904201e44cb60`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `technology_stack_identified` | PASS | with_skill 输出的 YAML Project Profile 包含 tech_stack.language、tech_stack.framework 和 tech_stack.package_manager。 |
| `project_structure_mapped` | PASS | with_skill 输出包含 architecture.source_dirs 和 architecture.test_dirs，分别识别为 src 和 test。 |
| `coding_conventions_identified` | PASS | with_skill 输出包含 conventions.linter 和 conventions.formatter，分别描述 ESLint 与 Prettier 配置。 |
| `structured_profile_output` | PASS | with_skill 输出使用 yaml fenced block，并以结构化 YAML 形式提供 project_profile。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=837dc8de0f6ee0a5b00b096c299632b673b54e061c071a047bc9d3b72d9f9f12; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整输出了包含技术栈、目录结构、编码规范的 YAML 项目概况。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=19186d8c41ffe991f155151b173b8554768479b82600997479c6917ca81f1ae3; snapshot_sha256=b80ea6b9d8a6d8b52a2cf088db8194c2d9c3f36a2840eca70cd503f4a4056e4a
- Behavior: 通过 PROJECT_PROFILE.yaml 文件交付了更完整的项目概况；其文件内容满足相关结构化信息要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
