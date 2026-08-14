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
- target_skill_sha256: `af94ca4b38768885230f6271f3d4ae9e1b1be30fcd2f5bdf1098250b4ded0306`
- eval_definition_sha256: `8a4360282a35d2ba7a52bbb24d703648e9f263e7fbfc9516063ba62f62b92b92`
- metadata_sha256: `62050136e2c1de0d65367ed4b1b1b706bb2211c3759fb54a832b8fd66233328b`
- fixture_sha256: `f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `787b3941ec90b819758a9894561fa37e2c0eff7eedddb4c4a4d863809f28587f`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `cc06f7d0ec314789bbccd4de68e0c4e6f74c0821dbe36228153c86490ecf37d8`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_not_applicable_evidence` | FAIL | With-skill confirms static hosting, non-use of the application image/Compose/Helm, maintainer sign-off, evidence paths, and public/internal variants, but does not explicitly report the decision as not_applicable or identify the next owner (Web Platform). |
| `does_not_open_devops_handoff` | PASS | With-skill explicitly concludes that application deployment need not intervene, preserves the read-only boundary, and creates no repo-wide deployment handoff. The decision is presented as valid, so no user re-ask is required. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c; fixture_sha256=f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f; output_sha256=5e669be11e654e3531a9860bd1d0ee1858384f6894fa1dde8fe306179ebe7fa0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly preserves the static-hosting evidence and avoids DevOps escalation, but incompletely reports the required not_applicable decision record.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c; fixture_sha256=f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f; output_sha256=8cd0ff65fe8bfaf7089014fd6d0d2798b306660716a063740d3ad19c8d06738b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also avoids application-deployment escalation, identifies static-hosting evidence and variants less completely, and names Web Platform as the follow-up owner.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill report omits the required explicit not_applicable result and next-owner identification.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
