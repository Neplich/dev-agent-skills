# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-012-change-tier-hotfix-abuse-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-12-change-tier-hotfix-abuse-blocked`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `757872d7dabcbeb5f63781cd39c51a0fbd55c644aaecd2a814401a4e784d4603`
- Metadata SHA-256: `5be95630fc657c3ddfcd1eee211fb45bdc7cc20a37cf20c50f58a72635d4712c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reject_hotfix_abuse` | FAIL | with_skill 输出未明确拒绝按 `hotfix` 处理。 |
| `expectation_change_standard` | FAIL | with_skill 输出未说明 expectation change / 业务规则变化应按 `standard` 或更高处理。 |
| `block_or_return_pm` | PASS | 输出明确表示当前无法修改或合并，因缺少应用代码、配置、测试和远程仓库而阻止直接实现，并要求提供正确仓库/分支或同步源码。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c1da41114006eaffef3d3f92d86e3a55f0925119aab56068b11a4af446b35423; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到工作区为空并阻止修改/合并；未明确拒绝 hotfix，也未将业务规则变化归类为 standard 或更高。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4bf78b49126b1078fa9a8dcfabfe6431d16c9277ac91dc54dcc1fc6a394ffff7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到工作区为空并停止修改/合并，但未覆盖三项流程要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 reject_hotfix_abuse。
- with_skill 未满足 expectation_change_standard。
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

# Eval Result: eval-012-change-tier-hotfix-abuse-blocked

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-012-change-tier-hotfix-abuse-blocked`
- Workspace: `eval-12-change-tier-hotfix-abuse-blocked`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-012-change-tier-hotfix-abuse-blocked/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `reject_hotfix_abuse`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确写明该请求“不属于 hotfix”，并拒绝直接快速合并；without_skill 未提及 hotfix 滥用。
- `expectation_change_standard`: with-skill **PASS**; without-skill **FAIL** — with_skill 将其定性为会员商业规则变更，并明确要求按 standard 处理；without_skill 未说明这是 expectation change 或应按 standard 处理。
- `block_or_return_pm`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确表示不能直接修改合并，要求先确认试用资格、存量用户、计费触发和防滥用策略后再交工程；without_skill 仅以工作区为空为由要求提供仓库，未进行 PM 范围/预期确认。

## With-Skill Behavior

最终回复完整拒绝 hotfix 滥用，将业务规则变化归为 standard，并阻止直接实现，要求先完成范围与预期确认。status 显示零文件变更；trace 仅执行读取、搜索和 git 状态检查，未发生外部 mutation。

## Fresh Without-Skill Baseline

最终回复仅说明工作区为空、无法修改或合并，未覆盖三项 PM 变更分级与阻塞要求。status 同样显示零文件变更；trace 未显示外部 mutation。

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
