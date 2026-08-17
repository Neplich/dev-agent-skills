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
- target_skill_sha256: `b41596991874aec0c37e12acb656078a02504e51d6536f47c1befab8e1f38b4a`
- eval_definition_sha256: `90a9cf04ee14bffff8a2eaca0298de327ed551cee77903fd69a219a57495281e`
- metadata_sha256: `6a1d045506a143598b535f56d88f45cff18b1438e131bb6af437dccabaf2255d`
- fixture_sha256: `3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `8eaf2480ee518c77bc5e1ae8a7f25c0acfc010e7317cc45d7143e8591e25551c`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `777451b1778a899115de1846bd3248acc1a8fef07fa6857039ca7e40cdac46e8`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_host_image_policy` | PASS | with_skill explicitly preserves immutable vX.Y.Z and git-<shortsha> tags, registry.example/project/service, tag-triggered production publication, and linux/amd64 plus linux/arm64 for both Public and Internal. |
| `verifies_each_published_variant` | PASS | with_skill states that both image units require separate build/publish validation and independent post-publication digest and multi-architecture checks, and explicitly says workflow presence is not publication evidence. No actual publication was claimed. |
| `keeps_delivery_authority_separate` | PASS | with_skill explicitly preserves the release-manager approval boundary and says no push, publication, tag, or release may be executed during this review. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=0cb563964464d9e23dbf22838c89ea445f4cdc89cb5b18175cfcd9257d729f10; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly maps the handoff rules to both image units, distinguishes required validation from unavailable implementation evidence, and preserves delivery authority boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=f72b7cca4b8affce66815157c6078df9c07579cde12d1e8afa41cc4f6b10e64f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a generally correct baseline summary of the host image policy and approval boundary, but is less explicit about independent per-unit validation and evidence limitations.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
