# DockerHomeWork_with_celery
 
Для запуска проекта:

Клонировать проект, перейти в папку проекта.
Проект использует подключение к mongo, поэтому для работы требуется создать .env со строкой подключения к MONGO_URL и заменить путь к env-file в docker-compose

Далее запустить в терминале следующие команды:
docker-compose build
docker-compose up

Протестировать решение можно с помощью ipynb файла в проекте. 

Добавлен файл test.py, логирование процесса, мониторинг в prometheus и mlflow

Образы в docker-hub:

https://hub.docker.com/repository/docker/1306613066/worker_image

https://hub.docker.com/repository/docker/1306613066/app_image

