---
name: maintain-skills
description: Maintain Skills, plugin registration, discovery metadata, documentation and installation consistency in this repository.
---

# Maintain Skills

Update the repository's professional knowledge library within the user's authorized scope. Select the relevant items from [change types](references/change-types.md) and [sync surfaces](references/sync-surfaces.md).

Use the request and current repository evidence to establish the expected result. Keep the implementation and verification proportionate to the change. Continue across documentation, metadata and code work using the same task authorization.

## Implementation

Keep Skill names, paths, references and discovery descriptions consistent. Update the owning plugin's capability directory when its contents change. Refresh `skills-lock.json` hashes for modified Skill files, and regenerate packaged shared references from their source.

Use plans and durable documents when they help readers or future maintenance. Record concise final facts and evidence. Preserve unrelated user work and credentials.

## Verification and Delivery

```bash
uv run scripts/generate_shared_contracts.py --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
git diff --check
```

Run relevant behavior and installation tests. Deliver through a PR with the final changes, verification results and material limitations. Use explicit maintainer authorization for merge and publication.
