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
- target_skill_sha256: `cf826e2e86ef193d8a7294a87c743dead6af892aefcc220dd56ae949fa5c3b40`
- eval_definition_sha256: `b572bcf4c18451eca03023d64515c12cbfbd9f67b27200f6bcd78820652e00b9`
- metadata_sha256: `31c2720a1114e612336c51527d7aae20dddb1f4e46b566ffffe4788d27952b8e`
- fixture_sha256: `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `dfbcad96e39d7a0ba2503c7d345d86b54a6c9e1188ff1c09f99476b24380e820`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `5604a6302ca4d09e2d73851673d45c2cd4c3d0cc0d875a00b8fdf3d59b145d56`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_manual_entry_basis` | PASS | The locked with_skill output and trace identify `manual-handoff.md` as satisfying the `manual-gen` entry basis, including the existing `docs/site/` foundation, bounded scope, confirmed running interface, and required output. |
| `routes_manual_gen` | PASS | The with_skill output explicitly states “路由结果：`manual-gen`” and names `manual-gen` as downstream owner; no alternative specialist is selected. |
| `preserves_manual_handoff_context` | PASS | The locked YAML preserves `request_type`, `change_tier`, `feature_path`, `host_repository`, `manual_scope`, `evidence_sources`, `required_output`, and `blockers_risks` from the fixture, with the host foundation represented separately as `docs_site_foundation`. |
| `references_manual_gate_only` | PASS | The with_skill output states `authorization_boundary: 仅完成路由；未写入站点、未生成手册`, identifies `manual-gen` as the next owner, and does not expose a local SKILL.md path or claim screenshot/site-generation/audit work. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=6f24e0714694f952455527b3d7a538801893d63f467c7cd29ed03dcd8092253e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly validates the handoff basis, preserves the required context, routes to manual-gen, and stops at the router boundary without generating the manual.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=b37780afd3e109d2b7c32043086222c5fcdc996513c167a39a359c3ceaf0a62e; snapshot_sha256=7d948be543a884e6f9549de8400cc160792be324ad1cf587f8324e67a13ed3a6
- Behavior: Generated and wrote a complete manual with SVG illustrations despite the fixture stating that the docs/site foundation and screenshots/manual body were not yet available; it did not perform the required router-only handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
