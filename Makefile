CONTAINERS = $(shell ls containers)

doc:
	@echo 'Usage'
	@echo '-----'
	@cat Makefile | sed -En 's|^#[[:space:]]*\[(.*)\]|	make \1:|p'

# [up] Build and up containers
up: build
	docker-compose up -d

# [build] Build Dockerfiles from the containers/ directory
build:
	@for name in ${CONTAINERS}; do \
		test -f containers/$$name/Dockerfile || continue; \
		echo "=== Building docker image le.taxi/$$name ==="; \
		docker build -t le.taxi/$$name containers/$$name; \
	done

# [logs] View containers logs
logs:
	docker-compose logs -f --tail 0
