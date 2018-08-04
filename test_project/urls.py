"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

import app
from app.views import *



# i18n_urls = (
#     url(r'^i18n/', include('django.conf.urls.i18n'), name='set_language'),
# )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('app.urls', namespace='myapp')),
]

# urlpatterns.extend(i18n_patterns(*i18n_urls, prefix_default_language=False))