## Требования
- Python 3.5 или выше;
- Django 2.2 или выше;
- PostgreSQL или MySQL на выбор.


## DRF Задача #1: Отзывы об автомобилях

### Развернуть Django проект, развернуть базу данных, настроить Django Rest Framework.


1. Создать [модели данных](https://github.com/FominSM/ElRos/blob/main/test_project/myapp/models.py):
    - Страна, с полями: «Имя»
    - Производитель, с полями: «Имя», «Страна»
    - Автомобиль, с полями: «Имя», «Производитель», «Год начала выпуска», «Год окончания выпуска»
    - Комментарий, с полями: «Email автора», «Автомобиль», «Дата создания», «Комментарий»


2. Создать Endpoint’ы (/api/…) для:
    - Добавления, изменения, удаления и просмотра(GET, POST, PUT, DELETE) записей в моделях: 
        - [«Страна»](https://github.com/FominSM/ElRos/blob/ffaca8732a6714cbbbb769fafbcf49d4d2a6fa1a/test_project/myapp/views.py#L11)  
        - [«Производитель»](https://github.com/FominSM/ElRos/blob/ffaca8732a6714cbbbb769fafbcf49d4d2a6fa1a/test_project/myapp/views.py#L22)
        - [«Автомобиль»](https://github.com/FominSM/ElRos/blob/ffaca8732a6714cbbbb769fafbcf49d4d2a6fa1a/test_project/myapp/views.py#L28) 
        - [«Комментарий»](https://github.com/FominSM/ElRos/blob/ffaca8732a6714cbbbb769fafbcf49d4d2a6fa1a/test_project/myapp/views.py#L43) 
    - Экспорта данных в формате [xlsx](https://github.com/FominSM/ElRos/blob/650a425d62637a223061a3c4d4b90262bd0d9e54/test_project/myapp/exported.py#L9) + [csv](https://github.com/FominSM/ElRos/blob/650a425d62637a223061a3c4d4b90262bd0d9e54/test_project/myapp/exported.py#L81) в зависимости от передаваемого в запросе GET параметра([маршруты для тестов](https://github.com/FominSM/ElRos/blob/2e07658532f8caffa32114e38a22b4b22249c130/test_project/myapp/urls.py#L27-L39)).

3. Настроить сериализаторы:
    - При запросе [страны](https://github.com/FominSM/ElRos/blob/650a425d62637a223061a3c4d4b90262bd0d9e54/test_project/myapp/serializers.py#L30) на стороне сериализатора добавить производителей в выдачу, которые ссылаются на нее.
    - При запросе [производителя](https://github.com/FominSM/ElRos/blob/650a425d62637a223061a3c4d4b90262bd0d9e54/test_project/myapp/serializers.py#L42) добавлять страну, автомобили и количество комментариев к ним к выдаче.
    - При запросе [автомобиля](https://github.com/FominSM/ElRos/blob/650a425d62637a223061a3c4d4b90262bd0d9e54/test_project/myapp/serializers.py#L58) добавить производителя и комментарии с их количеством в выдачу.
    - При добавлении комментария [проводить валидацию](https://github.com/FominSM/ElRos/blob/650a425d62637a223061a3c4d4b90262bd0d9e54/test_project/myapp/serializers.py#L23) входных данных.

4. Предоставить доступ к операциям: **добавления**, **редактирования**, **удаления** - *страны*, *производителя* и *автомобиля* только через передачу определенного токена. Доступ к **добавлению** и **просмотру** *комментария* оставить публичный, **редактирование** или **удаление** через токен.

> Доступ по токену реализован через библиотеку Djoser, ниже приведены команды для тестирования функционала черех Postman:

- create new user
    > http://127.0.0.1:8000/api/djoser/auth/users/ отправить POST запрос где Body - form data (username, password, email)

- register new user
    > http://127.0.0.1:8000/api/auth/token/login/ отправить POST запрос где Body - form data (username, password) -> получим в ответе токен авторизации 

- deleting a token
    > http://127.0.0.1:8000/api/auth/token/logout/ отправить POST запрос где Headers - Authorization - Token 1234213123131313


## Дополнительно, но не обязательно:
- К проекту приложить файл с дампом запросов из ПО для тестирования (прим.: Postman)

## При наличии знаний JS: 
- Создать и базово оформить веб-страницу для работы с API в корневом url. Отдавать ее используя встроенные средства Django.
- Используя Fetch/Axios написать базовый функционал для работы с API на странице.
- Динамически обновлять данные на странице при внесении изменений.

## При наличии знаний Docker:
- Контейнеризировать Базу данных и приложение Django, адаптировать проект для развертывания через Docker-Compose.

Порядок действий при наличии установленного и настроенного на ПК Docker:

1. Сменить настройки БД в файле проекта - settings.py, [эти строки](https://github.com/FominSM/ElRos/blob/2e07658532f8caffa32114e38a22b4b22249c130/test_project/test_project/settings.py#L81-L90) - закомментировать, [а эти](https://github.com/FominSM/ElRos/blob/2e07658532f8caffa32114e38a22b4b22249c130/test_project/test_project/settings.py#L93-L102) - раскомментировать
2. Файлы Docker - [Dockerfile](https://github.com/FominSM/ElRos/blob/main/test_project/Dockerfile) и .[yml](https://github.com/FominSM/ElRos/blob/main/test_project/docker-compose.yml)
3. В cmd перейти в дирректорию проекта и выполнить команду - **docker-compose up**
4. Произвести миграции, выполнив команду в терминале: **docker-compose run django python manage.py migrate**





Для запуска проекта на Django и базы данных PostgreSQL с использованием Docker Compose и заданным собственным портом для базы данных PostgreSQL, вы можете создать следующий файл docker-compose.yml в корне вашего проекта:

version: '3.8'

services:
  db:
    image: postgres:latest
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_HOST: db
      PG_PORT: ${DB_PORT}
    ports:
      - "${DB_PORT}:5432"
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - backend

  backend:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
    networks:
      - backend

networks:
  backend:
    driver: bridge

Замените DB_NAME, DB_USER, DB_PASSWORD и DB_PORT в файле docker-compose.yml на соответствующие значения из вашего файла .env.

Также убедитесь, что у вас есть файл .env в корне вашего проекта, содержащий следующие переменные:

DB_NAME=mydatabase
DB_USER=myuser
DB_PASSWORD=mypassword
DB_PORT=5432

Затем запустите Docker Compose:

docker-compose up --build

Теперь ваш проект на Django и база данных PostgreSQL запущены в Docker с помощью Docker Compose, и база данных PostgreSQL имеет заданный собственный порт.