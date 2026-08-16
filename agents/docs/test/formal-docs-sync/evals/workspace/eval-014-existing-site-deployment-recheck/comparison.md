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
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `db9d705a02de2df76d9e1b62334995eac21d110dc172ed350d92306793043708`
- metadata_sha256: `88632df23697500a0c7c41e94fb02d6159ef73b07b033169b66f45a2a56cdd01`
- fixture_sha256: `af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4b8356273a26d14ecc55ebfe7a9a2e541bdc3539a06437a0f30fb3a0dc7cbd4b`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reports_existing_site_integrated` | PASS | The with_skill output reports Atlas public/internal coverage, cites package.json, Dockerfile, Compose, Helm, and auth evidence, and states that no build/deploy work was repeated. |
| `detects_partial_variant_coverage` | PASS | The with_skill output explicitly distinguishes Orbit public as complete and internal as only a build script, listing missing internal Docker, Compose, auth, Helm, and CI paths. |
| `returns_gap_to_pm_read_only` | FAIL | The with_skill output identifies pm-agent as the next owner for a repo-wide deployment handoff and confirms read-only behavior, but it does not explicitly ask the user whether pm-agent should generate it. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107; output_sha256=8660c07e9b061c20f1eb56238f64ada3c8c1870babb582f67260beb0daca5005; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Accurately reports Atlas coverage, detects Orbit's partial internal coverage, and preserves read-only boundaries, but gives a next-owner recommendation instead of explicitly asking for pm-agent confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107; output_sha256=604b097078ac225da405b3e149227b0a036c698fbfe0fdebb37f7917b3207904; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also identifies the public/internal configuration differences and read-only state, but does not provide the required pm-agent handoff question.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The required user-facing question about whether pm-agent should generate the repo-wide deployment handoff is omitted.
- Next: Explicitly ask whether pm-agent should generate or confirm the repo-wide deployment handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
