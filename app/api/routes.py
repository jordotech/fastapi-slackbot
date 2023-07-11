from fastapi import APIRouter, Response

from api.public.routes import router as public_routes
from api.slack.routes import router as slack_routes

api_router = APIRouter()
# api_router.include_router(classes_routes, prefix="/classes", tags=["classes"])

api_router.include_router(slack_routes, prefix="/send-message", tags=["slack"])
api_router.include_router(public_routes, prefix="/public", tags=["public"])
