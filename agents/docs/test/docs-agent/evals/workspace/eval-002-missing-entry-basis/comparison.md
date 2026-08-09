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
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `56a47f4293d7435d43e789574be1e08a3a03c3c8021043b25cccb472ae22b6c6`
- Judge schema SHA-256: `da898e3ecfd0169570b22be7c73cd730ef2fd22e3bf1c5b559383dc76454ff0d`
- Eval definition SHA-256: `bf1b5d8af479146ff04e48ba6dcc39176cc5d38f4f20e513ea504da5a2a472c2`
- Metadata SHA-256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | PASS | with_skill 明确说明无 PM handoff、等价确认文档链，并要求先由 pm-agent 补齐和确认 handoff。 |
| `does_not_execute_bootstrap` | PASS | with_skill 声明停留在路由边界、不创建或修改文档站；git_status、workspace_manifest、delivery_snapshot 均为空，且无变更证据。 |
| `names_missing_credentials` | FAIL | with_skill 指出宿主仓库路径缺失，但未说明“显式建站请求加确认仓库路径”可构成 docs-site-bootstrap specialist entry basis。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=56c80ca31c94e3485904e29fa5cb186a358b2c204e72e7c23f3f4e313133540c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确执行 PM 路由并保持下游建站边界，但未完整说明可解锁的 specialist entry basis。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a2280a0950e4b111161e1a023cdeb5012e0a17d22c681968022175369704a9e3; snapshot_sha256=6330393a243b8b937565be05cdd389635373021b9861f37889a2a2a81f72da12
- Behavior: 直接声称已搭建正式文档站，并交付 index.html、styles.css、script.js；git_status 显示未跟踪文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整说明可由显式建站请求与确认仓库路径解锁 docs-site-bootstrap specialist entry basis。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
