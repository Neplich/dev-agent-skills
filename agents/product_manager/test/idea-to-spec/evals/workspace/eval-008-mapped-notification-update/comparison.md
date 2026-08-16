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
- target_skill_sha256: `62f7a88900be8a0aae1af9e34b28dc32abd76006ca95f89107567b68f5780813`
- eval_definition_sha256: `130498c1a4cc1643bdf013127365b28e5fdc8391203daf304f2cdc0ef5bc97d2`
- metadata_sha256: `071b1907c18a80afba8338dbc482c47ee9a6fa479b963c4fb7d1e4c62363e556`
- fixture_sha256: `177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7b19869a4835a1feeb491815cac7af7bde071247819525989c10dbfbc0acd2f7`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Raw trace shows the change-map was inspected for `src/notifications/**`, then the mapped `docs/site/api/notifications.md` was read; no unrelated site pages were traversed. |
| `verifies_against_code` | PASS | The locked fixture and trace show `src/notifications/channels.txt` contains only `enabled_channel: email`, while the mapped document claims email or webhook; the with_skill output explicitly treats code as authoritative. |
| `treats_unverified_as_low_trust` | PASS | The with_skill output explicitly identifies `last_verified_version: unverified` and lowers the document to navigation-only trust, grounding current behavior and impact in `channels.txt`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274; fixture_sha256=177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960; output_sha256=970e4911d8707d4a0cd2462be88d2a42fb2ee4d492427de31c0fb7b6b0e90253; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a trace-backed requirements scope, identified the email-only code/document webhook mismatch, and treated unverified documentation as low trust without mutating the fixture.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274; fixture_sha256=177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960; output_sha256=5c10e8658155da9a72033ed4360da2602aa9922a7b7df6af9a30e78ad0965a7a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a plausible requirements scope and identified the email/webhook mismatch, but lacked the explicit mapped-doc-first and low-trust process evidence present in the with_skill lane.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
