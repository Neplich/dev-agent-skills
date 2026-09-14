# GitHub 发布方法

## 目标与证据

确认仓库、目标标签、前一标签、目标提交和要执行的操作。将 ref 解析到具体提交，核对标签范围、正文和资产。读取站内文档、changelog、PR 或提交证据即可准备内容。

```bash
gh repo view --json nameWithOwner,url,defaultBranchRef
gh release list --json tagName,publishedAt,name,isDraft --order desc --limit 20
gh release view {THIS_TAG} --json tagName,name,body,isDraft,isPrerelease,publishedAt,targetCommitish,url
gh api repos/{OWNER}/{REPO}/compare/{PREV_TAG}...{TARGET_REF}
git ls-remote --tags origin refs/tags/{THIS_TAG}
```

写入前核对现有状态与当前授权。正文通过文件传入，保留真实换行。预览内容包括标题、正文、标签范围、prerelease/latest 选择和关键资产。

## 版本与 latest

按真实标签约定处理一个 `v` 前缀，使用严格 SemVer 比较并保留 prerelease/build 身份。预发布使用 `--prerelease` 与 `--latest=false`。稳定版本使用 `--prerelease=false`；目标稳定版明确高于当前 latest 时可使用 `--latest`，其余保持已有 latest。用户明确指定的 latest 策略作为操作依据。

草稿写入使用 prerelease 标志；latest 标志用于正式发布。每次实质写入前重新读取目标 Release、latest 和标签对象，核对并发变化。发现变化时根据当前事实重新判断，涉及新的实质取舍时再询问用户。

## 草稿与发布

现有草稿读取后选择更新或复用。目标 tag 已存在时，创建草稿使用 `--verify-tag` 明确绑定现有标签：

```bash
gh release create {THIS_TAG} --draft --verify-tag --title "{TITLE}" --notes-file {NOTES_FILE} {PRERELEASE_FLAG}
gh release edit {THIS_TAG} --title "{TITLE}" --notes-file {NOTES_FILE} {PRERELEASE_FLAG}
```

缺少 tag 时，按仓库发布方法和用户授权创建正确标签，随后核对指向。用户仅要求文案预览时交付预览即可。

发布前核对内容、标签、资产和相关检查结果，按已授权操作执行：

```bash
gh release edit {THIS_TAG} --draft=false {PRERELEASE_FLAG} {LATEST_FLAG}
```

回读目标 Release、latest、标签对象与资产，确认标题、正文、isDraft、isPrerelease、publishedAt、URL 和发布目标一致。已经符合目标状态时报告核实结果。命令或回读失败时先读取当前状态，区分已完成、部分完成与待修复事项，再在授权范围内继续。

已发布 Release 的内容修正与重新发布均按用户实际请求执行。标签移动、删除和额外外部变更使用其对应授权。
