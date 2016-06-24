# coding=utf-8
from django.conf.urls import url
from .views import  get_model_data_ajax


urlpatterns = [
   url(r'^get_data/$', get_model_data_ajax, name="getdata"),
]

