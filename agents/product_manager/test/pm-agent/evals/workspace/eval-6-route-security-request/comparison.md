# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-006-route-security-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-6-route-security-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `33054d35eb6adb9b2259eedec7e911d8545eb305cd711e4206483eea10d13a8f`
- Metadata SHA-256: `b68604b9408ecd1ae4f680e8b6bea0f1c221e273dc6389c6b8150eff4b36f0d2`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_security` | FAIL | with_skill 输出讨论安全审查，但没有明确将请求分类为 `security`。 |
| `security_scope_first` | FAIL | with_skill 输出未先记录 risk surface、assets、permissions、data flow 和 remediation expectations；仅说明工作区材料缺失并列出后续事项。 |
| `security_handoff` | FAIL | with_skill 输出没有 handoff Security，也未携带 scope 和 required output。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=10f5709554fd1f05db80eda41f4fde78b6e9edeeb70209a3584c2134046ffa93; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 指出无法完成代码级安全审查并给出上线前阻断项，但未满足三项结构化安全流程断言。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a87ac6a2c8ddea7ec4e431507f8ce429449a4a655650b0889176d97feb45cf44; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出安全审查材料缺失并给出上线前建议，但未执行要求的 security 分类、范围记录或 Security handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确分类为 `security`。
- with_skill 未先记录规定的安全范围字段。
- with_skill 未 handoff Security 并携带 scope 和 required output。
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
