from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .models import Country, Manufacturer, Car, Comment
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer, CountrySerializerV3, ManufacturerSerializerV3

def index(request):
    return HttpResponse("Hello, world!")

# создание класса-представления на основе .ModelViewSet, что добавляет фун-л GET, POST, PUT, DEL
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



# - При запросе страны на стороне сериализатора добавить производителей в выдачу, которые ссылаются на нее.
# - При запросе производителя добавлять страну, автомобили и количество комментариев к ним к выдаче.
# - При запросе автомобиля добавить производителя и комментарии с их количеством в выдачу.
# - При добавлении комментария проводить валидацию входных данных.


class CountryViewSetV3(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Country.objects.all()
        country = get_object_or_404(queryset, pk=pk)
        serializer = CountrySerializerV3(country)
        return Response(serializer.data)
    
class ManufacturerViewSetV3(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Country.objects.all()
        manufacturer = get_object_or_404(queryset, pk=pk)
        serializer = ManufacturerSerializerV3(manufacturer)
        return Response(serializer.data)