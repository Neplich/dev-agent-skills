# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6` from `agents/docs/test/docs-agent/evals/workspace/eval-003-route-release-audit`.
- Identity schema: `2`
- target_skill_sha256: `af94ca4b38768885230f6271f3d4ae9e1b1be30fcd2f5bdf1098250b4ded0306`
- eval_definition_sha256: `6d6a401b76741386ad3f6aee549b3bfaa2f477f4ced9973b14647dc8b591096b`
- metadata_sha256: `d582bafa2b7d4e637ef2b4b71f14f435256d70c30e92f7097a43cd40dc9da750`
- fixture_sha256: `aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f4f786bd56d6a5cbcee24193816a462566a8caafb4c223ef38759bdf64ee0486`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `505e784bf52b9cb6d00fcfd914382f9013b636eb784f4767105b0ee1e264c5bf`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_equivalent_chain` | PASS | With-skill output explicitly accepts the equivalent confirmed release-entry chain and identifies the release scope, v0.4.0, source document, evidence context, and audit request. |
| `routes_docs_audit` | PASS | With-skill output selects docs-audit, preserves the v0.4.0 audit scope and referenced changelog/evidence context, and defers execution to that specialist pending missing credentials. |
| `references_audit_gate_only` | PASS | With-skill output states that docs-audit owns the authoritative gate, does not execute the audit, exposes no local SKILL.md path, and does not reproduce the prohibited detailed protocols. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6; output_sha256=cce327eb7f9bc3185c56d14f9b9ecfad7b3a6976e9282ff4fe211f7eb45eca8a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly recognizes the equivalent release chain, routes the request to docs-audit, preserves context, and stops at the specialist gate because required evidence is missing.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6; output_sha256=4f8d835c675137a0ef7f1c2c8959226b39e28640687bf7508639af30fa934df6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Performs an audit-style assessment instead of routing, treating the release-entry claims as insufficient and recommending evidence remediation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
