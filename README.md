# DockerHomeWork_with_celery
 
Для запуска проекта:

Клонировать проект, перейти в папку проекта.
Проект использует подключение к mongo, поэтому для работы требуется создать .env со строкой подключения к MONGO_URL и заменить путь к env-file в docker-compose

Далее запустить в терминале следующие команды:
docker-compose build
docker-compose up

Добавлен файл test.py, логирование процесса, мониторинг в prometheus и mlflow

