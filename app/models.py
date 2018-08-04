from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
from django.urls import reverse


class PointType(models.Model):
    name = models.CharField(max_length=20, verbose_name=_(u'Имя типа точки'))
    description = models.CharField(max_length=20, verbose_name=_(u'Описание'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myapp:detail_url', kwargs={'model': 'pointtype', 'pk': self.id})


class Point(models.Model):
    name = models.CharField(max_length=20, verbose_name=_(u'Имя точки'))
    code = models.CharField(max_length=20, verbose_name=_(u'Код точки'))
    address = models.CharField(max_length=20, verbose_name=_(u'Адрес точки'))
    type = models.ForeignKey(PointType)
    latitude = models.DecimalField(max_digits=19, decimal_places=10, verbose_name=_(u'Широта'))
    longitude = models.DecimalField(max_digits=19, decimal_places=10, verbose_name=_(u'Долгота'))

    def __str__(self):
        return self.name

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('myapp:detail_url', kwargs={'model': 'point', 'pk': self.id})
