# 文档站页面字段

内置 VitePress 站点和校验脚本使用以下页面契约。宿主已经交付的脚本决定实际支持能力。

| 字段 | 类型与取值 | 含义 |
| --- | --- | --- |
| `title` | 非空字符串 | 页面标题 |
| `visibility` | `public`、`internal`、`both` | 构建目标可见性 |
| `doc_type` | `landing`、`release`、`design`、`api`、`database`、`ops`、`product`、`manual` | 页面类别 |
| `stage` | `draft`、`dev`、`ops`、`release` | 内容阶段 |
| `owners` | 非空字符串数组 | 维护团队或人员 |
| `related_code` | 非空字符串数组 | 代码与测试证据路径 |
| `last_verified_version` | 非空字符串 | 已核对版本或 `unverified` |

七个字段均由脚本校验。可选 `nav_order` 为 0 至 9007199254740991 的安全整数；在同一 sidebar section 内按数值升序排序，未设定的页面随后按路径 slug 排序。section 顺序由 `SECTION_ORDER` 决定。写入前查看宿主 `scripts/lib/sidebar.mjs` 的实际支持情况；已有宿主资产可按更新任务升级。

标准说明页面使用 `doc_type: design`；模板页面使用其目标类型。模板的占位内容用于生成页面，事实检查针对生成后的正文。`standards/change-map.yaml` 的描述性头部采用相同命名，结构由 change-map 工具检查。

`last_verified_version` 表示内容核对依据。有可验证版本时记录该版本，其余使用 `unverified`。页面核对可在写作、同步或审阅中完成。`layout` 等附加字段按宿主使用方式保留。

手册页面位于 `docs/site/manual/`。页面与资源的可见性应匹配，公共构建可访问其引用内容。
