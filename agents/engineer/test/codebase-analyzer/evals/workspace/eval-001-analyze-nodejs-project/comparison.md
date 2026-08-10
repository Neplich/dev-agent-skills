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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `de6d27a82a6affa1d54b83f57c4eb1889c4977944cd8849112c1a97798fbfd77`
- Skill overlay SHA-256: `2437579eab93080a360f91c28589c43439611fa078f69b97d2ce2bd37e59a941`
- Judge schema SHA-256: `4a44af8c4f43ac2a76bbdbb1c44519dabd549bb54a1dc48487259a1d80539946`
- Eval definition SHA-256: `dad930e2f7ff239d93a7a9675b382ce2b702f6090d6d7cc66b26e7ea598351d6`
- Metadata SHA-256: `5ca1d6325e7d73a97605eeb110ddc4062765b77075b5da8df9a904201e44cb60`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `technology_stack_identified` | PASS | The with_skill YAML includes tech_stack.language: JavaScript, tech_stack.framework: Express 5.1.0, and tech_stack.package_manager: npm. |
| `project_structure_mapped` | PASS | The with_skill YAML includes architecture.source_dirs: [src] and architecture.test_dirs: [test]. |
| `coding_conventions_identified` | PASS | The with_skill YAML includes conventions.linter with ESLint details and conventions.formatter with Prettier details. |
| `structured_profile_output` | PASS | The with_skill candidate presents Project Profile inside a YAML fenced code block. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=8180b2f33f1b3f1e9d9d21552d18d8f0dcff669dd5eec38d06980f0224c31a12; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a YAML Project Profile covering the requested technology stack, source/test structure, and lint/format conventions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=79fdfed1e21a5cc9c33b33bb8a7b5b9010f4c7f5f8b08b90fdeb99782e996996; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also produced a complete YAML profile, serving as a fresh-baseline comparison.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
