"""
excludeオプションで指定したテーブルは削除されない
excludeオプションを指定しない場合は、全てのテーブルが削除される

Usage:
    python script/drop_db_tables.py --exclude user word

"""
import argparse

import sqlalchemy

# TODO
# 削除したいテーブルのormモデルをimportする必要あり
# importしないと、そのテーブルが削除されない
from src.rdb.orm.user import User  # noqa F401
from src.settings import Base, Engine


def execute() -> None:
    # コマンドライン引数のパーサーを作成する
    parser = argparse.ArgumentParser()
    parser.add_argument("--exclude", nargs="+", help="tables to exclude from deletion")
    args = parser.parse_args()

    # 削除対象のテーブルを除外する
    exclude_tables = set(args.exclude or [])
    metadata = Base.metadata
    delete_target_tables = [t for t in metadata.sorted_tables if t.name not in exclude_tables]

    for table in delete_target_tables:
        if sqlalchemy.inspect(Engine).has_table(table.name):
            print(f"drop table {table.name}")
            table.drop(Engine)


if __name__ == "__main__":
    execute()
