# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-014-existing-site-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-014-existing-site-deployment-recheck`.
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `db9d705a02de2df76d9e1b62334995eac21d110dc172ed350d92306793043708`
- metadata_sha256: `88632df23697500a0c7c41e94fb02d6159ef73b07b033169b66f45a2a56cdd01`
- fixture_sha256: `af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4b8356273a26d14ecc55ebfe7a9a2e541bdc3539a06437a0f30fb3a0dc7cbd4b`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reports_existing_site_integrated` | FAIL | With_skill correctly lists Atlas's Public/Internal build, Docker, Compose, Helm, and auth evidence, but does not report the existing integrated chain as `integrated`; it instead flags CI and deployment gaps. |
| `detects_partial_variant_coverage` | PASS | With_skill identifies Orbit's Public build as publishable while Internal is only an isolated build script, and enumerates missing Internal Docker, Compose, Helm, and CI coverage without claiming completeness. |
| `returns_gap_to_pm_read_only` | FAIL | With_skill states the review was zero-write and excludes Dockerfiles, workflows, Compose, Helm, and deployment execution, but does not ask whether pm-agent should generate a repo-wide deployment handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107; output_sha256=bfa0fcee968246bf742ce85c44167e12f921e3b61c4274d5c3434fb414d5f670; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Performed a detailed read-only configuration review, accurately distinguishing Atlas's two configured variants from Orbit's Public-only publishable coverage, but missed two required user-visible conclusions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107; output_sha256=af43e86260e1f44482bef187077ed1d0733067e59f30563d2ef7b02053f58cd3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also correctly identified Atlas as dual-entry and Orbit as Public-only, with a concise evidence-backed read-only report; used only as comparison context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits the required integrated report for the existing site chain.
- The with_skill output omits the required pm-agent repo-wide deployment handoff question.
- Next: Add an explicit `integrated` conclusion for the existing site chain when supported by evidence.
- Next: Explicitly ask whether pm-agent should generate the repo-wide deployment handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
