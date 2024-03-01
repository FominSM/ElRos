from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from .views import *
from .exported import *


router_api_v1 = DefaultRouter()

router_api_v1.register(r'country', CountryViewSet)
router_api_v1.register(r'manufacturer', ManufacturerViewSet)
router_api_v1.register(r'car', CarViewSet)
router_api_v1.register(r'comment', CommentViewSet)


'''
Обычно вам не нужно указывать аргумент basename, но если у вас есть набор представлений, в котором вы определили 
пользовательский метод get_queryset, то набор представлений может не иметь атрибута .queryset. Если вы попытаетесь 
зарегистрировать этот набор представлений, вы увидите ошибку
'''
# router_api_v2 = DefaultRouter()
# router_api_v2.register(r'country', CountryViewSetV3, basename='Country')
# router_api_v2.register(r'manufacturer', ManufacturerViewSetV3, basename='Manufacturer')
# router_api_v2.register(r'car', CarViewSetV3, basename='Car')




urlpatterns = [
    path('v1/', include(router_api_v1.urls)),
    # path('v2/', include(router_api_v2.urls)),


    # Список актуальных пользователей доступен только через передачу токена
    path('djoser/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]