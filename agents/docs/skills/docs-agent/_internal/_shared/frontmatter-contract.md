# Default Frontmatter Contract

> Single source of truth owned by `docs-agent` for the default frontmatter
> contract of formal Markdown pages under `docs/site/`.
> `docs-site-bootstrap` consumes it for built-in pages, templates, and the
> validation script delivered to host repositories; `formal-docs-sync` and
> `release-notes-gen` consume it for created or updated pages; and
> `docs-audit` consumes it for frontmatter decisions. Producers and auditors
> must reach the same conclusion for the same page.

The initial rules were migrated from the verified AI Hub implementation for
issue #118. AI Hub is the source and compatibility baseline for this first
version, not a runtime dependency or the long-term owner of the rules.

## Required Fields

All seven fields are unconditionally required.

| Field | Type / Allowed Values | Rule |
| --- | --- | --- |
| `title` | Non-empty string | Human-readable page title. |
| `visibility` | `public`, `internal`, or `both` | Controls public and internal site inclusion. |
| `doc_type` | `landing`, `release`, `design`, `api`, `database`, `ops`, `product`, or `manual` | Selects the page category; no other value is valid. |
| `stage` | `draft`, `dev`, `ops`, or `release` | Records the page lifecycle stage. |
| `owners` | Non-empty array of strings | Identifies the roles or teams responsible for the page. |
| `related_code` | Non-empty array of strings | Defines the code and test evidence scope for every page type. |
| `last_verified_version` | Non-empty string | Stores a version anchor or the literal value `unverified`. |

## Optional Fields

| Field | Type / Allowed Values | Rule |
| --- | --- | --- |
| `nav_order` | Non-negative safe integer (`≤ 9007199254740991`) | Controls the display order of pages inside the same sidebar section. Lower values sort first; pages without `nav_order` fall back to path-slug lexicographic order and sort after any explicit order. Only the immediate section is affected — it never reorders sections, which follow the fixed `SECTION_ORDER`. The safe-integer bound matches the host validator (`Number.isSafeInteger`); larger integers cannot be represented exactly and are rejected. |

Producers set `nav_order` when a section's pages need a business-logic order
that path slugs cannot express (for example, keeping overview pages first or
grouping related feature pages). When a section reads naturally in slug order,
omit `nav_order` and keep the page set minimal.

Before emitting `nav_order`, every producer (including `formal-docs-sync` and
`release-notes-gen`) must confirm the host's delivered navigation generator
supports it: the host `docs/site/scripts/lib/sidebar.mjs` must reference
`nav_order` in its ordering logic. Delivered bootstrap assets are not upgraded
automatically — a host bootstrapped before the `nav_order` capability shipped
would ignore the field while the producer reports an intended sequence. If
host support is missing, do not write `nav_order`; report in the batch summary
that the host must rerun `docs-site-bootstrap` (or merge a confirmed bootstrap
upgrade) before the field can take effect.

## Notes

- `standard` is not a valid `doc_type` value. Standards explanation pages
  (`standards/index.md`, `doc-lifecycle.md`, and `doc-granularity.md`) use
  `doc_type: design`. The descriptive header in
  `standards/change-map.yaml` follows the same `doc_type: design` convention,
  but it is not a formal Markdown page and is outside both
  `check:frontmatter` and docs-audit frontmatter validation. Its structure and
  metadata are validated by the change-map toolchain owned by issue #122,
  matching the AI Hub baseline behavior. Template pages under
  `standards/templates/` follow the AI Hub precedent and use their target
  `doc_type` (`api`, `database`, `design`, `ops`, `product`, or `manual`).
  Template pages participate in internal-page validation, while their
  `doc_type` identifies the target page type represented by the template. They are reusable
  placeholder artifacts, so that target `doc_type` does not make the template
  itself subject to type-specific fact checks.
- `last_verified_version` is always required. Use `unverified` when the page
  has not been verified or no version anchor is available.
- Manual pages use `doc_type: manual` under the independent root
  `docs/site/manual/`, which is peer to the other five formal document types.
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
- `release-notes-gen` must apply this contract to versioned site Release
  Notes and keep `last_verified_version: unverified` until `docs-audit` owns the
  version-stamping sequence.
- `manual-gen` must apply this contract to every illustrated manual page it
  creates or updates, including the `nav_order` host-capability gate.
- `docs-audit` must use this contract for frontmatter decisions. A page with
  invalid frontmatter is `stale`, and a release must not `proceed` while any
  such page remains in scope.
