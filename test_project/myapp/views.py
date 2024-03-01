from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Country, Manufacturer, Car, Comment
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.authentication import TokenAuthentication
from .exported import ExportDataToCsvOrXlsx
from django.forms.models import model_to_dict



class BaseCustomModelViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        attr_to_export = ('id')

        if 'get' in request.GET:
            return ExportDataToCsvOrXlsx(request, self.queryset, self.attr_to_export, request.GET['get']).get_file()

        return super(BaseCustomModelViewSet, self).list(request, *args, **kwargs) 
  

class CountryViewSet(BaseCustomModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    attr_to_export = ('id', 'name')
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class ManufacturerViewSet(BaseCustomModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    attr_to_export = ('id', 'name', 'country')
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    

class CarViewSet(BaseCustomModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    attr_to_export = ('id', 'name', 'manufacturer', 'start_year', 'end_year')
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticatedOrReadOnly, )
   

class _ReadOnlyAndAppend(BasePermission):
    def has_permission(self, request, view):
        return request.method in ('GET', 'POST')


class CommentViewSet(BaseCustomModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    attr_to_export = ('id', 'created_at', 'email', 'car', 'text')
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticatedOrReadOnly|_ReadOnlyAndAppend, )







# class CountryViewSetV3(viewsets.ViewSet):
#     # переопределяем метод для выбора обьекта по указанному в url id
#     def retrieve(self, request, pk=None):
#         # получаем всю коллекцию класса
#         queryset = Country.objects.all()
#         # выбираем конкретный объект по id
#         country = get_object_or_404(queryset, pk=pk)
#         # передаем объект сериализатору
#         serializer = CountrySerializerV3(country)
#         # отправляем клиенту данные в b'data'
#         return Response(serializer.data)
    
# class ManufacturerViewSetV3(viewsets.ViewSet):
#     def retrieve(self, request, pk=None):
#         queryset = Manufacturer.objects.all()
#         manufacturer = get_object_or_404(queryset, pk=pk)
#         serializer = ManufacturerSerializerV3(manufacturer)
#         return Response(serializer.data)
    
# class CarViewSetV3(viewsets.ViewSet):
#     def retrieve(self, request, pk=None):
#         queryset = Car.objects.all()
#         car = get_object_or_404(queryset, pk=pk)
#         serializer = CarSerializerV3(car)
#         return Response(serializer.data)