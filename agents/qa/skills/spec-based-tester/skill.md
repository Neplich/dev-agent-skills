---
name: spec-based-tester
description: "Execute standard test cases based on Test Spec. Reads Test Spec + PRD + TRD to generate UI interaction and boundary tests using Playwright. Use when you need to verify documented requirements and edge cases."
---

# Spec-Based Tester

Execute standard test cases based on Test Spec documentation. This skill generates and runs UI interaction tests and boundary tests using Playwright.

## When to Use

- After Engineer completes implementation
- To verify documented requirements from Test Spec
- When user asks to "执行规范测试", "基于 Test Spec 测试", or "验证需求"
- Before releasing features to production

## Step 1 — Read specifications

Read the following documents to understand test requirements:

```bash
# Check if required documents exist
test -f docs/test-spec.md && echo "Test Spec found"
test -f docs/prd.md && echo "PRD found"
test -f docs/trd.md && echo "TRD found"
```

Read each document to extract:
- Test scenarios from Test Spec
- User stories and acceptance criteria from PRD
- Technical constraints from TRD

## Step 2 — Detect environment

Check if the application is already running:

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000
```

If response is not 200, proceed to start the application.

## Step 3 — Start application

Try to start the application using these methods in order:

1. Check `deploy/local.md` for startup commands
2. Try common commands:
   - `npm run dev`
   - `npm start`
   - `yarn dev`
   - `pnpm dev`
   - `docker-compose up -d`

Wait for health check (max 60 seconds, check every 2 seconds):

```bash
for i in {1..30}; do
  if curl -s http://localhost:3000 > /dev/null; then
    echo "App ready"
    break
  fi
  sleep 2
done
```

## Step 4 — Install dependencies

Install Playwright if not already installed:

```bash
npm install -D playwright
npx playwright install chromium
```

## Step 5 — Generate test cases

Create test file at `tests/spec-based.test.js`:

```javascript
const { chromium } = require('playwright');

const testResults = {
  total: 0,
  passed: 0,
  failed: 0,
  failures: []
};

async function runTest(name, testFn) {
  testResults.total++;
  try {
    await testFn();
    testResults.passed++;
    console.log(`✓ ${name}`);
  } catch (error) {
    testResults.failed++;
    testResults.failures.push({ name, error: error.message });
    console.log(`✗ ${name}: ${error.message}`);
  }
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('http://localhost:3000');

  // Generate tests based on Test Spec scenarios
  // UI interaction tests
  await runTest('User can navigate to login page', async () => {
    await page.click('a[href="/login"]');
    await page.waitForURL('**/login');
  });

  // Boundary tests
  await runTest('Empty form submission shows validation', async () => {
    await page.click('button[type="submit"]');
    const error = await page.locator('.error-message').textContent();
    if (!error) throw new Error('No validation error shown');
  });

  await browser.close();

  // Output results
  console.log(JSON.stringify(testResults, null, 2));
})();
```

Generate test cases for:

1. **UI Interaction Tests**: User flows from Test Spec
2. **Boundary Tests**: Empty values, max length, special characters, negative numbers

## Step 6 — Execute tests

Run the generated test suite:

```bash
node tests/spec-based.test.js > test-output.json 2>&1
```

Capture:
- Test results (pass/fail)
- Screenshots on failure
- Console errors
- Network failures

## Step 7 — Generate test report

Create test report at `docs/qa-reports/YYYY-MM-DD-test-report.md`:

```markdown
# 测试报告 - YYYY-MM-DD

**执行时间**: YYYY-MM-DD HH:MM - HH:MM
**测试类型**: 规范测试

## 统计
- 总用例数: N
- 通过: N
- 失败: N
- 跳过: 0

## 失败用例
1. [Bug #001](../bugs/bug-001.md) - [描述]
2. [Bug #002](../bugs/bug-002.md) - [描述]

## 测试覆盖
- UI 交互测试: N/N
- 边界测试: N/N

## 建议
- [改进建议]
```

For each failure, create a detailed bug report using the `bug-analyzer` skill.

## Step 8 — Cleanup

Close browser and stop application if it was started by this skill:

```bash
# Kill the process if started in Step 3
kill $APP_PID 2>/dev/null
```

## Step 9 — Commit results

Commit the test report:

```bash
git add docs/qa-reports/ tests/
git commit -m "Add spec-based test report - $(date +%Y-%m-%d)

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

## Configuration

Default settings (can be overridden by user):

- Target URL: http://localhost:3000
- Browser: Chrome (headless)
- Test timeout: 30 seconds per test
- Screenshot on failure: enabled
- Test data location: `test-data/`

## Boundary Test Data

Generate these test cases automatically:

- **Empty values**: "", null, undefined
- **Max length**: 255 characters, 1000 characters
- **Special characters**: `<script>`, `'; DROP TABLE--`, `../../../etc/passwd`
- **Negative numbers**: -1, -999999
- **Zero values**: 0, 0.0
- **Extreme dates**: 1900-01-01, 2099-12-31

## Edge Cases

- **Missing Test Spec**: Report error and ask user to create Test Spec first
- **App won't start**: Report error and ask user to start manually
- **Authentication required**: Ask user for login credentials or test URL
- **All tests pass**: Generate report with success summary
- **No test scenarios found**: Report warning and suggest adding test cases to Test Spec
