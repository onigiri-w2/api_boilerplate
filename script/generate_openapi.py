"""
openapi.jsonを生成するスクリプト
"""
import json
from pathlib import Path

from src.app import app
from src.settings import ROOT_PATH

OPEN_API_PATH = Path.joinpath(ROOT_PATH, ".dist", "openapi.json")


def execute() -> None:
    openapi_data = app.openapi()
    with open(OPEN_API_PATH, "w") as f:
        json.dump(openapi_data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    execute()
