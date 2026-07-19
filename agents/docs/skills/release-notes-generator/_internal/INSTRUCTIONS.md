# Release Notes Generator — Internal Instructions

站内 Release Notes 的完整执行协议。入口、feature-scope、正文确认和角色边界
由 `../SKILL.md` 定义；只有入口与站点基础门禁全部通过后才加载本文件。

## 1. 读取宿主规范与相邻版本

1. 确认固定目标根为 `docs/site/release-notes/`，目标页面使用
   `docs/site/release-notes/vX.Y.Z.md`，其中版本必须来自已确认输入，不得从分支、
   commit、包版本或文件名猜测。
2. 读取 `docs/site/release-notes/README.md` 或宿主等效编写规范。
3. 读取目标版本前后最接近的站内版本页，提取宿主当前的标题、章节、链接、语气
   和索引习惯；相邻页面只提供格式参考，不能作为本次版本事实。
4. 读取宿主 frontmatter、`docs/site/.meta/releases.json`、Release Notes index、
   导航生成方式和 docs check 入口。宿主存在明确契约时按契约执行；不得臆造
   metadata schema 或新增导航机制。

如果 `docs/site/release-notes/`、编写规范或站点基础缺失，停止且零写入，返回
`docs-site-bootstrap` handoff。不得自行初始化站点或只补一部分 Release Notes
目录。

## 2. 基于可验证证据生成版本页

先建立带来源的证据清单，再生成正文。可用证据包括已确认的 release scope、
PRD/TRD/实施计划、实际代码和配置 diff、数据库迁移、测试结果、部署与环境配置、
镜像或静态资产清单、升级与回滚说明，以及版本化 changelog。对每项关键声明
保留可追溯的仓库路径、命令结果、issue、PR 或其他明确来源。

当证据存在时，正文必须覆盖：

- 用户可见功能变化；
- 内部架构与关键实现变化；
- 数据库、数据结构或迁移；
- 部署、配置和环境变化；
- 镜像、静态资源或其他交付资产；
- 升级步骤、兼容性、回滚注意事项与已知风险。

不得为了简洁丢失研发、测试、运维和交付需要的关键事实。没有证据的类别不填充
猜测内容；应将证据缺口显式列为 unresolved，并在其影响版本事实或安全升级时
阻塞确认。正文描述已交付事实，不把计划、讨论过程或未实现范围写成当前状态。

## 3. 应用共享 Frontmatter 契约

读取并严格消费：

`agents/docs/skills/docs-agent/_internal/_shared/frontmatter-contract.md`

目标页面必须包含该契约的七个必填字段，并满足以下 Release Notes 约束：

- `title`：按宿主风格表达已确认目标版本；
- `visibility`：取宿主规范允许且适用的 `public`、`internal` 或 `both`；
- `doc_type: release`；
- `stage: release`，除非宿主明确要求在确认前使用其他合法阶段；
- `owners`：非空字符串数组，来源于已确认的宿主责任人；
- `related_code`：非空字符串数组，列出本次版本证据覆盖的仓库相对路径或 glob；
- `last_verified_version: unverified`。

`last_verified_version` 的统一版本盖章归 issue #117。即使目标版本已经确认，本
specialist 也不得把目标版本写入该字段以绕过审计时序。额外 frontmatter 字段
只能来自宿主现有契约。

## 4. 展示正文并等待确认

生成或更新候选 `vX.Y.Z.md` 后，向用户或维护者展示：

- 完整正文；
- 来源证据清单；
- unresolved 证据或风险；
- 确认后计划更新的 metadata、index 和必要导航路径。

等待明确确认。此时不得修改 `.meta/releases.json`、Release Notes index 或导航，
不得运行会自动改写这些文件的命令，也不得输出 ready handoff。若维护者要求修改
正文，应用修改后重新展示并重新等待确认。

## 5. 确认后更新 Metadata、Index 与必要导航

只有 `confirmation_status: confirmed` 后才执行：

1. 按宿主已有 schema 更新 `docs/site/.meta/releases.json`，保留未知字段、其他
   版本和人工内容；不重置 release metadata。
2. 按宿主编写规范更新 Release Notes index，确保目标版本链接、标题与页面一致，
   避免重复条目并保持宿主排序。
3. 仅在宿主导航不会自动生成且现有契约明确要求时更新必要导航。若 #122 形态的
   宿主由脚本生成导航，不手工维护 sidebar。
4. 回读页面、metadata、index 和实际修改的导航，验证目标版本一致、引用存在、
   既有内容未被覆盖。

这一步只维护站内发布文档事实，不创建 tag，不操作 GitHub Release，也不执行
部署或交付资产发布。

## 6. 执行宿主 Docs Checks

从宿主 `docs/site/package.json`、仓库脚本、贡献指南或 CI 读取权威命令，不自创
替代检查。记录每条命令、工作目录、退出状态和结果摘要。

- AI Hub-shaped 宿主必须在 `docs/site/` 对应工作目录执行与其 VitePress CI
  一致的 `npm run test:docs`。
- 宿主定义额外 required docs checks 时一并执行。
- 任一 required check 未执行、失败或结果不可验证时，handoff 必须 blocked。

检查失败时保留真实失败证据，不把部分通过描述为 ready，也不越界修改代码、
部署配置或其他角色文档来掩盖失败。

## 7. 输出 Issue #120 Ready Handoff

输出结构化 handoff，至少包含：

```yaml
handoff_target: "issue #120 / github-release-generator"
handoff_status: ready # 或 blocked
next_gate: "issue #117 pre-tag audit"
release_execution_authorized: false
release_version: "vX.Y.Z"
site_release_note_path: "docs/site/release-notes/vX.Y.Z.md"
confirmation_status: confirmed # 或 unconfirmed
docs_checks:
  - command: "npm run test:docs"
    cwd: "docs/site"
    result: passed # failed / not_run
updated_release_surfaces:
  release_metadata:
    - "docs/site/.meta/releases.json"
  indexes:
    - "<宿主实际 Release Notes index>"
  navigation:
    - "<仅列实际修改路径；无则为空数组>"
source_evidence:
  - source: "<仓库路径、命令结果、issue、PR 或其他来源>"
    supports: "<该来源支撑的版本事实>"
blockers: []
```

仅当 `confirmation_status: confirmed` 且所有宿主 required docs checks 均成功时，
`handoff_status` 才能是 `ready`。其他情况一律为 `blocked`，并准确列出未确认正文、
失败/未执行检查、版本不一致或证据缺口。

该 handoff 只证明站内 Release Notes 已确认且校验通过，是 #120 的必要输入，不是
GitHub Release 执行授权。应先把它交给 issue #117 执行 pre-tag audit；只有 #117
返回 `ready_for_tag` 后，#120 才可继续准备 GitHub Release 草稿。本 specialist 不
创建、编辑或发布 GitHub Release，不收集 GitHub Release 专用的 PR、贡献者或
compare 信息，不创建或移动 tag。issue #117 的 pre-tag/post-tag 审计与统一盖章
不能由本 handoff 代替。
