# Test execution record

| Required test | Result | Detail |
| --- | --- | --- |
| `test_summary_orders_fields` | PASSED | Stable field order verified. |
| `test_summary_omits_empty_values` | PASSED | Empty values omitted in standard rendering. |
| `test_compact_summary_handles_empty_values` | FAILED | Compact rendering included an empty `timezone` segment. |

The failed compact-rendering test is part of the confirmed plan and blocks delivery closeout.
