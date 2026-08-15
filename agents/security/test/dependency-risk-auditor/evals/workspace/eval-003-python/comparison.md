# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-003-python`.
- Identity schema: `2`
- target_skill_sha256: `4936716a99cef8bc1e927ef64eaa0d20fa85f573a00b76c6ef0e6212ccbb3af0`
- eval_definition_sha256: `b851960b1dd4c6ab11f9c42f685034d6bd0e27ae3c26e4256af19942329ed614`
- metadata_sha256: `ae72aa507a46a167a61a13af949f88d9dacf41d33161383d4a9754e7de06b4d8`
- fixture_sha256: `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `07345508cc5d326f024163cc8715111c4efeeb1bd80f16886d65b16eb2ef9292`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41b45499ae9ca5616b92679964200469b31cddbc1797bbf9c8e3a1dc71be48a5`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | With-skill report inventories the Python ecosystem and identifies requests, urllib3, and Jinja2 with exact pinned versions and relevant HTTP, TLS, and template risk surfaces. |
| `risk_classification` | PASS | With-skill report distinguishes public vulnerabilities, outdated versions, conditional exploitability, severity levels, and correctly notes that the projects remain maintained despite historical pinned versions. |
| `evidence` | PASS | The locked delivery snapshot directly cites requirements.txt, exact versions, CVE/GHSA advisories, affected conditions, and remediation versions. |
| `upgrade_plan` | PASS | The report provides coordinated upgrade targets, compatibility/testing order, temporary mitigations, release blocking criteria, and ownership/escalation guidance without modifying requirements.txt. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=c060b66ca6a3a8345bf126fdc4d81020f43d395428db80f61d19b66960bdeb24; snapshot_sha256=1bdf3c1c5d246ca2e26571ac0b35863bc151e73b0f9f1daef29d0d3fe12e3d73
- Behavior: Delivered a detailed, evidence-backed Python dependency security audit covering inventory, risk classification, exact-version evidence, upgrade targets, mitigations, and release disposition.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=0c40d629e3d2e953e43fa6a693a6e2fb1a0b7ce04d750a24b29c4abe88b2cdff; snapshot_sha256=70960d51ae21afaa324866a28d3e9eb98ba32c769909692174954467447688f3
- Behavior: Provided a shorter audit with useful findings and recommendations, but less complete coverage and less detailed evidence than the with_skill lane.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
