# Design System Data Reference Database

This directory contains the local design database and lookup tools used by
`visual-design`. Its reference organization draws on ui ux pro max and brings
product, visual, interaction, and stack guidance together under this repository.

## Contents

```text
design-system-data/
  data/
    products.csv
    styles.csv
    colors.csv
    typography.csv
    ux-guidelines.csv
    charts.csv
    landing.csv
    icons.csv
    stacks/
  scripts/
    search.py
    core.py
    design_system.py
```

The CSV collection also includes font, interface, and framework-specific
references. `core.py` provides BM25 search support, `search.py` exposes the CLI,
and `design_system.py` combines matches into a design-system recommendation.

## Search by Topic

Run these commands from this directory:

```bash
python3 scripts/search.py "analytics dashboard" --domain product
python3 scripts/search.py "table keyboard navigation" --domain ux --json
python3 scripts/search.py "financial dashboard" --domain color --max-results 5
python3 scripts/search.py "editorial headings" --domain typography
python3 scripts/search.py "rendering performance" --stack react
```

Domains cover style, color, charts, landing pages, products, UX, typography,
icons, React, web, and Google Fonts. Stack search includes web, mobile, and
platform frameworks; `--help` lists the values supported by the current CLI.

## Generate a Design-System Suggestion

```bash
python3 scripts/search.py "enterprise analytics dashboard" --design-system --format markdown
python3 scripts/search.py "healthcare appointment booking" --design-system --project-name "Clinic"
```

Use the result to compare product patterns, style direction, palettes,
typography, and feedback choices. Tie the selected direction to actual users,
information density, brand, and interaction needs.

## Save Reusable Output

When a durable reference is useful:

```bash
python3 scripts/search.py "analytics dashboard" --design-system --persist --project-name "Analytics"
python3 scripts/search.py "analytics settings" --design-system --persist --page "settings"
```

Persistence creates a master design reference and optional page-specific
material under `design-system/`. `--output-dir` selects the output location.
Keep useful final artifacts and remove task-only diagnostics after use.

## Apply the Findings

Use the data for a design document, prototype, or implemented interface.
Inspect the actual layout, contrast, typography, states, and responsive behavior.
Treat lookup matches as reference material and verify stack-specific guidance
against the project's current dependencies and conventions.

The surrounding [visual-design Skill](../../SKILL.md) links palettes, patterns,
typography, and quality references that complement the database.
