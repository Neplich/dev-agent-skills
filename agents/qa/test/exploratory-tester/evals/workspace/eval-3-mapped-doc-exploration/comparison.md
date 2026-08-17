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
- target_skill_sha256: `a0ccbf8ef4a1c709d054888b55b087565575c66027bff8bd5b33273b116324d3`
- eval_definition_sha256: `c4de00c65a5c492d58d182077c448786bbd54172790d4519f15e143439929064`
- metadata_sha256: `66549bc6a4cd28361d4fb0c300ac0600f32823bbce01dba9736725e4b2d843dd`
- fixture_sha256: `5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `649841709df98de32c59aff088c94eff0d9bbe6820d42c21a8e49cd3cf9838cb`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill trace reads the mapped formal document and only the checkout-related files; no broad docs/site content traversal is shown. |
| `verifies_against_code` | PASS | with_skill trace directly reads src/checkout/session.rules showing 10 minutes, reads the formal document showing 15 minutes, and the output uses 10 minutes as the exploration basis while preserving the discrepancy. |
| `treats_unverified_as_low_trust` | PASS | with_skill output explicitly treats last_verified_version: unverified as low trust, uses code as the behavior baseline, and routes the documentation discrepancy for audit. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=1863b0ac0878d076473b3e88135ac97e6df5c864dd23cc05f9f51e437224cf77; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly maps the checkout rule to the required document, verifies the 10-minute code value against the 15-minute documentation value, treats unverified metadata as low trust, and proposes focused boundaries. No runtime exploration was executed.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=6e15a4c72c308252a206a22ded59b171784c05815484c72705a074d56c2188dc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also identified the 10-minute code value and 15-minute documentation drift and proposed boundaries, but without the skill-specific preflight and routing context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Execute the proposed runtime boundary checks when the required harness or user confirmation is available.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
