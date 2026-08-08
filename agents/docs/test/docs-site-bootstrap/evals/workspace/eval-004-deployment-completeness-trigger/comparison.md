# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Fixture SHA-256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4a398cfa9db1074844549bc002d7714ae1641dceb87757d5c772d45182765b8a`
- Skill overlay SHA-256: `4e5a2571a4a7180fe735bec31f7744892dd9b213e7966b85237f9d1c2b22d88a`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- Metadata SHA-256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_first_bootstrap_integrated` | FAIL | with_skill 输出将 atlas-docs 判为“部分连通，未完成发布闭环”，未体现 durable commit 确认后的首次 integrated 判定或不重复执行 DevOps。 |
| `asks_first_bootstrap_choice` | FAIL | with_skill 输出未将镜像化宿主判为 not_integrated，也未明确询问纳入全部变体、独立托管 not_applicable、暂缓保留 blocker 三个选择。 |
| `rechecks_rebootstrap_drift` | FAIL | with_skill 输出未体现重复 bootstrap、重新读取配置、识别 Internal 启动路径漂移并重新询问进入 PM 到 DevOps 链路。 |
| `preserves_authorization_boundary` | PASS | 输出明确为只读检查，未声称执行 push、镜像发布、部署或修改 Docker/CI/CD/Compose/Helm；仅将后续工作交给文档维护者及发布/平台团队。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=09a202e03a46b7d1b4844a04fb56af5a2d9882fc13c8f2e59623440cd28b583c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供只读仓库链路审计、证据和责任分工；未执行或描述断言要求的 bootstrap 流程。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=3d3561d7588e7d04285e9ae0be1a6978a6aa5eac4b095225cf718ce88c0fda73; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供仓库链路审计和阻断点，但未覆盖首次 bootstrap 选择、重复 bootstrap 漂移或授权边界流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足首次 integrated 判定断言。
- with_skill 未满足首次未集成三选一断言。
- with_skill 未满足重复 bootstrap 漂移复核断言。
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

- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

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
| `classifies_first_bootstrap_integrated` | PASS | PASS | 两条 `result.txt` 均依据 `evidence.md`，列出 Public/Internal、Docker、Tag CI、Compose、Helm、健康检查、TLS 和网络认证，并说明仅做只读核验、未重复执行发布部署。 |
| `asks_first_bootstrap_choice` | FAIL | FAIL | 两条产物均仅说“补齐”缺失的 Dockerfile、CI、Compose、Helm 配置，没有明确询问三选一：全部纳入、独立托管 `not_applicable`、暂缓并保留 blocker。 |
| `rechecks_rebootstrap_drift` | FAIL | FAIL | 两条产物都识别了 `.generated/internal` → `.generated/private` 的路径漂移，但没有判为 `partial`，也没有重新询问是否进入 PM → DevOps 补齐链路。 |
| `preserves_authorization_boundary` | PASS | PASS | 两条产物均明确“仅获准只读检查和文档修改”，且未执行或授权 push、镜像发布、部署；没有让 Docs 明确修改 Docker、CI/CD、Compose 或 Helm。 |

未满足断言（with/without 任一 FAIL）：``asks_first_bootstrap_choice``、``rechecks_rebootstrap_drift``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 正确区分首次 integrated、首次 not_integrated、re-bootstrap partial 漂移，给出三选一和授权边界。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-004-deployment-completeness-trigger/candidate-output.md`.

## Fresh Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- BLOCKED (0/4)；识别事实但缺 durable commit trigger、稳定状态、完整三选一与 PM/DevOps 链路。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 缺少共享 closeout 协议。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
