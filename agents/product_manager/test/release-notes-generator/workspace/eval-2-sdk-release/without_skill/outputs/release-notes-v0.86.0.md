# Release Notes — anthropic-sdk-python v0.86.0

**Released:** March 18, 2026
**Full changelog:** [v0.85.0...v0.86.0](https://github.com/anthropics/anthropic-sdk-python/compare/v0.85.0...v0.86.0)

---

## What's New

### Filesystem-backed memory tool (beta)

The SDK now ships a built-in, filesystem-backed implementation of the memory tool (`memory_tool_20250818`). Previously, developers had to subclass `BetaAbstractMemoryTool` and implement every file operation themselves. The new concrete classes handle all I/O against a local directory, letting you drop memory support into an agent with minimal boilerplate.

**New public exports from `anthropic.tools`:**

| Class | Use case |
|---|---|
| `BetaLocalFilesystemMemoryTool` | Sync client |
| `BetaAsyncLocalFilesystemMemoryTool` | Async client |

The abstract base classes (`BetaAbstractMemoryTool`, `BetaAsyncAbstractMemoryTool`) remain available if you need a custom storage backend.

**Before (manual implementation required):**
```python
from anthropic.lib.tools import BetaAbstractMemoryTool

class MyMemoryTool(BetaAbstractMemoryTool):
    # had to implement create, delete, insert, rename, str_replace, view...
```

**After (ready to use):**
```python
from anthropic.tools import BetaLocalFilesystemMemoryTool

memory_tool = BetaLocalFilesystemMemoryTool(base_path="/tmp/agent-memory")
```

The tool supports the full command set: `view`, `create`, `delete`, `insert`, `rename`, and `str_replace`. The async variant uses `anyio` for non-blocking file I/O so it does not block the event loop.

### Model capabilities metadata on `/v1/models`

`ModelInfo` (and `BetaModelInfo` in the beta namespace) now carries an optional `capabilities` field that describes what a given model supports at a structured level. This allows you to programmatically gate features instead of hard-coding model ID checks.

**New types exported from `anthropic.types`:**

- `ModelCapabilities` — top-level capabilities object on `ModelInfo`
- `CapabilitySupport` — `{ supported: bool }` leaf node
- `ThinkingCapability` — whether the model supports extended thinking
- `ThinkingTypes` — `adaptive` and `enabled` support flags
- `EffortCapability` — `high` and `low` reasoning-effort support flags
- `ContextManagementCapability` — context-window management feature flags

Equivalent `Beta*` variants exist in `anthropic.types.beta` for beta API users.

**Example:**
```python
model = client.models.retrieve("claude-opus-4-5")
if model.capabilities and model.capabilities.thinking.supported:
    # safe to use extended thinking with this model
    ...
```

All capability fields are optional — absent values mean the API did not return that information for the model, not that the feature is unsupported.

---

## Bug Fixes

### Async client now raises the correct exception for HTTP 413 and 529

**Affected versions:** all prior releases since v0.x (commit b87dcf12, February 2025).

The synchronous `Anthropic` client correctly mapped:
- HTTP `413` → `RequestTooLargeError`
- HTTP `529` → `OverloadedError`

The `AsyncAnthropic` client missed both cases. It was raising `APIStatusError` for 413 and `InternalServerError` for 529 (since 529 ≥ 500 fell through to the catch-all).

This is now fixed. If you have `except InternalServerError` or `except APIStatusError` handlers in async code that were silently catching overload or payload-too-large responses, review them after upgrading.

```python
# Now works correctly in async code
try:
    response = await async_client.messages.create(...)
except anthropic.OverloadedError:
    # handles HTTP 529 — was previously InternalServerError
    ...
except anthropic.RequestTooLargeError:
    # handles HTTP 413 — was previously APIStatusError
    ...
```

### Pydantic: `by_alias` no longer passed unconditionally during model serialization

`model_dump()` in the SDK's internal compatibility layer was always forwarding `by_alias` to Pydantic, even when callers did not set it. This caused unexpected behavior with some Pydantic v2 configurations. The argument is now only forwarded when explicitly provided.

This is an internal change with no expected impact on typical usage, but if you were working around aliasing behavior in serialized SDK models, verify that the default serialization now matches your expectations.

### Dependency: minimum `typing-extensions` version raised to 4.14

The lower bound on `typing-extensions` has been updated from `>=4.10` to `>=4.14`. If your project pins `typing-extensions<4.14`, you will need to loosen that constraint. Run `pip install "anthropic>=0.86.0"` and check for resolution conflicts.

---

## Upgrade Notes

1. **`typing-extensions>=4.14` is now required.** Update your dependency constraints if you pin this package.
2. **Async error handling:** If your async code catches `InternalServerError` or the base `APIStatusError` to handle overload or request-too-large scenarios, update those handlers to use `OverloadedError` and `RequestTooLargeError` respectively.
3. **Memory tool import path changed.** The concrete filesystem memory tool classes are now importable from `anthropic.tools` (not `anthropic.lib.tools`). The internal path still works but is not part of the public API.

---

## Installation

```bash
pip install "anthropic==0.86.0"
# or
pip install --upgrade anthropic
```
