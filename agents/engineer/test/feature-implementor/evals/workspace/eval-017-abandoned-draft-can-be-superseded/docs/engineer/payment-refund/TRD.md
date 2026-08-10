---
title: "Payment Refund TRD"
type: TRD
version: "0.4.0"
status: Approved
author: "Neplich Codex"
date: "2026-07-27"
last_updated: "2026-07-27"
generated_by: "trd-gen"
feature: "payment-refund"
feature_path: "payment-refund"
parent_feature: "N/A"
feature_level: "1"
related_prd: "docs/pm/payment-refund/PRD.md"
---

# Payment Refund TRD

## Implementation

Replace the unfinished refund reason-code round with a refund review workflow.
`src/services/refund-review-service.ts` records a pending review and applies
approve or reject transitions idempotently; `src/routes/refund-review-route.ts`
uses the existing authorization and validation error shapes. No refund is sent
to the payment provider until an authorized approval succeeds.

## Impacted Components

| Path | Change |
| --- | --- |
| `src/services/refund-review-service.ts` | Create pending reviews and apply idempotent approve/reject transitions. |
| `src/routes/refund-review-route.ts` | Expose review actions through existing authorization and validation patterns. |
| `tests/refund-review-service.test.ts` | Cover pending creation, approval, rejection, duplicate actions, and unauthorized actions. |

## Verification

Run `npm test -- tests/refund-review-service.test.ts` and
`npm test -- refund-review-route`.

## Scope Boundary

No frontend UI, payment-provider integration, or shipped full-refund behavior
changes are part of this round.
