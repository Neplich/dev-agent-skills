# Skill Eval Comparison

## Evaluation Target

- Skill: `manual-gen`
- Eval: `eval-001-domain-provided`
- Target behavior: 用维护者提供的域名环境产出一批有限范围、以真实界面为证据的图文手册

## Test Set / Fixture Version

- Fixture version: `manual-gen-v0.1.2`
- Environment: `https://mermaid.live/`，匿名访问，域名由请求直接提供
- Lane isolation: 两条 lane 的 prompt 逐字相同、可见 fixture 完全相同，唯一变量是是否加载
  `manual-gen/SKILL.md` 与 `_internal/INSTRUCTIONS.md`。prompt 为自然用户目标，
  不含协议步骤、分层结构、字段清单或工具参数。`eval_metadata.json`、`pm-handoff.md`
  与采集脚本均已移出 lane 可见目录（见 `AGENTS.md` → Eval prompt 与 lane 隔离契约）。
- Executed: `2026-08-05`，两条 lane 各自独立 `codex exec` 冷启动会话

## Latest Result

- Behavior result: `PASS` — with_skill 在本轮实际触发的路径上满足对应 assertions，无回归。
- Coverage result: `PARTIAL` — 见下方未触发断言

Overall result: PASS (partial coverage)

## With-Skill Behavior

- 入口门禁通过，识别出请求已提供域名环境，**未进入本地启动分支、未重复询问域名**。
- 完成 Step 1–4：读宿主 standards 与 change-map、读 manual 模板、在真实界面梳理角色与流程、
  产出完整候选批次（三层页面树、3 张截图计划、索引与导航增量、change-map 原子 closure、显式排除项）。
- 停在 Step 4 候选确认门禁，**零页面写入、零截图落盘**。
- 额外识别出证据链缺口并如实报告：「由于当前宿主未包含 Mermaid Live 前端源码或映射示例，
  无法在不虚构 `related_code` 与映射字段的前提下给出可写入条目」。
- 预判 handoff 门禁：即使后续检查通过，无维护者确认的 `target_release_version` 时页面仍保持
  `unverified`，handoff 为等待发版上下文的 blocked。

## Without-Skill Baseline

- 来源：同一 prompt、同一 fixture 的独立冷启动会话，未加载 manual-gen 文档。
- 直接完成采集与写入：4 张截图 + 4 个 Markdown 页面，未提出候选批次也未请求确认。
- 契约违规：操作页 `doc_type: product`（手册页应为 `manual`）、
  `related_code: [https://mermaid.live/]`（应为仓库相对路径，此处填了外部 URL）、
  截图使用 `.jpg`（skill 规定 `step-<序号>-<slug>.png`）。
- 自行读取了 `standards/index.md` 并采用三层组织——该规则来自宿主交付物而非 skill 协议。

## Failures / Gaps

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
