# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`
- Scenario: AI Hub-shaped formal-docs release chain through gated GitHub Release handoff
- Review context: issue #150

## Test Set / Fixture Version

- Fixture version: `issue-150 fresh-paired group-b v1`（SHA-1 pinned synthetic Git fixture）
- Actual validation date: `2026-07-21`
- Fresh run: `tmp/eval-runs/issue-150/group-b/eval-005-integration-release-chain/`
- with-skill 与 without-skill 从同一 pristine fixture 独立复制；两者均在各自隔离 workspace 运行 `.eval/setup-git-fixture.sh`。

## Latest Result

**PASS（with-skill 8/8；fresh without-skill 8/8）** — with-skill 从共享 frontmatter、宿主模板、API/change-map 与 confirmed site Release Notes handoff，完整核验 pre-tag `ready_for_tag`、post-tag `release_verified` 与三门禁 GitHub Release handoff；所有结论来自真实 synthetic Git objects，且宿主/远端 tag 与 GitHub Release 零写入。fresh baseline 也完成相同 object-level protocol 并通过 8/8，因此本用例证明 fixture fidelity 与链路可执行性，但未显示相对 uplift。

## Assertions

- `validates_shared_frontmatter_contract`: PASS。全站正式 Markdown（排除 `.meta/**`）按七字段与 enum 核验；五模板分别使用 api/database/design/ops/product，只做 frontmatter 与结构检查。
- `uses_host_templates_and_scaffold`: PASS。核对五个宿主模板、`scripts/scaffold-doc.mjs`、`npm run new:doc` 与 package scripts 为唯一模板基础；未内嵌第二套模板。
- `reconciles_api_sync_and_change_map`: PASS。路由显式定义 `GET /api/search`、handler 与 `SearchItem`；`npm run test:api` 退出 0，覆盖注册、200/400、上下 clamp、fractional/NaN/Infinity 与空白 q；change-map 精确覆盖页面。
- `accepts_confirmed_site_release_notes_handoff`: PASS。handoff 含维护者确认 v1.4.0、confirmed 正文、页面/index/metadata、成功 docs checks、版本来源 inventory 与 evidence；站内 owner 和 GitHub Release owner 分离。
- `completes_pre_tag_ready_for_tag`: PASS。隔离 setup 解析 immutable base/target/anchor/handoff objects；pre-tag 两次 staged gate、committed delta gate、三页单字段 stamp、ordinary blobs、source binding、discovery/lineage self-check、release branch expected-old-value CAS 与 readback 全通过，结果 `ready_for_tag`。
- `completes_post_tag_release_verified`: PASS。lightweight tag tuple 两次一致；tag tree 与 trusted handoff tree 绑定；raw-form/SemVer、inventory/lineage/source binding、expected-head、单路径 staged/committed gate、evidence branch CAS/readback 通过。成功记录 Decision evidence 早于 Conclusion；blocked 模板只含 `blocked`。
- `hands_off_three_gates_to_github_release`: PASS。handoff 指向 `pm-agent:github-release-generator`，明确 confirmed site Release Notes、`ready_for_tag`、`release_verified` 三门禁，以及仍需维护者独立当前批准。
- `preserves_no_mutation_boundaries`: PASS。除隔离 setup 内的 synthetic local refs/tag，未创建、移动或删除宿主/远端 tag，未创建、修改或发布真实 GitHub Release；记录 tag/GitHub writes 为 0。

## With-Skill Behavior

- 完整读取 Docs router、shared frontmatter、formal/release/audit specialist contracts 与 PM safety-net/consumption contract，再执行对应边界。
- Synthetic object evidence：base `f655919e...`、target `e3ebc01f...`、anchor `50455ebe...`、handoff/tag commit `77866e0c...`、post-tag evidence commit `8822ef43...`；candidate/handoff/post-tag records 均为 `100644 blob`。
- `npm ci --ignore-scripts` 后，`RELEASE_VERSION=v1.4.0 npm run test:docs` 退出 0、74/74 tests；`npm run test:api` 退出 0。
- caller 固定在 pristine target，临时 worktree/ref 已清理；runtime evidence 仅作为索引，关键结论均由 `rev-parse`、`cat-file`、`diff`、`show`、`ls-tree` 独立复核。

## Fresh Without-Skill Baseline

- 来源：相同 prompt/assertions 与独立 pristine fixture 的 fresh `without_skill`；生成期间未读取目标 SKILL、Docs README、internal/shared 指令、旧 comparison、历史 baseline 或 with-skill 输出。
- baseline 运行同一 setup，独立读取相同 Git objects，验证 frontmatter/template/API/site handoff、pre/post gates、三门禁 handoff 与零 mutation；`test:api` 和 74/74 docs tests 均通过。
- 结果：8/8 PASS；未复用历史 baseline。

## Failures

- With-skill assertion failures: none。
- Without-skill assertion failures: none。
- Setup/API/docs command failures: none。一次首次 baseline harness 尝试把日志重定向到 runtime workspace，导致 setup 后日志文件出现在 status；该 attempt 被保留为 `without_skill-attempt1` 运行期诊断，随后从 pristine fixture 新建正式 baseline，并把日志置于 workspace 外，正式证据 caller 仅出现 setup 预期的 `.eval/runtime-git-evidence.md`。
- Non-blocking dependency diagnostic: fixture lockfile 安装报告 2 moderate 与 1 high audit findings；不属于 assertions，未改依赖。
- Comparative limitation: fixture setup 自身实现并 self-check 绝大多数协议，且 prompt/assertions 明确要求 object reads 与 handoff 字段，因此 baseline 同样通过。

## Next Steps

- 保持 durable `PASS`，作为 object-level release-chain fidelity 与 protocol executability 回归。
- 如需测 skill uplift，另增 setup 不提供成功结果、tag tuple 漂移、expected-head 并发移动或站内 handoff 缺字段的阻塞型集成用例。

## Runtime Artifact Policy

- Synthetic Git repositories、node_modules、candidate/response、日志、runtime evidence 和首次诊断 attempt 仅位于 `tmp/eval-runs/issue-150/group-b/eval-005-integration-release-chain/`，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
