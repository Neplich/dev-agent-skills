# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-002-confirmation-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc` from `agents/docs/test/release-notes-gen/evals/workspace/eval-002-confirmation-gate`.
- Identity schema: `2`
- target_skill_sha256: `3da1a9a1466d6ecd43ed5c082adf803d01b5c2ca25dfee7a882fcc8113f7ce5c`
- eval_definition_sha256: `734d8912f6102b866e236fb845ac847f11fde3651b05c29ee143e730ba9a8ce3`
- metadata_sha256: `244623c4cb29666e66fbef86938647497dad20990909aac70827020a236484a7`
- fixture_sha256: `d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f52a12716f836504537cf75e93c1e10d802a32eb7ad0a9945e2057c1a94c3f7c`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `9d7abf20333b60efc8aeaad2d302ecd422e44bb547e52f5a4d9623347a2b048b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_derived_surfaces_unchanged` | PASS | with_skill 的 git_evidence 显示仅新增候选正文文件，目标派生面无 diff；正文及交接说明明确确认前不修改 metadata、Release Notes index 和导航。 |
| `reports_unconfirmed_not_ready` | PASS | with_skill 输出明确给出 confirmation_status: unconfirmed、handoff_status: blocked，并未将候选页面描述为 ready。 |
| `waits_for_explicit_confirmation` | PASS | with_skill 提供候选正文、evidence/01 至 evidence/06 来源、确认后修改的派生路径，并明确请求确认后再更新和运行检查。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc; output_sha256=31e03589fcc97baec4cb54bf1eea0bebaed1bc07c8a9033d4011a70c14da259d; snapshot_sha256=0e18a065ee94e255a37559b25ccb23e9f485da669eb44514669b75912025e271
- Behavior: 生成完整候选正文，保持派生面未写入，明确未确认且 blocked，并等待确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc; output_sha256=0f17aa2e504b305430b7f73a4d1f08461c12c5bfd5a9a2f0f4f5ce2e9d74ab95; snapshot_sha256=141b24a1cb81971e09a48f85582d3d4a74e5efced5f075396c3ff22a3395d6f9
- Behavior: 生成候选正文并保持派生面未修改，但未报告 confirmation_status/handoff_status，也未明确等待确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
