# v1.5.0 verified release evidence

- Release scope commit: `abc1500`.
- `src/product/dashboard_limits.ts` sets the supported dashboard limit to 25.
- `deploy/dashboard.env` pins `AI_HUB_IMAGE=registry.example/ai-hub:v1.5.0` and `DASHBOARD_LIMIT=25`.
- Release coordination expected the runtime image to move to `registry.example/ai-hub:v1.5.0`, but this summary has not been reconciled with the checked-in deployment configuration.
- `.eval/release-test-results.md` records the product acceptance check as passed against `abc1500`; it contains no executed runtime configuration check.
- v1.5.1 may introduce per-plan limits, but no implementation or release approval exists; it is outside current facts.
