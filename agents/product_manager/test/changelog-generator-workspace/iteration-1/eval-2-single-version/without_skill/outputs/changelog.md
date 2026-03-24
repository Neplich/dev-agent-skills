# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.86.0] - 2026-03-18

### Added

- Add support for filesystem memory tools ([#1247](https://github.com/anthropics/anthropic-sdk-python/issues/1247))
- **api:** Add `/v1/models` capabilities expansion — new types for model capabilities including `ModelCapabilities`, `BetaModelCapabilities`, `CapabilitySupport`, `ContextManagementCapability`, `EffortCapability`, and related beta types

### Fixed

- **client:** `AsyncAnthropic._make_status_error` was missing the `529 → OverloadedError` and `413 → RequestTooLargeError` cases present in the sync client; async users were incorrectly receiving `InternalServerError` for HTTP 529 and base `APIStatusError` for HTTP 413 ([#1244](https://github.com/anthropics/anthropic-sdk-python/pull/1244))
- **pydantic:** Do not pass `by_alias` unless explicitly set
- **deps:** Bump minimum `typing-extensions` version

### Changed

- **internal:** Tweak CI branches configuration

[0.86.0]: https://github.com/anthropics/anthropic-sdk-python/compare/v0.85.0...v0.86.0
