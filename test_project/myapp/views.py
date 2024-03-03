from rest_framework import viewsets
from .models import Country, Manufacturer, Car, Comment
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.authentication import TokenAuthentication
from .exported import ExportDataToCsvOrXlsx



class BaseCustomModelViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        attr_to_export = ('id')

        if 'get' in request.GET:
            file_export = ExportDataToCsvOrXlsx(request, self.queryset, self.attr_to_export, request.GET['get'])

            return file_export.get_file()

        return super(BaseCustomModelViewSet, self).list(request, *args, **kwargs) 
  

class CountryViewSet(BaseCustomModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    attr_to_export = ('id', 'name')
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ManufacturerViewSet(BaseCustomModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    attr_to_export = ('id', 'name', 'country')
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, )
    

class CarViewSet(BaseCustomModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    attr_to_export = ('id', 'name', 'manufacturer', 'start_year', 'end_year')
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, )
   

class _ReadOnlyAndAppend(BasePermission):
    def has_permission(self, request, view):
        return request.method in ('GET', 'POST')


class CommentViewSet(BaseCustomModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    attr_to_export = ('id', 'created_at', 'email', 'car', 'text')
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly|_ReadOnlyAndAppend, )
