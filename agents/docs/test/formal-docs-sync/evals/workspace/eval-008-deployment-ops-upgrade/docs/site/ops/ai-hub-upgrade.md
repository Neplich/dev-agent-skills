---
title: AI Hub Runtime and Upgrade
visibility: internal
doc_type: ops
stage: dev
owners:
  - platform-team
related_code:
  - deploy/compose.yaml
last_verified_version: v1.3.0
---

# AI Hub Runtime and Upgrade

Production is managed by Helm. Run `helm upgrade --install` for every environment. Rollback is not documented and the health endpoint is `/ready`.
