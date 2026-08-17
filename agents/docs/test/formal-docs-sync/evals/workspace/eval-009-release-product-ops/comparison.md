# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-009-release-product-ops`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-009-release-product-ops`.
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `c9bcafbf3ecc8c0e0ac28908b463b075e9d1371a95444953a8afc3d41757e192`
- metadata_sha256: `d04b92e9a3754ad51ae5d707b3601a2084dc53a6e309122269ca881bc88a10ef`
- fixture_sha256: `88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `56b98af2f6fc5a04535db999157836236eb69830528cbecc99ca00f23b4d8d9e`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `limits_release_to_affected_product_ops` | PASS | delivery_snapshot contains only the two affected pages and their change-map file; no API, database, design, or unrelated site files. |
| `reconciles_confirmed_version_facts` | PASS | Locked files and release evidence show dashboard limit 25, image registry.example/ai-hub:v1.5.0, and no v1.5.1 content. |
| `preserves_release_notes_surfaces` | PASS | Locked delivery and git evidence show no Release Notes surfaces were modified; the handoff explicitly excludes them. |
| `keeps_release_pages_unverified` | FAIL | Both locked delivered pages set last_verified_version: v1.5.0, contradicting the required unverified state. |
| `runs_release_host_checks_and_handoffs` | NOT_EXERCISED | The with_skill lane stopped at a claimed release-evidence gate, so npm run test:docs and the completed docs-agent:docs-audit handoff were not exercised; no unsupported successful-check claim was made. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75; output_sha256=2837fffe86223ab53cfcf35f35e5feb2509d8e77b556393f1bc3a9fd80b362bc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Bounded the release scope and reconciled version facts, but wrote pages with v1.5.0 verification stamps and stopped before host checks and audit handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75; output_sha256=bbdd1a1c2d82e33314f12fca6ca500411cd43cd324efb4fc744a990ab587e6f0; snapshot_sha256=ca7408c1107c440491a4a042a66258034bd8ba6213cad15f714e26ecb18d08a4
- Behavior: Updated the affected pages and mapping, ran npm run test:docs, and reported successful checks, but did not provide the release-mode gate and audit handoff discipline shown by the skilled lane.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Both delivered product and ops pages were stamped v1.5.0 instead of remaining unverified.
- Next: Keep both affected pages unverified and complete the required host checks and docs-agent:docs-audit handoff once the release evidence gate is satisfied.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
