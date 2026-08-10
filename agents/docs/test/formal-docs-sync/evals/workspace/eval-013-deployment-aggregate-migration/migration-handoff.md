# PM → Docs confirmed aggregate-page migration handoff

- request_type: `formal_docs`
- delivery_mode: `deployment verification`
- change_tier: `standard`
- feature_path: `docs-deployment`
- downstream_owner: `Docs`
- required_output: Migrate the confirmed aggregate deployment page into the
  current three-class documentation structure, repair its documentation links
  and mappings, and report the executed host check.
- blockers_risks: The target release version is not confirmed, so the migrated
  pages remain unverified and the later pre-tag audit stays blocked.

- Old page: `docs/site/ops/deployment.md`
- New authority: deployment root index, shared environment reference, and Development/Docker/Kubernetes-Helm directories
- Confirmed atomic work: path migration, all inbound/internal link repairs, recursive navigation, per-class change-map entries, duplicate fact consolidation
- Preserve unknown change-map fields, excludes, and unrelated entries
- Target release version: not confirmed
