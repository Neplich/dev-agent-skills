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
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `ba37454a106688e9f5f2e2586231a60f2093e364612eb14bfa53540c9e2d1589`
- metadata_sha256: `fe53b448dd4fd2693ceb179d875dd617b7b717601fc7d9d3214cab940b4cdef7`
- fixture_sha256: `1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c8400122a967de4e5b8b409bbe920fe16ec946724a3aa7d4b3077b3582a3f2f0`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `320ded3db25222eda1be26706a57ed0471cc438157b54925db0b045d15abf8e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_structure_governance` | PASS | with_skill raw trace loads routing guidance stating read-only document structure governance stays in idea-to-spec:structure-governance; the structure-governance lane is selected and executed. |
| `read_only_audit` | PASS | with_skill output states the check is read-only and the locked git evidence shows unchanged HEAD, branch, status, index, worktree, and no untracked files. |
| `report_form` | PASS | with_skill raw trace records creation of structure-governance-report.html under a runtime tmp directory; the HTML content is present in locked command output, and the conversation output provides a conclusion summary and report path. |
| `scope_six_role_dirs` | PASS | The locked HTML report contains columns for PM, Engineer, Design, QA, DevOps, and Security, explicitly records the four absent roots as scan limitations, and the trace inventories the existing docs tree. |
| `structural_change_requires_confirmation` | PASS | The locked HTML report and conversation output recommend no merge/split/move, state that future structural changes require PM confirmation and change_tier major, and raw git evidence shows no mutation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3; fixture_sha256=1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8; output_sha256=992e52b64f40d738c3e6a672ef90de5d5eaeffee443fd3a8e2059c4fdc503cf0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Read-only structure-governance audit routed through the correct lane, produced a runtime HTML report, summarized findings, documented all six role roots including missing-root limitations, and made no repository changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3; fixture_sha256=1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8; output_sha256=f44d268397d5ae6efe0b23c144a629a6a8243a2a9550b19c13c981f381d71bfd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline produced a read-only prose audit of only the two existing role directories, with no HTML runtime report and no explicit six-role governance coverage.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
