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
        - [«Страна»](https://github.com/FominSM/ElRos/blob/97bdf376382f3724880fbc419be86f9240ebdb2d/test_project/myapp/views.py#L22)  
        - [«Производитель»](https://github.com/FominSM/ElRos/blob/97bdf376382f3724880fbc419be86f9240ebdb2d/test_project/myapp/views.py#L30)
        - [«Автомобиль»](https://github.com/FominSM/ElRos/blob/97bdf376382f3724880fbc419be86f9240ebdb2d/test_project/myapp/views.py#L38) 
        - [«Комментарий»](https://github.com/FominSM/ElRos/blob/97bdf376382f3724880fbc419be86f9240ebdb2d/test_project/myapp/views.py#L51) 
    - Экспорта данных в формате [xlsx + csv](https://github.com/FominSM/ElRos/blob/97bdf376382f3724880fbc419be86f9240ebdb2d/test_project/myapp/exported.py#L9) в зависимости от передаваемого в запросе GET параметра.

3. Настроить сериализаторы:
    - При запросе [страны](https://github.com/FominSM/ElRos/blob/97bdf376382f3724880fbc419be86f9240ebdb2d/test_project/myapp/serializers.py#L51) на стороне сериализатора добавить производителей в выдачу, которые ссылаются на нее.
    - При запросе [производителя](https://github.com/FominSM/ElRos/blob/97bdf376382f3724880fbc419be86f9240ebdb2d/test_project/myapp/serializers.py#L31) добавлять страну, автомобили и количество комментариев к ним к выдаче.
    - При запросе [автомобиля](https://github.com/FominSM/ElRos/blob/97bdf376382f3724880fbc419be86f9240ebdb2d/test_project/myapp/serializers.py#L12) добавить производителя и комментарии с их количеством в выдачу.
    - При добавлении комментария [проводить валидацию](https://github.com/FominSM/ElRos/blob/97bdf376382f3724880fbc419be86f9240ebdb2d/test_project/myapp/serializers.py#L6) входных данных.

4. Предоставить доступ к операциям: **добавления**, **редактирования**, **удаления** - *страны*, *производителя* и *автомобиля* только через передачу определенного токена. Доступ к **добавлению** и **просмотру** *комментария* оставить публичный, **редактирование** или **удаление** через токен.

> Доступ по токену реализован через библиотеку Djoser, ниже приведены команды для тестирования функционала черех Postman:

- create new user
    > http://127.0.0.1:8000/api/djoser/auth/users/ отправить POST запрос где Body - form data (username, password, email)

- register new user
    > http://127.0.0.1:8000/api/auth/token/login/ отправить POST запрос где Body - form data (username, password) -> получим в ответе токен авторизации 

- deleting a token
    > http://127.0.0.1:8000/api/auth/token/logout/ отправить POST запрос где Headers - Authorization - Token 123456789


## Дополнительно, но не обязательно:
- К проекту приложить файл с дампом запросов из ПО для тестирования (прим.: Postman)

## При наличии знаний JS: 
- Создать и базово оформить веб-страницу для работы с API в корневом url. Отдавать ее используя встроенные средства Django.
- Используя Fetch/Axios написать базовый функционал для работы с API на странице.
- Динамически обновлять данные на странице при внесении изменений.

## При наличии знаний Docker:
- Контейнеризировать Базу данных и приложение Django, адаптировать проект для развертывания через Docker-Compose.

Порядок действий при наличии установленного и настроенного на ПК Docker:

1. Файлы Docker - [Dockerfile](https://github.com/FominSM/ElRos/blob/main/test_project/Dockerfile) и .[yml](https://github.com/FominSM/ElRos/blob/main/test_project/docker-compose.yml)
2. В cmd перейти в дирректорию проекта и выполнить команду - **docker-compose up**
3. Произвести миграции, выполнив команду в терминале: **docker-compose run django python manage.py migrate**




### Комментарии к проекту

### API-запросы для экспорта данных
- http://127.0.0.1:8000/api/v1/country/?get=csv
- http://127.0.0.1:8000/api/v1/country/?get=xlsx
