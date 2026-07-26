---
type: TRD
feature: project-foundation
feature_path: project-foundation
parent_feature: N/A
feature_level: 1
version: 1.0.0
date: 2026-07-26
last_updated: 2026-07-26
related_prd: N/A
---

# Next.js Project Foundation

Status: Approved

## Scope

Initialize the application under `app/` with the official `create-next-app` CLI.

## Technical Decisions

- Next.js App Router with TypeScript.
- npm package manager and Node.js 22.
- Non-interactive CLI flags: TypeScript, ESLint, App Router, `src/` directory and no import-alias prompt.
- Add Prettier configuration and a `format:check` script.
- Add a minimal `node:test` smoke test and a `test` script.
- Add `.github/workflows/ci.yml` running install, lint, format check, test and build.

## Verification

Run from `app/`:

```bash
npm run build
npm run lint
npm run test
npm run format:check
```

All commands must pass before the bootstrap is reported complete.

## Non-goals

- Product feature implementation.
- Database, authentication or deployment configuration.
- Commit, push or PR creation.
