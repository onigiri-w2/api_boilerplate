# ボイラープレートの初期構築（初期構築が終わったら削除してもよし）
initialize_bp:
	sh .bp/initialize_bp.sh


# fastapiの起動
run:
	sh run.sh


# fastapi local dev run
local_run:
	poetry run python3 -m uvicorn src.app:app --reload
