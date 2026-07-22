import os

APP_PORT = int(os.getenv("APP_PORT", "8080"))
DATABASE_URL = os.environ["DATABASE_URL"]
