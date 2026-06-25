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

## Technical Scope

- Update `src/chat-interface/messages/history/search-service.ts` to apply
  workspace scoping and relevance-plus-recency sorting.
- Add deterministic tests in
  `tests/chat-interface/messages/history/search-service.test.ts`.

## Validation

- `uv run --with pytest pytest agents/test_eval_contract.py`
- Repository-specific TypeScript or unit test command if present in the target
  project fixture.
