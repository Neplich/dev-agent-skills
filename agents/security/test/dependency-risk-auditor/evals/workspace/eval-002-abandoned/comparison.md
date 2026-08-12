# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-002-abandoned`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-002-abandoned`.
- Identity schema: `2`
- target_skill_sha256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- eval_definition_sha256: `88dd9b929d53963534f872d5c6b43117be6b35cb41fa6b99bd7d05175018ade8`
- metadata_sha256: `6e01d4daa6b468e7c7a0ddfd1d17ad1116a727bf8d6709ea8ad0e5baec7fce48`
- fixture_sha256: `4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `07345508cc5d326f024163cc8715111c4efeeb1bd80f16886d65b16eb2ef9292`
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
| `dependency_inventory` | PASS | With_skill audit identifies the Node.js/npm ecosystem, both direct production packages (`request@2.88.2` and `node-uuid@1.4.8`), and their external-request/application-identifier risk surfaces. |
| `risk_classification` | PASS | The delivered audit distinguishes deprecated/unmaintained maintenance and supply-chain risk from unconfirmed CVEs, assigns HIGH/P0/P1 severity, and explains impact and exposure. |
| `evidence` | PASS | The audit directly cites `package.json`, exact versions, npm/upstream deprecation evidence, Node.js documentation, and the `ENOLOCK` limitation. |
| `upgrade_plan` | PASS | The audit provides prioritized replacement and mitigation steps: built-in `fetch`/`undici`, `crypto.randomUUID()`/`uuid`, compatibility testing, lockfile and audit follow-up, and temporary egress isolation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137; fixture_sha256=4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f; output_sha256=4191a3f0a4a8cfc465a877819fca88f313d58ef29269b499246fb9f4301fdb38; snapshot_sha256=014cecb12231bbdf244ec19c02db72c625e6ee46108e0187ce6bc6bff3a7e7db
- Behavior: Delivered the required structured dependency-risk audit artifact without modifying dependencies; it provides evidence-backed classifications and a remediation plan.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137; fixture_sha256=4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f; output_sha256=4c26a27acd4cd5ddf9ec6f37046a9b241aa506906e73e28f3603de0b256f7a69; snapshot_sha256=c08eac23b86f97150e95511ef36e07493e5e78a4ca583fc6bd0166151b35bf45
- Behavior: Fresh baseline also produced a substantially complete dependency audit, with less detailed risk and verification treatment than the with_skill artifact.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
