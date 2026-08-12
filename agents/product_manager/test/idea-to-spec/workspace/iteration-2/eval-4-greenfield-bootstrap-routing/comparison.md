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
- target_skill_sha256: `a5ef9beb8352f2c9b4cfde83ccd9caf0accd15d632ffa2d78214f3c51045041a`
- eval_definition_sha256: `8e113c060d578c3d672e422d3214efcf8ef5f3dc4a4d591f825ce19450902064`
- metadata_sha256: `af73e5b9a9192eb83b6e3ca2d5cae73fe4fd2b14b49ac401fa1a5f606db4bd6c`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `333e583cf4bb11484925925c3c083e2f295eb8670599a3d04a51d2b749c8668a`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `7ac19d358ca18ef7b2d109aeec17239bc9d0f4c0`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill explicitly reports an empty workspace, pending tech stack, and no existing docs before asking a product-direction question. |
| `pm_first_lane` | PASS | with_skill explicitly identifies the lane as `greenfield-discovery`, equivalent to the required PM-first new-project discovery path. |
| `pm_first` | PASS | with_skill stays in PM discovery, does not run scaffolding commands, and directs the flow toward PRD/DECISIONS after confirmation. |
| `assertion_4` | PASS | with_skill recommends forming a PRD skeleton and decision record, with durable documentation paths listed as pending. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=07ad031463d1a02999d61744584cdef4b87ec65e5c674a26d7b2beb3ee0ae855; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performs empty-workspace discovery, selects the PM-first greenfield lane, avoids project initialization, and identifies PRD/DECISIONS as the next documentation step.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=785d840d004d9f2276caf1d08245bde78a07bd51f4488bf9a3ca050ec1c33e93; snapshot_sha256=aa872f0629d272b58322b8752e946196678d342410e8a531f6fc7cf9ec5385d0
- Behavior: Creates a PRD and avoids initialization, but does not provide the explicit empty-workspace state or greenfield-discovery lane framing shown by with_skill.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Confirm the assistant's target-user direction before writing the pending PRD and DECISIONS documents.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
