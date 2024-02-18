from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comment

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        # список отображаемых полей при GET-запросе
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'