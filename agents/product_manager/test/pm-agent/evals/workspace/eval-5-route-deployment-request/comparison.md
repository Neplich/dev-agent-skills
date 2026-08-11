# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-005-route-deployment-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-5-route-deployment-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe`
- Repository HEAD: `b385df5d17058a52081357c8a8480fc146c3d989`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ecf67dca8a2fd53bb0dd6d0a63750ba2716e88dc4af4f77176ea061260d64286`
- Skill overlay SHA-256: `2ed9fef9a54be8009ea156c857682ad7dd82c0e56e3463d3257fe74fe9c977ec`
- Judge schema SHA-256: `42fd42dc7a350eab589db47b48a132e9f478c8e119c1fdbd30b4875075f9f0b5`
- Eval definition SHA-256: `73a2b58c1c65bf56a5f6d6f35f003c86e432caed7b530c34cf851322050e2633`
- Metadata SHA-256: `d17a05b229136107ac1e50142856979a9ae9f563cdb19b940e4810dadda79e1c`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_deployment` | PASS | With-skill output explicitly records `request_type: deployment`. |
| `repo_wide_scope_allowed` | PASS | With-skill output records `feature_path: N/A`, all feature fields as `N/A`, and `feature_path_evidence: []` for repository-wide CI/release-readiness work. |
| `devops_handoff_packet` | NOT_EXERCISED | The handoff is explicitly blocked because environment, release scope, rollback requirements, and related context are missing; DevOps execution cannot yet occur. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=9347c26a162d3bd91691543e990c6f24873987875385a99afdd5e65a55f2ea97; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the request as deployment, applied repository-wide N/A scope, and safely blocked the incomplete DevOps handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=25799a984fa1d3f2d2079c0a8b2019ef4dd6d21e92a45dd37188c5e5365f1f4b; snapshot_sha256=9536b845d706249d67bef15603631d07e84bc8b58bba4debc9bf8c4fb0acb5ee
- Behavior: Implemented generic CI files but did not provide the required deployment classification or structured handoff context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Supply the missing operational goal, environment, release scope, rollback needs, and risks, then complete the DevOps handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
