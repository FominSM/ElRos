from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *
from .exported import export_to_xlsx

# создание объекта-роутера
router = DefaultRouter()

# регистрация марщрутов для каждого представления в views.py
router.register(r'countries', CountryViewSet)
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'cars', CarViewSet)
router.register(r'comments', CommentViewSet)


# http://127.0.0.1:8000/api/export_to_xlsx/countries/
# http://127.0.0.1:8000/api/export_to_xlsx/manufacturers/
# http://127.0.0.1:8000/api/export_to_xlsx/cars/
# http://127.0.0.1:8000/api/export_to_xlsx/comments/



urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
    path('export_to_xlsx/<str:data_model>/', export_to_xlsx, name='export_to_xlsx'),
]