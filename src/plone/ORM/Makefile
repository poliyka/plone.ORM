m ?= $(m)

db_upgrade:
	alembic upgrade head

db_migration:
	alembic revision --autogenerate -m "$(m)"