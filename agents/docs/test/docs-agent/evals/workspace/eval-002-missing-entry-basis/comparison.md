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
- target_skill_sha256: `cf826e2e86ef193d8a7294a87c743dead6af892aefcc220dd56ae949fa5c3b40`
- eval_definition_sha256: `46e0e02295d606a359a2403ac234af592712f357041b544bb13a82efa1816296`
- metadata_sha256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `da898e3ecfd0169570b22be7c73cd730ef2fd22e3bf1c5b559383dc76454ff0d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c8a665c7632c31fce83103a67e411115fa7f6c456ea2edd0094ff12d3cf4e103`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `3605efbf3a3778b67aaca5565fc5172f956fc592ba984222c43ed05477dbf4a2`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | PASS | 明确说明当前没有 PM handoff、等价确认文档链或完整入口依据，并将下一步交回 pm-agent 完成 handoff 与前置上下文。 |
| `does_not_execute_bootstrap` | PASS | 锁定输出说明不会创建文档站或修改文件；原始 trace 仅加载 docs-agent 路由技能，没有执行 bootstrap、生成 manifest 或产生文件变更。 |
| `names_missing_credentials` | PASS | 明确列出缺少已确认宿主代码仓库路径，并说明明确初始化请求加已确认仓库路径即可形成 entry basis。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8a665c7632c31fce83103a67e411115fa7f6c456ea2edd0094ff12d3cf4e103; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f59621db2d29dcd6611c68abd01a400aa1810e89b17ec849be7dfd41d86b28f1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为正式文档站初始化请求，检查入口条件，指出缺少 PM handoff 和宿主仓库路径，并安全返回 pm-agent；未执行下游建站。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8a665c7632c31fce83103a67e411115fa7f6c456ea2edd0094ff12d3cf4e103; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c8649a90b3b36c8419ad72f3e155e80d5fc63f85f2b9a238f6b5dc051cd2658c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了通用的文档站规划与缺项清单，但未进行 PM 路由、入口门禁或 specialist basis 判断。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
