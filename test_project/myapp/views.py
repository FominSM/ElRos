from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.authentication import TokenAuthentication


# создание класса-представления на основе .ModelViewSet, что добавляет фун-л GET, POST, PUT, DEL
class CountryViewSet(viewsets.ModelViewSet):
    # создаем коллекцию всех обьектов модели
    queryset = Country.objects.all()
    # передаем данные в сериализатор
    serializer_class = CountrySerializer
    # пользователь является аутентифицированным если имеет токен
    authentication_classes = (TokenAuthentication, )
    # разрешение на чтение всем, на действия с данными - если аутентифицирован
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, )
    

'''
При условии, что они наследуются от rest_framework.permissions.BasePermission, разрешения могут быть составлены с
использованием стандартных побитовых операторов Python. Например, IsAuthenticatedOrReadOnly может быть написано:
'''
class _ReadOnlyAndAppend(BasePermission):
    def has_permission(self, request, view):
        return request.method in ('GET', 'POST')

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly|_ReadOnlyAndAppend, )



class CountryViewSetV3(viewsets.ViewSet):
    # переопределяем метод для выбора обьекта по указанному в url id
    def retrieve(self, request, pk=None):
        # получаем всю коллекцию класса
        queryset = Country.objects.all()
        # выбираем конкретный объект по id
        country = get_object_or_404(queryset, pk=pk)
        # передаем объект сериализатору
        serializer = CountrySerializerV3(country)
        # отправляем клиенту данные в b'data'
        return Response(serializer.data)
    
class ManufacturerViewSetV3(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Manufacturer.objects.all()
        manufacturer = get_object_or_404(queryset, pk=pk)
        serializer = ManufacturerSerializerV3(manufacturer)
        return Response(serializer.data)
    
class CarViewSetV3(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Car.objects.all()
        car = get_object_or_404(queryset, pk=pk)
        serializer = CarSerializerV3(car)
        return Response(serializer.data)