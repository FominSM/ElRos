from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, ManufacturerViewSet, CarViewSet, CommentViewSet



router_api_v1 = DefaultRouter()

router_api_v1.register(r'country', CountryViewSet)
router_api_v1.register(r'manufacturer', ManufacturerViewSet)
router_api_v1.register(r'car', CarViewSet)
router_api_v1.register(r'comment', CommentViewSet)

urlpatterns = [
    path('v1/', include(router_api_v1.urls)),
    path('djoser/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]