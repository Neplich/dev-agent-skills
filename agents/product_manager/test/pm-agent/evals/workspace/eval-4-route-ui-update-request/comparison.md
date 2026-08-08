# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-004-route-ui-update-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-4-route-ui-update-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `cc5c00e0814501d7ed50a7f0170322a995f768ddcee0b14ac461aa95868c10b8`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `601243bb221e4073b25a6eba61d2cbbc1d243cb0d11ebc88b60ef8187a2e86e1`
- Metadata SHA-256: `aa0eca0938ef56711257694af52b821c5be5dbedc9b5982d77710814288d3115`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_design_or_update` | FAIL | with_skill 未将请求明确分类为 `design` 或 `existing_update`，仅说明缺少现有页面/文档并提出方案确认。 |
| `pm_designer_engineer_decision` | FAIL | with_skill 未判断 PM 预期更新、Designer 设计产物或 Engineer 前端实现路径。 |
| `implementation_waits_for_alignment` | FAIL | with_skill 未提及 PM/TRD/design 对齐或向 Engineer handoff 的等待条件；虽未直接实现，但没有建立该明确门槛。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc5c00e0814501d7ed50a7f0170322a995f768ddcee0b14ac461aa95868c10b8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a92043b591d222960fea34825207e1eb7eb50ca78a20c507bba5757ca5766abc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 先指出缺少现有页面或设计文档，要求补充材料并确认桌面端双栏方案；未明确分类请求、区分 PM/Designer/Engineer 路径或定义对齐后 handoff 门槛。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc5c00e0814501d7ed50a7f0170322a995f768ddcee0b14ac461aa95868c10b8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=efbb516bf9eb9a3d00fdfccb4c8a5baad6a83d7d1b251eaad765b005f94469bc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 直接给出设置页双栏 UI 方案和交互细节，并建议确定决策后进入视觉稿或代码实现；未进行角色路径判断。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未满足三项断言。
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

# Eval Result: eval-004-route-ui-update-request

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-004-route-ui-update-request`
- Workspace: `eval-4-route-ui-update-request`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-004-route-ui-update-request/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 4/4 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `request_type_design_or_update`: with-skill **PASS**; without-skill **FAIL** — with_skill 最终回复明确分类为 existing_update；without_skill 直接判为 Engineer 路径，未作所需 PM 分类。
- `pm_designer_engineer_decision`: with-skill **PASS**; without-skill **FAIL** — with_skill 指出先由 PM 收敛需求，并按是否需要设计产物转 Designer、范围确认后转 Engineer；without_skill 将 Engineer 作为主要执行者，未完成 PM 路由判断。
- `implementation_waits_for_alignment`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确要求先确认设计和技术范围，再修改前端；without_skill 直接建议 Engineer 执行。
- `no_fresh_writes_or_external_mutation`: with-skill **PASS**; without-skill **PASS** — 两份 status 的 changes 均为空；trace 仅显示读取技能文件和输出回复，无写入或外部 mutation。

## With-Skill Behavior

正确走 PM 路径，分类为 existing_update；先收敛产品范围，再按需交接 Designer，设计和技术范围确认后交接 Engineer。

## Fresh Without-Skill Baseline

错误地直接走 Engineer 路径，仅将 Designer 作为可选参与者。

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
