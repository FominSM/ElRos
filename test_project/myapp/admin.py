from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Comment)

