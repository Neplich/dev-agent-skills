# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `visual-design`
- Eval: `eval-002-playful`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `42400da86be636a5c48d6ced7acfe1114f7f3fc84e29109517e26b5a0856067c` from `agents/designer/test/visual-design/workspace/eval-2-reference-design-system`.
- Identity schema: `2`
- target_skill_sha256: `7b149b6fe06b79fc3d427a1960513a2a422e6be13b6ef797018ec31a49be8d0b`
- eval_definition_sha256: `1e9739265f0721cb69546820ef87da3e0b8045e92accd200c449d4a7c5bab7c5`
- metadata_sha256: `dea024aad09482b4b51327a960ae6e8c89fbc9764107a299297b588df52b9aa7`
- fixture_sha256: `42400da86be636a5c48d6ced7acfe1114f7f3fc84e29109517e26b5a0856067c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `b207ccfef6c29a46ee4c39ebd7d39f4af35c494d6c841b0789899fe237e9584b`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `design_system_data` | PASS | The locked with_skill delivery file directly contains a Reference-Driven Design System, local Design System Data query and findings, product classification, recommended Data-Dense Dashboard pattern, Data-Dense + Minimal Trust style, color system, typography, UX Quality Rules, and Anti-patterns. |
| `assertion_2` | PASS | The locked with_skill delivery is a Markdown design document with no implementation code, installation commands, or file-by-file engineering task breakdown; the final message states the design boundary ends there. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=092b10f39d07502fd69cfd2b4992b956cec050d77722de8312a6a9dc94160cd6; fixture_sha256=42400da86be636a5c48d6ced7acfe1114f7f3fc84e29109517e26b5a0856067c; output_sha256=dc0a45df762adbaee8d14827540446758140d23f33570462016003cce2605d1d; snapshot_sha256=25fa7a2c4ab83eaa55413b758e94d3145ea5a61ad3bdb28df9503c4c0b4b0f14
- Behavior: Delivered the required reference-backed visual system document and stopped at the design handoff boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=092b10f39d07502fd69cfd2b4992b956cec050d77722de8312a6a9dc94160cd6; fixture_sha256=42400da86be636a5c48d6ced7acfe1114f7f3fc84e29109517e26b5a0856067c; output_sha256=358885fac2d70bf18d4df1bba3d745f36a108c3d59769180bdfd73c7d3f6615f; snapshot_sha256=90aa6c8797017d8288b671897c31d5318430de3bd8c0d8e28449da6ed7c97ff1
- Behavior: Delivered a visual system document, but its locked output does not evidence the required Design System Data/reference-driven content and mentions engineering adoption.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
