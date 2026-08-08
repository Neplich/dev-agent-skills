# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-009-missing-handoff-target-unavailable`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-9-missing-handoff-target-unavailable`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ea4ff3ed92cd6df9743d23b747dc29d9087560d5cfa7f5f4525b8e146b0b7e97`
- Metadata SHA-256: `f52777a03f0c132438bf125e153205560b01f6abb53fcb15add6a3552b96312b`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detect_missing_target` | PASS | with_skill 明确说明当前没有可调用的 designer-agent/设计交付代理。 |
| `mark_handoff_blocked` | PASS | with_skill 将交接状态标记为 BLOCKED，并说明需安装或启用提供 designer-agent 的插件。 |
| `do_not_perform_missing_role` | PASS | with_skill 仅产出 PM 路由与阻塞记录，明确不代替 Designer 完成正式视觉设计。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c036d0b275797fd6c89b277c3d0cc95e2c4ac9db484303f1052e6afcab5c80ec; snapshot_sha256=18f7ccddd468b841dba76d57b7e7fadefbd002984aaf28f6bf4ffc3ebe115e28
- Behavior: 识别设计能力缺失，记录 BLOCKED 状态及恢复条件，并保留 PM 路由而不代行 Designer 职责。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=8eb8db9576491f07e8a59fb10c40e831133ec66d46e237a3c4257af52e420d96; snapshot_sha256=fa38d98936128e3c416621d62cc15e479ed7dd75b2372b26b1ca754e0e521027
- Behavior: 生成了设计交接文档，但未识别 designer-agent 不可用，也未标记 handoff blocked。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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

# Eval Result: eval-009-missing-handoff-target-unavailable

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-009-missing-handoff-target-unavailable`
- Workspace: `eval-9-missing-handoff-target-unavailable`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-009-missing-handoff-target-unavailable/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `detect_missing_target`: with-skill **PASS**; without-skill **PASS** — with_skill 明确指出 designer-agent 未安装或无法访问；without_skill 也明确指出设计能力未安装。
- `mark_handoff_blocked`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确将设计阶段和当前状态标记为 blocked，并要求安装/启用设计能力；without_skill 未明确使用 blocked 状态。
- `do_not_perform_missing_role`: with-skill **PASS**; without-skill **PASS** — 两份回复均未代替 Designer 产出视觉规范或设计交付物。with_skill 还明确表示不会代行设计角色。

## With-Skill Behavior

最终回复完整满足三项断言。状态 changes 为空，trace 仅读取 pm-agent skill，无外部 mutation。

## Fresh Without-Skill Baseline

识别了设计能力不可用且未代行 Designer 职责，但未明确将 handoff 标记为 blocked。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- without_skill 未明确标记 handoff stage 为 blocked；该 baseline 失败不影响 Overall。

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
