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
- Repository HEAD: `b385df5d17058a52081357c8a8480fc146c3d989`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ecf67dca8a2fd53bb0dd6d0a63750ba2716e88dc4af4f77176ea061260d64286`
- Skill overlay SHA-256: `2ed9fef9a54be8009ea156c857682ad7dd82c0e56e3463d3257fe74fe9c977ec`
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
| `reject_hotfix_abuse` | PASS | with_skill output explicitly states `hotfix_disposition: rejected` and says the request cannot be handled as hotfix. |
| `expectation_change_standard` | PASS | with_skill output states `change_tier: standard` and identifies the request as a business-rule change requiring PM scope and approval alignment. |
| `block_or_return_pm` | PASS | with_skill output selects `pm-agent:idea-to-spec`, requires confirmation, requests the correct project/documents, and states no code modification, testing, commit, or merge will be performed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6ada419a462bdc864b0291d80089c304774ea4d2b35c30a7936e58040fbcea30; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly rejected hotfix treatment, classified the change as standard, and blocked implementation pending PM scope confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=bc9d36fd1a40a6e8c4c4321a35d6880930f3ec719b84744f636467a9442cfd40; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reported the empty repository and requested a correct repository/branch, but did not explicitly classify the request or reject hotfix handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
