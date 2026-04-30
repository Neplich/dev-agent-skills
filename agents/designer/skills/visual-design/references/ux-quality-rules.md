# UX Quality Rules

Use these as visual-system quality checks.

## Critical

- Accessibility: contrast 4.5:1 for normal text, visible focus states, labels for icon-only actions.
- Touch and interaction: primary targets at least 44px on touch devices, pressed/disabled/loading states defined.
- Responsive: mobile-first priority, no horizontal scroll, content hierarchy preserved at 375px, 768px, 1024px, and 1440px.

## High

- Data readability: legends, tooltips, labels, and status text; never rely on color alone.
- Navigation: current location is visible; back behavior is predictable; destructive paths have escape routes.
- Forms and feedback: inline errors near fields, empty states explain next action, long waits use skeleton/progress.

## Medium

- Motion: 150-300ms for micro-interactions, reduced-motion alternative, no decorative motion that blocks input.
- Density: compact surfaces need enough spacing to prevent misreads; spacious surfaces should not hide core actions.
- Consistency: one icon style, one elevation scale, one radius scale unless a documented exception exists.
