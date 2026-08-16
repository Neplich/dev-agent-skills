# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-003-engineer-ui-maintenance-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `821c99c85df4188cff291d55bb3f776ec720f8cbbd3f93df4bf7a03b6520bf3a` from `agents/designer/test/designer-agent/evals/workspace/eval-003-engineer-ui-maintenance-handoff`.
- Identity schema: `2`
- target_skill_sha256: `1d67d4772843dc0275749d693d7415791b7459f5d948588a69fb240bcfd7f02b`
- eval_definition_sha256: `138aebdae4a1049db8b791a6754cc321fff06d447fcae99b0206d1d5aa26e929`
- metadata_sha256: `f547a888a015d9e9862374a63fae63a3c03679e1e0f3c3c280b9cf0370c3b020`
- fixture_sha256: `821c99c85df4188cff291d55bb3f776ec720f8cbbd3f93df4bf7a03b6520bf3a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `642d6c7ee5330dc1af39bc9648e9c1bffdb74e1229fc98a9c317e40e13baaebf`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `92f4c4b043cb3aab774531019133e8d4e6f2d81d21a277f0cd9696a8cc0a58e7`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `902f97074f6d958600dd8079608539a38bff227cb03726b9ab277705b1b8ded7`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_engineer_design_handoff` | PASS | The with_skill trace reads the designer-agent routing contract, which defines an Engineer UI-maintenance/frontend-update handoff as a valid design entry; the locked final output identifies the entry as an Engineer UI maintenance handoff and stops at design delivery. |
| `uses_confirmed_feature_path` | PASS | Both locked design snapshots use feature_path "customer-portal/profile-settings" and list the matching PRD and TRD under source_documents; the trace shows both documents were read. |
| `routes_design_skills` | PASS | The trace reads ui-ux-design and visual-design skill instructions, and the delivered snapshots separately cover information hierarchy/layout and primary-button visual specifications. |
| `writes_design_outputs_only` | PASS | The locked workspace status shows only docs/design/ additions. The only delivered files are docs/design/customer-portal/profile-settings/ui-ux-spec.md and visual-system.md; their contents explicitly state they are design handoffs with no implementation artifacts. |
| `hands_back_to_engineer` | PASS | Both delivered snapshots state that design stops and the confirmed next owner is engineer-agent, responsible for TRD alignment, IMPLEMENTATION_PLAN.md, implementation, and tests; the final output repeats this handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=92f4c4b043cb3aab774531019133e8d4e6f2d81d21a277f0cd9696a8cc0a58e7; fixture_sha256=821c99c85df4188cff291d55bb3f776ec720f8cbbd3f93df4bf7a03b6520bf3a; output_sha256=c3442dd48d3a6aaf6a3f29a7bf93b5edc9880d0c4ce29d780b1289aab1dba966; snapshot_sha256=faab716e064401ed4e9324f13638807b66446d91e882a555461f91d8b09522d2
- Behavior: Accepted the Engineer design handoff, used the confirmed feature path and source documents, routed UX and visual work, wrote only the two permitted design artifacts, and handed implementation back to engineer-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=92f4c4b043cb3aab774531019133e8d4e6f2d81d21a277f0cd9696a8cc0a58e7; fixture_sha256=821c99c85df4188cff291d55bb3f776ec720f8cbbd3f93df4bf7a03b6520bf3a; output_sha256=b906d22a55a419cde5a7b864e0a342813318ad016381195bfe2702a7c06649be; snapshot_sha256=834b1cfc8befa23e18621dfcc5ef01dffe1d97c7442731104752c94612da04fd
- Behavior: Fresh baseline created a non-permitted DESIGN.md and modified the TRD, did not use the required output paths or explicit skill routing, and did not provide the required engineer-agent handoff framing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
