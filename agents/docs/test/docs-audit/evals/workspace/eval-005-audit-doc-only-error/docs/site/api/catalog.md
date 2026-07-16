---
title: Catalog API
visibility: both
doc_type: api
stage: release
owners:
  - catalog-team
related_code:
  - src/catalog/routes.txt
last_verified_version: v1.0.0
---

# Catalog API

`GET /catalog/items` is public and returns status 200 with an `items` array.

`DELETE /catalog/items/{item_id}` removes an item and returns status 204.
