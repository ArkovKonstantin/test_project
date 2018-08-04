from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from app.views import *


urlpatterns = [
    url(r'get$', ModelView.as_view(), name='model_get'),
    url(r'get/(?P<model>\w+)/$', ObjectView.as_view(), name='object_url'),
    url(r'get/(?P<model>\w+)/(?P<pk>[0-9]+)/$', ObjectDetailView.as_view(), name='detail_url'),
    url(r'create_point/$', CreatePoint.as_view(), name="create_point"),
    url(r'create_pointtype/$', CreatePointType.as_view(), name="create_pointtype"),
    url(r'update_point/(?P<id>[0-9]+)/$', UpdatePoint.as_view(), name='update_point'),
    url(r'update_pointtype/(?P<id>[0-9]+)/$', UpdatePointType.as_view(), name='update_pointtype'),
    url(r'^delete_point/(?P<pk>\d+)/$', PointDelete.as_view(), name="delete_point"),
    url(r'^delete_pointtype/(?P<pk>\d+)/$', PointTypeDelete.as_view(), name="delete_pointtype"),
    # url(r'^i18n/', include('django.conf.urls.i18n'), name='set_language'),
    url(r'^points/', PointList.as_view()),

]
# urlpatterns = format_suffix_patterns(urlpatterns)

