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
