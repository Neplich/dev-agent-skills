# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-003-block-bootstrap-conflict`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-003-block-bootstrap-conflict`.
- Identity schema: `2`
- target_skill_sha256: `f325a3bc283b067240ee3d50726f680693f5cd996590e717b72af686853dbf3e`
- eval_definition_sha256: `ef71b65d8d90e0a7a85b11140f77333b6bccfac4b39b25f67875d33153f0ebea`
- metadata_sha256: `dd91ae0a6e0ac8c19ffeb9b16bf575dc1d6e559c0626e7027f9e04c671f270d0`
- fixture_sha256: `67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `8fb0a4310aa73072ce3915bd9569df86e49409cfb5df2e41bfa626f79fa1e1ef`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `7e27a0b4acbeb0bbab6d1ce4f4eaef1707f80d3f366d62ddd92d0e2d6f621f17`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8a54b9d8ab53e6a7ef3187af8e3063aff036e0d1740a4b832c4d3a33058de445`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_complete_conflict_list` | NOT_EXERCISED | 候选明确要求用户确认完整 scaffold 与 manifest，当前未进入冲突扫描阶段，因此尚未形成冲突清单或 blocked 状态。 |
| `does_not_overwrite_conflict` | PASS | with_skill 的 git_status 和 git_diff 均为空，fixture 中的 standards/index.md 哈希保持不变，delivery_snapshot 为空。 |
| `offers_explicit_resolution_choices` | PASS | 候选明确提供 overwrite、explicit merge、keep-existing 三种选择，并未在用户选择前记录 kept-as-is。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7e27a0b4acbeb0bbab6d1ce4f4eaef1707f80d3f366d62ddd92d0e2d6f621f17; fixture_sha256=67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a; output_sha256=eaaea23bce357113a66cbe108f166e5ee4e3792edc6aedc9e9d2f8a4adcbd931; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确停在授权确认门槛，未修改工作区，并预先说明三种冲突解决选项。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7e27a0b4acbeb0bbab6d1ce4f4eaef1707f80d3f366d62ddd92d0e2d6f621f17; fixture_sha256=67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a; output_sha256=dde45ac4d3d789b1b2a188959983a9faca3c8e243cb2264e5c628b35faec9693; snapshot_sha256=435c96ee9220aca5a3a4ad4ca0ee7d6fcbcc3c48f0bf52dcbf7079255a0452ce
- Behavior: 直接补齐 scaffold 并修改 manifest，保留文件但未展示完整冲突清单或明确阻塞流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 用户确认后扫描并列出完整冲突清单，明确将未解决覆盖阶段标记为 blocked。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
