---
name: visual-design
description: Use when the user needs a visual design system, aesthetic direction, color, typography, component styling, copy tone, or reference-backed UI quality rules before engineering implementation.
---

## Hard Boundaries

This skill defines a visual system only.

Allowed actions:
- Read PM docs and existing design docs
- Read internal visual-design references for design-system reasoning
- Run the local `references/design-system-data/scripts/search.py` helper for design-system lookup and reference search
- Choose a product-appropriate aesthetic direction and justify it
- Define color, typography, spacing, component, and copy guidelines
- Write or update `docs/design/{feature-name}/visual-system.md`

Forbidden actions:
- Writing or modifying source code, tests, design tokens in code, configs, or deployment files
- Emitting implementation plans, code snippets for production use, shell commands, install commands, or engineer task lists
- Generating Tailwind config, CSS variables, React/Vue/SwiftUI components, shadcn commands, or file-by-file implementation instructions
- Calling Engineer skills or continuing into implementation after the visual system is complete

If the input includes a completed PM or UX spec, use it to shape the visual system and stop at design handoff.

## Execution Steps

### Step 1: Gather Context

1. **Read PM documents**:
   - BRD: brand tone, target audience, business goals
   - PRD: product type and features
   - DECISIONS: confirmed design constraints and trade-offs
   - TRD: platform constraints that affect presentation choices
   - UI/UX spec (if exists): component list

2. **Extract design-system inputs**:
   - Product type and domain
   - Target users and usage context
   - Brand tone and trust requirements
   - Platform and device constraints
   - Data density, workflow complexity, and accessibility risks

### Step 2: Read Internal References

Use the local Design System Data database first, then use local Markdown references for boundary and synthesis rules.

Primary reference database:

- `references/design-system-data/data/` - full CSV design database managed under this skill
- `references/design-system-data/scripts/search.py` - BM25 search and design-system output helper
- `references/design-system-data/README.md` - data notes and local no-code usage boundary

For design-system generation, run the helper from the repository root as internal analysis:

```bash
uv run python agents/designer/skills/visual-design/references/design-system-data/scripts/search.py "<product type> <industry> <keywords>" --design-system -p "<Project Name>" -f markdown
```

For focused lookup, use domains such as `product`, `style`, `color`, `typography`, `ux`, `chart`, or `landing`:

```bash
uv run python agents/designer/skills/visual-design/references/design-system-data/scripts/search.py "enterprise analytics dashboard" --domain product
```

Supplementary local references:

- `references/design-system-framework.md` - output model and required reasoning fields
- `references/product-patterns.md` - product category to pattern mapping
- `references/style-patterns.md` - style direction selection rules
- `references/color-palettes.md` - product-aware color systems
- `references/typography-pairings.md` - font pairing options by tone and data density
- `references/ux-quality-rules.md` - visual UX quality checklist
- `references/anti-patterns.md` - forbidden generic or implementation-oriented output

Reference outputs are evidence for design choices only. Do not copy raw CSV rows, CSS imports, Tailwind snippets, code examples, stack implementation guidance, or install commands into the final design artifact. Synthesize a focused recommendation for the feature.

### Step 3: Classify Product and Design Risk

Choose the closest product category, then record the reason.

Examples:
   - SaaS dashboard → professional, clean
   - E-commerce → vibrant, trustworthy
   - Content platform → readable, engaging
   - Mobile app → touch-friendly, simple
   - Enterprise analytics → data-dense, trustworthy, highly scannable
   - Fintech → conservative trust, clear status colors, low ambiguity
   - Healthcare → calm, accessible, human, error-resistant

If the category is ambiguous, choose the safest adjacent category and list the assumption in the output.

### Step 4: Choose Aesthetic Direction

If the user gave a style preference, validate it against the product category and note any trade-off. If no style preference is provided, infer the style from the references and product context.

Ask one concise clarification only when the style choice would materially change the result:

```
Question: "What aesthetic direction fits your product best?"
Options:
- "Minimalist" - Clean, spacious, restrained
- "Bold/Brutalist" - Strong typography, high contrast
- "Playful" - Rounded corners, bright colors
- "Professional" - Corporate, trustworthy
- "Modern/Tech" - Gradients, glassmorphism
- "Let the AI decide based on product type"
```

Avoid generic patterns:
- AI-purple/blue gradients unless they are explicitly brand-appropriate
- Defaulting to Inter/Roboto unless matching an existing product system
- Generic rounded cards everywhere
- Decorative motion without UX purpose
- Low-contrast gray-on-gray interfaces

Prefer:
- Product-specific style selection
- Purposeful color roles
- Distinctive but readable font pairings
- Explicit anti-patterns to avoid
- Accessibility and data readability checks

### Step 5: Generate Reference-Driven Design System

Create a compact design-system recommendation from the Design System Data design-system output before detailing visual rules:

```markdown
## 1. Reference-Driven Design System

- Product category: [category]
- Recommended pattern: [layout / product pattern]
- Style direction: [primary style + optional secondary style]
- Design rationale: [why this fits audience, domain, risk]
- Key effects: [motion/elevation/feedback rules, if useful]
- Avoid: [top anti-patterns for this product]
- Source references: [which Design System Data domains influenced the choice]
```

### Step 6: Define Color System

Create a purposeful color palette:

