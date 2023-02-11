test:
	python hack/test.py
run:
	uvicorn server.main:app
dev:
	uvicorn server.main:app --reload
lint:
	ruff check server
