from django.contrib import admin
from django.urls import path

from . import views

app_name = 'index'
urlpatterns = [
    path('get_site_link', views.get_site_link, name='get_site_link'),
    path('post_stie', views.post_site, name="post_site")
]
