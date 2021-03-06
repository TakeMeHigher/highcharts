"""highcharts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from charts import views as cview
from stock import views as sview


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^c1/', cview.c1),
    url(r'^c2/', cview.c2),
    url(r'^c3/', cview.c3),
    url(r'^s1/', sview.s1),
]
