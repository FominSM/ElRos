from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comment



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
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


# - При запросе страны на стороне сериализатора добавить производителей в выдачу, которые ссылаются на нее.
class CountrySerializerV3(serializers.BaseSerializer):
    def to_representation(self, instance):
        list_manufacturers = Manufacturer.objects.filter(country=instance.pk)
        country_producers = [manufacturer.name for manufacturer in list_manufacturers]

        return {
            'country': instance.name,
            'manufacturers': country_producers
        }


# - При запросе производителя добавлять страну, автомобили и количество комментариев к ним к выдаче.
class ManufacturerSerializerV3(serializers.BaseSerializer):
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


# - При запросе автомобиля добавить производителя и комментарии с их количеством в выдачу.
class CarSerializerV3(serializers.BaseSerializer):
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