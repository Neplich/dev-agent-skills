# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-003-xss`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `746acb9424bcff0e7d1cdbd84db8418dc8fed63831bb1cdba56197295fa9433e` from `agents/security/test/appsec-checklist/evals/workspace/eval-003-xss`.
- Fixture SHA-256: `746acb9424bcff0e7d1cdbd84db8418dc8fed63831bb1cdba56197295fa9433e`
- Prompt SHA-256: `4fbcbae96df725d2ae68317bce92f64188686abcfd62940b28a42e14a09de97f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `33e7e73c99fb4e7a6f2d6ab5104b8298fc067235a29614a6e32ee61035051666`
- Judge schema SHA-256: `dd30fe689fbcc65952d80f9f7fb0f55e7cc2d55b9002a172d25f15b8b97c4288`
- Eval definition SHA-256: `6b75287b771a74771292ff6a9a4b1d4288f8c6b58ea121782df92af92abb087a`
- Metadata SHA-256: `8b9d5478f14d810cc31c023b6e6a4956d8afc5605aa60470f7733640de6334fb`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | With-skill report identifies HTML injection/XSS through unencoded author/body values inserted into innerHTML, with relevant payload examples. |
| `evidence_and_impact` | PASS | Locked delivery snapshot provides code locations, API-to-DOM data flow, affected commenter/viewer roles, assets, and cross-user impact. |
| `severity_rationale` | PASS | Report rates the issue High and explains attacker control, innerHTML sink, viewer-triggered execution, cross-user exposure, and pure-text contract violation. |
| `remediation` | PASS | Report gives actionable textContent/DOM API remediation and browser/automated regression steps covering author/body payloads, DOM structure, execution, and edge cases. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4fbcbae96df725d2ae68317bce92f64188686abcfd62940b28a42e14a09de97f; fixture_sha256=746acb9424bcff0e7d1cdbd84db8418dc8fed63831bb1cdba56197295fa9433e; output_sha256=56b13a5830b1fbab729b0c4b61438857dcb364b6756b22a42ec421613aa80b4b; snapshot_sha256=08a29af110cc95398b544013af3c857788e675c55e0448fc46de65728e0b7ebc
- Behavior: Produced the required security checklist with accurate findings, evidence, impact, severity rationale, remediation, and verification; did not modify application code.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4fbcbae96df725d2ae68317bce92f64188686abcfd62940b28a42e14a09de97f; fixture_sha256=746acb9424bcff0e7d1cdbd84db8418dc8fed63831bb1cdba56197295fa9433e; output_sha256=80095c07f4d81563f95739d8dca4d6a57d33cbf2ae3029bddc9e468bfd5acd3f; snapshot_sha256=0f3a1e2dcd51cfbb244e92d9936b7b7c6619b3596733507d3e622db8a9b330ac
- Behavior: Also identified the core XSS issue and remediation, but provided a less structured and less complete report for comparison.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
