# Release Notes — 0.135.0 (2026-03-01)

> FastAPI now has native Server-Sent Events support, making real-time push from server to client as straightforward as writing an async generator.

## ✨ What's New

### Server-Sent Events (SSE)

You can now stream real-time events from your FastAPI endpoints to browser clients using the new SSE support — no third-party library required. Define an async generator that yields `ServerSentEvent` objects and return it directly from your route; FastAPI handles the `text/event-stream` response, keep-alive, and proper connection teardown automatically.

See the new docs: [Server-Sent Events (SSE)](https://fastapi.tiangolo.com/tutorial/server-sent-events/)

```python
from fastapi import FastAPI
from fastapi.responses import EventSourceResponse
from sse_starlette import ServerSentEvent

app = FastAPI()

@app.get("/events")
async def events():
    async def generate():
        for i in range(10):
            yield ServerSentEvent(data=f"message {i}")
    return EventSourceResponse(generate())
```

## 🐛 Bug Fixes

- Fixed an edge case where yielding from inside a `TaskGroup` could cause the request async exit stack to hang. FastAPI now correctly uses `TaskGroup` only as an async context manager rather than with `yield`, in line with [PEP 789](https://peps.python.org/pep-0789/). (PR [#15038](https://github.com/fastapi/fastapi/pull/15038))

## ⬆️ Upgrading

```bash
pip install fastapi==0.135.0
```

No breaking changes in this release. Existing applications upgrade without modification.
