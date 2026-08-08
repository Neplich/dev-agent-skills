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
- Fixture SHA-256: `177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960`
- Prompt SHA-256: `8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9c3b136c6958582b2c5c3d552759bbe4fd3ef24876075804e91c5b21980a34af`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `130498c1a4cc1643bdf013127365b28e5fdc8391203daf304f2cdc0ef5bc97d2`
- Metadata SHA-256: `071b1907c18a80afba8338dbc482c47ee9a6fa479b963c4fb7d1e4c62363e556`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill artifacts identify the notifications change-map requirement and the mapped notifications API document, with no unrelated site pages used. |
| `verifies_against_code` | PASS | With-skill output explicitly confirms channels.txt contains only enabled_channel: email, identifies the undocumented-by-code webhook claim, and treats code as authoritative. |
| `treats_unverified_as_low_trust` | PASS | With-skill PRD explicitly notes last_verified_version: unverified and bases current-state conclusions on the code evidence, leaving unsupported provider and workflow details as open decisions. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274; fixture_sha256=177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960; output_sha256=816e5e4d28adb7ac3e0708d6b40c5a216c1b54c2b126444e08c092702575459e; snapshot_sha256=d62d607b34288d5baddb0fa801deb6f504885edaeeae2135ab0792ca765986a2
- Behavior: Created Draft PRD and decision log grounded in the mapped documentation and channels.txt, explicitly reconciled the webhook discrepancy, discounted unverified documentation, and recorded open decisions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274; fixture_sha256=177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960; output_sha256=a19dd2c16d2b99f82f004425fe77c722f30fd9026ab63607304b81d1738246f1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline correctly inspected the mapped documentation and code, but produced a broad scope without explicitly framing the unverified document as lower-trust or separating unconfirmed decisions as rigorously.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-008-mapped-notification-update

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: PASS — 3/3 assertions passed.
- Coverage result: FULL — all 3 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `reads_mapped_docs_first`: PASS — the trace read the mapped notifications page before `channels.txt` and did not traverse unrelated site pages.
- `verifies_against_code`: PASS — code showed email only and the response preserved the webhook documentation conflict.
- `treats_unverified_as_low_trust`: PASS — the unverified page was treated as low trust and checked against code.

### With-Skill / Baseline Comparison

The with-skill response stayed read-only and formed the SMS-channel update scope from mapped docs plus code truth. The baseline edited the documentation directly; it is comparison evidence only.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-008-mapped-notification-update/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-008-mapped-notification-update`
- Workspace: `workspace/eval-008-mapped-notification-update`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; notification source, change map, `unverified` API page, and email-only code fact.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-008-mapped-notification-update/`

## Latest Result

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `reads_mapped_docs_first`: PASS — maps `src/notifications/` to and reads only `docs/site/api/notifications.md`.
- `verifies_against_code`: PASS — treats `channels.txt` email-only state as ground truth and reports webhook drift.
- `treats_unverified_as_low_trust`: PASS — explicitly gives the unverified page the lowest trust and rechecks all key facts in code.

## With-Skill Behavior

The response preserves the mapped-document-first and code-ground-truth protocol, structures the email/webhook discrepancy, and frames SMS as an `existing-project-update` whose stable product facts belong in PRD/DECISIONS. No BRD stage or artifact appears.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. Strong fixture cues led it to the correct factual discrepancy, but it did not establish the same precise consumption order, trust model, or single-decision update protocol.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no evidence-consumption regression.

## Next Steps

- Keep this eval as coverage for change-map consumption and code verification feeding directly into PRD/DECISIONS scope.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-008-mapped-notification-update/` and are not committed.
