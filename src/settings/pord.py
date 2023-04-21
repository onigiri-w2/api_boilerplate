"""
環境変数が定義されてなかったら、プログラムが失敗するようにしたい。
なので、os.getenv() ではなく os.environ[] を使う。
"""

import logging
import os

# CORS設定
CORS_ORIGINS = [v.strip() for v in os.environ["CORS_ORIGINS"].split(",")]

# SQL Alchemy DB URI
SQLALCHEMY_ENGINE_URI = os.environ["SQLALCHEMY_ENGINE_URI"]

# 最低限のログレベル
MIN_LOG_LEVEL = logging.INFO
