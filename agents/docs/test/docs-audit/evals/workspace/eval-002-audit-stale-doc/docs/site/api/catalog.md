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

`GET /catalog/items` accepts optional query parameter `limit`. It returns status 200 with an `items` array. Blank locale values are not described.
