# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-018-scope-guard-explicit-invocation`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-18-scope-guard-explicit-invocation`.
- Identity schema: `2`
- target_skill_sha256: `a37bf10fca64a8e15e6213ecdd45b65783814d307c78fd8d8ce6ab45b20effef`
- eval_definition_sha256: `fbd5b3a5e4c0be83eacf913e76dfe890f776915d3d24ba4fd45c191e31196a40`
- metadata_sha256: `d008e123b4ee70f7bf43fcaf109d74c9d72e4654db9631f703b1f4b299706113`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3a5175573f5c12faf8ef17031068ea4a3554be3c63ea98a9f0e35a5de2fe7ef6`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34`
- Repository HEAD: `3f5e81c4837ef85284a7d5381575e40267796c92`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b63527fcaf0019710c1759725af4572c6d06eff41061de787b57dc1dae12ee7c`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `explicit_invocation_proceeds` | PASS | With-skill trace shows it read and applied pm-agent's entry rules, recognized the explicit invocation, honestly determined the request was outside PM's product/engineering scope, and performed no contradictory routing or file mutation. |
| `classifies_general_request` | PASS | With-skill trace explicitly records the classification as local file organization outside PM's categories and says it will not invent new_feature or delivery routing; it did not skip classification to execute file operations. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=81e25b33d580b5a083000609564f27d16ae32b9620ab0050bc7bcac8f4fc45ce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Used pm-agent, classified the explicitly invoked request honestly as outside PM scope, and stopped without unsupported file operations because Downloads was unavailable.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=916b7d46f32c52bb1b9ecfd40f51d98917fcbf3e5872a5e6261935a3e2fb0390; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reported pm-agent was unavailable and Downloads was inaccessible; it did not perform PM classification.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
