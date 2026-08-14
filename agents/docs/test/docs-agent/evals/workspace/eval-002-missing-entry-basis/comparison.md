# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-agent/evals/workspace/eval-002-missing-entry-basis`.
- Identity schema: `2`
- target_skill_sha256: `af94ca4b38768885230f6271f3d4ae9e1b1be30fcd2f5bdf1098250b4ded0306`
- eval_definition_sha256: `46e0e02295d606a359a2403ac234af592712f357041b544bb13a82efa1816296`
- metadata_sha256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `da898e3ecfd0169570b22be7c73cd730ef2fd22e3bf1c5b559383dc76454ff0d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c8a665c7632c31fce83103a67e411115fa7f6c456ea2edd0094ff12d3cf4e103`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7fb7d802028a8a942f6b1255f456e633ed5d87cdb3abb170effa7be87cac74e5`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | PASS | with_skill 明确指出没有 PM handoff 或等价证据链、入口尚未完整，并将 return_owner 指向 pm-agent。 |
| `does_not_execute_bootstrap` | PASS | with_skill 的 delivery_snapshot 为空，git evidence 显示无变更；输出声明当前仅分类与检查、不执行建站写入，且未加载或复述 bootstrap 模板。 |
| `names_missing_credentials` | PASS | with_skill 明确列出缺少已确认宿主代码仓库路径或身份，并说明“明确的文档站初始化请求 + 已确认宿主仓库路径”足以完成 docs-site-bootstrap 入口。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8a665c7632c31fce83103a67e411115fa7f6c456ea2edd0094ff12d3cf4e103; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=94d3ed247d1ec4276b91ec9944321d8df4a0cfbf92f0d0d803fee82c8d697ca5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确分类并停在建站专项入口门槛，指出缺少宿主仓库、引导回 pm-agent，且未产生写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8a665c7632c31fce83103a67e411115fa7f6c456ea2edd0094ff12d3cf4e103; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=91f3b9f77ecefb7f32d73c1e30dd7c1ba75c52f32161a8994598c8761f0cb8b2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了通用的文档站规划与前置条件说明，但未执行 PM 路由或明确 specialist entry basis；仅作基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
