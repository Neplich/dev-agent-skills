# Design Sync Instructions

Load this module only when the confirmed scope contains `doc_type: design`.

## Evidence Checks

In feature-delivery mode, first pass the common Design Delivery Closeout Gate.
Then use final code and passing tests to verify, as applicable:

- owned capability, explicit non-goals, and adjacent-module boundaries;
- real entry points, orchestration, domain/data access, and test locations;
- end-to-end control and data flow;
- directly owned state, configuration, interfaces, and compatibility limits;
- authorization, sensitive-data, error ownership, timeout, retry, and recovery
  behavior;
- regression tests supporting each material design claim.

Approved design intent alone is not evidence of delivered current state. Do
not publish future architecture, unfinished implementation, or option analysis.

## Template and Output Rules

Read the design template linked from the host standards entry—normally
`docs/site/standards/templates/feature-design.md`—and consume its single
`docs-scaffold` block for a new page. Do not copy the template into this skill.

Use a real code map and Mermaid flow only where final code and tests support
them. Link authoritative API and database pages instead of duplicating their
full contracts. Treat each design page and its design change-map entry as one
atomic scope; a failed closeout gate changes neither.
