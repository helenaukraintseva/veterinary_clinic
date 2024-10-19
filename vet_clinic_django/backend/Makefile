# Запуск контейнера с базой данных
run-db:
	docker compose up -d app-db

# Остановка контейнера с базой данных
stop-db:
	docker compose stop app-db

# Удаление контейнера с базой данных
remove-db:
	docker compose down app-db

# Создание миграций
create-migration:
	python app/manage.py makemigrations

# Применение миграций
migrate:
	python app/manage.py migrate

# Создание администратора
create-admin:
	python app/manage.py createsuperuser
