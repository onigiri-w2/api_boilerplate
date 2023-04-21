# bp_api

python でバックエンド API を作る際のボイラープレート

# 前提

1. VSCode で開発する
2. Mac 上で開発する
3. python のフレームワークに`FastAPI`を使う
4. DB は MySQL を利用する

# Usage

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

6. VSCode の python インタープリターに`.venv`にある python バイナリを指定する。

- 注意 1：`.venv` は「5.」のプロセスを実施することで生成されます。
- 注意 2：ただ、まあ settings.json の`python.defaultInterpreterPath`に指定してるので、特段何もせずともインタープリターに自動設定されるかも。

# Features

## vscode の設定及び拡張

vscode で作る前提で開発環境を作ってる。dev-container とかも vscode の機能だし。
まあ、vscode を使わなくてもボイラープレート自体は使えるが。

- TODO: README.md の整理
- TODO: deploy 周りの整理（AWS かなぁ？）
- TODO: fastapi のテスト
- TODO: それ以外の utils 系のテスト
