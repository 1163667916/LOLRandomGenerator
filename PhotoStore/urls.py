from django.urls import path

from . import views

app_name = 'PhotoStore'
urlpatterns = [
    path('', views.index),
]
