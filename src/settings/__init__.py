"""
本プロジェクトでの設定値を定義する
設定値には以下2つのものがある
    1. 環境関係なく共通の設定値
    2. 環境ごとに異なる設定値
1. はこのファイルに定義する
2. は環境ごとのファイル（settings/dev.py, settings/prod.py）に定義する
どちらのファイルを読み込むかは環境変数 ENV で指定する

他ファイルから、このファイルで定義した設定値を読み込むには以下のようにする
Usage:
    # sample.py
    from src.settings import ROOT_PATH, ERROR_CODE_MAP_PATH, CORS_ORIGINS
"""

import os
from importlib.machinery import SourceFileLoader
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

env = os.environ.get("ENV", "dev")

# settings/prod.py または settings/dev.py を読み込む
env_settings = SourceFileLoader("env_settings", f"src/settings/{env}.py").load_module()

# ---------------- #
# 環境依存の設定値
# ---------------- #
CORS_ORIGINS = env_settings.CORS_ORIGINS
SQLALCHEMY_ENGINE_URI = env_settings.SQLALCHEMY_ENGINE_URI
MIN_LOG_LEVEL = env_settings.MIN_LOG_LEVEL

# ---------------- #
# 共通の設定値
# ---------------- #
# ルートディレクトリ
ROOT_PATH = Path(__file__).parent.parent.parent


# SQL Alchemy
Engine = create_engine(SQLALCHEMY_ENGINE_URI)
Session = scoped_session(sessionmaker(bind=Engine))
Base = declarative_base()

# テーブル名一覧
TABLE_NAME_USER = "user"
