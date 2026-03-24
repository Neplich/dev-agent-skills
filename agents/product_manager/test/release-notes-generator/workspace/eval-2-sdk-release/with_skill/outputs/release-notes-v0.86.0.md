# Release Notes — v0.86.0 (2026-03-18)

> Filesystem-backed memory tools land in the SDK, the `/v1/models` endpoint now returns structured capability data, and two async error-handling bugs are fixed.

## ✨ What's New

### Filesystem Memory Tools

You can now give Claude persistent, file-based memory across conversations using the built-in `BetaLocalFilesystemMemoryTool` (sync) or `BetaAsyncLocalFilesystemMemoryTool` (async), both exported from `anthropic.tools`.

The tool handles all memory commands (view, create, delete, insert, rename, str_replace) against files on your local filesystem. If you need a different storage backend (database, cloud storage, encrypted files), subclass `BetaAbstractMemoryTool` / `BetaAsyncAbstractMemoryTool` and implement the abstract methods.

```python
from anthropic import Anthropic
from anthropic.tools import BetaLocalFilesystemMemoryTool

client = Anthropic()
memory_tool = BetaLocalFilesystemMemoryTool()

message = client.beta.messages.run_tools(
    model="claude-sonnet-4-5",
    messages=[{"role": "user", "content": "Remember that I prefer concise answers."}],
    tools=[memory_tool],
).until_done()
```

See `examples/memory/basic.py` in the repository for a full working example including context management configuration.

### Model Capabilities via `/v1/models`

The `ModelInfo` object returned by the Models API now includes an optional `capabilities` field of type `ModelCapabilities`. This structured object lets you programmatically inspect what a given model supports before making API calls:

- `batch` — Batch API support
- `citations` — Citation generation
- `code_execution` — Code execution tools
- `context_management` — Available context management strategies
- `effort` — `reasoning_effort` support and available levels
- `image_input` / `pdf_input` — Multimodal input support
- `structured_outputs` — JSON mode / strict tool schemas
- `thinking` — Extended thinking support and type configurations

```python
model_info = client.models.retrieve("claude-sonnet-4-5")
if model_info.capabilities and model_info.capabilities.thinking.type == "enabled":
    # use extended thinking
    ...
```

## 🐛 Bug Fixes

### Async client now raises the correct error types for HTTP 529 and 413

The async client (`AsyncAnthropic`) was silently falling back to generic base-class exceptions for two specific HTTP status codes that the sync client already handled correctly:

- **HTTP 529** raised `InternalServerError` instead of `OverloadedError`
- **HTTP 413** raised `APIStatusError` instead of `RequestTooLargeError`

If your async error-handling code catches `OverloadedError` or `RequestTooLargeError`, it will now work as expected without needing to fall back to catching the parent class.

### Pydantic serialization: `by_alias` no longer passed when not explicitly set

`by_alias` is no longer forwarded to Pydantic's serialization methods unless you explicitly set it. This prevents unexpected field-name aliasing in serialized output for users who rely on default (non-alias) field names.

### Minimum `typing-extensions` version bumped

The minimum required version of `typing-extensions` has been raised to ensure compatibility with newer type constructs used internally by the SDK. If you see a dependency conflict after upgrading, run `pip install --upgrade typing-extensions`.

## ⬆️ Upgrading

```bash
pip install anthropic==0.86.0
```

No breaking changes in this release. The new `capabilities` field on `ModelInfo` is optional and defaults to `None`, so existing code that reads model info will continue to work without changes.
