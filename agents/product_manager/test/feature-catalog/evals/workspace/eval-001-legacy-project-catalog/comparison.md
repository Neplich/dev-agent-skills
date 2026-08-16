# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-001-legacy-project-catalog`.
- Identity schema: `2`
- target_skill_sha256: `7440f3be22fb3254e3abf20bcd1c6ebca9f2fdee2fae7f710cc03af349b94250`
- eval_definition_sha256: `6316196cbc0024d8a369162c20842d191078adb23f3f59cfbc5541923081da5e`
- metadata_sha256: `aa9b419ec00ff2ce5f9c2775fc1e620cf1eb45a8d316e5adf573b14f5b74c3e2`
- fixture_sha256: `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6731c51ff9f69981e5ade0a40fa5fb4f93b6c439e428212a1b46155c6fa123f1`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `855b39267bf29cb8319dc4bcf28cd88b5cba0ad0d7279c117acb672b2cd4540b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `draft_before_formal_docs` | PASS | With-skill output is explicitly labeled “功能目录草案（待确认）”; locked git evidence shows no worktree changes or delivered docs/pm files. |
| `evidence_and_confidence` | PASS | Each of the three candidate features includes evidence categories drawn from the fixture and a low confidence label. |
| `business_capability_naming` | PASS | Features are named as customer-facing capabilities such as 客户身份认证、订单创建与查询、订单状态通知; code paths are listed separately as evidence. |
| `open_questions_present` | PASS | Each candidate includes open_questions addressing uncertain boundaries or scope. |
| `confirmation_gate` | PASS | The output ends by asking the maintainer to confirm feature_path values and explicitly states that docs/pm/FEATURE_CATALOG.md and PRD/TRD handoff will wait until confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=aa4bd23dddb8d8033b7c4505ed46049467015746f15aea7c45cdd0c965c583e8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced an evidence-backed, low-confidence feature catalog draft with unresolved questions, no formal-document mutation, and a confirmation gate.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=7cc1b50f12fede2c8bb03c50628838f75b44bdf42f5f53ad33482a5aba2aaacf; snapshot_sha256=d36c9a38b59288bf6e074c1b8081d7d41037f2a27da53da746c712c673b88700
- Behavior: Created a formal feature catalog immediately and presented completed findings without a pending-confirmation draft gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
