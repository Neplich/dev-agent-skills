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
- Repository HEAD: `8813f864e743f7c83dc2e51e0b5add79f312e870`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0616a11ea39f978cac34906ca01c79a336316825183bb1897d900f056d8544f7`
- Skill overlay SHA-256: `4d4a580c5e7c36b9199abb80221829f90c900c96463581d7f87c6d7ccc538bd7`
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
| `request_type_deployment` | PASS | With_skill explicitly states `request_type: deployment` in its Routing decision. |
| `repo_wide_scope_allowed` | PASS | With_skill uses `feature_path: N/A`, `feature: N/A`, `parent_feature: N/A`, and `feature_path_evidence: []` for repository-wide work. |
| `devops_handoff_packet` | NOT_EXERCISED | The DevOps handoff is explicitly blocked because the target agent and required release context are unavailable; the actual handoff cannot yet occur. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=259042ca0672c7b0cc9ca01dcd11fa18d6918cce2344e47e60d0cdb8db780016; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies the request as deployment, permits repository-wide N/A scope, and stops before an unsupported DevOps handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3ea9ec3f666f17ed064514f2fafa4c925fc8f737b7904e6aa6d9c97d2b17679d; snapshot_sha256=df9e7182eb760cabfbd10b7e99ad05abcb8ad7436780a669611ff080265c733b
- Behavior: Implemented repository-level CI artifacts but did not provide the required deployment classification or structured handoff context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Confirm environment, release scope, rollback needs, and risks, then hand off to DevOps when the target is available.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
