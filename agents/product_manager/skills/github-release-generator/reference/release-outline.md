# GitHub Release Outline

The confirmed site Release Notes are the version fact source. Preserve their
functional, architecture, database, deployment, asset, upgrade, compatibility,
and risk facts. GitHub data may add traceability and repository-native format;
it must not add, omit, or rewrite release facts.

## GitHub Release Name

For this repository, use:

```text
v{VERSION} - {概括性简述}
```

The summary should reflect about three confirmed highlights and must not be
only the bare tag.

## Body

```markdown
# Release Notes - {THIS_TAG} ({YYYY-MM-DD})

{站内 Release Notes 已确认的版本主题。}

## 重点更新

### {已确认的重点}

{保持站内事实，按需补代表性 PR/commit 链接。}

## 其他改进

- {已确认的改进。}

## 升级说明

{保持站内升级、兼容性和风险事实。}

## 变更明细

- {conventional title} by @{author} in [#{number}]({PR_URL})

完整变更： {REPO_URL}/compare/{PREV_TAG}...{THIS_TAG}
```

## Conversion Rules

- Keep the site's release-note ordering.
- Preserve conventional prefixes from PR titles or commit subjects.
- Link major confirmed highlights to representative PRs or commits.
- Mention contributors using the repository's existing style.
- Put the complete compare link after the curated detail section.
- Do not paste the full PR or commit feed as the user-facing narrative.
- Do not add a product claim that is absent from the confirmed site page.
- Keep internal quality evidence, including skill eval results, assertion counts,
  review rounds, and QA evidence summaries, only in the repository changelog's
  Skill Eval summary. Do not include it in the user-facing GitHub Release body,
  and do not let adjacent Release presentation habits introduce sections beyond
  this outline's four sections: 重点更新, 其他改进, 升级说明, and 变更明细.
- If GitHub evidence contradicts or materially extends the page, block and
  return it to Docs for renewed confirmation instead of editing around it.

## Traceability Checks

For each linked item, verify that it belongs to the declared compare range and
supports a fact already present in the site Release Notes. Direct commits may
use a short SHA and author when no PR exists. Contributor attribution must come
from the included PR or commit evidence, not inference.
