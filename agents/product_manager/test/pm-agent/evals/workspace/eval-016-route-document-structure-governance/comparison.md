# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-016-route-document-structure-governance`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8` from `agents/product_manager/test/pm-agent/evals/workspace/eval-016-route-document-structure-governance`.
- Identity schema: `2`
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `ba37454a106688e9f5f2e2586231a60f2093e364612eb14bfa53540c9e2d1589`
- metadata_sha256: `fe53b448dd4fd2693ceb179d875dd617b7b717601fc7d9d3214cab940b4cdef7`
- fixture_sha256: `1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c8400122a967de4e5b8b409bbe920fe16ec946724a3aa7d4b3077b3582a3f2f0`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `15f4acf7caf3d5cd73abf45c67ad35faa887bc8f89f51c7e53854fb1514182b5`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_structure_governance` | PASS | With-skill trace reads the pm-agent routing rules, which explicitly route read-only document structure governance to idea-to-spec:structure-governance. |
| `read_only_audit` | PASS | The with-skill output explicitly states the audit was read-only and documents were not modified; git evidence shows unchanged HEAD, clean docs state, and no diffs. |
| `report_form` | PASS | Locked trace evidence shows an HTML report was written under /tmp, verified to exist, and checked for report sections; the output provides its path and summarizes conclusions. |
| `scope_six_role_dirs` | PASS | The with-skill output and HTML report explicitly cover docs/pm, docs/engineer, docs/design, docs/qa, docs/devops, and docs/security, recording absent roots as scan limitations. |
| `structural_change_requires_confirmation` | PASS | The output proposes no structural action and states that later structural work requires confirmation and change_tier: major; the HTML report likewise says it does not authorize execution. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3; fixture_sha256=1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8; output_sha256=b3a6d54d72516308cd4094b32daf702055e6ce76651dda95d60a065f572b4754; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Completed a read-only six-role structure audit, delivered a runtime HTML report, summarized findings, and preserved structural changes behind confirmation with major-tier handling.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3; fixture_sha256=1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8; output_sha256=9505ee229b1b8a4841760030eb4631a55043bb8d7baf2bd756131a86fa64436c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a read-only prose report covering only the two existing role directories, with no runtime HTML report or six-role scan.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
