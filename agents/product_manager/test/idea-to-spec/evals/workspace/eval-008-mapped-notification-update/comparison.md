# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-008-mapped-notification-update`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960` from `agents/product_manager/test/idea-to-spec/evals/workspace/eval-008-mapped-notification-update`.
- Fixture SHA-256: `177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960`
- Prompt SHA-256: `8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c0da2e0366232678672d0c64ce9fa764d3b78f3caaaa8493348af1a7e1cd00fe`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `130498c1a4cc1643bdf013127365b28e5fdc8391203daf304f2cdc0ef5bc97d2`
- Metadata SHA-256: `071b1907c18a80afba8338dbc482c47ee9a6fa479b963c4fb7d1e4c62363e556`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 锁定输出说明 change-map 指向目标 API 文档并称已读取，但原始证据无法证明实际读取顺序或是否遍历了无关页面。 |
| `verifies_against_code` | PASS | 锁定输出明确指出 channels.txt 仅启用 email，并识别 API 文档声称支持 webhook、但代码未验证该能力，按代码事实判断不一致。 |
| `treats_unverified_as_low_trust` | PASS | 锁定输出明确将 last_verified_version: unverified 标为低信任，并以 channels.txt 等代码/仓库事实复核现状与影响范围。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274; fixture_sha256=177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960; output_sha256=2833ab216bcd8c43a43c2c2ab55b20dac291470a30a4c51de8ce57f607fc6bc9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确梳理了当前 email 配置、文档与代码的不一致，并将未验证文档降为低信任；未修改文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274; fixture_sha256=177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960; output_sha256=a566a7bba61ccdd01b530dd52f882849fdd19cebb18135979319031359057d94; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 也识别了 email-only 配置及 webhook 文档不一致，但未明确降低未验证文档的信任。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
