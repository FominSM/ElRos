from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

# создание объекта-роутера
router = DefaultRouter()

# регистрация марщрутов для каждого представления в views.py
router.register(r'countries', CountryViewSet)
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'cars', CarViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
]