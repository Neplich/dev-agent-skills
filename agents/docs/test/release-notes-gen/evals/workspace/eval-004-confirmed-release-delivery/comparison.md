# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator` → `release-notes-gen`（改名后新入口待重跑验证）
- Eval: `eval-004-confirmed-release-delivery`
- Scenario: 维护者已确认目标版本与完整正文后的站内 Release Notes 成功交付
- Review context: PR #187 follow-up for issue #177

## Test Set / Fixture Version

- Fixture version: `confirmed release delivery v1`
- Validation time: `2026-07-29 01:33:08 CST`
- Runtime: `tmp/eval-runs/issue-177/rng-eval-004/`
- 两条 candidate 使用同一 prompt 与独立 pristine fixture；with-skill 只额外读取
  Docs Agent 与目标 skill 协议，without-skill 未读取或应用 skill、Agent README、
  eval metadata、assertions、comparison、with-skill 输出或历史 lane。
- 独立 judge 读取 assertions、源 fixture 与两条当前 lane 产物逐条判定；候选运行时
  不可见 assertions。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（5/5 assertions exercised）
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

- With-skill: **5/5 PASS**
- Fresh without-skill: **2/5 PASS、3/5 FAIL**
- Relative uplift: **+3 assertions / +60 percentage points**

## Assertion Results

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `delivers_confirmed_release_page` | PASS | FAIL | 两侧均覆盖六类证据；with-skill 保持 `last_verified_version: unverified`，baseline 提前写入 `v1.0.0`。 |
| `updates_derived_surfaces_after_confirmation` | PASS | FAIL | with-skill 按新到旧更新 index，追加 metadata 且保留旧版本、旧 `verifiedDocs` 与 `manualNote`；baseline 提前登记 verifiedDocs、盖章 index，且索引顺序错误。 |
| `passes_host_docs_checks` | PASS | PASS | 两侧均在 `docs/site` 执行锁定依赖安装及权威 `npm run test:docs`，最终 75/75 tests、退出码 0。 |
| `returns_complete_ready_handoff` | PASS | FAIL | with-skill 输出完整 `docs-agent:docs-audit / pre-tag` ready handoff；baseline 缺少明确 handoff/downstream target、next gate、更新面、blockers 与 `release_execution_authorized: false`。 |
| `preserves_external_release_boundary` | PASS | FAIL | 两侧均未执行外部发布操作；baseline 仍越权完成页面、index 和 `verifiedDocs` 盖章。 |

## With-Skill Behavior

- 生成 `docs/site/release-notes/v1.0.0.md`，完整保留用户功能、架构、数据库、
  部署配置、交付资产、升级兼容与风险六类证据。
- 页面应用合法 release frontmatter，审计前保持
  `last_verified_version: unverified`。
- 确认记录成立后更新 Release Notes index 与 release metadata，不手工修改自动
  生成导航，不覆盖既有版本、verifiedDocs 或宿主自有字段。
- 最终 `npm run test:docs` 通过：75/75 tests，退出码 0。
- 输出字段完整的 pre-tag ready handoff，并明确
  `downstream_target: pm-agent:github-release-gen` 与
  `release_execution_authorized: false`。
- 未执行 GitHub Release、tag、部署、镜像操作、Git 写入或 docs-audit 盖章。
- Response SHA-256:
  `39f842d0317c1fdce8182598600a5ae2811691236a5d1600a5e1286f2c5878b0`。

## Fresh Without-Skill Baseline

- baseline 能生成六类证据正文、更新 index/metadata，并真实通过宿主 docs checks。
- baseline 把页面和 index 的 `last_verified_version` 提前写成 `v1.0.0`，同时把
  新页面加入 `verifiedDocs`，越过 docs-audit 盖章时序。
- baseline 的 index 未保持宿主要求的新到旧排序；handoff 虽表达 ready_for_audit，
  但缺少完整目标、授权边界、更新面与 blockers 字段。
- Response SHA-256:
  `d049d1f7a8d878c4f26acb4044d621e34f369ad0ffe2c5acae8b0b249a0f38d7`。

## Failures And Limitations

- With-skill assertion failures: none.
- Infrastructure or credential blockers: none.
- Baseline failures: 审计前盖章、派生面排序/verifiedDocs 错误、pre-tag handoff
  字段与授权边界不完整。
- 当前 fixture 在候选启动前已保存维护者对完整正文事实类别的确认，因此能验证
  确认后的正确 delta，但“确认前派生面零变化”依赖源 fixture 初态与最终差异作
  间接判定；交互式确认时序继续由既有 confirmation-gate eval 覆盖。
- lane 的读取隔离依据 run log 和产物边界，不是操作系统级 file-access audit。

## Next Steps

- 保留本用例作为成功交付路径回归，继续由 eval-001/002/003 覆盖入口版本确认、
  正文确认和站点 foundation 门禁。
- 每次运行从只读源 fixture 重建 lane workspace，不原地复用已修改的 index 或
  release metadata。

## Runtime Artifact Policy

- 当前 lane 的 workspace、依赖、生成站点、response、handoff、run log、judge
  verdict 与作废轮次只保留在 `tmp/eval-runs/issue-177/rng-eval-004/`，不提交。
- 只提交 eval 定义、fixture、metadata 与本 durable `comparison.md`。
