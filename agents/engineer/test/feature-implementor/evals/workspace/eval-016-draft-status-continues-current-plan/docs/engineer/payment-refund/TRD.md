---
title: "Payment Refund TRD"
type: TRD
version: "0.3.0"
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

Extend `src/services/refund-service.ts` and `src/routes/refund-route.ts` with a
typed refund reason code. Reject missing or unsupported codes through the
existing request-validation path before the provider call, and keep full and
partial refund amount behavior unchanged.

## Impacted Components

| Path | Change |
| --- | --- |
| `src/services/refund-service.ts` | Carry a validated reason code into the existing refund request. |
| `src/routes/refund-route.ts` | Validate the reason-code input using the existing request error shape. |
| `tests/refund-service.test.ts` | Cover accepted, missing, and unsupported reason codes. |

## Verification

Run `npm test -- tests/refund-service.test.ts` and `npm test -- refund-route`.

## Scope Boundary

No UI, provider, database-schema, or shipped full-refund behavior changes are
part of this round.
