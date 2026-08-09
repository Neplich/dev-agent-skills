# Test execution record

| Required test | Result | Evidence |
| --- | --- | --- |
| `test_summary_orders_fields` | PASSED | Output follows `language`, `timezone`, `theme`. |
| `test_summary_omits_empty_values` | PASSED | Empty values do not produce field-value pairs. |
| `test_compact_summary_uses_visible_values` | PASSED | Compact output joins the same non-empty ordered pairs. |
