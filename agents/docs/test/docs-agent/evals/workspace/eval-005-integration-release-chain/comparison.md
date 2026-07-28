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
- with-skill 读取 Docs router、`release-notes-generator`、`docs-audit` 与 PM `github-release-generator` 契约；without-skill 未读取或应用目标 skill、Agent README、assertions、旧 comparison、历史 baseline 或 with-skill 输出。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（7/7 assertions exercised）
- Overall result: PASS
- With-skill: **7/7 PASS**
- Fresh without-skill: **4/7 PASS、3/7 FAIL**
- Relative uplift: **+3 assertions**，语义通过率从 57.1% 提升到 100%。

两侧都正确返回 `blocked`，但不是等价表现。with-skill 识别站内 Release Notes 正文确认凭据缺口、缺失的 pre-tag 权威、tag/tree 漂移和 evidence branch 并发漂移，并把不同缺口交还正确 owner。baseline 只识别了对象漂移和 pre/post-tag 成功证据缺失。

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
- 将 fixture 与脚手架中的历史 issue 身份引用替换为 `docs-agent:release-notes-generator`、`docs-agent:docs-audit`、`pm-agent:github-release-generator`。

## Assertions

- `accepts_release_audit_entry`: with-skill PASS；baseline PASS。两侧均接受已确认版本、范围与只读边界。
- `evaluates_site_release_notes_gate`: with-skill PASS；baseline **FAIL**。with-skill 拒绝缺少正文确认凭据的 ready handoff，并返回 `docs-agent:release-notes-generator`；baseline 将其视为可进入 docs-audit。
- `validates_release_window_basis`: with-skill PASS；baseline **FAIL**。with-skill 解析 base、target、previous tag 与版本 surfaces；baseline 未验证完整 compare window。
- `rejects_missing_pre_tag_authority`: with-skill PASS；baseline PASS。两侧均未从原始目标树推断 `ready_for_tag`。
- `detects_post_tag_evidence_drift`: with-skill PASS；baseline PASS。两侧均发现实际 tag/tree 与 snapshot 不同，且 evidence branch 不等于 expected ref。
- `blocks_github_release_handoff`: with-skill PASS；baseline **FAIL**。with-skill 按依赖顺序返回 Release Notes owner、宿主 tag owner 与 docs-audit；baseline 跳过正文确认 owner，直接交给 docs-audit。
- `preserves_no_mutation_boundaries`: with-skill PASS；baseline PASS。两侧均未执行真实 tag、远端或 GitHub Release 写入。

## With-Skill Behavior

- 将现有 `docs/site/` 识别为 site-enabled host，不允许以无文档站路径降级。
- 发现 `release-notes-handoff.md` 自称 ready，但缺少正文确认凭据，因此不能作为 docs-audit 的有效上游 handoff。
- 从实际 Git 对象确认 `v1.3.0` 指向 base，target/tag-entry snapshot 指向目标 commit，当前 `v1.4.0` tag 多出 `.eval-drift-marker`。
- 确认 target 与 tag tree 均缺少固定 pre-tag candidate/discovery 权威，不能产生 `ready_for_tag` 或 `release_verified`。
- 确认 release-evidence branch 已偏离 expected ref，禁止覆盖并发移动。
- 结果：7/7 PASS；Behavior PASS；Coverage FULL。

## Fresh Without-Skill Baseline

- 来源：同一新 prompt 与独立 pristine fixture 的 fresh baseline；未复用历史 baseline。
- 正确识别 tag/tree 漂移、evidence branch 漂移、缺少 pre/post-tag 成功证据和零写入边界。
- 未识别站内 ready handoff 缺少权威正文确认凭据，未证明完整 release window，并把首要补救直接交给 docs-audit。
- 结果：4/7 PASS、3/7 FAIL；相对 with-skill 存在 3 条可测量差距。

## Failures And Iterations

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
