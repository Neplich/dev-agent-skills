# Release Notes — v2.88.0 (March 10, 2026)

> Request Copilot code reviews, close duplicate issues, and filter diffs — all from your terminal.

## ✨ What's New

### Request Copilot Code Review as a Reviewer

You can now add GitHub Copilot as a code reviewer directly from `gh pr create` and `gh pr edit`. Copilot appears in the interactive reviewer search prompt alongside human reviewers, or you can add it non-interactively with `--add-reviewer @copilot` / `--reviewer @copilot`. ([#12627](https://github.com/cli/cli/pull/12627))

```sh
# Request Copilot review at PR creation time
gh pr create --reviewer @copilot

# Add Copilot to an existing PR
gh pr edit --add-reviewer @copilot
```

### Close Issues as Duplicates

`gh issue close` gains a `--duplicate-of` flag so you can mark a closed issue as a duplicate and link it to the canonical issue in one command. Use `--reason duplicate` alone when you want to set the close reason without specifying a linked issue. ([#12811](https://github.com/cli/cli/pull/12811))

```sh
# Close issue 123 as a duplicate of issue 456
gh issue close 123 --duplicate-of 456

# Close with duplicate reason only (no linked issue)
gh issue close 123 --reason duplicate
```

### Filter Files from PR Diffs

`gh pr diff` now accepts an `--exclude` flag to strip specific files or glob patterns from the diff output — useful for ignoring generated files, lock files, or vendored code you didn't touch. ([#12655](https://github.com/cli/cli/pull/12655))

```sh
# Exclude lock files and generated protobuf output from a diff
gh pr diff --exclude "go.sum" --exclude "*.pb.go"
```

### JSON Output for `gh agent-task`

`gh agent-task list` and `gh agent-task view` now support `--json`, `--jq`, and `--template` flags, bringing them in line with the rest of the `gh` command family. ([#12806](https://github.com/cli/cli/pull/12806), [#12807](https://github.com/cli/cli/pull/12807))

```sh
# List agent tasks as JSON, filter by state
gh agent-task list --json id,name,state
gh agent-task view <id> --json state --jq '.state'
```

### Browse File Blame in the Browser

`gh browse` adds a `--blame` flag that opens the blame view for a file directly in your browser, saving you a few clicks when you need to track down who last touched a line. ([#11486](https://github.com/cli/cli/pull/11486))

```sh
# Open blame view for a specific file
gh browse --blame src/main.go
```

### Friendly Display Names in `pr view` and `issue view`

`gh pr view` and `gh issue view` now show human-readable display names for all actors (assignees, reviewers, authors) instead of raw login handles where a display name is available. ([#12854](https://github.com/cli/cli/pull/12854))

### Skip Upstream Setup on Clone

`gh repo clone` gains a `--no-upstream` flag. When cloning a fork, this prevents `gh` from automatically adding the parent repository as an `upstream` remote — handy when you manage remotes yourself or work in monorepo setups. ([#12686](https://github.com/cli/cli/pull/12686))

```sh
gh repo clone my-org/my-fork --no-upstream
```

### Configure Squash Merge Commit Message via `gh repo edit`

You can now set the default squash-merge commit message format for a repository using the new `--squash-merge-commit-message` flag on `gh repo edit`. ([#12846](https://github.com/cli/cli/pull/12846))

```sh
gh repo edit --squash-merge-commit-message PR_BODY
```

### `changeType` Field in PR Files JSON

`gh pr view` and `gh pr list` JSON output for the `files` field now includes a `changeType` property (`added`, `modified`, `deleted`, `renamed`, `copied`) per file, making it easier to script against file-level change metadata. ([#12657](https://github.com/cli/cli/pull/12657))

## 🐛 Bug Fixes

- Fixed `gh project item-edit` erroring when editing a Draft Issue with only `--title` or `--body` (not both). ([#12787](https://github.com/cli/cli/pull/12787))
- Fixed extension install error messages showing a raw Go struct instead of the expected `owner/repo` format. ([#12836](https://github.com/cli/cli/pull/12836))
- Fixed `assignees[].databaseId` always returning `0` in `--json` output. ([#12783](https://github.com/cli/cli/pull/12783))
- Fixed invalid ANSI SGR escape codes appearing in JSON and diff colorization output. ([#12720](https://github.com/cli/cli/pull/12720))
- Fixed `.git/config` corruption that could occur when running `gh issue develop --name` repeatedly on the same branch. ([#12651](https://github.com/cli/cli/pull/12651))
- Fixed an error when using the `--remote` flag together with a repo argument. ([#12375](https://github.com/cli/cli/pull/12375))
- Fixed a redundant API call in `gh issue view --comments`. ([#12652](https://github.com/cli/cli/pull/12652))
- Fixed incorrect integer conversion (int → uint16) in the port forwarder. ([#12831](https://github.com/cli/cli/pull/12831))
- Improved the scope error message when creating issues for projects. ([#12596](https://github.com/cli/cli/pull/12596))
- `gh issue list` now correctly rejects pull-request-only search qualifiers (e.g., `is:unmerged`) that were previously silently accepted. ([#12623](https://github.com/cli/cli/pull/12623))

## 🔧 Other Improvements

- `gh copilot` now sets the `COPILOT_GH` environment variable when launching the Copilot CLI, enabling downstream tooling to detect the launch context. ([#12821](https://github.com/cli/cli/pull/12821))
- Licenses are now generated and isolated per platform (os/arch combination) to prevent cross-platform contamination in builds. ([#12774](https://github.com/cli/cli/pull/12774))

## ⬆️ Upgrading

**macOS:**
```sh
brew upgrade gh
```

**Windows:**
```sh
winget upgrade --id GitHub.cli
```

**Linux:** See the [installation docs](https://github.com/cli/cli/blob/trunk/docs/install_linux.md) for your distribution.

---

Full changelog: https://github.com/cli/cli/compare/v2.87.3...v2.88.0

Thanks to our 13 first-time contributors: @srt32, @itchyny, @VishnuVV27, @elijahthis, @ManManavadaria, @maxbeizer, @LouisLau-art, @4RH1T3CT0R7, @yuvrajangadsingh, @masonmcelvain, @scarf005, @tksohishi, @tidy-dev
