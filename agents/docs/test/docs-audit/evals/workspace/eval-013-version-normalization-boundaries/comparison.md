# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-013-version-normalization-boundaries`
- Validation time: `2026-07-20 00:23:28 CST`
- Target behavior: pre-tag/post-tag 的严格 SemVer 来源形态、完整 identity、canonical version-source inventory digest 与 actual-tag pending 边界。

## Test Set / Fixture Version

- Fixture version: current working-tree fixture / 2026-07-20
- Fixture source: `evals.json` 中 eval-013 的 prompt/assertions、`eval_metadata.json` 与 `.eval/version-cases.md`。
- Assertions: 5
- Inventory sources: 7（`index`、`marketplace`、`notes`、`package`、`releases`、`tag`、`target`）。
- Fresh pair: 本会话先在不读取或应用 `docs-audit` skill、内部指令、Docs Agent README 与旧 comparison 的条件下生成 baseline；随后读取完整 skill 指令，并针对同一份 pristine fixture 重新生成 with-skill 结果。

## Latest Result

**PASS — fresh with-skill 5 / 5 assertions passed.** 候选只对要求前缀的来源移除恰好一个小写 `v`，严格保留 `rc.1` 与 `Build.7`，并按大小写敏感的完整 SemVer identity 比较。`V`、`vv`、缺 `v`、unprefixed source 带 `v`、缺失 prerelease/build、大小写差异、缺失或非法来源全部 `blocked`。

Fresh without-skill baseline 同为 **5 / 5**。两次评审都按 `source_id` 排序 7 个 exact 六字段对象，并以 RFC 8259 UTF-8、对象键排序、compact JSON、无 trailing newline 重算 1333 字节 canonical input；结果均为 `sha256:e511aca5591ef721dbe1095876fe9b718e7434a83a48e14de1e0f845124cced6`，与 fixture 一致。pre-tag 保留 `tag` 来源的完整六字段 locator contract，并记录 `pre_tag_value: pending_expected_absent`；post-tag 消费同一 inventory 后再填入实际 tag raw value，不把 pending 状态加入六字段 digest input。

## Assertion Results

| Assertion | With skill | Without skill | Evidence summary |
| --- | --- | --- | --- |
| `preserves_prerelease_and_build_identity` | PASS | PASS | 两者均把带前缀和无前缀合法值规范化为完整 `1.2.0-rc.1+Build.7`，保留 prerelease/build，并拒绝用忽略 build metadata 的 precedence 比较代替 identity equality。 |
| `enforces_source_specific_prefix_forms` | PASS | PASS | 两者均要求 target/tag/Release Notes/index/releases.json 恰有一个小写 `v`，拒绝 `V`、`vv` 和缺 `v`；marketplace/package 必须无 `v`，不做静默修正。 |
| `compares_semver_components_case_sensitively` | PASS | PASS | 两者均判定 `rc.1 != RC.1`、`Build.7 != build.7`，并把缺失 prerelease 或 build component 视为 pre-tag/post-tag blocker。 |
| `reports_all_missing_or_invalid_sources` | PASS | PASS | 两者均遍历完整 source inventory，一次报告缺失 Release Notes index、空 releases.json value、缺失 marketplace version 与非法 package loose version，不在首错停止，也不从有效来源补值。 |
| `persists_and_reuses_exact_inventory` | PASS | PASS | 两者均重算 exact 六字段 canonical inventory digest 为 `sha256:e511aca5591ef721dbe1095876fe9b718e7434a83a48e14de1e0f845124cced6`；pre-tag 持久化 7 个来源并将 actual tag 标为 `pending_expected_absent`，post-tag 消费同一 inventory，从 peeled tag tree/tag ref 复核并再次重算。缺 selector、多匹配、unknown extractor 或 digest 不等均 blocked。 |

## With-Skill Behavior

- 来源：本会话 fresh with-skill 评审；读取当前 `docs-audit` SKILL、完整内部协议、Docs Agent README、eval 定义和 pristine fixture。
- 结果：5 / 5。skill 明确定义来源专属 raw form、严格 SemVer identity、六字段 digest input、actual-tag pre-tag pending 状态及 pre-tag producer / post-tag consumer 对称契约。
- Digest 核验：按 `source_id` 排序 exact 六字段数组后生成 1333 字节 canonical JSON，无 trailing newline；SHA-256 为 `e511aca5591ef721dbe1095876fe9b718e7434a83a48e14de1e0f845124cced6`，与 fixture 声明完全一致。
- 裁定：合法 pair 归一到完整 identity；fixture 中每个独立 invalid case 均单独报告为 blocker。任何来源缺失、raw form 非法、identity 不等或 inventory digest 不等时，pre-tag 不得 `ready_for_tag`，post-tag 不得 `release_verified`。

## Without-Skill Fresh Baseline

- 来源：本会话全新 baseline；只读取 eval prompt/assertions、`eval_metadata.json` 和 version-cases fixture，未读取或应用 skill、Docs Agent README、历史 baseline或旧 comparison。
- 结果：5 / 5。baseline 能按测试输入中的明确清单执行严格 parse、全量 blocker 汇总、exact digest 重算、actual-tag pending 记录及 producer/consumer inventory 复用。
- Digest 核验：同一 7-source、1333-byte canonical input 重算为 `sha256:e511aca5591ef721dbe1095876fe9b718e7434a83a48e14de1e0f845124cced6`。
- 对比结论：skill 把这些要求固化为可复用协议，但测试输入已直接暴露完整答案边界，未产生额外 assertion 得分。

## Failures and Limitations

- With-skill 无失败；without-skill 无 assertion 失败；inventory 声明摘要与两次独立重算均一致，因此未触发 mismatch FAIL。
- fixture 为合成 version case 清单，没有真实 tag peel、Git object read 或 release surface 文件树。
- baseline 5 / 5 表明本例区分度不足；当前结果验证 skill 遵守协议，不证明未使用 skill 时通常会遗漏这些边界。

## Next Steps

- 后续如增强 eval 区分度，可把 source inventory 分散到真实 fixture 文件并减少 assertion 对规范化算法的直接提示，再用 Git harness 验证 peeled tag tree、raw form、mode/type/blob/hash 与 inventory digest。

## Runtime Artifact Policy

- 本轮未创建 transcript、candidate output、subagent verdict、timing、diagnostics、with-skill/without-skill 目录或其他 runtime artifact。
- Durable 结果仅为本 `comparison.md`；未复用历史 baseline。
