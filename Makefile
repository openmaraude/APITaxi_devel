CONTAINER_RULES = $(addprefix cont_,$(shell find containers -name Dockerfile | awk -F/ '{print $$2}' | sort))

doc:
	@echo 'Usage'
	@echo '-----'
	@cat Makefile | sed -En 's|^#[[:space:]]*\[(.*)\]|	make \1:|p'

# [up] Build and up containers
up:
	docker-compose up -d

# [logs] View containers logs
logs:
	docker-compose logs -f --tail 0

update-submodules:
	git submodule update --init --recursive --remote

ifeq (shell,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "shell"
  DOCKER_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(DOCKER_ARGS):;@:)
endif

# [shell <container_name>] Run a shell in a container, eg. `make shell api`, `make shell worker`, `make shell -- --service-ports geotaxi`
shell :
	docker-compose run --rm --entrypoint bash --no-deps $(DOCKER_ARGS)
