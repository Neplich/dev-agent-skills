# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-003-docs-image-release-rules`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf` from `agents/devops/test/cicd-bootstrap/evals/workspace/eval-003-docs-image-release-rules`.
- Fixture SHA-256: `3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf`
- Prompt SHA-256: `d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `86f7228d11d9f7ad3ec145d83be1c28f8a4bb93afea61016f55ed2860069bc68`
- Skill overlay SHA-256: `c8eba5ff7fa14d3a9d17d2f0e6e7ee710355737a3424af1c887580cc79ea33c4`
- Judge schema SHA-256: `8eaf2480ee518c77bc5e1ae8a7f25c0acfc010e7317cc45d7143e8591e25551c`
- Eval definition SHA-256: `90a9cf04ee14bffff8a2eaca0298de327ed551cee77903fd69a219a57495281e`
- Metadata SHA-256: `3fa9951d25624dea3daa1a46647a39c6e45e551d897c4684f13850f3c7afbfd4`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_host_image_policy` | PASS | with_skill accurately restates immutable tags, registry, tag trigger, and amd64/arm64 requirements for both Public and Internal; fixture confirms these host policies. |
| `verifies_each_published_variant` | NOT_EXERCISED | No proposed workflow, delivery snapshot, or published runtime evidence exists; with_skill states validation is required but cannot exercise it. |
| `keeps_delivery_authority_separate` | PASS | with_skill explicitly states that writing CI/CD configuration does not authorize push, publication, commit, tagging, or deployment; git evidence shows no mutation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=020354b50093f60d4b1d9a92745c2c71e9ab332356854b032e75aead541aefdf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the absent CI/CD change, preserves the host image rules, describes per-variant manifest/digest validation, and keeps release authority separate.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=a909f44597d1d5fd68102b605cc11eea98b143082aff4fee865e64478a8b3e6a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also reports the absent change and host conventions, providing a fresh baseline with less explicit validation and authority-boundary detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide a proposed workflow or diff and published manifest/digest evidence to exercise per-variant validation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
