# v1.5.0 verified release evidence

- Release scope commit: `abc1500`.
- `src/product/dashboard_limits.ts` sets the supported dashboard limit to 25.
- `deploy/dashboard.env` pins `AI_HUB_IMAGE=registry.example/ai-hub:v1.5.0` and `DASHBOARD_LIMIT=25`.
- `.eval/release-test-results.md` records the product acceptance and runtime configuration checks as passed against `abc1500`.
- v1.5.1 may introduce per-plan limits, but no implementation or release approval exists; it is outside current facts.
