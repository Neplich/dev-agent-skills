# PM → Docs deployment recheck handoff

- request_type: `formal_docs`
- delivery_mode: `deployment verification`
- change_tier: `hotfix`
- feature_path: `docs-deployment-recheck`
- scope_decision: Read-only recheck of the existing documentation-site build
  and release configuration for `sites/atlas-portal/` and
  `sites/orbit-console/` after content synchronization.
- downstream_owner: `Docs`
- required_output: An evidence-backed assessment of the access variants each
  site currently covers, the remaining deployment gaps, and the appropriate
  next owner.
- exclusions: No edits to Dockerfiles, workflows, Compose, Helm, or any other
  deployment asset; do not execute deployment work.
- blockers_risks: A site-level gap may require a separate repository-wide
  deployment handoff before operational changes can be planned.
