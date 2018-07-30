from django.db import models


# Create your models here.
class PointType(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя типа точки')
    description = models.CharField(max_length=20, verbose_name='Описание')

    def __str__(self):
        return self.name


class Point(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя точки')
    code = models.CharField(max_length=20, verbose_name='Код точки')
    address = models.CharField(max_length=20, verbose_name='Адрес точки')
    type = models.ForeignKey(PointType)
    latitude = models.DecimalField(max_digits=19, decimal_places=10, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=19, decimal_places=10, verbose_name='Долгота')

    def __str__(self):
        return self.name

    objects = models.Manager()
