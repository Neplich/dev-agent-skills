# Eval Result: eval-006-route-security-request

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-006-route-security-request`
- Workspace: `eval-6-route-security-request`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-006-route-security-request/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `request_type_security`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确写出 request_type: security；without_skill 未明确给出该分类。
- `security_scope_first`: with-skill **FAIL**; without-skill **FAIL** — with_skill 记录了仓库安全范围、权限模型、依赖和 secrets，但未完整、明确记录 data flow 及五项要求对应的结构化字段；without_skill 也未记录完整的 risk surface、assets、permissions、data flow、remediation expectations。
- `security_handoff`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确 downstream_owner: Security，并提供 scope_decision 与 required_output；without_skill 未明确交接给 Security。

## With-Skill Behavior

with_skill 正确识别 security，并完成 Security 交接包，但安全范围记录缺少明确完整的 data flow 等必需维度。status 显示零文件变更，trace 仅执行读取命令，无外部 mutation。

## Fresh Without-Skill Baseline

without_skill 给出了风险分类和一般交接清单，但未完成明确的 security 路由分类和 Security handoff。trace 包含一次 git status 命令失败，但无写入或外部 mutation。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill 未满足 security_scope_first：未完整明确记录 risk surface、assets、permissions、data flow 和 remediation expectations，尤其缺少 data flow。

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
