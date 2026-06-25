---
title: "Message History Search TRD"
type: TRD
feature: "search"
feature_path: "chat-interface/messages/history/search"
parent_feature: "chat-interface/messages/history"
feature_level: "4"
related_prd: "docs/pm/chat-interface/messages/history/search/PRD.md"
date: "2026-06-25"
last_updated: "2026-06-25"
---

# Message History Search TRD

The implementation reads `SEARCH_API_KEY` and `SEARCH_INDEX_NAME` at runtime.
Deployment must provide both variables in local, Docker, Helm, and CI/CD
environments.
