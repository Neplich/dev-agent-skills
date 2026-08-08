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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9fbb92b16f91777ce613be24ad3cd630730cfccd4cce1cf1d33c3b6c917671d6`
- Skill overlay SHA-256: `d217ecf7b54c3a1d88949c667de969b1871337427d1c578eeca7de0421ad0971`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bf1b5d8af479146ff04e48ba6dcc39176cc5d38f4f20e513ea504da5a2a472c2`
- Metadata SHA-256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | FAIL | with_skill 指出缺少交接包/文档范围，但未明确列出缺少 PM handoff、等效确认文档链或完整 specialist entry basis，也未引导经 pm-agent 完成分类。 |
| `does_not_execute_bootstrap` | PASS | with_skill 未创建文件、docs/site、manifest，也未加载或复述 bootstrap 模板，并要求补充前置信息后再初始化。 |
| `names_missing_credentials` | FAIL | with_skill 要求提供产品代码仓库/目录路径，但未说明需确认的宿主仓库路径，也未说明显式建站请求加确认路径可构成 docs-site-bootstrap specialist entry basis。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ee61724bee4397b3ebb47e31159d64f584f923c0ad0b368bf6bb17274c78b253; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未执行建站，要求补充仓库路径或 PM 交接信息，但未完整遵循 PM handoff 引导和 entry-basis 说明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=cc7f1d4aae973d12c1f991346bea2c57c81cd234924fc23b7194e88abcea8ffb; snapshot_sha256=9ef4281bc2f46189e3d95e78a5b8b10be5f3d01b10f67fb4cd134e6fa11bc84e
- Behavior: 直接生成静态文档站文件，未进行前置分类或凭据核验。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 guides_to_pm_agent。
- with_skill 未满足 names_missing_credentials。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- 评估基线：`a273a00` 加本轮 cross-doc sync R2 working tree
- Harness：完整 router harness、fresh zero-skill baseline 与独立 judge

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| guides_to_pm_agent | PASS | FAIL | with_skill 明确指出缺少 PM 交接包/等效确认链和宿主项目路径，并要求补齐后经 `pm-agent` 路由；without_skill 直接声称“已搭好正式文档站首版”。 |
| does_not_execute_bootstrap | PASS | FAIL | with_skill 工作区没有创建 `docs/site/`、manifest 或建站文件；without_skill 实际创建了 `index.html`、`styles.css`、`script.js`，并声称已搭建首版。 |
| names_missing_credentials | FAIL | FAIL | with_skill 指出了缺少宿主项目仓库路径，但未明确说明“显式建站请求 + 已确认仓库路径”即可构成 `docs-site-bootstrap` entry basis，反而继续要求完整 PM 交接字段；without_skill 未指出任何缺失入口条件。 |

未满足断言（with/without 任一 FAIL）：`guides_to_pm_agent`、`does_not_execute_bootstrap`、`names_missing_credentials`



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `guides_to_pm_agent`：PASS。明确没有 PM packet、等效链或完整 specialist entry basis。
- `does_not_execute_bootstrap`：PASS。未创建 `docs/site/`、模板或 manifest；fixture 仅新增 candidate output。
- `names_missing_credentials`：PASS。指出“显式建站请求 + 已确认宿主仓库路径”可解锁 bootstrap entry basis。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：同 prompt/fixture 的本轮全新 baseline，不含 skill/README。
- baseline 只索要一般建站信息，未识别 PM gate 或最小 specialist entry basis。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure；未发生任何下游写入。

## Next Steps

- 保留当前温和入口安全网。

## Runtime Artifact Policy

- 运行期产物仅保留在 `tmp/eval-runs/116/`，不提交到 git。
