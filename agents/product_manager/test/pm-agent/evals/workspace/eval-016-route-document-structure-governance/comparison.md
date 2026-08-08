# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-016-route-document-structure-governance`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8` from `agents/product_manager/test/pm-agent/evals/workspace/eval-016-route-document-structure-governance`.
- Fixture SHA-256: `1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8`
- Prompt SHA-256: `78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ba37454a106688e9f5f2e2586231a60f2093e364612eb14bfa53540c9e2d1589`
- Metadata SHA-256: `fe53b448dd4fd2693ceb179d875dd617b7b717601fc7d9d3214cab940b4cdef7`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_structure_governance` | NOT_EXERCISED | with_skill 输出未说明主 route 或路由目标。 |
| `read_only_audit` | PASS | 明确称已完成“只读检查”、仓库未修改；git evidence 显示无变更。 |
| `report_form` | PASS | 提供了运行期 tmp 目录中的 HTML 报告链接，并在对话中给出结论摘要。 |
| `scope_six_role_dirs` | FAIL | 明确指出当前仅有 PM、Engineer 两个角色目录，未覆盖 Design、QA、DevOps、Security。 |
| `structural_change_requires_confirmation` | NOT_EXERCISED | 输出未提出合并、拆分或移动建议，也未说明需确认或 change_tier major。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3; fixture_sha256=1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8; output_sha256=b4a752abfee5d7c81671c7157923e966b100985f34eae02a12f0c74ad8c6c2d8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 明确执行只读检查，生成并链接了 tmp HTML 报告，识别出缺失的四个角色目录；未展示路由选择或结构变更确认规则。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a9ed4a2ff6af194b93c81277958547f5a87533a70b2aa14e43822f139e54d3; fixture_sha256=1a6d7fa4c22a394f3c854eef7a25f4d0cf2e6b4ecd7c7a3d3bf15d295d6e43f8; output_sha256=9cdba9ca5f8bcbd7767dd9666ff2dd88f9977d2882bcd9d8cfa7df07dd261c08; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了基础文档长度、目录和路径检查，但仅覆盖实际存在的 PM 与 Engineer 目录，未体现六角色范围、路由或结构变更确认语义。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未满足六角色目录覆盖要求。
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

# Eval Result: eval-016-route-document-structure-governance

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-016-route-document-structure-governance`
- Workspace: `eval-016-route-document-structure-governance`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-016-route-document-structure-governance/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: PARTIAL — 4/5 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `routes_to_structure_governance`: with-skill **PASS**; without-skill **NOT_EXERCISED** — with_skill trace 明确分类为 document_structure_governance，且读取的 pm-agent 路由表指定 idea-to-spec:structure-governance。
- `read_only_audit`: with-skill **PASS**; without-skill **PASS** — 两份最终回复及 trace 均声明只读检查；两份 status 的 added/removed/modified 均为空，且 result_manifest 与 fixture_manifest 一致。
- `report_form`: with-skill **FAIL**; without-skill **FAIL** — 两份最终回复都只提供 Markdown 对话内容；trace 中没有生成或写入 HTML 运行期 tmp 报告的工具调用。
- `scope_six_role_dirs`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — fixture 实际仅包含 docs/pm 与 docs/engineer，缺少 design、qa、devops、security 实体，因此按规则标记为 NOT_EXERCISED。
- `structural_change_requires_confirmation`: with-skill **FAIL**; without-skill **FAIL** — with_skill trace/最终回复未说明合并、拆分、移动建议需用户确认、change_tier=major，或明确不在本次梳理中执行；without_skill 同样未覆盖该治理约束。

## With-Skill Behavior

正确识别并路由为 document_structure_governance，执行了只读扫描且没有文件变更；但未生成 HTML 运行期报告，也未在结论中落实 major/用户确认约束。六角色覆盖因 fixture 缺少实体而无法评估。

## Fresh Without-Skill Baseline

完成了基础只读目录检查且无文件变更，但没有可验证的结构治理路由、HTML 运行期报告或结构变更确认约束；六角色覆盖因 fixture 缺少实体而无法评估。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill 未生成 HTML 写入运行期 tmp 的报告。
- with_skill 未明确结构变更建议须用户确认并按 change_tier=major 另行执行。
- without_skill 同样未满足 HTML 报告形态和结构变更确认约束。

## Coverage Gaps

- fixture 仅有 pm、engineer 两个角色目录，design、qa、devops、security 缺失，六角色覆盖断言无法实际评估。

## Blockers

- None.

## Historical Result (Pre-#234)

- The previous durable result recorded Behavior **PASS**, Coverage **FULL**, and Overall **BLOCKED** after issue #234 identified prompt/fixture leakage.
- That pre-remediation result is retained only as history and is superseded by this strict fresh run.

## Next Steps

- Fix the with-skill failures listed above, then rerun this eval with the same strict isolation and independent-judge protocol.

## Runtime Artifacts Policy

- Candidate responses, traces, status manifests, isolation records, and judge evidence remain under the gitignored runtime path above and are not committed.
