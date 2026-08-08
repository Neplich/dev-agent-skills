# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-015-route-docs-site-deployment-gap`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013` from `agents/product_manager/test/pm-agent/evals/workspace/eval-015-route-docs-site-deployment-gap`.
- Fixture SHA-256: `16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013`
- Prompt SHA-256: `f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6e2d29edefa67ed434a00461a929405f7c4bccd693a99ad48559b546fe6fab29`
- Metadata SHA-256: `e7a743e88e4c53094e4afe2903a87ebcc467ace2dc58c61ccb0a0dcf64ebf2fd`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unknown_evidence` | FAIL | 当前材料没有环境权限证据；with_skill 未报告 unknown 或明确指出该缺口，反而称范围已明确。 |
| `builds_repo_wide_deployment_packet` | FAIL | with_skill 未生成包含 request_type=deployment、N/A feature fields、空 feature_path_evidence、source_documents 和 blockers_risks 的结构化 handoff packet。 |
| `routes_devops_ordered_chain` | FAIL | with_skill 仅给出泛化的建议顺序，未按要求交接给指定的四个 agent，也未明确最终 Docs 步只同步已落地且验证的运维事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=e34b3c550d50c324cad8d420ff1bb1a2b1efc220ce7b40169d50b4573d202795; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出 CI/Helm 范围不足及维护者授权边界，并建议补齐配置和验证，但未满足所要求的 unknown、结构化 deployment handoff 或指定 agent 链路。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=eaeb5f42e4cb8fe98d59aba4d06ecd1fda09d3a45e4460966e56360a9d9a021c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出 CI 仅构建 public、Helm 未启用 internal，并建议计划与责任交接。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足三个断言。
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

# Eval Result: eval-015-route-docs-site-deployment-gap

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-015-route-docs-site-deployment-gap`
- Workspace: `eval-015-route-docs-site-deployment-gap`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-015-route-docs-site-deployment-gap/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `blocks_unknown_evidence`: with-skill **PASS**; without-skill **PASS** — 两组最终回复及 trace 都保留了初始 unknown、Public 已集成、Internal 缺失，并明确未验证部署/不推断 ready handoff。
- `builds_repo_wide_deployment_packet`: with-skill **FAIL**; without-skill **FAIL** — with_skill 未生成或呈现 deployment handoff packet，缺少 request_type、N/A feature fields、空 feature_path_evidence 及结构化 source_documents/blockers_risks。without_skill 仅生成完整性报告。
- `routes_devops_ordered_chain`: with-skill **FAIL**; without-skill **FAIL** — 两组最终回复均未按 devops-agent:deployment-planner → devops-agent:cicd-bootstrap → devops-agent:env-config-auditor → docs-agent:formal-docs-sync 给出有序 handoff，也未证明 Docs 仅同步已落地且验证的运维事实。

## With-Skill Behavior

证据不确定性处理正确，但未完成所需的 repo-wide deployment packet 和有序 DevOps/Docs 路由。status 显示零 fresh 文件写入；trace 仅执行读取与回复，无外部 mutation。

## Fresh Without-Skill Baseline

正确保留 unknown/缺口边界，但同样未生成 deployment packet 或完成有序路由；status 显示新增 docs-site-completeness-report.md。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill 未满足 builds_repo_wide_deployment_packet。
- with_skill 未满足 routes_devops_ordered_chain。

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
