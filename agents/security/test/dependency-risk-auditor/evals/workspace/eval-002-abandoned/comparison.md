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
- target_skill_sha256: `4936716a99cef8bc1e927ef64eaa0d20fa85f573a00b76c6ef0e6212ccbb3af0`
- eval_definition_sha256: `88dd9b929d53963534f872d5c6b43117be6b35cb41fa6b99bd7d05175018ade8`
- metadata_sha256: `5e0c35c826a7733ee387d4f323da117f6699f11274aa5fd48097e667d23e3045`
- fixture_sha256: `4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `07345508cc5d326f024163cc8715111c4efeeb1bd80f16886d65b16eb2ef9292`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41b45499ae9ca5616b92679964200469b31cddbc1797bbf9c8e3a1dc71be48a5`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | The locked audit identifies the Node.js ecosystem and both direct production dependencies, `request@2.88.2` and `node-uuid@1.4.8`, with their relevant network-request and UUID risk sources. |
| `risk_classification` | PASS | The audit distinguishes deprecation/unmaintained status from unassessed CVE/transitive risk, assigns High maintenance risk, and gives P0/P1 priorities with conditional escalation criteria. |
| `evidence` | PASS | The delivered file cites `package.json`, PM handoff and PRD scope, exact package versions, npm deprecation evidence, Node.js documentation, the missing-lockfile `ENOLOCK` limitation, and relevant repository findings. |
| `upgrade_plan` | PASS | The audit recommends replacing `request` with built-in `fetch` or a maintained client, replacing `node-uuid` with `crypto.randomUUID()` or `uuid` as appropriate, plus migration tests, isolation, outbound restrictions, lockfile creation, and follow-up ownership. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137; fixture_sha256=4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f; output_sha256=2606ce730a43993086bbed000310bba9b01d8685e14930a997273031f6450c96; snapshot_sha256=3a54d54d56d9eb66a972be56b4124160ff85f4e6a0d6f9ea903bcba57ddb38e9
- Behavior: Produced the required feature-scoped dependency audit in the PM-designated directory without modifying dependencies, covering both packages, evidence, risk classification, and a concrete replacement/mitigation plan.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137; fixture_sha256=4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f; output_sha256=0baebc92daca4e221c5335e70e228ed5a4d0cb28712bd491b7c9f5345640ef44; snapshot_sha256=71c412d5a83e795caad45aff6d13c16c7506450a5fa1fa6268313c9f36376180
- Behavior: Produced a semantically complete audit with similar dependency findings, evidence, risk priorities, and migration guidance; used only as comparison context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
