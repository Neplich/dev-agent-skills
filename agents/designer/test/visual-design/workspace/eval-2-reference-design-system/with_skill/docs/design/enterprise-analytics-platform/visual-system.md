# Visual Design System

## 1. Reference-Driven Design System

- Product category: Enterprise Analytics Dashboard
- Recommended pattern: Data-Dense Dashboard
- Style direction: Data-Dense + Minimal Trust
- Design rationale: Operations leaders and analysts need fast scanning, reliable comparison, and clear status interpretation. The visual system should reduce decoration, keep data surfaces calm, and reserve emphasis for status, filters, alerts, and primary decisions.
- Key effects: Subtle row hover, focused filter states, restrained elevation for overlays, and short feedback transitions for loading and status updates.
- Avoid: Decorative gradients behind dense data, oversized marketing cards, ambiguous red/green-only status, low-contrast table text, and icon-only actions without labels.
- Source references: Design System Data `product`, `style`, `color`, `typography`, `landing`, and `ux` domains.

## 2. Color System

### Primary Colors

- Primary: #1E40AF - trust blue for primary actions, selected navigation, and key drill-down links
- Primary Dark: #1E3A8A - hover and active states
- Primary Light: #DBEAFE - selected filter chips and quiet highlights
- Secondary: #3B82F6 - secondary actions, linked data labels, and comparative emphasis

### Semantic Colors

- Success: #15803D - healthy status and positive movement
- Warning: #B45309 - degraded status or thresholds needing attention
- Error: #B91C1C - failed state, destructive action, or critical alert
- Info: #2563EB - neutral system information

### Neutral Colors

- Text Primary: #1E3A8A - main text and table values
- Text Secondary: #64748B - secondary labels and metadata
- Border: #DBEAFE - table grid, filters, and panel separation
- Background: #F8FAFC - low-noise workspace background
- Surface: #FFFFFF - cards, tables, and side panels

## 3. Typography

### Font Families

- Heading: Fira Code - precise technical tone for dashboard headings and key metrics
- Body: Fira Sans - readable operational copy and table labels
- Mono: Fira Code - IDs, timestamps, and tabular numeric values only

### Font Scale

- H1: 32px / 40px / 700
- H2: 24px / 32px / 600
- H3: 20px / 28px / 600
- Body: 16px / 24px / 400
- Body Small: 14px / 20px / 400
- Caption: 12px / 16px / 500

## 4. Spacing Scale

- xs: 4px
- sm: 8px
- md: 16px
- lg: 24px
- xl: 32px
- 2xl: 48px

## 5. Component Styles

### Buttons

- Primary: #1E40AF background, white text, 40px height, 6px radius
- Secondary: white background, #DBEAFE border, #1E3A8A text
- Ghost: transparent background, #1E40AF text, visible hover surface
- Destructive: #B91C1C background, white text, confirm-before-commit usage

### Input Fields and Filters

- Height: 40px desktop, 44px touch surfaces
- Border: #DBEAFE 1px
- Focus: #1E40AF border with visible focus ring
- Error: #B91C1C border with inline recovery text

### Tables and Cards

- Tables use quiet borders, sticky headers where helpful, and tabular numeric alignment
- Cards use #FFFFFF surfaces, 1px border, subtle shadow only for layered panels
- Metric cards show label, value, trend, timestamp, and status text when status is meaningful

## 6. UX Quality Rules

- Accessibility: maintain WCAG AA contrast, visible focus states, and labels for icon-only actions.
- Interaction states: define hover, pressed, selected, disabled, loading, empty, and error states for every control family.
- Responsive behavior: prioritize filters, core metrics, and alerts on mobile before secondary charts.
- Data readability: pair status color with text or symbols; legends and tooltips must be explicit.
- Feedback: loading over 300ms uses skeleton or progress; failed refresh includes retry and timestamp context.

## 7. Anti-patterns to Avoid

- Decorative gradients behind tables - they reduce legibility and make status colors harder to parse.
- Oversized marketing cards in the workbench - they waste scanning space for operational users.
- Red/green-only meaning - analysts need labels or symbols for accessibility and auditability.
- Hidden filters on desktop - filtering is a primary analytics action, not secondary navigation.
- Generic rounded-card dashboard styling - it makes every surface feel equally important.

## 8. Copy Guidelines

### Voice and Tone

Precise, operational, and calm. Prefer specific system language over marketing copy.

### Examples

- Buttons: "Apply filters", "Export report", "Acknowledge alert"
- Empty state: "No incidents match these filters. Adjust status or time range."
- Error: "Report refresh failed. Retry or use the last updated data from 09:42."
- Success: "Filters applied. 128 records shown."

## Design Handoff

Designer stops here.
Next role: `engineer-agent`.
