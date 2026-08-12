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
- target_skill_sha256: `7350d982beaf3dbc1ec747d4598f05c9a1dfb9b1eb61dcb04ae43dfd72f6fcfd`
- eval_definition_sha256: `3255bddbc0ba9d00273a741fab78b9e223454656c0b7cbcdb74a3b3b193952f9`
- metadata_sha256: `c58e464b2f51cbecc05208e0f4320ff2bade980227072a25840336ba048c489e`
- fixture_sha256: `26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `58d5f8c73c18457a8d0864b8f5e21613dc914d57c8f96acc11ce98a78c601f05`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea`
- Repository HEAD: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41df440b7248e793c6d9703098fb03264d5ab1871ee7f72726859596ddf5327e`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `updates_existing_trd` | PASS | With-skill delivery snapshot contains only the existing TRD, with version 1.2.0 and generated_by: trd-gen; its body has no routing instructions. The summary names the owner/path without claiming transfer, start, or routing. |
| `body_consolidation` | PASS | The locked TRD body describes the event-driven design and contains no retained polling plan or deprecation-status wording. |
| `removal_recorded_in_changelog` | PASS | Frontmatter includes a changelog with the 1.2.0 update and prior 1.1.0 entry; the version was updated from 1.1.0 to 1.2.0. |
| `no_implementation_plan_or_code` | PASS | The delivery snapshot contains only TRD.md; no implementation plan, source-code, or test-file mutation is evidenced. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=ee26287fc58756a1916e0e1446e2fa7bcb1ce88e62d1b7b2c79f35d3de45c0d8; snapshot_sha256=6a31c9c534f8b1311aea0b5b4a9eba9808ef141aab1976a3166bd2b6241319fa
- Behavior: Updated the existing TRD into a detailed event-driven specification with generated-by provenance, changelog, and no downstream execution claim.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=9a698def02f4cdf1fbf6288f9cc272608de72abf6db798e94a77579e171c5fa7; snapshot_sha256=ac45d65ebd638d80574971ce7cd5854efc950aee2f709850219a997355b5ab30
- Behavior: Updated the existing TRD to an event-driven design, but the snapshot omitted the required changelog and trd-gen provenance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
