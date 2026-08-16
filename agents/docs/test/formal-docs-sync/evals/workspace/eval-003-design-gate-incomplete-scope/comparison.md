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
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `b2bf4f8fb3d18226f8bc19c0ca91afcf8f927301ac6d8c89204f1fa6248c4f6b`
- metadata_sha256: `60fd8d12ce139674523c1a361254f5e8a91b8a162c74d8b2d6b08ca495888809`
- fixture_sha256: `8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4b5a2072f392f239ebcef5483d2cd7f59525e9dddc22047a3017a3927cbc8008`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_incomplete_scope` | PASS | with_skill 明确记录 `SCOPE-02` 为 TODO、属于当前交付范围、owner 为 Engineer，并要求完成代码与全部验证后重新进入 closeout gate。 |
| `design_zero_change` | PASS | with_skill 的锁定 git evidence 显示 head、branch、worktree、index、refs 均无变化；输出明确说明未修改两个 design 范围文件且 change-map 未应用。 |
| `no_tentative_design` | PASS | with_skill 在 blocked 状态下未生成或交付任何 design 文件（delivery_snapshot 为空、git diff 为空），仅报告阻断原因和后续完成条件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174; fixture_sha256=8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66; output_sha256=cbc63f8fcb0c60eb68218c930aae5454604134c4e3cdf349bf15302a4a8c050c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别未完成的 SCOPE-02，阻断同步并保持 design 范围零写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174; fixture_sha256=8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66; output_sha256=55ef361a0b3e62765a472e20e91400d1b53afebd7d928634d5fc357076a03b54; snapshot_sha256=771d019cb1e9482087e3c46053f8dbf29ae10be9079cc5bcb94385a7abcf9020
- Behavior: 在 SCOPE-02 仍为 TODO 时仍修改了 design 页面和 change-map，形成 fresh baseline 对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
