# Documentation hosting decision

- Repository: `atlas-console`
- Decision date: `2026-07-11`
- Reviewed after content batch: `docs-2026-07-18`
- Decision owner: Repository Maintainer
- Operations owner: Web Platform

Public and Internal documentation are published as static artifacts by
`.github/workflows/publish-docs-static.yml`. The application image and its
Compose and Helm definitions do not contain or start the documentation site.

The maintainer reviewed the workflow, bucket destinations, and access policy
after the latest content batch and signed the existing arrangement without a
configuration change.

- Signed by: `Repository Maintainer`
- Signed at: `2026-07-18T16:20:00+08:00`
