CONTAINER_RULES = $(addprefix cont_,$(shell find containers -name Dockerfile | awk -F/ '{print $$2}' | sort))

doc:
	@echo 'Usage'
	@echo '-----'
	@cat Makefile | sed -En 's|^#[[:space:]]*\[(.*)\]|	make \1:|p'

# [up] Build and up containers
up: build
	docker-compose up -d

# [build] Build Dockerfiles from the containers/ directory
build: $(CONTAINER_RULES)
	docker-compose build

cont_%: NAME=$*
cont_%:
	@echo "=== Building docker image le.taxi/$(NAME) ==="
	docker build -t le.taxi/$(NAME) containers/$(NAME)

# [logs] View containers logs
logs:
	docker-compose logs -f --tail 0

update-submodules:
	git submodule update --init --recursive --remote
