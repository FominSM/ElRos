from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *
from .exported import *

# создание объекта-роутера
router_api_v1 = DefaultRouter()

# регистрация марщрутов для каждого представления в views.py
router_api_v1.register(r'country', CountryViewSet)
router_api_v1.register(r'manufacturer', ManufacturerViewSet)
router_api_v1.register(r'car', CarViewSet)
router_api_v1.register(r'comment', CommentViewSet)


'''
Обычно вам не нужно указывать аргумент basename, но если у вас есть набор представлений, в котором вы определили 
пользовательский метод get_queryset, то набор представлений может не иметь атрибута .queryset. Если вы попытаетесь 
зарегистрировать этот набор представлений, вы увидите ошибку
'''
router_api_v2 = DefaultRouter()
router_api_v2.register(r'country', CountryViewSetV3, basename='Country')
router_api_v2.register(r'manufacturer', ManufacturerViewSetV3, basename='Manufacturer')
router_api_v2.register(r'car', CarViewSetV3, basename='Car')


'''
url example for def export_to_xlsx()
http://127.0.0.1:8000/api/export_to_xlsx/country/
http://127.0.0.1:8000/api/export_to_xlsx/manufacturer/
http://127.0.0.1:8000/api/export_to_xlsx/car/
http://127.0.0.1:8000/api/export_to_xlsx/comment/

url example for def export_to_csv()
http://127.0.0.1:8000/api/export_to_csv/country/
http://127.0.0.1:8000/api/export_to_csv/manufacturer/
http://127.0.0.1:8000/api/export_to_csv/car/
http://127.0.0.1:8000/api/export_to_csv/comment/
'''

urlpatterns = [
    path('v1/', include(router_api_v1.urls)),
    path('v2/', include(router_api_v2.urls)),
    path('export_to_xlsx/<str:data_model>/', export_to_xlsx, name='export_to_xlsx'),
    path('export_to_csv/<str:data_model>/', export_to_csv, name='export_to_csv'),

    # Список актуальных пользователей доступен только через передачу токена
    path('djoser/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]


# create new user
# http://127.0.0.1:8000/api/djoser/auth/users/ отправить POST запрос где Body - form data (username, password, email)

# register new user
# http://127.0.0.1:8000/api/auth/token/login/ отправить POST запрос где Body - form data (username, password) -> получим в ответе токен авторизации 

# удаление токена пользователя-выход
# http://127.0.0.1:8000/api/auth/token/logout/ отправить POST запрос где Headers - Authorization - Token 1234213123131313