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
- target_skill_sha256: `cd54295a0cbcb90462d5e5533bde1937cc7e871f8f4c9c53d7773ed40ace553e`
- eval_definition_sha256: `88dd9b929d53963534f872d5c6b43117be6b35cb41fa6b99bd7d05175018ade8`
- metadata_sha256: `5e0c35c826a7733ee387d4f323da117f6699f11274aa5fd48097e667d23e3045`
- fixture_sha256: `4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `07345508cc5d326f024163cc8715111c4efeeb1bd80f16886d65b16eb2ef9292`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `dede36cbf22736a6194a488a09a7dab4d5a1092bacb831a4913854fdff85a07a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | The with_skill delivery snapshot identifies the Node.js ecosystem and both direct production dependencies: request@2.88.2 and node-uuid@1.4.8, including their external-request and UUID risk surfaces. |
| `risk_classification` | PASS | It distinguishes deprecated/unmaintained status from unasserted CVEs, explains missing security maintenance and transitive-dependency exposure, and assigns high/P0 priorities. |
| `evidence` | PASS | It cites package names and pinned versions, package metadata, Node.js documentation, PM_HANDOFF.md, and the PRD; the locked file content directly contains the evidence. |
| `upgrade_plan` | PASS | It recommends fetch or undici for request, crypto.randomUUID or uuid for node-uuid, plus compatibility checks, lockfile generation, npm audit, migration tests, and release gates. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137; fixture_sha256=4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f; output_sha256=bf0273d801c90d91f487f30a9abeb319fdecc91d494d5b48dac3c60307c16efd; snapshot_sha256=4492ef122b8428a86ad09f80a6092d2b365322b9bb5e9d31816dc175b7d335e5
- Behavior: Delivered a structured dependency risk audit with evidence-based classifications and an actionable replacement plan.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137; fixture_sha256=4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f; output_sha256=db95711b442c7db7ec31e4d895ba48a25d7c429e413b5e24eb5617f6258dfe80; snapshot_sha256=16327196545aef402bb46bc436164ac41d1ae795fc7034d4ece91896f1b8d667
- Behavior: Delivered a correct but less detailed dependency audit and replacement summary.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
