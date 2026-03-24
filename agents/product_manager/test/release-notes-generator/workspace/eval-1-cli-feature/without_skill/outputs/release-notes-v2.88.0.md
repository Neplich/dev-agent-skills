# GitHub CLI 2.88.0 Release Notes

**Released:** March 10, 2026

---

## Highlights

### Request Copilot Code Review from `gh`

You can now add GitHub Copilot as a code reviewer directly from the command line. `gh pr create` and `gh pr edit` both support `--add-reviewer @copilot` (or `--reviewer @copilot` on create), and Copilot also appears as a selectable option in the interactive reviewer prompt.

```sh
# Request Copilot review when creating a PR
gh pr create --reviewer @copilot

# Add Copilot review to an existing PR
gh pr edit --add-reviewer @copilot
```

### Close Issues as Duplicates

A new `--duplicate-of` flag on `gh issue close` lets you mark an issue as a duplicate and link it to the original in one step. You can also use `--reason duplicate` if you just want to set the close reason without referencing a specific issue.

```sh
# Close issue 123 as a duplicate of issue 456
gh issue close 123 --duplicate-of 456

# Close with duplicate reason only
gh issue close 123 --reason duplicate
```

### JSON Output for `gh agent-task`

`gh agent-task list` and `gh agent-task view` now support `--json`, `--jq`, and `--template` flags, making it easy to script and pipe agent task data the same way you do with other `gh` commands.

```sh
gh agent-task list --json id,name,state
gh agent-task view <id> --json state --jq '.state'
```

---

## New Features

- **`gh pr create` / `gh pr edit`** — Copilot Code Review can be requested as a reviewer using `--reviewer @copilot` or `--add-reviewer @copilot`. The interactive reviewer search also surfaces Copilot by name.

- **`gh issue close`** — New `--duplicate-of` flag accepts an issue number or URL to close an issue as a duplicate and link it to the original. `--reason duplicate` is also now supported as a standalone option.

- **`gh pr diff`** — New `--exclude` flag lets you filter specific files out of diff output, useful for ignoring generated or lock files.

- **`gh pr view` / `gh pr list`** — The `files` JSON field now includes a `changeType` property (e.g., `added`, `modified`, `deleted`) for each file entry.

- **`gh repo clone`** — New `--no-upstream` flag skips adding the upstream remote when cloning a fork, giving you more control over your remote configuration.

- **`gh repo edit`** — New `--squash-merge-commit-message` flag lets you set the default squash merge commit message format for a repository.

- **`gh browse`** — New `--blame` flag opens the blame view for a file directly in the browser.

- **`gh pr view` / `gh issue view`** — Actor display names are now shown in a friendly, human-readable format throughout these views.

- **`gh agent-task list` / `gh agent-task view`** — Full `--json`, `--jq`, and `--template` support added.

- **`gh copilot`** — The `COPILOT_GH` environment variable is now set when launching the Copilot CLI, enabling better integration between tools.

---

## Bug Fixes

- **`gh project item-edit`** — Fixed an error that occurred when editing a Draft Issue using only one of `--title` or `--body`.

- **Extension install errors** — Fixed an error message that was displaying a raw Go struct instead of the expected `owner/repo` format.

- **Port forwarder** — Fixed an incorrect integer conversion from `int` to `uint16` that could cause unexpected behavior with port numbers.

- **Color output** — Fixed an invalid ANSI escape code in JSON and diff colorization that could produce garbled output in some terminals.

- **`--json` assignees output** — Fixed a bug where the `databaseId` field for assignees was always returned as `0`.

- **`gh issue list`** — Search qualifiers that are only valid for pull requests are now properly rejected with a clear error message.

- **`gh issue view --comments`** — Eliminated a redundant API call, making this command more efficient.

- **`gh issue develop --name`** — Fixed a bug that could corrupt `.git/config` when the command was run repeatedly with the same branch name.

- **`--remote` flag with repo argument** — Fixed an error that occurred when using `--remote` together with an explicit repo argument.

- **Project scope errors** — Improved the error message shown when creating issues for projects with insufficient scopes.

---

## What's New for Contributors

Thirteen new contributors made their first contribution to `cli/cli` in this release. Thank you to @srt32, @itchyny, @VishnuVV27, @elijahthis, @ManManavadaria, @maxbeizer, @LouisLau-art, @4RH1T3CT0R7, @yuvrajangadsingh, @masonmcelvain, @scarf005, @tksohishi, and @tidy-dev.

---

## Upgrade

Update to the latest version using your package manager, or download directly from the [releases page](https://github.com/cli/cli/releases/tag/v2.88.0).

```sh
# macOS (Homebrew)
brew upgrade gh

# Windows (winget)
winget upgrade --id GitHub.cli

# Linux (apt)
sudo apt update && sudo apt upgrade gh
```

**Full changelog:** https://github.com/cli/cli/compare/v2.87.3...v2.88.0
