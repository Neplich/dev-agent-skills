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

**Gate**: the title must match the `v{VERSION} - {主题概述}` shape. A title
missing the topic summary, a bare `v{VERSION}` tag, or a summary unrelated to
the confirmed facts is not a submit-ready preview: it must not be delivered for
maintainer approval, and no draft may be created or updated with it.

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
update. For this marketplace the three instruction subsections are all
mandatory; for other hosts only the subsections applicable to the confirmed
fact source are required.

1. **简述**：首段为固定结构，内容受已确认事实源约束。仅当事实源同时确认
   无新增 plugin、plugin 集合与当前 7 个 role plugin 一致、且无破坏性变更
   时（本仓库 marketplace 发版即此语境），以「无破坏性变更，也没有新增
   plugin。7 个 role plugin 均更新到 `v{VERSION}`。」开头；存在破坏性变更
   或事实源不完整支持该句时，按事实源如实改写（新增数量、plugin 集合按
   已确认 marketplace 事实推导），不得新增事实源之外的发布声明；随后按需
   追加「注意 N 项契约/输出变化」段落，写明生效范围与影响面。
2. **指令**：`### Claude Code`、`### Codex` 与 `### Kimi Code` 三个小节。
   仅当宿主是本 marketplace（dev-agent-skills）发版时，内容为以下固定模板
   （逐字使用，不随版本内容裁剪或增删）；其他宿主不适用这些安装命令，按
   已确认事实源给出对应的升级动作，或省略不适用的小节：

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

3. **收尾句**：收尾句必须存在。仅当事实源确认无新增 plugin 且 plugin
   集合与当前 7 个 role plugin 一致时，以「更新仓库后重新运行安装器，
   即可同步全部 7 个 role plugin 的 `v{VERSION}` 能力。」结束；其他宿主
   按事实源给出对应的升级动作收尾，不得写事实源之外的安装器或 plugin
   声明。

## Traceability Checks

For each linked item, verify that it belongs to the declared compare range and
supports a fact already present in the applicable confirmed fact source. Direct commits may
use a short SHA and author when no PR exists. Contributor attribution must come
from the included PR or commit evidence, not inference.
