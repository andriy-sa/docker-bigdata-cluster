help:
	@echo "usage: make COMMAND"
	@echo ""
	@echo "Commands:"
	@echo "  migrate          Create and migrate db schema"


submit:
	docker-compose run python-services export ENABLE_INIT_DAEMON=false
	docker-compose run python-services sh submit.sh