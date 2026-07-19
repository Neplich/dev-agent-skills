# Confirmed deployment-verification handoff

- request_type: `delivery`
- change_tier: `standard`
- feature_path: `ai-hub-runtime`
- mode: `deployment verification`
- confirmed_scope: `deploy/compose.yaml` and `docs/site/ops/ai-hub-upgrade.md`
- source_documents: `docs/engineer/ai-hub-runtime/TRD.md`, `.eval/deployment-results.md`, and `deployment-plan.md`
- environment_differences: Development uses port 8080; staging uses port 9080. Both use the same Compose service and `/healthz` check.
- candidate_scope_confirmation: The maintainer confirms the single ops page and `deploy/**` map entry for writing.
- exclusions: Kubernetes/Helm migration, product behavior, Release Notes, deployment execution, and all unrelated pages.
