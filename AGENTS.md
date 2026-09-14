# Repository Instructions

This repository publishes an on-demand professional knowledge library: six plugins and thirty-seven directly usable Skills. Role names organize expertise. The current assistant owns the user's task and combines relevant capabilities through completion.

## Working Approach

Use the user's request, issues, code, tests and existing documents to establish the expected outcome. Select references, plans, formal documents and sub-agents when they materially help the task. Continue within existing authorization; ask when a material decision is missing or an action needs additional permission.

Repository Skill content is the product being maintained. Maintain this repository using the active assistant's configuration and the user's instructions. Preserve unrelated user changes, credentials and accurate verification evidence. Keep final artifacts and remove task-created temporary files and caches at completion.

## Source Layout

- Plugins live in `agents/{role}/`, with bilingual READMEs and `skills/`.
- Each `SKILL.md` describes a directly usable capability; `_internal/` and `references/` provide optional detail.
- `.claude-plugin/marketplace.json`, plugin manifests and `skills-lock.json` describe installation and distribution.
- Shared references are maintained in `agents/product_manager/skills/idea-to-spec/_internal/_shared/`. Generate their packaged copies with `scripts/generate_shared_contracts.py`.
- `AGENTS.md` is the repository guidance source; `CLAUDE.md` is its relative symlink.

See [architecture](docs/architecture.md), [document guidance](docs/AGENTS.md) and [Skill maintenance](docs/cookbook/maintain-skills.md) for the relevant details.

## Git and Release

Make maintenance changes on a branch and deliver them through a PR. Use `<type>(<scope>): <中文描述>` for commit and PR titles, Chinese bodies, and the author's own attribution. Preserve existing commits after a PR is created; append and push new commits normally. Amend, rebase and force-push require an explicit user request.

Merge after explicit maintainer authorization, using squash by default. After a verified merge, switch to the default branch, pull with `--ff-only`, and delete the exact merged local branch. Remote branch deletion requires explicit authorization.

Use the [manual release procedure](docs/cookbook/release.md). Publication and deployment follow the user's explicit authorization. GitHub operations prefer Connector, then authenticated `gh` / GraphQL, then Chrome; verify bulk writes with `gh`.

## Verification

Prefer `uv` for Python and Chrome-based tools for browser interaction. Read local time for time-sensitive work. Run relevant behavior tests together with:

```bash
uv run scripts/generate_shared_contracts.py --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
git diff --check
```

Report what changed, the verification results and any remaining limitations.
