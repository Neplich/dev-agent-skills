# Design Sync Instructions

Load this module only when a confirmed write scope or an explicitly requested
read-only candidate-planning scope contains `doc_type: design`.

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

Derive the hierarchy from stable system / domain / subsystem / component
ownership, then corroborate it with `feature_path`, TRD impact scope, final
code, and tests. Do not derive pages from file count.

- `docs/site/design/index.md` is only the system map, domain boundaries, and
  global navigation.
- Give every domain and non-leaf design node an `index.md` that states
  responsibility, non-goals, children, adjacent modules, and authority
  evidence without repeating child content.
- Separate independently owned components from cross-component control/data
  flows and from security, authorization, error-ownership, or recovery
  boundaries when each has an independent reader task or maintenance cycle.
- Keep one authority page for a cross-domain capability and link to it from
  other domains.
- Every component page links its participating flows; every flow page links
  back to all participating components. Link authoritative API and Database
  pages rather than repeating complete paths, payloads, fields, or constraints.
  When the confirmed Database scope preserves an existing stable feature-level
  authority or compatibility page, each participating component page and the
  flow page link that stable page directly. Links to a nested data-domain,
  relationship, or entity page are additional detail and never replace the
  stable Database authority link. Verify both categories during read-back just
  as feature-level and entity-specific API links are verified separately.

For the candidate scope, show the complete parent-child tree and, per page,
reader task, owner, evidence, code glob, change-map delta, links, and
exclusions. Use a real code map and Mermaid flow only where final code and
tests support them. Apply the Design Delivery Closeout Gate page by page and
show the required page-by-seven-item matrix before writing; each cell names its
evidence and pass/fail status, so a feature-level summary cannot substitute for
page-level closeout. Preserve the common gate's runtime-only pre-write matrix
and changed-path snapshot before touching any formal page or map; the final
report may summarize it but cannot replace that ordering evidence.

For every Design `code_glob`, list the complete atomic mapping closure in
`required_docs`: each affected leaf or compatibility page, the Design root and
every changed domain/subsystem ancestor `index.md` needed to reach it, plus the
pages whose reciprocal links change. When a mapped component participates in a
cross-component flow, its closure also includes the API and Database authority
pages linked by that flow; each participating code glob carries this closure
independently rather than relying on another glob's union.

In a confirmed Database + Design atomic scope, every participating code glob's
own `required_docs` must contain both complete closures: the changed Design root
and all changed Design ancestor indexes, and the changed Database root,
database/schema root, data-domain index, relationship page, affected entity or
compatibility pages, reciprocal-link pages, and Database/API authority pages.
Build and verify this checklist separately for invitation, repository/schema,
service, audit, and any broad feature glob in scope. This explicitly includes
`src/audit/**`: do not reduce that row to Design pages plus a single Database
authority page merely because the audit source does not query the database.
Shared ancestors may and must repeat across mappings; a complete broad feature
glob never fills a gap in an exact glob. Check each glob before writing and
again after reading the map back. Treat that closure, its navigation/link
delta, and its change-map entry as one atomic scope. A failed page row changes
none of those surfaces but does not block independently evidenced pages. Never
place a blocked page's future design in another page.
