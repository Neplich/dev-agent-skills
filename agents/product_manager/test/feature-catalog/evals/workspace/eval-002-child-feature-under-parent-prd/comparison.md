# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-002-child-feature-under-parent-prd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-002-child-feature-under-parent-prd`.
- Identity schema: `2`
- target_skill_sha256: `217c9b057b0819a52534f84f10e4d4a1bc905c2af1e21214f5f09bf51cb17566`
- eval_definition_sha256: `381b074083537f3d71cb0a28bd3dbbcbf80ece8371ca5fba3a891d822f995603`
- metadata_sha256: `9511751d671a5ae5883161ea664a79cdce7fc89cb2e17e607a976174a239c8f6`
- fixture_sha256: `e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c03c0410b926db4903e624e0fe3e993a88d8b355caa51278c9f027aa7078ef66`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6cef39f1b1cce23592397054fa6d427258c02b6778c43df49e227da056eafd0d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `parent_prd_context_read` | PASS | 输出引用 docs/pm/order-management/PRD.md，并明确复用 feature_path: order-management；原始工具证据也显示读取了该 PRD。 |
| `child_nested_under_parent` | PASS | 建议路径为 order-management/refunds，仍是 order-management 下的 lower kebab-case 子路径，而非顶层目录。 |
| `feature_level_metadata` | PASS | 输出明确给出 parent_feature: order-management、feature_level: 2，且建议路径包含两段。 |
| `handoff_packet_fields` | NOT_EXERCISED | 候选要求先等待用户确认；确认后的 handoff 尚未发生，因此无法验证完整 handoff packet 及 feature_path_evidence 契约。 |
| `no_bulk_prd` | FAIL | 未生成 PRD/TRD 正文，但将 PRD/DECISIONS 交给 idea-to-spec，而断言要求指向 prd-gen；Engineer 侧虽明确指向 engineer-agent:trd-gen，整体路由要求未满足。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e; fixture_sha256=e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910; output_sha256=306cadd495ffcddc9c3922fa0f3a8784c9b277eae127efd98e23a19dfaf1465d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别并建议退款嵌套在 order-management 下，且给出一致的元数据；但未形成确认后的 handoff packet，并错误指定 PRD 交接方。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e; fixture_sha256=e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910; output_sha256=f6881488e7bb0c6fbf375d5e32d94069469849fcad0ebaa105c20e5d9df46836; snapshot_sha256=4668468aedb4a0941a841f5bda2861ed8b260bd25be12d9004bb04c95c0f6017
- Behavior: 基线直接更新了功能目录和退款画像，路径与元数据完整，但未提供要求的 handoff packet 契约字段。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 将 PRD/DECISIONS 后续交给 idea-to-spec，而非要求的 prd-gen。
- Next: 确认后补齐包含 feature_path、feature、parent_feature、feature_level 和 feature_path_evidence 的 handoff packet，并将 PRD/DECISIONS 创建或更新明确交给 prd-gen。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
