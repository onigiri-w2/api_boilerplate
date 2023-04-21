"""
firebaseのサービスを使いたいなら、初めにこの関数を呼び出す必要がある。
今回のAPIの場合なら、app.pyの最初に呼び出せばいい。
``` app.py
from fastapi import FastAPI
from src.external.firebase.initialize import initialize as firebase_initialize

firebase_initialize()

app = FastAPI()
```

なお、firebaseでは、初期化の前提条件として環境変数「GOOGLE_APPLICATION_CREDENTIALS」に、シークレットキーのファイルのパスを設定しておく必要がある。
もちろん、そのパスには、シークレットキーのファイルが存在している必要がある。

参考：https://firebase.google.com/docs/admin/setup?hl=ja#initialize_the_sdk_in_non-google_environments
"""
import firebase_admin


def initialize() -> None:
    firebase_admin.initialize_app()
