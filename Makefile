test:
	rm -f test.db
	pytest --cov
type:
	mypy . --enable-incomplete-feature=Unpack
run:
	uvicorn server.main:app
dev:
	uvicorn server.main:app --reload
lint:
	ruff check .
lint-fix:
	ruff check . --fix
init:
	pre-commit install
