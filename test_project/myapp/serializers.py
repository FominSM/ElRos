from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comment



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    def to_representation(self, instance):
        car_comments = Comment.objects.filter(car=instance)
        comments_dict = {}
        comments_dict['total comments'] = car_comments.count()
        for comment in car_comments:
            comments_dict[comment.email] = f'{comment.text}'

        return {
            'car': instance.name,
            'manufacturer': str(instance.manufacturer),
            'comments': comments_dict
        }


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = '__all__'

    def to_representation(self, instance):
        cars_list = Car.objects.filter(manufacturer=instance)
        car_comments = {}
        for car in cars_list:
            comment_count = Comment.objects.filter(car=car).count()
            car_comments[car.name] = f'{comment_count} comment(s)'

        return {
            'manufacturer': instance.name,
            'country': str(instance.country),
            'cars': car_comments
        }


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = ManufacturerSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'manufacturers')
