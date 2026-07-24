import os

APP_PORT = int(os.getenv("APP_PORT", "8080"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")
if LOG_LEVEL not in {"debug", "info", "warning", "error"}:
    raise ValueError("invalid LOG_LEVEL")
DATABASE_URL = os.environ["DATABASE_URL"]
