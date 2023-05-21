# ボイラープレートの初期構築（初期構築が終わったら削除してもよし）
initialize_bp:
	sh .bp/initialize_bp.sh


# fastapiの起動
## docker環境で起動する時
f_pr:
	sh run.sh

## local環境で起動する時
## devdocker内で起動する時は、FASTAPI_HOST=0.0.0.0と指定するといい。
## example) make f_lr FASTAPI_HOST=0.0.0.0
FASTAPI_HOST = localhost
f_lr:
	poetry run python3 script/create_rdb_tables.py && poetry run python3 -m uvicorn src.app:app --host ${FASTAPI_HOST} --reload


# dockerの操作
## 本番
dp_cr:
	docker-compose -f .docker/docker-compose.prod.yml up -d --build
dp_dr:
	docker-compose -f .docker/docker-compose.prod.yml down --rmi all

## 開発
dd_cr:
	docker-compose -f .docker/docker-compose.dev.yml up -d --build
dd_dr:
	docker-compose -f .docker/docker-compose.dev.yml down --rmi all


## openapiの生成
openapi:
	poetry run python3 script/generate_openapi.py
