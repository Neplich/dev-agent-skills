# Searchable Design References

This directory contains local CSV references and BM25 search tools for product
patterns, styles, colors, typography, UX, charts, landing pages, icons, and
framework-specific guidance. The reference organization draws on ui ux pro max.

## Contents

- `data/`: design and stack reference datasets.
- `scripts/search.py`: domain and stack search, plus design-system suggestions.
- `scripts/core.py`: search support.
- `scripts/design_system.py`: design-system synthesis and optional persistence.

From this directory:

```bash
python3 scripts/search.py "analytics dashboard" --design-system --format markdown
python3 scripts/search.py "forms" --domain ux --json
python3 scripts/search.py "rendering" --stack react --max-results 3
```

Use the results to inform the requested design document, prototype, or working
interface. Validate their suitability against the product and current stack.
The CLI's `--help` describes supported domains, stacks, and optional output
persistence. Keep only the outputs useful to the requested task.
