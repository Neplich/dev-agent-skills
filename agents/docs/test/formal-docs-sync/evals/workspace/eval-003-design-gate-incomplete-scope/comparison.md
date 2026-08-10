# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-003-design-gate-incomplete-scope`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-003-design-gate-incomplete-scope`.
- Fixture SHA-256: `8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66`
- Prompt SHA-256: `56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `4b5a2072f392f239ebcef5483d2cd7f59525e9dddc22047a3017a3927cbc8008`
- Eval definition SHA-256: `b2bf4f8fb3d18226f8bc19c0ca91afcf8f927301ac6d8c89204f1fa6248c4f6b`
- Metadata SHA-256: `60fd8d12ce139674523c1a361254f5e8a91b8a162c74d8b2d6b08ca495888809`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_incomplete_scope` | PASS | with_skill 明确指出 `SCOPE-02` 仍为 TODO，且下一步由 Engineer 完成代码、测试和完成态证据后重新提交；这与原始实施计划中的范围、owner 和状态一致。 |
| `design_zero_change` | FAIL | with_skill 的锁定 `git_evidence` 显示两个目标文件均有工作区修改，且 `delivery_snapshot` 直接包含修改后的文件内容；其“零变化”声明与原始证据矛盾。 |
| `no_tentative_design` | FAIL | 在 blocked 状态下，with_skill 的锁定 `delivery_snapshot` 包含大段新增 design 正文，并将实现行为写入设计页；这违反了 blocked 时不生成部分 design 正文的要求。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174; fixture_sha256=8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66; output_sha256=a70d972c966d4e8e94ec4250a86f54f6e507988f0d46eba1147dc2326e8c7695; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别未完成的 SCOPE-02 并阻断同步，但仍修改了两个受保护文件并生成 design 正文。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174; fixture_sha256=8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66; output_sha256=1d1d3664004f33c204533564646584e641745228c03e67a417407a92dac23999; snapshot_sha256=87dd907750e14f226ba00387a785148dcc1b95aeb79d567d0b9f8602f4dd6519
- Behavior: 更新了 design 页面和 change-map，虽提及 SCOPE-02 TODO，但未阻断同步。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 修改了 design 页面和 change-map，违反零变化门禁。
- with_skill 在门禁失败后仍生成了 design 正文。
- Next: 完成 SCOPE-02 及对应验证后，再重新提交同步请求。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
