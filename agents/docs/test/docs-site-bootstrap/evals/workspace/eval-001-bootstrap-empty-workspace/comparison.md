# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`

## Test Set / Fixture Version

- Fixture: `issue-122-assets-38-v1`
- Branch fixture commit: `a2a30a3`
- Execution cleanup: `docs/site`
- Fresh validation date: `2026-07-19`

## Latest Result

**PASS** — fresh judge 对 6 条 assertions 全部判定 PASS。上轮 PARTIAL 的唯一根因是 `_internal/INSTRUCTIONS.md` 完成报告协议缺少入口依据与无显式 opt-in 时的 pre-write stop；协议补全后，本轮 fresh with-skill 报告完整声明用户显式 opt-in、已确认宿主、固定 `docs/site/` 根，以及缺少显式 opt-in 时必须在任何文件写入前停止。

## With-Skill Behavior

- 6 条 assertions 全部 PASS，包括修复后的 `requires_explicit_opt_in`。
- 38/38 静态目标与 `assets/docs/site/` 逐字节一致；manifest 覆盖全部 38 个路径，磁盘共 39 个文件。
- `package.json` 只有一个 `new:doc` 命令，scaffold 实现和测试存在；五模板各含恰好一个 `docs-scaffold` 区块并全部由 `standards/index.md` 索引。
- 16 个 Markdown 页面满足七字段 frontmatter；重复执行前后 39 个文件 SHA-256 快照一致，`createdAt` 保持不变。
- 完成报告明确列出本次写入的三项入口依据，并声明缺少显式 opt-in 时在任何文件写入前停止。

## Without-Skill Baseline

- 来源：本次全新 Codex subagent，使用相同原始 prompt 与 cleanup 后空 fixture，新生成且未读取或应用 skill 文档、Agent README 或历史 baseline。
- baseline 自行创建 10 个受管文件，manifest 位于 `docs/site/bootstrap-manifest.json`，没有 38 项 packaged inventory、规定的 scaffold 测试、五模板 marker/index 体系或入口依据报告协议。
- baseline 能验证其自建文件的 read-back、重复执行幂等和简单 `new:doc` 拒绝覆盖，但不满足 docs-site-bootstrap 资产契约。

## Failures

- 无 assertion failure。独立 judge 在隔离宿主直接执行 scaffold 测试时因未安装 `gray-matter` 停在依赖解析；该 assertion 要求交付测试资产，文件存在且与权威资产逐字节一致，因此不影响 PASS。

## Next Steps

- 保留本结果；资产清单、脚手架契约、入口报告协议或 manifest 状态机变化时重新生成 fresh with/without validation。

## Runtime Artifact Policy

- 本次响应、生成站点副本、baseline 和独立 judge verdict 仅位于 `tmp/eval-runs/122-c3b-20260719/eval-001-bootstrap-empty-workspace/`，不提交到 git。
