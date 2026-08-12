# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-agent/evals/workspace/eval-002-missing-entry-basis`.
- Identity schema: `2`
- target_skill_sha256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- eval_definition_sha256: `46e0e02295d606a359a2403ac234af592712f357041b544bb13a82efa1816296`
- metadata_sha256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `da898e3ecfd0169570b22be7c73cd730ef2fd22e3bf1c5b559383dc76454ff0d`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | PASS | The with_skill output states no PM handoff/equivalent confirmed chain/specialist basis is present, names pm-agent as return owner, and directs completion through PM context before execution. |
| `does_not_execute_bootstrap` | PASS | The with_skill output explicitly sets the execution boundary to routing only, with no file creation, repository writes, deployment, or bootstrap execution; git evidence shows no changes. |
| `names_missing_credentials` | PASS | The with_skill output names the missing confirmed host repository path and states that an explicit site request plus that path completes the docs-site-bootstrap entry basis. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8a665c7632c31fce83103a67e411115fa7f6c456ea2edd0094ff12d3cf4e103; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c4df99f3715647d3c3ec3679757f119099237dfecc7ab1b7c282435b7baed6ff; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks downstream bootstrap, routes to docs-site-bootstrap, guides return to pm-agent, and names the missing host repository path and unblock combination.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8a665c7632c31fce83103a67e411115fa7f6c456ea2edd0094ff12d3cf4e103; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b3fa782b947e607f39324cd7245bfaad78422dc356de71669e5346ff20e32986; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a general workspace assessment and lists missing repository and project decisions, but does not provide the required PM routing or explicit specialist entry-basis guidance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
