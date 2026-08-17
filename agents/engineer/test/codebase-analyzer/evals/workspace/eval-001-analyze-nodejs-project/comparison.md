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
- target_skill_sha256: `41cf810393df0fdc64cc71f6ce5757c78fe5ad5c36eeff2140239588b7aedce4`
- eval_definition_sha256: `dad930e2f7ff239d93a7a9675b382ce2b702f6090d6d7cc66b26e7ea598351d6`
- metadata_sha256: `b09b2e34a1bc5ec08902e953078b6e50b9b3e493d87817195c6c1c1de0770c57`
- fixture_sha256: `70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4a44af8c4f43ac2a76bbdbb1c44519dabd549bb54a1dc48487259a1d80539946`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `c866a1fd5261fa544cd5ead0d94e8cdbb452e17b33cb77d4568d44490e6053bf`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `technology_stack_identified` | PASS | With-skill YAML includes language, framework, runtime, and package_manager under tech_stack. |
| `project_structure_mapped` | PASS | With-skill YAML explicitly includes source_dirs: [src] and test_dirs: [test]. |
| `coding_conventions_identified` | PASS | With-skill YAML includes ESLint linter rules and Prettier formatter configuration details. |
| `structured_profile_output` | PASS | With-skill delivery contains a Project Profile in a fenced YAML block. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=dfd937cf8504bf5d19419da7228a810a8918a995d5d8cf9061a3cd55ccefb1e9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced an evidence-backed YAML project profile covering all requested areas.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cad1b3715da2e128465b3215c9e0ead310ad90fc998d9d73f08f99586980cace; fixture_sha256=70d2400afd3b1f84a7248de72cf04a9e4741bffe1ed6525d4f1cdd2942b2f522; output_sha256=05961a202ab7fffb0b931eca197aa8b6a6fb8ae4154bd3c4d6e8526b90ebc64e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also produced a YAML profile covering the assertions, serving as the fresh baseline comparison.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
