"""
定義されてるormモデルを元に、テーブルを作成する
"""

# TODO
# 作成したいテーブルのormモデルをimportする必要あり
# importしないと、metadata.create_allでテーブルが作成されない
from src.rdb.orm.user import User  # noqa F401
from src.settings import Base, Engine


def execute() -> None:
    Base.metadata.create_all(bind=Engine)


if __name__ == "__main__":
    execute()
