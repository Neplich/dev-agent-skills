# Release Notes — v2.88.0 (2026-03-10)

> GitHub CLI now lets you request Copilot Code Review, close duplicate issues, filter diffs, and browse blame — all from the terminal.

## ✨ What's New

### Request Copilot Code Review from the CLI

You can now add Copilot as a reviewer when creating or editing a pull request. Pass `--reviewer @copilot` (or `--add-reviewer @copilot`) to request an AI-powered code review without leaving your terminal. ([#12627](https://github.com/cli/cli/pull/12627))

### Close Issues as Duplicates

A new `--duplicate-of` flag on `gh issue close` lets you mark an issue as a duplicate and link it to the original in one step. You can also use `--reason duplicate` to set the close reason without specifying a linked issue. ([#12811](https://github.com/cli/cli/pull/12811))

### Filter PR Diffs by File

`gh pr diff` now supports an `--exclude` flag so you can strip generated files, lock files, or any pattern from diff output. ([#12655](https://github.com/cli/cli/pull/12655))

### Blame View in the Browser

`gh browse --blame` opens the blame view for the current file directly in your browser, saving the extra click from the GitHub UI. ([#11486](https://github.com/cli/cli/pull/11486))

## 🐛 Bug Fixes

- Fixed `gh project item-edit` failing when only `--title` or `--body` was passed for a Draft Issue. ([#12787](https://github.com/cli/cli/pull/12787))
- Fixed extension install errors showing a raw Go struct instead of a readable `owner/repo` format. ([#12836](https://github.com/cli/cli/pull/12836))
- Fixed an integer overflow in the port forwarder that could cause unexpected behavior on high port numbers. ([#12831](https://github.com/cli/cli/pull/12831))
- Fixed broken ANSI color codes in JSON and diff output. ([#12720](https://github.com/cli/cli/pull/12720))
- Fixed assignee `databaseId` always returning `0` in `--json` output. ([#12783](https://github.com/cli/cli/pull/12783))
- Fixed an error when using `--remote` together with a repo argument. ([#12375](https://github.com/cli/cli/pull/12375))
- Fixed `.git/config` corruption caused by repeated `gh issue develop --name` calls. ([#12651](https://github.com/cli/cli/pull/12651))
- Fixed a redundant API call in `gh issue view --comments`. ([#12652](https://github.com/cli/cli/pull/12652))

## 🔧 Other Improvements

- `gh repo clone` now supports `--no-upstream` to skip setting up the upstream remote. ([#12686](https://github.com/cli/cli/pull/12686))
- `gh repo edit` gains `--squash-merge-commit-message` for configuring squash merge commit messages. ([#12846](https://github.com/cli/cli/pull/12846))
- `gh agent-task list` and `gh agent-task view` now support `--json`, `--jq`, and `--template` flags, consistent with other `gh` commands. ([#12806](https://github.com/cli/cli/pull/12806), [#12807](https://github.com/cli/cli/pull/12807))
- `gh pr view` and `gh issue view` now display friendly display names for all actors. ([#12854](https://github.com/cli/cli/pull/12854))
- `gh pr view/list` JSON output now includes a `changeType` field per file. ([#12657](https://github.com/cli/cli/pull/12657))
- PR and issue search qualifiers are now validated earlier, preventing confusing errors when using pull-request-only filters in `gh issue list`. ([#12623](https://github.com/cli/cli/pull/12623))

## ⬆️ Upgrading

**macOS (Homebrew):**
```
brew upgrade gh
```

**Windows (winget):**
```
winget upgrade --id GitHub.cli
```

**Linux:** See the [installation docs](https://github.com/cli/cli/blob/trunk/docs/install_linux.md) for your package manager.

Full changelog: https://github.com/cli/cli/compare/v2.87.3...v2.88.0
