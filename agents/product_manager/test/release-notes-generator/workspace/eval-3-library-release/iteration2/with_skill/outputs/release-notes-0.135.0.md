# Release Notes — 0.135.0 (2026-03-01)

> FastAPI now supports Server-Sent Events natively, letting you push real-time data to browsers with a simple `yield`-based route handler.

## ✨ What's New

### Server-Sent Events (SSE)

FastAPI 0.135.0 adds first-class support for Server-Sent Events — a browser-native protocol for one-way, real-time data streams over HTTP. You define an SSE endpoint the same way you write any async generator route: `yield` each event, and FastAPI handles the framing, headers, and connection lifecycle automatically.

**Ideal for:**
- Live dashboards that push metric updates or log lines to the browser without polling
- AI/LLM applications that stream token-by-token responses to a frontend client
- Notification systems where the server pushes status changes (job progress, alerts) to an open browser tab

```python
from fastapi import FastAPI
from fastapi.responses import EventSourceResponse

app = FastAPI()

async def number_generator():
    for i in range(10):
        yield {"data": str(i)}

@app.get("/stream")
async def stream_numbers():
    return EventSourceResponse(number_generator())
```

See docs: [Server-Sent Events (SSE)](https://fastapi.tiangolo.com/tutorial/server-sent-events/)

## Bug Fixes

- Fixed a crash when using `yield` inside a `TaskGroup` within a dependency. `TaskGroup` is now only used as an async context manager and is properly closed in the request async exit stack, following [PEP 789](https://peps.python.org/pep-0789/) semantics. ([#15038](https://github.com/fastapi/fastapi/pull/15038))

## Upgrading

```
pip install fastapi==0.135.0
```

No breaking changes. Existing applications upgrade without modification.

---

Full changelog: https://github.com/fastapi/fastapi/compare/0.134.0...0.135.0
