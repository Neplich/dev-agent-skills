# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-003-mapped-doc-exploration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421` from `agents/qa/test/exploratory-tester/evals/workspace/eval-3-mapped-doc-exploration`.
- Identity schema: `2`
- target_skill_sha256: `ad5f15f98798fd005013d9360ccfb1f546134b65d875e1399c704387da8bd759`
- eval_definition_sha256: `c4de00c65a5c492d58d182077c448786bbd54172790d4519f15e143439929064`
- metadata_sha256: `66549bc6a4cd28361d4fb0c300ac0600f32823bbce01dba9736725e4b2d843dd`
- fixture_sha256: `5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `1f8ea470403a23486f27834f156d91882ffb60f2aff635a7aa34b64347c884e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill trace reads the change map, then the mapped API document, then session.rules; no docs/site traversal is shown. |
| `verifies_against_code` | PASS | with_skill identifies the documented 15-minute value versus the code value of 10 minutes and uses 10 minutes as the exploration basis, including 9:59, 10:00, and post-threshold checks. |
| `treats_unverified_as_low_trust` | PASS | with_skill explicitly treats last_verified_version: unverified as low trust and requires code/test confirmation for behavior claims. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=aba012c6a9a4e1e50cbde12dcafd35fca9306881c713ca9c420c1adff5fe8b3b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced an evidence-backed minimal exploration charter using the mapped document, verified code threshold, documented discrepancy, and low-trust handling.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=51a51e32ce7642de38471f19af1ebe3d53eb92849ca54d90cc44ee241167b30d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also identified the threshold discrepancy and proposed boundaries, serving as a fresh baseline comparison.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
