# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-005-mapped-notification-ui`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a` from `agents/designer/test/ui-ux-design/evals/workspace/eval-005-mapped-notification-ui`.
- Fixture SHA-256: `cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a`
- Prompt SHA-256: `2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `78da31c45df217a9e90f29e80573d99066d6964c62a108fc4cb609c96341db51`
- Skill overlay SHA-256: `b9db71f44c6cca6e399d27edcc8fe58463a8d7a3c9a80f1728f1e7571f16e7df`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `25a9beaf5037d128f11073d7bdad29e775b60a170f80ba9b4b2cd556e1ef1469`
- Metadata SHA-256: `10998afd499537d318b7152b7f04f522887c53c432e959ff9a023e23e13617cb`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | The with_skill output identifies and cites the mapped required document docs/site/api/notification-preferences.md, and no unrelated formal documents appear in the evidence. |
| `verifies_against_code` | PASS | It explicitly reports that src/ui/notification-preferences.html lacks a checked attribute and correctly identifies the resulting unchecked browser default, contrasting it with the document's default-on claim. |
| `treats_unverified_as_low_trust` | PASS | It notes last_verified_version is unverified, treats the HTML as the current factual baseline, and defers adopting the documented default until product confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a; fixture_sha256=cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a; output_sha256=4543122e05df8795fab43e9055072ba8a8eb2e04b1d2d545774a59b32b4075b0; snapshot_sha256=4835b3b312efa83beec28fd2aa155f3980699450f8143efa3a65cad369a57a70
- Behavior: Produced a detailed UI/UX specification grounded in the HTML, identified the code/document mismatch, and treated the unverified document cautiously.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a; fixture_sha256=cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a; output_sha256=b28227420398078267cb299e07882e93c36fe4de216d25f207d9d749c7694244; snapshot_sha256=4d7b68187a19567654521c74009ce426b7e078b859ad63f9d9206fda4e3c8660
- Behavior: Produced a detailed spec and explicitly reconciled the documented default-on requirement with the unchecked HTML implementation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

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

# Eval Result: eval-005-mapped-notification-ui

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-005-mapped-notification-ui`
- Test case: Mapped Notification UI Documentation
- Workspace: `workspace/eval-005-mapped-notification-ui`

## Test Set or Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`
- Fresh run time: `2026-08-07 00:04:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/ui-ux-design/eval-005-mapped-notification-ui/`
- Fixture: `change-map.yaml`, mapped notification document, and notification-preferences HTML

## Latest Result

- Behavior result: **PASS**
- Coverage result: **PARTIAL** (2/3 assertions exercised; read-order evidence unavailable)
Overall result: PASS (partial coverage)

## Assertion Results (Current)

- reads_mapped_docs_first: **NOT EXERCISED** — current runtime evidence proves the mapped document was read and no unrelated formal document was used, but no persisted transcript proves read order.
- verifies_against_code: **PASS** — the candidate identifies the unchecked HTML control and reports the conflict with the document's enabled-by-default claim.
- treats_unverified_as_low_trust: **PASS** — last_verified_version: unverified triggers code verification and prevents blind trust in the formal document.

## With-Skill Behavior (Current)

The candidate correctly applies the low-trust and code-ground-truth rules,
reports the discrepancy, and stops at the missing feature-path gate. The
mapped-document-first ordering assertion could not be independently verified
from the retained runtime evidence.

## Fresh Without-Skill Baseline (Current)

The baseline was generated before the with-skill root existed, with the same
prompt and fixture in an independent top-level workspace under isolated
HOME/CODEX_HOME. It edits the HTML to match the stale document, demonstrating
the skill's code-ground-truth value; baseline behavior does not set Overall.

## Failures (Current)

- No behavior failure on exercised assertions.
- Coverage gap: read order was not retained as judgeable transcript evidence.

## Next Steps (Current)

- Persist the fresh lane transcript on the next run to exercise reads_mapped_docs_first.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All three consumption-contract assertions were exercised.

## Assertion Results

- `reads_mapped_docs_first`: **PASS** — the task path is reverse-mapped to the sole required document, with no unrelated formal-doc traversal.
- `verifies_against_code`: **PASS** — the document says enabled by default while the checkbox lacks `checked`, so the current static markup is unchecked.
- `treats_unverified_as_low_trust`: **PASS** — `last_verified_version: unverified` triggers code verification of every key claim rather than blind trust or refusal.

## With-Skill Behavior

- Preserves a structured discrepancy containing the documentation claim, HTML fact, and design impact.
- Correctly stops at the PM handoff/feature-path gate instead of inventing a design artifact path.
- The reached consumption and gate behavior does not use BRD; its removal causes no difference.

## Fresh Without-Skill Baseline

- This baseline was newly generated in this run from only the same prompt and fixture; it did not apply the Designer README, skill, consumption contract, with-skill output, or old comparison.
- It notices the unchecked HTML control but does not systematically establish mapped-document-first ordering, lowest trust for `unverified`, or structured discrepancy evidence.
- It contains no BRD reference.

## Failures

- None.

## Next Steps

- No skill or fixture correction is required for this case.

## Runtime Artifact Policy

- Runtime candidates, fresh baseline, and judge evidence remain under the ignored runtime directory and are not committed.
- Only this durable `comparison.md` is updated.
