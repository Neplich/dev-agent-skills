# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-018-scope-guard-explicit-invocation`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-18-scope-guard-explicit-invocation`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `ead0a8a200281bbfa0afaf7a39e0f1af2941a392e02ec1305327c3034a58f2be`
- Repository HEAD: `e2d0e3e00078c297194828182b4d6445ecbb492d`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c658e8351498435bd5246b692fbf8a3a6d40caa45d6998b37785e6522243068b`
- Skill overlay SHA-256: `2a468ab17f03f6a66d3f4083da133fc1c0904ede59404e5cd9fe19f49032d89d`
- Judge schema SHA-256: `fa178b3d583b780cd4e045f7de5ab1850835a5c0245473688f5c3beae5d52f79`
- Eval definition SHA-256: `ace076e0dee3d458a090ce0c8c5d192739433f53b806c4c331f56cbac3d014b6`
- Metadata SHA-256: `2b6018f581af1ec4cac560c19b2a62982e54f3798f08f9183632d72326c13a3d`
- Executor SHA-256: `a4bdc62ab64b81e98e050718e983a49fe8219a833420e63178b355862f4129df`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `explicit_invocation_proceeds` | PASS | With-skill output explicitly provides a Routing decision containing request_type, change_tier, and selected_owner fields, and identifies pm-agent:idea-to-spec. |
| `routes_to_product_discovery` | PASS | With-skill output routes to pm-agent:idea-to-spec, keeps the execution boundary at PM discovery, and explicitly states that no requirements implementation, design, or code will be performed. The downstream discovery could not continue because the target skill was unavailable. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ead0a8a200281bbfa0afaf7a39e0f1af2941a392e02ec1305327c3034a58f2be; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=77d37cbaa05431d25a65f336562b6e23a737268349a84103cd1b7e920afdb84e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performs explicit PM routing and preserves the request on the product-discovery path without code execution, but stops at the routing boundary because the downstream skill is unavailable.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ead0a8a200281bbfa0afaf7a39e0f1af2941a392e02ec1305327c3034a58f2be; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=d0b6a14676fe004a43a6455e439000cf09eaa4425bec11ac9d9679574eef0bde; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a substantive product-scope proposal and confirmation questions without an explicit routing decision; useful as fresh baseline comparison only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Install or enable pm-agent:idea-to-spec to continue the product-discovery workflow.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
