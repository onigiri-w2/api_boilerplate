import logging
import os

# CORS設定
CORS_ORIGINS = ["*"]

# SQL Alchemy DB URI
SQLALCHEMY_ENGINE_URI = os.getenv("SQLALCHEMY_ENGINE_URI", "sqlite:///./dev.db")

# 最低限のログレベル
MIN_LOG_LEVEL = logging.DEBUG
