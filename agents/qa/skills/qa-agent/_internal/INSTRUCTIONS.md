# QA Agent Dispatcher Instructions

## Available Skills

- `exploratory-tester` - Exploratory testing
- `spec-based-tester` - Spec-based testing
- `bug-analyzer` - Bug analysis and reporting
- `regression-suite` - Regression test management

## Intent Mapping

| User Intent | Skills to Execute |
|-------------|------------------|
| "探索性测试" | exploratory-tester |
| "规范测试" | spec-based-tester |
| "分析 bug" | bug-analyzer |
| "回归测试" | regression-suite |
| "完整测试" | spec-based-tester → exploratory-tester → regression-suite |
