# eval-008-feature-path-mismatch-blocked

This fixture verifies that `feature-implementor` blocks implementation planning when PRD and TRD paths do not describe the same feature.

The PRD uses:

```text
feature_path: chat-interface/history-search
```

The TRD uses:

```text
feature_path: chat-interface
```
