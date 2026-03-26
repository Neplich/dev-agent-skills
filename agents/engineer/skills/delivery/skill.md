---
name: delivery
description: "Manage Git branches, commits, and PRs for delivering completed work. Use this skill when code is ready to be committed, a PR needs to be created, or changes need to be pushed. Trigger on phrases like '提交代码', '创建 PR', '提 PR', 'commit', 'create pull request', 'push changes', 'deliver', or after feature-implementor and test-writer complete their work."
---

# Delivery

Manage the Git workflow for delivering completed code: branch creation, meaningful commits, PR creation with proper references, and CI status verification.

## When to Use

- Code and tests are complete, ready to commit
- User asks to create a PR
- User asks to commit or push changes
- After `feature-implementor` + `test-writer` + optional `debugger` complete

## Step 1 — Assess current Git state

```bash
git status
git branch --show-current
git log --oneline -5
```

Determine:
- Are we on main/master or a feature branch?
- Are there unstaged changes?
- Are there already commits for this feature?

## Step 2 — Create feature branch (if needed)

If currently on main/master, create a branch:

```bash
git checkout -b <branch-name>
```

### Branch naming

Check if the project has a convention:

```bash
git branch -r | head -20
```

Follow existing patterns. Common conventions:
- `feature/<description>` or `feat/<description>`
- `fix/<description>`
- `<username>/<description>`

If no convention detected, use: `feat/<short-description>`

Use lowercase, hyphens for spaces. Keep it short and descriptive.

## Step 3 — Stage and commit

### Determine commit strategy

Check if the project uses Conventional Commits:

```bash
git log --oneline -20
```

Look for `feat:`, `fix:`, `chore:` prefixes.

### Stage files

Stage only the files related to this feature. Never use `git add -A` or `git add .` blindly.

```bash
git add <specific-files>
```

Review what's staged:

```bash
git diff --staged --stat
```

### Commit

If small feature (1-5 files changed): single commit.
If larger feature: group by logical unit (data model, business logic, API routes, tests).

```bash
git commit -m "<type>: <description>"
```

Commit message rules:
- Use Conventional Commits format if the project uses it
- First line under 72 characters
- Reference the PM doc or Issue if applicable: `feat: add notification endpoints (per TRD §3.4)`
- Don't include file lists in the message — that's what `git diff` is for

## Step 4 — Push to remote

```bash
git push -u origin <branch-name>
```

If the push fails due to auth, tell the user to check their GitHub authentication (`gh auth status`).

## Step 5 — Create PR

```bash
gh pr create --title "<title>" --body "$(cat <<'EOF'
## Summary

<1-3 bullet points describing the change>

## PM Documents

- PRD: <reference if applicable>
- TRD: <reference if applicable>
- Related Issue: <#number if applicable>

## Changes

<brief description of what was added/modified>

## Testing

- [ ] Unit tests pass
- [ ] Integration tests pass (if applicable)
- [ ] Manual testing done (if applicable)

## Checklist

- [ ] Code follows project conventions
- [ ] Self-review completed
- [ ] Tests cover P0 acceptance criteria
EOF
)"
```

### PR title

- Under 72 characters
- Use conventional format if the project does: `feat: add notification system`
- Clear and descriptive

### Link to Issues

If there's a related GitHub Issue:

```bash
gh pr create --title "..." --body "..."
```

Add `Closes #<number>` or `Relates to #<number>` in the body.

## Step 6 — Verify CI

After PR is created, check CI status:

```bash
gh pr checks <pr-number> --watch
```

If CI fails:
- Read the failure logs: `gh pr checks <pr-number> --json name,state,description`
- If it's a lint/test failure from our code: fix it, commit, push
- If it's a CI infrastructure issue: report to user

## Step 7 — Summary

```text
## 交付完成

- **分支**: <branch-name>
- **PR**: <PR URL>
- **提交数**: <N>
- **CI 状态**: ✅ 通过 / ⏳ 运行中 / ❌ 失败

### PR 内容
- <brief summary of changes>
```

## Edge Cases

- **No remote**: If `git remote -v` shows nothing, ask the user to add a remote first.
- **Branch already exists**: Ask to use existing branch or create a new one.
- **Merge conflicts with main**: Report the conflict and ask the user how to resolve (rebase, merge, or manual).
- **Large number of changes**: If > 20 files changed, suggest splitting into multiple PRs if the changes can be logically separated.
- **Draft PR**: If the user says the work isn't complete, use `gh pr create --draft`.
- **No CI configured**: Note the absence and suggest adding CI with `project-bootstrap`.
