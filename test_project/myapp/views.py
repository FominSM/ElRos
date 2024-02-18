from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Country, Manufacturer, Car, Comment
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer

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
    queryset = Comment.objects
    serializer_class = CommentSerializer

