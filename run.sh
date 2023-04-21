poetry run python3 script/create_db_tables.py
poetry run python3 -m uvicorn src.app:app --host 0.0.0.0
