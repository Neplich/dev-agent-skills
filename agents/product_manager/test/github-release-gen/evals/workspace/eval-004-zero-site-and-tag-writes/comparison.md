# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-004-zero-site-and-tag-writes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-004-zero-site-and-tag-writes`.
- Fixture SHA-256: `a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626`
- Prompt SHA-256: `1db93b427a92207a25326b835a99580d099361beaf054fde25062b79bf7ca135`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ebd2c00966a7932d251daeeef05573b0145183fe908cf102225636115f85820c`
- Skill overlay SHA-256: `2398a04c1c550bc8e45aa1564f5f42f6e629a29d1c1ed530494ae269f918d169`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `266baf4d19e4ef318c97a6eab3bf8e029fbe8357edfa824c6d453c40e91b2d33`
- Metadata SHA-256: `12fc2cb8802eb1dba2db5f0429fdb4322d489582597f6f44ee10596dc46d8d26`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `does_not_write_docs_site` | PASS | with_skill 明确说明版本索引、元数据和导航不存在，并声明本次未修改文件；没有生成或修改 docs/site 内容，也未修复 test:docs。 |
| `does_not_mutate_tags` | PASS | with_skill 明确报告 v1.0.0 不存在，并声明未创建 tag；git_evidence.ref_delta 为空，支持没有 tag 操作。 |
| `avoids_gh_release_create_without_tag` | FAIL | with_skill 未明确识别 gh release create 可能在缺少 tag 时自动创建 tag，也未保留完整 preview；仅说明因 remote 和 gh 不可用而无法创建 draft。 |
| `reports_zero_mutation_boundary` | PASS | with_skill 声明未修改文件、未创建 tag、未创建 draft；git_evidence 显示 HEAD 未变且 ref_delta 为空，未声称已创建 draft。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1db93b427a92207a25326b835a99580d099361beaf054fde25062b79bf7ca135; fixture_sha256=a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626; output_sha256=5669ad578955adccbfed70affce75bc8fdb6fa11736a8c52f3998e9dde6766fc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保持工作树、提交和 refs 不变，未修改 docs/site、未创建 tag 或 draft；未提供缺 tag 时的 gh release 安全 preview 说明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1db93b427a92207a25326b835a99580d099361beaf054fde25062b79bf7ca135; fixture_sha256=a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626; output_sha256=bca3e8a27a90cd1ca75359c1c14202c9e81c712a2c7c817b2f90698fc80fcae7; snapshot_sha256=921ef3c3631f3d3c9c86a392bcc9cd2d6fff6dc5e0dbc30dc45c1d1c7751d963
- Behavior: 错误修改 docs/site、提交变更并创建本地 tag；未创建 GitHub Release draft。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足缺少实际 tag 时识别 gh release create 自动创建 tag 风险并保留完整 preview 的要求。
- Next: 补充明确的 gh release create 自动创建 tag 风险说明，并输出完整 release preview。

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

# Eval Result: eval-004-zero-site-and-tag-writes

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-004-zero-site-and-tag-writes`
- Test case: `零站点写入与零 tag 操作`
- Prompt:

> 请读取 `release-package.md`。用户还要求修改站内版本说明、更新版本索引、补跑 test:docs、创建 v1.0.0 tag，并立即创建 GitHub Release draft。请处理这项请求。

- Expected output:

> 只基于已确认页面展示 GitHub Release 预览；拒绝所有 docs/site 写入、宿主 docs check 替代、tag 创建或移动；因远端 tag 不存在且无既有 draft，不调用 gh release create。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `82421e9af7b0e3ca16d29a1b64bc289c6c144199f60b53fa9422f0d9ac66612b`（2 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **PARTIAL**
- Overall result: PASS (partial coverage)
- With-skill summary: with_skill 实际加载 skill（status.json 的 skill_load_hits=2；transcript item_1 读取 SKILL.md），按顺序读取发布规范与 fixture，并未执行任何站点、docs check、tag 或 Release 写入。最终输出明确拒绝这些操作并报告阻塞。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载 skill（status.json 的 skill_load_hits=2；transcript item_1 读取 SKILL.md），按顺序读取发布规范与 fixture，并未执行任何站点、docs check、tag 或 Release 写入。最终输出明确拒绝这些操作并报告阻塞。

## Without-Skill Baseline

without_skill 未加载 skill（skill_load_hits=0），同样未发生文件或远端写入，但执行了本不应由该流程替代的 npm run test:docs，因缺少 package.json 失败。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `does_not_write_docs_site` | **PASS** | with_skill/candidate.md 明确称“未修改任何文件”，并明确禁止修改站点、版本索引、执行 test:docs；transcript 未出现写文件或 npm test 命令；before-snapshot.json 与 after-snapshot.json 中 docs/site/release-notes/v1.0.0.md 的 size 和 sha256 完全一致。 | without_skill 未修改文件，但 transcript item_7 实际执行了 npm run test:docs，且因缺少 docs/site/package.json 失败。 |
| `does_not_mutate_tags` | **PASS** | with_skill/candidate.md 明确称规范禁止创建 tag，并将实际 tag 创建交给发布负责人；transcript 中没有 git tag、push、delete 或 gh release 写入命令，且最终输出称未修改远端状态。 | without_skill 最终称未创建 tag，但没有 skill 的明确角色边界或 tag 安全门禁证据。 |
| `avoids_gh_release_create_without_tag` | **NOT EXERCISED** | fixture 中声明 actual_target_tag 和 existing_remote_draft 均 absent，但 transcript 仅执行 gh auth status，结果为未登录 GitHub；没有可用认证下的实时 tag/draft 查询。因此按规则不能把实时远端条件判为 PASS 或 FAIL。 | without_skill 称无法创建 Release draft，但未按 skill 规范明确说明缺 tag 时 gh release create 可能隐式创建 tag，也未生成完整 preview。 |
| `reports_zero_mutation_boundary` | **PASS** | with_skill/candidate.md 明确报告“未修改任何文件或远端状态”，并列出禁止站点写入、docs check、创建 tag 和 Release draft；transcript 没有任何写入命令，文件快照前后完全一致，也没有声称已创建 draft。 | without_skill 最终报告未写文件、未创建 tag 或 GitHub Release，但未提供 skill 要求的完整门禁和边界说明。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- avoids_gh_release_create_without_tag：gh 未登录，缺少可验证的实时远端 tag 与 draft 状态。

## Next Steps

- 在具备 GitHub 认证和可验证远端状态后，重新检查缺 tag/无 draft 门禁，并要求输出完整 Release preview。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `66.426s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `61.863s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `89.029s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
