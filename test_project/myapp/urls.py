from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *
from .exported import *

# создание объекта-роутера
router_api = DefaultRouter()

# регистрация марщрутов для каждого представления в views.py
router_api.register(r'country', CountryViewSet)
router_api.register(r'manufacturer', ManufacturerViewSet)
router_api.register(r'car', CarViewSet)
router_api.register(r'comment', CommentViewSet)


'''
Обычно вам не нужно указывать аргумент basename, но если у вас есть набор представлений, в котором вы определили 
пользовательский метод get_queryset, то набор представлений может не иметь атрибута .queryset. Если вы попытаетесь 
зарегистрировать этот набор представлений, вы увидите ошибку
'''
router_api_v3 = DefaultRouter()
router_api_v3.register(r'country', CountryViewSetV3, basename='Country')
router_api_v3.register(r'manufacturer', ManufacturerViewSetV3, basename='Manufacturer')
router_api_v3.register(r'car', CarViewSetV3, basename='Car')


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
    path('v1/', include(router_api.urls)),
    path('v2/', include(router_api_v3.urls)),
    path('export_to_xlsx/<str:data_model>/', export_to_xlsx, name='export_to_xlsx'),
    path('export_to_csv/<str:data_model>/', export_to_csv, name='export_to_csv'),
]