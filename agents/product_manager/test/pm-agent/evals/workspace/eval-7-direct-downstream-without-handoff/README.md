# Direct Downstream Without Handoff Fixture

This workspace represents a user trying to jump directly into a downstream
role router before PM classification or source documents exist.

The dispatcher or downstream entry gate should return the request to `pm-agent`
instead of starting implementation.
