---
title: "Payment Refund TRD"
type: TRD
version: "0.2.0"
status: Approved
author: "Neplich Codex"
date: "2026-06-30"
last_updated: "2026-06-30"
generated_by: "trd-gen"
feature: "payment-refund"
feature_path: "payment-refund"
parent_feature: "N/A"
feature_level: "1"
related_prd: "docs/pm/payment-refund/PRD.md"
---

# Payment Refund TRD

## Implementation

Extend `src/services/refund-service.ts` to compute and validate partial refund
amounts, then wire the new path through `src/routes/refund-route.ts`. A partial
refund amount must be greater than zero and no greater than the remaining
refundable amount; invalid amounts return the existing validation error without
calling the payment provider.

## Impacted Components

| Path | Change |
| --- | --- |
| `src/services/refund-service.ts` | Add remaining-balance validation and partial-refund calculation. |
| `src/routes/refund-route.ts` | Pass the requested partial amount to the service and preserve existing error mapping. |
| `tests/refund-service.test.ts` | Cover valid partial refunds, zero/negative amounts, and amounts above the remaining balance. |

## Verification

Run `npm test -- tests/refund-service.test.ts` and `npm test -- refund-route`.

## Scope Boundary

No UI, database-schema, payment-provider, or full-refund behavior changes are
part of this round.
