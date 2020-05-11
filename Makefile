CONTAINER_RULES = $(addprefix cont_,$(shell find containers -name Dockerfile | awk -F/ '{print $$2}'))

doc:
	@echo 'Usage'
	@echo '-----'
	@cat Makefile | sed -En 's|^#[[:space:]]*\[(.*)\]|	make \1:|p'

# [up] Build and up containers
up: build
	docker-compose up -d

# [build] Build Dockerfiles from the containers/ directory
build: $(CONTAINER_RULES)

cont_%: NAME=$*
cont_%:
	@echo "=== Building docker image le.taxi/$(NAME) ==="
	docker build -t le.taxi/$(NAME) containers/$(NAME)

# [logs] View containers logs
logs:
	docker-compose logs -f --tail 0

# [test] Launch api test
test: build
	docker-compose -f docker-compose.yml -f docker-compose-test.yml run api nosetests -x tests
