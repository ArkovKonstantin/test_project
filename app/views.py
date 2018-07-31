from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.apps import apps
from rest_framework.response import Response
from rest_framework.views import APIView

from app.forms import PointCreateForm, PointTypeCreateForm
from app.models import Point, PointType
from app.serializers import PointSerializer


class PointList(APIView):
    def get(self, request):
        points = Point.objects.all()
        serializer = PointSerializer(points, many=True)
        return Response(serializer.data)

# Вывод списка моделей
class ModelView(TemplateView):
    template_name = 'models.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        models = apps.all_models['app']  # returns dict with all models you defined
        data['models'] = models
        return data


# Вывод списка объектов выбранной модели
class ObjectView(ListView):
    template_name = 'objects.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # models = apps.all_models['app']  # returns dict with all models you defined
        data['model'] = self.kwargs['model']
        return data

    def get_queryset(self):
        qs = apps.all_models['app'][self.kwargs['model']].objects.all()
        return qs


# Вывод информации о выбранном объекте
class ObjectDetailView(TemplateView):
    template_name = 'object_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        qs = apps.all_models['app'][self.kwargs['model']].objects.filter(pk=self.kwargs['pk'])
        data['qs'] = qs.values()[0]
        data['model'] = self.kwargs['model']
        return data


# Создание нового объекта класса Point
class CreatePoint(CreateView):
    template_name = 'form.html'
    model = Point
    form_class = PointCreateForm


# Создание нового объекта класса PointType
class CreatePointType(CreateView):
    template_name = 'form.html'
    model = PointType
    form_class = PointTypeCreateForm


class UpdatePoint(UpdateView):
    template_name = 'form.html'
    form_class = PointCreateForm

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Point, id=id)


class UpdatePointType(UpdateView):
    template_name = 'form.html'
    form_class = PointTypeCreateForm

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(PointType, id=id)


class PointDelete(DeleteView):
    template_name = 'delete.html'
    model = Point
    success_url = reverse_lazy('myapp:object_url', kwargs={"model": 'point'})


class PointTypeDelete(DeleteView):
    template_name = 'delete.html'
    model = PointType
    success_url = reverse_lazy('myapp:object_url', kwargs={"model": 'pointtype'})
