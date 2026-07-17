# Default Frontmatter Contract

> Single source of truth owned by `docs-agent` for the default frontmatter
> contract of formal documentation pages.
> `docs-site-bootstrap` consumes it for built-in pages, templates, and the
> validation script delivered to host repositories; `formal-docs-sync`
> consumes it for created or updated pages; `docs-audit` consumes it for
> frontmatter decisions. Producers and auditors must reach the same conclusion
> for the same page.

The initial rules were migrated from the verified AI Hub implementation for
issue #118. AI Hub is the source and compatibility baseline for this first
version, not a runtime dependency or the long-term owner of the rules.

## Required Fields

All seven fields are unconditionally required.

| Field | Type / Allowed Values | Rule |
| --- | --- | --- |
| `title` | Non-empty string | Human-readable page title. |
| `visibility` | `public`, `internal`, or `both` | Controls public and internal site inclusion. |
| `doc_type` | `landing`, `release`, `design`, `api`, `database`, `ops`, or `product` | Selects the page category; no other value is valid. |
| `stage` | `draft`, `dev`, `ops`, or `release` | Records the page lifecycle stage. |
| `owners` | Non-empty array of strings | Identifies the roles or teams responsible for the page. |
| `related_code` | Non-empty array of strings | Defines the code and test evidence scope for every page type. |
| `last_verified_version` | Non-empty string | Stores a version anchor or the literal value `unverified`. |

## Notes

- `standard` is not a valid `doc_type` value. Standards and writing-guidance pages use
  `doc_type: design`, following the AI Hub precedent.
- `last_verified_version` is always required. Use `unverified` when the page
  has not been verified or no version anchor is available.
- `last_verified_version` records the version against which the page content
  was verified; it does not describe release status. The stamping sequence is
  owned by `docs-audit`.
- Additional fields such as `layout` are allowed and are outside this
  contract.

## Consumers

- `docs-site-bootstrap` must apply this contract to built-in pages, templates,
  and the host validation script it delivers.
- `formal-docs-sync` must apply this contract whenever it creates or updates a
  formal documentation page.
- `docs-audit` must use this contract for frontmatter decisions. A page with
  invalid frontmatter is `stale`, and a release must not `proceed` while any
  such page remains in scope.
