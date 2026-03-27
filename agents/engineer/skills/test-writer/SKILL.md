---
name: test-writer
description: "Write tests based on PM Test Spec and implemented code. Use this skill whenever the user asks to write tests, add test coverage, create unit tests, or validate an implementation with tests. Trigger on phrases like '写测试', '补测试', '添加测试', 'write tests', 'add test coverage', 'test this feature', or after feature-implementor completes and tests are needed."
---

# Test Writer

Write tests based on PM Test Spec documents and implemented code. Identifies the project's testing framework and conventions, writes tests that verify the implementation meets acceptance criteria, and runs them to confirm they pass.

## When to Use

- After `feature-implementor` completes a feature implementation
- When the user asks to add tests for existing code
- When Test Spec exists and tests need to be written
- Standalone: to add test coverage for untested code

## Step 1 — Read Test Spec

Locate the Test Spec:

```bash
ls docs/test-spec*.md docs/tspecs*.md docs/TEST_SPEC*.md 2>/dev/null
```

Extract:
- Test scenarios (happy path, edge cases, error cases)
- Test data requirements
- Coverage requirements (which components must be tested)
- Integration test scenarios (if any)

If no Test Spec exists, derive test cases from:
1. PRD acceptance criteria (each P0 criterion = at least one test)
2. API Spec (each endpoint = request validation + success + error tests)
3. Obvious edge cases from reading the code

## Step 2 — Detect testing setup

Identify the project's test framework and conventions:

| Framework | Detection | Config File | Run Command |
|-----------|-----------|-------------|-------------|
| Jest | `jest` in package.json deps | `jest.config.*` | `npx jest` |
| Vitest | `vitest` in package.json deps | `vitest.config.*` | `npx vitest run` |
| Pytest | `pytest` in requirements/pyproject | `pytest.ini`, `pyproject.toml` | `pytest` |
| Go test | Go project | N/A (built-in) | `go test ./...` |
| Cargo test | Rust project | N/A (built-in) | `cargo test` |
| RSpec | `rspec` in Gemfile | `.rspec` | `bundle exec rspec` |

Also check:
- Where do existing tests live? (`tests/`, `__tests__/`, `*_test.go`, `*_test.rs`)
- What patterns do existing tests follow? (describe/it, test(), function names)
- Are there test utilities, fixtures, or helpers? Read them.
- What mocking approach is used? (jest.mock, unittest.mock, testify, etc.)

## Step 3 — Plan test files

Map Test Spec scenarios to test files:

```text
## 测试计划

| 测试文件 | 测试对象 | 场景数 | 类型 |
|----------|---------|--------|------|
| `tests/services/notification-service.test.ts` | NotificationService | 5 | 单元测试 |
| `tests/api/notifications.test.ts` | POST/GET /notifications | 8 | 集成测试 |
```

## Step 4 — Write tests

For each test file:

1. **Read the source code** being tested — understand the public interface
2. **Read existing test files** in the same directory for pattern matching
3. **Write tests** following the project's testing conventions:
   - Test file naming: match the project's pattern (`*.test.ts`, `*_test.go`, `test_*.py`)
   - Test structure: match existing style (describe/it blocks, flat test functions, etc.)
   - Assertions: use the project's assertion library
   - Mocking: use the project's mocking approach

### Test case priorities

Write tests in this order:
1. **Happy path**: The main success scenario from Test Spec
2. **Input validation**: Invalid inputs, missing fields, wrong types
3. **Error cases**: What happens when dependencies fail
4. **Edge cases**: Boundary values, empty lists, max limits
5. **Integration**: Cross-module interactions (if Test Spec requires)

### Test naming

Follow the project's naming convention. If no convention exists:
- Describe WHAT is being tested and WHAT should happen
- `test_create_notification_returns_201_with_valid_input`
- `it('should return 404 when notification not found')`

## Step 5 — Run tests

Execute the full test suite:

```bash
# Use the project's test command
npm test        # Node.js
pytest -v       # Python
go test ./... -v  # Go
cargo test      # Rust
```

### Analyze results

- **All pass**: Report success and coverage summary
- **Test failures**: For each failure, determine:
  - Is this a **code bug**? → Flag it and recommend `debugger` skill
  - Is this a **test bug**? → Fix the test and re-run
  - Is this a **missing dependency**? → Install and re-run

## Step 6 — Report

```text
## 测试结果

- **测试框架**: <framework>
- **测试文件**: <N> 个
- **测试用例**: <N> 个
- **通过**: <N> ✅
- **失败**: <N> ❌ (如有)

### Test Spec 覆盖
| Test Spec 场景 | 对应测试 | 状态 |
|----------------|---------|------|
| <scenario> | <test name> | ✅/❌ |

### 建议下一步
- <recommendation based on results>
```

## Edge Cases

- **No test framework installed**: Install the most common one for the language (vitest for TS, pytest for Python, etc.) and configure it minimally. Ask user before installing.
- **Existing tests break**: If running the full suite reveals pre-existing failures, report them separately from new test results.
- **Test Spec scenarios not testable**: Some scenarios (e.g., "user perceives fast response") can't be unit tested. Flag them and suggest manual testing or E2E test approaches.
- **Flaky tests**: If a test passes sometimes and fails sometimes, flag it as flaky and investigate the cause (timing, state, randomness).