```markdown
## Color System

### Primary Colors
- Primary: #[hex] - Main brand color
- Primary Dark: #[hex] - Hover/active states
- Primary Light: #[hex] - Backgrounds

### Semantic Colors
- Success: #[hex] - Confirmations, success states
- Warning: #[hex] - Warnings, cautions
- Error: #[hex] - Errors, destructive actions
- Info: #[hex] - Information, neutral feedback

### Neutral Colors
- Text Primary: #[hex] - Main text (ensure 4.5:1 contrast)
- Text Secondary: #[hex] - Secondary text
- Border: #[hex] - Dividers, borders
- Background: #[hex] - Page background
- Surface: #[hex] - Card/panel background
```

Include light/dark mode guidance only when relevant. Accessibility: Ensure WCAG AA contrast ratios (4.5:1 for text, 3:1 for UI elements).


### Step 7: Define Typography System

Choose font pairings that match product tone and reading density:

```markdown
## Typography

### Font Families
- Heading: [Font Name] - Display/headings
- Body: [Font Name] - Body text, UI
- Mono: [Monospace Font] - Code, technical content

### Font Scale
- Display: 48px / 56px line-height / 700 weight
- H1: 36px / 44px / 700
- H2: 30px / 38px / 600
- H3: 24px / 32px / 600
- H4: 20px / 28px / 600
- Body Large: 18px / 28px / 400
- Body: 16px / 24px / 400
- Body Small: 14px / 20px / 400
- Caption: 12px / 16px / 400
```


### Step 8: Define Spacing System

```markdown
## Spacing Scale

Based on 8px grid:
- xs: 4px
- sm: 8px
- md: 16px
- lg: 24px
- xl: 32px
- 2xl: 48px
- 3xl: 64px
```

### Step 9: Define Component Styles

```markdown
## Component Styles

### Buttons
- Primary: [background] [text color] [padding] [border-radius]
- Secondary: [styles]
- Ghost: [styles]
- Sizes: sm (32px), md (40px), lg (48px)

### Input Fields
- Border: [color] [width]
- Focus: [border color] [shadow]
- Error: [border color]
- Height: 40px (md), 48px (lg)

### Cards
- Background: [color]
- Border: [style]
- Shadow: [elevation]
- Padding: [spacing]
- Border radius: [value]
```


### Step 10: Define UX Quality Rules

Document visual UX quality rules that Engineer and QA can later verify without turning this skill into implementation:

```markdown
## UX Quality Rules

- Accessibility: [contrast, focus, text scaling]
- Interaction states: [hover, pressed, disabled, loading]
- Responsive behavior: [mobile/tablet/desktop priorities]
- Data readability: [tables/charts/status colors if relevant]
- Feedback: [empty/error/success/loading states]
```

### Step 11: Define Anti-patterns to Avoid

Include product-specific anti-patterns:

```markdown
## Anti-patterns to Avoid

- [anti-pattern] - [why it is wrong for this product]
- [anti-pattern] - [risk]
```

### Step 12: Define Copy Guidelines

```markdown
## Copy & Tone Guidelines

### Voice & Tone
Based on product type:
- SaaS: Professional, helpful, clear
- Consumer: Friendly, approachable, conversational
- Enterprise: Authoritative, precise, formal

### Button Labels
- Primary actions: "Get Started", "Create Account", "Save Changes"
- Secondary: "Learn More", "Cancel", "Go Back"
- Avoid: "Click Here", "Submit"

### Empty States
- Encouraging: "No items yet. Create your first one!"
- Helpful: "Upload files to get started"

### Error Messages
- Clear: "Email is required"
- Helpful: "Password must be at least 8 characters"
- Avoid: "Error 400", "Invalid input"

### Success Messages
- Specific: "Profile updated successfully"
- Actionable: "Email sent! Check your inbox"
```


### Step 13: Generate Output Document

Create `docs/design/{feature-name}/visual-system.md` with this structure:

```markdown
# Visual Design System

## 1. Reference-Driven Design System
[Product category, recommended pattern, style direction, rationale, key effects, avoid list]

## 2. Color System
[Primary, semantic, neutral colors with hex codes]

## 3. Typography
[Font families, scale, weights]

## 4. Spacing
[8px grid scale]

## 5. Component Styles
[Buttons, inputs, cards, etc.]

## 6. UX Quality Rules
[Accessibility, states, responsive, data readability, feedback rules]

## 7. Anti-patterns to Avoid
[Product-specific anti-patterns and risks]

## 8. Copy Guidelines
[Voice, tone, examples]

## Design Handoff
Designer stops here. Next role: `engineer-agent`.
```

## Quality Checklist

- [ ] Colors meet WCAG AA contrast requirements
- [ ] Font choices are product-appropriate and not generic defaults unless justified
- [ ] Spacing follows consistent scale
- [ ] Component styles are complete
- [ ] Copy guidelines match brand tone
- [ ] Product category and style rationale are explicit
- [ ] Design System Data design-system lookup was used when available
- [ ] UX quality rules cover accessibility, responsive behavior, and feedback states
- [ ] Anti-patterns are product-specific
- [ ] Output contains no code, shell commands, config snippets, CSS imports, install commands, or engineer task list

## Completion Criteria

This skill is complete only when:
- `docs/design/{feature-name}/visual-system.md` has been written or updated
- The final response summarizes the visual system deliverable and its file location
- The workflow stops at design handoff

After completion:
- Do not propose code changes
- Do not generate implementation steps
- If implementation is required, tell the user to invoke `engineer-agent`

## Output Location

Write to: `docs/design/{feature-name}/visual-system.md`
