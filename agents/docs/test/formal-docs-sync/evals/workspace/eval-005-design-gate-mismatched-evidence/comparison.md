# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-005-design-gate-mismatched-evidence`.
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `9b46c27014c750c2c7c902ee9b735c340d6216e70bd1db10e9ac7cfe4ffa72b8`
- metadata_sha256: `8201495b57b213f9db3f5219d86222ff877b211b7bfe7d5c149fe15482812507`
- fixture_sha256: `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c9b93b28ac72af6810f4752921bb72d418af8d9162ae5d66c15fe90f929562c8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | with_skill 明确指出请求/计划的 `preferences-summary` 与 PRD/TRD 的 `account-preferences` 冲突，并在 scope confirmation/write phase 前阻断。 |
| `design_zero_change` | PASS | with_skill 报告 `zero-write`、`none changed`、`change_map_delta: none applied`；锁定 git evidence 显示 HEAD、分支及工作树均未变化。 |
| `routes_to_owner` | PASS | with_skill 将产品/元数据冲突路由至 `pm-agent`，将 TRD 路径/影响范围冲突路由至 `engineer-agent:trd-gen`，并要求修正后重试。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=64d8cd62a9f29de377c47066403cd1dc121fb5dbee1ca12548592b99cf89c770; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别 feature_path 证据冲突，阻断确认与写入，保持 design 原子范围零变化并路由给对应 owner。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=d77f1edb05cb1a7e04bb11da8862d66a0ae9b0a1e90479c7afbf0025aafe0db6; snapshot_sha256=d39206766755fc9020924f912ead52c9bd2992f2037dd5c06db65cc7d071f299
- Behavior: 误将交付视为可执行并修改 design 页面及 change-map，未因 feature_path 冲突阻断。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
