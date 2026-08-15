# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-006-delivery-polling-to-events`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74` from `agents/engineer/test/trd-gen/evals/workspace/eval-006-delivery-polling-to-events`.
- Identity schema: `2`
- target_skill_sha256: `47bb3c8e8bad899368b78c2d70a8b75f85c0900f5ef5546caa9c9be9e034ebd2`
- eval_definition_sha256: `3255bddbc0ba9d00273a741fab78b9e223454656c0b7cbcdb74a3b3b193952f9`
- metadata_sha256: `349f9852eee2f1f2a334e786dfe6be905191fc49881eadf61556b46ab3eeb5b7`
- fixture_sha256: `26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `58d5f8c73c18457a8d0864b8f5e21613dc914d57c8f96acc11ce98a78c601f05`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b2bd7a022294f7539263ea78da33349f841bc77d827c181e2b2867a85cb18e8f`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `updates_existing_trd` | NOT_EXERCISED | The locked snapshot shows the existing TRD updated and no other feature document, but the locked raw evidence cannot independently prove that trd-gen performed the edit. |
| `body_consolidation` | PASS | The locked TRD body directly specifies event-driven delivery and does not retain the polling design as a deprecated or otherwise status-labeled section. |
| `removal_recorded_in_changelog` | PASS | The locked frontmatter adds a changelog entry documenting replacement of polling and updates version from 1.1.0 to 1.2.0. |
| `no_implementation_plan_or_code` | PASS | The locked delivery snapshot and git evidence show only TRD.md changed; no implementation plan, code, or tests were added. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=10715d8e9666f4d43950d7be0fc7c58cf6853025df1c9082edc93bd04986f291; snapshot_sha256=2f31843f403946176b7dc491abad8342792d86e8c0afb27ab3661bd994e12927
- Behavior: The existing TRD was updated to an event-driven design with changelog/version updates, while no implementation artifacts were added. The authoring-agent process is not independently provable from the locked evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=a7dc134045cbccc65980aa10419b08c5350697c7cf13eccf87790572e67ce8a1; snapshot_sha256=6fb691f4bc760983ba2764f481857a3fe26832689c905062a96e322887ecba67
- Behavior: The baseline updated the existing TRD to event-driven delivery and version 1.2.0, but its snapshot omitted the required changelog.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
