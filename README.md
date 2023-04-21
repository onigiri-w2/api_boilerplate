# bp_api

python でバックエンド API を作る際のボイラープレート

# 前提

1. VSCode で開発する
2. Mac 上で開発する
3. python のフレームワークに`FastAPI`を使う
4. DB は MySQL を利用する

# Install

1. リポジトリをクローンする。

```bash
git clone https://github.com/onigiri-w2/bp_api
```

2. Docker for Mac をインストールしておく。

- brew でインストールするもよし、ダウンロードしてからインストールするもよし。

3. direnv もインストールしておく。

- brew でインストールかな。
- zshrc だか bashrc だかに、何かしらコード記載しておかないといけないっぽい。詳しくは google で。

4. `poetry`をインストールする。（以下リンク参考）

- https://python-poetry.org/docs/

5. `make`で初期構築を実施する。

```
make initialize_bp
```

# Usage

## 開発は以下の流れかも

1. devcontainer 立ち上げる。
2. fastapi 起動する。
3. 必要なコードを追加したり修正したりする。
4. ある程度動作確認（テスト）する。
5. local に戻って、docker-compose.dev.yml から Docker 環境立てて、動作確認してみたりする。
6. 本番環境にこのコード持っていって、docker-compose.prod.yml から環境立てて、動作確認したりする。

これ実行したら、`dist/openapi.json`としてファイルが生成される。

## 内部（src/配下）の開発は、構造読んで雰囲気で

説明するのサボってるだけ。。。

## openapi.json が欲しいなら...

```sh
poetry run python3 script/generate_openapi.py
```
