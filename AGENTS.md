# Repository Instructions

This repository publishes seven role-based Agent plugins for product, design,
engineering, QA, DevOps, security, and formal documentation work. The current
architecture is documented in [docs/architecture.md](docs/architecture.md).

## Always-Loaded Invariants

- Each Agent lives under `agents/{agent-name}/` with role README files,
  `skills/`, and tests.
- `SKILL.md` is the public Skill contract. Optional private staged instructions
  live under `_internal/`; generated contracts under `_internal/_generated/`
  are read-only.
- `.claude-plugin/marketplace.json` registers Agent plugins and Skills.
  `skills-lock.json` records installed Skill metadata.
- `AGENTS.md` is the repository guidance source. `CLAUDE.md` remains a
  relative symlink to it and must not be edited separately.
- Follow the exact requested and approved scope. Do not refactor adjacent code,
  add speculative abstractions, or modify unrelated user changes.
- New formal documents default to a document-writing sub-agent. Complex coding
  uses a scoped implementation sub-agent and separate validation sub-agent when
  the owning Skill requires that split.
- Prefer `uv` for Python and Chrome-based tooling for frontend interaction.
  Fetch local time before time-sensitive operations.

Document hierarchy, ownership, frontmatter, links, QA E2E assets, generated
content, and archive lifecycle are authoritative in
[docs/AGENTS.md](docs/AGENTS.md).

## PM Entry and Role Gates

Explicitly named capabilities keep their own gates. Otherwise product or
engineering R&D intent enters `pm-agent`; ordinary non-R&D work stays with the
current assistant. Project docs, code, and markers are classification evidence
only after PM entry.

Downstream role routers require a PM handoff packet, equivalent confirmed
document chain, or their Specialist's accepted entry basis. Routers keep only
entry credentials, routing, blockers, and Specialist pointers. Authoritative
cross-role contracts live under
`agents/product_manager/skills/idea-to-spec/_internal/_shared/`; downstream
plugins consume generated local copies.

After a role completes, recommend the next owner. Auto-continue automates
handoff proposals but never bypasses role boundaries, hard gates, authorization,
or unavailable targets.

## Change Tier

| Tier | Typical scope | Signal |
| --- | --- | --- |
| `hotfix` | Direct single-file correction or existing failing-test repair | Approved PRD/TRD expectation is unchanged and one direct verification covers the change |
| `standard` | Normal feature behavior change or multi-file refactor | A feature path exists and expectations or technical design need alignment |
| `major` | Cross-role feature, Agent/Skill lifecycle, contract surface, release | Multiple role documents, marketplace surfaces, or contract scripts are affected |

`pm-agent` assigns the tier. Unclear work is `standard`. A request cannot use
`hotfix` to skip expected-behavior alignment. Every tier retains evidence;
`hotfix` only uses lighter plan/closeout/QA forms defined by the owning Skill.

## Engineering and Validation

- PM owns product requirements and decisions. Engineer owns TRD/API/ADR and
  implementation. Designer stops at design delivery. QA, DevOps, Security, and
  Docs keep their role boundaries.
- Existing behavior changes and bug repairs align PRD/TRD before mutation.
  Explicit diagnosis-only work may collect evidence without mutation under its
  own gate.
- `feature-implementor` requires a confirmed plan before implementation.
  Active and archived plan rules are in [docs/AGENTS.md](docs/AGENTS.md).
- QA E2E reuses persistent cases before exploration and follows the QA Router
  references named in [docs/AGENTS.md](docs/AGENTS.md).
- Role Skill or Agent lifecycle changes use the repository
  `maintain-skills` Skill and
  [maintenance cookbook](docs/cookbook/maintain-skills.md).
- Eval creation, modification, execution, diagnosis, and durable comparison use
  `skill-eval-runner` and the
  [eval cookbook](docs/cookbook/run-skill-evals.md).

Each implementation plan states expected code-size magnitude and exact
verification. Iterate until the approved requirements, plan, tests, and diff
agree. Remove runtime artifacts before delivery.

## Git and GitHub

- Never make maintenance changes directly on `main`; create a branch and merge
  through a PR.
- GitHub operations prefer Connector, then authenticated `gh` / GraphQL, then
  Chrome. Verify bulk writes with `gh`.
- Commit and PR titles use `<type>(<scope>): <中文描述>`; bodies are Chinese.
  Do not add co-author trailers.
- After a PR exists, add new commits and push normally. Do not amend, rebase, or
  force-push unless explicitly requested.
- Never merge a PR without explicit maintainer confirmation. Default merge mode
  is squash.
- After a verified merge, switch to the default branch, pull with
  `--ff-only`, and delete only the exact merged local branch. Do not delete the
  remote branch unless requested.

The manual release sequence is authoritative in
[docs/cookbook/release.md](docs/cookbook/release.md). Do not add Release CI,
upload marketplace packages automatically, or configure release-bot bypass.

## Required Checks

Run checks proportional to the change and any stronger plan-specific list:

```bash
uv run scripts/generate_shared_contracts.py --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
git diff --check
```

Repository Skills define additional lifecycle and eval checks; do not duplicate
their full protocols here.

## 开发工作流

分支、实施与验证入口见上文；顺序化维护流程见 `docs/cookbook/`。

## 文档组织

文档树、frontmatter、owner 与生命周期见 [docs/AGENTS.md](docs/AGENTS.md)。

## 仓库治理

Git、PR 和 release 权限边界见上文及
[release cookbook](docs/cookbook/release.md)。

## Skill 测试

Skill eval 统一使用 `skill-eval-runner` 与
[eval cookbook](docs/cookbook/run-skill-evals.md)。

## QA E2E 测试用例持久化

QA E2E 目录与三个格式 owner 见 [docs/AGENTS.md](docs/AGENTS.md#qa-e2e-资产)。
