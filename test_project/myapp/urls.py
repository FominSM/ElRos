from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *
from .exported import *

# создание объекта-роутера
router_api = DefaultRouter()

# регистрация марщрутов для каждого представления в views.py
router_api.register(r'countries', CountryViewSet)
router_api.register(r'manufacturers', ManufacturerViewSet)
router_api.register(r'cars', CarViewSet)
router_api.register(r'comments', CommentViewSet)

# for def export_to_xlsx()
# http://127.0.0.1:8000/api/export_to_xlsx/country/
# http://127.0.0.1:8000/api/export_to_xlsx/manufacturer/
# http://127.0.0.1:8000/api/export_to_xlsx/car/
# http://127.0.0.1:8000/api/export_to_xlsx/comment/

# for def export_to_csv()
# http://127.0.0.1:8000/api/export_to_csv/country/
# http://127.0.0.1:8000/api/export_to_csv/manufacturer/
# http://127.0.0.1:8000/api/export_to_csv/car/
# http://127.0.0.1:8000/api/export_to_csv/comment/


# router_api_v3 = DefaultRouter()

# router_api_v3.register(r'countries', CountryViewSetV3)


urlpatterns = [
    path('', include(router_api.urls)),

    path('export_to_xlsx/<str:data_model>/', export_to_xlsx, name='export_to_xlsx'),
    path('export_to_csv/<str:data_model>/', export_to_csv, name='export_to_csv'),

    path('v3/country/<int:pk>/', CountryViewSetV3.as_view({'get': 'retrieve'}), name='get_country_with_parameters'),
    path('v3/manufacturer/<int:pk>/', ManufacturerViewSetV3.as_view({'get': 'retrieve'}), name='get_manufacturer_with_parameters'),
    path('v3/car/<int:pk>/', CarViewSetV3.as_view({'get': 'retrieve'}), name='get_car_with_parameters'),

    # path('v3/', include(router_api_v3.urls)),
]