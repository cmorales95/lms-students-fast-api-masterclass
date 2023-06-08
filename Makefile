env-create:
	@python -m venv venv

env-activate:
	@source venv/bin/activate

init:
	@poetry init

run-uvicorn:
	@uvicorn main:app --reload