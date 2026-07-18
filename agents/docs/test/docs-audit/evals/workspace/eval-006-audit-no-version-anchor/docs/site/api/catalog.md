---
title: Catalog API
visibility: both
doc_type: api
stage: dev
owners:
  - catalog-team
related_code:
  - src/catalog/routes.txt
last_verified_version: unverified
---

# Catalog API

`GET /catalog/items` is public, accepts no parameters, and returns status 200 with an `items` array. It has no defined error response and does not stream or transfer files.
