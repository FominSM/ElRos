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



# - При запросе страны на стороне сериализатора добавить производителей в выдачу, которые ссылаются на нее.
# - При запросе производителя добавлять страну, автомобили и количество комментариев к ним к выдаче.
# - При запросе автомобиля добавить производителя и комментарии с их количеством в выдачу.
# - При добавлении комментария проводить валидацию входных данных.



class CountrySerializerV3(serializers.BaseSerializer):
    def to_representation(self, instance):
        list_manuf = Manufacturer.objects.filter(country=instance.pk)
        res = [val.name for val in list_manuf]

        return {
            'country': instance.name,
            'manufacturers': res
        }

class ManufacturerSerializerV3(serializers.BaseSerializer):
    def to_representation(self, instance):
        list_manuf = Manufacturer.objects.filter(country=instance.pk)
        res = [val.name for val in list_manuf]

        return {
            'manufacturer': instance.name,
            'manufacturer': res,
            'cars': asdadd, 
            'comments': asdasd
        }


# def tests_f(request, id_n):
#     country_name = Country.objects.get(pk=id_n)
#     list_manuf = Manufacturer.objects.filter(country=id_n)
#     print(country_name, [val.name for val in list_manuf], sep='\n')
#     return HttpResponse(f'{country_name} - {[value.name for value in list_manuf]}')




