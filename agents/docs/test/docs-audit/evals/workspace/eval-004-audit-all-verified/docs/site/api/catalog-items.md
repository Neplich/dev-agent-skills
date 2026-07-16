---
title: Catalog Items API
visibility: both
doc_type: api
stage: release
owners:
  - catalog-team
related_code:
  - src/catalog/routes.txt
last_verified_version: v1.0.0
---

# Catalog Items API

`GET /catalog/items` is public and accepts no parameters. It returns status 200 with an `items` array and has no defined error response. It does not stream or transfer files.
