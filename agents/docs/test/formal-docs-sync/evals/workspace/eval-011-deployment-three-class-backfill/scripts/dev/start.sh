#!/bin/sh
exec uv run python -m app --port "${APP_PORT:-8080}"
