---
feature: ai-hub-runtime
feature_path: ai-hub-runtime
parent_feature: null
feature_level: 1
version: 1.0.0
date: 2026-07-17
last_updated: 2026-07-17
status: Confirmed
related_code:
  - deploy/compose.yaml
---

# AI Hub Runtime TRD

The supported deployment surface is the `app` service in `deploy/compose.yaml`. Operations require a container health check, an image-variable upgrade path, and a pinned-image rollback path.
