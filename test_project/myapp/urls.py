from django.db import router
from django.urls import path
from .views import *
from .exported import export_to_xlsx



urlpatterns = [
    path('', index, name='index'),
    path('export_to_xlsx/<str:data_model>/', export_to_xlsx, name='export_all'),
    
]