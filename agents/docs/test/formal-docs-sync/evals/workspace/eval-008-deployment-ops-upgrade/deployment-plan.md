# Deployment plan

## Current verified path

Keep Docker Compose as the supported runtime for development and staging.

## Planned, not executed

Migrate production to Kubernetes with a Helm chart and `helm upgrade --install`. No chart, cluster validation, rollout result, or rollback drill exists yet.
