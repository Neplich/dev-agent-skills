# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-001-gdpr`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-001-gdpr`.
- Identity schema: `2`
- target_skill_sha256: `2d9aa34423715a24783169e774af3c68a95cbc320b5fc5af4b5753bd7785f2a0`
- eval_definition_sha256: `3e00fd5f68469b1dbad14f0a400fd8e41079d5a8aa0df077168fd2333bd41a39`
- metadata_sha256: `4d071b9edabea5e4f158bcdc27c2e5647782f2e593dd3fe3c48f455551d94297`
- fixture_sha256: `fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `2eea2d31331dfff7d98326573b856ca9f269bca068d5f182bf99e8b0d5d75219`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | The locked privacy-map.md inventories name, email, IP, User-Agent, userId, and account_created, with code/config/PRD entry points and purposes. |
| `sharing_and_retention` | PASS | The report identifies ExampleAnalytics sharing, enabled-by-default/no-consent configuration, null retention, unknown database/log retention, and missing deletion synchronization. |
| `user_rights` | PASS | The report explicitly checks access, deletion, export/portability, and correction, and documents the absence of supporting interfaces or synchronization flows. |
| `compliance_gaps` | PASS | The locked report provides prioritized remediation covering consent, minimization, retention/deletion, rights workflows, vendor governance, logging, and an onboarding/upcoming-release decision. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=6ff6377ae679598bb3b5be3ddd3c3440cb561ac0ccabdb745aa681f3d2e7fecd; snapshot_sha256=3e7e3db3a884dccbccc11c27ea76d74fdcf6e9fb35ae47d06ab7e3860dbefb19
- Behavior: Delivered a traceable privacy-processing report with evidence-backed inventory, risks, rights gaps, prioritized recommendations, and handoff context.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da21f882704758587ca44f889b8ee407dbf02d8334de8546d9781960b0a34c12; fixture_sha256=fc7c85721e9b7bd81a9ba3e487c8f00f57880deb91ce00e1ae1258884cc231db; output_sha256=032f3329fceab7d051763d5b228881068a76074c57223de754cf167318dcaf37; snapshot_sha256=71ea472ea0e9f92baed7af5b2ee3b2fffb7b774c58ecdb11b3dea2c7f4889256
- Behavior: Delivered a comparable privacy-processing report covering the requested areas and an explicit do-not-launch conclusion; less structured than the with_skill report.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
