# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1632db2ef57cd08fd5111dc591159b38c9384e4241c7c2810f25eebdc67d578a` from `agents/docs/test/docs-agent/evals/workspace/eval-005-integration-release-chain`.
- Fixture SHA-256: `1632db2ef57cd08fd5111dc591159b38c9384e4241c7c2810f25eebdc67d578a`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9fbb92b16f91777ce613be24ad3cd630730cfccd4cce1cf1d33c3b6c917671d6`
- Skill overlay SHA-256: `5c882a57295d157e3993960abec476d2e269c34163ca7490bf29b90ab3d78823`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- Metadata SHA-256: `c1ee9aeb87a312a5a12a5c6bde57cbe238245b2c2b0147ad5f64c990238e5981`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | With-skill output recognizes v1.4.0 maintainer confirmation, the documented release scope, and the read-only/no-write boundary. |
| `evaluates_site_release_notes_gate` | FAIL | It calls the Release Notes handoff ready and does not return the site Release Notes owner as responsible for the incomplete handoff credentials, despite the missing pre-tag authority and release verification. |
| `validates_release_window_basis` | FAIL | It identifies the candidate/tag tree mismatch but does not verify the configured previous-tag and base-ref comparison window from the signed snapshot. |
| `rejects_missing_pre_tag_authority` | PASS | It explicitly states that formal pre-tag audit authority is missing and refuses to infer that the tag is bound to an audited document tree. |
| `detects_post_tag_evidence_drift` | PASS | It correctly identifies that the v1.4.0 tag tree differs from the release-candidate/tag-entry tree and concludes the chain is blocked. |
| `blocks_github_release_handoff` | PASS | It concludes GitHub Release preparation or publication cannot continue and does not generate a preview, draft, or publish handoff. |
| `preserves_no_mutation_boundaries` | PASS | It explicitly states that no tag or GitHub Release writes were performed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=1632db2ef57cd08fd5111dc591159b38c9384e4241c7c2810f25eebdc67d578a; output_sha256=15a71edc0f173c63796641377b57dcd988a934565232df33e561a67a3335ea76; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks GitHub Release progression, detects tag/tree drift, rejects missing pre-tag authority, and preserves read-only boundaries, but misses the required release-window validation and assigns incomplete handoff remediation to the wrong owner.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=1632db2ef57cd08fd5111dc591159b38c9384e4241c7c2810f25eebdc67d578a; output_sha256=f4d26bf940bfd37291e2232f0112fd75227e9663d79f489f37d17f7faa0d5810; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks release progression and identifies tree drift, missing post-tag evidence, and inconsistent documentation verification, but provides less explicit pre-tag authority analysis.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not validate the previous-tag/base-ref release window and comparison anchor.
- It treats the site Release Notes handoff as ready and does not return the site Release Notes owner for incomplete gate credentials.
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`
- Scenario: 基于原始站内 Release Notes 与 synthetic Git 对象判断发布链是否具备 GitHub Release 资格
- Review context: issue #177 sub-batch 4a

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-2b`
- Actual validation date: `2026-07-28`
- Fresh run: `tmp/eval-runs/issue-177/docs-agent-eval-005/round-2b-fixture-correction/`
- with-skill 与 without-skill 使用同一 prompt 和独立 pristine fixture；两侧均只在各自隔离 workspace 执行 setup。
- with-skill 读取 Docs router、`release-notes-gen`、`docs-audit` 与 PM `github-release-gen` 契约；without-skill 未读取或应用目标 skill、Agent README、assertions、旧 comparison、历史 baseline 或 with-skill 输出。

## Latest Result

- Behavior result: `PASS`（with）/ `PASS`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `PARTIAL`（with）/ `PARTIAL`（without）— 本轮重跑实际触发的断言场景
Overall result: BLOCKED
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `PARTIAL`
- without_skill：Behavior `PASS` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `accepts_release_audit_entry` | PASS | PASS | `release-chain-entry.md` 明确给出 `target_release_version: v1.4.0`、维护者确认、审计阶段、范围及“仅资格审查、不写入”限制。 |
| `evaluates_site_release_notes_gate` | PASS | PASS | `release-notes-handoff.md` 虽为 `handoff_status: ready` 且 `blockers: []`，但两条 lane 均识别 `evidence/docs-checks.md` 缺失，并将责任交回 `release-notes-gen`。 |
| `validates_release_window_basis` | NOT_EXERCISED | NOT_EXERCISED | 入口虽声明 `previous_tag: v1.3.0`、`intended_target_tag: v1.4.0` 及多个 ref，但 `.git` 初始化失败且 `.eval/runtime-git-evidence.md` 不存在，版本窗口与比较锚点未在 synthetic repository 中实际解析。 |
| `rejects_missing_pre_tag_authority` | PASS | PASS | 两条结果均明确：不能继续 `docs-audit pre-tag`，不能将 handoff 自称的 `passed` 视为可复核的 pre-tag 权威。 |
| `detects_post_tag_evidence_drift` | NOT_EXERCISED | NOT_EXERCISED | `setup-git-fixture.sh` 虽定义了 drift commit 和漂移 tag，但 `.git` 初始化失败，未生成 runtime Git 对象，也未实际完成 post-tag 对象比较。 |
| `blocks_github_release_handoff` | PASS | PASS | 两条结果均明确不得进入 GitHub Release handoff；`release_execution_authorized: false`，且要求等待 `ready_for_tag`、实际 tag、`release_verified` 和独立批准。 |
| `preserves_no_mutation_boundaries` | PASS | PASS | with_skill 明确“未执行任何真实 tag 或 GitHub Release 写入”；without_skill 仅尝试隔离 synthetic fixture setup，因 `.git` 写入受限失败，未修改真实 tag 或 Release。 |

本轮无 FAIL 断言。

未触发断言：`validates_release_window_basis`、`detects_post_tag_evidence_drift`

基础设施阻塞说明：Git 仓库缺失；对应断言不构成 skill 行为回归。



## Leakage Surface Analysis

重做前，baseline 可直接看到并复用以下协议：

- prompt 明示临时 worktree、object reads、两次 staged gate、committed delta gate、CAS、三项 GitHub Release 上游门禁和输出结构。
- assertions 复制七字段 frontmatter、API 细节、Git 命令、candidate/discovery/post-tag schema、路径互指和 handoff 字段清单。
- 910 行 setup 生成并自检 `candidate_verified`、`ready_for_tag` 和 `release_verified`，完成 schema、delta、CAS、readback 与末尾全等 self-check。
- candidate、discovery、成功/阻塞 post-tag 模板直接提供预期记录；baseline 只需复述 setup 已证明的成功结论。
- fixture 文案残留本仓库历史 issue 身份引用，使责任链可从编号而非 skill 语义推断。

## Redesign

- prompt 仅保留任务意图、入口指针、隔离范围与禁止真实写入边界。
- assertions 收敛为 7 条语义结果，不复制字段清单、命令序列或记录 schema；judge 必须对照 skill 文档判断。
- setup 从 910 行缩减为 70 行，只构造 base/target、previous tag、进入检查时的 tag snapshot、漂移后的实际 tag、预期 evidence ref 和并发移动后的 evidence branch。
- 删除 pre-tag candidate/discovery、post-tag success/blocked 模板及全部 setup 协议自检；setup 不生成任何 audit record、success handoff、`ready_for_tag` 或 `release_verified`。
- fixture 增加一个自称 `ready` 但缺少正文确认凭据的站内 handoff，并保留 tag tuple 与 expected-head 漂移，使 skill 门禁而非 setup 成为判定来源。
- 将 fixture 与脚手架中的历史 issue 身份引用替换为 `docs-agent:release-notes-gen`、`docs-agent:docs-audit`、`pm-agent:github-release-gen`。

## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `accepts_release_audit_entry`: with-skill PASS；baseline PASS。两侧均接受已确认版本、范围与只读边界。
- `evaluates_site_release_notes_gate`: with-skill PASS；baseline **FAIL**。with-skill 拒绝缺少正文确认凭据的 ready handoff，并返回 `docs-agent:release-notes-gen`；baseline 将其视为可进入 docs-audit。
- `validates_release_window_basis`: with-skill PASS；baseline **FAIL**。with-skill 解析 base、target、previous tag 与版本 surfaces；baseline 未验证完整 compare window。
- `rejects_missing_pre_tag_authority`: with-skill PASS；baseline PASS。两侧均未从原始目标树推断 `ready_for_tag`。
- `detects_post_tag_evidence_drift`: with-skill PASS；baseline PASS。两侧均发现实际 tag/tree 与 snapshot 不同，且 evidence branch 不等于 expected ref。
- `blocks_github_release_handoff`: with-skill PASS；baseline **FAIL**。with-skill 按依赖顺序返回 Release Notes owner、宿主 tag owner 与 docs-audit；baseline 跳过正文确认 owner，直接交给 docs-audit。
- `preserves_no_mutation_boundaries`: with-skill PASS；baseline PASS。两侧均未执行真实 tag、远端或 GitHub Release 写入。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 将现有 `docs/site/` 识别为 site-enabled host，不允许以无文档站路径降级。
- 发现 `release-notes-handoff.md` 自称 ready，但缺少正文确认凭据，因此不能作为 docs-audit 的有效上游 handoff。
- 从实际 Git 对象确认 `v1.3.0` 指向 base，target/tag-entry snapshot 指向目标 commit，当前 `v1.4.0` tag 多出 `.eval-drift-marker`。
- 确认 target 与 tag tree 均缺少固定 pre-tag candidate/discovery 权威，不能产生 `ready_for_tag` 或 `release_verified`。
- 确认 release-evidence branch 已偏离 expected ref，禁止覆盖并发移动。
- 结果：7/7 PASS；Behavior PASS；Coverage FULL。

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- 来源：同一新 prompt 与独立 pristine fixture 的 fresh baseline；未复用历史 baseline。
- 正确识别 tag/tree 漂移、evidence branch 漂移、缺少 pre/post-tag 成功证据和零写入边界。
- 未识别站内 ready handoff 缺少权威正文确认凭据，未证明完整 release window，并把首要补救直接交给 docs-audit。
- 结果：4/7 PASS、3/7 FAIL；相对 with-skill 存在 3 条可测量差距。

## Failures And Iterations
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Round 1：with-skill 与 baseline 均识别对象漂移并阻止 GitHub Release，仍无区分度。
- Round 2：加入站内 handoff 语义门禁后产生 +2 uplift，但简化 setup 时遗漏入口声明的 synthetic `v1.3.0`，导致双方漏过 release-window assertion；judge 判 with-skill 6/7、Behavior FAIL。
- Round 2 fixture correction：只在 base commit 补回已声明的 `v1.3.0`，不改变 prompt、assertions 或目标阻塞场景；fresh paired rerun 与 fresh judge 得到 with-skill 7/7、baseline 4/7。
- Setup/API/docs command failures: none。

## Next Steps

- 保持本用例为阻塞型集成回归：它衡量完整上游资格与 owner 边界，不把总体 `blocked` 文案当作通过依据。
- 后续若修改 Release Notes、docs-audit 或 GitHub Release gate，应重跑 fresh paired validation，并以本 comparison 的 7 条语义 assertions 判断回归和 uplift。

## Runtime Artifact Policy

- Synthetic repositories、`response.md`、judge verdict、setup logs、runtime object index 与依赖目录仅位于 `tmp/eval-runs/issue-177/docs-agent-eval-005/` 或系统临时目录，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
