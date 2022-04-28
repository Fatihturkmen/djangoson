start:
	cd blog_projesi ;\
	docker-compose -f local.yaml up

stop:
	cd blog_projesi ;\
	docker-compose -f local.yaml down
	