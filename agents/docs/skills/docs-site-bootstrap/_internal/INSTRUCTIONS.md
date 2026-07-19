# Docs Site Bootstrap — Internal Instructions

`docs-site-bootstrap` 的详细执行协议。公开入口、显式 opt-in、幂等与冲突
gate 由 `../SKILL.md` 定义；只有这些 gate 全部通过后才加载本文件。

所有静态宿主输出以 `../assets/docs/site/**` 为唯一来源，并按相同相对路径
逐字节复制到宿主 `docs/site/**`。正式 Markdown 页面与 frontmatter 校验脚本
消费 `agents/docs/skills/docs-agent/_internal/_shared/frontmatter-contract.md`。
`standards/change-map.yaml` 的描述性头部沿用共享字段命名与
`doc_type: design`，但不是 `check:frontmatter` 目标；其结构和元数据校验归
issue #122 的 change-map 工具链。

## 1. 入口与固定根目录

- 仅在 `../SKILL.md` 的入口凭据与权威 opt-in gate 通过后执行。
- 宿主生成根固定为 `docs/site/`，不得静默适配到其他目录。
- 已确认范围必须包含完整 scaffold 和运行时生成的
  `docs/site/.meta/bootstrap-manifest.json`。
- Bootstrap 始终处理完整 inventory；后续文档编写的渐进加载不允许缩减
  Bootstrap 输出。

## 2. 完整 Inventory

静态 inventory 是下方资产索引中的 40 个文件。另加一个仅运行时目标：

- `docs/site/.meta/bootstrap-manifest.json`

inventory 覆盖 npm 项目、七个入口脚本及其最小 helper、脚手架测试与 fixture、
共享/public/internal VitePress 配置、主题与 Mermaid 渲染、两个首页、七个
section 首页、三页 standards、五类内容模板、Release Notes 编写规范、
空 change map 和 release metadata。

静态资产遵循以下发布规则：

- 同时用于 public/internal 的资源放在 `docs/site/public/`，完整复制到两套
  生成树；动态或间接路径引用的资源也应放在这里。
- 其他资源仅在已包含页面直接引用时复制；internal-only 资源不得放进
  `docs/site/public/`，可与引用它的 internal 页面同目录。
- 不把 `standards/change-map.yaml`、`.meta/**`、未显式接线的
  `.vitepress/**`、`node_modules/**` 或 `.generated/**` 复制进生成树。

## 3. 冲突分类与 `kept-as-is`

写入前先建立完整 inventory，并为每个静态目标按对应资产字节分类：

| 分类 | 行为与 manifest 状态 |
| --- | --- |
| 目标不存在 | 从资产逐字节创建，记录 `created`。 |
| 目标与资产字节相同 | 不重写，记录 `skipped-identical`。 |
| 已有有效 `kept-as-is` | 不做资产等价检查，继续记录 `kept-as-is`。 |
| 其他差异 | 加入完整冲突列表，未经授权不得覆盖。 |

已有有效 `created` 或 `skipped-identical` 记录且目标仍与资产相同时，保留原
disposition，避免重复运行改写 manifest。发现冲突时一次报告全部路径，并为
每个路径提供 overwrite、明确 merge 或保留现有文件三种选择：

- overwrite 只在用户明确授权后执行；
- merge 必须先给出具体合并内容并获得批准；
- 保留现有文件时记录 `kept-as-is`，没有隐式 keep；
- `kept-as-is` 只表示该精确路径以后跳过资产等价检查，不授权覆盖或归一化。

未解决冲突不得伪造成成功 manifest 状态。已确认 bootstrap 范围内不存在
冲突的新文件可以创建，但不得在冲突解决前部分覆盖任何差异文件。

## 4. Manifest 协议

先加载或在内存中建立 manifest，再写任何 scaffold 文件。已有 manifest 必须
解析并保留有效的 `kept-as-is`；无效 manifest 本身是冲突，在解决前阻塞写入。
首次运行先在内存准备 manifest，并把 `.meta/` 作为第一次文件系统变更。

manifest 形状如下；`createdAt` 只在首次创建时写入，zero-change 重跑不更新：

```json
{
  "schemaVersion": "1.0",
  "generatedRoot": "docs/site",
  "createdAt": "<ISO-8601 timestamp>",
  "files": {
    "docs/site/package.json": "created"
  }
}
```

`files` 的路径按字典序稳定排序，值只能是 `created`、
`skipped-identical` 或 `kept-as-is`。这些值记录持久化 bootstrap disposition，
不是执行次数。

## 5. 写入顺序

1. 从下方索引构建 40 个静态目标，加上运行时 manifest，形成完整 inventory。
2. 读取或在内存建立 manifest；解析失败时停止。
3. 对全部静态目标完成 missing / identical / kept-as-is / conflict 分类。
4. 汇总全部冲突并取得逐项决定；未授权的差异文件不得写入。
5. 首次运行创建 `docs/site/.meta/`。
6. 对获准创建或覆盖的静态目标，按下方资产索引顺序从对应资产文件逐字节
   复制；`release-notes/README.md` 必须在 `release-notes/index.md` 之前写入。
   明确 merge 仅写入已批准内容。不得从其他仓库获取 scaffold 文件。
7. 确定性写入 manifest，路径按字典序排列。
8. 回读每个已写静态目标并与资产或已批准 merge 结果逐字节核对；回读并解析
   manifest，核对所有记录的路径与状态。
9. 从磁盘重新分类完整 inventory，确认同一资产与用户决定下再次执行为
   zero-diff。

