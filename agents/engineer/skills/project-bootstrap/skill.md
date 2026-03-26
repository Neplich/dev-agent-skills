---
name: project-bootstrap
description: "Initialize a new project from scratch based on a TRD. Use this skill when the user wants to create a new project, scaffold a new codebase, set up a new repository, or bootstrap a project structure. Trigger on phrases like '新建项目', '初始化项目', '搭建项目', 'scaffold', 'bootstrap', 'create new project', or when a TRD describes a project that doesn't exist yet."
---

# Project Bootstrap

Initialize a new project from scratch based on TRD specifications. Intelligently chooses between official CLI tools and manual setup depending on the tech stack.

## When to Use

- TRD describes a project that doesn't exist yet
- User explicitly asks to create/scaffold/bootstrap a new project
- `codebase-analyzer` reports an empty directory

## Step 1 — Read TRD for tech stack requirements

Locate and read the TRD document:

```bash
ls docs/trd*.md docs/TRD*.md 2>/dev/null
```

If no TRD exists, ask the user for:
1. Primary language and framework
2. Key features that drive architecture (API-only? Full-stack? CLI tool?)
3. Any specific tooling preferences

Extract from TRD:
- **Language + framework** (e.g., TypeScript + Next.js)
- **Database** (if any)
- **Architecture pattern** (monorepo, serverless, etc.)
- **Key integrations** (auth provider, external APIs, etc.)

## Step 2 — Choose initialization method

Apply this decision tree:

```
Has official CLI scaffolder?
├── Yes → Use it (e.g., create-next-app, cargo init)
│   └── Does TRD specify options? → Pass them as CLI flags
└── No → Manual setup
    └── Create directory structure + manifest + minimal config
```

### Official CLI mapping

| Framework | Command | Common Options |
|-----------|---------|---------------|
| Next.js | `npx create-next-app@latest <name>` | `--typescript --tailwind --eslint --app --src-dir` |
| Vite (React) | `npm create vite@latest <name> -- --template react-ts` | |
| Vite (Vue) | `npm create vite@latest <name> -- --template vue-ts` | |
| Express | Manual (no official CLI) | |
| NestJS | `npx @nestjs/cli new <name>` | `--strict --package-manager <pm>` |
| FastAPI | Manual | |
| Django | `django-admin startproject <name>` | |
| Go module | `go mod init <module-path>` | |
| Rust | `cargo init <name>` | `--lib` or `--bin` |
| Tauri | `npm create tauri-app@latest` | |

If unsure, tell the user which CLI you plan to use and confirm before running.

## Step 3 — Run initialization

Execute the chosen method. For CLI tools, use non-interactive flags where possible to avoid prompts.

After initialization, verify the project structure:

```bash
ls -la
```

## Step 4 — Configure project infrastructure

Based on TRD requirements and detected tech stack, set up:

### Linting & Formatting
- **TypeScript/JS**: ESLint + Prettier (or Biome)
- **Python**: Ruff
- **Go**: Built-in (`go fmt`, `go vet`) + golangci-lint
- **Rust**: rustfmt + clippy

### Git configuration
- `.gitignore` (use the framework's default, extend if needed)
- `.editorconfig` if the TRD mentions team-wide formatting

### CI (if TRD specifies)
Create `.github/workflows/ci.yml` with:
- Lint step
- Test step
- Build step

Use the simplest working CI config. Don't over-engineer.

## Step 5 — Install core dependencies

Based on TRD, install:
- Database ORM/driver
- Auth libraries
- Testing framework (if not included by the scaffolder)
- Any other TRD-specified dependencies

Use the detected package manager's install command.

## Step 6 — Verify the project works

Run these checks in order:

1. **Build**: `npm run build` / `cargo build` / `go build ./...` / etc.
2. **Lint**: `npm run lint` / `ruff check .` / `golangci-lint run` / etc.
3. **Test**: `npm test` / `pytest` / `go test ./...` / `cargo test` / etc. (expect 0 tests but no errors)

If any step fails, fix it before proceeding.

## Step 7 — Generate Project Profile

Run `codebase-analyzer` logic on the newly created project to produce a Project Profile. This becomes the handoff packet for subsequent skills.

## Step 8 — Summary

Output a summary:

```
## 项目初始化完成

- **项目名**: <name>
- **技术栈**: <language + framework>
- **包管理器**: <pm>
- **目录结构**: <brief description>
- **已配置**: lint ✅ / format ✅ / CI ✅ / test framework ✅
- **验证**: build ✅ / lint ✅ / test ✅

### 建议下一步
- 使用 `feature-implementor` 开始实现功能
```

## Edge Cases

- **TRD specifies unfamiliar framework**: Search for the framework's official getting-started guide and follow it. Don't guess.
- **Monorepo**: Use workspace tools (pnpm workspaces, Turborepo, Nx) as specified in TRD. Initialize root workspace first, then individual packages.
- **No TRD available**: Ask the user the minimum questions (language, framework, project type) and proceed. Generate a minimal viable setup.
- **CLI tool not installed**: Check with `which <tool>` or `npx` fallback. Install globally only if the user agrees.
- **Conflicting TRD requirements**: Flag the conflict to the user and ask for a decision before proceeding.
```
