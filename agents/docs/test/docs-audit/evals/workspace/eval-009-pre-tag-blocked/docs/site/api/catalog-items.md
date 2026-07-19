---
title: Catalog Items API
visibility: both
doc_type: api
stage: release
owners:
  - catalog-team
related_code:
  - src/catalog/routes.txt
last_verified_version: v1.1.0
---

# Catalog Items API

`GET /catalog/items` is public. It requires the nonblank `locale` query
parameter, accepts an optional `limit` with default 20 and maximum 100, and
returns status 200 with an `items` array.
