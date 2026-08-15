# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-004-catalog-mapped-billing-feature`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-004-catalog-mapped-billing-feature`.
- Identity schema: `2`
- target_skill_sha256: `217c9b057b0819a52534f84f10e4d4a1bc905c2af1e21214f5f09bf51cb17566`
- eval_definition_sha256: `8d7030970f6fab5f1056baaa7f97792f12e093b11e3211055d5ae790cf0d3bc2`
- metadata_sha256: `b6e639db89ad7dc9c01b74ff5037844027a7f93b1a684864779b0328b14ee4bc`
- fixture_sha256: `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6cef39f1b1cce23592397054fa6d427258c02b6778c43df49e227da056eafd0d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With_skill trace shows the change-map was read for `src/billing/**`, then the mapped `docs/site/api/billing.md` was read; no unrelated document contents were traversed. |
| `verifies_against_code` | PASS | The delivered output preserves the documentation path and claim (monthly and annual), the code path and fact (`service.txt` supports only monthly and `create_subscription`), and the resulting discrepancy/open confirmation question. |
| `treats_unverified_as_low_trust` | PASS | The output explicitly marks `last_verified_version: unverified` as low trust and states that conclusions are based on code evidence, while recording annual as unconfirmed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=4ea4cc2236f98583d7213396674363d178f58bfbbc1fb4820a9dba034930cb67; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a cautious, code-grounded billing feature catalog, preserved the documentation/code discrepancy, and gated the result pending confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=c094e58d090cd2021a96b059dd7823906f271d22bcf3ae489c192eba69b869ca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a broader billing inventory and independently identified the monthly-versus-annual discrepancy, but did not follow the mapped-document-first workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
