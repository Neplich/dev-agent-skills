# Product Sync Instructions

Load this module only when the confirmed scope contains `doc_type: product`.

## Evidence Checks

Use current user-facing implementation and acceptance evidence to verify, as
applicable:

- intended user roles, entry points, supported scenarios, and capability
  boundaries;
- current terms, objects, states, and constraints shown by the product;
- the real user flow from entry and configuration through result or recovery;
- role-based visibility, authorization, limits, validation, failure feedback,
  and recovery paths;
- UI, API, integration, acceptance, and E2E evidence for material behavior;
- in release mode, the confirmed version scope for every changed product fact.

Do not turn roadmap scope, a PRD target, or a Release Notes statement into
current product behavior without implementation and test evidence.

## Template and Output Rules

Read the product template linked from the host standards entry—normally
`docs/site/standards/templates/product-handbook.md`—and consume its single
`docs-scaffold` block for a new page. Do not copy the template into this skill.

Write for the confirmed audience and describe existing behavior, constraints,
permissions, failures, and recovery. Link design, API, database, and ops pages
instead of duplicating their contracts. Keep product pages and their
change-map entries in the same confirmed write/read-back scope. Release Notes
content, index, metadata, and navigation remain outside this module and must be
handed to `docs-agent:release-notes-generator`.
