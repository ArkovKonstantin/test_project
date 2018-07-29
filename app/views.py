from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from django.apps import apps

from app.models import Point


class ModelView(TemplateView):
    template_name = 'models.html'

    # app_models = apps.get_app_config('app').get_models()
    # for model in app_models:
    #     print('model', str(model))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        models = apps.all_models['app']  # returns dict with all models you defined
        data['models'] = models
        return data



