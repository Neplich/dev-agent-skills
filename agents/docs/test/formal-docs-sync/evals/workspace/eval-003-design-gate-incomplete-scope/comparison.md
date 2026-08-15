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
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `b2bf4f8fb3d18226f8bc19c0ca91afcf8f927301ac6d8c89204f1fa6248c4f6b`
- metadata_sha256: `60fd8d12ce139674523c1a361254f5e8a91b8a162c74d8b2d6b08ca495888809`
- fixture_sha256: `8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4b5a2072f392f239ebcef5483d2cd7f59525e9dddc22047a3017a3927cbc8008`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_incomplete_scope` | PASS | with_skill 输出明确将同步判定为 blocked，并指出 `SCOPE-02` compact rendering 仍为 `TODO`；最终要求 Engineer 完成 compact rendering、对应测试和完成态材料后重新进入门禁。实施计划原始证据将其列为本次 delivery 的 Engineer TODO。 |
| `design_zero_change` | PASS | with_skill 的锁定 git_evidence 显示前后 HEAD、分支、index、worktree 和未跟踪文件均无变化；输出明确报告 design 页与 change-map 均 zero-write。 |
| `no_tentative_design` | PASS | with_skill 的锁定 git_evidence 显示无文件变更，delivery_snapshot 为空；输出保持 blocked 状态，未生成任何 provisional、tentative、planned、future-state 或部分 design 正文。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174; fixture_sha256=8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66; output_sha256=c9181fdad8711fe04cc75880485f1c8847ef5cfc13153f1d7c1383c6e9c2640c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核验未完成范围并阻断同步；保持 design 页和 change-map 零变化。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174; fixture_sha256=8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66; output_sha256=6d73ffaf144bb9fdbb4e576ba6fa6f833f1520cd6ccdd7e23255285ad61ab1d0; snapshot_sha256=4f58bd6db4e44fe0a5abd6cf6dff89e0d914f7141417b5d1d1f75ba978239929
- Behavior: 识别了 SCOPE-02 尚未实现，但仍修改了 design 页和 change-map 并宣称完成同步。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
