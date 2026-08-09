# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-004-docs-build-variant-matrix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5` from `agents/devops/test/deployment-planner/evals/workspace/eval-004-docs-build-variant-matrix`.
- Fixture SHA-256: `1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5`
- Prompt SHA-256: `449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `762ea3248d76c5c9e715368b11ab616562bb9bdb0e2bd6a6aad38d47cc80b3af`
- Skill overlay SHA-256: `52ed13d453014671ce8cc7f7f7ce4b4108c3a5cc943fcf3bece1ac66b08625d5`
- Judge schema SHA-256: `cfb4e9daef57a9f8f8f71bd53e7b9c04b3f443f035ca06014209a131297ec22b`
- Eval definition SHA-256: `4c14837e1c149db8fdda5fa172eb35b4e3c167d223226adbc87832c6a7126d6f`
- Metadata SHA-256: `ae56541ba154741dfb7ef84587ce065786aeb8ae82c4a282fa656aa8884b399e`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `enumerates_all_docs_variants` | FAIL | With_skill only returns RETURN_TO_PM and does not deliver a deployment-unit matrix containing the three variants, despite naming them in prose. |
| `covers_deployment_unit_chain` | FAIL | With_skill provides only a brief coverage summary and omits the required per-variant chain checks for build context/static entry, image unit, Compose, Deployment/Service/Ingress or Gateway, values, health checks, and runtime entry. |
| `hands_units_to_cicd` | FAIL | With_skill records no per-variant integrated/alternative/deferred/blocked disposition and does not hand confirmed image units to cicd-bootstrap. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=e28a6c27c7bbacf8d72d22fc8f3ad55ee43a2be9776bdd6bba0ce80ff36e3471; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Refused the requested assessment and returned the work to PM without a delivery.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=59b5e5e9b894a0e0792730320dd14bffea5f7fa588dccb16b41d18db13e0e026; snapshot_sha256=bbf1a3007eccf8b1ef6f17b90e27b8b9c554bc17681ebe67bd1777119a484d5f
- Behavior: Produced a file-backed three-variant matrix and documented major gaps, though its matrix remained less detailed than the full assertion chain and included no evidenced cicd-bootstrap handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane incorrectly gates on a missing PM/DevOps handoff instead of evaluating the supplied fixture and producing the requested matrix.
- No deployment-unit matrix or CI/CD handoff was delivered in the with_skill lane.
- Next: Produce the complete three-variant deployment-unit matrix from the fixture.
- Next: Record the required chain fields and per-variant disposition, then hand confirmed image units to cicd-bootstrap without writing workflow code.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
