# Nested Feature Path Fixture

This fixture represents an existing project with approved PM PRDs for
`chat-interface`, `chat-interface/messages`, and
`chat-interface/messages/history`. The eval asks `idea-to-spec` to add message
history search as a child feature and verifies that the PM path resolves to
`chat-interface/messages/history/search` instead of a parallel top-level or
truncated folder.
