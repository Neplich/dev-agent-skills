# FastAPI 0.135.0 Release Notes

**Released:** March 1, 2026

---

## What's New

### Server-Sent Events (SSE) Support

FastAPI 0.135.0 introduces built-in support for **Server-Sent Events (SSE)**, allowing you to push real-time updates from your server to connected clients over a persistent HTTP connection.

SSE is ideal for use cases such as:

- Live notifications and activity feeds
- Real-time dashboards and progress indicators
- Streaming AI/LLM responses to a browser
- Any scenario where the server needs to push data to clients without requiring WebSockets

#### How it works

With SSE support, you can now return a stream of events from a route handler using a simple, idiomatic FastAPI pattern. The server keeps the connection open and sends data as it becomes available, while the client receives updates without polling.

#### Example

```python
from fastapi import FastAPI
from fastapi.responses import EventSourceResponse

app = FastAPI()

async def event_generator():
    for i in range(10):
        yield {"data": f"Update {i}"}

@app.get("/events")
async def stream_events():
    return EventSourceResponse(event_generator())
```

#### Documentation

Full usage guide and examples are available in the new tutorial:
[Server-Sent Events (SSE)](https://fastapi.tiangolo.com/tutorial/server-sent-events/)

---

## Upgrading

This release contains no breaking changes. Update via pip:

```bash
pip install --upgrade fastapi
```

---

## Full Changelog

- PR [#15030](https://github.com/fastapi/fastapi/pull/15030) — Add support for Server Sent Events by [@tiangolo](https://github.com/tiangolo)

---

## Previous Release

Looking for what changed in 0.134.0? See the [0.134.0 release notes](https://github.com/fastapi/fastapi/releases/tag/0.134.0), which introduced streaming JSON Lines and binary data with `yield`.
