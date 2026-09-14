# 文档检查方法

## 确定范围

读取用户指定页面或比较范围。变更检查覆盖相关提交、工作区修改和新增页面，记录采用的基线；发布检查使用明确的目标版本和对应提交或标签。核对历史版本时读取实际 Git 对象。

利用 `related_code`、change-map、直接链接、路由与配置发现受影响页面，包括图片、导航和映射自身的变化。普通文档检查可以使用当前工作区的可核实内容。

## 格式与事实

按 [页面字段](../../docs-agent/_internal/_shared/frontmatter-contract.md) 核对站点 frontmatter。普通 Markdown 使用宿主格式。

逐项核对描述与其证据：产品行为对照实现、测试和界面；技术设计对照真实入口与数据流；API 对照 route、schema 和 contract tests；数据库对照 migration、模型与查询；运维对照配置、运行结果和恢复路径。手册同时核对步骤、截图、角色和导航。

将发现写成具体问题、位置、影响和证据。已授权修复直接修改并复查。历史版本锚和 `unverified` 提示需要复核的范围，事实是否准确由内容证据决定。

## 工具检查

使用宿主实际命令。内置站点在 `docs/site/` 提供：

```bash
npm run check:frontmatter
npm run check:affected -- --base <base-ref>
npm run check:version
npm run test:docs
npm run build:public
npm run build:internal
```

`test:docs` 检查页面字段、版本数据和脚本行为。`check:affected` 按需提供文档影响提示；显式 `--base` 固定比较基线。宿主可按自身需要选用 `--strict` 将映射检查设为 CI 条件，此模式使用可解析的提交基线。构建结果结合实际页面检查链接、图片、布局与可见性。

## 版本核对

`last_verified_version` 记录页面实际核对过的版本。有可靠版本锚且内容通过核对后可更新；其余保留 `unverified` 或已有真实锚。

内置 `.meta/releases.json` 包含 `latest`、`released`、`verifiedDocs`。`released` 是无重复版本数组，`latest` 为其最后一项，空数组对应 `null`；`verifiedDocs` 将页面映射到已列入 `released` 的版本。保留其他版本与扩展字段。

`check:version` 按显式 `--version`、`RELEASE_VERSION`、HEAD 的精确 tag 获取版本锚；锚可用时要求 `latest` 一致，锚不可用时检查 metadata 内部一致性。各来源按自身格式核对 SemVer，保留 prerelease 与 build 身份。

发布任务核对页面、metadata、实际标签指向、版本资产与最终检查证据。新修改后重做受影响验证。版本记录与 GitHub 发布按用户已有授权推进。

交付检查范围、修复结果、命令结果和真实剩余事项。独立报告只在审计交付或长期维护需要时保存。
