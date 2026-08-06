# Skill Eval Comparison

## Evaluation Target

- Skill: `manual-gen`
- Eval: `eval-001-domain-provided`
- Target behavior: 用维护者提供的域名环境产出一批有限范围、以真实界面为证据的图文手册

## Test Set / Fixture Version

- Fixture version: `manual-gen-v0.1.3`（#235：被测平台改为执行前维护者确认注入）
- Environment: 测试平台由执行前维护者确认注入（平台名 + 平台本地代码路径）；本结论基于旧契约的 mermaid.live 占位
- Lane isolation: 两条 lane 的 prompt 逐字相同、可见 fixture 完全相同，唯一变量是是否加载
  `manual-gen/SKILL.md` 与 `_internal/INSTRUCTIONS.md`。prompt 为自然用户目标，
  不含协议步骤、分层结构、字段清单或工具参数。`eval_metadata.json`、`pm-handoff.md`
  与采集脚本均已移出 lane 可见目录（见 `AGENTS.md` → Eval prompt 与 lane 隔离契约）。
- Executed: `2026-08-05`，两条 lane 各自独立 `codex exec` 冷启动会话

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `PARTIAL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景

Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `PARTIAL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `uses_provided_domain_without_local_start` | PASS | FAIL | with_skill 的 `result.txt` 明确记录 `https://wiki.jototech.cn/` 及“来源为维护者交接包”，且未执行本地启动；without_skill 的结果未记录环境 URL 或维护者来源。 |
| `confirms_one_bounded_batch` | FAIL | FAIL | with_skill 仅记录角色、场景和排除项，未展示候选父子树、逐页证据、截图计划、change-map 与导航增量；without_skill 直接写入手册，也没有写入前确认记录。 |
| `records_viewport_set_and_readback` | NOT_EXERCISED | FAIL | with_skill 明确记录“视口设定 / 回读：未执行”；without_skill 的 SVG 实际尺寸为 `1200×760`，手册与报告均无 `1920×1080` 设定及运行时回读。 |
| `captures_sanitized_product_evidence` | NOT_EXERCISED | FAIL | with_skill 明确记录“采集截图清单：无”；without_skill 的 3 个截图是静态 SVG（`width="1200" height="760"`），无真实运行界面证据。 |
| `writes_evidence_bounded_manual` | FAIL | FAIL | with_skill 记录“未写入站点文件”，没有手册条目或资产；without_skill 的 `anonymous-edit-preview.md:13` 将 `last_verified_version` 写成 `live-interface-2026-08-06`，违反应保持 `unverified`。 |
| `checks_render_and_handoffs_audit` | FAIL | FAIL | with_skill 记录 `npm run test:docs` 在 `docs/site` 通过，但渲染验收未执行，且 handoff 仅写 `blocked`，未明确给出渲染命令及 `blocked docs-agent:docs-audit`；without_skill 只在结果中声称检查通过，未记录渲染验收、版本门禁或 blocked handoff，并生成了 Release Notes 之外的实际手册产物但未满足版本交接条件。 |

未满足断言（with/without 任一 FAIL）：``uses_provided_domain_without_local_start``、``confirms_one_bounded_batch``、``records_viewport_set_and_readback``、``captures_sanitized_product_evidence``、``writes_evidence_bounded_manual``、``checks_render_and_handoffs_audit``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 入口门禁通过，识别出请求已提供域名环境，**未进入本地启动分支、未重复询问域名**。
- 完成 Step 1–4：读宿主 standards 与 change-map、读 manual 模板、在真实界面梳理角色与流程、
  产出完整候选批次（三层页面树、3 张截图计划、索引与导航增量、change-map 原子 closure、显式排除项）。
- 停在 Step 4 候选确认门禁，**零页面写入、零截图落盘**。
- 额外识别出证据链缺口并如实报告：「由于当前宿主未包含 Mermaid Live 前端源码或映射示例，
  无法在不虚构 `related_code` 与映射字段的前提下给出可写入条目」。
- 预判 handoff 门禁：即使后续检查通过，无维护者确认的 `target_release_version` 时页面仍保持
  `unverified`，handoff 为等待发版上下文的 blocked。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：同一 prompt、同一 fixture 的独立冷启动会话，未加载 manual-gen 文档。
- 直接完成采集与写入：4 张截图 + 4 个 Markdown 页面，未提出候选批次也未请求确认。
- 契约违规：操作页 `doc_type: product`（手册页应为 `manual`）、
  `related_code: [https://mermaid.live/]`（应为仓库相对路径，此处填了外部 URL）、
  截图使用 `.jpg`（skill 规定 `step-<序号>-<slug>.png`）。
- 自行读取了 `standards/index.md` 并采用三层组织——该规则来自宿主交付物而非 skill 协议。

## Failures / Gaps
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 skill 行为回归。with_skill 在实际触发的 Step 1–4 路径上满足对应 assertions。
- 未触发：`records_viewport_set_and_readback`、`captures_sanitized_product_evidence`、
  `writes_evidence_bounded_manual`、`checks_render_and_handoffs_audit`（依赖 Step 5–8）。

## Next Steps

- issue #235：本测试集为外部站点，宿主内不存在其前端源码，FR-M12 的 `related_code`
  「非空且可定位」无法满足，正向写入路径在该测试集上走不完。
- 单轮 lane 与 Step 4 确认门禁存在结构性冲突：协议要求展示候选页面树与截图计划后再确认，
  而单轮会话无法提供第二轮确认。要覆盖 Step 5–8 需多轮 lane 或改用宿主内应用作测试集。
- issue #234：全仓 eval 的 prompt / fixture 泄漏普查与批量整改。

## Runtime Artifact Policy

运行期产物（截图、生成页面、lane 报告、transcript）写入隔离 scratch workspace，不入库。
本文件是唯一持久化结果。
