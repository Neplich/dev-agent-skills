# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-002-route-bugfix-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-2-route-bugfix-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `fe6d213ce4edb254dae39c5fefca87002824c8356e6ca05dfa6b8b92c57d378d`
- Metadata SHA-256: `163386e80d321ea48ddfd244853e278bc70ea13a08cdc68ac01f85bf3ba7240f`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_bug_report` | FAIL | With-skill output does not classify the request as `bug_report`; it only reports the workspace is empty. |
| `expectation_first` | FAIL | With-skill output does not consult or mention approved PRD/TRD or equivalent product expectations. |
| `debugger_handoff_after_confirmation` | FAIL | With-skill output contains no confirmation of implementation deviation and no Engineer/debugger handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=8c618b38c767d02b9ca4c2c7d5244f9d87b6240fc1904b5ba7903c1bbbee76c8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reports the workspace is empty and requests project source; does not classify, confirm expectations, or hand off.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=0034a86619eb3ff167c0bd848d86879b01d3b6a68b9a7849bc83015c6ccbbbcc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reports the workspace is empty and requests project source; does not classify, confirm expectations, or hand off.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- All three required with-skill behaviors are absent.
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

# Eval Result: eval-002-route-bugfix-request

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-002-route-bugfix-request`
- Workspace: `eval-2-route-bugfix-request`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-002-route-bugfix-request/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `request_type_bug_report`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确分类为 `bug_report`；without_skill 仅称为登录/鉴权模块前端缺陷，未使用要求的 `bug_report` 分类。
- `expectation_first`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确要求先确认 token 过期后的正确预期，并核对 PRD/TRD 或登录流程文档；without_skill 未要求对照 approved PRD/TRD 或等价产品预期。
- `debugger_handoff_after_confirmation`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确表示只有确认是实现偏差后才交给 `engineer-agent` 调试；without_skill 直接建议交给前端登录/鉴权负责人，未设置“确认实现偏差后”门槛。

## With-Skill Behavior

最终回复完整满足三项 PM 路由断言：分类为 bug_report，先确认 approved PRD/TRD 预期及复现证据，确认实现偏差后再交给 Engineer/debugger。status 显示无 added/removed/modified，trace 仅读取技能与文件，没有外部 mutation。

## Fresh Without-Skill Baseline

回复提供了部分排查信息，但未按要求进行稳定的 bug_report 分类，未先核对 approved PRD/TRD 预期，并在确认实现偏差前直接提出工程负责人路由。status 显示无文件变更；trace 仅执行读取命令。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- None.

## Coverage Gaps

- None.

## Blockers

- None.

## Historical Result (Pre-#234)

- The previous durable result recorded Behavior **PASS**, Coverage **FULL**, and Overall **BLOCKED** after issue #234 identified prompt/fixture leakage.
- That pre-remediation result is retained only as history and is superseded by this strict fresh run.

## Next Steps

- Keep this case as a regression gate and rerun it after changes to `pm-agent`, its routing contract, or this fixture.

## Runtime Artifacts Policy

- Candidate responses, traces, status manifests, isolation records, and judge evidence remain under the gitignored runtime path above and are not committed.
