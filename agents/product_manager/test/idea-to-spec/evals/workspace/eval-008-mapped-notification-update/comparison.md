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
- Identity schema: `2`
- target_skill_sha256: `34042e851466ff927567e09fc5777d952f1546cabc96fbe4de98617d27f5b1fb`
- eval_definition_sha256: `130498c1a4cc1643bdf013127365b28e5fdc8391203daf304f2cdc0ef5bc97d2`
- metadata_sha256: `071b1907c18a80afba8338dbc482c47ee9a6fa479b963c4fb7d1e4c62363e556`
- fixture_sha256: `177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274`
- Repository HEAD: `c13c53a9b6e4cf18215450050bc9e7d0a810b73c`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `55d032569bbd4014a60103aafb1c0773a93ff9dbe0ea681c46297ebeef4a35b3`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | with_skill 的锁定 trace 显示先读取 skill 与 change-map，随后在同一命令中读取 channels.txt，最后才读取 notifications.md；未满足先读取 required_docs 的顺序。 |
| `verifies_against_code` | PASS | 输出明确以 src/notifications/channels.txt 认定仅启用 email，并指出 notifications.md 声称支持 webhook 的不一致，未以文档覆盖代码事实。 |
| `treats_unverified_as_low_trust` | PASS | 输出明确指出 last_verified_version: unverified，仅作导航，并以 channels.txt 作为代码事实复核现状与影响范围。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274; fixture_sha256=177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960; output_sha256=17d55e9fa92e794ef1ee865d5a978707478e5d2f7475bdca050fe73ece910d0a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成代码核证和低信任处理，但未满足映射文档优先读取顺序。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d974654e1fcdbd5fc645c2a9f10feef6661d70a858e4722087a732bb9d82274; fixture_sha256=177b1f9c445f127660775572bba7b23413067a88e77389cbdec983886f090960; output_sha256=23065c071a3f27aed4055255ab04ae560010078411a106da1c542b7fb7bd1ba0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 基线输出正确识别 email/webhook 差异，但未提供可证明的映射文档优先读取流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未按要求先读取 docs/site/api/notifications.md；锁定 trace 显示读取顺序包含 channels.txt 在前。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
