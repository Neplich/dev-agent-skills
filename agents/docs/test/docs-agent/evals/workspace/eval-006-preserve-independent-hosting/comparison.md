# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-006-preserve-independent-hosting`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f` from `agents/docs/test/docs-agent/evals/workspace/eval-006-preserve-independent-hosting`.
- Identity schema: `2`
- target_skill_sha256: `cf826e2e86ef193d8a7294a87c743dead6af892aefcc220dd56ae949fa5c3b40`
- eval_definition_sha256: `8a4360282a35d2ba7a52bbb24d703648e9f263e7fbfc9516063ba62f62b92b92`
- metadata_sha256: `62050136e2c1de0d65367ed4b1b1b706bb2211c3759fb54a832b8fd66233328b`
- fixture_sha256: `f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `787b3941ec90b819758a9894561fa37e2c0eff7eedddb4c4a4d863809f28587f`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `4a886ffdcb18b30d43dbd2f9ee95780d97f9d5daf71fdddfd34bccc37d3c110d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_not_applicable_evidence` | PASS | With_skill reports `not_applicable`, cites hosting/decision-record.md, identifies the static workflow's public/internal variants, and names the repository maintainer/documentation publisher as the next owner. Raw fixture evidence confirms the maintainer-signed static-hosting decision and both variants. |
| `does_not_open_devops_handoff` | PASS | With_skill concludes no application deployment-team involvement is needed, records no handoff or delivered mutation, and confirms the valid not_applicable decision does not trigger a deployment route. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c; fixture_sha256=f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f; output_sha256=1c8974593b946335d22501053cb3b2f55854e5ff07091dfae93319e2fb5a4e61; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Preserved the valid not_applicable hosting decision, its evidence, variants, and next owner; avoided a DevOps handoff while accurately noting missing workflow inputs.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c; fixture_sha256=f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f; output_sha256=e5b87d70da99aede513f770767e27d9c81d0a8ede81a5b47dc79d6fcaa33e787; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reached the same no-DevOps conclusion and identified hosting evidence, but did not explicitly report the required not_applicable status or structured next-owner evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
