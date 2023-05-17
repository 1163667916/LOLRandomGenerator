from django.contrib import admin
from django.urls import path

from . import views

app_name = 'lol'
urlpatterns = [
    path('request_legend_list', views.request_legend_list)
]