from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^car_form/(?P<city_id>[0-9]+)$', views.newcar)
]