不得重置已经填充的 `standards/change-map.yaml`、`.meta/releases.json` 或正式
文档页面；除非已有明确 `kept-as-is`，差异仍按冲突处理。

## 6. 资产索引

以下映射均执行逐字节复制；左侧为本 skill 资产，右侧为宿主目标。

| 资产路径 | 宿主目标 |
| --- | --- |
| `assets/docs/site/package-lock.json` | `docs/site/package-lock.json` |
| `assets/docs/site/package.json` | `docs/site/package.json` |
| `assets/docs/site/scripts/lib/paths.mjs` | `docs/site/scripts/lib/paths.mjs` |
| `assets/docs/site/scripts/lib/pages.mjs` | `docs/site/scripts/lib/pages.mjs` |
| `assets/docs/site/scripts/lib/frontmatter.mjs` | `docs/site/scripts/lib/frontmatter.mjs` |
| `assets/docs/site/scripts/lib/sidebar.mjs` | `docs/site/scripts/lib/sidebar.mjs` |
| `assets/docs/site/scripts/check-frontmatter.mjs` | `docs/site/scripts/check-frontmatter.mjs` |
| `assets/docs/site/scripts/check-affected.mjs` | `docs/site/scripts/check-affected.mjs` |
| `assets/docs/site/scripts/check-version.mjs` | `docs/site/scripts/check-version.mjs` |
| `assets/docs/site/scripts/prepare-nav.mjs` | `docs/site/scripts/prepare-nav.mjs` |
| `assets/docs/site/scripts/prepare-site.mjs` | `docs/site/scripts/prepare-site.mjs` |
| `assets/docs/site/scripts/dev-site.mjs` | `docs/site/scripts/dev-site.mjs` |
| `assets/docs/site/scripts/scaffold-doc.mjs` | `docs/site/scripts/scaffold-doc.mjs` |
| `assets/docs/site/scripts/__tests__/scaffold-doc.test.mjs` | `docs/site/scripts/__tests__/scaffold-doc.test.mjs` |
| `assets/docs/site/scripts/__tests__/fixtures/change-map.yaml` | `docs/site/scripts/__tests__/fixtures/change-map.yaml` |
| `assets/docs/site/.vitepress/config.shared.ts` | `docs/site/.vitepress/config.shared.ts` |
| `assets/docs/site/.vitepress/config.public.ts` | `docs/site/.vitepress/config.public.ts` |
| `assets/docs/site/.vitepress/config.internal.ts` | `docs/site/.vitepress/config.internal.ts` |
| `assets/docs/site/.vitepress/theme/index.ts` | `docs/site/.vitepress/theme/index.ts` |
| `assets/docs/site/.vitepress/theme/MermaidRenderer.vue` | `docs/site/.vitepress/theme/MermaidRenderer.vue` |
| `assets/docs/site/.vitepress/theme/custom.css` | `docs/site/.vitepress/theme/custom.css` |
| `assets/docs/site/index.public.md` | `docs/site/index.public.md` |
| `assets/docs/site/index.internal.md` | `docs/site/index.internal.md` |
| `assets/docs/site/api/index.md` | `docs/site/api/index.md` |
| `assets/docs/site/database/index.md` | `docs/site/database/index.md` |
| `assets/docs/site/design/index.md` | `docs/site/design/index.md` |
| `assets/docs/site/product/index.md` | `docs/site/product/index.md` |
| `assets/docs/site/ops/index.md` | `docs/site/ops/index.md` |
| `assets/docs/site/release-notes/README.md` | `docs/site/release-notes/README.md` |
| `assets/docs/site/release-notes/index.md` | `docs/site/release-notes/index.md` |
| `assets/docs/site/standards/index.md` | `docs/site/standards/index.md` |
| `assets/docs/site/standards/doc-lifecycle.md` | `docs/site/standards/doc-lifecycle.md` |
| `assets/docs/site/standards/doc-granularity.md` | `docs/site/standards/doc-granularity.md` |
| `assets/docs/site/standards/templates/api-template.md` | `docs/site/standards/templates/api-template.md` |
| `assets/docs/site/standards/templates/database.md` | `docs/site/standards/templates/database.md` |
| `assets/docs/site/standards/templates/feature-design.md` | `docs/site/standards/templates/feature-design.md` |
| `assets/docs/site/standards/templates/ops-runbook.md` | `docs/site/standards/templates/ops-runbook.md` |
| `assets/docs/site/standards/templates/product-handbook.md` | `docs/site/standards/templates/product-handbook.md` |
| `assets/docs/site/standards/change-map.yaml` | `docs/site/standards/change-map.yaml` |
| `assets/docs/site/.meta/releases.json` | `docs/site/.meta/releases.json` |

`docs/site/.meta/bootstrap-manifest.json` 没有对应资产，必须按本次运行结果动态生成。

## 7. 回读、Zero-Diff 与完成报告

回读失败、静态目标字节不一致、manifest 解析失败或记录缺失均阻塞完成。完成后
分别报告：

- 本次写入的入口依据：用户显式 opt-in、已确认的宿主仓库与固定 `docs/site/` 根；若缺少显式 opt-in，必须在任何文件写入前停止；
- created 与 skipped-identical 路径；
- kept-as-is 路径及授权该决定的用户选择；
- unresolved conflicts 与可选解决方式；
- manifest 路径及回读结果；
- 第二次完整分类是否 zero-diff。

存在 manifest 错误、未授权冲突、写入失败或回读不一致时，不得宣称 Bootstrap
完成。
