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

`GET /catalog/items` accepts optional query parameter `limit` with a default of 20 and maximum of 100. It returns status 200 with an `items` array. An invalid limit returns status 400 with code `invalid_limit`. The route is public and does not stream or transfer files.
