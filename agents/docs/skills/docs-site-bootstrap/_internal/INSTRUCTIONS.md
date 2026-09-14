# 文档站安装与更新

内置静态资产位于 `assets/docs/site/`，目标根为 `docs/site/`。按下方映射复制文件，并根据本次结果生成 `.meta/bootstrap-manifest.json`。页面和脚本共同使用 [页面字段](../../docs-agent/_internal/_shared/frontmatter-contract.md)。

## 文件与 manifest

盘点完整资产和宿主目标，读取已有 manifest，然后按实际差异处理：

| 情况 | 处理与记录 |
| --- | --- |
| 目标缺失 | 复制资产，记录 `created` |
| 字节一致 | 复用文件，记录 `skipped-identical` |
| 需要保留的宿主内容 | 保持当前内容，记录 `kept-as-is` |
| 可在授权范围内合并的差异 | 保留宿主事实并应用更新，记录 `kept-as-is` |

用户已有内容、填充的 change-map 和 release metadata 保持完整。独立改动存在实质冲突时展示具体差异和取舍。解析失败的 manifest 先检查实际文件和原记录，在可验证基础上修复。

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

`files` 使用稳定排序的目标路径。相同资产重复运行保留有效 disposition 和 `createdAt`，达到 zero-diff；`kept-as-is` 表示保留宿主内容。新增文件逐字节从内置资产复制，合并文件核对最终差异。

## 资源和构建

public/internal 共用资源可放入 `docs/site/public/`；页面专用资源放在引用页附近，并由页面直接引用。生成树根据可见页面与资源规则构建，内部资料放在相应内部页面范围内。

依照 package-lock.json 安装依赖，执行 `npm run test:docs` 和受影响构建。确认页面、资源、导航、manifest 与重复运行行为。交付最终站点和必要运行说明，清理临时检查产物。

## 资产索引

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
| `assets/docs/site/.vitepress/navigation.public.json` | `docs/site/.vitepress/navigation.public.json` |
| `assets/docs/site/.vitepress/navigation.internal.json` | `docs/site/.vitepress/navigation.internal.json` |
| `assets/docs/site/.vitepress/theme/index.ts` | `docs/site/.vitepress/theme/index.ts` |
| `assets/docs/site/.vitepress/theme/Mermaid.vue` | `docs/site/.vitepress/theme/Mermaid.vue` |
| `assets/docs/site/.vitepress/theme/custom.css` | `docs/site/.vitepress/theme/custom.css` |
| `assets/docs/site/index.public.md` | `docs/site/index.public.md` |
| `assets/docs/site/index.internal.md` | `docs/site/index.internal.md` |
| `assets/docs/site/api/index.md` | `docs/site/api/index.md` |
| `assets/docs/site/database/index.md` | `docs/site/database/index.md` |
| `assets/docs/site/design/index.md` | `docs/site/design/index.md` |
| `assets/docs/site/product/index.md` | `docs/site/product/index.md` |
| `assets/docs/site/manual/index.md` | `docs/site/manual/index.md` |
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
| `assets/docs/site/standards/templates/manual-guide.md` | `docs/site/standards/templates/manual-guide.md` |
| `assets/docs/site/standards/change-map.yaml` | `docs/site/standards/change-map.yaml` |
| `assets/docs/site/.meta/releases.json` | `docs/site/.meta/releases.json` |
运行时 manifest 根据实际安装结果生成。
