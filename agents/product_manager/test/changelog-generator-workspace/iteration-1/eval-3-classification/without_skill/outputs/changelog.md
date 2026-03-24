# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added

- feat(auth): add OAuth2 login support (#101)

### Changed

- perf: reduce API response time by caching (#104)
- feat!: redesign plugin configuration API (#105)

### Fixed

- fix: resolve crash when token expires (#102)
- fix(ui): correct button alignment on mobile (#107)

### Removed

- remove: drop Python 3.7 support (#109)

### Security

- security: patch XSS vulnerability in template renderer (#110)
