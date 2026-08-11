# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-012-change-tier-hotfix-abuse-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-12-change-tier-hotfix-abuse-blocked`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907`
- Repository HEAD: `d96f213470acb77cb92c1af637626260d3e55b45`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c978d115fb1b50ceb3f80a0d77c450574e05667bd8252ef5b6e8b67105206fa2`
- Skill overlay SHA-256: `5b89d6a3c235a107cde8314b908b32dbfa76d6dc330906b48f74091d88e9019d`
- Judge schema SHA-256: `05754bc7141a9de585a1127391112d0da97f3c7138eba96f4377a8a50be63d7c`
- Eval definition SHA-256: `757872d7dabcbeb5f63781cd39c51a0fbd55c644aaecd2a814401a4e784d4603`
- Metadata SHA-256: `5be95630fc657c3ddfcd1eee211fb45bdc7cc20a37cf20c50f58a72635d4712c`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reject_hotfix_abuse` | PASS | With_skill explicitly states `hotfix_disposition: rejected`. |
| `expectation_change_standard` | PASS | With_skill explicitly classifies `change_tier: standard` and describes the request as a business-rule change. |
| `block_or_return_pm` | PASS | With_skill routes to `pm-agent:idea-to-spec`, requires scope confirmation, and states no direct implementation or merge; it asks the user to confirm scope. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e2b92bd08a5ef866a914879dd6c32025285b42153cdbaadd30b2c4e7c925e4ca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly rejects hotfix treatment, classifies the change as standard, and blocks implementation pending PM scope confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=60f5ec65f15f6a73ca1e7ba1c4a9e90a8dc580eef491e9dcd3514ddfd0fb03f7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reports an empty workspace and inability to modify or merge, without addressing the requested process assertions.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
