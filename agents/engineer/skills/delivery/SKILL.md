---
name: delivery
description: "Prepare focused commits and pull requests, verify CI, and complete authorized Git delivery with accurate descriptions and a clean workspace."
---

# Delivery

Inspect the repository, branch, working tree, remote, and current PR before
writing. The user's request and existing session authorization establish the
delivery scope; apply repository-specific Git conventions.

## Prepare and deliver

1. Review the diff, preserve unrelated user changes, and run the relevant checks.
2. Use a dedicated branch for the change. Keep the requested base and branch
   naming convention.
3. Stage the intended files and write a commit message describing the resulting
   behavior. Use ordinary follow-up commits for an existing PR.
4. Push the branch and create or update the PR with the problem, final change,
   verification, and material risks. Reference the relevant issues.
5. Read back the PR's head and CI results. Resolve relevant failures and report
   the final review state.
6. Merge when the user has authorized that action and the required checks pass.
   Match the reviewed head, verify the merge, synchronize the default branch,
   and perform the requested branch cleanup.

A concise PR body is usually sufficient. Expand it for compatibility changes,
migrations, rollout steps, or important review tradeoffs. Use exact newline-
preserving text inputs for multiline descriptions.

Summarize the delivered commit or PR, test results, merge state, and outstanding
items. Keep irreversible and externally visible actions within the established
permission scope, and ask only for authorization that is still missing.
