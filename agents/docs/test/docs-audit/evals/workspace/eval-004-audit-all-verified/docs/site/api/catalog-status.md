---
title: Catalog Status API
visibility: internal
doc_type: api
stage: release
owners:
  - catalog-team
related_code:
  - src/catalog/routes.txt
last_verified_version: v1.0.0
---

# Catalog Status API

`GET /catalog/status` requires a service token and accepts no parameters. It returns status 200 with `{"status": "ready"}`. Missing authentication returns status 401 with code `unauthorized`. It does not stream or transfer files.
