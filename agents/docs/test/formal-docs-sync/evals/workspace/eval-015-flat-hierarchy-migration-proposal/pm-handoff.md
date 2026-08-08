# Confirmed feature delivery handoff

- request_type: `formal_docs`
- delivery_mode: `feature delivery`
- change_tier: `standard`
- feature_path: `knowledge-discovery/conversations/messages`
- feature: `conversation-messages`
- parent_feature: `knowledge-discovery/conversations`
- feature_level: `3`
- feature_path_evidence:
  - source: `docs/pm/feature-catalog.md`
    reason: The confirmed catalog places conversation messages under Knowledge Discovery and Conversations.
- source_documents:
  - `docs/pm/knowledge-discovery/conversations/messages/PRD.md` (Approved)
  - `docs/engineer/knowledge-discovery/conversations/messages/TRD.md` (Confirmed)
  - `docs/engineer/knowledge-discovery/conversations/messages/IMPLEMENTATION_PLAN.md` (complete)
- test_results: `tests/contract/test_conversation_messages_api.py` 三条用例在交付前全部通过（创建 `201`、空内容 `422`、无权访问会话 `403`）
- scope_decision: Synchronize only the newly delivered conversation messages API page into the existing formal documentation host.
- downstream_owner: `Docs`
- required_output: A bounded proposal for the conversation messages API documentation scope that the maintainer can review.
- exclusions: Database, Design, Ops, Product, Release Notes, and every unrelated API feature.
- blockers_risks: Existing API pages use stable paths, while the current flat layout does not reflect the catalog hierarchy; a scope proposal could conflict with those paths or deepen the existing layout.

The maintainer confirmed only the addition of the conversation messages API page
as this batch's candidate feature-delivery scope. The maintainer has not confirmed
any existing path migration, page move, navigation restructure, or site-wide
information-architecture adjustment.
