# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-001-npm-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-001-npm-audit`.
- Identity schema: `2`
- target_skill_sha256: `cd54295a0cbcb90462d5e5533bde1937cc7e871f8f4c9c53d7773ed40ace553e`
- eval_definition_sha256: `971feaa0f85d14f75fe45df2640551915965f181de289e0a977efb57d2391e3e`
- metadata_sha256: `b384f8f560614179a0a93d18259ac2f4d1d78a8283a28bd2f5b6097f32a74e67`
- fixture_sha256: `5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `07345508cc5d326f024163cc8715111c4efeeb1bd80f16886d65b16eb2ef9292`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `dede36cbf22736a6194a488a09a7dab4d5a1092bacb831a4913854fdff85a07a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | The locked with_skill report identifies the Node.js ecosystem, both production packages (`minimist` and `lodash`), missing lockfiles, and relevant vulnerability/supply-chain risk sources. |
| `risk_classification` | PASS | The report distinguishes Critical/High/Moderate vulnerabilities, discusses abandonment and provenance signals, and assigns P0/P1 priorities with impact and exploitability context. |
| `evidence` | PASS | The locked report cites `package.json`, exact versions, CVE/GHSA identifiers, severity scores, affected ranges, fix versions, and advisory links. |
| `upgrade_plan` | PASS | The report provides prioritized upgrades, lockfile/npm ci steps, regression checks, short-term input restrictions, and release-blocker guidance. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=e43366f10812d6448ebf24aac87af8739d8871fc64882f0de5e5e17bccff9bb6; snapshot_sha256=b1913cc5e73d5472a5ce18fd3212e175179dc6d7e153b0811efb2632b0a76a9d
- Behavior: Delivered a complete structured dependency-risk audit covering inventory, classification, evidence, mitigations, upgrade sequencing, verification, and release readiness.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=8a192e73a47e667892d9f77f06ebb8b4eb66c8ccbdc0cfcfdebe71f7f80d4dbe; snapshot_sha256=6c0fca61d993caf8176594464edb443757caf2531eb102a81b3df77cd32a58e6
- Behavior: Fresh baseline also delivered a substantively complete audit, but with less detailed provenance and classification coverage.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
