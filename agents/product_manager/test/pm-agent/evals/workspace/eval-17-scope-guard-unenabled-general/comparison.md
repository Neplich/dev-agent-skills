# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-017-scope-guard-unenabled-general`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-17-scope-guard-unenabled-general`.
- Identity schema: `2`
- target_skill_sha256: `6f8f132bc1f6eba3f9eb10727126ee30960b503351486b4fb6204e20571ffb35`
- eval_definition_sha256: `2b26ec5b13cba548fe19b4f508977afc54ba26189b14fbc48be376e4d57b8178`
- metadata_sha256: `05ea9f60607f11132b0f5ec8ca00cda463398f718c44648a9e2be81e39b17991`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c5629d3608d1f142562d32ed4b435e3d2c557d9aa8b1c8b5f72fce35ca63e9a2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `0d80b9dec86a17116de51354d4b9cf60c96709a915b3655bf693ad2757979eb9`
- Repository HEAD: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `637830d1287a617a207310e2740f1a3d3e1e42266df7b99ca4de0e57c2a0c6d6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scope_guard_stops_general_request` | PASS | with_skill 输出明确说明“当前目录未启用”并停止；锁定 trace 显示其检查了当前目录及父级的 dev-agent-skills 标记，且未输出 request_type、change_tier、selected_owner 或下游文档/handoff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0d80b9dec86a17116de51354d4b9cf60c96709a915b3655bf693ad2757979eb9; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6d50e13d8821bc4fc003b4f0506e1421f60c8653847cef87c025aadb5cc64e49; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 检查目录启用状态，判定未启用后以一句简短说明停止。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0d80b9dec86a17116de51354d4b9cf60c96709a915b3655bf693ad2757979eb9; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a435c8569a3cb0612f9f6281fa6220f33bfcb5c7ccf9b31ff815e3bba9677fca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 尝试访问 ~/Downloads，因路径/权限问题未执行整理；未体现目录启用状态检查。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
