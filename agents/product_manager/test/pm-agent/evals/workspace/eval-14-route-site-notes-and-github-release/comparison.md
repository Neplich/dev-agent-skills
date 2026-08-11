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
- Repository HEAD: `e2d0e3e00078c297194828182b4d6445ecbb492d`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c658e8351498435bd5246b692fbf8a3a6d40caa45d6998b37785e6522243068b`
- Skill overlay SHA-256: `6e906e23fd0805526cda111a5e2e74eb02ce2f72534b3e384e90b10a34160090`
- Judge schema SHA-256: `0e6be21ab02e72aa076a9b774d5cc60139434feba550f781574340027908427d`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | PASS | with_skill 的路由决策明确将站内版本说明的 selected_owner 设为 docs-agent:release-notes-gen，并说明先处理站内说明。 |
| `routes_github_release_to_pm_specialist` | NOT_EXERCISED | with_skill 明确列出 PM github-release-gen 为后续能力，但该能力未安装；GitHub Release 路由/执行尚未发生，因缺少运行时能力而未行使。 |
| `preserves_release_sequence` | NOT_EXERCISED | with_skill 说明站内说明先于 GitHub Release 预览，但确认、Docs gates、ready handoff 与 release audit evidence 的后续流程尚未发生，因缺少专项能力及确认输入而未行使。 |
| `does_not_use_old_pm_skill_name` | PASS | with_skill 将 docs-agent:release-notes-gen 与 PM github-release-gen 明确区分，未把 PM owner 命名为 release-notes-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=667902e72aa6ee3e6c7beccfc1df946bb11b6dca62cdf1e1c21bee9de8de118b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成 Docs 路由并识别后续 PM 专项，但在缺少专项能力和确认输入时安全阻塞，未生成或发布未经依据的内容。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=7a1530cedb8271581c7ea2b69dcd86b49d79fb082f649e671892274674c32d7c; snapshot_sha256=db80a02e38a3542f8fbd6b2d0f9cec17568a8b59eb5f8745d9420ec45d950e05
- Behavior: 直接创建站内版本说明和 GitHub Release 预览草稿，未发布；未体现专项路由或 site-first handoff 流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 安装所需 Docs 与 PM 专项能力，并提供或确认 v1.0.0 变更资料后继续交互流程。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
