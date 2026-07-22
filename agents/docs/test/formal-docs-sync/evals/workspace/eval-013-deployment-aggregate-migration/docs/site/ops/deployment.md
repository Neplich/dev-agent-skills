---
title: Deployment
visibility: both
doc_type: ops
stage: ops
owners: [platform-ops]
related_code: [scripts/dev, deploy/docker, deploy/helm]
last_verified_version: unverified
---
# Deployment

Use `APP_PORT=8080` for every mode. Development starts from source, Docker uses Compose, and Kubernetes uses Helm.

Run the appropriate start command, check `/healthz`, and use the matching rollback command. This page currently duplicates prerequisites and configuration for all three modes.
