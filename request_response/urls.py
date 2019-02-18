from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^weather/[a-z]+/\d{4}/$', views.weather1),
]