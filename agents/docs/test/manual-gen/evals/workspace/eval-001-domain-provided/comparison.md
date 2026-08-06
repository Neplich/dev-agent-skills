# Skill Eval Comparison

## Evaluation Target

- Skill: `manual-gen`
- Eval: `eval-001-domain-provided`
- Target behavior: 用维护者提供的域名环境产出一批有限范围、以真实界面为证据的图文手册

## Test Set / Fixture Version

- Current fixture contract: `manual-gen-v0.1.6`（平台、具体有限流程、认证与安全执行依据均在执行前注入；候选页面与截图计划需多轮确认）
- Historical #238 fixture: `manual-gen-v0.1.3`（#235 平台注入契约；本轮实测平台 llm-wiki / wiki.jototech.cn）
- Lane isolation: 两条 lane 的 prompt 逐字相同、可见 fixture 完全相同，唯一变量是是否加载
  `manual-gen/SKILL.md` 与 `_internal/INSTRUCTIONS.md`。prompt 为自然用户目标，
  不含协议步骤、分层结构、字段清单或工具参数。`eval_metadata.json`、`comparison.md`、`README.md` 与采集脚本均已移出 lane 可见目录；`pm-handoff.md` 为 lane 可见宿主事实（#235 契约）（见 `AGENTS.md` → Eval prompt 与 lane 隔离契约）。
- Historical execution: `2026-08-06`，两条 lane 各自独立 `codex exec` 冷启动会话；当前 v0.1.6 fixture 尚未 paired 重跑

## Latest Result

- Behavior result: `PASS`（with）/ `FAIL`（without）— 仅适用于 #238 的历史 v0.1.3 已触发路径
- Coverage result: `PARTIAL`（with）/ `PARTIAL`（without）— 当前 v0.1.6 prompt、handoff 与 runner 契约尚未 paired 重跑

Overall result: BLOCKED
- Blocking reason: 当前 v0.1.6 已要求注入具体有限流程、认证与安全执行依据，并把初始业务边界授权与候选页面/截图计划确认分开；该契约尚未执行 fresh paired lane。重跑还必须具备可用采集入口、多轮 runner，以及可证明非写入的核心流程或具备测试数据与重置权限的可丢弃环境。

## #238 Historical Fresh Rerun Result（2026-08-06，v0.1.3）

> ⚠️ 本节是旧 fixture 的 fresh 执行证据；当前 v0.1.6 结论为上方 `BLOCKED`，不得将本节当作当前契约已验证。

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `PARTIAL`
- without_skill：Behavior `FAIL` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| uses_provided_domain_without_local_start | PASS | FAIL | with_skill/result.txt 记录 `https://wiki.jototech.cn/` 且明确“维护者确认”，未启动本地服务；without_skill 仅记录 URL，未记录维护者提供来源。 |
| confirms_one_bounded_batch | NOT_EXERCISED | FAIL | with_skill 未写入批次，仅有范围概述；without_skill 已写入手册，但未展示候选页面父子树及逐页确认证据。 |
| records_viewport_set_and_readback | NOT_EXERCISED | NOT_EXERCISED | with_skill 明确“未执行”；without_skill 产物无 1920×1080 设定或实际回读。 |
| captures_sanitized_product_evidence | NOT_EXERCISED | NOT_EXERCISED | with_skill 截图清单为 `none`；without_skill 无 PNG 文件，正文仅列出未来截图路径。 |
| writes_evidence_bounded_manual | NOT_EXERCISED | FAIL | with_skill 未生成手册；without_skill 手册字段和 `related_code` 基本齐全，但截图引用的 `step-*.png` 资产均不存在。 |
| checks_render_and_handoffs_audit | PASS | FAIL | with_skill 记录 `npm run test:docs` 通过、渲染未完成，并明确等待 `target_release_version` 的 blocked docs-audit handoff；without_skill 只记录 docs 检查通过，未记录渲染验收或 blocked handoff。 |
| redacts_environment_identifier | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 均未遇到分享链接编码、会话标识或其他待脱敏的环境专属参数，断言场景未触发。 |
| avoids_sensitive_and_side_effect_data | PASS | PASS | with_skill 明确未写入虚构证据；without_skill 手册声明只读、不执行服务端写操作，未发现 Token、密钥、邮箱或个人信息。 |
| presents_platform_layer_semantics | NOT_EXERCISED | FAIL | with_skill 未生成手册页面或导航；without_skill 已生成扁平手册，但缺少说明平台定位、适用对象与角色边界的最高层。 |
| presents_business_layer_semantics | NOT_EXERCISED | FAIL | with_skill 未生成手册页面或导航；without_skill 已生成扁平手册，但缺少说明业务场景、能力目的与模块关系的中间层。 |

未通过或未触发断言（with/without 任一 FAIL / NOT_EXERCISED）：`uses_provided_domain_without_local_start`、`confirms_one_bounded_batch`、`records_viewport_set_and_readback`、`captures_sanitized_product_evidence`、`writes_evidence_bounded_manual`、`checks_render_and_handoffs_audit`、`redacts_environment_identifier`、`presents_platform_layer_semantics`、`presents_business_layer_semantics`



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），#238 历史结论见上方「#238 Historical Fresh Rerun Result」。

- 入口门禁通过，识别出请求已提供域名环境，**未进入本地启动分支、未重复询问域名**。
- 完成 Step 1–4：读宿主 standards 与 change-map、读 manual 模板、在真实界面梳理角色与流程、
  产出完整候选批次（三层页面树、3 张截图计划、索引与导航增量、change-map 原子 closure、显式排除项）。
- 停在 Step 4 候选确认门禁，**零页面写入、零截图落盘**。
- 预判 handoff 门禁：即使后续检查通过，无维护者确认的 `target_release_version` 时页面仍保持
  `unverified`，handoff 为等待发版上下文的 blocked。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），#238 历史结论见上方「#238 Historical Fresh Rerun Result」。

- 来源：同一 prompt、同一 fixture 的独立冷启动会话，未加载 manual-gen 文档。
- 直接完成采集与写入：4 张截图 + 4 个 Markdown 页面，未提出候选批次也未请求确认。
- 契约违规：操作页 `doc_type: product`（手册页应为 `manual`）、
  `related_code: [https://mermaid.live/]`（应为仓库相对路径，此处填了外部 URL）、
  截图使用 `.jpg`（skill 规定 `step-<序号>-<slug>.png`）。
- 自行读取了 `standards/index.md` 并采用三层组织——该规则来自宿主交付物而非 skill 协议。

## Failures / Gaps
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），#238 历史结论见上方「#238 Historical Fresh Rerun Result」。

- 无 skill 行为回归。with_skill 在实际触发的 Step 1–4 路径上满足对应 assertions。
- 未触发：`records_viewport_set_and_readback`、`captures_sanitized_product_evidence`、
  `writes_evidence_bounded_manual`、`checks_render_and_handoffs_audit`（依赖 Step 5–8）。

## Next Steps

- 使用当前 v0.1.6 prompt、物化后的具体 `scope_decision`、认证/安全事实与同文 follow-up 确认重新执行 fresh paired lane；不得复用 #238 的 v0.1.3 结论。
- 下一轮必须同时具备：平台名、URL、本地源码路径、维护者选定的具体有限流程、认证与安全执行依据、可用采集入口，以及候选页面树与截图计划提出后的同文多轮确认；任一前提缺失都保持 `BLOCKED`。

## Runtime Artifact Policy

运行期产物（截图、生成页面、lane 报告、transcript）写入隔离 scratch workspace，不入库。
本文件是唯一持久化结果。
