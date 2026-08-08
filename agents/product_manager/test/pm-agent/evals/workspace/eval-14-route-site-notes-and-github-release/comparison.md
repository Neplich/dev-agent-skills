# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `847ec25f3bf19681577a3386dfc21c378712f63dee7629dde5750b16901ab4e4`
- Skill overlay SHA-256: `85498141fecd6ca653a495454d16dd5a8f8fa77675af6eb45d6d223d0cab1fbd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | NOT_EXERCISED | with_skill 未实际执行 handoff；候选输出因缺少版本范围与变更证据而请求补充信息。 |
| `routes_github_release_to_pm_specialist` | NOT_EXERCISED | with_skill 未实际生成或路由 GitHub Release preview；该后续步骤依赖用户确认和运行时证据。 |
| `preserves_release_sequence` | NOT_EXERCISED | 候选输出仅表达“站内版本说明 → GitHub Release 预览”的计划顺序，未执行 Docs gates、ready handoff 或 release audit evidence 流程。 |
| `does_not_use_old_pm_skill_name` | PASS | with_skill 输出未将 PM owner 命名为 release-notes-gen，也未使用该旧名。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=928ef682e653c06526583f0443664f452ca734aa07f68b3fde172f508e70ae49; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因缺少确认后的版本范围和变更证据而暂停，明确后续顺序并承诺不实际发布；未执行 specialist 路由。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f0bd05858e16fa6309272eaf0afe83a0dbd660c05880464e5439ea14dcf608a8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因仓库无内容而请求版本变更信息；未执行路由或发布，工作区保持不变。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供已确认的 v1.0.0 变更清单或 Issue/PR/提交后，再验证实际 Docs handoff、PM 路由及 release audit evidence 消费。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `847ec25f3bf19681577a3386dfc21c378712f63dee7629dde5750b16901ab4e4`
- Skill overlay SHA-256: `780c8f93b8e6c45b2ccd3c9782ab0565304ee40820ab216a99298b8a0a82b7f1`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | FAIL | with_skill 输出仅列出站内版本说明文件，未明确 handoff 到 docs-agent:release-notes-gen。 |
| `routes_github_release_to_pm_specialist` | FAIL | with_skill 输出仅列出 GitHub Release 预览文件，未路由到 PM github-release-gen。 |
| `preserves_release_sequence` | FAIL | 文档提到完成文档审计后进入 GitHub Release 流程，但未说明 ready handoff、PM github-release-gen 消费或 release audit evidence。 |
| `does_not_use_old_pm_skill_name` | PASS | with_skill 输出及两份文档均未将 PM owner 命名为 release-notes-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=19a1d0f7fdf24b545f96dc52b88151d49a71a13a694a014fcfdf7f1b06e9266a; snapshot_sha256=ffcb749898b3af7b15f2989647f493276c1f7cef577730ebaf5bb80cb0df23a1
- Behavior: 生成站内版本说明草稿和 GitHub Release 预览，并保留未确认、不可发布状态；但未明确 specialist 路由或 handoff 链路。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=307626c1214f041d67f0e6548b160132a7a3de144b49a9a4a86ccbe59a9dd126; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因仓库为空而拒绝生成任何输出，未体现路由行为。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确 docs-agent:release-notes-gen、PM github-release-gen 及 ready handoff/release audit evidence。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | FAIL | with_skill 输出未创建或说明站内版本说明，也未 handoff 到 docs-agent:release-notes-gen。 |
| `routes_github_release_to_pm_specialist` | FAIL | with_skill 输出未生成 GitHub Release 预览，也未路由到 PM github-release-gen。 |
| `preserves_release_sequence` | FAIL | with_skill 输出仅说明无法完成，并未说明站内说明先经 Docs gates 确认，再由 PM 消费 ready handoff 和 audit evidence。 |
| `does_not_use_old_pm_skill_name` | PASS | with_skill 输出未将 PM owner 命名为 release-notes-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=41602464cf3b536e8dd6f911e19f41e17b121203e4556ec1d6fe620582deb79e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因声称仓库为空而拒绝执行任务，未创建任何输出，也未展示路由或发布流程。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=96d818fcf61ffcfb326658ca1f96896af48bb3e59c1d3e45ebc56b2f415e4152; snapshot_sha256=5bc8109740576060b8d1edcaa3723defb56d431b2c21631753a371038142ba7c
- Behavior: 创建了站内版本说明和 GitHub Release 预览，但未提供所需 specialist 路由或 site-first handoff 证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完成任务要求的两类输出及其 specialist 路由。
- with_skill 未证明站内版本说明确认后再生成 GitHub Release 预览的顺序。
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

# Eval Result: eval-014-route-site-notes-and-github-release

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`
- Workspace: `eval-14-route-site-notes-and-github-release`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-014-route-site-notes-and-github-release/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: PARTIAL — 0/4 with-skill assertion scenarios were exercised.
Overall result: PASS (partial coverage)

## Assertion Results

- `routes_site_notes_to_docs_specialist`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — 两份最终回复均未执行或承诺具体 handoff；v1.0.0 的确认范围/实体不存在，无法实际触发 A 路由。
- `routes_github_release_to_pm_specialist`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — 两份最终回复均未生成 GitHub Release preview，也未展示 PM github-release-gen 路由；v1.0.0 来源不足。
- `preserves_release_sequence`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — 未进入站内说明确认或 Release audit gates 阶段，因此无法核对 site-first 顺序。
- `does_not_use_old_pm_skill_name`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — 最终回复和工具轨迹未发生实际 PM owner 命名或路由，无法核对旧名回退。

## With-Skill Behavior

行为未触发断言失败；轨迹识别为 release_notes 工作流并先检查资料，但因缺少 v1.0.0 的项目内容、Git 历史和确认范围而停止澄清。status 显示零新增、零删除、零修改。

## Fresh Without-Skill Baseline

行为未触发断言失败；轨迹通过只读 GitHub 查询确认目标仓库当前为 v0.5.7-fix1、没有 v1.0.0 依据后停止澄清。status 显示零文件变更，未见外部写入或发布调用。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- None.

## Coverage Gaps

- 四项 with_skill assertions 均未实际执行，无法验证具体 specialist handoff、顺序或旧名约束。
- 缺少 v1.0.0 的确认版本范围、变更依据或可消费的 release handoff。

## Blockers

- 实时数据中不存在断言所需的 v1.0.0 版本实体/确认范围。

## Historical Result (Pre-#234)

- The previous durable result recorded Behavior **PASS**, Coverage **FULL**, and Overall **BLOCKED** after issue #234 identified prompt/fixture leakage.
- That pre-remediation result is retained only as history and is superseded by this strict fresh run.

## Next Steps

- Keep the passing behavior result, and rerun when the missing live entities or fixture conditions can exercise the listed coverage gaps.

## Runtime Artifacts Policy

- Candidate responses, traces, status manifests, isolation records, and judge evidence remain under the gitignored runtime path above and are not committed.
