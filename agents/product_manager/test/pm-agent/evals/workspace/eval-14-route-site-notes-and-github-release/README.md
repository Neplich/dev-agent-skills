# Release Communication Routing Fixture

This fixture contains two distinct release communication outcomes for the same
AI Hub-shaped version:

1. a user-facing version page under `docs/site/release-notes/` that does not yet
   exist and therefore needs the Docs writing, confirmation, metadata, index,
   and host-check workflow;
2. a GitHub Release preview requested only after that page has a confirmed
   ready handoff and the required release-audit evidence.

The router must preserve the order and must not collapse both outcomes into a
single PM `release-notes-generator` route.
