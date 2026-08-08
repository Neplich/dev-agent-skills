# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-007-direct-downstream-without-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-7-direct-downstream-without-handoff`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b986e7826ca166d1da0b8e0017bd8206728589a4fd4770b206226ac2a418b2fb`
- Metadata SHA-256: `70b36659756bbd4d7fc0e09d0fabc7ee5ba1a168323c148fa735110fb59ec768`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reject_direct_downstream` | FAIL | with_skill 仅说明当前无法直接实现，未明确提及不能进入 engineer-agent 或其他 downstream execution。 |
| `return_to_pm_agent` | FAIL | with_skill 输出未将请求返回 pm-agent，也未要求进行 request_type、scope、feature_path 和 handoff readiness 分类。 |
| `require_handoff_or_docs` | FAIL | with_skill 仅要求源码、文件路径或技术栈，未要求 PM handoff packet 或等价的 PRD/TRD/design/test/deployment/security 文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6e33ed424c8e600a69dfd513e595e398605065a74cfd6afc1707be91475b2c92; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别空仓库并停止工程实现，要求源码或初始化选项，但未执行规定的 PM 分类与 handoff gate。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e3866dd33f7475fede8a21e070a45cf68fb5ccb8f9a6710eb97f418c1e604320; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别空仓库并停止实现，但未覆盖规定的 PM 入口、下游拒绝和 handoff 文档要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确拒绝进入 engineer-agent 或其他 downstream execution。
- with_skill 未返回 pm-agent 进行请求分类。
- with_skill 未要求 PM handoff packet 或等价确认文档。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

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

# Eval Result: eval-007-direct-downstream-without-handoff

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-007-direct-downstream-without-handoff`
- Workspace: `eval-7-direct-downstream-without-handoff`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-007-direct-downstream-without-handoff/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 4/4 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `reject_direct_downstream`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确拒绝直接修改/代替 Engineer；without_skill 仅说明工作区为空。
- `return_to_pm_agent`: with-skill **FAIL**; without-skill **FAIL** — 两者均未明确返回 pm-agent 并完成 request_type、scope、feature_path、handoff readiness 分类。
- `require_handoff_or_docs`: with-skill **FAIL**; without-skill **FAIL** — 两者均未要求 PM handoff packet 或等价已确认 PRD/TRD/design/test/deployment/security 文档。
- `_status_and_trace_zero_write_check`: with-skill **PASS**; without-skill **PASS** — 两份 status 均无 added/removed/modified；trace 仅有读取命令，无写入或外部 mutation。

## With-Skill Behavior

拒绝直接修改成立，但缺少 PM 分类回流和 handoff/document 门禁。

## Fresh Without-Skill Baseline

未执行 PM 路由门禁。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill 未满足 return_to_pm_agent
- with_skill 未满足 require_handoff_or_docs
- without_skill 未满足三项行为断言

## Coverage Gaps

- None.

## Blockers

- None.

## Historical Result (Pre-#234)

- The previous durable result recorded Behavior **PASS**, Coverage **FULL**, and Overall **BLOCKED** after issue #234 identified prompt/fixture leakage.
- That pre-remediation result is retained only as history and is superseded by this strict fresh run.

## Next Steps

- Fix the with-skill failures listed above, then rerun this eval with the same strict isolation and independent-judge protocol.

## Runtime Artifacts Policy

- Candidate responses, traces, status manifests, isolation records, and judge evidence remain under the gitignored runtime path above and are not committed.
