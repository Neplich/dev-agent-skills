# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-007-route-manual-gen`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8` from `agents/docs/test/docs-agent/evals/workspace/eval-007-route-manual-gen`.
- Identity schema: `2`
- target_skill_sha256: `af94ca4b38768885230f6271f3d4ae9e1b1be30fcd2f5bdf1098250b4ded0306`
- eval_definition_sha256: `b572bcf4c18451eca03023d64515c12cbfbd9f67b27200f6bcd78820652e00b9`
- metadata_sha256: `31c2720a1114e612336c51527d7aae20dddb1f4e46b566ffffe4788d27952b8e`
- fixture_sha256: `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `dfbcad96e39d7a0ba2503c7d345d86b54a6c9e1188ff1c09f99476b24380e820`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `9fb87f2f78aa3667a6ac45d4638b5d2f77454f04c57c127222d45ced6a6bf97f`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_manual_entry_basis` | PASS | with_skill 明确接受 manual-handoff.md，并识别宿主仓库、手册范围、运行界面证据来源和所需输出。 |
| `routes_manual_gen` | PASS | with_skill 明确选择 manual-gen，未改派其他 specialist。 |
| `preserves_manual_handoff_context` | PASS | with_skill 保留了八项要求的交接上下文，包括 blockers_risks。 |
| `references_manual_gate_only` | PASS | with_skill 将后续工作交给 manual-gen，仅引用其入口门禁，未执行生成、截图采集、站点写入或审计 handoff，也未暴露本地路径。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=3fbe57a0c37d03e5740d4f0f0a1dcc031d85661a6cc78cea2426f586ffbda862; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成入口识别、路由和上下文保留，并保持 router 与 manual-gen 的职责边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=a5757a09d9627a3e4a8887e108fb92534a6bc6d6b8abc51f37e27fa53b04ab8d; snapshot_sha256=0771a9372cd0da07930d160fcdcfec83e010e7dd306af651191fd297f5b4e96a
- Behavior: 直接生成并写入了手册文件，未执行所需的路由职责；仅作对比背景。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
