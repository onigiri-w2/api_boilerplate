import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.utils.exception.handler import add_exception_handlers
from src.api.utils.exception.middleware import CustomServerErrorHandler
from src.api.utils.logging.route_class import LoggingRoute
from src.api.v1.route import router as v1_router
from src.settings import CORS_ORIGINS, MIN_LOG_LEVEL

logger = logging.getLogger("src")
logger.setLevel(MIN_LOG_LEVEL)
logger.addHandler(logging.StreamHandler())


app = FastAPI(debug=True)
add_exception_handlers(app)
app.router.route_class = LoggingRoute

app.include_router(v1_router, prefix="/api/v1")

app.add_middleware(CustomServerErrorHandler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
