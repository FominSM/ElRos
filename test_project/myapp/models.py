from django.db import models

from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def _for_export(self):
        return f'{self.name} | {self.country}'

class Car(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.name
    
    def _for_export(self):
        return f'{self.name} | {self.manufacturer._for_export()} | {self.start_year} | {self.end_year}'

class Comment(models.Model):
    email = models.EmailField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.car.name} - {self.text[:20]}..."
    
    def _for_export(self):
        return f"{self.email} | {self.created_at} | {self.car.name} | {self.text}"