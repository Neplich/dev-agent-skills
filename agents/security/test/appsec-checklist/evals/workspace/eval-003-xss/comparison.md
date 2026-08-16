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
- Identity schema: `2`
- target_skill_sha256: `412a68c0dfdb2d720e3447fdc4faf74b408d3de29706093a3a69fb0ca69d983c`
- eval_definition_sha256: `6b75287b771a74771292ff6a9a4b1d4288f8c6b58ea121782df92af92abb087a`
- metadata_sha256: `4abdb4afdb25b3301062311f0106269361c2da7348712e8f551f5749c515259e`
- fixture_sha256: `746acb9424bcff0e7d1cdbd84db8418dc8fed63831bb1cdba56197295fa9433e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `dd30fe689fbcc65952d80f9f7fb0f55e7cc2d55b9002a172d25f15b8b97c4288`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `4fbcbae96df725d2ae68317bce92f64188686abcfd62940b28a42e14a09de97f`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `035cdf3596c1888564523ed3d4e73116a3d2b231b30d91c462fb62cf6da52e05`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | The delivered report identifies stored DOM XSS caused by interpolating author/body into innerHTML, with concrete payload examples and affected user roles. |
| `evidence_and_impact` | PASS | The report directly cites src/ui/comment-display.js:2-4, explains the API-to-DOM flow, and describes impact to sessions, page integrity, phishing, and data exposure. |
| `severity_rationale` | PASS | It rates the issue High and justifies that rating using persistent commenter-controlled input, viewer impact, direct HTML parsing, and the product's plain-text requirement. |
| `remediation` | PASS | It provides an actionable textContent/createElement remediation, forbids unsafe HTML rendering, and specifies browser regression checks for author/body payloads, execution, DOM structure, and text preservation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4fbcbae96df725d2ae68317bce92f64188686abcfd62940b28a42e14a09de97f; fixture_sha256=746acb9424bcff0e7d1cdbd84db8418dc8fed63831bb1cdba56197295fa9433e; output_sha256=2a1a2cfb20f1753850dca248e18de83ed4d9abb3c9403a0523990f0d85801a60; snapshot_sha256=33f607709e50d4d86d818d4ca5095757f59247de9b17bd956ac148693eddf930
- Behavior: Produced the required security report artifact and accurately documented the XSS finding, evidence, impact, severity, remediation, and verification boundary without modifying application code.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4fbcbae96df725d2ae68317bce92f64188686abcfd62940b28a42e14a09de97f; fixture_sha256=746acb9424bcff0e7d1cdbd84db8418dc8fed63831bb1cdba56197295fa9433e; output_sha256=08a8fce0d9403a87110ccc931b8fc428d2b8b000eb7618e3eb060d56d848ed97; snapshot_sha256=29f4de22e5c7e14d6c0a9dae1dcb4884b7727748d720292251e8c9f39990dd1e
- Behavior: Also identified the core XSS risk and proposed remediation, but provided less detailed locked report content; comparison only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
