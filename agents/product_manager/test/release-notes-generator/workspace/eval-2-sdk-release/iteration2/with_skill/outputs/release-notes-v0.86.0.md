# Release Notes — v0.86.0 (2026-03-18)

> Persistent memory tools for Claude agents, richer model capability metadata from `/v1/models`, and two async error-handling fixes.

## ✨ What's New

### Filesystem Memory Tools (Beta)

Claude agents can now persist and retrieve information across conversations using a local filesystem-backed memory tool. `BetaLocalFilesystemMemoryTool` implements the `memory` server tool, handling all read/write operations on disk so Claude can store facts, preferences, and context between sessions without you managing storage manually.

**Quick start:**

```python
from anthropic import Anthropic
from anthropic.tools import BetaLocalFilesystemMemoryTool

client = Anthropic()
memory = BetaLocalFilesystemMemoryTool()  # stores to local filesystem by default

runner = client.beta.messages.tool_runner(
    model="claude-sonnet-4-20250514",
    betas=["context-management-2025-06-27"],
    max_tokens=2048,
    system="Store facts about the user and their preferences.",
    messages=[{"role": "user", "content": "Remember that I prefer concise answers."}],
    tools=[memory],
)

for message in runner:
    for block in message.content:
        if block.type == "text":
            print(block.text)
```

**Custom backend:** Subclass `BetaAbstractMemoryTool` (sync) or `BetaAsyncAbstractMemoryTool` (async) to back memory with your own storage — a database, encrypted files, cloud storage, etc. — by implementing `view`, `create`, `insert`, `str_replace`, `delete`, and `rename`.

Both classes are exported from `anthropic.tools`.

### Model Capabilities via `/v1/models`

The `ModelInfo` object returned by `client.models.list()` and `client.models.retrieve()` now includes a `capabilities` field describing what each model supports. You can now introspect at runtime instead of hardcoding per-model logic:

```python
model = client.models.retrieve("claude-sonnet-4-20250514")

caps = model.capabilities
print(caps.thinking.supported)          # True/False
print(caps.effort.high.supported)       # True/False — reasoning_effort="high"
print(caps.batch.supported)             # True/False — Batch API
print(caps.image_input.supported)       # True/False
print(caps.structured_outputs.supported)  # True/False
```

Available capability fields: `batch`, `citations`, `code_execution`, `context_management`, `effort` (with `low`/`medium`/`high`/`max` levels), `image_input`, `pdf_input`, `structured_outputs`, `thinking`.

## 🐛 Bug Fixes

**Async client now raises correct error types for HTTP 529 and 413**

The async `AsyncAnthropic` client was falling through to generic error types for two specific HTTP status codes, while the sync `Anthropic` client handled them correctly:

| Status | Before (async) | After (async) |
|--------|---------------|---------------|
| `529` (overloaded) | `InternalServerError` | `OverloadedError` |
| `413` (payload too large) | `APIStatusError` | `RequestTooLargeError` |

If you were catching `InternalServerError` to handle 529 in async code, update to `OverloadedError`. No change needed for the sync client.

**Pydantic serialization: `by_alias` no longer passed when not explicitly set**

`model.model_dump()` was unconditionally passing `by_alias`, which caused unexpected field naming behavior in certain Pydantic v2 configurations. The SDK now only passes `by_alias` when explicitly configured.

**Minimum `typing-extensions` version bumped to `>=4.14`**

The SDK now requires `typing-extensions>=4.14`. If your environment pins an older version, update your dependencies:

```
pip install "typing-extensions>=4.14"
```

## ⚠️ Upgrade Actions

1. **Async error handling:** If you catch `InternalServerError` to handle HTTP 529 (overloaded) in async code, update to `OverloadedError`:
   ```python
   # Before
   except anthropic.InternalServerError as e:
       if e.status_code == 529: handle_overload()

   # After
   except anthropic.OverloadedError:
       handle_overload()
   ```
2. **Dependency pin:** Ensure `typing-extensions>=4.14` in your `requirements.txt` or `pyproject.toml`.

## ⬆️ Upgrading

```
pip install anthropic==0.86.0
```

No breaking changes to existing API call patterns. The `capabilities` field on `ModelInfo` is optional (may be `None` for older model entries).

---
Full changelog: https://github.com/anthropics/anthropic-sdk-python/compare/v0.85.0...v0.86.0
