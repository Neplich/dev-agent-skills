# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-004-greenfield-bootstrap-routing`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/idea-to-spec/workspace/iteration-2/eval-4-greenfield-bootstrap-routing`.
- Identity schema: `2`
- target_skill_sha256: `62f7a88900be8a0aae1af9e34b28dc32abd76006ca95f89107567b68f5780813`
- eval_definition_sha256: `8e113c060d578c3d672e422d3214efcf8ef5f3dc4a4d591f825ce19450902064`
- metadata_sha256: `af73e5b9a9192eb83b6e3ca2d5cae73fe4fd2b14b49ac401fa1a5f606db4bd6c`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `333e583cf4bb11484925925c3c083e2f295eb8670599a3d04a51d2b749c8668a`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7b19869a4835a1feeb491815cac7af7bde071247819525989c10dbfbc0acd2f7`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | FAIL | The with_skill output says it starts from an empty directory, but does not state that the tech stack is undecided or that existing documents are empty, and it does not begin with an explicit workspace inspection. |
| `pm_first_lane` | PASS | The output explicitly identifies the lane as `greenfield-discovery`, describing PM-oriented product discovery for the empty workspace. |
| `pm_first` | PASS | The output explicitly says the current scope does not involve project initialization and routes first through product decisions and PRD/DECISIONS documentation rather than scaffolding. |
| `assertion_4` | PASS | The output names PRD.md and DECISIONS.md as pending durable documents and recommends drafting them after confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e54d3a1fa8816350f94e98867274b11c36d9bb0d0e06fd24c26f028576162cdb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly selected a PM-first greenfield-discovery route, avoided project initialization, and requested one product decision before drafting PRD/DECISIONS documents.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=bf19bd8e9522c825459dd62f1e9e54989aa729088b1841d72efc2267884035e6; snapshot_sha256=e8dcf5eb94b51a5ce7a1a703cd4ad56072b1a37ea373b9eb24e149e7ef3b7653
- Behavior: Created a detailed PRD file without initialization, but did not demonstrate explicit PM lane selection or the required initial workspace/technology/document-state framing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omits the required explicit statement that the tech stack is undecided and existing documentation is empty.
- Next: After user confirmation, draft the pending PRD/DECISIONS documents.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
