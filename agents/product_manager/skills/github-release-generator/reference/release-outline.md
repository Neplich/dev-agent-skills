# GitHub Release Outline

Use the fact source selected by the `SKILL.md` applicability gate: confirmed
site Release Notes for a site-enabled host, or the maintainer-confirmed fallback
fact source for a site-less host. Preserve its functional, architecture,
database, deployment, asset, upgrade, compatibility, and risk facts. GitHub
data may add traceability and repository-native format; it must not add, omit,
or rewrite release facts.

## GitHub Release Name

For this repository, use:

```text
v{VERSION} - {主题概述}
```

The summary should reflect about three confirmed highlights and must not be
only the bare tag.

**Gate**: for this marketplace the title must match the
`v{VERSION} - {主题概述}` shape. For any other host, follow the host's
confirmed release-naming convention; no additional format gate applies. In
either case a title that is only a bare version string is not a submit-ready
preview: it must not be delivered for maintainer approval, and no draft may
be created or updated with it.

## Body

```markdown
# Release Notes - {THIS_TAG} ({YYYY-MM-DD})

{适用版本事实源已确认的版本主题。}

## 重点更新

### {已确认的重点}

{保持已确认事实，按需补代表性 PR/commit 链接。}

## 其他改进

- {已确认的改进。}

## 升级说明

{按下方 "Upgrade Note Template" 的固定结构完整呈现，保留已确认的升级、兼容性和风险事实。}

## 变更明细

- {conventional title} by @{author} in [#{number}]({PR_URL})

完整变更： {REPO_URL}/compare/{PREV_TAG}...{THIS_TAG}
```

## Conversion Rules

- Preserve the applicable confirmed version facts and their logical relationships; this outline determines the section order of the user-facing body.
- Preserve risk qualifiers when summarizing confirmed facts. In particular, do
  not describe a migration as reversible or rollback-safe when the confirmed
  notes state that rollback deletes data or requires a backup.
- Preserve conventional prefixes from PR titles or commit subjects.
- Link major confirmed highlights to representative PRs or commits.
- Mention contributors using the repository's existing style.
- Put the complete compare link after the curated detail section.
- Do not paste the full PR or commit feed as the user-facing narrative.
- Do not add a product claim that is absent from the applicable confirmed fact source.
- Keep internal quality evidence, including skill eval results, assertion counts,
  review rounds, and QA evidence summaries, only in the repository changelog's
  Skill Eval summary. Do not include it in the user-facing GitHub Release body,
  and do not let adjacent Release presentation habits introduce sections beyond
  this outline's four sections: 重点更新, 其他改进, 升级说明, and 变更明细.
- If GitHub evidence contradicts or materially extends the fact source, block.
  Return site Release Notes to Docs, or a site-less fallback source to the
  maintainer, for renewed confirmation instead of editing around it.

## Upgrade Note Template

The `## 升级说明` section is mandatory and must follow this fixed structure.
A placeholder sentence, or a missing instruction subsection that applies to
the host, is not a submit-ready upgrade note and blocks draft creation or
update. For this marketplace, every instruction subsection whose target tag
is verified to support it, and the closing sentence, are mandatory; for other
hosts the upgrade note follows the confirmed fact source without invented
client-installation subsections or shell commands.

1. **简述**：首段为固定结构，内容受已确认事实源约束。仅当事实源同时确认
   无新增 plugin、plugin 集合与目标版本 `.claude-plugin/marketplace.json`
   注册的 role plugins 一致（当前形态为 7 个）、且无破坏性变更时（本仓库
   marketplace 发版即此语境），以「无破坏性变更，也没有新增 plugin。N 个
   role plugin 均更新到 `v{VERSION}`。」开头（N 按目标版本 manifest 推导，
   当前为 7）；存在破坏性变更或事实源不完整支持该句时，按事实源如实改写
   （新增数量、plugin 集合按已确认 marketplace 事实推导），不得新增事实源
   之外的发布声明；随后按需追加「注意 N 项契约/输出变化」段落，写明生效
   范围与影响面。
2. **指令**：`### Claude Code`、`### Codex` 与 `### Kimi Code` 三个小节。
   仅当宿主是本 marketplace（dev-agent-skills）发版时使用；指令列表与数量
   以目标版本 `.claude-plugin/marketplace.json` 注册的 role plugins 为准
   （下方 7 行是当前形态，逐字使用，不随版本内容裁剪或增删；manifest
   变化时按 manifest 推导列表）。Claude Code 小节仅适用于本 marketplace
   当前发布（`/plugin update` 无版本 pin，无法固定历史版本）；为历史 tag
   重跑正文时省略该小节并说明平台限制。Codex 指令仅在目标 release 的 tag
   包含 `TARGET_TAG` 安装支持时使用，Kimi 指令仅在目标 release 的 tag 包含
   `.kimi-plugin/plugin.json` 时使用；历史或能力不完整的 tag 按目标 tag
   实际内容给出升级方式或省略该小节。其他宿主不适用这些安装命令，按
   已确认事实源给出对应的升级动作，不生成空壳小节：

   ```text
   /plugin marketplace update dev-agent-skills
   /plugin update pm-agent@dev-agent-skills
   /plugin update designer-agent@dev-agent-skills
   /plugin update engineer-agent@dev-agent-skills
   /plugin update qa-agent@dev-agent-skills
   /plugin update devops-agent@dev-agent-skills
   /plugin update security-agent@dev-agent-skills
   /plugin update docs-agent@dev-agent-skills
   /reload-plugins
   ```

   ```text
   Fetch and follow instructions from https://raw.githubusercontent.com/Neplich/dev-agent-skills/refs/tags/v{VERSION}/.codex/INSTALL.md, setting TARGET_TAG=v{VERSION} so the clone or update stays pinned to this release
   ```

   ```text
   /plugins install https://github.com/Neplich/dev-agent-skills/releases/tag/v{VERSION}
   ```

3. **收尾句**：本 marketplace 宿主的收尾句必须存在。仅当事实源确认无
   新增 plugin 且 plugin 集合与目标版本 manifest 一致时，以「更新仓库后
   重新运行安装器，即可同步全部 N 个 role plugin 的 `v{VERSION}` 能力。」
   结束（N 按 manifest 推导，当前为 7）；其他宿主按事实源给出对应的升级
   动作收尾或省略，不得写事实源之外的安装器或 plugin 声明。

## Traceability Checks

For each linked item, verify that it belongs to the declared compare range and
supports a fact already present in the applicable confirmed fact source. Direct commits may
use a short SHA and author when no PR exists. Contributor attribution must come
from the included PR or commit evidence, not inference.
