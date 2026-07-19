---
title: Catalog Status API
visibility: internal
doc_type: api
stage: release
owners:
  - catalog-team
related_code:
  - src/catalog/routes.txt
last_verified_version: unverified
---

# Catalog Status API

`GET /catalog/status` requires a service token, returns status 200 with
`{"status": "ready"}`, and returns a 401 `unauthorized` error without one.
