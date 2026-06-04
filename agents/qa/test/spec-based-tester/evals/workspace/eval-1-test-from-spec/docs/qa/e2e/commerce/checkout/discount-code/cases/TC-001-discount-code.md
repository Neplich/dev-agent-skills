# TC-001 Discount Code

## Basic Info

- Feature directory: `docs/qa/e2e/commerce/checkout/discount-code/`
- Scenario: `feature-update`
- Platform version: `v0.3.0-dev`

## Assertions

- One eligible discount code applies during checkout.
- Expired codes are rejected before payment submission.
- Original subtotal is preserved when validation fails.
