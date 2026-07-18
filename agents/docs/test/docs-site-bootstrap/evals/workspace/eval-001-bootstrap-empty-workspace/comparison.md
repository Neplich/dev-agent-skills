# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Branch fixture commit: `71bbb09`
- Execution cleanup: `docs/site`

## Latest Result

**PASS** — fresh judge 对 5 条 assertions 全部判定 PASS。with-skill 在显式 opt-in 后生成 35 个嵌入模板目标和 `.meta/bootstrap-manifest.json`；磁盘实际为 35 个静态文件加 manifest，16 个 Markdown 页面全部满足七字段 frontmatter，第二次分类为 35 项 identical、0 missing、0 conflict、无需写入。

## With-Skill Behavior

- 严格把生成范围限制在 `docs/site/`，manifest 覆盖全部 35 个静态目标且路径有序。
- 所有正式 Markdown 页面均使用合法枚举、非空 `owners` / `related_code` 和必填 `last_verified_version: unverified`。
- 回读 manifest 成功；独立字节比较确认 35 个目标与嵌入模板一致，重复执行保留 `createdAt` 并产生 zero-diff。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，使用相同原始 prompt 与 cleanup 后的空 fixture，新生成且未接触 skill 文档或 Agent README。
- baseline 自行创建 7 个框架无关文件，manifest 位于错误的 `docs/site/bootstrap-manifest.json`，没有生成规定的 35 项清单。
- 其 6 个 Markdown 中有 2 个无 frontmatter，其余使用另一套四字段 metadata，不满足七字段契约；仅目录边界和通用幂等性成立。

## Failures

- 无 assertion failure。运行中用于 read-back 的 Ruby 辅助检查遇到旧版本 API与字符串编码差异，改用兼容 Hash 统计和 byte-array 比较后完成验证；模板产物未因此重写或降级。

## Next Steps

- 保留本结果；模板清单、manifest 或 frontmatter 生成规则变化时重跑此 eval。

## Runtime Artifact Policy

- 本次 transcripts、生成站点副本和 judge verdict 仅位于 `tmp/eval-runs/118/eval-001-bootstrap-empty-workspace/`，不提交到 git。
