from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *
from .exported import export_to_xlsx, export_to_csv, tests_f

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
    path('', index, name='index'),
    path('', include(router_api.urls)),
    path('export_to_xlsx/<str:data_model>/', export_to_xlsx, name='export_to_xlsx'),
    path('export_to_csv/<str:data_model>/', export_to_csv, name='export_to_csv'),
    path('v3/<int:pk>/', CountryViewSetV3.as_view({'get': 'retrieve'}), name='export'),
    
    # path('v3/', include(router_api_v3.urls)),
    # path('test/<int:id_n>/', tests_f, name='tests_f'),
]