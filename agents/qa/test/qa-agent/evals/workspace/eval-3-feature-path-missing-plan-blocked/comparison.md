# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc` from `agents/qa/test/qa-agent/evals/workspace/eval-3-feature-path-missing-plan-blocked`.
- Identity schema: `2`
- target_skill_sha256: `87273b18e32710512ee493a3e80a098f8b357ae29e71e4e0a6f3bdb4e8e38c08`
- eval_definition_sha256: `ec357d7e216245f12726027da14d7981d249bcac4a9eff1a2ed19f5ffc8af4f2`
- metadata_sha256: `aa798ca118679678c2fef882d4726badd357a387202dcb387aceaa4b86696bd0`
- fixture_sha256: `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7c827cee8609863280607c031efdc95a92d32b851664d68126eccd9d66c1f27a`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8bdd2e06aa5b2802048e58c95086ce3578e5b5c6997eaafa30b5cfbddd879d53`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_same_feature_path` | PASS | Trace shows direct reads of the same-path PRD, TRD, and QA directory; the handoff preserves feature_path account/profile/preferences and the QA path. |
| `specialist_gate_pointer` | PASS | The output selects spec-based-tester, identifies the missing IMPLEMENTATION_PLAN.md and blocked execution, and states that execution/assets belong to the specialist; trace shows no file-change or E2E execution event. |
| `keeps_single_route` | PASS | Only one QA route, spec-based-tester, is selected; the trace contains no parallel QA route, specialist execution, or implementation repair. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=129bc5ac1e11162e87317fc340802f641c4f53108da5ac01cec37a51f1956738; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Routes the request to the single narrow spec-based-tester specialist, preserves the feature path and QA context, and stops at the specialist gate with explicit blockers.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=b4adf397744257f7612029915c44f0a3f92b91ecace8e52c274b0ee2e6a77fa1; snapshot_sha256=04c5884ef54cdb3169b505d9cf6e41c54a8e87f3aef84ac34eaa589ea34dd9d5
- Behavior: Fresh baseline updated QA files and reported blocked E2E execution, but did not provide the specialist-gated single-route behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
