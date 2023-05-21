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

## 全体的な開発の流れ

1. コーディングの前に以下のこと決めておく
   a. どういう機能が欲しい？機能一覧を決める。
   b. それらの機能を API の定義に落とし込む。（名前、リクエスト情報、レスポンス情報、可能性のあるエラー内容（これは最悪後ででいい））
   c. モデル定義。DDD とかそういうの参考に、どういうモデルが必要なのか、それらの関係などを定義しておく。あとモデルごとの値の制約とかも。
   d. 永続化に使うシステム決める。RDB？NoSQL？DynamoDB？
2. コーディングに入る
3. まずは api のコーディングから、中身は記載せずともスキーマやら必要な api 関数を全て作り切る。
4. 次に model の実装を行なっていく。「1.」で作ったモデル通りに作っていこう。entity と valueobject の違いは意識して。
5. 次に 永続化 の実装を行なっていく。（まだ、rdb バージョンしか例示がないけど...w）
6. 最後に API 関数の実装を、機能要件を満たすように埋めていく。（API の実装から先にやった方がいいかな？こういう風に作ってっていう骨子を先に作るために）

## openapi.json が欲しいなら...

```sh
poetry run python3 script/generate_openapi.py
```
