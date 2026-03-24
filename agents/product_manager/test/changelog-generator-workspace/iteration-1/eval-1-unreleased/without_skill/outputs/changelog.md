# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

> No changes have been merged into `main` since the v0.86.0 release (2026-03-18).

<!-- Pending open PRs (not yet merged as of 2026-03-20):
  - #1263 fix: map SSE error types to correct HTTP status codes in streaming
  - #1261 test(lib/tools): test unit tests for tool_runner observability hooks
  - #1259 feat(lib/tools): add observability hooks to tool_runner
  - #1255 fix: remove spurious pass statement in signature_delta handler
  - #1253 docs: remove outdated single-content-block note from get_final_text
  - #1252 Add arithmetic calculator example using tool use
  - #1251 Fix: IndexError when streaming with multiple content blocks (#1192)
  - #1248 docs(examples): add module docstring to messages.py example
  - #1247 perf: skip no-op recursive transform for types without PropertyInfo
  - #1246 fix(bedrock): add missing stream() method to beta.messages
-->

---

## [0.86.0] - 2026-03-18

Full Changelog: [v0.85.0...v0.86.0](https://github.com/anthropics/anthropic-sdk-python/compare/v0.85.0...v0.86.0)

### Added

- Add support for filesystem memory tools ([#1247](https://github.com/anthropics/anthropic-sdk-python/issues/1247))
- **api:** manual updates — `/v1/models` capabilities expansion

### Fixed

- `AsyncAnthropic._make_status_error` missing 529 and 413 cases ([#1244](https://github.com/anthropics/anthropic-sdk-python/pull/1244))
- **deps:** bump minimum `typing-extensions` version
- **pydantic:** do not pass `by_alias` unless set

### Changed

- **internal:** tweak CI branches

[Unreleased]: https://github.com/anthropics/anthropic-sdk-python/compare/v0.86.0...HEAD
[0.86.0]: https://github.com/anthropics/anthropic-sdk-python/compare/v0.85.0...v0.86.0
