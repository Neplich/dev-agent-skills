# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-008-mapped-notification-update`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960` from `agents/product_manager/test/idea-to-spec/evals/workspace/eval-008-mapped-notification-update`.
- Identity schema: `2`
- target_skill_sha256: `0f0c72145289aa20c9f9e2b8953104e7776465f3453dfea622022098ed6ce507`
- eval_definition_sha256: `130498c1a4cc1643bdf013127365b28e5fdc8391203daf304f2cdc0ef5bc97d2`
- metadata_sha256: `071b1907c18a80afba8338dbc482c47ee9a6fa479b963c4fb7d1e4c62363e556`
- fixture_sha256: `177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `c40e2467241d61e6995a6131388bc32d701c6b675b7822ba6b51ce9428570cb3`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Raw trace shows the lane identified src/notifications/**, read change-map.yaml, then read the mapped notifications.md before source verification; no unrelated site pages were traversed. |
| `verifies_against_code` | PASS | The locked output and raw trace both establish channels.txt contains only enabled_channel: email, while notifications.md claims email or webhook; the lane explicitly treats code as authoritative. |
| `treats_unverified_as_low_trust` | PASS | The locked output explicitly states last_verified_version: unverified lowers document trust and bases current behavior on code evidence; the raw trace confirms this reasoning. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274; fixture_sha256=177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960; output_sha256=b29a79881c81233b4f248a87bef4d0564c3675153a2ff11d6a76e68e793df970; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly mapped the change-map, read the required notification document, verified behavior against the source fixture, identified the documentation conflict, and treated unverified documentation as low trust.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274; fixture_sha256=177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960; output_sha256=c61cb54b577b58b0cb2f636003979c99ab7ac858d0b9b84756e7969a3423e460; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also identified the email-only source configuration and email/webhook documentation mismatch, but did not establish the mapped-document-first process or explicit low-trust handling as clearly.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
