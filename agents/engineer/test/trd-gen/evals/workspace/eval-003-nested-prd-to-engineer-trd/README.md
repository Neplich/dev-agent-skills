# eval-003-nested-prd-to-engineer-trd

This fixture verifies that `trd-gen` mirrors a nested PM feature path when producing an Engineer TRD.

The expected output path is:

```text
docs/engineer/chat-interface/history-search/TRD.md
```

The fixture intentionally contains only the PM PRD so the skill must derive the Engineer output path from `feature_path`.
