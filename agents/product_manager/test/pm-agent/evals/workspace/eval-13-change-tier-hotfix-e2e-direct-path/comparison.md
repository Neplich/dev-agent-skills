# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-013-change-tier-hotfix-e2e-direct-path`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-13-change-tier-hotfix-e2e-direct-path`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `4b716f413649b163f4dd5dcd45dc5b4214bafbb5cb059afb757fef3a77b94653`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0e4e9687500855bbb8cac580183d47bafa14e53a69d5477185a5ceacddfe1857`
- Metadata SHA-256: `385a2edb2c46d9f3ce571c34b812bf357f9247b71af061faebaf0764c87334a2`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `hotfix_direct_path_only` | FAIL | with_skill 输出仅说明无法定位源码并请求补充项目文件，未说明 hotfix 的 QA/E2E 覆盖可限制到 directly affected path。 |
| `evidence_still_required` | FAIL | with_skill 输出未要求记录 verification evidence、结果或任何 blocked checks。 |
| `no_full_suite_required` | FAIL | with_skill 输出未说明不需要完整 E2E suite，也未提及 standard / major 风险或范围升级例外。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4b716f413649b163f4dd5dcd45dc5b4214bafbb5cb059afb757fef3a77b94653; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3e19e24ef4b08296352e49e6993e0eec8998936d75aeff56eff59353098e0d04; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 无法定位源码，直接请求补充项目文件；未提供任何断言要求的 QA、证据或套件范围指导。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4b716f413649b163f4dd5dcd45dc5b4214bafbb5cb059afb757fef3a77b94653; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5c481761c7c50bb7568d8dca183e4bb5cf116766767cd4532a8c05094ebd7318; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 无法定位源码，直接请求补充项目文件；未提供任何断言要求的 QA、证据或套件范围指导。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足三项断言。
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

# Eval Result: eval-013-change-tier-hotfix-e2e-direct-path

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-013-change-tier-hotfix-e2e-direct-path`
- Workspace: `eval-13-change-tier-hotfix-e2e-direct-path`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-013-change-tier-hotfix-e2e-direct-path/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `hotfix_direct_path_only`: with-skill **FAIL**; without-skill **FAIL** — 两份最终回复仅判定为 hotfix 并说明无法定位文件；均未明确说明 hotfix QA/E2E 可限制到 directly affected path。with_skill trace 仅提到“只处理登录页对应文案”，不足以满足该断言。
- `evidence_still_required`: with-skill **FAIL**; without-skill **FAIL** — with_skill 最终回复说无法验证并请求提供项目目录，但未要求记录 verification evidence、验证结果和 blocked checks；trace 也未形成该要求。without_skill 同样缺失。
- `no_full_suite_required`: with-skill **FAIL**; without-skill **FAIL** — 两份最终回复均未说明不需要完整 E2E suite，或仅在风险/范围升级到 standard/major 时需要全量套件。

## With-Skill Behavior

with_skill 正确识别 hotfix，并如实报告工作区缺少源码、无法修改或验证；status 显示零文件变更，trace 仅执行读取与仓库状态检查。但最终回复没有覆盖三项 hotfix QA 输出要求。

## Fresh Without-Skill Baseline

without_skill 同样如实报告空工作区并保持零写入，但也未覆盖任何断言要求。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill 未说明 QA/E2E 覆盖可限制到 directly affected path。
- with_skill 未要求记录 verification evidence、结果及 blocked checks。
- with_skill 未说明无需完整 E2E suite，除非升级为 standard/major。

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
