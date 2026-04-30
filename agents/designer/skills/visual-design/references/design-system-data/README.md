# Design System Data Reference Database

This directory stores the local design database and design-system lookup scripts for `visual-design` reasoning.

The data design references ui ux pro max: product categories, style patterns, color palettes, typography pairings, UX guidelines, charts, landing patterns, icons, and stack guideline dimensions are organized here under this repository's own path.

This directory does not carry a separate license file. License management follows the repository root `LICENSE`.

## Included

- `data/` - CSV design database, including product types, colors, styles, typography, UX guidelines, charts, landing patterns, icons, and stack guideline data.
- `scripts/` - BM25 search and design-system generator scripts.

## Local Usage Boundary

This repository uses the database for `visual-design` design reasoning only.

Allowed:

- Run design-system lookup to choose product pattern, style direction, colors, typography, key effects, and anti-patterns.
- Search product, style, color, typography, UX, chart, and landing references as design evidence.
- Save raw lookup output as eval diagnostics when needed.

Forbidden:

- Generate application code.
- Emit Tailwind config, CSS variables, React/Vue/SwiftUI components, shadcn install commands, or implementation checklists in final design artifacts.
- Treat stack-specific code examples as implementation instructions.

Final `visual-design` output must remain a Markdown design handoff under `docs/design/{feature-name}/visual-system.md`.
