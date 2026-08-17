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
- target_skill_sha256: `023cc6d8aa109db6ff7dcd662df567ae4f0c79dddb66dfe7bcf6f1eb91d20f39`
- eval_definition_sha256: `46e0e02295d606a359a2403ac234af592712f357041b544bb13a82efa1816296`
- metadata_sha256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `da898e3ecfd0169570b22be7c73cd730ef2fd22e3bf1c5b559383dc76454ff0d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c8a665c7632c31fce83103a67e411115fa7f6c456ea2edd0094ff12d3cf4e103`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `9c576146684d18c7504052238ca8bebbfdee0dbeda9095dc883a11efcc91b8a9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | PASS | With-skill output identifies the missing PM handoff/confirmation basis and names pm-agent as the return owner; trace corroborates routing back to PM. |
| `does_not_execute_bootstrap` | PASS | With-skill delivery_snapshot and git evidence show no changes; output does not claim bootstrap execution or generate a manifest, and the trace only loads the docs-agent routing skill. |
| `names_missing_credentials` | PASS | With-skill output explicitly names the missing confirmed target repository path and states that an explicit initialization request plus confirmed host repository path supplies the entry basis. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8a665c7632c31fce83103a67e411115fa7f6c456ea2edd0094ff12d3cf4e103; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=2cba0bf478e9f967d913d0a1d6e5a4fc39b35fd7473000c5856ea5b501d04bf7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the incomplete formal documentation-site request back to pm-agent, preserves the execution boundary, and identifies the missing repository and PM confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8a665c7632c31fce83103a67e411115fa7f6c456ea2edd0094ff12d3cf4e103; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5be83ae4b0059b50b0c85a562e1a34537d29e1f0c8c405880e141be4fe458290; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a generic planning-oriented response and identifies a missing repository, but does not provide the explicit PM routing and specialist entry-basis guidance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
