# poetryでpython環境を作成する
poetry config virtualenvs.create true
poetry install

# 配布用ディレクトリを作成する（主にopenapi.jsonを格納する）
mkdir dist

