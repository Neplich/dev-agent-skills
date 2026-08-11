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
- Repository HEAD: `e2d0e3e00078c297194828182b4d6445ecbb492d`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c658e8351498435bd5246b692fbf8a3a6d40caa45d6998b37785e6522243068b`
- Skill overlay SHA-256: `6e906e23fd0805526cda111a5e2e74eb02ce2f72534b3e384e90b10a34160090`
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
| `reject_hotfix_abuse` | PASS | with_skill output explicitly states `hotfix_disposition: rejected`; the locked trace repeats this routing decision. |
| `expectation_change_standard` | PASS | with_skill output explicitly states `change_tier: standard` and describes the request as a business-rule change. |
| `block_or_return_pm` | PASS | with_skill output sets `entry_basis: blocked`, selects `pm-agent:idea-to-spec`, requires PM scope confirmation, and prohibits direct implementation or merge. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fa86f3ec61d1d832f22173b37fdd9d5088a328c60ebc5ef8eefe7b5158ee89c7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly rejects hotfix handling, classifies the change as standard, and blocks implementation pending PM scope confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f96e30bcd5c8c7a6d28d3d2758d1358fbd3adaea681ab152c6ff37b548a5318b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline reports the empty repository and requests the correct project code, but does not address hotfix abuse, standard classification, or PM gating.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
