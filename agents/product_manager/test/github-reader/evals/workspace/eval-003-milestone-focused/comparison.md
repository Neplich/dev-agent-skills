# Eval Result: eval-003-milestone-focused

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-003-milestone-focused`
- Test case: `milestone-focused`
- Prompt:

> 看一下 facebook/react 最近的 milestone，哪个进度最慢或者已经逾期了？

- Expected output:

> Milestone 状态报告，识别出进度最慢或逾期的 milestone，给出具体数据支撑

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`（0 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
- Overall result: FAIL
- With-skill summary: with_skill 实际加载了 github-reader（skill_load_hits=2），按顺序读取技能后尝试查询仓库和 milestone，但 GitHub CLI 未认证且网络请求失败，最终如实报告无法判断；输出未使用状态 emoji。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载了 github-reader（skill_load_hits=2），按顺序读取技能后尝试查询仓库和 milestone，但 GitHub CLI 未认证且网络请求失败，最终如实报告无法判断；输出未使用状态 emoji。

## Without-Skill Baseline

without_skill 未加载技能（skill_load_hits=0），通过网页搜索输出了 19.0.0、54%（6/11）等结论，并同样未使用状态 emoji。仅作对照，不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `assertion_1` | **NOT EXERCISED** | with_skill transcript 中 gh repo view 与 milestones 查询因未登录失败，随后 curl 因无法解析 api.github.com 失败；candidate 明确写明“目前无法可靠判断”，因此实时 milestone 实体不可用，不能判定该断言。 | without_skill 明确指出 19.0.0 是进度最慢/停滞目标，但该对照行为不改变 with_skill 结论。 |
| `assertion_2` | **NOT EXERCISED** | 所需实时 milestone 数据不可用；with_skill candidate 没有提供 open/closed 数量或完成率，而是如实说明无法获取数据，因此该实时数据断言不能判 PASS 或 FAIL。 | without_skill 输出 54%（6/11）和 5 个 open issue。 |
| `assertion_3` | **FAIL** | with_skill candidate 只说明 CLI 未登录和无法判断，没有使用要求的 ✅、🟢、🟡、🔴、⚪ 任一状态 emoji；技能加载成功且不是基础设施缺口。 | without_skill candidate 同样没有使用要求的状态 emoji。 |

## Failures

- assertion_3 未满足：最终输出缺少要求的 emoji 状态标识。

## Not Exercised

- assertion_1：GitHub CLI 未认证、API 网络不可用，无法获得实时 milestone 集合。
- assertion_2：GitHub CLI 未认证、API 网络不可用，无法获得实时完成率数据。

## Next Steps

- 认证 GitHub CLI 或提供可用的实时 GitHub 数据后，重新评估 milestone 识别和完成率断言。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `62.459s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `57.834s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `76.421s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
