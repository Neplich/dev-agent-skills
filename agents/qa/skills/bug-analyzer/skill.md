---
name: bug-analyzer
description: "Analyze test failures and generate detailed bug reports. Automatically detects project type and creates either Markdown files or GitHub Issues. Use when tests fail or unexpected behavior is discovered."
---

# Bug Analyzer

Analyze test failures and generate detailed bug reports with reproduction steps, screenshots, logs, and environment information.

## When to Use

- After test failures in exploratory-tester or spec-based-tester
- When unexpected behavior is discovered during manual testing
- To document bugs before Engineer fixes them

## Step 1 — Collect failure information

Gather all available information about the failure:

```bash
# If from test output, capture the failure details
# Expected: test name, error message, stack trace
```

Required information:
- Test name or scenario
- Error message
- Stack trace (if available)
- Timestamp

## Step 2 — Capture screenshots and logs

If the bug involves UI:

```bash
# Screenshots should be saved during test execution
# Check for: screenshots/*.png in test output directory
```

Collect:
- Screenshot of failure state
- Browser console logs
- Network request logs
- Application logs (if accessible)

## Step 3 — Determine severity

Analyze impact and assign severity:

- **Critical**: Application crash, data loss, security vulnerability
- **High**: Major feature broken, blocking user workflow
- **Medium**: Feature partially broken, workaround exists
- **Low**: Minor issue, cosmetic problem

## Step 4 — Generate reproduction steps

Create clear, numbered steps to reproduce:

1. Start from a known state (e.g., "Open homepage")
2. List each action (click, input, navigate)
3. Include specific data used
4. Note the expected vs actual result

## Step 5 — Detect project type

Check if project is connected to GitHub:

```bash
gh repo view 2>/dev/null
if [ $? -eq 0 ]; then
  echo "GitHub project detected"
  PROJECT_TYPE="github"
else
  echo "Local project"
  PROJECT_TYPE="local"
fi
```

## Step 6 — Generate bug report

### For Local Projects

Create Markdown file in `docs/bugs/`:

```bash
# Get next bug number
LAST_BUG=$(ls docs/bugs/bug-*.md 2>/dev/null | tail -1 | grep -o '[0-9]*' || echo "0")
BUG_NUM=$(printf "%03d" $((LAST_BUG + 1)))

# Create bug report
cat > docs/bugs/bug-${BUG_NUM}.md << 'BUGEOF'
# Bug #${BUG_NUM}: [标题]

**严重程度**: Critical / High / Medium / Low
**发现时间**: $(date +"%Y-%m-%d %H:%M")
**复现率**: 100% / 偶现

## 复现步骤
1. [步骤1]
2. [步骤2]
3. [步骤3]

## 预期结果
[描述预期行为]

## 实际结果
[描述实际行为]

## 环境信息
- 浏览器: Chrome $(google-chrome --version 2>/dev/null | grep -o '[0-9.]*' | head -1)
- 操作系统: $(uname -s) $(uname -r)
- 应用版本: [从 package.json 或 git tag 获取]

## 相关日志
\`\`\`
[错误堆栈或日志]
\`\`\`

## 截图
![screenshot](../../screenshots/bug-${BUG_NUM}.png)

## 关联文档
- Test Spec: docs/test-spec.md#[section]
- PRD: docs/prd.md#[feature]
BUGEOF
```

### For GitHub Projects

Create GitHub Issue:

```bash
gh issue create \
  --title "Bug: [标题]" \
  --label "bug" \
  --body "$(cat << 'ISSUEEOF'
**严重程度**: Critical / High / Medium / Low
**复现率**: 100% / 偶现

## 复现步骤
1. [步骤1]
2. [步骤2]

## 预期结果
[描述预期行为]

## 实际结果
[描述实际行为]

## 环境信息
- 浏览器: Chrome [version]
- 操作系统: [OS]
- 应用版本: [version]

## 相关日志
\`\`\`
[错误堆栈]
\`\`\`

## 关联文档
- Test Spec: docs/test-spec.md
- PRD: docs/prd.md
ISSUEEOF
)"
```

## Step 7 — Output summary

Print bug report location:

```bash
if [ "$PROJECT_TYPE" = "github" ]; then
  echo "Bug reported: $(gh issue list --limit 1 --json number,url --jq '.[0].url')"
else
  echo "Bug report created: docs/bugs/bug-${BUG_NUM}.md"
fi
```

## Configuration

Default severity mapping:
- Application crash → Critical
- Feature completely broken → High
- Partial functionality loss → Medium
- UI glitch, typo → Low

## Edge Cases

**No screenshots available**: Include note in report, describe visual issue in text

**Cannot determine severity**: Default to Medium, let Engineer adjust

**GitHub CLI not authenticated**: Fall back to local Markdown even if .git exists

**Duplicate bug**: Check existing bugs/issues before creating new one
