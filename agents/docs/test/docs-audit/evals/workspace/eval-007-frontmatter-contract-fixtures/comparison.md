# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-007-frontmatter-contract-fixtures`

## Test Set / Fixture Version

- Fixture: `frontmatter-contract-v1`
- Branch fixture commit: `71bbb09`
- Contract: `agents/docs/skills/docs-agent/_internal/_shared/frontmatter-contract.md`

## Latest Result

**PASS** — fresh judge 对 7 条 assertions 全部判定 PASS。with-skill 将合法 API 页面送入事实层并判为 `verified`，将 `doc_type: standard`、空 `related_code`、缺少 `last_verified_version`、空 `owners` 四页分别按对应契约错误判为 `stale`，最终 release blocked 且不得局部盖章。

## With-Skill Behavior

- 明确使用 docs-agent 共享 frontmatter 契约真源逐页校验七个必填字段。
- 实际复现 `docs-site-bootstrap` 内嵌 validator，得到四类预期错误和合法页空错误列表，确认生成端与审计端结论一致。
- 合法页继续核对 `src/catalog/routes.txt`；完整影响域为 `1 verified / 4 stale`，release 不得 `proceed`，fixture 未被修改。

## Without-Skill Baseline

- 来源：本次第二轮 fresh `codex exec` 独立子进程，使用相同原始 prompt 与 fixture，新生成且未接触 skill 文档或 Agent README。
- baseline 也从显著的 fixture 信号得出 1 个合法页、4 个非法页和 release blocked。
- baseline 明确承认未读取共享契约或 bootstrap validator，无法证明审计端与生成端的同源闭环；with-skill 的主要增益是提供可复核的实现级一致性证据。

## Failures

- 最终轮无 assertion failure。
- 首轮 judge 因 with-skill workspace 未包含 assertion 明确依赖的 bootstrap 内嵌 validator，给出 `PARTIAL（6 PASS / 1 PARTIAL）`；随后用相同 prompt 和 fixture 重新生成完整 with-skill、without_skill 与 judge，补齐依赖材料后得到本次 PASS。首轮产物仅保留在 tmp，不参与 Latest Result。

## Next Steps

- 保留本结果；共享契约或 bootstrap validator 变化时同时重跑本 eval。

## Runtime Artifact Policy

- 最终轮运行期产物仅位于 `tmp/eval-runs/118/eval-007-frontmatter-contract-fixtures/`；首轮诊断产物位于同级 `eval-007-frontmatter-contract-fixtures-attempt1/`。二者均不提交到 git。
