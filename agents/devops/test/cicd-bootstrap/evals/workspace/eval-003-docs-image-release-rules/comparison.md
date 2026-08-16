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
- Identity schema: `2`
- target_skill_sha256: `aed48fddfc5ff065b4c42b3cee1081c6e2b92b1fe8557c1413f01e05c0f91ef0`
- eval_definition_sha256: `90a9cf04ee14bffff8a2eaca0298de327ed551cee77903fd69a219a57495281e`
- metadata_sha256: `6a1d045506a143598b535f56d88f45cff18b1438e131bb6af437dccabaf2255d`
- fixture_sha256: `3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `8eaf2480ee518c77bc5e1ae8a7f25c0acfc010e7317cc45d7143e8591e25551c`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `f170ac0192e8f110fe74b7c61766437cb8268e62c38697fb51b94a3db4467e5f`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_host_image_policy` | PASS | The with_skill output explicitly carries forward immutable vX.Y.Z and git-<shortsha> tags, registry.example/project/service, linux/amd64 and linux/arm64, and tag-triggered production publication for both Public and Internal. |
| `verifies_each_published_variant` | PASS | The with_skill output gives Public and Internal separate build/publish-validation and manifest/digest-check rules, and explicitly states that a workflow definition is not evidence of publication; the locked evidence shows no workflow or published delivery exists, so the candidate correctly presents these as required rules rather than completed publication. |
| `keeps_delivery_authority_separate` | PASS | The with_skill output explicitly preserves the release-manager approval boundary and states that commit, push, image publication, tag/release creation, and production deployment were neither executed nor implicitly authorized. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=f259b6daf20d8981b7c333f9f15445be1dd01535b1dd9fc3b5fc519d07c42cc5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly reviews the available handoff evidence, distinguishes required CI/CD rules from absent implementation/publication evidence, covers both image units, and preserves delivery authorization boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=19f3dbb8a8856536621f65072c4f49ef620527967134bcbcc6812a49d7bcdbbe; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also identifies the handoff rules and approval boundary, but provides a less explicit per-variant validation treatment; it is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
