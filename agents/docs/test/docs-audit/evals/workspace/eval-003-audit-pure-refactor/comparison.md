# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-003-audit-pure-refactor`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677` from `agents/docs/test/docs-audit/evals/workspace/eval-003-audit-pure-refactor`.
- Identity schema: `2`
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `a7212e3282f2eaaa660e0675fb965d5050f366a07c153f3821d78fdab8976de5`
- metadata_sha256: `1e20c97bb5ffc477023f6bbbd217e71d747297cb0b8f52652660b6b2d10adc7a`
- fixture_sha256: `a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3e58dae2a34edb25f9589f7bddb4e3282cd1f66e3b0c3f35187db4ed16fd5f23`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `sends_refactor_suspect_to_fact_layer` | NOT_EXERCISED | Raw trace does not independently prove the hidden suspect-to-fact-layer handoff; only process narration and skill instructions are present. |
| `classifies_accurate_refactor_verified` | PASS | The with_skill output explicitly concludes the page is `verified` and lists matching GET path, optional limit, 200 response, and 400 error evidence. |
| `does_not_force_noop_doc_edit` | PASS | The with_skill output explicitly states `documentation_change_required: false` and explains that the change is a pure implementation refactor. |
| `does_not_block_for_unchanged_accurate_doc` | PASS | The with_skill output does not classify the page as stale; it reports `verified`, blocks only because required release-version surfaces and persistent handoff evidence are absent, and does not return `ready_for_tag`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f; fixture_sha256=a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677; output_sha256=26de41473f0f1f09dea0b35f97823d91fd2722bc062a3ccab5939d39f074a209; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly verifies the unchanged API contract, avoids a no-op documentation edit, and blocks only on incomplete release-version evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f; fixture_sha256=a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677; output_sha256=229ae28026b58e54f9ad9bcc0874c3e4f16db4854f9fe3f21e2b8774e34b8b16; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline incorrectly treats the audit as passed and does not identify the affected page as suspect or the release evidence gap as blocking.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
