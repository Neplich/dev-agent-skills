---
title: "Message History Search TRD"
type: TRD
feature: "search"
feature_path: "chat-interface/messages/history/search"
parent_feature: "chat-interface/messages/history"
feature_level: "4"
version: "1.0.0"
status: Approved
author: "Neplich Codex"
date: "2026-06-25"
last_updated: "2026-06-25"
related_prd: "docs/pm/chat-interface/messages/history/search/PRD.md"
---

# Message History Search TRD

## Technical Overview

The search service receives workspace-scoped candidates, orders higher
relevance scores first, and uses the newest message timestamp to break equal
scores.
