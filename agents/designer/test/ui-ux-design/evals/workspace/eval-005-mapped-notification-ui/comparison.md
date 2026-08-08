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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5df1c01e08aa97e9873a8076a8bc80b312ca23697bf7b8274e324d7feecebbd3`
- Skill overlay SHA-256: `91cbd0b25abda706f069ede3ae1d7e4f14e2da2a5a0702fbf7cbcb22b29ac6e2`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `25a9beaf5037d128f11073d7bdad29e775b60a170f80ba9b4b2cd556e1ef1469`
- Metadata SHA-256: `10998afd499537d318b7152b7f04f522887c53c432e959ff9a023e23e13617cb`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出说明命中了 change-map 和 required_docs，但锁定的原始证据无法证明实际读取顺序。 |
| `verifies_against_code` | PASS | 规格明确以 src/ui/notification-preferences.html 为事实来源，指出 checkbox 没有 checked 属性、实际默认关闭，并记录其与正式说明的冲突。 |
| `treats_unverified_as_low_trust` | PASS | 规格明确识别 last_verified_version: unverified，并要求在产品确认前保留代码所示的关闭状态，不直接采信文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a; fixture_sha256=cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a; output_sha256=c6f9994bb7b83ab812b1e9ffef0d9f3ff664f8aae3a8829a8815e0941356353c; snapshot_sha256=e375752963a407fb39e499d8d24a43fac146538dc9357cb5ebff6b97ab700be8
- Behavior: 生成了完整的 UI/UX 规格与前端交接说明，正确核对代码默认状态并记录 unverified 文档冲突，未修改源代码。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a; fixture_sha256=cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a; output_sha256=7b9420c1cb4350f98167d76e29f8de8e5320c274f233ca677f6c67c9edcfdde6; snapshot_sha256=c4578d43dd7b28ddfdee4730408bfaff45a9339e548dba04023e173fb17949cf
- Behavior: 完成了文档补充并正确识别代码中的默认关闭状态，但主要修改了正式说明。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **CLEAN**
- Target skill tree SHA-256: `55ad2c448de2c695b60ea88a19ae003113180ae2a2d97a343e4f35f303c19535`
- Skill overlay SHA-256: `fc3846cf4ed109d2936b6a81a0907b781f51176c2c40fb9bff4e0a41fc616558`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `25a9beaf5037d128f11073d7bdad29e775b60a170f80ba9b4b2cd556e1ef1469`
- Metadata SHA-256: `10998afd499537d318b7152b7f04f522887c53c432e959ff9a023e23e13617cb`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | The with_skill output identifies and uses the mapped required document, the source HTML, and the change map, with no unrelated formal documents evidenced. |
| `verifies_against_code` | PASS | It explicitly verifies that the HTML lacks checked and correctly concludes the browser-rendered default is unchecked despite the document stating enabled by default. |
| `treats_unverified_as_low_trust` | PASS | It notes the mismatch and treats the unverified formal document as intent requiring code confirmation, preserving the HTML fact as an open discrepancy. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a; fixture_sha256=cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a; output_sha256=b9bd31c10b2c26b8c6e3382ac987a8501abefc45fea695b5c39fab651d12eafe; snapshot_sha256=590e1cb8df87f9e9f122b3fa5a8c1fa8c9031efd0a0005c7f31968015a43e1ab
- Behavior: Created a dedicated UI/UX specification grounded in the mapped document and source HTML, explicitly documenting the default-state discrepancy and frontend handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a; fixture_sha256=cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a; output_sha256=124aa78cc1666f1a63641c3c2074c516d9de85b47dd0aed860c9b3305cf19efa; snapshot_sha256=d7abf900692409a197aef8a745ba4f321b29b462dc0ad456d37a231f7490a89e
- Behavior: Updated the mapped API document directly and identified the documented-default versus HTML-default mismatch.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
