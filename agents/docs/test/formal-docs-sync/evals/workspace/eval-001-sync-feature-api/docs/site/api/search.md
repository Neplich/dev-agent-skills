---
title: Search API
visibility: both
doc_type: api
stage: dev
owners:
  - search-team
related_code:
  - src/api/search.py
last_verified_version: v0.8.0
---

# Search API

`POST /v1/find` accepts a JSON body containing `term` and always returns an array.

Errors are not currently defined.
