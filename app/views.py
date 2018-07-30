from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from django.apps import apps

from app.models import Point


class ModelView(TemplateView):
    template_name = 'models.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        models = apps.all_models['app']  # returns dict with all models you defined
        data['models'] = models
        return data


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


class ObjectDetailView(TemplateView):

    template_name = 'object_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        qs = apps.all_models['app'][self.kwargs['model']].objects.filter(pk=self.kwargs['pk'])
        print('qs', qs.values()[0])
        data['qs'] = qs.values()[0]
        return data



