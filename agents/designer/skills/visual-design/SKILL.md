---
name: visual-design
description: "Create and apply coherent visual systems using product context, reusable design data, typography, color, spacing, and interaction feedback."
---

# Visual Design

Start with the product's audience, tasks, information density, brand, and
existing interface. Select a coherent visual direction and explain how it
supports the user experience. Preserve useful established conventions.

## Build the system

- Choose a layout and style suited to the content and interaction frequency.
- Define brand, neutral, and semantic colors with readable contrast and clear
  state meaning. Pair status color with text or symbols.
- Choose typography by language coverage, reading density, and product tone;
  define roles, size, line height, weight, and numeric treatment.
- Establish spacing, alignment, component shape, elevation, and interaction
  feedback that create a consistent hierarchy.
- Include loading, empty, error, focus, pressed, disabled, and success states.
  Adapt layouts to content and the project's target devices.
- Apply the system to the requested specification, prototype, or interface.
  Inspect rendered results and relevant interactions for implementation work.

## Reference library

Read the references that help the current design:

- [System outline](./references/design-system-framework.md)
- [Product patterns](./references/product-patterns.md)
- [Style patterns](./references/style-patterns.md)
- [Color palettes](./references/color-palettes.md)
- [Typography](./references/typography-pairings.md)
- [Quality checks](./references/ux-quality-rules.md)
- [Focused design practices](./references/anti-patterns.md)
- [Searchable design data](./references/design-system-data/README.md)

The local database includes product, style, color, typography, charts, icons,
UX, and stack guidance. From this Skill directory, for example:

```bash
python3 references/design-system-data/scripts/search.py "analytics dashboard" --design-system --format markdown
python3 references/design-system-data/scripts/search.py "table keyboard" --domain ux --json
```

Use lookup results as reference material and adapt them to the actual product.
Present the selected design, important rationale, and verified artifact.
