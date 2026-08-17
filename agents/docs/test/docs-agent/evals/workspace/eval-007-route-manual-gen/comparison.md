# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-007-route-manual-gen`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8` from `agents/docs/test/docs-agent/evals/workspace/eval-007-route-manual-gen`.
- Identity schema: `2`
- target_skill_sha256: `023cc6d8aa109db6ff7dcd662df567ae4f0c79dddb66dfe7bcf6f1eb91d20f39`
- eval_definition_sha256: `b572bcf4c18451eca03023d64515c12cbfbd9f67b27200f6bcd78820652e00b9`
- metadata_sha256: `31c2720a1114e612336c51527d7aae20dddb1f4e46b566ffffe4788d27952b8e`
- fixture_sha256: `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `dfbcad96e39d7a0ba2503c7d345d86b54a6c9e1188ff1c09f99476b24380e820`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `1fd712d33d9c027bbddf431b7e1d0692e12253350db6a00382930fc1f0850317`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_manual_entry_basis` | PASS | with_skill explicitly identifies the complete handoff basis, including host repository, bounded scope, running-interface evidence, and required output. |
| `routes_manual_gen` | PASS | with_skill explicitly routes the work to manual-gen and does not select any alternative specialist. |
| `preserves_manual_handoff_context` | PASS | The with_skill handoff reproduces all required fields: request_type, change_tier, feature_path, host_repository, manual_scope, evidence_sources, required_output, and blockers_risks. |
| `references_manual_gate_only` | PASS | The candidate stops at the router boundary, identifies manual-gen as the next responsibility, exposes no local SKILL.md path to the user, and locked git evidence shows no file or repository mutation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=ddc01c283cc36886db67f4c237f9ebb01423fe7914aa1b388822cde9a27b4f41; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly validates the manual handoff, preserves its context, routes to manual-gen, and stops before specialist execution or mutations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=b569d2bc62dbf5ab493222c59842b2d5bd1d5cc2f9bd62935cd949872c3b98d3; snapshot_sha256=c248224b27a26693e51dd5586a8e23ce1d795caeb296fcbf95fcff16f4c683fb
- Behavior: Fresh baseline incorrectly claims to have completed manual generation and contains delivered manual files, rather than remaining at the routing boundary.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
