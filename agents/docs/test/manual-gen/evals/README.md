# manual-gen Eval 执行说明

## 被测平台注入（issue #235）

manual-gen 的 eval **不写死测试平台**。每轮执行前必须先向维护者确认被测平台的三项事实：

1. **平台名**：手册的平台层定位与 `related_code` 映射依据。
2. **可访问 URL**：可直接导航的线上界面。按 skill 环境门禁，只有具备确认域名的环境才视为「已提供环境」，因此 URL 为必填；缺 URL 时 lane 只能进入本地启动协商或阻塞分支。
3. **平台在本地代码中的路径（pwd）**：平台代码副本成为 lane 宿主仓库后，`related_code` 才能填可定位的仓库相对路径（满足 FR-M12 的非空可定位要求）。

### 执行步骤

1. 询问维护者被测平台的平台名、可访问 URL、本地代码 pwd，确认值作为本轮「已提供环境」的事实。
2. 在隔离 scratch workspace（`tmp/eval-runs/manual-gen/...`）物化本轮宿主仓库：复制平台本地代码仓库（含前端源码），把 eval workspace 的 `docs/site/` 文档站 fixture 与 `pm-handoff.md` 嵌入该副本，使副本成为 lane 的宿主仓库（`host_repository` 指向该副本）；将确认值写入副本 `pm-handoff.md` 的 `source_documents` 与 `eval_metadata.json` 的 `environment`。
3. 从两条 lane 可见目录物理排除评测文件：`eval_metadata.json`、`comparison.md`、`README.md`；已提交的 `pm-handoff.md` 不含协议步骤或门禁术语，直接使用。prompt 中的平台声明与副本一致，两条 lane 逐字相同。
4. 若维护者确认的平台仅有可访问界面、宿主仓库内无本地代码（如外部站点场景），写入路径（Step 5–8）无法走完：如实记录 Coverage `PARTIAL` 与未覆盖断言，不虚构 `related_code`。拒绝虚构证据并停在写入前的阻塞语义是 skill 的差异化行为，照常断言。

### 各 eval 场景

- eval-001：匿名基础编辑与预览流程（写入路径完整覆盖依赖平台本地代码可定位）。
- eval-002：无域名环境时须明确询问本地启动授权，同意前零启动、零写入。
- eval-003：无环境且拒绝本地启动时阻塞，零写入、不虚构界面证据。
- eval-004：匿名导出与分享流程，分享链接中的环境编码标识不进入手册正文。
- eval-005：平台 / 业务 / 操作三层手册语义，导航与证据均来自真实界面。
