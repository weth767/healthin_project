#!make

docker_up:
	@echo "executing docker compose up detached"
	@cd docker && docker-compose up -d

docker_stop:
	@echo "executing docker stop"
	@cd docker && docker stop $(docker ps -aq)

docker_rm:
	@echo "executing docker rm"
	@cd docker && docker rm $(docker ps -aq)

docker_stop_rm: docker_stop docker_rm

migrate_run:
	@echo "executing migrate"
	@npx prisma migrate dev

nest_start_dev:
	@echo "executing nest start dev"
	@npm run start:dev

start: docker_up nest_start_dev