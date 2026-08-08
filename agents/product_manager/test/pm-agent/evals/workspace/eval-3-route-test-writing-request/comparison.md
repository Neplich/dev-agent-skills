# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-003-route-test-writing-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-3-route-test-writing-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4c0ee7c09752627d6057c1ccc0d45cb292b19c1428b51ca9513725150029cf5a`
- Metadata SHA-256: `48e1e31078cfd6a23e5c1bdb5481d8f4c6428eb757f9b42750f6377a78297239`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_validation` | FAIL | with_skill 输出仅说明工作区缺少源码/测试文件并请求挂载正确工作区，未将请求分类为 validation 或等价测试验证路径。 |
| `test_basis_first` | FAIL | with_skill 输出未确认 PRD、TRD、IMPLEMENTATION_PLAN 或既有验收记录作为测试依据。 |
| `qa_or_test_writer_handoff` | FAIL | with_skill 输出未说明在预期稳定且来源文档明确后再 handoff QA 或 Engineer/test-writer。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=9020bc3b9011e3b19b959cafaeb5eb9e20d46453339dae772afea43b40b44da9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样发现工作区为空并请求挂载源码；未体现 validation 分类、测试依据确认或条件化 handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=44d0b57e599ce510063a92e201c3b6a74f55d7c64529ca0661bb9412aea320dd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 发现工作区为空并请求挂载源码；未体现三项流程要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足任一断言。
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

# Eval Result: eval-003-route-test-writing-request

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-003-route-test-writing-request`
- Workspace: `eval-3-route-test-writing-request`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-003-route-test-writing-request/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `request_type_validation`: with-skill **PASS**; without-skill **FAIL** — with_skill-final 明确分类为 `validation`；without_skill 仅称“测试补充/回归测试”，未使用 validation 或等价路由分类。
- `test_basis_first`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确要求先确认 PRD、DECISIONS、TRD/API 契约、实现计划及验收记录，并因依据缺失而阻塞；without_skill 罗列状态机、接口契约等测试内容，但未明确先确认指定的 PRD/TRD/IMPLEMENTATION_PLAN/既有验收记录。
- `qa_or_test_writer_handoff`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确说明预期和来源文档确认前不能 handoff，确认后自动化测试交 Engineer、测试用例/验证交 QA；without_skill 建议交 QA/测试工程师，但未明确以预期稳定且来源文档明确作为前置条件。

## With-Skill Behavior

准确完成 validation 路由；明确测试依据必须先确认，并在依据缺失时阻塞后续 handoff，同时区分 Engineer 与 QA 的职责。status 显示无文件变更，trace 仅读取技能和上下文，无外部 mutation。

## Fresh Without-Skill Baseline

能识别退款异常测试主题并列出测试依据与覆盖点，但未完成规范的 validation 分类，也未满足指定依据和稳定预期后的条件式 handoff。无文件变更，trace 仅读取空工作区。

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
