# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.86.0] - 2026-03-18

### Added

- Add support for filesystem memory tools ([#1247](https://github.com/anthropics/anthropic-sdk-python/issues/1247))
- API: expand `/v1/models` capabilities (manual updates)

### Changed

- API: manual updates

### Fixed

- Fix `AsyncAnthropic._make_status_error` missing 529 and 413 error cases ([#1244](https://github.com/anthropics/anthropic-sdk-python/pull/1244))
- Pydantic: do not pass `by_alias` unless set
- Deps: bump minimum `typing-extensions` version
