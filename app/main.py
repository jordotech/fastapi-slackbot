import logging
import os
from logging.config import dictConfig

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from api.routes import api_router
from config import settings
from local_logger import log_config

# Optionally you can use a prefix

logger = logging.getLogger("app")
dictConfig(log_config)

app_version = "v1.0.0"
app = FastAPI(
    title="FastAPI Slackbot API",
    debug=settings.DEBUG,
    version=app_version,
)

app.include_router(api_router)


app.add_middleware(SessionMiddleware, secret_key=settings.SESSION_SECRET_KEY)

app = ProxyHeadersMiddleware(app, trusted_hosts="*")
